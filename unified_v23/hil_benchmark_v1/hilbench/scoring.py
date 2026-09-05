"""Transparent HIL-Core scoring for one frozen model--harness pair."""

from __future__ import annotations

import math
from collections import defaultdict
from typing import Any, Iterable

from .constants import (
    ALL_COORDINATES,
    BENCHMARK_VERSION,
    DEFAULT_FALSE_COMPLETION_LOSS_RATIO,
    DEFAULT_LEVEL_THRESHOLD,
    DEFAULT_RELIABILITY,
    INDIVIDUAL_DIMENSIONS,
    LEVEL_NAMES,
    ORGANIZATION_DIMENSIONS,
    REPORT_SCHEMA_VERSION,
    U_GATES,
)


def _round(value: float, digits: int = 3) -> float:
    return round(float(value), digits)


def wilson_interval(successes: int, total: int, z: float = 1.959963984540054) -> list[float] | None:
    """Two-sided 95% Wilson interval, returned on a 0--100 scale."""
    if total <= 0:
        return None
    proportion = successes / total
    denominator = 1.0 + z * z / total
    centre = (proportion + z * z / (2.0 * total)) / denominator
    margin = z * math.sqrt(proportion * (1.0 - proportion) / total + z * z / (4.0 * total * total)) / denominator
    return [_round(max(0.0, centre - margin) * 100.0), _round(min(1.0, centre + margin) * 100.0)]


def _geometric_mean(values: Iterable[float]) -> float:
    numbers = list(values)
    if not numbers:
        raise ValueError("geometric mean requires at least one value")
    if any(value <= 0.0 for value in numbers):
        return 0.0
    return math.exp(sum(math.log(value) for value in numbers) / len(numbers))


def _level_label(coordinate: str, numeric: int) -> str:
    if numeric < 0:
        return f"below_{coordinate}0"
    names = LEVEL_NAMES[coordinate]
    name = names[numeric] if numeric < len(names) else "beyond-instrument"
    return f"{coordinate}{numeric} ({name})"


def _not_applicable() -> dict[str, Any]:
    return {
        "status": "not_applicable",
        "achievement_pct": None,
        "ordinal_level": "N/A",
        "tasks": 0,
        "passes": 0,
        "ci95_pct": None,
        "level_bands": [],
        "coverage": {"families": 0, "mechanisms": 0},
        "headroom": {"status": "unassessed", "value": None},
    }


def _unassessed() -> dict[str, Any]:
    return {
        "status": "unassessed",
        "achievement_pct": None,
        "ordinal_level": "unassessed",
        "tasks": 0,
        "passes": 0,
        "ci95_pct": None,
        "level_bands": [],
        "coverage": {"families": 0, "mechanisms": 0},
        "headroom": {"status": "unassessed", "value": None},
    }


def _score_cumulative(coordinate: str, rows: list[dict[str, Any]], threshold: float) -> tuple[dict[str, Any], int | None]:
    if not rows:
        return _unassessed(), None
    by_level: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_level[int(row["level"])].append(row)
    bands = []
    running_min = 1.0
    weighted_sum = 0.0
    weight_total = 0.0
    highest = -1
    expected_next = 0
    for level in sorted(by_level):
        level_rows = by_level[level]
        raw = sum(float(row.get("score", bool(row.get("verifier_pass")))) for row in level_rows) / len(level_rows)
        running_min = min(running_min, raw)
        level_weight = float(2**level)
        weighted_sum += level_weight * running_min
        weight_total += level_weight
        contiguous = level == expected_next
        if contiguous:
            expected_next += 1
            if running_min >= threshold:
                highest = level
        bands.append(
            {
                "level": level,
                "raw_rate": _round(raw),
                "cumulative_rate": _round(running_min),
                "tasks": len(level_rows),
                "threshold": threshold,
            }
        )
    passes = sum(bool(row.get("verifier_pass")) for row in rows)
    result = {
        "status": "assessed",
        "achievement_pct": _round(100.0 * weighted_sum / weight_total),
        "ordinal_level": _level_label(coordinate, highest),
        "tasks": len(rows),
        "passes": passes,
        "ci95_pct": wilson_interval(passes, len(rows)),
        "level_bands": bands,
        "coverage": {
            "families": len({row["family"] for row in rows}),
            "mechanisms": len({row["mechanism"] for row in rows}),
        },
        "headroom": {"status": "unassessed", "value": None},
    }
    return result, highest


def _score_delegation(
    rows: list[dict[str, Any]], reliability: float, loss_ratio: float
) -> tuple[dict[str, Any], tuple[int, int] | None]:
    if not rows:
        result = _unassessed()
        result.update({"surface": [], "frontiers": {f"H{h}": "unassessed" for h in range(6)}})
        return result, None
    cells: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        cells[(int(row["T"]), int(row["H"]))].append(row)
    surface = []
    cell_net: dict[tuple[int, int], float] = {}
    weighted_sum = 0.0
    weight_total = 0.0
    delivered_pass_total = 0
    false_completion_total = 0
    held_back_total = 0
    false_rejection_total = 0
    for (t_band, h_band), cell_rows in sorted(cells.items(), key=lambda item: (item[0][1], item[0][0])):
        total = len(cell_rows)
        verifier_passes = sum(bool(row["verifier_pass"]) for row in cell_rows)
        delivered_pass = sum(
            bool(row["verifier_pass"]) and row.get("harness_accepted") is not False for row in cell_rows
        )
        false_completion = sum(
            not bool(row["verifier_pass"]) and row.get("harness_accepted") is not False for row in cell_rows
        )
        held_back = sum(
            not bool(row["verifier_pass"]) and row.get("harness_accepted") is False for row in cell_rows
        )
        false_rejection = sum(
            bool(row["verifier_pass"]) and row.get("harness_accepted") is False for row in cell_rows
        )
        raw = verifier_passes / total
        net = max(0.0, delivered_pass / total - loss_ratio * false_completion / total)
        cell_net[(t_band, h_band)] = net
        weight = float((2**t_band) * (6 - h_band))
        weighted_sum += weight * net
        weight_total += weight
        delivered_pass_total += delivered_pass
        false_completion_total += false_completion
        held_back_total += held_back
        false_rejection_total += false_rejection
        surface.append(
            {
                "T": t_band,
                "H": h_band,
                "tasks": total,
                "raw_success_rate": _round(raw),
                "net_delivered_score": _round(net),
                "delivered_correct": delivered_pass,
                "false_completions": false_completion,
                "held_back": held_back,
                "false_rejections": false_rejection,
                "ci95_delivered_pct": wilson_interval(delivered_pass, total),
            }
        )
    frontiers: dict[str, str] = {}
    numeric_frontiers: dict[int, int | None] = {}
    for h_band in range(6):
        observed = sorted(t for (t, h) in cell_net if h == h_band)
        if not observed:
            frontiers[f"H{h_band}"] = "unassessed"
            numeric_frontiers[h_band] = None
            continue
        frontier = -1
        expected_t = 0
        for t_band in observed:
            if t_band != expected_t or cell_net[(t_band, h_band)] < reliability:
                break
            frontier = t_band
            expected_t += 1
        numeric_frontiers[h_band] = frontier
        frontiers[f"H{h_band}"] = f"T{frontier}" if frontier >= 0 else "below_T0"
    measured_pairs = [(t, h) for h, t in numeric_frontiers.items() if t is not None and t >= 0]
    best = sorted(measured_pairs, key=lambda pair: (-pair[0], pair[1]))[0] if measured_pairs else None
    passes = sum(bool(row["verifier_pass"]) for row in rows)
    result = {
        "status": "assessed",
        "achievement_pct": _round(100.0 * weighted_sum / weight_total),
        "ordinal_level": f"T{best[0]}/H{best[1]}" if best else "below_T0",
        "tasks": len(rows),
        "passes": passes,
        "ci95_pct": wilson_interval(delivered_pass_total, len(rows)),
        "reliability_threshold": reliability,
        "false_completion_loss_ratio": loss_ratio,
        "surface": surface,
        "frontiers": frontiers,
        "false_completion_rate": _round(false_completion_total / len(rows)),
        "held_back_rate": _round(held_back_total / len(rows)),
        "false_rejection_rate": _round(false_rejection_total / len(rows)),
        "coverage": {
            "families": len({row["family"] for row in rows}),
            "mechanisms": len({row["mechanism"] for row in rows}),
            "T_bands": sorted({int(row["T"]) for row in rows}),
            "H_bands": sorted({int(row["H"]) for row in rows}),
        },
        "headroom": {"status": "unassessed", "value": None},
    }
    result["_numeric_frontiers"] = numeric_frontiers
    return result, best


def _unified_level(
    numeric_levels: dict[str, int | None], delegation: dict[str, Any], track: str
) -> tuple[int, list[str]]:
    frontiers = delegation.get("_numeric_frontiers", {})
    achieved = -1
    for u_level, gate in sorted(U_GATES.items()):
        failures = []
        for coordinate in ("C", "I", "SA", "M"):
            value = numeric_levels.get(coordinate)
            if value is None or value < gate[coordinate]:
                failures.append(coordinate)
        if track == "organization":
            value = numeric_levels.get("O")
            if value is None or value < gate["O"]:
                failures.append("O")
        delegation_pass = any(
            frontier is not None and h_band <= gate["max_H"] and frontier >= gate["T"]
            for h_band, frontier in frontiers.items()
        )
        if not delegation_pass:
            failures.append("DI")
        if failures:
            break
        achieved = u_level
    next_level = achieved + 1
    if next_level not in U_GATES:
        return achieved, ["instrument_ceiling"]
    gate = U_GATES[next_level]
    bottlenecks = []
    for coordinate in ("C", "I", "SA", "M"):
        value = numeric_levels.get(coordinate)
        if value is None or value < gate[coordinate]:
            bottlenecks.append(coordinate)
    if track == "organization":
        value = numeric_levels.get("O")
        if value is None or value < gate["O"]:
            bottlenecks.append("O")
    if not any(
        frontier is not None and h_band <= gate["max_H"] and frontier >= gate["T"]
        for h_band, frontier in frontiers.items()
    ):
        bottlenecks.append("DI")
    return achieved, bottlenecks


def _pair_hlis(coordinates: dict[str, dict[str, Any]], track: str) -> dict[str, Any]:
    declared = list(ORGANIZATION_DIMENSIONS if track == "organization" else INDIVIDUAL_DIMENSIONS)
    assessed = [dimension for dimension in declared if coordinates[dimension]["status"] == "assessed"]
    omitted_unassessed = [dimension for dimension in declared if coordinates[dimension]["status"] == "unassessed"]
    if omitted_unassessed:
        return {
            "status": "incomplete",
            "hlis": None,
            "ci95": None,
            "declared_dimension_set": declared,
            "scored_dimension_set": assessed,
            "omitted_unassessed": omitted_unassessed,
            "weights": {dimension: 1.0 for dimension in declared},
            "note": "No numeric HLIS is emitted when a required coordinate is unassessed.",
        }
    values = [coordinates[dimension]["achievement_pct"] / 100.0 for dimension in declared]
    hlis = 100.0 * _geometric_mean(values)
    lower = [coordinates[dimension]["ci95_pct"][0] / 100.0 for dimension in declared]
    upper = [coordinates[dimension]["ci95_pct"][1] / 100.0 for dimension in declared]
    return {
        "status": "complete",
        "hlis": _round(hlis),
        "ci95": [_round(100.0 * _geometric_mean(lower)), _round(100.0 * _geometric_mean(upper))],
        "declared_dimension_set": declared,
        "scored_dimension_set": declared,
        "omitted_unassessed": [],
        "weights": {dimension: 1.0 for dimension in declared},
        "note": "HLIS is a pair score; U* remains the promotion rule.",
    }


def _coverage(rows: list[dict[str, Any]], expected_tasks: int, track: str) -> dict[str, Any]:
    by_coordinate = {}
    for coordinate in ALL_COORDINATES:
        if coordinate == "O" and track == "individual":
            by_coordinate[coordinate] = {"status": "not_applicable", "tasks": 0}
            continue
        count = sum(row["coordinate"] == coordinate for row in rows)
        by_coordinate[coordinate] = {"status": "assessed" if count else "unassessed", "tasks": count}
    return {
        "expected_tasks": expected_tasks,
        "completed_tasks": len(rows),
        "fraction": _round(len(rows) / expected_tasks) if expected_tasks else 0.0,
        "by_coordinate": by_coordinate,
        "families": sorted({row["family"] for row in rows}),
        "mechanisms": sorted({row["mechanism"] for row in rows}),
    }


def score_episodes(
    episodes: list[dict[str, Any]],
    *,
    pair: dict[str, Any],
    track: str,
    split: str,
    mode: str,
    expected_tasks: int | None = None,
    reliability: float = DEFAULT_RELIABILITY,
    level_threshold: float = DEFAULT_LEVEL_THRESHOLD,
    loss_ratio: float = DEFAULT_FALSE_COMPLETION_LOSS_RATIO,
    resources: dict[str, Any] | None = None,
    adapter_name: str = "unknown",
) -> dict[str, Any]:
    if track not in {"individual", "organization"}:
        raise ValueError("track must be 'individual' or 'organization'")
    expected_tasks = len(episodes) if expected_tasks is None else expected_tasks
    grouped = {coordinate: [row for row in episodes if row["coordinate"] == coordinate] for coordinate in ALL_COORDINATES}
    coordinates: dict[str, dict[str, Any]] = {}
    numeric_levels: dict[str, int | None] = {}
    for coordinate in ("C", "I", "O", "SA", "M"):
        if coordinate == "O" and track == "individual":
            coordinates[coordinate] = _not_applicable()
            numeric_levels[coordinate] = None
        else:
            coordinates[coordinate], numeric_levels[coordinate] = _score_cumulative(
                coordinate, grouped[coordinate], level_threshold
            )
    coordinates["DI"], _ = _score_delegation(grouped["DI"], reliability, loss_ratio)
    u_numeric, bottlenecks = _unified_level(numeric_levels, coordinates["DI"], track)
    coordinates["DI"].pop("_numeric_frontiers", None)
    pair_hil = _pair_hlis(coordinates, track)
    applicable_core = ORGANIZATION_DIMENSIONS if track == "organization" else INDIVIDUAL_DIMENSIONS
    profile = {
        coordinate: coordinates[coordinate]["ordinal_level"]
        for coordinate in ("C", "I", "O", "DI", "SA", "M")
    }
    if split == "certification" and mode == "full" and adapter_name not in {"oracle-self-test", "mock-abstain"}:
        cert_status = "organizer_review_required"
        cert_eligible = len(episodes) == expected_tasks and all(
            coordinates[d]["status"] == "assessed" for d in applicable_core
        )
    elif adapter_name in {"oracle-self-test", "mock-abstain"}:
        cert_status, cert_eligible = "apparatus_self_test_only", False
    elif mode == "quick":
        cert_status, cert_eligible = "screening_only", False
    else:
        cert_status, cert_eligible = "development_only", False
    report = {
        "report_schema_version": REPORT_SCHEMA_VERSION,
        "benchmark_version": BENCHMARK_VERSION,
        "pair": pair,
        "track": track,
        "split": split,
        "mode": mode,
        "adapter": adapter_name,
        "coordinate_results": coordinates,
        "coordinate_achievement_pct": {
            coordinate: coordinates[coordinate]["achievement_pct"] for coordinate in ALL_COORDINATES
        },
        "coordinate_levels": {
            coordinate: coordinates[coordinate]["ordinal_level"] for coordinate in ALL_COORDINATES
        },
        "memory": {
            "status": coordinates["M"]["status"],
            "achievement_pct": coordinates["M"]["achievement_pct"],
            "ordinal_level": coordinates["M"]["ordinal_level"],
            "role": "supporting prerequisite; excluded from HLIS to avoid double counting I",
        },
        "delegation": {
            key: coordinates["DI"][key]
            for key in (
                "achievement_pct",
                "ordinal_level",
                "reliability_threshold",
                "false_completion_loss_ratio",
                "surface",
                "frontiers",
                "false_completion_rate",
                "held_back_rate",
                "false_rejection_rate",
            )
        },
        "unified": {
            "u_star": f"U{u_numeric}" if u_numeric >= 0 else "below_U0",
            "numeric_level": u_numeric,
            "profile": profile,
            "bottlenecks_to_next_gate": bottlenecks,
            "gate_is_cumulative": True,
            "instrument_ceiling": "U2",
        },
        "pair_hil": pair_hil,
        "coverage": _coverage(episodes, expected_tasks, track),
        "uncertainty": {
            "method": "Wilson 95% intervals on observed binary outcomes; HLIS bounds propagate coordinate bounds",
            "small_sample_warning": len(episodes) < 30,
            "repeat_run_variance": "unassessed",
        },
        "resources": resources or {},
        "certification": {
            "status": cert_status,
            "eligible_for_organizer_review": cert_eligible,
            "quick_is_certification": False,
            "requires_private_full_split": True,
            "claim": "No run is certified automatically by this reference implementation.",
        },
        "instrument": {
            "level_threshold": level_threshold,
            "reliability_threshold": reliability,
            "false_completion_loss_ratio": loss_ratio,
            "concordance_audit": {"status": "unassessed", "last_date": None, "flagged_items": None},
            "calibration_status": "research prototype; thresholds are working definitions",
        },
    }
    return report
