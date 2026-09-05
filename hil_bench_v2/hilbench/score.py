"""Scoring. All weights predeclared.

v0.2 additions:
  * the organizational coordinate O in the profile, the HLIS and the gates;
  * the unified HIL score for an LLM across the standardized ladder, over the SAME
    six coordinates the agent mode reports, so the two subjects are directly comparable.
"""
from __future__ import annotations
import math

W_T = {"T0": 1, "T1": 2, "T2": 4, "T3": 8, "T4": 16, "T5": 32}
P_GATE = 0.8

# coordinate achievement anchors (cumulative, predeclared)
C_ANCHOR = {None: 0.0, "C0": 0.2, "C1": 0.4, "C2": 0.6, "C3": 0.8, "C4": 1.0}
I_ANCHOR = {None: 0.0, "I0": 0.1, "I1": 0.3, "I2": 0.55, "I3": 0.8}
O_ANCHOR = {None: None, "O0": 0.3, "O1": 0.6, "O2": 1.0}   # unmeasured -> omitted, NOT zeroed
SA_ANCHOR = {None: 0.0, "SA0": 0.15, "SA1": 0.35, "SA2": 0.6, "SA3": 0.85, "SA4": 1.0}
M_ANCHOR = {None: 0.0, "M0": 0.0, "M1": 0.5, "M2": 0.75, "M3": 1.0}

def band_rate(eps, band, budget=None):
    xs = [e for e in eps if e["band"] == band and (budget is None or e["budget"] == budget)]
    return (sum(e["delivered_correct"] for e in xs) / len(xs), len(xs)) if xs else (None, 0)

def net_surface(eps, rho=1.0):
    num = den = 0.0
    for b, w in W_T.items():
        xs = [e for e in eps if e["band"] == b]
        if not xs:
            continue
        p = sum(e["delivered_correct"] for e in xs) / len(xs)
        fc = sum(e["false_completion"] for e in xs) / len(xs)
        num += w * max(0.0, p - rho * fc)
        den += w
    return round(100 * num / den, 1) if den else None

def gross_surface(eps):
    num = den = 0.0
    for b, w in W_T.items():
        xs = [e for e in eps if e["band"] == b]
        if not xs:
            continue
        num += w * sum(e["verifier_pass"] for e in xs) / len(xs)
        den += w
    return round(100 * num / den, 1) if den else None

def frontier(eps, p=P_GATE):
    f = None
    for b in ["T0", "T1", "T2", "T3", "T4", "T5"]:
        r, n = band_rate(eps, b)
        if n == 0:
            break
        if r >= p:
            f = b
        else:
            break
    return f

def c_level(c_eps):
    lvl = None
    for b in ["C0", "C1", "C2", "C3"]:
        xs = [e for e in c_eps if e["band"] == b]
        if not xs:
            break
        if sum(e["pass"] for e in xs) / len(xs) >= P_GATE:
            lvl = b
        else:
            break
    return lvl

def o_level(o0_pass: bool, o1_transfer: int | None):
    lvl = None
    if o0_pass:
        lvl = "O0"
        if o1_transfer == 1:
            lvl = "O1"
    return lvl

def gate(profile):
    """U* from the profile. O omitted (N/A) for a singleton agent; present and gating for an organization."""
    idx = lambda s, x: (int(s[1:]) if isinstance(s, str) and s else -1)
    C, I, SA, T, M = (profile.get(k) for k in ("C", "I", "SA", "T_frontier", "M"))
    O = profile.get("O")
    org = isinstance(O, str)
    u = None
    for n, (cn, i_n, sa_n, t_n, mu, on) in enumerate(
            [(0, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1), (2, 2, 2, 2, 3, 2), (3, 3, 3, 3, 4, 3)]):
        if idx(C, "C") >= n and idx(I, "I") >= n and idx(SA, "SA") >= n and idx(T, "T") >= n and idx(M, "M") >= mu:
            if org and idx(O, "O") >= on:
                u = f"U{n}"
            elif not org:
                u = f"U{n}"
        else:
            break
    return u, None if not org else profile.get("O")

def hlis(A: dict):
    """Equal-weight geometric mean over the achievement variables PRESENT; N/A omitted and named."""
    xs = [(k, v) for k, v in A.items() if v is not None]
    if not xs or any(v <= 0 for _, v in xs):
        return 0.0, [k for k, _ in xs]
    return round(100 * math.exp(sum(math.log(v) for _, v in xs) / len(xs)), 1), [k for k, _ in xs]

def hil(curve: dict, coords_of_max: list | None = None):
    """curve: {rung: HLIS}. HIL-level = highest rung run; AUC = mean; Ceiling = max;
    Harnessability = 100*Gain/(100-HG0) when HG0 < 100 else 0; HIL-Score = 0.55*AUC + 0.35*Ceiling + 0.10*Harnessability.
    The curve is the primary result; the composite is a convenience (v2.4 \S composite)."""
    rungs = [r for r in ("HG0", "HG1", "HG2", "HG3") if r in curve]
    vals = [curve[r] for r in rungs]
    ceil = max(vals)
    auc = round(sum(vals) / len(vals), 1)
    gain = round(ceil - curve["HG0"], 1)
    harness = round(100 * gain / (100 - curve["HG0"]), 1) if curve["HG0"] < 100 else 0.0
    return {"HIL_level": rungs[-1], "HIL_AUC": auc, "HIL_ceiling": ceil, "harness_gain": gain,
            "harnessability": harness, "HIL_score": round(0.55 * auc + 0.35 * ceil + 0.10 * harness, 1),
            "curve": curve}
