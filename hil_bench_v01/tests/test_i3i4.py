"""I3/I4 campaign gates and the Theta manifest, against the development dataset's examples."""
from __future__ import annotations
import copy, json, sys, unittest
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
if str(PKG) not in sys.path: sys.path.insert(0, str(PKG))
from hilbench import laws
from hilbench.i3i4_scoring import i3_gates, i4_gates, i5_gates, iomega_gates, memory_gates, i_certification_with_memory
DS = PKG / "dataset" / "dev_v0_4"

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
        base = {"psi_modification": {"psi_diff": 1, "within_scope": 1, "psi1_active": 1, "behavior_probe_passes": 1, "behavior_probe_total": 1, "behavior_threshold": 0.0},
                "validation": {"psi0_i3_passes": 2, "psi0_i3_total": 6, "psi1_i3_passes": 4, "psi1_i3_total": 6,
                               "minimum_meaningful_improvement": 0.2, "independent_promoter_accepts": 1},
                "regression": {"max_observed_drop": 0.0, "maximum_allowed_drop": 0.05},
                "retention": {"I0": 1, "I1": 1, "I2": 1, "I3": 1}}
        self.assertEqual(i4_gates(base)["z_I4"], 1)
        fixed_psi = copy.deepcopy(base); fixed_psi["psi_modification"]["psi_diff"] = 0
        self.assertEqual(i4_gates(fixed_psi)["z_I4"], 0, "repeated Theta changes from a fixed Psi remain I3")
        no_rise = copy.deepcopy(base); no_rise["validation"]["psi1_i3_passes"] = 2
        self.assertEqual(i4_gates(no_rise)["z_I4"], 0)

    def test_i4_v2_requires_an_agent_generated_change_shown_on_meta_behavior_probes(self):
        base = {"psi_modification": {"psi_diff": 1, "within_scope": 1, "psi1_active": 1, "agent_generated": 1,
                                     "behavior_probe_passes": 4, "behavior_probe_total": 5, "behavior_threshold": 0.75},
                "validation": {"psi0_i3_passes": 2, "psi0_i3_total": 6, "psi1_i3_passes": 4, "psi1_i3_total": 6,
                               "minimum_meaningful_improvement": 0.2, "independent_promoter_accepts": 1},
                "regression": {"max_observed_drop": 0.0, "maximum_allowed_drop": 0.05},
                "retention": {"I0": 1, "I1": 1, "I2": 1, "I3": 1}, "recursive_transitions": [{"agent_generated": 1, "active": 1, "externally_validated_improvement": 1}]}
        g = i4_gates(base); self.assertEqual((g["z_I4"], g["recursive_depth"]), (1, 1))
        human_written = copy.deepcopy(base); human_written["psi_modification"]["agent_generated"] = 0
        self.assertEqual(i4_gates(human_written)["z_I4"], 0, "an evaluator-written Psi1 establishes nothing about the individual")
        no_signature = copy.deepcopy(base); no_signature["psi_modification"]["behavior_probe_passes"] = 2
        self.assertEqual(i4_gates(no_signature)["z_I4"], 0, "the changed process must show on the probes")


class MemoryI5IOmegaTests(unittest.TestCase):
    def test_example_memory_result_passes_its_gate_and_needs_lower_retention(self):
        r = json.loads((DS / "examples" / "memory_result.example.json").read_text())
        self.assertEqual(memory_gates(r)["z_M"], 1)
        r2 = copy.deepcopy(r); r2["retention"]["M1"] = False
        self.assertEqual(memory_gates(r2)["z_M"], 0, "memory levels are cumulative")

    def test_memory_can_gate_but_never_promote_i(self):
        self.assertEqual(i_certification_with_memory("I2", True, "M3")["certified"], 1)
        self.assertEqual(i_certification_with_memory("I2", True, "M1")["certified"], 0, "I2 needs M3")
        self.assertEqual(i_certification_with_memory("I2", False, "MΩ")["certified"], 0, "high M never promotes I")
        self.assertEqual(i_certification_with_memory("IΩ", True, "M5")["required_M"], "M5")
        self.assertEqual(i_certification_with_memory("IΩ", True, "M5", memory_architecture_evolution_claim=True)["certified"], 0)

    def test_i5_incorporation_gate_separates_discovery_from_storage(self):
        r = json.loads((DS / "examples" / "i5_result.example.json").read_text())
        self.assertEqual(i5_gates(r)["z_I5"], 1)
        stored = copy.deepcopy(r); stored["incorporation"]["discovery_successes"] = stored["incorporation"]["control_successes"]
        self.assertEqual(i5_gates(stored)["P"], 0, "a stored discovery that changes nothing after restart does not pass P")

    def test_iomega_needs_repeated_causal_frontier_expansion(self):
        r = json.loads((DS / "examples" / "iomega_result.example.json").read_text())
        g = iomega_gates(r); self.assertEqual(g["z_IOmega"], 1)
        one = copy.deepcopy(r); one["cycles"] = one["cycles"][:1]
        self.assertEqual(iomega_gates(one)["z_IOmega"], 0, "one instrument is not IOmega")
        no_cause = copy.deepcopy(r)
        for c in no_cause["cycles"]: c["ablation_successes"] = c["post_successes"]
        self.assertEqual(iomega_gates(no_cause)["z_IOmega"], 0, "the instrument must contribute causally")

if __name__ == "__main__":
    unittest.main()
