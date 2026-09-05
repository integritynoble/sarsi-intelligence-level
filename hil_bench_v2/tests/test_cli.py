from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

from hilbench import split
from hilbench.__main__ import _parse_seed_spec, main


class CLITests(unittest.TestCase):
    def test_seed_spec_accepts_ranges_and_rejects_descending_range(self):
        self.assertEqual(_parse_seed_spec("0-2,7,9-10"), [0, 1, 2, 7, 9, 10])
        with self.assertRaises(Exception):
            _parse_seed_spec("3-1")

    def test_agent_subcommand_dispatches_public_seeds(self):
        with tempfile.TemporaryDirectory() as directory, mock.patch(
            "hilbench.__main__.core.run_agent"
        ) as run_agent:
            rc = main(
                [
                    "agent",
                    "--label",
                    "pair",
                    "--exec",
                    "runner --prompt {prompt}",
                    "--root",
                    directory,
                    "--limit",
                    "7",
                ]
            )
        self.assertEqual(rc, 0)
        run_agent.assert_called_once_with(
            "pair",
            "runner --prompt {prompt}",
            Path(directory),
            split.PUBLIC_SEEDS,
            7,
        )

    def test_agent_rejects_executor_without_prompt_placeholder(self):
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                main(
                    [
                        "agent",
                        "--label",
                        "pair",
                        "--exec",
                        "runner",
                        "--root",
                        directory,
                    ]
                )
        self.assertEqual(raised.exception.code, 2)

    def test_llm_subcommand_dispatches_endpoint_options(self):
        with tempfile.TemporaryDirectory() as directory, mock.patch(
            "hilbench.__main__.core.run_llm"
        ) as run_llm:
            rc = main(
                [
                    "llm",
                    "--label",
                    "model",
                    "--root",
                    directory,
                    "--base",
                    "http://model.invalid/v1",
                    "--key",
                    "test-key",
                    "--model",
                    "test-model",
                ]
            )
        self.assertEqual(rc, 0)
        run_llm.assert_called_once_with(
            "model",
            Path(directory),
            split.PUBLIC_SEEDS,
            120,
            base="http://model.invalid/v1",
            key="test-key",
            model="test-model",
        )

    def test_private_cli_dispatch_never_passes_salt_to_core_record(self):
        salt = b"evaluator-private-salt"
        with tempfile.TemporaryDirectory() as directory:
            salt_file = Path(directory) / "salt.bin"
            commitment_file = Path(directory) / "commitment.json"
            salt_file.write_bytes(salt)
            commitment_file.write_text(
                json.dumps({"commitment": split.commitment(salt)}), encoding="utf-8"
            )
            with (
                mock.patch.object(split, "COMMITMENT_FILE", commitment_file),
                mock.patch("hilbench.__main__.core.run_agent") as run_agent,
            ):
                rc = main(
                    [
                        "agent",
                        "--label",
                        "private-pair",
                        "--exec",
                        "runner {prompt}",
                        "--root",
                        str(Path(directory) / "run"),
                        "--split",
                        "private",
                        "--salt-file",
                        str(salt_file),
                    ]
                )
        self.assertEqual(rc, 0)
        positional = run_agent.call_args.args
        self.assertEqual(positional[3], split.private_seeds(salt))
        self.assertNotIn(salt, positional)
        self.assertNotIn(str(salt_file), positional)


if __name__ == "__main__":
    unittest.main()
