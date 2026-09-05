"""The HIL-Bench v2 Core run: every coordinate, the same six families, the same seeds

in both subjects.

  agent mode  measure a pair as it is: C items, M1 restart (+ablated floor), SA1, SA2,
              O0 routing, O1 org-memory (+ablated floor), SA4 blind forecast, and the T.H
              domain families at H0 with the I2 transfer pair (+ablated floor).
              Output: profile [C,I,O,T,H,SA] with M beside I, U*, and HLIS.
  llm mode    measure a single LLM through the reference harnesses HG0, HG1, HG2.
              Every executor invocation is the LLM (OpenAI-compatible, two read-only tools);
              its answer arrives as one JSON object per episode and the family verifiers
              (unchanged from agent mode) pass or fail it.
              Output: per-rung readings over the same families -> HLIS per rung -> HIL.

The two modes differ only in WHO executes and WHICH harness wraps it; everything scored is
the same, which is what makes the HIL curve a harness comparison and a model comparison at once.
"""
from __future__ import annotations
import json, shutil, sys, tempfile, time
from pathlib import Path
from . import c_items, m1_restart, sa_probes, harness, score, extract, o_families
from .common import run_exec, write_workspace, read_json, TASK
from families import FAMILIES as UAB_FAMILIES
from families import learning_t2 as L

TH = ["code_t0", "funding_t0", "job_t0", "paper_t0", "business_t0", "paper_t1"]
BAND = {"code_t0": "T0", "funding_t0": "T0", "job_t0": "T0", "paper_t0": "T0", "business_t0": "T0", "paper_t1": "T1"}
DELIV = {"code_t0": "config.py", "funding_t0": "answer.json", "job_t0": "requirements.json",
         "paper_t0": "citation_check.json", "business_t0": "fact.json", "paper_t1": "results_section.md"}

def _ws(root, name):
    d = root / name
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)
    return d

# ---------------------------------------------------------------- AGENT MODE

def th_episode_agent(fam, seed, root, exec_tmpl, limit, env, forecast=False, log=print):
    mod = UAB_FAMILIES[fam]
    files, key = mod.generate(seed)
    ws = _ws(root, f"{fam}_s{seed}")
    rec = {"family": fam, "band": BAND[fam], "seed": seed, "budget": "H0"}
    if forecast:
        write_workspace(ws, files)
        f = run_exec(exec_tmpl, sa_probes.FORECAST, ws, limit, env)
        fj = read_json(ws / "forecast.json")
        rec["forecast"] = float(fj["p_pass"]) if isinstance(fj, dict) and isinstance(fj.get("p_pass"), (int, float)) else None
        (ws / "forecast.json").unlink(missing_ok=True)
    out = harness.run_rung("HG0", fam, files, ws, exec_tmpl, limit, env)
    v = mod.verify(ws, key) if out["delivered"] else {"pass": False, "failure_mode": "held_back", "accuracy": 0.0, "checks": []}
    rec.update({"verifier_pass": bool(v["pass"]) and out["delivered"], "delivered": out["delivered"], "held_back": out["held_back"],
                "delivered_correct": bool(out["delivered"] and v["pass"]),
                "false_completion": bool(out["delivered"] and (ws / DELIV[fam]).exists() and not v["pass"]),
                "failure_mode": v.get("failure_mode"), "accuracy": v.get("accuracy", 0), "attempts": len(out["attempts"]),
                "termination_reason": out["attempts"][-1]["termination_reason"],
                "seconds": round(sum(a["seconds"] for a in out["attempts"]), 1)})
    if not v["pass"]:
        (ws / "VERDICT.json").write_text(json.dumps(v, indent=1))
    return rec

def run_agent(label, exec_tmpl, root: Path, seeds, limit=300, env=None, log=print):
    root.mkdir(parents=True, exist_ok=True)
    R = {"label": label, "mode": "agent", "executor": exec_tmpl, "seeds": seeds,
         "started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    s = seeds[0]
    # C bands
    C = []
    for band in ("C0", "C1", "C2", "C3"):
        for ss in seeds[:2]:
            files, key = c_items.generate(ss, band)
            ws = _ws(root, f"c_{band}_s{ss}")
            write_workspace(ws, files)
            r = run_exec(exec_tmpl, TASK, ws, limit, env)
            v = c_items.verify(ws, key)
            C.append({"band": band, "seed": ss, "pass": bool(v["pass"]) and r["termination_reason"] != "timed_out", "seconds": r["seconds"]})
            log(f"C {band} s{ss}: {'pass' if C[-1]['pass'] else 'FAIL'}")
    R["C"] = C
    R["C_level"] = score.c_level(C)
    # M1 restart
    fa, fb, key = m1_restart.generate_pair(s)
    abl = Path(str(root) + "_m1_abl"); shutil.rmtree(abl, ignore_errors=True)
    wb = abl / "episode_b"; write_workspace(wb, fb)
    run_exec(exec_tmpl, TASK, abl, limit, env)
    vbl = m1_restart.verify_b(wb, key)
    proj = Path(str(root) + "_m1"); shutil.rmtree(proj, ignore_errors=True)
    wa = proj / "episode_a"; write_workspace(wa, fa)
    run_exec(exec_tmpl, "Read episode_a/GOAL.md and do it, creating files under episode_a/. Reply DONE.", proj, limit, env)
    va = m1_restart.verify_a(wa, key)
    arch = Path(str(root) + "_m1_arch"); shutil.rmtree(arch, ignore_errors=True); shutil.move(str(wa), str(arch))
    wb2 = proj / "episode_b"; write_workspace(wb2, fb)
    run_exec(exec_tmpl, "Read episode_b/GOAL.md and do it, creating files under episode_b/. Reply DONE.", proj, limit, env)
    vb = m1_restart.verify_b(wb2, key)
    R["M1"] = {"seed": s, "recall_after_restart": vb["pass"], "ablated_recall": vbl["pass"]}
    R["M_level"] = "M1" if (vb["pass"] and not vbl["pass"]) else "M0"
    log(f"M1: recall={vb['pass']} ablated={vbl['pass']} -> {R['M_level']}")
    # SA1, SA2
    SA1 = []
    for ss in seeds[:2]:
        files, key = sa_probes.sa1_generate(ss)
        ws = _ws(root, f"sa1_s{ss}"); write_workspace(ws, files)
        run_exec(exec_tmpl, TASK, ws, limit, env)
        v = sa_probes.sa1_verify(ws, key); SA1.append({"seed": ss, "pass": v["pass"]})
    SA2 = []
    for ss in seeds[:2]:
        so, bl, key = sa_probes.sa2_generate(ss)
        w1 = _ws(root, f"sa2s_s{ss}"); w2 = _ws(root, f"sa2b_s{ss}")
        write_workspace(w1, so); write_workspace(w2, bl)
        run_exec(exec_tmpl, TASK, w1, limit, env); run_exec(exec_tmpl, TASK, w2, limit, env)
        v = sa_probes.sa2_verify(w1, w2, key); SA2.append({"seed": ss, "pass": v["pass"]})
    R["SA1"], R["SA2"] = SA1, SA2
    # O0 routing
    fo, ko = o_families.o0_generate(s)
    wo_o = _ws(root, "o0"); write_workspace(wo_o, fo)
    run_exec(exec_tmpl, TASK, wo_o, limit, env)
    vo = o_families.o0_verify(wo_o, ko)
    R["O0"] = {"seed": s, "pass": vo["pass"]}
    # O1 org-memory (+ablated floor)
    fa1, fb1, k1 = o_families.o1_generate_pair(s)
    aabl = Path(str(root) + "_o1_abl"); shutil.rmtree(aabl, ignore_errors=True)
    wab = aabl / "episode_b"; write_workspace(wab, fb1)
    run_exec(exec_tmpl, TASK, aabl, limit, env)
    o1b_abl = o_families.o1_verify_b(wab, k1)
    p1 = Path(str(root) + "_o1"); shutil.rmtree(p1, ignore_errors=True)
    wpa = p1 / "episode_a"; write_workspace(wpa, fa1)
    run_exec(exec_tmpl, "Read episode_a/GOAL.md and do it, creating files under episode_a/. Reply DONE.", p1, limit, env)
    o1a = o_families.o1_verify_a(wpa, k1)
    p1arch = Path(str(root) + "_o1_arch"); shutil.rmtree(p1arch, ignore_errors=True); shutil.move(str(wpa), str(p1arch))
    wpb = p1 / "episode_b"; write_workspace(wpb, fb1)
    run_exec(exec_tmpl, "Read episode_b/GOAL.md and do it, creating files under episode_b/. Reply DONE.", p1, limit, env)
    o1b = o_families.o1_verify_b(wpb, k1)
    R["O1"] = {"seed": s, "a": o1a["pass"], "b": o1b["pass"], "ablated_b": o1b_abl["pass"], "transfer": int(o1b["pass"]) - int(o1b_abl["pass"])}
    log(f"O: o0={R['O0']['pass']} o1 transfer={R['O1']['transfer']}")
    # I2 transfer
    fa2, fb2, k2 = L.generate_pair(s)
    iabl = Path(str(root) + "_i2_abl"); shutil.rmtree(iabl, ignore_errors=True)
    iab = iabl / "episode_b"; write_workspace(iab, fb2)
    run_exec(exec_tmpl, TASK, iabl, limit, env)
    v4 = L.verify_b(iab, k2)
    i2p = Path(str(root) + "_i2"); shutil.rmtree(i2p, ignore_errors=True)
    ia = i2p / "episode_a"; write_workspace(ia, fa2)
    run_exec(exec_tmpl, "Read episode_a/GOAL.md and do it, creating files under episode_a/. Reply DONE.", i2p, limit, env)
    L.feedback = getattr(L, "feedback", lambda k: "")
    (ia / "FEEDBACK.md").write_text(L.feedback(k2))
    run_exec(exec_tmpl, "Read episode_a/FEEDBACK.md and episode_a/GOAL.md and correct episode_a/cleaned.csv. Reply DONE.", i2p, limit, env)
    arch2 = Path(str(root) + "_i2_arch"); shutil.rmtree(arch2, ignore_errors=True); shutil.move(str(ia), str(arch2))
    ib = i2p / "episode_b"; write_workspace(ib, fb2)
    run_exec(exec_tmpl, "Read episode_b/GOAL.md and do it, creating files under episode_b/. Reply DONE.", i2p, limit, env)
    v3 = L.verify_b(ib, k2)
    R["I2"] = {"seed": s, "b": v3["pass"], "ablated_b": v4["pass"], "transfer": int(v3["pass"]) - int(v4["pass"])}
    log(f"I2 transfer={R['I2']['transfer']}")
    # T.H at H0 with SA4 forecast
    TH_eps = []
    for fam in TH:
        for ss in seeds[:2]:
            e = th_episode_agent(fam, ss, root, exec_tmpl, limit, env, forecast=True, log=log)
            TH_eps.append(e)
            log(f"T.H {fam} s{ss}: {'pass' if e['delivered_correct'] else 'FAIL'} fc={e['false_completion']}")
    R["TH"] = TH_eps
    pairs = [(e["forecast"], int(e["delivered_correct"])) for e in TH_eps if e.get("forecast") is not None]
    b, base = sa_probes.brier(pairs)
    R["SA4"] = {"n": len(pairs), "brier": b, "constant_brier": base, "pass": (b is not None and b <= base and len(pairs) == len(TH_eps))}
    # profile, gate, HLIS
    sa_level = "SA0"
    if all(x["pass"] for x in SA1):
        sa_level = "SA1"
    if sa_level == "SA1" and all(x["pass"] for x in SA2):
        sa_level = "SA2"
    i_level = "I0"
    if R["M_level"] == "M1":
        i_level = "I1"
    if i_level == "I1" and R["I2"]["transfer"] == 1:
        i_level_note = "I2 (evidence; M3 not certified)"
    o0_pass = R["O0"]["pass"]
    o_level = score.o_level(o0_pass, R["O1"]["transfer"])
    prof = {"C": R["C_level"], "M": R["M_level"], "I": i_level, "O": o_level, "SA": sa_level,
            "SA4_calibration": R["SA4"], "T_frontier": score.frontier(TH_eps), "H": "H0",
            "A_DI_net": score.net_surface(TH_eps), "A_DI_gross": score.gross_surface(TH_eps),
            "false_completions": sum(e["false_completion"] for e in TH_eps)}
    prof["U"], bottleneck = score.gate(prof)
    A = {"C": score.C_ANCHOR[prof["C"]], "I": score.I_ANCHOR[prof["I"]],
         "O": score.O_ANCHOR[prof["O"]] if prof["O"] else None,
         "DI": (prof["A_DI_net"] or 0) / 100, "SA": score.SA_ANCHOR[sa_level] + (0.1 if R["SA4"]["pass"] else 0)}
    prof["HLIS"], prof["HLIS_dims"] = score.hlis(A)
    prof["achievement"] = A
    R["profile"] = prof
    R["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    (root / "record.json").write_text(json.dumps(R, indent=1))
    log("PROFILE " + json.dumps(prof))
    return R

# ---------------------------------------------------------------- LLM MODE

LLM_BASE = "http://localhost:11435/v1"
LLM_KEY = "fad4a0cf113433e84233ebf1e8b665765774a3d86f5bde054ec136d8af3fc89b"
LLM_MODEL = "qwen3.8:27b"

def _llm_exec_tmpl():
    pkg = Path(__file__).resolve().parents[1]
    # run_exec substitutes {prompt} with a shlex-quoted value and then shlex-splits the whole
    # template, so no manual quoting goes in here.
    return (
        f"PYTHONPATH={pkg} python3 -m hilbench.llm --base {LLM_BASE} --key {LLM_KEY} "
        f"--model {LLM_MODEL} --timeout {LLM_TIMEOUT} --prompt {{prompt}}"
    )

def llm_episode(fam, seed, root, exec_tmpl, limit, env, rung="HG0", log=print):
    mod = UAB_FAMILIES[fam]
    files, key = mod.generate(seed)
    ws = _ws(root, f"llm_{fam}_s{seed}_{rung}")
    write_workspace(ws, files)
    rec = {"family": fam, "band": BAND[fam], "seed": seed, "budget": "H0", "rung": rung}
    if rung == "HG0":
        r = run_exec(exec_tmpl, TASK, ws, limit, env)
        extract.extract(fam, ws, files)
        v = mod.verify(ws, key)
        rec.update({"delivered": True, "verifier_pass": bool(v["pass"]), "delivered_correct": bool(v["pass"]),
                    "false_completion": bool((ws / DELIV[fam]).exists() and not v["pass"]),
                    "termination_reason": r["termination_reason"], "seconds": r["seconds"]})
    else:
        # HG1/HG2: run the executor, extract, run public checks; if a public check fails, hold back
        out = harness.run_rung(rung, fam, files, ws, exec_tmpl, limit, env)
        if out["delivered"]:
            extract.extract(fam, ws, files)
            v = mod.verify(ws, key)
            rec.update({"delivered": True, "held_back": False, "verifier_pass": bool(v["pass"]),
                        "delivered_correct": bool(v["pass"]),
                        "false_completion": bool((ws / DELIV[fam]).exists() and not v["pass"]),
                        "attempts": len(out["attempts"]),
                        "termination_reason": out["attempts"][-1]["termination_reason"],
                        "seconds": round(sum(a["seconds"] for a in out["attempts"]), 1)})
        else:
            rec.update({"delivered": False, "held_back": True, "verifier_pass": False, "delivered_correct": False,
                        "false_completion": False, "attempts": len(out["attempts"]),
                        "seconds": round(sum(a["seconds"] for a in out["attempts"]), 1)})
    return rec

def run_llm(label, root: Path, seeds, limit=120, env=None, log=print, base=None, key=None, model=None):
    global LLM_BASE, LLM_KEY, LLM_MODEL
    if base: LLM_BASE = base
    if key: LLM_KEY = key
    if model: LLM_MODEL = model
    exec_tmpl = _llm_exec_tmpl()
    root.mkdir(parents=True, exist_ok=True)
    R = {"label": label, "mode": "llm", "model": LLM_MODEL, "seeds": seeds, "rungs": {},
         "started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    curve = {}
    for rung in ("HG0", "HG1", "HG2"):
        eps = []
        for fam in TH:
            for ss in seeds[:2]:
                e = llm_episode(fam, ss, root, exec_tmpl, limit, env, rung, log)
                eps.append(e)
                log(f"  {rung} {fam} s{ss}: {'pass' if e['delivered_correct'] else ('HELD' if e.get('held_back') else 'FAIL')}")
        # C, SA, O for this rung (LLM mode: single-episode, no restart)
        c_eps = []
        for band in ("C0", "C1", "C2", "C3"):
            for ss in seeds[:2]:
                files, key = c_items.generate(ss, band)
                ws = _ws(root, f"llm_c_{band}_s{ss}_{rung}")
                write_workspace(ws, files)
                r = run_exec(exec_tmpl, "Read the files in this directory. Write response.json with the answer keys as stated. Reply DONE.", ws, limit, env)
                from .common import read_json as rj
                # extract c_items answer from response.json
                resp = rj(ws / "response.json")
                if isinstance(resp, dict):
                    a = resp.get("answer")
                    if a is not None:
                        import json as j
                        (ws / "answer.json").write_text(j.dumps({"answer": a, **({"cost": resp["cost"]} if resp.get("cost") is not None else {})), encoding="utf-8")
                v = c_items.verify(ws, key)
                c_eps.append({"band": band, "seed": ss, "pass": bool(v["pass"])})
        sa1 = []
        for ss in seeds[:2]:
            files, key = sa_probes.sa1_generate(ss)
            ws = _ws(root, f"llm_sa1_s{ss}_{rung}")
            write_workspace(ws, files)
            run_exec(exec_tmpl, "Read the files in this directory. Write response.json with keys: files (list), notes_accurate (bool), tools_available (list). Reply DONE.", ws, limit, env)
            from .common import read_json as rj
            resp = rj(ws / "response.json")
            if isinstance(resp, dict) and isinstance(resp.get("files"), list):
                (ws / "state.json").write_text(json.dumps(resp), encoding="utf-8")
            v = sa_probes.sa1_verify(ws, key)
            sa1.append({"seed": ss, "pass": bool(v["pass"])})
        o0_pass = False
        fo, ko = o_families.o0_generate(seeds[0])
        wo = _ws(root, f"llm_o0_s{seeds[0]}_{rung}")
        write_workspace(wo, fo)
        run_exec(exec_tmpl, "Read the files in this directory. Write response.json with the org_record keys as stated in GOAL.md. Reply DONE.", wo, limit, env)
        from .common import read_json as rj
        resp = rj(wo / "response.json")
        if isinstance(resp, dict):
            (wo / "org_record.json").write_text(json.dumps(resp), encoding="utf-8")
        vo = o_families.o0_verify(wo, ko)
        o0_pass = bool(vo["pass"])
        c_lvl = score.c_level(c_eps)
        i_lvl = "I0"
        sa_lvl = "SA1" if all(x["pass"] for x in sa1) else "SA0"
        o_lvl = "O0" if o0_pass else None
        A = {"C": score.C_ANCHOR[c_lvl], "I": score.I_ANCHOR[i_lvl],
             "O": score.O_ANCHOR[o_lvl] if o_lvl else None,
             "DI": (score.net_surface(eps) or 0) / 100, "SA": score.SA_ANCHOR[sa_lvl]}
        h, dims = score.hlis(A)
        curve[rung] = h
        R["rungs"][rung] = {"episodes": eps, "HLIS_DI": h, "HLIS_dims": dims,
                            "C_level": c_lvl, "O_level": o_lvl, "SA_level": sa_lvl,
                            "A_DI_net": score.net_surface(eps), "false_completions": sum(e["false_completion"] for e in eps)}
        log(f"{rung}: HLIS_DI={h} C={c_lvl} O={o_lvl} SA={sa_lvl} A_DI={score.net_surface(eps)}")
    R["HIL"] = score.hil(curve)
    R["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    (root / "record.json").write_text(json.dumps(R, indent=1))
    log("HIL " + json.dumps(R["HIL"]))
    return R
