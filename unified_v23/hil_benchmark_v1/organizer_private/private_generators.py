"""Held-out certification mechanisms.

This module, its task specifications, and its keys must never be distributed in
the public benchmark archive.
"""

from __future__ import annotations

from typing import Any, Callable

from hilbench.constants import BENCHMARK_VERSION


def _base(spec: dict[str, Any], prompt: str, task_input: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": spec["id"],
        "benchmark_version": BENCHMARK_VERSION,
        "split": "certification",
        "coordinate": spec["coordinate"],
        "level": int(spec["level"]),
        "family": spec["family"],
        "mechanism": spec["mechanism"],
        "seed": int(spec["seed"]),
        "track": spec.get("track", "both"),
        "quick": bool(spec.get("quick", False)),
        "difficulty": spec.get("difficulty"),
        "prompt": prompt,
        "input": task_input,
        "answer_schema": {"type": "object", "additionalProperties": False},
        "scoring": {"method": "exact_json", "weight": 1.0},
    }


def c_relation_induction(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed, level = int(spec["seed"]), int(spec["level"])
    offset = seed % 5 + 1
    scale = level + 2
    examples = [{"x": x, "y": scale * x * x + offset} for x in range(1, level + 4)]
    query = level + 5
    prompt = "Infer the single relation fitting every example and return its output for query_x."
    return _base(spec, prompt, {"examples": examples, "query_x": query}), {"value": scale * query * query + offset}


def i_policy_reversal(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed, level = int(spec["seed"]), int(spec["level"])
    policy = "blue" if seed % 2 else "amber"
    revised = "amber" if policy == "blue" else "blue"
    events = [
        {"id": "p1", "kind": "policy", "action": policy, "valid_from": 1},
        {"id": "p2", "kind": "counterevidence", "action": revised, "valid_from": 2 + level},
        {"id": "p3", "kind": "obsolete_copy", "action": policy, "valid_from": 1},
    ]
    prompt = "Apply the latest evidence-backed policy after the restart and cite its event."
    return _base(spec, prompt, {"events": events, "current_step": 3 + level, "restart": level >= 1}), {
        "action": revised,
        "source": "p2",
    }


def o_failure_reconfiguration(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed, level = int(spec["seed"]), int(spec["level"])
    failed = f"primary-{seed % 3}"
    agents = [
        {"id": failed, "skill": "verify", "available": False},
        {"id": f"backup-{seed % 5}", "skill": "verify", "available": True},
        {"id": f"builder-{seed % 7}", "skill": "build", "available": True},
    ]
    roles = ["verify"] + (["build"] if level >= 1 else [])
    assignment = {
        role: next(agent["id"] for agent in agents if agent["skill"] == role and agent["available"])
        for role in roles
    }
    prompt = "Reconfigure around the failed member and assign every requested role to an available skilled member."
    return _base(spec, prompt, {"agents": agents, "roles": roles, "failure_event": failed}), {"assignments": assignment}


def di_regime_switch(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed = int(spec["seed"])
    t_band = int(spec["difficulty"]["T"])
    h_band = int(spec["difficulty"]["H"])
    start = seed % 9 + 1
    before = seed % 3 + 1
    after = before + t_band + 2
    switch_after = 2 + t_band
    values = [start]
    for index in range(1, switch_after + 2):
        delta = before if index <= switch_after else after
        values.append(values[-1] + delta)
    visible = values[:-1]
    hint = None if h_band == 0 else {"boundary_after_index": switch_after}
    prompt = "Detect the changed transition regime and return the next value."
    return _base(spec, prompt, {"observations": visible, "bounded_assistance": hint}), {"next": values[-1]}


def sa_causal_diagnosis(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed, level = int(spec["seed"]), int(spec["level"])
    causes = ["tool_denied", "stale_state", "budget_exhausted"]
    cause = causes[seed % len(causes)]
    trace = {
        "intended_action": "verify artifact",
        "observed_result": "not verified",
        "tool_status": "denied" if cause == "tool_denied" else "available",
        "state_age": 9 if cause == "stale_state" else 0,
        "calls_left": 0 if cause == "budget_exhausted" else 2,
        "evidence_step": level + 2,
    }
    prompt = "Diagnose the single cause supported by the trace and cite the grounding field."
    grounding = {"tool_denied": "tool_status", "stale_state": "state_age", "budget_exhausted": "calls_left"}[cause]
    return _base(spec, prompt, {"trace": trace, "candidate_causes": causes}), {"cause": cause, "grounding": grounding}


def m_snapshot_recovery(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed, level = int(spec["seed"]), int(spec["level"])
    value = seed % 17 + 30
    snapshots = [
        {"id": "s0", "parent": None, "integrity": "valid", "value": value},
        {"id": "s1", "parent": "s0", "integrity": "valid", "value": value + 1},
        {"id": "s2", "parent": "s1", "integrity": "corrupt", "value": value + 99},
    ]
    if level >= 3:
        snapshots.append({"id": "s3", "parent": "s1", "integrity": "valid", "value": value + 3})
        chosen = snapshots[-1]
    else:
        chosen = snapshots[1]
    prompt = "Recover the newest valid snapshot whose ancestry is entirely valid."
    return _base(spec, prompt, {"snapshots": list(reversed(snapshots)), "restart": level >= 1}), {
        "snapshot_id": chosen["id"],
        "value": chosen["value"],
    }


PRIVATE_GENERATORS: dict[str, Callable[[dict[str, Any]], tuple[dict[str, Any], dict[str, Any]]]] = {
    "relation_induction": c_relation_induction,
    "policy_reversal": i_policy_reversal,
    "failure_reconfiguration": o_failure_reconfiguration,
    "regime_switch": di_regime_switch,
    "causal_diagnosis": sa_causal_diagnosis,
    "snapshot_recovery": m_snapshot_recovery,
}


def materialize_private(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    try:
        return PRIVATE_GENERATORS[spec["mechanism"]](spec)
    except KeyError as exc:
        raise ValueError(f"unknown private mechanism: {spec.get('mechanism')!r}") from exc
