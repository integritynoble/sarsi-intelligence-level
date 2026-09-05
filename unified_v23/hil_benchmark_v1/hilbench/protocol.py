"""HIL-Core JSONL request/response protocol validation."""

from __future__ import annotations

from typing import Any

from .constants import PROTOCOL_VERSION


class ProtocolError(ValueError):
    """A candidate process returned a malformed response."""


def make_request(task: dict[str, Any], run_id: str, mode: str) -> dict[str, Any]:
    return {
        "protocol_version": PROTOCOL_VERSION,
        "type": "task",
        "run_id": run_id,
        "task": task,
        "context": {"mode": mode, "expected_answer_is_hidden": True},
    }


def validate_response(value: Any, task_id: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ProtocolError("response must be a JSON object")
    if value.get("protocol_version") != PROTOCOL_VERSION:
        raise ProtocolError(f"protocol_version must be {PROTOCOL_VERSION!r}")
    if value.get("task_id") != task_id:
        raise ProtocolError("task_id does not match request")
    if "answer" not in value:
        raise ProtocolError("response must contain answer")
    accepted = value.get("harness_accepted")
    if accepted is not None and not isinstance(accepted, bool):
        raise ProtocolError("harness_accepted must be true, false, or null")
    attempts = value.get("attempts", 1)
    if not isinstance(attempts, int) or isinstance(attempts, bool) or attempts < 1:
        raise ProtocolError("attempts must be a positive integer")
    return {
        "protocol_version": PROTOCOL_VERSION,
        "task_id": task_id,
        "answer": value["answer"],
        "harness_accepted": accepted,
        "attempts": attempts,
        "verification_responsive": value.get("verification_responsive"),
        "usage": value.get("usage"),
    }
