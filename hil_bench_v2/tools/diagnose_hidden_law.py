#!/usr/bin/env python3
"""Diagnose a hidden-law prediction record without modifying benchmark data.

This evaluator-side utility is intentionally standard-library only.  It reports
the exact RMSE, the nearest-neighbour baseline and acceptance bar, localizes
errors by the true regime when evaluator metadata are available, and can fit a
damped-wave counterfactual from *visible observations only*.

The private truth file is read at evaluation time and is never copied into the
public result record by this program.  Use ``--redact-private`` for a shareable
summary.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable, Sequence


def _load(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def _finite_numbers(values: Iterable[object], label: str) -> list[float]:
    result: list[float] = []
    for index, value in enumerate(values):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{label}[{index}] is not numeric")
        number = float(value)
        if not math.isfinite(number):
            raise ValueError(f"{label}[{index}] is not finite")
        result.append(number)
    return result


def _points(value: object, label: str, require_y: bool = False) -> list[dict]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} must be a non-empty JSON array")
    result = []
    keys = ("a", "b", "y") if require_y else ("a", "b")
    for index, point in enumerate(value):
        if not isinstance(point, dict):
            raise ValueError(f"{label}[{index}] must be an object")
        clean = {}
        for key in keys:
            raw = point.get(key)
            if isinstance(raw, bool) or not isinstance(raw, (int, float)):
                raise ValueError(f"{label}[{index}].{key} is not numeric")
            clean[key] = float(raw)
            if not math.isfinite(clean[key]):
                raise ValueError(f"{label}[{index}].{key} is not finite")
        result.append(clean)
    return result


def _rmse(predicted: Sequence[float], actual: Sequence[float], mask: Sequence[bool] | None = None) -> float | None:
    indices = range(len(actual)) if mask is None else (i for i, keep in enumerate(mask) if keep)
    squared = [(predicted[i] - actual[i]) ** 2 for i in indices]
    return math.sqrt(sum(squared) / len(squared)) if squared else None


def _round(value, digits: int = 12):
    return None if value is None else round(float(value), digits)


def _regime_mask(points: Sequence[dict], params: dict) -> list[bool]:
    """True means high regime for u*a + v*b > t."""
    try:
        u, v, threshold = (float(params[key]) for key in ("u", "v", "t"))
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("truth regime metadata requires numeric u, v, and t") from exc
    return [u * p["a"] + v * p["b"] > threshold for p in points]


def _candidate_mask(points: Sequence[dict], boundary: tuple[float, float, float]) -> list[bool]:
    u, v, threshold = boundary
    return [u * p["a"] + v * p["b"] > threshold for p in points]


def _parse_boundary(text: str) -> tuple[float, float, float]:
    pieces = text.split(",")
    if len(pieces) != 3:
        raise argparse.ArgumentTypeError("boundary must be U,V,T for U*a + V*b > T")
    try:
        boundary = tuple(float(piece) for piece in pieces)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("boundary entries must be numeric") from exc
    if not all(math.isfinite(x) for x in boundary):
        raise argparse.ArgumentTypeError("boundary entries must be finite")
    if boundary[0] == 0 and boundary[1] == 0:
        raise argparse.ArgumentTypeError("at least one boundary coefficient must be nonzero")
    return boundary  # type: ignore[return-value]


def _linear_fit(x: Sequence[float], y: Sequence[float]) -> tuple[float, float, float]:
    """Least-squares y=A*x+c, returning A, c, SSE."""
    n = len(x)
    mean_x, mean_y = sum(x) / n, sum(y) / n
    denominator = sum((value - mean_x) ** 2 for value in x)
    amplitude = (sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / denominator
                 if denominator > 1e-15 else 0.0)
    offset = mean_y - amplitude * mean_x
    sse = sum((amplitude * x[i] + offset - y[i]) ** 2 for i in range(n))
    return amplitude, offset, sse


def _fit_damped_wave(observations: Sequence[dict], high_mask: Sequence[bool]) -> dict:
    """Fit A*exp(-lambda*a)*sin(k*b)+c by deterministic grid refinement."""
    samples = [point for point, high in zip(observations, high_mask) if high]
    if len(samples) < 8:
        raise ValueError("damped-wave counterfactual needs at least eight high-regime observations")
    y = [point["y"] for point in samples]
    best = None
    lam_lo, lam_hi, k_lo, k_hi = 0.0, 1.5, 0.1, 3.0
    # Four refinements are fast for hundreds of samples and stable across platforms.
    for _ in range(4):
        n_lam, n_k = 51, 81
        for li in range(n_lam):
            lam = lam_lo + (lam_hi - lam_lo) * li / (n_lam - 1)
            decay = [math.exp(-lam * point["a"]) for point in samples]
            for ki in range(n_k):
                wave_number = k_lo + (k_hi - k_lo) * ki / (n_k - 1)
                x = [decay[i] * math.sin(wave_number * samples[i]["b"]) for i in range(len(samples))]
                amplitude, offset, sse = _linear_fit(x, y)
                candidate = (sse, lam, wave_number, amplitude, offset)
                if best is None or candidate < best:
                    best = candidate
        assert best is not None
        _, lam, wave_number, _, _ = best
        lam_step = (lam_hi - lam_lo) / (n_lam - 1)
        k_step = (k_hi - k_lo) / (n_k - 1)
        lam_lo, lam_hi = max(0.0, lam - lam_step), lam + lam_step
        k_lo, k_hi = max(1e-6, wave_number - k_step), wave_number + k_step
    sse, lam, wave_number, amplitude, offset = best
    return {
        "form": "A*exp(-lambda*a)*sin(k*b)+c",
        "n_visible_observations": len(samples),
        "A": _round(amplitude),
        "lambda": _round(lam),
        "k": _round(wave_number),
        "c": _round(offset),
        "visible_fit_rmse": _round(math.sqrt(sse / len(samples))),
    }


def diagnose(args: argparse.Namespace) -> dict:
    observations = _points(_load(args.observations), "observations", require_y=True)
    evaluation = _points(_load(args.predict_at), "predict_at")
    predictions_raw = _load(args.predictions)
    if isinstance(predictions_raw, dict):
        predictions_raw = predictions_raw.get("predictions")
    if not isinstance(predictions_raw, list):
        raise ValueError("predictions must be an array or an object with a predictions array")
    predicted = _finite_numbers(predictions_raw, "predictions")
    truth_object = _load(args.truth)
    if not isinstance(truth_object, dict) or not isinstance(truth_object.get("y"), list):
        raise ValueError("truth must be an object with a y array")
    actual = _finite_numbers(truth_object["y"], "truth.y")
    if len(evaluation) != len(predicted) or len(actual) != len(predicted):
        raise ValueError(
            f"length mismatch: predict_at={len(evaluation)}, predictions={len(predicted)}, truth={len(actual)}"
        )

    baseline = truth_object.get("nn_rmse")
    if isinstance(baseline, bool) or not isinstance(baseline, (int, float)) or not math.isfinite(float(baseline)):
        raise ValueError("truth.nn_rmse must be finite and numeric")
    baseline = float(baseline)
    acceptance_bar = args.bar_ratio * baseline
    overall = _rmse(predicted, actual)
    errors = [abs(predicted[i] - actual[i]) for i in range(len(actual))]
    worst_index = max(range(len(errors)), key=errors.__getitem__)

    result = {
        "schema": "hil.hidden-law-diagnostic.v1",
        "status": "pass" if overall is not None and overall <= acceptance_bar else "fail",
        "metrics": {
            "n_observations": len(observations),
            "n_predictions": len(predicted),
            "rmse": _round(overall),
            "nearest_neighbor_rmse": _round(baseline),
            "acceptance_ratio": args.bar_ratio,
            "acceptance_bar": _round(acceptance_bar),
            "rmse_over_baseline": _round(overall / baseline if baseline else math.inf),
            "prediction_range": [_round(min(predicted)), _round(max(predicted))],
            "truth_range": [_round(min(actual)), _round(max(actual))],
            "worst_case": {
                "index": worst_index,
                "input": evaluation[worst_index],
                "prediction": _round(predicted[worst_index]),
                "truth": _round(actual[worst_index]),
                "absolute_error": _round(errors[worst_index]),
            },
        },
        "artifact_hashes": {
            "observations": _sha256(args.observations),
            "predict_at": _sha256(args.predict_at),
            "predictions": _sha256(args.predictions),
            "truth": _sha256(args.truth),
        },
    }

    params = truth_object.get("params")
    if truth_object.get("kind") == "regime_switch" and isinstance(params, dict):
        true_observation_high = _regime_mask(observations, params)
        true_evaluation_high = _regime_mask(evaluation, params)
        low_mask = [not value for value in true_evaluation_high]
        result["regime_diagnostics"] = {
            "observation_counts": {
                "low": len(observations) - sum(true_observation_high),
                "high": sum(true_observation_high),
            },
            "evaluation_counts": {
                "low": len(evaluation) - sum(true_evaluation_high),
                "high": sum(true_evaluation_high),
            },
            "rmse": {
                "low": _round(_rmse(predicted, actual, low_mask)),
                "high": _round(_rmse(predicted, actual, true_evaluation_high)),
                "high_and_b_gt_5": _round(_rmse(
                    predicted, actual,
                    [high and point["b"] > 5 for high, point in zip(true_evaluation_high, evaluation)],
                )),
                "high_and_a_gt_5": _round(_rmse(
                    predicted, actual,
                    [high and point["a"] > 5 for high, point in zip(true_evaluation_high, evaluation)],
                )),
            },
        }
        if args.candidate_boundary is not None:
            candidate_observation_high = _candidate_mask(observations, args.candidate_boundary)
            candidate_evaluation_high = _candidate_mask(evaluation, args.candidate_boundary)
            boundary = {
                "u": args.candidate_boundary[0],
                "v": args.candidate_boundary[1],
                "t": args.candidate_boundary[2],
            }
            result["candidate_boundary"] = {
                "definition": boundary,
                "observation_classification_errors": sum(
                    left != right for left, right in zip(candidate_observation_high, true_observation_high)
                ),
                "evaluation_classification_errors": sum(
                    left != right for left, right in zip(candidate_evaluation_high, true_evaluation_high)
                ),
            }
            if args.fit_damped_wave:
                fit = _fit_damped_wave(observations, candidate_observation_high)
                counterfactual = list(predicted)
                for index, (point, high) in enumerate(zip(evaluation, candidate_evaluation_high)):
                    if high:
                        counterfactual[index] = (
                            fit["A"] * math.exp(-fit["lambda"] * point["a"])
                            * math.sin(fit["k"] * point["b"]) + fit["c"]
                        )
                fit["evaluation_high_rmse"] = _round(_rmse(counterfactual, actual, true_evaluation_high))
                fit["hybrid_total_rmse"] = _round(_rmse(counterfactual, actual))
                fit["hybrid_status"] = "pass" if fit["hybrid_total_rmse"] <= acceptance_bar else "fail"
                result["damped_wave_counterfactual"] = fit

    if args.redact_private:
        result["artifact_hashes"].pop("truth", None)
        worst = result["metrics"].get("worst_case")
        if isinstance(worst, dict):
            worst.pop("truth", None)
        result["privacy"] = "private truth hash and point truth values redacted"
    return result


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--observations", type=Path, required=True)
    parser.add_argument("--predict-at", type=Path, required=True)
    parser.add_argument("--predictions", type=Path, required=True)
    parser.add_argument("--truth", type=Path, required=True, help="evaluator-only truth.json")
    parser.add_argument("--bar-ratio", type=float, default=0.25)
    parser.add_argument("--candidate-boundary", type=_parse_boundary, metavar="U,V,T")
    parser.add_argument("--fit-damped-wave", action="store_true")
    parser.add_argument("--redact-private", action="store_true")
    parser.add_argument("--output", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    if not math.isfinite(args.bar_ratio) or args.bar_ratio <= 0:
        parser.error("--bar-ratio must be finite and positive")
    if args.fit_damped_wave and args.candidate_boundary is None:
        parser.error("--fit-damped-wave requires --candidate-boundary")
    try:
        result = diagnose(args)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.exit(2, f"diagnostic error: {exc}\n")
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
