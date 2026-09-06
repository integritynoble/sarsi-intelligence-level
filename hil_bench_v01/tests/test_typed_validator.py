"""Prove the five rejections REFUSE, not only that the real dataset passes: break each rule on a copy and watch."""
from __future__ import annotations
import json, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PKG / "tools")); sys.path.insert(0, str(PKG))
import validate_dataset as V

def _copy(): d = Path(tempfile.mkdtemp()) / "ds"; shutil.copytree(PKG / "dataset" / "ail_v0_3", d); return d
def _edit(d, rel, level, **kv):
    p = d / rel; rows = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
    for r in rows:
        if r.get("level") == level: r.update(kv)
    p.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n")

class TypedValidatorTests(unittest.TestCase):
    def test_real_dataset_passes(self): self.assertEqual(V.typed_cumulative_rules(PKG / "dataset" / "ail_v0_3"), [])
    def test_i_gp_missing_lower(self):
        d = _copy(); _edit(d, "public/gui_screen.jsonl", "GP3", required_lower_levels=["GP0", "GP2"]); self.assertTrue(any("(i)" in x for x in V.typed_cumulative_rules(d)))
    def test_ii_t_record_with_retention(self):
        d = _copy(); _edit(d, "public/task_difficulty.jsonl", "T2", required_lower_levels=["T0", "T1"]); self.assertTrue(any("(ii)" in x for x in V.typed_cumulative_rules(d)))
        d = _copy(); _edit(d, "public/human_intervention.jsonl", "H2", cumulative_type="hard_capability"); self.assertTrue(any("(ii)" in x for x in V.typed_cumulative_rules(d)))
    def test_iii_frontier_without_retention_law(self):
        d = _copy(); _edit(d, "DI_Bench/Surface/public_forms.jsonl", "DI-surface", retention_rule="none"); self.assertTrue(any("(iii)" in x for x in V.typed_cumulative_rules(d)))
    def test_iv_gp_claims_promotion(self):
        d = _copy(); _edit(d, "public/gui_screen.jsonl", "GP5", promotes="C^GUI"); self.assertTrue(any("(iv)" in x for x in V.typed_cumulative_rules(d)))
    def test_v_hg_missing_prior_rung(self):
        d = _copy(); _edit(d, "public/harness_generation.jsonl", "HG2", required_lower_levels=["HG0"]); self.assertTrue(any("(v)" in x for x in V.typed_cumulative_rules(d)))

if __name__ == "__main__":
    unittest.main()
