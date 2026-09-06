"""The latent AI-Level Index: an unbounded, difficulty-calibrated scale fitted over canonical evidence units.

Following the index paper: for a binary evidence unit i on coordinate d, P(Y_mdi = 1) = sigma(theta_md - b_i) (the
one-parameter form; discrimination a_i = 1 in v1), theta_H = sum_d w_d theta_md, \mathrm{AILI} = 100 + s * theta_H with
s = 10 and equal weights. Items are pooled across every model record in `records/` (same benchmark version, same
split), so the scale is a property of the population of rows and a new row is placed by the SAME item difficulties
once anchors are frozen. Until anchors are ratified the fit is a CURRENT-FIT DIAGNOSTIC and says so in its output.

Evidence units for a bare-model record: every delegation episode (family, seed, rung), every C item (band, seed,
rung), every SA1 / SA2 probe (seed, rung), and O0 (seed, rung). Coordinates: C, DI, SA (and O when present). A bare
model has I0 by construction, so theta_I is not estimated for model rows; the headline uses the coordinates present
with weights renormalized, and the record says which.

Estimation: joint maximum likelihood by alternating Newton steps on theta and b with the constraint mean(b) = 0
(the origin) and a mild ridge on both (0.01) for identifiability at the extremes; standard errors from the observed
Fisher information. Items every model passes or every model fails carry no information about relative ability and
are dropped from the fit with a count reported.
"""
from __future__ import annotations
import json, math
from pathlib import Path

S_SCALE = 10.0
WEIGHTS = {"C": 0.25, "I": 0.25, "DI": 0.25, "SA": 0.25}

def evidence_units(R: dict) -> list:
    """(unit_id, coordinate, y) triples from one bare-model record."""
    out = []
    for rung, V in R["rungs"].items():
        for e in V["episodes"]:
            out.append((f"DI:{e['family']}:s{e['seed']}:{rung}", "DI", int(bool(e["delivered_correct"]))))
        for c in V.get("C", []):
            out.append((f"C:{c['band']}:{c.get('item','')}:s{c['seed']}:{rung}", "C", int(bool(c["pass"]))))
        for x in V.get("SA1", []): out.append((f"SA:sa1:s{x['seed']}:{rung}", "SA", int(bool(x["pass"]))))
        for x in V.get("SA2", []): out.append((f"SA:sa2:s{x['seed']}:{rung}", "SA", int(bool(x["pass"]))))
        if "O0" in V: out.append((f"O:o0:{rung}", "O", int(bool(V["O0"]["pass"]))))
    return out

def _sig(x): return 1.0 / (1.0 + math.exp(-x)) if x > -35 else 0.0

def fit_rasch(obs: dict, iters: int = 200, ridge: float = 0.01):
    """obs: {(model, item): y}. Returns theta {model: value}, b {item: value}, se {model: value}, dropped items."""
    models = sorted({m for m, _ in obs}); items = sorted({i for _, i in obs})
    # drop items with no variance across models (they cannot rank models)
    by_item = {}
    for (m, i), y in obs.items(): by_item.setdefault(i, []).append(y)
    dropped = [i for i, ys in by_item.items() if len(set(ys)) < 2 or len(ys) < 2]
    items = [i for i in items if i not in dropped]
    obs = {(m, i): y for (m, i), y in obs.items() if i in items}
    theta = {m: 0.0 for m in models}; b = {i: 0.0 for i in items}
    for _ in range(iters):
        for m in models:                                   # Newton step on theta_m
            g = -ridge * theta[m]; h = ridge
            for i in items:
                if (m, i) in obs:
                    p = _sig(theta[m] - b[i]); g += obs[(m, i)] - p; h += p * (1 - p)
            theta[m] += g / max(h, 1e-6)
        for i in items:                                    # Newton step on b_i
            g = -ridge * b[i]; h = ridge
            for m in models:
                if (m, i) in obs:
                    p = _sig(theta[m] - b[i]); g += p - obs[(m, i)]; h += p * (1 - p)
            b[i] += g / max(h, 1e-6)
        mean_b = sum(b.values()) / max(len(b), 1)          # origin: mean item difficulty = 0
        for i in items: b[i] -= mean_b
        for m in models: theta[m] -= mean_b
    se = {}
    for m in models:
        info = ridge + sum(_sig(theta[m] - b[i]) * (1 - _sig(theta[m] - b[i])) for i in items if (m, i) in obs)
        se[m] = 1.0 / math.sqrt(info)
    return theta, b, se, dropped

def latent_index(records: list, weights: dict = WEIGHTS, s: float = S_SCALE) -> dict:
    """records: list of (label, record dict). Fits one Rasch scale per coordinate over all models and returns the
    per-coordinate thetas, the headline theta_H with renormalized weights over the coordinates present, and
    \mathrm{AILI} = 100 + s * theta_H, with standard errors."""
    per_coord = {}
    for label, R in records:
        for unit, d, y in evidence_units(R): per_coord.setdefault(d, {})[(label, unit)] = y
    coords = [d for d in ("C", "I", "DI", "SA", "O") if d in per_coord]
    fits = {d: fit_rasch(per_coord[d]) for d in coords}
    labels = sorted({l for l, _ in records}); out = {"scale": {"origin": "mean item difficulty = 0 per coordinate", "s": s, "weights_v1": weights,
            "status": "CURRENT-FIT DIAGNOSTIC: anchors not yet ratified; the scale moves when rows are added, and a frozen historical index is published only after ratification"},
            "coordinates": {}, "models": {}}
    for d in coords:
        th, b, se, dropped = fits[d]
        out["coordinates"][d] = {"n_items": len(b), "dropped_no_variance": len(dropped), "difficulty_range": [round(min(b.values()), 2), round(max(b.values()), 2)] if b else None}
    used = [d for d in coords if d in weights]; wsum = sum(weights[d] for d in used)
    for m in labels:
        thetas = {d: fits[d][0].get(m) for d in coords if m in fits[d][0]}; ses = {d: fits[d][2].get(m) for d in coords if m in fits[d][2]}
        w = {d: weights[d] / wsum for d in used if d in thetas}; wn = sum(w.values()) or 1.0
        theta_H = sum(w[d] * thetas[d] for d in w) / wn; se_H = math.sqrt(sum((w[d] / wn) ** 2 * ses[d] ** 2 for d in w))
        out["models"][m] = {"theta": {d: round(v, 3) for d, v in thetas.items()}, "se": {d: round(v, 3) for d, v in ses.items()},
                            "theta_H": round(theta_H, 3), "se_H": round(se_H, 3), "HILIndex_latent": round(100 + s * theta_H, 1),
                            "HILIndex_latent_ci95": [round(100 + s * (theta_H - 1.96 * se_H), 1), round(100 + s * (theta_H + 1.96 * se_H), 1)],
                            "weights_used": {d: round(w[d] / wn, 3) for d in w}, "I": "I0 by construction (bare model); theta_I not estimated"}
    return out

def compact_string(index: dict, latent: dict | None = None, label: str | None = None) -> str:
    """The report string of the index paper: `<index> | U<level> | [C, I, T/H, SA] | M<level>` for a bare model."""
    b = index.get("bare", {}); lat = (latent or {}).get("models", {}).get(label or "", {})
    head = f"{lat['HILIndex_latent']}" if lat else f"{index['HIL_Index']}"
    return f"{head} | {b.get('U')} | [{b.get('C')}, I0, {b.get('T_frontier')}/H0, {b.get('SA')}] | M0"

def load_records(dirpath: Path, split: str = "public") -> list:
    out = []
    for p in sorted(dirpath.glob("*.json")):
        try: R = json.loads(p.read_text())
        except Exception: continue
        bare = R.get("mode") == "llm" and "rungs" in R and not any(k in str(R.get("executor", "")) for k in ("claude -p", "opencode run", "codex"))
        if bare and (R.get("evaluator", {}).get("split", "public") == split):
            out.append((R.get("model") or R.get("label") or p.stem, R))
    best = {}
    for lab, R in out:                       # one row per model: the record with the most evidence units
        n = sum(len(V["episodes"]) for V in R["rungs"].values())
        if lab not in best or n > best[lab][0]: best[lab] = (n, R)
    return [(lab, R) for lab, (n, R) in sorted(best.items())]
