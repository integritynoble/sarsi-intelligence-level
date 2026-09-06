from __future__ import annotations
import sys, unittest
from pathlib import Path
import numpy as np
PKG = Path(__file__).resolve().parents[1]
if str(PKG) not in sys.path: sys.path.insert(0, str(PKG))
from hilbench import index_sim as S, latent

class EstimatorTests(unittest.TestCase):
    def test_the_fast_fit_agrees_with_the_package_estimator(self):
        rng = np.random.default_rng(0); theta = rng.normal(0, 1, 6); b = rng.normal(0, 1.2, 60)
        Y = S.responses(theta, b, None, rng)
        th, bb, se, keep = S.fit(Y)
        obs = {(f"m{m}", f"i{i}"): float(Y[m, i]) for m in range(Y.shape[0]) for i in range(Y.shape[1])}
        th2, b2, se2, dropped = latent.fit_rasch(obs)
        a = np.array([th2[f"m{m}"] for m in range(len(theta))]); a -= a.mean()
        c = th - th.mean()
        self.assertGreater(float(np.corrcoef(a, c)[0, 1]), 0.999)
        self.assertLess(float(np.max(np.abs(a - c))), 0.05)
    def test_more_items_buy_a_tighter_interval_and_a_better_ordering(self):
        few = S.recovery(12, 40, reps=8, seed=1); many = S.recovery(12, 320, reps=8, seed=1)
        self.assertGreater(many["spearman"], few["spearman"]); self.assertLess(many["median_se"], few["median_se"])
    def test_neighbour_separation_falls_as_the_population_grows(self):
        """The finding the resolution law formalizes: at fixed evidence, more models means fewer separable neighbours."""
        small = S.recovery(4, 320, reps=10, seed=2); large = S.recovery(20, 320, reps=10, seed=2)
        self.assertGreater(small["adjacent_pairs_separated"], large["adjacent_pairs_separated"])
        self.assertGreaterEqual(large["spearman"], 0.95)   # the ordering is still good; it is the resolution that is gone
    def test_frozen_anchors_hold_published_scores_still(self):
        d = S.equating_drift(reps=8)
        self.assertLess(d["drift_frozen_anchors"], d["drift_free_recalibration"])
    def test_a_fixed_suite_loses_discrimination_as_the_frontier_advances(self):
        rows = S.saturation(years=5, reps=6)
        self.assertGreater(rows[0]["separation_fixed"], rows[-1]["separation_fixed"])
        self.assertGreater(rows[-1]["separation_refreshed"], rows[-1]["separation_fixed"])
    def test_the_net_primitive_can_reverse_a_success_only_order(self):
        b = S.bluff_pricing(grid=9)
        self.assertGreater(b["share_where_net_reverses_the_order"], 0.0)
    def test_linking_needs_common_items_not_complete_coverage(self):
        m = {r["coverage"]: r for r in S.coverage_study(reps=10)}
        blk = [v for k, v in m.items() if k.startswith("blocked")][0]
        dis = [v for k, v in m.items() if k.startswith("disjoint")][0]
        comp = m["complete"]
        # a gap that keeps common items is survivable; a gap with no shared item is not
        self.assertGreater(blk["spearman"], dis["spearman"])
        self.assertLess(abs(blk["spearman"] - comp["spearman"]), 0.08)
        # and the models that skipped are placed with a wider interval, not a confident wrong number
        self.assertGreater(blk["median_se_partial_models"], comp["median_se"])

if __name__ == "__main__":
    unittest.main()
