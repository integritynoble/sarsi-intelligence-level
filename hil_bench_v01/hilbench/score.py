"""Levels from readings; the gate; HLIS; HIL over the reference rungs. Weights predeclared."""
from __future__ import annotations
# Coordinate achievement anchors, predeclared. A coordinate that was not measured is None and is
# OMITTED from HLIS -- never zeroed, which is the framework's rule for `unmeasured`.
C_ANCHOR  = {None: 0.0, "C0": 0.2, "C1": 0.4, "C2": 0.6, "C3": 0.8, "C4": 1.0}
I_ANCHOR  = {None: 0.0, "I0": 0.1, "I1": 0.3, "I2": 0.55, "I3": 0.8}
O_ANCHOR  = {None: None, "O0": 0.3, "O1": 0.6, "O2": 1.0}
SA_ANCHOR = {None: 0.0, "SA0": 0.15, "SA1": 0.35, "SA2": 0.6, "SA3": 0.85, "SA4": 1.0}  # SA4 = self-change awareness (ratified ladder); the calibration forecast is SA-cal, a diagnostic bonus, not a rung
M_ANCHOR  = {None: 0.0, "M0": 0.0, "M1": 0.5, "M2": 0.75, "M3": 1.0}

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
    """(U*, bottleneck) from the profile dict with keys C, I, SA, T_frontier, M, and O.

    O participates only when it was measured: for an individual pair with no O suite, O is None or
    "N/A (individual)" and is omitted -- never treated as 0. The bottleneck names the coordinate reading
    that refused the next level (the first one checked that falls short), or None at the top."""
    order = lambda s: int("".join(ch for ch in s if ch.isdigit())) if isinstance(s, str) and any(ch.isdigit() for ch in s) else -1
    C, I, SA, T, M, O = (profile.get(k) for k in ("C", "I", "SA", "T_frontier", "M", "O"))
    O_measured = isinstance(O, str) and O[:1] == "O" and O[1:2].isdigit()
    ladder = [("C0", "I0", "SA0", "T0", "M0", "O0"), ("C1", "I1", "SA1", "T1", "M1", "O1"), ("C2", "I2", "SA2", "T2", "M3", "O2"), ("C3", "I3", "SA3", "T3", "M4", "O3")]
    u, bottleneck = None, None
    for n, (cn, i_n, sa_n, t_n, mu, on) in enumerate(ladder):
        short = [name for name, have, need in (("C", C, cn), ("I", I, i_n), ("SA", SA, sa_n), ("T", T, t_n), ("M", M, mu)) if order(have) < order(need)]
        if O_measured and order(O) < order(on): short.append("O")
        if short:
            bottleneck = {"C": C, "I": I, "SA": SA, "T": T, "M": M, "O": O}[short[0]]; break
        u = f"U{n}"
    return u, bottleneck

def hlis(A):
    """Weighted geometric mean over the achievement variables present (equal weights); N/A omitted and named."""
    import math
    xs = [(k, v) for k, v in A.items() if v is not None]
    if not xs or any(v <= 0 for _, v in xs): return 0.0, [k for k, _ in xs]
    return round(100 * math.exp(sum(math.log(v) for _, v in xs) / len(xs)), 1), [k for k, _ in xs]

def hil(curve):
    """curve: {rung: HLIS}. HIL-Level = highest rung run; AUC = mean; Ceiling = max; Gain = max - HG0;
    Harnessability = 100*Gain/(100-HG0) (0 when HG0 = 100); HIL-Score = 0.55 AUC + 0.35 Ceiling + 0.10 Harnessability.
    The curve must start at HG0 and be contiguous, and every value must be a finite number in [0, 100]."""
    import math
    rungs = [r for r in ("HG0", "HG1", "HG2", "HG3") if r in curve]
    if not rungs or rungs[0] != "HG0" or rungs != ["HG0", "HG1", "HG2", "HG3"][:len(rungs)] or len(rungs) != len(curve):
        raise ValueError(f"HIL curve must be contiguous from HG0: {sorted(curve)}")
    vals = [curve[r] for r in rungs]
    for v in vals:
        if not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v) or not 0 <= v <= 100:
            raise ValueError(f"HLIS values must be finite numbers in [0, 100]: {v!r}")
    ceil = max(vals); auc = round(sum(vals) / len(vals), 1); gain = round(ceil - curve["HG0"], 1)
    harness = 100 * gain / (100 - curve["HG0"]) if curve["HG0"] < 100 else 0.0
    return {"HIL_level": rungs[-1], "HIL_AUC": auc, "HIL_ceiling": ceil, "harness_gain": gain, "harnessability": round(harness, 1),
            "HIL_score": round(0.55 * auc + 0.35 * ceil + 0.10 * harness, 1), "curve": curve}

SACAL_MAX_BRIER = 0.25; SACAL_TOLERANCE = 0.05

def sacal_pass(sa4: dict, n_expected: int) -> bool:
    """Predeclared calibration rule: Brier at most 0.25, no worse than the post-hoc constant forecast by
    more than 0.05 (a pair with a perfect record cannot beat a constant 1.0 fitted after the fact), and a
    forecast recorded for every delegated episode."""
    b, c, n = sa4.get("brier"), sa4.get("constant_forecast_brier"), sa4.get("n")
    return bool(b is not None and c is not None and b <= SACAL_MAX_BRIER and b - c <= SACAL_TOLERANCE and n == n_expected)

def o_level(o0_pass: bool, o1_transfer: int):
    """O0 is coordination under real role separation; O1 additionally requires the organization's own
    memory to decide a later, different instance, with the ablated arm failing it."""
    if not o0_pass: return None
    return "O1" if o1_transfer == 1 else "O0"


def frontier_cumulative(eps, p=P_GATE, rho=1.0, budget=None):
    """DF(h,p) = max{T_b : every T_j, j<=b, meets S_net >= p at H<=h}.  A pass at a hard band cannot leap over a failed
    easier band: lower-T retention is a property of the FRONTIER, not of a T item certificate (T is an ordered axis)."""
    bands = [b for b in W_T]; best = None
    for b in bands:
        sub = [e for e in eps if e.get("band") == b and (budget is None or e.get("budget", "H0") <= budget)]
        if not sub: break
        s_net = sum(1.0 for e in sub if e.get("delivered_correct")) / len(sub) - rho * sum(1.0 for e in sub if e.get("false_completion")) / len(sub)
        if s_net >= p: best = b
        else: break
    return best
