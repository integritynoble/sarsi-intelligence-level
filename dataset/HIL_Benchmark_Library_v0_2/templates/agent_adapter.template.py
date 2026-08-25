#!/usr/bin/env python3
"""Adapter interface for a model+harness system under HIL evaluation."""
from typing import Dict, Any

class HILAgentAdapter:
    def reset(self, task: Dict[str, Any]) -> None:
        """Start a fresh benchmark run under the declared harness."""
        raise NotImplementedError

    def act(self, observation: Dict[str, Any]) -> Dict[str, Any]:
        """Return one bounded action or final artifact."""
        raise NotImplementedError

    def snapshot(self) -> Dict[str, Any]:
        """Return auditable harness state allowed by the benchmark protocol."""
        raise NotImplementedError
