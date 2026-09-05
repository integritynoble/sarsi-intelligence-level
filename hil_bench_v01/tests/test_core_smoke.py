from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

from hilbench import core, harness


class FakeExecutor:
    """In-process executor double: deterministic, offline, and intentionally weak."""

    def __init__(self) -> None:
        self.calls: list[dict] = []

    def __call__(self, command, prompt, cwd, limit, env=None):
        workspace = Path(cwd)
        self.calls.append(
            {
                "command": command,
                "prompt": prompt,
                "cwd": workspace,
                "limit": limit,
            }
        )
        # Exercise forecast ingestion while leaving task deliverables absent.
        if "forecast.json" in prompt:
            (workspace / "forecast.json").write_text(
                json.dumps({"p_pass": 0.25}), encoding="utf-8"
            )
        return {
            "exit": 0,
            "termination_reason": "normal",
            "seconds": 0.0,
            "stdout_tail": "FAKE",
        }


class CoreOfflineSmokeTests(unittest.TestCase):
    def _patch_executor(self, fake: FakeExecutor):
        return mock.patch.multiple(core, run_exec=fake, TH=["funding_t0"])

    def test_agent_core_completes_and_persists_a_record_with_fake_executor(self):
        fake = FakeExecutor()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "agent-run"
            with self._patch_executor(fake), mock.patch.object(harness, "run_exec", fake):
                record = core.run_agent(
                    "offline-agent-smoke",
                    "fake-executor {prompt}",
                    root,
                    [1],
                    limit=1,
                    log=lambda _message: None,
                )

            self.assertEqual(record["mode"], "agent")
            self.assertEqual(record["label"], "offline-agent-smoke")
            self.assertIn("profile", record)
            self.assertIn("HLIS", record["profile"])
            self.assertGreater(len(fake.calls), 0)
            persisted = json.loads((root / "record.json").read_text(encoding="utf-8"))
            self.assertEqual(persisted["profile"], record["profile"])

    def test_llm_core_runs_every_reference_rung_without_network(self):
        fake = FakeExecutor()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "llm-run"
            with (
                self._patch_executor(fake),
                mock.patch.object(harness, "run_exec", fake),
                mock.patch.object(core, "_llm_exec_tmpl", return_value="fake-llm {prompt}"),
            ):
                record = core.run_llm(
                    "offline-llm-smoke",
                    root,
                    [1],
                    limit=1,
                    log=lambda _message: None,
                )

            self.assertEqual(record["mode"], "llm")
            self.assertEqual(set(record["rungs"]), {"HG0", "HG1", "HG2"})
            self.assertEqual(set(record["HIL"]["curve"]), {"HG0", "HG1", "HG2"})
            self.assertGreater(len(fake.calls), 0)
            persisted = json.loads((root / "record.json").read_text(encoding="utf-8"))
            self.assertEqual(persisted["HIL"], record["HIL"])


if __name__ == "__main__":
    unittest.main()
