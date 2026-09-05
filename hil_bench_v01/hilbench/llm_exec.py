"""Runnable alias: python3 -m hilbench.llm_exec ...  The implementation lives in hilbench.llm."""
import sys
from .llm import *  # noqa: F401,F403
from .llm import _parse, _call, run, main  # noqa: F401
if __name__ == "__main__":
    sys.exit(main())
