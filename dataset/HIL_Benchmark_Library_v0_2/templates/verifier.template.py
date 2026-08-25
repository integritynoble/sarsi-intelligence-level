#!/usr/bin/env python3
"""Minimal HIL verifier template.

The verifier must run outside the candidate agent's write scope.
Replace `evaluate()` with benchmark-specific checks. Never trust a candidate's
self-reported success flag as the verdict.
"""
import json
import sys
from pathlib import Path

def evaluate(candidate_path: Path, hidden_reference_path: Path):
    candidate = json.loads(candidate_path.read_text())
    reference = json.loads(hidden_reference_path.read_text())
    passed = candidate == reference
    return {"pass": passed, "score": 1.0 if passed else 0.0}

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: verifier.py candidate.json hidden_reference.json")
    result = evaluate(Path(sys.argv[1]), Path(sys.argv[2]))
    print(json.dumps(result))
