"""Harness-generation conformance: a rung is certified as z = E · U · Δ_g · K — the mechanism exists in the frozen
contract, it FIRES on a witness, and it changes the outcome against the previous rung on the same seeds.

The witness is a scripted executor whose first deliverable is the family's named wrong method (the trap) and whose
second is the reference solution.  Under HG0 the wrong deliverable is delivered (a false completion); under HG1 a
failing public check holds it back; under HG2 the workspace is restored and the retry, told which check failed, delivers
the correct one.  The three outcomes on the same seed ARE the Δ factors.  The probe runs offline: no model is called.
"""
from __future__ import annotations
import json, shutil
from pathlib import Path
from . import harness

def _scripted(mod, key):
    n = {"calls": 0}
    def run(exec_tmpl, task, ws, limit, env=None):
        n["calls"] += 1
        fn = mod.naive_solve if n["calls"] == 1 else mod.reference_solve
        try: fn(Path(ws), key)
        except TypeError: fn(Path(ws))          # UAB families solve from the workspace alone
        return {"termination_reason": "scripted", "calls": n["calls"], "exit": 0}
    return run

def probe(fam: str, seed: int, root: Path) -> dict:
    import sys; sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from families import FAMILIES
    mod = FAMILIES[fam]; files, key = mod.generate(seed); out = {"family": fam, "seed": seed, "rungs": {}}
    saved = harness.run_exec
    try:
        for rung in ("HG0", "HG1", "HG2"):
            ws = root / f"hg_{fam}_s{seed}_{rung}"; shutil.rmtree(ws, ignore_errors=True); ws.mkdir(parents=True)
            harness.run_exec = _scripted(mod, key)
            r = harness.run_rung(rung, fam, files, ws, "scripted", 60)
            v = mod.verify(ws, key) if r["delivered"] else {"pass": False}
            out["rungs"][rung] = {"delivered": r["delivered"], "held_back": r["held_back"], "attempts": len(r["attempts"]),
                                  "verifier_pass": bool(r["delivered"] and v["pass"]), "false_completion": bool(r["delivered"] and not v["pass"]),
                                  "public_failed": [n for n, ok, _ in (r.get("public") or []) if not ok]}
    finally:
        harness.run_exec = saved
    g0, g1, g2 = (out["rungs"][k] for k in ("HG0", "HG1", "HG2"))
    trap_public = bool(g1["public_failed"]) or g1["held_back"]      # the trap must be publicly visible for HG1 to have anything to hold
    out["factors"] = {
        "HG0": {"E": g0["attempts"] == 1 and g0["delivered"]},
        "HG1": {"E": True, "U": g1["held_back"] and not g1["delivered"], "Δ_1": g0["false_completion"] and not g1["false_completion"], "K": g0["attempts"] == 1},
        "HG2": {"E": True, "U": g2["attempts"] >= 2 and g2["delivered"], "Δ_2": g2["verifier_pass"] and not g1["verifier_pass"], "K": g1["held_back"] or g2["attempts"] >= 2},
    }
    out["trap_publicly_visible"] = trap_public
    out["z"] = {r: all(f.values()) for r, f in out["factors"].items()}
    return out

def run_all(root: Path, fams=("code_t0", "funding_t0", "job_t0", "paper_t0", "business_t0", "paper_t1"), seeds=(0, 1, 2)) -> dict:
    res = [probe(f, s, root) for f in fams for s in seeds]
    vis = [r for r in res if r["trap_publicly_visible"]]
    summary = {rung: {"witnesses": len(vis), "z_pass": sum(r["z"][rung] for r in vis)} for rung in ("HG0", "HG1", "HG2")}
    summary["not_publicly_visible"] = [(r["family"], r["seed"]) for r in res if not r["trap_publicly_visible"]]
    (root / "hg_conform.json").write_text(json.dumps({"summary": summary, "probes": res}, indent=1, ensure_ascii=False))
    return summary
