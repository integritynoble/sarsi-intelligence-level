#!/usr/bin/env python3
"""Recompute the Version 2.0 paper dataset's reported statistics."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HSC = ROOT / "evidence" / "harness_scaling_curve"
REGIME = ROOT / "evidence" / "regime_switch"
T_WEIGHTS = {"T0": 1.0, "T1": 2.0, "T2": 4.0, "T3": 8.0}
RUNG_ORDER = ("HG0", "HG1", "HG2", "HG3")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def exact_two_sided_binomial_p(successes: int, trials: int) -> float:
    if trials == 0:
        return 1.0
    observed = math.comb(trials, successes)
    numerator = sum(
        math.comb(trials, k)
        for k in range(trials + 1)
        if math.comb(trials, k) <= observed
    )
    return min(1.0, numerator / (2**trials))


def hsc_analysis() -> dict[str, object]:
    rows = read_csv(HSC / "episodes.csv")
    by_rung: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_rung[row["rung"]].append(row)

    rung_results = []
    for rung in RUNG_ORDER:
        rung_rows = by_rung[rung]
        by_band: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rung_rows:
            by_band[row["T_band"]].append(row)

        weighted_gross = 0.0
        weighted_net = 0.0
        total_weight = 0.0
        surface = {}
        for band in sorted(by_band, key=lambda item: int(item[1:])):
            band_rows = by_band[band]
            count = len(band_rows)
            pass_rate = sum(int(row["verifier_pass"]) for row in band_rows) / count
            false_rate = sum(int(row["false_completion"]) for row in band_rows) / count
            weight = T_WEIGHTS[band]
            surface[band] = {
                "episodes": count,
                "pass_rate": pass_rate,
                "false_completion_rate": false_rate,
                "net_rate_rho_1": pass_rate - false_rate,
            }
            weighted_gross += weight * pass_rate
            weighted_net += weight * (pass_rate - false_rate)
            total_weight += weight

        gross = weighted_gross / total_weight
        net = weighted_net / total_weight
        rung_results.append(
            {
                "rung": rung,
                "episodes": len(rung_rows),
                "gross_a_di": gross,
                "gross_hlis_di": 100 * gross,
                "net_a_di_rho_1": net,
                "net_hlis_di_rho_1": 100 * net,
                "false_completions": sum(int(row["false_completion"]) for row in rung_rows),
                "held_back": sum(int(row["held_back"]) for row in rung_rows),
                "false_rejections": sum(int(row["false_rejection"]) for row in rung_rows),
                "harness_iterations": sum(int(row["harness_iterations"]) for row in rung_rows),
                "model_calls": sum(int(row["model_calls"]) for row in rung_rows),
                "runner_seconds": sum(float(row["wall_time_seconds"]) for row in rung_rows),
                "surface": surface,
            }
        )

    gross_curve = [result["gross_hlis_di"] for result in rung_results]
    net_curve = [result["net_hlis_di_rho_1"] for result in rung_results]
    return {
        "episodes": len(rows),
        "rungs": rung_results,
        "gross_curve": gross_curve,
        "net_curve_rho_1": net_curve,
        "gross_hil_ceiling": max(gross_curve),
        "gross_hil_auc": statistics.fmean(gross_curve),
        "gross_harness_gain": max(gross_curve) - gross_curve[0],
        "net_harness_gain_rho_1": max(net_curve) - net_curve[0],
        "harness_iterations": sum(int(row["harness_iterations"]) for row in rows),
        "model_calls": sum(int(row["model_calls"]) for row in rows),
        "runner_seconds": sum(float(row["wall_time_seconds"]) for row in rows),
    }


def regime_analysis() -> tuple[dict[str, object], list[dict[str, object]]]:
    frontier = {int(row["seed"]): row for row in read_csv(REGIME / "frontier.csv")}
    haiku = {int(row["seed"]): row for row in read_csv(REGIME / "haiku.csv")}
    if frontier.keys() != haiku.keys():
        raise ValueError("Frontier and Haiku seed sets differ")

    paired = []
    frontier_only = haiku_only = both_pass = both_fail = 0
    frontier_lower = haiku_lower = ties = 0
    for seed in sorted(frontier):
        f = frontier[seed]
        h = haiku[seed]
        f_pass = f["result"] == "pass"
        h_pass = h["result"] == "pass"
        if f_pass and h_pass:
            pair = "both_pass"
            both_pass += 1
        elif f_pass:
            pair = "frontier_only"
            frontier_only += 1
        elif h_pass:
            pair = "haiku_only"
            haiku_only += 1
        else:
            pair = "both_fail"
            both_fail += 1

        f_rmse = float(f["extrapolation_rmse"])
        h_rmse = float(h["extrapolation_rmse"])
        baseline = float(f["nn_baseline_rmse"])
        if not math.isclose(baseline, float(h["nn_baseline_rmse"]), rel_tol=0, abs_tol=1e-12):
            raise ValueError(f"Nearest-neighbour baseline differs at seed {seed}")
        if f_rmse < h_rmse:
            winner = "frontier"
            frontier_lower += 1
        elif h_rmse < f_rmse:
            winner = "haiku"
            haiku_lower += 1
        else:
            winner = "tie"
            ties += 1
        paired.append(
            {
                "seed": seed,
                "frontier_result": f["result"],
                "haiku_result": h["result"],
                "frontier_rmse": f_rmse,
                "haiku_rmse": h_rmse,
                "nn_baseline_rmse": baseline,
                "bar": float(f["bar"]),
                "frontier_normalized_rmse": f_rmse / baseline,
                "haiku_normalized_rmse": h_rmse / baseline,
                "pass_pair": pair,
                "rmse_winner": winner,
            }
        )

    f_rmse_values = [row["frontier_rmse"] for row in paired]
    h_rmse_values = [row["haiku_rmse"] for row in paired]
    f_norm = [row["frontier_normalized_rmse"] for row in paired]
    h_norm = [row["haiku_normalized_rmse"] for row in paired]
    discordant = frontier_only + haiku_only
    non_tied_rmse = frontier_lower + haiku_lower
    summary = {
        "seeds": [row["seed"] for row in paired],
        "episodes": 2 * len(paired),
        "frontier_passes": sum(row["frontier_result"] == "pass" for row in paired),
        "haiku_passes": sum(row["haiku_result"] == "pass" for row in paired),
        "paired_outcomes": {
            "frontier_only": frontier_only,
            "haiku_only": haiku_only,
            "both_pass": both_pass,
            "both_fail": both_fail,
        },
        "paired_pass_rate_difference": (frontier_only - haiku_only) / len(paired),
        "mcnemar_exact_two_sided_p": exact_two_sided_binomial_p(frontier_only, discordant),
        "rmse_ordering": {
            "frontier_lower": frontier_lower,
            "haiku_lower": haiku_lower,
            "ties": ties,
        },
        "sign_test_exact_two_sided_p": exact_two_sided_binomial_p(frontier_lower, non_tied_rmse),
        "median_rmse": {
            "frontier": statistics.median(f_rmse_values),
            "haiku": statistics.median(h_rmse_values),
        },
        "median_normalized_rmse": {
            "frontier": statistics.median(f_norm),
            "haiku": statistics.median(h_norm),
        },
        "frontier_failures_worse_than_nearest_neighbour": sum(
            row["frontier_result"] != "pass" and row["frontier_normalized_rmse"] > 1
            for row in paired
        ),
        "haiku_failures_worse_than_nearest_neighbour": sum(
            row["haiku_result"] != "pass" and row["haiku_normalized_rmse"] > 1
            for row in paired
        ),
    }
    return summary, paired


def write_outputs(hsc: dict[str, object], regime: dict[str, object], paired: list[dict[str, object]]) -> None:
    (HSC / "analysis_results.json").write_text(
        json.dumps(hsc, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (REGIME / "analysis_results.json").write_text(
        json.dumps(regime, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    fields = list(paired[0])
    with (REGIME / "paired_results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(paired)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write derived result files")
    args = parser.parse_args()
    hsc = hsc_analysis()
    regime, paired = regime_analysis()
    results = {"harness_scaling_curve": hsc, "regime_switch": regime}
    if args.write:
        write_outputs(hsc, regime, paired)
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
