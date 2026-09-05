"""Suite loading, execution, external verification, and resource accounting."""

from __future__ import annotations

import hashlib
import time
import uuid
from pathlib import Path
from typing import Any

from .adapters import MockAdapter, OracleAdapter, SubprocessAdapter
from .constants import BENCHMARK_VERSION
from .generators import materialize_public
from .io import canonical_json, read_json, read_jsonl, write_jsonl
from .protocol import make_request
from .scoring import score_episodes

PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def _private_materializer():
    try:
        from organizer_private.private_generators import materialize_private
    except ImportError as exc:
        raise FileNotFoundError("organizer-private generator is unavailable in this distribution") from exc
    return materialize_private


def suite_paths(split: str) -> tuple[Path, Path]:
    if split in {"dev", "validation"}:
        return (
            PACKAGE_ROOT / "tasks" / "public" / f"{split}.jsonl",
            PACKAGE_ROOT / "tasks" / "public" / "keys" / f"{split}_keys.json",
        )
    if split == "certification":
        return (
            PACKAGE_ROOT / "organizer_private" / "tasks" / "certification.jsonl",
            PACKAGE_ROOT / "organizer_private" / "keys" / "certification_keys.json",
        )
    raise ValueError("split must be dev, validation, or certification")


def load_suite(
    split: str,
    mode: str,
    track: str,
    *,
    allow_private: bool = False,
) -> tuple[list[dict[str, Any]], dict[str, Any], int]:
    if mode not in {"quick", "full"}:
        raise ValueError("mode must be quick or full")
    if track not in {"individual", "organization"}:
        raise ValueError("track must be individual or organization")
    if split == "certification" and not allow_private:
        raise PermissionError("certification data requires explicit --allow-private organizer access")
    spec_path, key_path = suite_paths(split)
    specs = read_jsonl(spec_path)
    stored_keys = read_json(key_path)
    materializer = _private_materializer() if split == "certification" else materialize_public
    tasks: list[dict[str, Any]] = []
    keys: dict[str, Any] = {}
    seen: set[str] = set()
    for spec in specs:
        if spec.get("benchmark_version") != BENCHMARK_VERSION:
            raise ValueError(f"{spec.get('id')}: benchmark version mismatch")
        if spec.get("split") != split:
            raise ValueError(f"{spec.get('id')}: split mismatch")
        task, computed_key = materializer(spec)
        task_id = task["id"]
        if task_id in seen:
            raise ValueError(f"duplicate task id: {task_id}")
        seen.add(task_id)
        if task_id not in stored_keys:
            raise ValueError(f"{task_id}: missing answer key")
        if canonical_json(stored_keys[task_id]) != canonical_json(computed_key):
            raise ValueError(f"{task_id}: specification--key consistency failure")
        if mode == "quick" and not task["quick"]:
            continue
        if track == "individual" and task["track"] == "organization":
            continue
        tasks.append(task)
        keys[task_id] = stored_keys[task_id]
    return tasks, keys, len(tasks)


def load_profile(path: Path | None, track: str | None = None) -> tuple[dict[str, Any], str]:
    if path is None:
        chosen_track = track or "individual"
        pair = {
            "model": {"id": "unspecified", "version": "unassessed", "hash": "unassessed"},
            "harness": {"id": "unspecified", "version": "unassessed", "manifest_hash": "unassessed"},
            "frozen": False,
        }
        return pair, chosen_track
    profile = read_json(path)
    if profile.get("profile_schema_version") != "1.0":
        raise ValueError("unsupported profile_schema_version")
    profile_track = profile.get("track")
    chosen_track = track or profile_track
    if chosen_track not in {"individual", "organization"}:
        raise ValueError("profile track must be individual or organization")
    pair = {
        "model": profile["model"],
        "harness": profile["harness"],
        "frozen": bool(profile.get("frozen", False)),
        "profile_id": profile["profile_id"],
    }
    return pair, chosen_track


def _adapter(kind: str, command: list[str] | None, timeout_seconds: float):
    if kind == "oracle":
        return OracleAdapter()
    if kind == "mock":
        return MockAdapter()
    if kind == "subprocess":
        if not command:
            raise ValueError("--command is required with --adapter subprocess")
        return SubprocessAdapter(command, timeout_seconds)
    raise ValueError("adapter must be oracle, mock, or subprocess")


def run_suite(
    *,
    split: str,
    mode: str,
    track: str,
    pair: dict[str, Any],
    adapter_kind: str,
    command: list[str] | None = None,
    timeout_seconds: float = 15.0,
    allow_private: bool = False,
    events_path: Path | None = None,
) -> dict[str, Any]:
    tasks, keys, expected_count = load_suite(split, mode, track, allow_private=allow_private)
    adapter = _adapter(adapter_kind, command, timeout_seconds)
    run_id = str(uuid.uuid4())
    started = time.monotonic()
    episodes: list[dict[str, Any]] = []
    token_fields = {"input_tokens": 0, "output_tokens": 0, "llm_calls": 0, "cost_usd": 0.0}
    usage_complete = True
    for task in tasks:
        expected = keys[task["id"]]
        request = make_request(task, run_id, mode)
        result = adapter.invoke(request, expected)
        response = result.response
        verifier_pass = canonical_json(response.get("answer")) == canonical_json(expected)
        accepted = response.get("harness_accepted")
        usage = response.get("usage")
        if not isinstance(usage, dict) or not all(field in usage for field in token_fields):
            usage_complete = False
        else:
            for field in token_fields:
                token_fields[field] += usage[field]
        difficulty = task.get("difficulty") or {}
        episodes.append(
            {
                "run_id": run_id,
                "task_id": task["id"],
                "coordinate": task["coordinate"],
                "level": task["level"],
                "family": task["family"],
                "mechanism": task["mechanism"],
                "T": difficulty.get("T"),
                "H": difficulty.get("H"),
                "weight": task["scoring"]["weight"],
                "verifier_pass": verifier_pass,
                "harness_accepted": accepted,
                "attempts": response.get("attempts", 1),
                "verification_responsive": response.get("verification_responsive"),
                "protocol_valid": result.error is None,
                "adapter_error": result.error,
                "timed_out": result.timed_out,
                "latency_ms": round(result.latency_ms, 3),
                "answer_sha256": hashlib.sha256(canonical_json(response.get("answer")).encode("utf-8")).hexdigest(),
            }
        )
    wall_ms = (time.monotonic() - started) * 1000.0
    if events_path is not None:
        write_jsonl(events_path, episodes)
    resources = {
        "wall_time_ms": round(wall_ms, 3),
        "adapter_calls": len(episodes),
        "attempts": sum(row["attempts"] for row in episodes),
        "timeouts": sum(row["timed_out"] for row in episodes),
        "protocol_errors": sum(not row["protocol_valid"] for row in episodes),
        "token_usage": token_fields if usage_complete else {"status": "unassessed", "value": None},
        "retail_cost_usd": token_fields["cost_usd"] if usage_complete else None,
        "compute_class": "unassessed",
        "persistent_memory_bytes": "unassessed",
        "tool_access": pair.get("harness", {}).get("tool_access", "unassessed"),
        "external_knowledge_access": pair.get("harness", {}).get("external_knowledge_access", "unassessed"),
        "subagent_count": pair.get("harness", {}).get("subagent_count", "unassessed"),
        "human_interventions": {"status": "unassessed", "count": None, "cognitive_minutes": None},
    }
    return score_episodes(
        episodes,
        pair=pair,
        track=track,
        split=split,
        mode=mode,
        expected_tasks=expected_count,
        resources=resources,
        adapter_name=adapter.name,
    )
