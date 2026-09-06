"""What it takes for a capability index to mean anything: the estimator, measured on populations where truth is known.

An index that fits a latent scale reports a number whatever the data are.  The questions that decide whether the number
is worth publishing are not answerable from a leaderboard: how many models and how many items before the ordering is
recoverable; what happens to already-published scores when a new cohort is added; whether a fixed suite keeps
discriminating as the frontier advances; and whether the scoring primitive prices a confident wrong answer correctly.
Each is a simulation with known truth, and each is run in `run_all`.

The estimator here is the same one-parameter joint-maximum-likelihood fit as `latent.fit_rasch`, vectorized; a test
asserts the two agree on a shared case, so speed does not buy a different estimator.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np

# --------------------------------------------------------------------------------------------------- the estimator
def fit(Y: np.ndarray, mask: np.ndarray | None = None, iters: int = 300, ridge: float = 0.01):
    """Y[m, i] in {0,1}; mask[m, i] True where observed.  Returns theta, b, se, kept-item index.

    Joint ML by alternating Newton steps, origin fixed at mean item difficulty, ridge for identifiability at the
    extremes, and items with no between-model variance dropped: an item everyone passes or everyone fails carries no
    information about who is stronger, and keeping it only shrinks the scale."""
    M, K = Y.shape
    mask = np.ones_like(Y, dtype=bool) if mask is None else mask.astype(bool)
    n = mask.sum(0); s = np.where(mask, Y, 0).sum(0)
    keep = (n >= 2) & (s > 0) & (s < n)
    Y, mask = Y[:, keep], mask[:, keep]
    if Y.shape[1] == 0: return np.zeros(M), np.zeros(0), np.full(M, np.inf), keep
    theta = np.zeros(M); b = np.zeros(Y.shape[1])
    for _ in range(iters):
        p = 1.0 / (1.0 + np.exp(-(theta[:, None] - b[None, :]))); w = p * (1 - p) * mask
        g = ((Y - p) * mask).sum(1) - ridge * theta; h = w.sum(1) + ridge
        theta += g / np.maximum(h, 1e-9)
        p = 1.0 / (1.0 + np.exp(-(theta[:, None] - b[None, :]))); w = p * (1 - p) * mask
        gb = ((p - Y) * mask).sum(0) - ridge * b; hb = w.sum(0) + ridge
        b += gb / np.maximum(hb, 1e-9)
        c = b.mean(); b -= c; theta -= c
    p = 1.0 / (1.0 + np.exp(-(theta[:, None] - b[None, :]))); info = (p * (1 - p) * mask).sum(1) + ridge
    return theta, b, 1.0 / np.sqrt(info), keep

def responses(theta, b, a=None, rng=None):
    a = np.ones_like(b) if a is None else a
    p = 1.0 / (1.0 + np.exp(-a[None, :] * (theta[:, None] - b[None, :])))
    return (rng.random(p.shape) < p).astype(float)

def _spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float); ry = np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1]) if len(x) > 1 else float("nan")

def _center(x): return x - x.mean()

# ------------------------------------------------------------------------------- 1. recovery and sample requirements
def recovery(n_models, n_items, reps=40, seed=0, a_sd=0.0, missing=0.0, spread=1.0):
    """How well the fit recovers a known ordering, as a function of population size and item count."""
    rng = np.random.default_rng(seed); rho = []; rmse = []; inv = []; cov = []; se = []; dropped = []; adj = []
    for _ in range(reps):
        theta = rng.normal(0, spread, n_models); b = rng.normal(0, 1.2, n_items)
        a = np.exp(rng.normal(0, a_sd, n_items)) if a_sd else None
        Y = responses(theta, b, a, rng)
        mask = rng.random(Y.shape) >= missing if missing else None
        th, bb, s, keep = fit(Y, mask)
        if not np.isfinite(s).all() or len(bb) == 0: continue
        rho.append(_spearman(theta, th)); rmse.append(float(np.sqrt(np.mean((_center(th) - _center(theta)) ** 2))))
        order_true = np.argsort(theta); order_hat = np.argsort(th)
        inv.append(float(np.mean(order_true != order_hat)))
        lo, hi = _center(th) - 1.96 * s, _center(th) + 1.96 * s
        cov.append(float(np.mean((_center(theta) >= lo) & (_center(theta) <= hi))))
        se.append(float(np.median(s))); dropped.append(1.0 - keep.mean())
        o = np.argsort(-th)                                   # the leaderboard order, best first
        if len(o) > 1:
            sep = [(th[o[k]] - 1.96 * s[o[k]]) > (th[o[k + 1]] + 1.96 * s[o[k + 1]]) for k in range(len(o) - 1)]
            adj.append(float(np.mean(sep)))
    f = lambda v: float(np.median(v)) if v else float("nan")
    return {"n_models": n_models, "n_items": n_items, "reps": len(rho), "spearman": f(rho), "rmse_logit": f(rmse),
            "rank_error_rate": f(inv), "ci95_coverage": f(cov), "median_se": f(se), "items_dropped": f(dropped),
            "adjacent_pairs_separated": f(adj),
            "note": ("Spearman is uninformative below about eight models: with two or three, any estimator orders them "
                     "almost surely. The quantity a leaderboard needs is the share of ADJACENT pairs whose 95% intervals "
                     "do not overlap -- and that falls as the population grows, because neighbours crowd faster than "
                     "errors shrink. There is no per-cell 'usable' verdict: ordering, interval and separation are three "
                     "different questions and a single flag would hide which one a cell fails.")}

def sample_requirements(models=(2, 3, 5, 8, 12, 20, 40), items=(40, 80, 160, 320), reps=30, seed=0):
    return [recovery(m, k, reps=reps, seed=seed + 7 * m + k) for m in models for k in items]

# ------------------------------------------------------------------------------------ 2. anchors and score stability
def equating_drift(n_old=8, n_new=8, n_anchor=60, n_fresh=120, shift=0.8, reps=40, seed=1):
    """A second cohort arrives, stronger, measured on the anchors plus fresh items.  What happens to the first
    cohort's already-published numbers under free recalibration, and under frozen anchors?"""
    rng = np.random.default_rng(seed); free = []; anch = []; free_signed = []; anch_signed = []; noise = []
    for _ in range(reps):
        th_old = rng.normal(0, 1, n_old); th_new = rng.normal(shift, 1, n_new)
        b_anchor = rng.normal(0, 1.2, n_anchor); b_fresh = rng.normal(shift, 1.2, n_fresh)   # fresh items track the frontier
        Y1 = responses(th_old, b_anchor, None, rng)
        t1, b1, _, keep1 = fit(Y1)                                     # published year 1, origin = mean anchor difficulty
        b_hat_anchor = np.full(n_anchor, np.nan); b_hat_anchor[keep1] = b1
        b_all = np.concatenate([b_anchor, b_fresh])
        Y2 = responses(np.concatenate([th_old, th_new]), b_all, None, rng)
        t2_free, _, _, _ = fit(Y2)                                     # year 2, everything recalibrated together
        free.append(float(np.mean(np.abs(_center(t2_free)[:n_old] - _center(t1)))))
        free_signed.append(float(np.mean(_center(t2_free)[:n_old] - _center(t1))))
        # frozen anchors: b of anchor items held at year-1 values; only fresh items and abilities are estimated
        t2a = _fit_with_fixed_anchors(Y2, b_hat_anchor, n_anchor)
        anch.append(float(np.mean(np.abs(t2a[:n_old] - _center(t1)))))
        anch_signed.append(float(np.mean(t2a[:n_old] - _center(t1))))
        noise.append(float(np.median(_se_of(Y1))))
    return {"n_old": n_old, "n_new": n_new, "shift": shift, "reps": reps,
            "drift_free_recalibration": round(float(np.median(free)), 3), "drift_frozen_anchors": round(float(np.median(anch)), 3),
            "systematic_free": round(float(np.median(free_signed)), 3), "systematic_frozen": round(float(np.median(anch_signed)), 3),
            "measurement_noise_se": round(float(np.median(noise)), 3),
            "reading": "absolute drift mixes noise with bias; the signed drift is the bias. Under free recalibration the first cohort's published scores move systematically when a stronger cohort is added; under frozen anchors the movement is at the level of the standard error."}

def _se_of(Y):
    _, _, se, _ = fit(Y); return se

def _fit_with_fixed_anchors(Y, b_anchor_fixed, n_anchor, iters=300, ridge=0.01):
    M, K = Y.shape; b = np.zeros(K); free = np.ones(K, dtype=bool)
    have = ~np.isnan(b_anchor_fixed); b[:n_anchor][have] = b_anchor_fixed[have]; free[:n_anchor][have] = False
    theta = np.zeros(M)
    for _ in range(iters):
        p = 1.0 / (1.0 + np.exp(-(theta[:, None] - b[None, :]))); w = p * (1 - p)
        theta += ((Y - p).sum(1) - ridge * theta) / np.maximum(w.sum(1) + ridge, 1e-9)
        p = 1.0 / (1.0 + np.exp(-(theta[:, None] - b[None, :]))); w = p * (1 - p)
        step = ((p - Y).sum(0) - ridge * b) / np.maximum(w.sum(0) + ridge, 1e-9)
        b = np.where(free, b + step, b)          # the anchors do not move: they carry the scale from year 1
    return theta

# --------------------------------------------------------------------------------------- 3. saturation resistance
def separation(theta_hat, se):
    """Separation reliability: the share of observed spread that is not measurement error.  Below ~0.7 a leaderboard
    is ordering noise."""
    v = float(np.var(theta_hat, ddof=1)); e = float(np.mean(se ** 2))
    return max(0.0, (v - e) / v) if v > 0 else 0.0

def saturation(years=6, n_models=12, n_items=160, advance=0.6, reps=25, seed=2):
    """The frontier advances by `advance` logits a year.  A fixed suite keeps its year-0 items; a refreshed suite keeps
    the same LEVELS but redraws witness difficulty to track the population, which is what 'saturation motivates harder
    witnesses, not a redefined level' means operationally."""
    rng = np.random.default_rng(seed); out = []
    b0 = rng.normal(0, 1.2, n_items)
    for t in range(years):
        fx, rf, ceil_fx, ceil_rf, comp_fx, comp_rf, mean_fx = [], [], [], [], [], [], []
        for _ in range(reps):
            theta = rng.normal(advance * t, 1.0, n_models)
            Yf = responses(theta, b0, None, rng); tf, _, sf, _ = fit(Yf)
            b_t = rng.normal(advance * t, 1.2, n_items)
            Yr = responses(theta, b_t, None, rng); tr, _, sr, _ = fit(Yr)
            fx.append(separation(tf, sf)); rf.append(separation(tr, sr))
            ceil_fx.append(float(np.mean(Yf.mean(1) > 0.95))); ceil_rf.append(float(np.mean(Yr.mean(1) > 0.95)))
            comp_fx.append(float(np.std(Yf.mean(1), ddof=1))); comp_rf.append(float(np.std(Yr.mean(1), ddof=1)))
            mean_fx.append(float(np.mean(Yf.mean(1))))
        out.append({"year": t, "frontier_logits": round(advance * t, 2),
                    "separation_fixed": round(float(np.median(fx)), 3), "separation_refreshed": round(float(np.median(rf)), 3),
                    "at_ceiling_fixed": round(float(np.median(ceil_fx)), 3), "at_ceiling_refreshed": round(float(np.median(ceil_rf)), 3),
                    "composite_mean_fixed": round(float(np.median(mean_fx)), 3),
                    "composite_spread_fixed": round(float(np.median(comp_fx)), 3), "composite_spread_refreshed": round(float(np.median(comp_rf)), 3)})
    return out

# ------------------------------------------------------------------------------------------- 4. pricing a bluff
def bluff_pricing(rho=1.0, grid=21, seed=3, n=400):
    """Two systems of equal underlying competence q: one attempts everything, one declines what it judges it cannot do.
    Under a success-only primitive the decliner is punished for every refusal; under the delivered-outcome primitive a
    refusal costs nothing and a confident wrong answer costs rho.  The question is how often the ordering inverts, and
    what the delegator actually pays."""
    rng = np.random.default_rng(seed); rows = []; inversions = 0; total = 0
    for q in np.linspace(0.3, 0.9, grid):
        for skill in np.linspace(0.0, 1.0, grid):          # how well the decliner tells its failures from its successes
            correct = rng.random(n) < q
            declines = (~correct) & (rng.random(n) < skill) | (correct & (rng.random(n) < skill * 0.15))   # some false rejection
            delivered = ~declines
            dc = float(np.mean(delivered & correct)); fc = float(np.mean(delivered & ~correct)); hb = float(np.mean(declines))
            s_success = float(np.mean(correct))                                   # success-only: refusals invisible
            s_net = dc - rho * fc                                                 # delivered-outcome
            bluff_success, bluff_net = q, q - rho * (1 - q)
            rows.append({"q": round(float(q), 3), "decline_skill": round(float(skill), 3), "delivered_correct": round(dc, 3),
                         "false_completion": round(fc, 3), "held_back": round(hb, 3), "s_success": round(s_success, 3),
                         "s_net": round(s_net, 3), "bluffer_net": round(bluff_net, 3), "net_prefers_decliner": bool(s_net > bluff_net)})
            total += 1
            if s_success <= bluff_success and s_net > bluff_net: inversions += 1
    share = inversions / total
    return {"rho": rho, "cells": total, "share_where_net_reverses_the_order": round(share, 3),
            "reading": "the share of the (competence, discrimination) grid on which a success-only index ranks the bluffer at least as high while the delivered-outcome primitive prefers the system that declines",
            "cost_identity": "E[cost to the delegator] = c_wrong*P(false completion) + c_redo*P(held back); S_net is the linear proxy with rho = c_wrong/c_redo",
            "rows": rows[:0]}

# ------------------------------------------------------------- 4b. the resolution law: items needed to rank M models
def _adjacent_separated(n_models, n_items, reps, rng):
    got = []
    for _ in range(reps):
        theta = rng.normal(0, 1, n_models); b = rng.normal(0, 1.2, n_items)
        th, _, se, _ = fit(responses(theta, b, None, rng))
        if not np.isfinite(se).all(): continue
        o = np.argsort(-th)
        got.append(float(np.mean([(th[o[k]] - 1.96 * se[o[k]]) > (th[o[k + 1]] + 1.96 * se[o[k + 1]]) for k in range(len(o) - 1)])))
    return float(np.median(got)) if got else 0.0

def resolution_law(models=(4, 6, 8, 12, 16), target=0.5, reps=12, seed=5, k_max=20000):
    """How many items are needed before a leaderboard can actually separate NEIGHBOURING models?

    The gap between adjacent abilities shrinks as the population grows -- with M draws from a unit normal the typical
    middle gap is of order 1/M -- while the standard error of a fit on K binary items falls only as 1/sqrt(K).  So the
    item count needed to resolve neighbours should grow like M^2.  This scans K for each M and reports the smallest K
    reaching `target` separation, then fits the exponent."""
    rng = np.random.default_rng(seed); rows = []
    for M in models:
        K = 64; found = None
        while K <= k_max:
            v = _adjacent_separated(M, K, reps, rng)
            if v >= target: found = K; break
            K *= 2
        rows.append({"n_models": M, "items_for_%d%%_separation" % int(target * 100): found, "capped": found is None})
    xs = [r["n_models"] for r in rows if r["items_for_%d%%_separation" % int(target * 100)]]
    ys = [r["items_for_%d%%_separation" % int(target * 100)] for r in rows if r["items_for_%d%%_separation" % int(target * 100)]]
    slope = float(np.polyfit(np.log(xs), np.log(ys), 1)[0]) if len(xs) > 2 else float("nan")
    return {"target_separation": target, "rows": rows, "log_log_slope": round(slope, 2),
            "reading": "the exponent of items against models; near 2 means resolving twice as many models costs four times the evidence, which is why a dense leaderboard should publish bands rather than ranks"}

def bands(scores, ses, z=1.96):
    """Group models whose intervals overlap into statistically indistinguishable bands, best first.  A leaderboard that
    prints a rank it cannot support is reporting noise; a band is the honest unit."""
    order = sorted(range(len(scores)), key=lambda i: -scores[i]); out = []; cur = [order[0]]
    for a, b in zip(order, order[1:]):
        if (scores[a] - z * ses[a]) > (scores[b] + z * ses[b]): out.append(cur); cur = [b]
        else: cur.append(b)
    out.append(cur); return out

# ------------------------------------------------------------------------- 5. partial coverage: what linking needs
def coverage_study(n_models=12, n_items=160, reps=30, seed=4):
    """Not every model runs every cell.  The hazard is not a gap; it is a gap with no common items across it.

    Four regimes: complete; missing at random; blocked by difficulty (half the models run only the easy half, so the
    hard items are still answered by the other half and carry the scale); and disjoint (the two halves of the
    population share no item at all).  Reported per regime: the ordering recovered, and the interval on the models
    that skipped -- a model measured on a subset it ceilings is not misplaced, it is placed with a wide interval."""
    rng = np.random.default_rng(seed); out = []
    for kind in ("complete", "missing at random, 40%", "blocked by difficulty, items shared",
                 "disjoint: the halves share no item"):
        rho = []; se_all = []; se_part = []
        for _ in range(reps):
            theta = rng.normal(0, 1, n_models); b = np.sort(rng.normal(0, 1.2, n_items))
            Y = responses(theta, b, None, rng); mask = np.ones_like(Y, dtype=bool); half = n_models // 2
            if kind.startswith("missing at random"): mask = rng.random(Y.shape) >= 0.4
            elif kind.startswith("blocked"): mask[:half, n_items // 2:] = False
            elif kind.startswith("disjoint"):
                mask[:half, n_items // 2:] = False; mask[half:, :n_items // 2] = False
            th, bb, s, _ = fit(Y, mask)
            if not np.isfinite(s).all(): continue
            rho.append(_spearman(theta, th)); se_all.append(float(np.median(s)))
            se_part.append(float(np.median(s[:half])) if kind.startswith(("blocked", "disjoint")) else float(np.median(s)))
        out.append({"coverage": kind, "spearman": round(float(np.median(rho)), 3),
                    "median_se": round(float(np.median(se_all)), 3),
                    "median_se_partial_models": round(float(np.median(se_part)), 3)})
    return out

# ------------------------------------------------------------------------------------------------------- run them all
def run_all(out_dir: Path, quick=False) -> dict:
    reps = 8 if quick else 30
    res = {"sample_requirements": sample_requirements(reps=reps),
           "equating": equating_drift(reps=reps), "saturation": saturation(reps=max(8, reps // 2)),
           "bluff": bluff_pricing(grid=11 if quick else 21), "coverage": coverage_study(reps=reps),
           "resolution": resolution_law(reps=6 if quick else 12)}
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index_sim.json").write_text(json.dumps(res, indent=1))
    return res
