"""`ailevel` is the public name of the instrument (the Artificial Intelligence Level, formerly the Harness Intelligence
Level).  The implementation lives in `hilbench`, whose name is kept for the archived records and tests; this package
re-exports it so `python3 -m ailevel ...` and `import ailevel` are the same instrument under its current name."""
import sys as _sys, hilbench as _h
from hilbench import *          # noqa: F401,F403
_sys.modules.setdefault("ailevel.core", _h.core if hasattr(_h, "core") else None)
