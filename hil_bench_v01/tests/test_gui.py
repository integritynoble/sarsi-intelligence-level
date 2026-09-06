from __future__ import annotations
import sys, unittest, subprocess
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
if str(PKG) not in sys.path: sys.path.insert(0, str(PKG))
from hilbench import gui_laws, gui_scoring

class GuiTests(unittest.TestCase):
    def test_containment_and_no_promotion(self):
        # GP evidence is not an input to the C^GUI gate: a perfect GP profile with a failed C_k witness does not pass
        self.assertFalse(gui_laws.cgui_gate(False, True)); self.assertFalse(gui_laws.cgui_gate(True, False)); self.assertTrue(gui_laws.cgui_gate(True, True))
        self.assertTrue(set(gui_laws.GP_LEVELS).isdisjoint(gui_laws.CGUI_WITNESSES))
        self.assertIn("GUI/screen", gui_laws.DOMAIN_PANEL); self.assertEqual(len(gui_laws.DOMAIN_PANEL), 8)
    def test_failure_attribution_names_the_limiting_stage(self):
        r = gui_laws.failure_record(0.2, 0.9, 0.25); self.assertAlmostEqual(r["delta_GP"], 0.7); self.assertEqual(r["limit"], "perception")
        r = gui_laws.failure_record(0.3, 0.32, 0.9); self.assertEqual(r["limit"], "action")
        r = gui_laws.failure_record(0.3, 0.32, 0.33); self.assertEqual(r["limit"], "cognition")
        d = gui_scoring.failure_attribution(0.2, 0.9, 0.25); self.assertAlmostEqual(d["delta_GP"], 0.7)
    def test_dataset_v0_7_validates_with_the_gui_package(self):
        out = subprocess.run([sys.executable, str(PKG / "tools" / "validate_dataset.py"), str(PKG / "dataset" / "dev_v0_7")], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stdout + out.stderr)
        forms = (PKG / "dataset" / "dev_v0_7" / "C_Bench" / "GUI_SCREEN" / "public_forms.jsonl").read_text().splitlines()
        self.assertEqual(len(forms), 14)
    def test_ailevel_alias_is_the_same_instrument(self):
        import ailevel, hilbench
        self.assertIs(sys.modules["hilbench"], hilbench); self.assertTrue(hasattr(ailevel, "__doc__"))

if __name__ == "__main__":
    unittest.main()
