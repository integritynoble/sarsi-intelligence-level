from __future__ import annotations
import sys, unittest, random
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
if str(PKG) not in sys.path: sys.path.insert(0, str(PKG))
from hilbench import latent

class RaschTests(unittest.TestCase):
    def test_recovers_ordering_and_drops_uninformative_items(self):
        rnd = random.Random(0); true = {"strong": 1.5, "mid": 0.0, "weak": -1.5}; obs = {}
        for i in range(60):
            b = rnd.uniform(-2, 2)
            for m, th in true.items(): obs[(m, f"it{i}")] = int(rnd.random() < 1 / (1 + 2.718281828 ** -(th - b)))
        for m in true: obs[(m, "everyone_passes")] = 1
        theta, b, se, dropped = latent.fit_rasch(obs)
        self.assertIn("everyone_passes", dropped)
        self.assertGreater(theta["strong"], theta["mid"]); self.assertGreater(theta["mid"], theta["weak"])
        self.assertAlmostEqual(sum(b.values()) / len(b), 0.0, places=6)
    def test_index_is_unbounded_and_carries_an_interval(self):
        R = {"rungs": {"HG0": {"episodes": [{"family": "f", "seed": 0, "delivered_correct": True}, {"family": "g", "seed": 0, "delivered_correct": False}],
                              "C": [{"band": "C0", "seed": 0, "pass": True}], "SA1": [{"seed": 0, "pass": True}], "SA2": [{"seed": 0, "pass": False}], "O0": {"pass": True}}}}
        R2 = {"rungs": {"HG0": {"episodes": [{"family": "f", "seed": 0, "delivered_correct": False}, {"family": "g", "seed": 0, "delivered_correct": False}],
                               "C": [{"band": "C0", "seed": 0, "pass": False}], "SA1": [{"seed": 0, "pass": False}], "SA2": [{"seed": 0, "pass": False}], "O0": {"pass": False}}}}
        out = latent.latent_index([("a", R), ("b", R2)])
        self.assertGreater(out["models"]["a"]["HILIndex_latent"], out["models"]["b"]["HILIndex_latent"])
        self.assertEqual(len(out["models"]["a"]["HILIndex_latent_ci95"]), 2); self.assertIn("DIAGNOSTIC", out["scale"]["status"])

if __name__ == "__main__":
    unittest.main()
