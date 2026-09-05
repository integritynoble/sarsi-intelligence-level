from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

from hilbench import score


def delegation_episode(
    band: str,
    *,
    correct: bool,
    false_completion: bool = False,
    verifier_pass: bool | None = None,
    budget: str = "H0",
) -> dict:
    return {
        "band": band,
        "budget": budget,
        "delivered_correct": correct,
        "false_completion": false_completion,
        "verifier_pass": correct if verifier_pass is None else verifier_pass,
    }


class CoordinateScoringTests(unittest.TestCase):
    def test_band_rate_honors_budget(self):
        episodes = [
            delegation_episode("T0", correct=True, budget="H0"),
            delegation_episode("T0", correct=False, budget="H1"),
        ]
        self.assertEqual(score.band_rate(episodes, "T0"), (0.5, 2))
        self.assertEqual(score.band_rate(episodes, "T0", "H0"), (1.0, 1))
        self.assertEqual(score.band_rate(episodes, "T1"), (None, 0))

    def test_net_surface_penalizes_false_completion(self):
        episodes = [
            delegation_episode("T0", correct=True),
            delegation_episode("T0", correct=False, false_completion=True),
            delegation_episode("T1", correct=True),
        ]
        self.assertEqual(score.net_surface(episodes), 66.7)
        self.assertEqual(score.gross_surface(episodes), 83.3)

    def test_frontier_is_cumulative_and_stops_at_first_failed_band(self):
        episodes = [
            *[delegation_episode("T0", correct=True) for _ in range(4)],
            delegation_episode("T0", correct=False),
            delegation_episode("T1", correct=True),
            *[delegation_episode("T2", correct=True) for _ in range(3)],
            delegation_episode("T2", correct=False),
        ]
        self.assertEqual(score.frontier(episodes), "T1")

    def test_frontier_does_not_skip_an_unmeasured_band(self):
        episodes = [
            delegation_episode("T0", correct=True),
            delegation_episode("T2", correct=True),
        ]
        self.assertEqual(score.frontier(episodes), "T0")

    def test_c_level_requires_lower_band_retention(self):
        passing = [
            {"band": band, "pass": True} for band in ("C0", "C1", "C2", "C3")
        ]
        self.assertEqual(score.c_level(passing), "C3")
        failing_middle = [dict(row) for row in passing]
        failing_middle[1]["pass"] = False
        self.assertEqual(score.c_level(failing_middle), "C0")

    def test_o_level_requires_base_routing_before_transfer(self):
        self.assertIsNone(score.o_level(False, 1))
        self.assertEqual(score.o_level(True, 0), "O0")
        self.assertEqual(score.o_level(True, 1), "O1")

    def test_unified_gate_applies_memory_and_organization_bottlenecks(self):
        profile = {
            "C": "C2",
            "I": "I2",
            "O": None,
            "SA": "SA2",
            "T_frontier": "T2",
            "M": "M3",
        }
        self.assertEqual(score.gate(profile)[0], "U2")

        memory_limited = {**profile, "M": "M1"}
        self.assertEqual(score.gate(memory_limited)[0], "U1")

        organization_limited = {**profile, "O": "O1"}
        level, bottleneck = score.gate(organization_limited)
        self.assertEqual(level, "U1")
        self.assertEqual(bottleneck, "O1")

    def test_hlis_omits_na_but_does_not_omit_zero(self):
        value, dimensions = score.hlis({"C": 0.25, "I": 1.0, "O": None})
        self.assertEqual(value, 50.0)
        self.assertEqual(dimensions, ["C", "I"])

        value, dimensions = score.hlis({"C": 0.25, "I": 0.0, "O": None})
        self.assertEqual(value, 0.0)
        self.assertEqual(dimensions, ["C", "I"])


class HILScoringTests(unittest.TestCase):
    def test_hil_composite_preserves_ordered_curve_and_exact_components(self):
        result = score.hil({"HG0": 20.0, "HG1": 40.0, "HG2": 30.0})
        self.assertEqual(result["HIL_level"], "HG2")
        self.assertEqual(result["HIL_AUC"], 30.0)
        self.assertEqual(result["HIL_ceiling"], 40.0)
        self.assertEqual(result["harness_gain"], 20.0)
        self.assertEqual(result["harnessability"], 25.0)
        self.assertEqual(result["HIL_score"], 33.0)
        self.assertEqual(list(result["curve"]), ["HG0", "HG1", "HG2"])

    def test_hil_requires_a_contiguous_curve_starting_at_hg0(self):
        for curve in ({}, {"HG1": 20.0}, {"HG0": 10.0, "HG2": 30.0}):
            with self.subTest(curve=curve):
                with self.assertRaises(ValueError):
                    score.hil(curve)

    def test_hil_rejects_nonfinite_or_out_of_range_scores(self):
        for value in (-0.1, 100.1, math.nan, math.inf):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    score.hil({"HG0": value})


if __name__ == "__main__":
    unittest.main()
