from __future__ import annotations
import sys, unittest
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
if str(PKG) not in sys.path: sys.path.insert(0, str(PKG))
sys.path.insert(0, str(PKG / "tools"))
import validate_dataset

class DevDatasetTests(unittest.TestCase):
    def test_development_dataset_validates(self):
        self.assertEqual(validate_dataset.validate(PKG / "dataset" / "ail_v0_4"), [])

if __name__ == "__main__":
    unittest.main()
