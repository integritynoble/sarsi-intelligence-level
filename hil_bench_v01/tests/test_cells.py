from __future__ import annotations
import sys, unittest, tempfile
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
if str(PKG) not in sys.path: sys.path.insert(0, str(PKG))
from hilbench import cells, h_ledger, hg_conform, laws

class GridTests(unittest.TestCase):
    def test_grid_is_complete_and_unique(self):
        ids = [c["cell"] for c in cells.CELLS]; self.assertEqual(len(ids), len(set(ids)))
        for want in ["C0","C5","CΩ","C3^GUI","GP5","I0","I5","IΩ","M0","MΩ","O0","OΩ","SA0","SA-cal","SAΩ","T0","T6","TΩ","H0","H5","DF","HG0","HG3","HGΩ","U0","U6","UΩ"]:
            self.assertIn(want, ids, want)
        self.assertEqual(set(c["ladder"] for c in cells.CELLS), set(cells.LADDERS))
    def test_every_cell_has_the_six_parts_and_a_control_arm(self):
        for c in cells.CELLS:
            for k in ("construct","prereq","witness","control_arm","factors","gate","law","key","status"): self.assertTrue(c[k], (c["cell"], k))
            for f in c["factors"]: self.assertIn(f["locus"], cells.LOCI, c["cell"])
            if c["prereq"] != "none" and c["ladder"] not in ("H","DI","GP"): self.assertEqual(c["factors"][-1]["symbol"], "K", c["cell"])
    def test_a_runs_cell_names_a_generator_that_resolves(self):
        for c in cells.CELLS:
            if c["status"] == "runs":
                self.assertTrue(c["generator"], c["cell"]); self.assertTrue(callable(cells.resolve(c["generator"])), c["cell"])
            if c["generator"]: cells.resolve(c["generator"])
    def test_status_is_about_the_package_not_the_level(self):
        n = cells.counts(); self.assertGreater(n["total"]["runs"], 20); self.assertGreater(n["total"]["specification"], 10)
    def test_the_grid_matches_the_laws(self):
        for k, v in laws.LAWS.items():
            if k == "DI": continue
            key = k.replace("Omega", "Ω"); self.assertIn(key, cells.by_cell(), k)

class HLedgerTests(unittest.TestCase):
    def test_content_classifies_not_count(self):
        self.assertEqual(h_ledger.h_class([]), "H0")
        self.assertEqual(h_ledger.h_class([{"kind": "unavailable_fact"}] * 9), "H1")
        self.assertEqual(h_ledger.h_class([{"kind": "unavailable_fact"}, {"kind": "strategy"}]), "H5")
        self.assertEqual(h_ledger.h_class([{"kind": "something_new"}]), "H5")
        self.assertTrue(h_ledger.within([{"kind": "local_correction"}], "H2")); self.assertFalse(h_ledger.within([{"kind": "periodic_review"}], "H2"))

class HGConformTests(unittest.TestCase):
    def test_rungs_are_certified_by_their_contrast_on_the_same_seed(self):
        with tempfile.TemporaryDirectory() as d:
            s = hg_conform.run_all(Path(d), seeds=(0, 1))
            self.assertGreater(s["HG1"]["witnesses"], 0, "no family whose trap is publicly visible: HG1 has nothing to hold back")
            for rung in ("HG0", "HG1", "HG2"): self.assertEqual(s[rung]["z_pass"], s[rung]["witnesses"], (rung, s))

if __name__ == "__main__":
    unittest.main()
