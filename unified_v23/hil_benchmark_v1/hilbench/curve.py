"""Model-HIL curve contract across the frozen public reference harness ladder."""

from __future__ import annotations

from typing import Any

from .constants import BENCHMARK_VERSION, CURVE_SCHEMA_VERSION, REFERENCE_HARNESSES, REFERENCE_LADDER_ID


def _parse_u(value: str) -> int:
    if value == "below_U0":
        return -1
    if not value.startswith("U") or not value[1:].isdigit():
        raise ValueError(f"invalid U* value: {value!r}")
    return int(value[1:])


def build_model_hil_curve(reports: list[dict[str, Any]]) -> dict[str, Any]:
    if not reports:
        raise ValueError("at least one pair report is required")
    model = reports[0]["pair"]["model"]
    model_identity = (model.get("id"), model.get("version"), model.get("hash"))
    by_harness: dict[str, dict[str, Any]] = {}
    for report in reports:
        if report.get("benchmark_version") != BENCHMARK_VERSION:
            raise ValueError("all reports must use the current benchmark version")
        candidate = report["pair"]["model"]
        identity = (candidate.get("id"), candidate.get("version"), candidate.get("hash"))
        if identity != model_identity:
            raise ValueError("a Model-HIL curve must hold the frozen model identity fixed")
        harness_id = report["pair"]["harness"].get("id")
        if harness_id in by_harness:
            raise ValueError(f"duplicate harness report: {harness_id}")
        by_harness[harness_id] = report
    points = []
    cumulative_gate = True
    hil_level = -1
    numeric_scores: list[float] = []
    for generation, harness_id, target_u in REFERENCE_HARNESSES:
        report = by_harness.get(harness_id)
        if report is None:
            cumulative_gate = False
            points.append(
                {
                    "generation": generation,
                    "harness_id": harness_id,
                    "target_u": f"U{target_u}",
                    "status": "unassessed",
                    "u_star": "unassessed",
                    "hlis": None,
                }
            )
            continue
        hlis = report["pair_hil"].get("hlis")
        u_star = report["unified"]["u_star"]
        meets = hlis is not None and _parse_u(u_star) >= target_u
        cumulative_gate = cumulative_gate and meets
        if cumulative_gate:
            hil_level = target_u
        if hlis is not None:
            numeric_scores.append(float(hlis))
        points.append(
            {
                "generation": generation,
                "harness_id": harness_id,
                "target_u": f"U{target_u}",
                "status": "assessed" if hlis is not None else "incomplete_pair_report",
                "meets_cumulative_target": meets,
                "u_star": u_star,
                "hlis": hlis,
            }
        )
    complete = all(point["status"] == "assessed" for point in points)
    hg0_score = points[0]["hlis"]
    ceiling = max(numeric_scores) if numeric_scores else None
    gain = round(ceiling - hg0_score, 3) if ceiling is not None and hg0_score is not None else None
    auc = round(sum(numeric_scores) / len(numeric_scores), 3) if numeric_scores else None
    return {
        "model_hil_schema_version": CURVE_SCHEMA_VERSION,
        "benchmark_version": BENCHMARK_VERSION,
        "reference_ladder_id": REFERENCE_LADDER_ID,
        "model": model,
        "curve_is_primary_result": True,
        "curve": points,
        "summary": {
            "status": "complete" if complete else "truncated_not_comparable_to_complete_curve",
            "hil_level": f"HG{hil_level}" if hil_level >= 0 else "below_HG0_target",
            "hil_auc": auc,
            "hil_auc_denominator": len(numeric_scores),
            "hil_ceiling": ceiling,
            "harness_gain": gain,
            "verification_responsiveness": "unassessed",
            "single_composite": "not_reported",
        },
        "claim": "This characterizes one frozen model across named reference harnesses; it is not a bare-model score.",
    }
