from __future__ import annotations
import sys, unittest
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
if str(PKG) not in sys.path: sys.path.insert(0, str(PKG))
from hilbench import laws

class SchemaTests(unittest.TestCase):
    def test_every_law_carries_factors_control_and_prereq(self):
        for k, v in laws.LAWS.items():
            self.assertTrue(v.get("factors"), k); self.assertTrue(v.get("control"), k); self.assertIn("prereq", v, k)
    def test_retention_is_a_factor_of_every_level_above_the_floor(self):
        floors = {"C0", "SA-cal", "O0"}
        for k, v in {**laws.LAWS, **{kk: vv for kk, vv in laws.LADDERS.items() if not kk.startswith("H")}}.items():
            if k in floors or k in ("HG0",): continue
            self.assertEqual(v["factors"][-1], "K", k)
    def test_every_ladder_is_present_in_one_form(self):
        want = ["C6", "COmega", "SA5", "SA6", "SAOmega", "O3", "O4", "O5", "OOmega", "T0", "T6", "TOmega", "H0", "H5", "HG0", "HG3", "HG6", "HGOmega", "U0", "U6", "UOmega"]
        for k in want: self.assertIn(k, laws.LADDERS, k)
        self.assertEqual(laws.LADDERS["HG0"]["factors"], ["E"])
    def test_gate_is_a_product_and_an_absent_factor_is_zero(self):
        f = laws.LAWS["I3"]["factors"]
        self.assertTrue(laws.factor_gate({x: True for x in f}, f)); self.assertFalse(laws.factor_gate({x: True for x in f[:-1]}, f))
        self.assertFalse(laws.factor_gate({**{x: True for x in f}, "V": False}, f))

if __name__ == "__main__":
    unittest.main()
