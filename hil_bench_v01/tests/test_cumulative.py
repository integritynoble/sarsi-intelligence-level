from __future__ import annotations
import sys, unittest
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
if str(PKG) not in sys.path: sys.path.insert(0, str(PKG))
from hilbench import cells, laws, score

class TypedCumulativeTests(unittest.TestCase):
    def test_every_ladder_has_a_type(self):
        for c in cells.CELLS: self.assertIn(c["cumulative_type"], ("hard_capability","hard_capability_from_SA1","cumulative_diagnostic","cumulative_frontier","ordered_axis","cumulative_engineering"), c["cell"])
    def test_axes_carry_no_retention_and_capability_ladders_do(self):
        for c in cells.CELLS:
            syms = [f["symbol"] for f in c["factors"]]
            if c["ladder"] in ("T", "H"): self.assertNotIn("K", syms, c["cell"]); self.assertEqual(c["retention"], "")
            elif c["cell"] in ("SA0", "SA1", "SA-cal") or c["cell"].endswith("0") and c["ladder"] != "DI": self.assertNotIn("K", syms, c["cell"])
            elif c["ladder"] == "DI": self.assertIn("K_T", syms)
            else: self.assertIn("K", syms, c["cell"]); self.assertTrue(c["retention"], c["cell"])
    def test_gp_is_cumulative_and_never_promotes(self):
        for c in cells.CELLS:
            if c["ladder"] == "GP":
                self.assertIn("¬promote", [f["symbol"] for f in c["factors"]]); 
                if c["cell"] != "GP0": self.assertIn("K", [f["symbol"] for f in c["factors"]])
    def test_frontier_cannot_leap_a_failed_band(self):
        ok = lambda b: {"band": b, "delivered_correct": True, "false_completion": False}
        bad = lambda b: {"band": b, "delivered_correct": False, "false_completion": True}
        eps = [ok("T0")] * 5 + [bad("T1")] * 5 + [ok("T2")] * 5
        self.assertEqual(score.frontier_cumulative(eps), "T0")
        self.assertEqual(score.frontier_cumulative([ok("T0")] * 5 + [ok("T1")] * 5 + [ok("T2")] * 5), "T2")
        self.assertIsNone(score.frontier_cumulative([bad("T0")] * 5))
    def test_retention_rule_text(self):
        self.assertEqual(laws.retention_rule("T", "T3"), ""); self.assertEqual(laws.retention_rule("SA", "SA1"), ""); self.assertTrue(laws.retention_rule("SA", "SA3")); self.assertTrue(laws.retention_rule("HG", "HG2")); self.assertEqual(laws.retention_rule("HG", "HG0"), "")

if __name__ == "__main__":
    unittest.main()
