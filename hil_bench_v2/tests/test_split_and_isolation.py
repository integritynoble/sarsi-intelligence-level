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

from hilbench import c_items, common, split
from hilbench.__main__ import _selected_seeds


class DeterministicSplitTests(unittest.TestCase):
    def test_public_split_is_stable_unique_and_reserved(self):
        self.assertEqual(split.PUBLIC_SEEDS, [0, 1, 2, 3, 4, 5])
        self.assertEqual(len(split.PUBLIC_SEEDS), len(set(split.PUBLIC_SEEDS)))
        self.assertTrue(all(seed < 1000 for seed in split.PUBLIC_SEEDS))

    def test_private_derivation_is_reproducible_and_domain_separated(self):
        salt = bytes(range(32))
        first = split.private_seeds(salt, n=16, family="alpha")
        self.assertEqual(first, split.private_seeds(salt, n=16, family="alpha"))
        self.assertNotEqual(first, split.private_seeds(salt, n=16, family="beta"))
        self.assertEqual(len(first), 16)
        self.assertEqual(len(first), len(set(first)))
        self.assertTrue(all(1000 <= seed < 1_001_000 for seed in first))
        self.assertTrue(set(first).isdisjoint(split.PUBLIC_SEEDS))

    def test_commitment_accepts_only_the_committed_salt(self):
        salt = b"correct private evaluator salt"
        with tempfile.TemporaryDirectory() as directory:
            commitment_file = Path(directory) / "commitment.json"
            commitment_file.write_text(
                json.dumps({"commitment": split.commitment(salt)}), encoding="utf-8"
            )
            with mock.patch.object(split, "COMMITMENT_FILE", commitment_file):
                self.assertTrue(split.check_commitment(salt))
                self.assertFalse(split.check_commitment(b"wrong salt"))

            published = commitment_file.read_text(encoding="utf-8")
            self.assertNotIn(salt.decode(), published)
            self.assertIn("sha256:", published)

    def test_private_selection_requires_a_matching_commitment(self):
        salt = b"held by evaluator only"
        with tempfile.TemporaryDirectory() as directory:
            salt_file = Path(directory) / "salt.bin"
            commitment_file = Path(directory) / "commitment.json"
            salt_file.write_bytes(salt)
            commitment_file.write_text(
                json.dumps({"commitment": split.commitment(salt)}), encoding="utf-8"
            )
            with mock.patch.object(split, "COMMITMENT_FILE", commitment_file):
                seeds = _selected_seeds("private", str(salt_file))
                self.assertEqual(seeds, split.private_seeds(salt))

                salt_file.write_bytes(b"not the committed value")
                with self.assertRaisesRegex(ValueError, "does not match"):
                    _selected_seeds("private", str(salt_file))

    def test_public_selection_never_reads_a_supplied_salt_path(self):
        with mock.patch.object(Path, "read_bytes", side_effect=AssertionError("salt read")):
            self.assertEqual(_selected_seeds("public", "/must/not/be/read"), split.PUBLIC_SEEDS)

    def test_hidden_key_is_not_written_into_executor_workspace(self):
        private_seed = split.private_seeds(b"workspace isolation salt", n=1)[0]
        files, key = c_items.generate(private_seed, "C3")
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            common.write_workspace(workspace, files)
            self.assertEqual(
                sorted(path.name for path in workspace.iterdir()), sorted(files)
            )
            self.assertFalse((workspace / "key.json").exists())
            self.assertNotIn("naive_name", (workspace / "GOAL.md").read_text(encoding="utf-8"))
            self.assertIn("key", key)


if __name__ == "__main__":
    unittest.main()
