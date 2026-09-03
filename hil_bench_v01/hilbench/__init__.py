"""HIL-Bench v0.1 -- the Harness Intelligence Level benchmark.

One instrument measures two things:
  * an AGENT, as the frozen model-harness pair it is: a per-coordinate profile [C, I, O, T, H, SA] with M
    beside I, the gated Unified level U*, and the continuous pair score HLIS;
  * an LLM, through reference harnesses HG0/HG1/HG2 built into this package: HLIS at each rung, and
    from them HIL-Level, HIL-AUC, HIL-Ceiling, Harness Gain and HIL-Score.

Every family is seeded. Public seeds ship with keys; private seeds are derived from a withheld salt whose
commitment is published. Standard library only; the domain families are imported from ../uab_v01.
"""
import sys
from pathlib import Path
UAB = Path(__file__).resolve().parents[2] / "uab_v01"
if str(UAB) not in sys.path:
    sys.path.insert(0, str(UAB))
