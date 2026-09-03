#!/usr/bin/env python3
"""Validate package structure, source hashes and headline statistics."""

from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

from analyze import hsc_analysis, regime_analysis


ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR = ROOT.parent
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def close(actual: float, expected: float, tolerance: float = 1e-12) -> bool:
    return math.isclose(actual, expected, rel_tol=0, abs_tol=tolerance)


def validate_schema_value(value: Any, rule: dict[str, Any], field: str, row_id: str) -> None:
    allowed = rule.get("type")
    allowed_types = [allowed] if isinstance(allowed, str) else allowed or []
    type_checks = {
        "null": value is None,
        "string": isinstance(value, str),
        "boolean": isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
    }
    if allowed_types:
        require(any(type_checks[item] for item in allowed_types), f"{row_id}: {field} has invalid type")
    if value is None:
        return
    if "enum" in rule:
        require(value in rule["enum"], f"{row_id}: {field} is outside schema enum")
    if "const" in rule:
        require(value == rule["const"], f"{row_id}: {field} differs from schema const")
    if "minimum" in rule:
        require(value >= rule["minimum"], f"{row_id}: {field} is below schema minimum")
    if "exclusiveMinimum" in rule:
        require(value > rule["exclusiveMinimum"], f"{row_id}: {field} is below schema exclusive minimum")


def validate_csv_schema(path: Path, schema_path: Path, boolean_fields: set[str], integer_fields: set[str], number_fields: set[str], id_field: str) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    require(schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema", f"unexpected schema draft: {schema_path}")
    rows = read_csv(path)
    properties = schema["properties"]
    require(set(rows[0]) == set(properties), f"CSV columns differ from schema properties: {path}")
    for raw in rows:
        row: dict[str, Any] = {}
        for field, value in raw.items():
            if value == "":
                row[field] = None
            elif field in boolean_fields:
                require(value in {"0", "1"}, f"{path.name}: {field} must be encoded as 0 or 1")
                row[field] = bool(int(value))
            elif field in integer_fields:
                row[field] = int(value)
            elif field in number_fields:
                row[field] = float(value)
            else:
                row[field] = value
        row_id = str(row[id_field])
        for required in schema["required"]:
            require(row.get(required) is not None, f"{row_id}: missing required field {required}")
        if schema.get("additionalProperties") is False:
            require(not (set(row) - set(properties)), f"{row_id}: unexpected properties")
        for field, value in row.items():
            validate_schema_value(value, properties[field], field, row_id)


def validate_sources() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    embedded_dependency = ROOT / "dependencies" / "HIL_Coordinate_Benchmark_Datasets_v1_2.zip"
    sibling_dependency = DATASET_DIR / "HIL_Coordinate_Benchmark_Datasets_v1_2.zip"
    dependency = embedded_dependency if embedded_dependency.exists() else sibling_dependency
    require(dependency.exists(), f"missing coordinate dependency: {dependency}")
    if dependency.exists():
        require(
            sha256(dependency) == manifest["coordinate_dataset_dependency"]["sha256"],
            "coordinate dependency SHA-256 mismatch",
        )

    released_hashes = [
        (
            ROOT / "evidence" / "regime_switch" / "frontier.csv",
            manifest["studies"]["regime_switch"]["frontier_csv_sha256"],
        ),
        (
            ROOT / "evidence" / "regime_switch" / "haiku.csv",
            manifest["studies"]["regime_switch"]["haiku_csv_sha256"],
        ),
        (
            ROOT / "evidence" / "harness_scaling_curve" / "canonical_report.txt",
            manifest["studies"]["harness_scaling_curve"]["canonical_report_sha256"],
        ),
    ]
    for released, expected_hash in released_hashes:
        require(released.exists(), f"missing released artifact: {released}")
        if released.exists():
            require(sha256(released) == expected_hash, f"released artifact SHA-256 mismatch: {released}")

    optional_source_pairs = [
        (
            DATASET_DIR.parent / "measurements" / "regime_switch_frontier.csv",
            ROOT / "evidence" / "regime_switch" / "frontier.csv",
        ),
        (
            DATASET_DIR.parent / "measurements" / "regime_switch_haiku.csv",
            ROOT / "evidence" / "regime_switch" / "haiku.csv",
        ),
        (
            DATASET_DIR / "HIL_Benchmark_Library_v0_2" / "HSC_measured_2026-08-25.txt",
            ROOT / "evidence" / "harness_scaling_curve" / "canonical_report.txt",
        ),
    ]
    for source, released in optional_source_pairs:
        if source.exists() and released.exists():
            require(sha256(source) == sha256(released), f"released copy differs from source: {released}")


def validate_checksums() -> None:
    checksum_path = ROOT / "checksums.sha256"
    require(checksum_path.exists(), "missing checksums.sha256")
    if not checksum_path.exists():
        return
    dependency = ROOT / "dependencies" / "HIL_Coordinate_Benchmark_Datasets_v1_2.zip"
    if not dependency.exists():
        dependency = DATASET_DIR / "HIL_Coordinate_Benchmark_Datasets_v1_2.zip"
    expected_paths = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.name != "checksums.sha256"
        and path != dependency
        and "__pycache__" not in path.parts
        and not path.name.endswith(".pyc")
    }
    expected_paths.add(f"dependencies/{dependency.name}")
    recorded_paths = set()
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        digest, separator, relative = line.partition("  ")
        require(bool(separator) and len(digest) == 64, f"malformed checksum line: {line}")
        if not separator:
            continue
        recorded_paths.add(relative)
        target = dependency if relative == f"dependencies/{dependency.name}" else ROOT / relative
        require(target.exists(), f"checksum target is missing: {relative}")
        if target.exists():
            require(sha256(target) == digest, f"checksum mismatch: {relative}")
    require(recorded_paths == expected_paths, "checksums.sha256 path set differs from package files")


def validate_hsc() -> dict[str, object]:
    validate_csv_schema(
        ROOT / "evidence" / "harness_scaling_curve" / "episodes.csv",
        ROOT / "schemas" / "hsc_episode.schema.json",
        {"verifier_pass", "harness_accepted", "false_completion", "held_back", "false_rejection"},
        {"seed", "harness_iterations", "model_calls"},
        {"wall_time_seconds"},
        "episode_id",
    )
    episodes = read_csv(ROOT / "evidence" / "harness_scaling_curve" / "episodes.csv")
    require(len(episodes) == 48, "HSC must contain 48 episodes")
    require(len({row["episode_id"] for row in episodes}) == 48, "HSC episode IDs must be unique")
    for row in episodes:
        require(row["rung"] in {"HG0", "HG1", "HG2", "HG3"}, f"invalid rung: {row['rung']}")
        require(row["T_band"] in {"T0", "T1", "T2", "T3"}, f"invalid T band: {row['T_band']}")
        require(row["H_budget"] == "H1", f"unexpected H budget: {row['H_budget']}")
        require(row["verifier_pass"] in {"0", "1"}, f"invalid verifier_pass: {row['episode_id']}")
        require(row["false_completion"] in {"0", "1"}, f"invalid false_completion: {row['episode_id']}")
        require(row["held_back"] in {"0", "1"}, f"invalid held_back: {row['episode_id']}")
        require(row["false_rejection"] in {"0", "1"}, f"invalid false_rejection: {row['episode_id']}")
        require(int(row["harness_iterations"]) >= int(row["model_calls"]), f"model calls exceed iterations: {row['episode_id']}")
        if row["rung"] == "HG0":
            require(row["harness_accepted"] == "", f"HG0 acceptance must be empty: {row['episode_id']}")
        else:
            require(row["harness_accepted"] in {"0", "1"}, f"acceptance missing: {row['episode_id']}")

    result = hsc_analysis()
    expected_curve = [93.33333333333333, 93.33333333333333, 96.66666666666667, 96.66666666666667]
    require(all(close(a, b) for a, b in zip(result["gross_curve"], expected_curve)), "HSC gross curve mismatch")
    require(close(result["gross_hil_auc"], 95.0), "HSC AUC mismatch")
    require(close(result["gross_harness_gain"], 3.333333333333343), "HSC gross harness gain mismatch")
    require(close(result["net_harness_gain_rho_1"], 10.0), "HSC net harness gain mismatch")
    require(result["harness_iterations"] == 53, "HSC harness iteration total must be 53")
    require(result["model_calls"] == 52, "HSC model-call total must be 52")
    require(result["runner_seconds"] == 4867, "HSC rounded runner seconds must total 4867")
    return result


def validate_regime() -> dict[str, object]:
    for name in ("frontier.csv", "haiku.csv"):
        validate_csv_schema(
            ROOT / "evidence" / "regime_switch" / name,
            ROOT / "schemas" / "regime_switch_observation.schema.json",
            {"mechanism_stated"},
            {"seed", "exit_code"},
            {"extrapolation_rmse", "bar", "nn_baseline_rmse", "target_spread", "seconds"},
            "seed",
        )
    result, paired = regime_analysis()
    require(len(paired) == 12, "regime-switch comparison must contain 12 pairs")
    require(result["episodes"] == 24, "regime-switch comparison must contain 24 episodes")
    require(result["frontier_passes"] == 5, "frontier pass count mismatch")
    require(result["haiku_passes"] == 1, "Haiku pass count mismatch")
    require(result["paired_outcomes"] == {"frontier_only": 4, "haiku_only": 0, "both_pass": 1, "both_fail": 7}, "paired outcome table mismatch")
    require(close(result["mcnemar_exact_two_sided_p"], 0.125), "McNemar p-value mismatch")
    require(result["rmse_ordering"] == {"frontier_lower": 11, "haiku_lower": 1, "ties": 0}, "RMSE ordering mismatch")
    require(close(result["sign_test_exact_two_sided_p"], 0.00634765625), "sign-test p-value mismatch")
    require(close(result["median_rmse"]["frontier"], 0.6385), "frontier median RMSE mismatch")
    require(close(result["median_rmse"]["haiku"], 5.1115), "Haiku median RMSE mismatch")
    require(close(result["median_normalized_rmse"]["frontier"], 0.35933368576416513), "frontier normalized median mismatch")
    require(close(result["median_normalized_rmse"]["haiku"], 2.142054756962124), "Haiku normalized median mismatch")
    require(result["frontier_failures_worse_than_nearest_neighbour"] == 3, "frontier worse-than-NN failure count mismatch")
    require(result["haiku_failures_worse_than_nearest_neighbour"] == 11, "Haiku worse-than-NN failure count mismatch")
    return result


def validate_derived(hsc: dict[str, object], regime: dict[str, object]) -> None:
    hsc_path = ROOT / "evidence" / "harness_scaling_curve" / "analysis_results.json"
    regime_path = ROOT / "evidence" / "regime_switch" / "analysis_results.json"
    paired_path = ROOT / "evidence" / "regime_switch" / "paired_results.csv"
    require(hsc_path.exists(), "missing generated HSC analysis_results.json")
    require(regime_path.exists(), "missing generated regime analysis_results.json")
    require(paired_path.exists(), "missing generated paired_results.csv")
    if hsc_path.exists():
        require(json.loads(hsc_path.read_text(encoding="utf-8")) == hsc, "stored HSC analysis is stale")
    if regime_path.exists():
        require(json.loads(regime_path.read_text(encoding="utf-8")) == regime, "stored regime analysis is stale")
    if paired_path.exists():
        require(len(read_csv(paired_path)) == 12, "paired_results.csv must contain 12 rows")


def main() -> int:
    validate_sources()
    validate_checksums()
    hsc = validate_hsc()
    regime = validate_regime()
    validate_derived(hsc, regime)
    report = {
        "hsc_episodes": hsc["episodes"],
        "regime_switch_episodes": regime["episodes"],
        "errors": ERRORS,
    }
    print(json.dumps(report, indent=2))
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
