"""Built-in self-test adapters and a provider-neutral subprocess adapter."""

from __future__ import annotations

import json
import subprocess
import time
from dataclasses import dataclass
from typing import Any, Sequence

from .constants import PROTOCOL_VERSION
from .io import canonical_json
from .protocol import ProtocolError, validate_response


@dataclass
class AdapterResult:
    response: dict[str, Any]
    latency_ms: float
    error: str | None = None
    timed_out: bool = False


class OracleAdapter:
    """Answer-key self-test. It is never a candidate measurement."""

    name = "oracle-self-test"

    def invoke(self, request: dict[str, Any], expected: Any) -> AdapterResult:
        started = time.monotonic()
        response = {
            "protocol_version": PROTOCOL_VERSION,
            "task_id": request["task"]["id"],
            "answer": expected,
            "harness_accepted": True,
            "attempts": 1,
            "verification_responsive": None,
            "usage": None,
        }
        return AdapterResult(response, (time.monotonic() - started) * 1000.0)


class MockAdapter:
    """Safe deterministic plumbing test which deliberately abstains."""

    name = "mock-abstain"

    def invoke(self, request: dict[str, Any], expected: Any) -> AdapterResult:
        del expected
        started = time.monotonic()
        response = {
            "protocol_version": PROTOCOL_VERSION,
            "task_id": request["task"]["id"],
            "answer": {"abstain": True},
            "harness_accepted": False,
            "attempts": 1,
            "verification_responsive": None,
            "usage": None,
        }
        return AdapterResult(response, (time.monotonic() - started) * 1000.0)


class SubprocessAdapter:
    """Run one isolated candidate process per task using JSONL over stdio."""

    name = "subprocess"

    def __init__(self, command: Sequence[str], timeout_seconds: float = 15.0) -> None:
        if not command or not all(isinstance(part, str) and part for part in command):
            raise ValueError("subprocess command must be a non-empty argument vector")
        self.command = list(command)
        self.timeout_seconds = timeout_seconds

    def invoke(self, request: dict[str, Any], expected: Any) -> AdapterResult:
        del expected
        started = time.monotonic()
        task_id = request["task"]["id"]
        try:
            completed = subprocess.run(
                self.command,
                input=canonical_json(request) + "\n",
                text=True,
                capture_output=True,
                timeout=self.timeout_seconds,
                check=False,
            )
        except subprocess.TimeoutExpired:
            elapsed = (time.monotonic() - started) * 1000.0
            return AdapterResult(_error_response(task_id), elapsed, "timeout", timed_out=True)
        elapsed = (time.monotonic() - started) * 1000.0
        if completed.returncode != 0:
            detail = completed.stderr.strip()[:500]
            error = f"candidate exited {completed.returncode}" + (f": {detail}" if detail else "")
            return AdapterResult(_error_response(task_id), elapsed, error)
        lines = [line for line in completed.stdout.splitlines() if line.strip()]
        if len(lines) != 1:
            return AdapterResult(_error_response(task_id), elapsed, "stdout must contain exactly one JSON line")
        try:
            raw = json.loads(lines[0])
            response = validate_response(raw, task_id)
        except (json.JSONDecodeError, ProtocolError) as exc:
            return AdapterResult(_error_response(task_id), elapsed, f"protocol error: {exc}")
        return AdapterResult(response, elapsed)


def _error_response(task_id: str) -> dict[str, Any]:
    return {
        "protocol_version": PROTOCOL_VERSION,
        "task_id": task_id,
        "answer": None,
        "harness_accepted": False,
        "attempts": 1,
        "verification_responsive": None,
        "usage": None,
    }
