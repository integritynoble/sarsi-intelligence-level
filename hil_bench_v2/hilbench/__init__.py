"""HIL-Bench v0.2 -- the Unified Agent Benchmark (HIL).

One instrument, two subjects, six coordinates:

  * an AGENT is measured as the frozen model-harness pair it is and gets a per-coordinate
    profile [C, I, O, T, H, SA] with M beside I, the gated Unified level U*, and the
    continuous pair score HLIS;
  * an LLM is measured through the reference harnesses HG0/HG1/HG2 built into this package
    and gets, at each rung, every coordinate plus the rung score HLIS_DI, and from the
    curve HIL-Level, HIL-AUC, HIL-Ceiling, Harnessability, Memory, and HIL-Score.

v0.2 over v0.1:
  * the Organizational coordinate O is bound. O0 (routing: functional decomposition of a
    task across separated roles with per-role evidence and an explicit anti-rubber-stamp
    statement) and O1 (persistent organizational memory: a standing routing decision is
    recorded in a harness-held registry and recalled, not guessed, in a later episode;
    the floor is the ablated arm with the registry withheld).
  * the profile and the HLIS now include O.
  * the LLM-mode HIL score is unified across the two subjects: the same six coordinates
    are measured in both modes, the same family set, the same seeds.

Every family is seeded. Public seeds ship with keys; private seeds are derived from a
withheld salt whose commitment is published (ARC-AGI-style). Standard library only.
"""
import sys
from pathlib import Path
UAB = Path(__file__).resolve().parents[2] / "uab_v01"
if str(UAB) not in sys.path:
    sys.path.insert(0, str(UAB))

VERSION = "HIL-Bench v0.2"
QWEN_TAG = ("Qwenps -- Qwen 3.8 27B (local) ran the benchmark's selftest and the "
            "reference-LLM smoke record of this release.")
