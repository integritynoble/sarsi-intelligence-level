"""Deterministic public task mechanisms.

Only public development mechanisms live here. Certification mechanisms are kept
under ``organizer_private`` and are excluded from the public release.
"""

from __future__ import annotations

from typing import Any, Callable

from .constants import BENCHMARK_VERSION


def _base(spec: dict[str, Any], prompt: str, task_input: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": spec["id"],
        "benchmark_version": BENCHMARK_VERSION,
        "split": spec["split"],
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
        "scoring": {"method": "exact_json", "weight": float(spec.get("weight", 1.0))},
    }


def c_affine_chain(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed, level = int(spec["seed"]), int(spec["level"])
    start = seed % 7 + 1
    operations: list[dict[str, int | str]] = []
    value = start
    for index in range(level + 2):
        multiplier = 2 + ((seed + index) % 2)
        addend = ((seed // (index + 1)) % 5) - 2
        operations.extend(({"op": "multiply", "value": multiplier}, {"op": "add", "value": addend}))
        value = value * multiplier + addend
    prompt = "Apply the listed operations in order and return {\"value\": integer}."
    return _base(spec, prompt, {"start": start, "operations": operations}), {"value": value}


def i_revision_ledger(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed, level = int(spec["seed"]), int(spec["level"])
    initial = seed % 11 + 10
    events = [
        {"id": "e1", "kind": "observe", "value": initial, "valid": True},
        {"id": "e2", "kind": "revise", "value": initial + level + 3, "valid": True},
        {"id": "e3", "kind": "distractor", "value": initial - 4, "valid": False},
    ]
    if level >= 2:
        events.append({"id": "e4", "kind": "consolidate", "value": initial + level + 4, "valid": True})
    current = next(event for event in reversed(events) if event["valid"])
    prompt = "Recover the current valid value and its provenance; ignore invalid stale events."
    task_input = {"entity": f"project-{seed % 5}", "events": events, "restart_boundary": level >= 1}
    return _base(spec, prompt, task_input), {"value": current["value"], "source": current["id"]}


def o_role_assignment(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed, level = int(spec["seed"]), int(spec["level"])
    rotation = seed % 3
    agents = [
        {"id": f"a{(rotation + 0) % 3}", "skill": "plan"},
        {"id": f"a{(rotation + 1) % 3}", "skill": "build"},
        {"id": f"a{(rotation + 2) % 3}", "skill": "verify"},
    ]
    required = ["plan", "build"] + (["verify"] if level >= 1 else [])
    assignments = {skill: next(a["id"] for a in agents if a["skill"] == skill) for skill in required}
    prompt = "Assign each required role to the uniquely skilled available agent."
    task_input = {"agents": agents, "required_roles": required, "evidence_required": level >= 2}
    return _base(spec, prompt, task_input), {"assignments": assignments}


def di_dependency_plan(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed = int(spec["seed"])
    difficulty = spec["difficulty"]
    t_band, h_band = int(difficulty["T"]), int(difficulty["H"])
    labels = [chr(ord("A") + ((seed + i) % 20)) for i in range(t_band + 2)]
    steps = []
    for index, label in enumerate(labels):
        steps.append({"id": label, "requires": [] if index == 0 else [labels[index - 1]]})
    assistance = None if h_band == 0 else {"kind": "bounded_hint", "text": f"Begin with {labels[0]}."}
    prompt = "Return a valid execution order as {\"order\": [...]}; dependencies must precede dependants."
    task_input = {"steps": list(reversed(steps)), "assistance": assistance}
    return _base(spec, prompt, task_input), {"order": labels}


def sa_grounded_status(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed, level = int(spec["seed"]), int(spec["level"])
    calls_left = seed % 4
    limit = "network_unavailable" if seed % 2 else "write_scope_restricted"
    facts = {
        "role": "benchmark_solver",
        "phase": ["observe", "plan", "verify"][level % 3],
        "calls_left": calls_left,
        "observed_limit": limit,
        "fresh_at_step": level + 1,
    }
    fields = ["role", "phase"]
    if level >= 1:
        fields.extend(["calls_left", "observed_limit"])
    if level >= 2:
        fields.append("fresh_at_step")
    prompt = "Report only the requested self-state fields, grounded in the supplied runtime facts."
    return _base(spec, prompt, {"runtime_facts": facts, "requested_fields": fields}), {
        "state": {field: facts[field] for field in fields}
    }


def m_provenance_retrieval(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    seed, level = int(spec["seed"]), int(spec["level"])
    base = seed % 13 + 20
    records = [
        {"id": "r1", "time": 1, "value": base, "status": "current", "source": "observation"},
        {"id": "r2", "time": 2, "value": base + 2, "status": "current", "source": "verified-update"},
    ]
    if level >= 2:
        records.append({"id": "r3", "time": 3, "value": base - 5, "status": "obsolete", "source": "stale-cache"})
    if level >= 3:
        records.append({"id": "r4", "time": 4, "value": base + 3, "status": "current", "source": "consolidation"})
    chosen = max((row for row in records if row["status"] == "current"), key=lambda row: row["time"])
    prompt = "Return the latest non-obsolete value, record id, and source."
    task_input = {"records": list(reversed(records)) if seed % 2 else records, "restart_boundary": level >= 1}
    answer = {"value": chosen["value"], "record_id": chosen["id"], "source": chosen["source"]}
    return _base(spec, prompt, task_input), answer


PUBLIC_GENERATORS: dict[str, Callable[[dict[str, Any]], tuple[dict[str, Any], dict[str, Any]]]] = {
    "affine_chain": c_affine_chain,
    "revision_ledger": i_revision_ledger,
    "role_assignment": o_role_assignment,
    "dependency_plan": di_dependency_plan,
    "grounded_status": sa_grounded_status,
    "provenance_retrieval": m_provenance_retrieval,
}


def materialize_public(spec: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    try:
        generator = PUBLIC_GENERATORS[spec["mechanism"]]
    except KeyError as exc:
        raise ValueError(f"unknown public mechanism: {spec.get('mechanism')!r}") from exc
    return generator(spec)
