#!/usr/bin/env python3
"""HLIS v0.2 — the geometric mean, plus the delegation repair.

Two changes from v0.1.

**A_DI is computed net of false completions.** v0.1's A_DI is the weighted mean
of `P(verifier_pass)`. Acceptance does not change the probability of success; it
changes what is *reported* as success. So two harness generations differing only
in whether wrong work is handed back as done receive the same A_DI — which was
measured, not hypothesised: HG0 and HG1 produced an identical pass pattern and
differed entirely in false completions. A scaling curve built on P(success)
cannot see its own first rung.

    S_net(T,H) = P(verifier_pass) − ρ · P(false_completion)

with ρ from the class's own loss terms. A refusal costs human load and enters
nowhere in this expression; a confident wrong answer costs ρ.

**N/A dimensions are omitted, never zeroed.** v1.3 §13.11 says so for O on a
singleton, and this enforces it: a dimension with no evidence is dropped from D
and named in the output, so a missing suite cannot silently read as a failed one.
"""
from __future__ import annotations

import argparse
import json
import math
from typing import Dict, List, Optional, Tuple

W_T = {"T0": 1.0, "T1": 2.0, "T2": 4.0, "T3": 8.0, "T4": 16.0, "T5": 32.0,
       "T6": 64.0, "TOmega": 128.0}
V_H = {"H0": 6.0, "H1": 5.0, "H2": 4.0, "H3": 3.0, "H4": 2.0, "H5": 1.0}


def a_di(surface: Dict[str, Dict[str, float]],
         false_completion: Optional[Dict[str, Dict[str, float]]] = None,
         rho: float = 1.0, net: bool = True) -> float:
    """Weighted mean of the success surface, net of false completions."""
    num = den = 0.0
    for t, row in surface.items():
        for h, s in row.items():
            w = W_T.get(t, 1.0) * V_H.get(h, 1.0)
            v = float(s)
            if net and false_completion:
                v -= rho * float(false_completion.get(t, {}).get(h, 0.0))
            num += w * max(0.0, v)
            den += w
    return (num / den) if den else 0.0


def hlis(components: Dict[str, Optional[float]],
         weights: Optional[Dict[str, float]] = None) -> Tuple[float, List[str], List[str]]:
    """(score, dimensions used, dimensions omitted).

    A dimension whose value is None has no evidence and is OMITTED from D --
    it is not zero. A dimension that is genuinely zero does force the product to
    zero, which is the intended hard signal.
    """
    weights = weights or {}
    used, omitted = [], []
    for k, v in sorted(components.items()):
        w = float(weights.get(k, 1.0))
        if v is None or w <= 0:
            omitted.append(k)
            continue
        v = float(v)
        if not 0.0 <= v <= 1.0:
            raise ValueError("%s must be in [0,1], got %r" % (k, v))
        used.append((k, v, w))
    if not used:
        raise ValueError("no dimension has evidence; there is nothing to score")
    if any(v == 0.0 for _, v, _ in used):
        return 0.0, [k for k, _, _ in used], omitted
    num = sum(w * math.log(v) for _, v, w in used)
    den = sum(w for _, _, w in used)
    return 100.0 * math.exp(num / den), [k for k, _, _ in used], omitted


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--components", required=True,
                   help='JSON, e.g. {"C":0.9,"I":0.7,"DI":0.8,"SA":0.75,"O":null}')
    p.add_argument("--weights", default="{}")
    p.add_argument("--surface", default=None,
                   help='JSON {"T2":{"H1":0.9}} — computes DI from the surface')
    p.add_argument("--false-completion", dest="fc", default=None,
                   help='JSON in the same shape as --surface')
    p.add_argument("--rho", type=float, default=1.0)
    p.add_argument("--gross", action="store_true",
                   help="compute A_DI the v0.1 way, ignoring false completions")
    a = p.parse_args()

    comp = json.loads(a.components)
    if a.surface:
        surface = json.loads(a.surface)
        fc = json.loads(a.fc) if a.fc else None
        comp["DI"] = a_di(surface, fc, a.rho, net=not a.gross)
    score, used, omitted = hlis(comp, json.loads(a.weights))
    out = {"HLIS": round(score, 2), "dimensions_used": used,
           "dimensions_omitted_no_evidence": omitted,
           "A_DI_net_of_false_completion": not a.gross}
    if omitted:
        out["warning"] = ("%s omitted for want of evidence, not scored as zero. "
                          "A score over a subset is not comparable with one over "
                          "the full set." % ", ".join(omitted))
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
