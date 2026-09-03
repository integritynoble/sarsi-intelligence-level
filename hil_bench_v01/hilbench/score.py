"""Levels from readings; the gate; HLIS; HIL over the reference rungs. Weights predeclared."""
from __future__ import annotations
W_T = {"T0": 1, "T1": 2, "T2": 4, "T3": 8, "T4": 16, "T5": 32}
P_GATE = 0.8

def band_rate(eps, band, budget=None):
    xs = [e for e in eps if e["band"] == band and (budget is None or e["budget"] == budget)]
    return (sum(e["delivered_correct"] for e in xs) / len(xs), len(xs)) if xs else (None, 0)

def net_surface(eps, rho=1.0):
    """A_DI (net) over the T bands present, weights W_T; delivered-outcome primitive, clamped at 0."""
    num = den = 0.0
    for b, w in W_T.items():
        xs = [e for e in eps if e["band"] == b]
        if not xs: continue
        p = sum(e["delivered_correct"] for e in xs) / len(xs); fc = sum(e["false_completion"] for e in xs) / len(xs)
        num += w * max(0.0, p - rho * fc); den += w
    return round(100 * num / den, 1) if den else None

def gross_surface(eps):
    num = den = 0.0
    for b, w in W_T.items():
        xs = [e for e in eps if e["band"] == b]
        if not xs: continue
        num += w * sum(e["verifier_pass"] for e in xs) / len(xs); den += w
    return round(100 * num / den, 1) if den else None

def frontier(eps, p=P_GATE):
    f = None
    for b in ["T0", "T1", "T2", "T3", "T4", "T5"]:
        r, n = band_rate(eps, b)
        if n == 0: break
        if r >= p: f = b
        else: break
    return f

def c_level(c_eps):
    lvl = None
    for b in ["C0", "C1", "C2", "C3", "C4"]:
        xs = [e for e in c_eps if e["band"] == b]
        if not xs: break
        if sum(e["pass"] for e in xs) / len(xs) >= P_GATE: lvl = b
        else: break
    return lvl

def gate(profile):
    """U* from the profile dict with keys C, I, SA, T_frontier (at the budget run), M; O omitted for individuals."""
    order = lambda s, x: int("".join(ch for ch in s if ch.isdigit())) if s else -1
    C, I, SA, T, M = (profile.get(k) for k in ("C", "I", "SA", "T_frontier", "M"))
    u = None
    for n, (cn, i_n, sa_n, t_n, mu) in enumerate([("C0", "I0", "SA0", "T0", "M0"), ("C1", "I1", "SA1", "T1", "M1"), ("C2", "I2", "SA2", "T2", "M3"), ("C3", "I3", "SA3", "T3", "M4")]):
        if order(C, "C") >= n and order(I, "I") >= n and order(SA, "SA") >= n and order(T, "T") >= n and order(M, "M") >= order(mu, "M"): u = f"U{n}"
        else: break
    return u

def hlis(A):
    """Weighted geometric mean over the achievement variables present (equal weights); N/A omitted and named."""
    import math
    xs = [(k, v) for k, v in A.items() if v is not None]
    if not xs or any(v <= 0 for _, v in xs): return 0.0, [k for k, _ in xs]
    return round(100 * math.exp(sum(math.log(v) for _, v in xs) / len(xs)), 1), [k for k, _ in xs]

def hil(curve):
    """curve: {rung: HLIS_DI}. HIL-Level = highest rung run; AUC = mean; Ceiling = max; Gain = max - HG0; HIL-Score."""
    rungs = [r for r in ("HG0", "HG1", "HG2", "HG3") if r in curve]
    vals = [curve[r] for r in rungs]; ceil = max(vals); auc = round(sum(vals) / len(vals), 1); gain = round(ceil - curve["HG0"], 1)
    harness = 100 * gain / (100 - curve["HG0"]) if curve["HG0"] < 100 else 0.0
    return {"HIL_level": rungs[-1], "HIL_AUC": auc, "HIL_ceiling": ceil, "harness_gain": gain,
            "HIL_score": round(0.55 * auc + 0.35 * ceil + 0.10 * harness, 1), "curve": curve}

SA4_MAX_BRIER = 0.25; SA4_TOLERANCE = 0.05

def sa4_pass(sa4: dict, n_expected: int) -> bool:
    """Predeclared calibration rule: Brier at most 0.25, no worse than the post-hoc constant forecast by
    more than 0.05 (a pair with a perfect record cannot beat a constant 1.0 fitted after the fact), and a
    forecast recorded for every delegated episode."""
    b, c, n = sa4.get("brier"), sa4.get("constant_forecast_brier"), sa4.get("n")
    return bool(b is not None and c is not None and b <= SA4_MAX_BRIER and b - c <= SA4_TOLERANCE and n == n_expected)
