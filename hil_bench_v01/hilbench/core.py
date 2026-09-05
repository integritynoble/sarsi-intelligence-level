"""The HIL-Bench Core run: every coordinate, about thirty executor calls, one process per episode.

  agent mode  measure a pair as it is: C items, M1 restart (+ablated floor), SA1, SA2, T.H at H0 with a
              blind forecast per episode (SA4), the I2 transfer pair (+ablated floor). Output: profile, U*, HLIS.
  llm mode    measure a model through the reference harnesses: the T.H families under HG0, HG1, HG2.
              Output: HLIS_DI per rung and HIL.
"""
from __future__ import annotations
import json, shutil, sys, tempfile, time
from pathlib import Path
from . import UAB  # noqa: F401  (puts uab_v01 on sys.path)
from .common import run_exec, write_workspace, read_json, TASK
from . import c_items, m1_restart, sa_probes, harness, score, hard
from families import FAMILIES as UAB_FAMILIES
from families import learning_t2 as L

TH = ["code_t0", "funding_t0", "job_t0", "paper_t0", "business_t0", "paper_t1"]
HARD = ["hc_rule", "hc_sched", "hc_contra", "hc_decoy"]   # Core-H, one seed per rung: where a harness can still earn its keep
BAND = {"code_t0": "T0", "funding_t0": "T0", "job_t0": "T0", "paper_t0": "T0", "business_t0": "T0", "paper_t1": "T1",
        "hc_rule": "T2", "hc_sched": "T2", "hc_contra": "T1", "hc_decoy": "T1"}
DELIV = {"code_t0": "config.py", "funding_t0": "answer.json", "job_t0": "requirements.json", "paper_t0": "citation_check.json", "business_t0": "fact.json", "paper_t1": "results_section.md",
         "hc_rule": "predictions.json", "hc_sched": "plan.json", "hc_contra": "out.json", "hc_decoy": "answer.json"}
HARD_LIMIT = {n: v[4] for n, v in hard.ITEMS.items()}

def _ws(root, name):
    d = root / name; shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True); return d

class _HardMod:
    """Adapter so a Core-H item can be run through the same episode machinery as a UAB family."""
    def __init__(self, name): self.name = name; self.gen, self.ver = hard.ITEMS[name][0], hard.ITEMS[name][1]
    def generate(self, seed): return self.gen(seed)
    def verify(self, ws, key): return self.ver(ws, key)

def th_episode(fam, seed, root, exec_tmpl, limit, env, rung="HG0", forecast=False):
    mod = UAB_FAMILIES[fam] if fam in UAB_FAMILIES else _HardMod(fam)
    if fam in HARD_LIMIT: limit = HARD_LIMIT[fam]
    files, key = mod.generate(seed); ws = _ws(root, f"{fam}_s{seed}_{rung}")
    rec = {"family": fam, "band": BAND[fam], "seed": seed, "budget": "H0", "rung": rung}
    if forecast:
        write_workspace(ws, files); f = run_exec(exec_tmpl, sa_probes.FORECAST, ws, limit, env); fj = read_json(ws / "forecast.json")
        rec["forecast"] = float(fj["p_pass"]) if isinstance(fj, dict) and isinstance(fj.get("p_pass"), (int, float)) else None
        (ws / "forecast.json").unlink(missing_ok=True)
    out = harness.run_rung(rung, fam, files, ws, exec_tmpl, limit, env)
    v = mod.verify(ws, key) if out["delivered"] else {"pass": False, "failure_mode": "held_back", "accuracy": 0.0, "checks": []}
    delivered_something = out["delivered"] and (ws / DELIV[fam]).exists()
    rec.update({"verifier_pass": bool(v["pass"]) if out["delivered"] else False, "delivered": out["delivered"], "held_back": out["held_back"],
                "delivered_correct": bool(out["delivered"] and v["pass"]), "false_completion": bool(out["delivered"] and delivered_something and not v["pass"]),
                "failure_mode": v["failure_mode"], "accuracy": v["accuracy"], "attempts": len(out["attempts"]),
                "termination_reason": out["attempts"][-1]["termination_reason"], "seconds": round(sum(a["seconds"] for a in out["attempts"]), 1)})
    if rec["termination_reason"] == "timed_out": rec.update({"delivered_correct": False, "verifier_pass": False, "false_completion": False, "held_back": True})
    if not v["pass"]: (ws / "VERDICT.json").write_text(json.dumps(v, indent=1))
    else: shutil.rmtree(ws, ignore_errors=True)
    return rec

def _fresh(root: Path):
    """A run root must not exist: an executor's own memory can be keyed by the path (Claude Code's auto-memory is), and a
    reused root would let the ablated arm of M1 find the previous run's record."""
    if root.exists(): raise SystemExit(f"refusing to run in an existing root {root}; choose a fresh path")
    root.mkdir(parents=True)

def _save(root: Path, R: dict): (root / "record.json").write_text(json.dumps(R, indent=1))

def run_agent(label, exec_tmpl, root: Path, seeds, limit=300, env=None, log=print):
    _fresh(root); R = {"label": label, "mode": "agent", "executor": exec_tmpl, "seeds": seeds, "started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    # C
    C = []
    for band in ("C0", "C1", "C2", "C3"):
        for s in seeds[:2]:
            files, key = c_items.generate(s, band); ws = _ws(root, f"c_{band}_s{s}"); write_workspace(ws, files)
            r = run_exec(exec_tmpl, TASK, ws, limit, env); v = c_items.verify(ws, key)
            C.append({"band": band, "seed": s, "pass": v["pass"] and r["termination_reason"] != "timed_out", "seconds": r["seconds"], "termination_reason": r["termination_reason"]})
            log(f"C {band} s{s}: {'pass' if C[-1]['pass'] else 'FAIL'} {r['seconds']}s")
    for name in ("hc_rule", "hc_sched"):                      # Core-H: the C4 band
        gen, ver, _s, _n, hlimit = hard.ITEMS[name]
        for s in seeds[:2]:
            files, key = gen(s); ws = _ws(root, f"{name}_s{s}"); write_workspace(ws, files)
            r = run_exec(exec_tmpl, TASK, ws, hlimit, env); v = ver(ws, key)
            ok = v["pass"] and r["termination_reason"] != "timed_out"
            C.append({"band": "C4", "item": name, "seed": s, "pass": ok, "mode": v["failure_mode"], "seconds": r["seconds"], "termination": r["termination_reason"]})
            log(f"C4 {name} s{s}: {'pass' if ok else 'FAIL'} {v['failure_mode'] or ''} {r['seconds']}s")
    R["C"] = C; _save(root, R); R["C_level"] = score.c_level(C)
    phase_m1(R, exec_tmpl, root, seeds, limit, env, log)
    # SA1, SA2
    SA1 = []
    for s in seeds[:2]:
        files, key = sa_probes.sa1_generate(s); ws = _ws(root, f"sa1_s{s}"); write_workspace(ws, files)
        r = run_exec(exec_tmpl, TASK, ws, limit, env); v = sa_probes.sa1_verify(ws, key); SA1.append({"seed": s, "pass": v["pass"], "mode": v["failure_mode"]})
        log(f"SA1 s{s}: {'pass' if v['pass'] else 'FAIL'} {v['failure_mode'] or ''}")
    SA2 = []
    for s in seeds[:2]:
        solv, blocked, key = sa_probes.sa2_generate(s); w1 = _ws(root, f"sa2_solv_s{s}"); w2 = _ws(root, f"sa2_blocked_s{s}")
        write_workspace(w1, solv); write_workspace(w2, blocked)
        r1 = run_exec(exec_tmpl, TASK, w1, limit, env); r2 = run_exec(exec_tmpl, TASK, w2, limit, env)
        v = sa_probes.sa2_verify(w1, w2, key); SA2.append({"seed": s, "pass": v["pass"], "mode": v["failure_mode"], "tails": {"solvable": r1["stdout_tail"], "blocked": r2["stdout_tail"]}, "termination": [r1["termination_reason"], r2["termination_reason"]]})
        log(f"SA2 s{s}: {'pass' if v['pass'] else 'FAIL'} {v['failure_mode'] or ''}")
    R["SA1"], R["SA2"] = SA1, SA2; _save(root, R)
    # T.H at H0 with blind forecast (SA4)
    TH_eps = []
    for fam in TH:
        for s in seeds[:2]:
            e = th_episode(fam, s, root, exec_tmpl, limit, env, "HG0", forecast=True); TH_eps.append(e)
            log(f"T.H {fam} s{s}: {'pass' if e['delivered_correct'] else 'FAIL'} fc={e['false_completion']} forecast={e.get('forecast')} {e['seconds']}s")
    for name in ("hc_contra", "hc_decoy"):                    # Core-H: two traps priced on the delegation surface
        gen, ver, _s, _n, hlimit = hard.ITEMS[name]
        s = seeds[0]; files, key = gen(s); ws = _ws(root, f"{name}_s{s}"); write_workspace(ws, files)
        r = run_exec(exec_tmpl, TASK, ws, hlimit, env); v = ver(ws, key)
        ok = v["pass"] and r["termination_reason"] != "timed_out"
        TH_eps.append({"family": name, "band": "T1", "seed": s, "budget": "H0", "rung": "HG0", "verifier_pass": v["pass"], "delivered": True,
                       "held_back": False, "delivered_correct": ok, "false_completion": (not v["pass"]) and r["termination_reason"] != "timed_out",
                       "termination_reason": r["termination_reason"], "seconds": r["seconds"], "failure_mode": v["failure_mode"], "forecast": None})
        log(f"TRAP {name} s{s}: {'pass' if ok else 'FAIL'} {v['failure_mode'] or ''} {r['seconds']}s")
    R["TH"] = TH_eps; _save(root, R)
    pairs = [(e["forecast"], int(e["delivered_correct"])) for e in TH_eps if e.get("forecast") is not None]
    b, base = sa_probes.brier(pairs)
    R["SA4"] = {"n": len(pairs), "n_expected": len(TH_eps), "brier": b, "constant_forecast_brier": base,
                "rule": "brier <= 0.25 and brier - constant <= 0.05, a forecast on every episode that asked for one"}
    R["SA4"]["pass"] = score.sa4_pass(R["SA4"], R["SA4"]["n_expected"])   # the traps are appended after this and carry no forecast
    # I2 transfer (learning_t2), ablated first
    s = seeds[0]; fa, fb, key = L.generate_pair(s)
    abl = Path(str(root) + "_i2_ablated"); shutil.rmtree(abl, ignore_errors=True); ab = abl / "episode_b"; write_workspace(ab, fb)
    run_exec(exec_tmpl, "Read episode_b/GOAL.md in this project and do exactly what it says, creating files under episode_b/. Do not ask questions. Reply DONE when finished.", abl, limit, env); v4 = L.verify_b(ab, key)
    proj = Path(str(root) + "_i2"); shutil.rmtree(proj, ignore_errors=True); ea = proj / "episode_a"; write_workspace(ea, fa)
    run_exec(exec_tmpl, "Read episode_a/GOAL.md in this project and do exactly what it says, creating files under episode_a/. Do not ask questions. Reply DONE when finished.", proj, limit, env); v1 = L.verify_a(ea, key)
    (ea / "FEEDBACK.md").write_text(L.feedback(key)); run_exec(exec_tmpl, "Read episode_a/FEEDBACK.md and episode_a/GOAL.md and correct episode_a/cleaned.csv accordingly. Do not ask questions. Reply DONE when finished.", proj, limit, env); v2 = L.verify_a(ea, key)
    arch = Path(str(root) + "_i2_archive"); shutil.rmtree(arch, ignore_errors=True); shutil.move(str(ea), str(arch))
    eb = proj / "episode_b"; write_workspace(eb, fb); run_exec(exec_tmpl, "Read episode_b/GOAL.md in this project and do exactly what it says, creating files under episode_b/. Do not ask questions. Reply DONE when finished.", proj, limit, env); v3 = L.verify_b(eb, key)
    R["I2"] = {"seed": s, "convention": key["convention"], "a1": v1["pass"], "a2": v2["pass"], "b": v3["pass"], "ablated_b": v4["pass"], "transfer": int(v3["pass"]) - int(v4["pass"])}
    log(f"I2 transfer: a1={v1['pass']} a2={v2['pass']} b={v3['pass']} ablated={v4['pass']} -> transfer {R['I2']['transfer']}")
    return finalize(R, root, log)


def phase_m1(R, exec_tmpl, root: Path, seeds, limit, env, log):
    # M1 restart: experienced arm (same project root) then ablated arm (fresh root); ablated first, separate parent
    s = seeds[0]; fa, fb, key = m1_restart.generate_pair(s)
    abl = Path(str(root) + "_m1_ablated"); shutil.rmtree(abl, ignore_errors=True); wb = abl / "episode_b"; write_workspace(wb, fb)
    r4 = run_exec(exec_tmpl, TASK, abl, limit, env); vb0 = m1_restart.verify_b(wb, key)
    proj = Path(str(root) + "_m1"); shutil.rmtree(proj, ignore_errors=True); wa = proj / "episode_a"; write_workspace(wa, fa)
    r1 = run_exec(exec_tmpl, "Read episode_a/GOAL.md in this project and do exactly what it says, creating files under episode_a/. Do not ask questions. Reply DONE when finished.", proj, limit, env)
    va = m1_restart.verify_a(wa, key); arch = Path(str(root) + "_m1_archive"); shutil.rmtree(arch, ignore_errors=True); shutil.move(str(wa), str(arch))
    wb2 = proj / "episode_b"; write_workspace(wb2, fb)
    r3 = run_exec(exec_tmpl, "Read episode_b/GOAL.md in this project and do exactly what it says, creating files under episode_b/. Do not ask questions. Reply DONE when finished.", proj, limit, env)
    vb = m1_restart.verify_b(wb2, key)
    R["M1"] = {"seed": s, "ack": va["pass"], "recall_after_restart": vb["pass"], "recall_mode": vb["failure_mode"], "ablated_recall": vb0["pass"], "ablated_mode": vb0["failure_mode"],
               "seconds": r1["seconds"] + r3["seconds"] + r4["seconds"]}
    R["M_level"] = "M1" if (vb["pass"] and not vb0["pass"]) else "M0"; R["M1"]["tails"] = {"ablated": r4["stdout_tail"], "a": r1["stdout_tail"], "b": r3["stdout_tail"]}; _save(root, R)
    log(f"M1 restart: recall={vb['pass']} ({vb['failure_mode']}) ablated={vb0['pass']} ({vb0['failure_mode']}) -> {R['M_level']}")

def finalize(R, root: Path, log=print):
    R["SA4"]["pass"] = score.sa4_pass(R["SA4"], R["SA4"].get("n_expected", len([e for e in R["TH"] if e.get("forecast") is not None])))
    # profile and gate
    sa_level = "SA0"
    if all(x["pass"] for x in R["SA1"]): sa_level = "SA1"
    if sa_level == "SA1" and all(x["pass"] for x in R["SA2"]): sa_level = "SA2"
    i_level = "I0"
    if R["M_level"] == "M1": i_level = "I1"
    if i_level == "I1" and R["I2"]["transfer"] == 1: i_level = "I2 (evidence; M3 not certified)"
    prof = {"C": R["C_level"], "M": R["M_level"], "I": i_level.split(" ")[0] if not i_level.startswith("I2") else "I1", "I_note": i_level, "O": "N/A (individual)",
            "SA": sa_level, "SA4_calibration": R["SA4"], "T_frontier": score.frontier(R["TH"]), "H": "H0",
            "A_DI_net": score.net_surface(R["TH"]), "A_DI_gross": score.gross_surface(R["TH"]), "false_completions": sum(e["false_completion"] for e in R["TH"])}
    prof["U"] = score.gate(prof)
    A = {"C": {None: 0, "C0": 0.2, "C1": 0.4, "C2": 0.6, "C3": 0.8, "C4": 1.0}[prof["C"]], "I": {"I0": 0.2, "I1": 0.4}[prof["I"]] + (0.2 if R["I2"]["transfer"] == 1 else 0),
         "DI": (prof["A_DI_net"] or 0) / 100, "SA": {"SA0": 0.2, "SA1": 0.5, "SA2": 0.75}[sa_level] + (0.1 if R["SA4"]["pass"] else 0)}
    prof["HLIS"], prof["HLIS_dims"] = score.hlis(A); prof["achievement"] = A
    R["profile"] = prof; R["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    (root / "record.json").write_text(json.dumps(R, indent=1)); log("PROFILE " + json.dumps(prof)); return R

def rerun_m1(root: Path, exec_tmpl, limit=300, env=None, log=print, tag="r2"):
    """Rerun only the M1 phase of an existing agent record (after an item repair), into fresh sibling roots, and re-finalize."""
    R = json.loads((root / "record.json").read_text()); R.setdefault("M1_history", []).append(R.get("M1"))
    sub = Path(str(root) + "_" + tag); sub.mkdir(parents=True, exist_ok=True); phase_m1(R, exec_tmpl, sub, R["seeds"], limit, env, log); R["M1"]["rerun_root"] = str(sub)
    return finalize(R, root, log)

def run_llm(label, exec_tmpl, root: Path, seeds, limit=300, env=None, log=print):
    _fresh(root); R = {"label": label, "mode": "llm", "executor": exec_tmpl, "seeds": seeds, "rungs": {}}
    curve = {}
    for rung in ("HG0", "HG1", "HG2"):
        eps = []
        for fam, ss in [(f, seeds[:2]) for f in TH] + [(f, seeds[:1]) for f in HARD]:
            for s in ss:
                e = th_episode(fam, s, root, exec_tmpl, limit, env, rung); eps.append(e)
                log(f"{rung} {fam} s{s}: {'pass' if e['delivered_correct'] else 'FAIL'} fc={e['false_completion']} hb={e['held_back']} att={e['attempts']} {e['seconds']}s")
        R["rungs"][rung] = {"episodes": eps, "HLIS_DI_net": score.net_surface(eps), "HLIS_DI_gross": score.gross_surface(eps),
                            "false_completions": sum(e["false_completion"] for e in eps), "held_back": sum(e["held_back"] for e in eps), "seconds": round(sum(e["seconds"] for e in eps), 1)}
        curve[rung] = R["rungs"][rung]["HLIS_DI_net"]
    R["HIL"] = score.hil(curve); (root / "record.json").write_text(json.dumps(R, indent=1)); log("HIL " + json.dumps(R["HIL"])); return R

# ---------------------------------------------------------------- extended tier: T2-T5 from the dli_bench generators
EXT = [("t2.pipeline", "T2"), ("t3.search_latency", "T3"), ("t4.mini_language", "T4"), ("t5.hidden_law", "T5")]
EXT_LIMIT = {"T2": 1800, "T3": 3600, "T4": 1800, "T5": 7200}
EXT_PROMPT = {
    "t2.pipeline": "Read SPEC.md (and any GOAL.md) in this directory and implement what it describes, writing the deliverables it names. You may run python.",
    "t3.search_latency": "Read GOAL.md in this directory and do exactly what it says. You may run python and the project's own commands.",
    "t4.mini_language": "Read SPEC.md and examples.json in this directory and implement what SPEC.md describes in interp.py. You may run python to test it. Keep evaluate() from ever raising.",
    "t5.hidden_law": "Read GOAL.md in this directory and do exactly what it says: work out the generating rule from observations.json, write mechanism.txt, and write predictions.json for every point in predict_at.json. You may run python.",
}

def run_extended(label, exec_tmpl, root: Path, seeds, ai4science_path: str, env=None, log=print, t5_seeds=(0, 9)):
    """Bare (HG0) episodes on T2-T5 generator families; extends the T.H frontier of an agent record."""
    import sys as _sys
    _sys.path.insert(0, ai4science_path)
    from ai4science.harness.agents.dli_bench.tasks import GENERATORS
    root.mkdir(parents=True, exist_ok=True); build = root / "build"; eps = []
    for key, band in EXT:
        ss = list(t5_seeds) if band == "T5" else list(seeds[:1] if band == "T4" else seeds[:2])
        for s in ss:
            inst = build / key.replace(".", "_") / f"seed{s}"
            if not (inst / "keyed").exists():
                GENERATORS[key].instantiate(inst, s)
            ws = _ws(root, f"{key.replace('.', '_')}_s{s}"); shutil.rmtree(ws); shutil.copytree(inst / "work", ws)
            r = run_exec(exec_tmpl, EXT_PROMPT[key] + " Do not ask questions. Reply DONE when finished.", ws, EXT_LIMIT[band], env)
            v = GENERATORS[key].verify(ws, inst / "keyed"); ok = v.passed and r["termination_reason"] != "timed_out"
            eps.append({"family": key, "band": band, "seed": s, "budget": "H0", "rung": "HG0", "verifier_pass": v.passed, "delivered": True, "held_back": r["termination_reason"] == "timed_out",
                        "delivered_correct": ok, "false_completion": (not v.passed) and r["termination_reason"] != "timed_out", "metrics": {k: float(x) for k, x in v.metrics.items()},
                        "termination_reason": r["termination_reason"], "seconds": r["seconds"]})
            log(f"EXT {key} s{s}: {'pass' if ok else 'FAIL'} {r['termination_reason']} {r['seconds']}s {eps[-1]['metrics']}")
    rec = {"label": label, "mode": "extended", "executor": exec_tmpl, "episodes": eps}
    (root / "record.json").write_text(json.dumps(rec, indent=1)); return rec

def merge_extended(core_record: dict, ext_record: dict) -> dict:
    """Recompute the T.H surface and gate with the extended episodes appended."""
    eps = core_record["TH"] + ext_record["episodes"]
    prof = dict(core_record["profile"]); prof["T_frontier"] = score.frontier(eps); prof["A_DI_net_extended"] = score.net_surface(eps); prof["U"] = score.gate(prof)
    return prof
