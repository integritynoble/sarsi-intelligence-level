"""I3/I4 campaign gates and the Theta manifest, against the development dataset's examples."""
from __future__ import annotations
import copy, json, sys, unittest
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
if str(PKG) not in sys.path: sys.path.insert(0, str(PKG))
from hilbench import laws
from hilbench.i3i4_scoring import i3_gates, i4_gates
DS = PKG / "dataset" / "dev_v0_1"

class ThetaManifestTests(unittest.TestCase):
    def test_example_manifest_passes_every_manifest_level_check(self):
        m = json.loads((DS / "examples" / "theta_manifest.example.json").read_text())
        m.update({"persists_across_restart": True, "ablation_delta": None, "psi_paths": []})
        checks = dict((n, ok) for n, ok, _ in laws.theta_check(m, ["/hidden/eval", "/hidden/verifier"]))
        for name in ("theta_nonempty", "theta_persists_across_restart", "theta_disjoint_from_criterion", "psi_declared", "manifest_entries_complete"):
            self.assertTrue(checks[name], name)
        self.assertFalse(checks["theta_causally_efficacious"], "efficacy is proven by a run, never by a manifest")

    def test_manifest_overlapping_the_criterion_is_refused(self):
        m = json.loads((DS / "examples" / "theta_manifest.example.json").read_text())
        m.update({"persists_across_restart": True, "ablation_delta": 0.2, "psi_paths": []})
        m["theta_components"][0]["write_scope"] = ["/hidden/eval/suite"]
        checks = dict((n, ok) for n, ok, _ in laws.theta_check(m, ["/hidden/eval"]))
        self.assertFalse(checks["theta_disjoint_from_criterion"])

class I3I4GateTests(unittest.TestCase):
    def setUp(self):
        self.ex = json.loads((DS / "examples" / "i3_result.example.json").read_text())

    def test_example_campaign_passes_and_factors_match_hand_computation(self):
        g = i3_gates(self.ex)
        self.assertEqual((g["D"], g["M_theta"], g["V"], g["G"], g["K"], g["z_I3"]), (1, 1, 1, 1, 1, 1))
        self.assertAlmostEqual(g["delta_theta"], 0.25)
        self.assertAlmostEqual(g["behavior_rate"], 0.9)

    def test_each_factor_can_fail_the_campaign_alone(self):
        for path, value in ((("diagnosis", "causal_test_pass"), 0), (("modification", "theta1_active"), 0),
                            (("validation", "independent_promoter_accepts"), 0), (("regression", "max_observed_drop"), 0.5),
                            (("retention", "I2"), 0)):
            r = copy.deepcopy(self.ex); r[path[0]][path[1]] = value
            self.assertEqual(i3_gates(r)["z_I3"], 0, path)

    def test_a_no_op_change_cannot_pass(self):
        r = copy.deepcopy(self.ex); r["modification"]["artifact_diff"] = 0
        self.assertEqual(i3_gates(r)["M_theta"], 0)

    def test_i4_requires_the_process_to_change_and_the_i3_rate_to_rise(self):
        base = {"psi_modification": {"psi_diff": 1, "within_scope": 1, "psi1_active": 1},
                "validation": {"psi0_i3_passes": 2, "psi0_i3_total": 6, "psi1_i3_passes": 4, "psi1_i3_total": 6,
                               "minimum_meaningful_improvement": 0.2, "independent_promoter_accepts": 1},
                "regression": {"max_observed_drop": 0.0, "maximum_allowed_drop": 0.05},
                "retention": {"I0": 1, "I1": 1, "I2": 1, "I3": 1}}
        self.assertEqual(i4_gates(base)["z_I4"], 1)
        fixed_psi = copy.deepcopy(base); fixed_psi["psi_modification"]["psi_diff"] = 0
        self.assertEqual(i4_gates(fixed_psi)["z_I4"], 0, "repeated Theta changes from a fixed Psi remain I3")
        no_rise = copy.deepcopy(base); no_rise["validation"]["psi1_i3_passes"] = 2
        self.assertEqual(i4_gates(no_rise)["z_I4"], 0)

if __name__ == "__main__":
    unittest.main()
