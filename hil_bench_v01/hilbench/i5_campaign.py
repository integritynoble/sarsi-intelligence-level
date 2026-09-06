"""I5-DISC on the cancer field agent: one development-bound discovery campaign.

    z_I5 = U * H * E * L * V * P * K5

U  the unknown is the field's own, recorded in its document: the site-disjoint external drop of the TCGA-LUAD
   prognostic model -- is it the model reading the hospital, or the held-out case mix? Nobody has checked.
H  the pair must state >= 2 competing hypotheses, each with the probe that would discriminate it.
E  probes are chosen and run by the pair (Cox fits and statistics on discovery seeds 0-3), budget 12.
L  lineage.json links every probe to a hypothesis and an evidence value and says kept / rejected.
V  the finding is a machine-checkable prediction about SEALED seeds 4-11 the pair never saw, scored by this
   module and not by the pair: the sign and minimum strength of a correlation between a named per-seed
   statistic and the external drop, across fresh default fits.
   Consolidation is permitted only after V passes; then a real restart (episode A removed).
P  hidden transfer on seeds 12-15: the discovery arm (same project root, its memory intact) and a control
   arm (fresh root from the same pre-discovery checkpoint) each choose and fit a model for a new split;
   Q = external C-index scored by the benchmark's own statistic; delta_inc = mean(Q_disc - Q_ctrl) >= delta.
K5 I0-I4 retention: this pair has no certified I3 or I4, so K5 = 0 and z_I5 = 0 by the cumulative law; the
   discovery-specific factors are reported on their own. That is the honest outcome, not a defect.
"""
from __future__ import annotations
import json, os, shutil, subprocess, sys, time
from pathlib import Path
import numpy as np
from .common import run_exec, read_json

AI4 = Path(os.environ.get("AI4SCIENCE_PKG", "/home/spiritai/pwm/Physics_World_Model/AI4Science"))
PY = str(AI4 / ".venv" / "bin" / "python") if (AI4 / ".venv" / "bin" / "python").exists() else sys.executable
ONCO = AI4 / "ai4science" / "harness" / "agents" / "research_agents" / "runners" / "payload" / "onco"
DISC_SEEDS, SEALED_SEEDS, TRANSFER_SEEDS = list(range(0, 4)), list(range(4, 12)), list(range(12, 16))
STATS = ("stage_mix_distance", "age_mix_distance", "male_mix_distance", "prior_mix_distance", "ext_n", "ext_event_rate", "dev_event_rate", "event_rate_gap", "ext_n_sites",
         "beta_shift", "stage_beta_ext", "stage_beta_dev")   # v0.3: coefficient statistics, so a mechanism claim about non-transport can be staked on sealed seeds
DELTA_INC = 0.01     # preregistered minimum mean gain in external C-index for the incorporation gate (development value)

# ---------------------------------------------------------------- the benchmark's own statistics (independent of the pair)
def c_index(risk, time, event):
    n = 0; conc = 0.0
    for i in range(len(time)):
        if event[i] != 1: continue
        for j in range(len(time)):
            if time[j] > time[i]:
                n += 1; conc += 1.0 if risk[i] > risk[j] else (0.5 if risk[i] == risk[j] else 0.0)
    return conc / n if n else float("nan")

def _cox_fit():
    import importlib.util
    spec = importlib.util.spec_from_file_location("onco_run_solver", ONCO / "run_solver.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.cox_fit

def coefficient_stats(ws: Path) -> dict:
    """The development fit and an ORACLE refit on the external cohort itself (its outcomes are the verifier's to use):
    beta_shift = ||beta_ext - beta_dev||, and the stage coefficient in each. Columns: age, male, stage, prior."""
    d = lambda n: np.load(ws / "data" / (n + ".npy")); cox = _cox_fit()
    bd = cox(d("dev_X"), d("dev_time"), d("dev_event")); be = cox(d("ext_X"), d("ext_time"), d("ext_event"))
    return {"beta_shift": float(np.linalg.norm(be - bd)), "stage_beta_ext": float(be[2]), "stage_beta_dev": float(bd[2])}

def per_seed_stats(ws: Path) -> dict:
    d = lambda n: np.load(ws / "data" / (n + ".npy"))
    Xd, Xe = d("dev_X"), d("ext_X")                     # standardized on dev; columns age, male, stage, prior
    ed, ee = d("dev_event"), d("ext_event")
    with open(ws / "meta.json") as f: meta = json.load(f)
    return {"stage_mix_distance": float(abs(Xe[:, 2].mean() - Xd[:, 2].mean())), "age_mix_distance": float(abs(Xe[:, 0].mean() - Xd[:, 0].mean())),
            "male_mix_distance": float(abs(Xe[:, 1].mean() - Xd[:, 1].mean())), "prior_mix_distance": float(abs(Xe[:, 3].mean() - Xd[:, 3].mean())),
            "ext_n": float(len(ee)), "ext_event_rate": float(ee.mean()), "dev_event_rate": float(ed.mean()), "event_rate_gap": float(abs(ee.mean() - ed.mean())),
            "ext_n_sites": float(len(meta.get("held_out_sites", []))), **coefficient_stats(ws)}

def default_fit_drop(ws: Path) -> dict:
    """Fit the reference solver at its defaults and return internal, external C-index and the drop."""
    run = ws / "_default_fit"; shutil.rmtree(run, ignore_errors=True); shutil.copytree(ws / "data", run / "data")
    subprocess.run([PY, str(ONCO / "run_solver.py"), "--workspace", str(run)], check=True, capture_output=True)
    d = lambda n: np.load(ws / "data" / (n + ".npy")); r = lambda n: np.load(run / "results" / (n + ".npy"))
    ci, ce = c_index(r("risk_dev"), d("dev_time"), d("dev_event")), c_index(r("risk_ext"), d("ext_time"), d("ext_event"))
    return {"c_internal": ci, "c_external": ce, "external_drop": ci - ce}

def make_seed_ws(root: Path, seed: int) -> Path:
    ws = root / f"seed{seed}"; ws.mkdir(parents=True, exist_ok=True)
    out = subprocess.run([PY, str(ONCO / "generate.py"), "--workspace", str(ws), "--seed", str(seed)], capture_output=True, text=True,
                         env={**os.environ, "AI4SCIENCE_PKG": str(AI4)}, check=True)
    (ws / "meta.json").write_text(out.stdout.strip().splitlines()[-1]); return ws

# ---------------------------------------------------------------- episode A: discovery
GOAL_A = """# GOAL (episode A: discovery)

You are the cancer field agent. The prognostic model here (Cox on age, sex, stage, prior malignancy; `solver/run_solver.py`)
is developed on TCGA-LUAD cases from two thirds of the contributing hospitals and validated on the held-out third
(`seeds/seedN/data`, `seeds/seedN/meta.json`). Its C-index falls from internal to external, and by different amounts on
different seeds. **The field does not know what that site-disjoint drop is made of** -- is the model reading the hospital
(site-level hazard the covariates do not carry), or is it the held-out case mix (a different stage/age/event-rate
distribution), or something else the data here can show? Nobody has checked. Find out.

Rules of the campaign (they are checked):
1. Write `hypotheses.json`: a list of at least TWO competing hypotheses, each `{"id", "statement", "discriminating_probe"}`
   -- a probe the data in `seeds/` can run that would come out differently under this hypothesis than under the others.
2. Run your probes yourself on discovery seeds 0-3 ONLY (you may run `python solver/run_solver.py --workspace <copy>`
   with a `params.json`, write your own fits, compute statistics with `stats.py`, permute site labels, reweight, etc.).
   Budget: at most 12 probes. Record every probe in `lineage.json` as
   `{"probe", "hypothesis_ids", "command_or_method", "evidence": <number or short fact>, "verdict": "supports"|"refutes"|"inconclusive"}`.
3. Write `finding.json`:
   `{"claim": "<one sentence>", "prediction": {"statistic": <one of %s>, "sign": "+"|"-", "min_abs_r": <0.3..0.9>},
     "rejected_alternatives": [<hypothesis ids you refuted and why>], "mechanism": "<why, in the field's terms>"}`.
   The prediction is a SEALED-CASE test: on seeds you have never seen, an independent verifier will compute the named
   per-seed statistic (see `stats.py`) and the external drop of the default fit, and check the sign and strength of their
   correlation. Predict only what your evidence supports; a claim that fails the sealed test is recorded as refuted.
Do not modify `solver/` or `stats.py`. Do not ask questions. Reply DONE when finished.
""" % (list(STATS),)

STATS_PY = '''"""Per-seed statistics the independent verifier computes. Use the same ones so your prediction is checkable."""
import json, sys, numpy as np
from pathlib import Path
def per_seed_stats(ws):
    ws = Path(ws); d = lambda n: np.load(ws / "data" / (n + ".npy")); Xd, Xe = d("dev_X"), d("ext_X"); ed, ee = d("dev_event"), d("ext_event")
    meta = json.load(open(ws / "meta.json"))
    return {"stage_mix_distance": float(abs(Xe[:,2].mean()-Xd[:,2].mean())), "age_mix_distance": float(abs(Xe[:,0].mean()-Xd[:,0].mean())),
            "male_mix_distance": float(abs(Xe[:,1].mean()-Xd[:,1].mean())), "prior_mix_distance": float(abs(Xe[:,3].mean()-Xd[:,3].mean())),
            "ext_n": float(len(ee)), "ext_event_rate": float(ee.mean()), "dev_event_rate": float(ed.mean()), "event_rate_gap": float(abs(ee.mean()-ed.mean())),
            "ext_n_sites": float(len(meta.get("held_out_sites", []))), **coefficient_stats(ws)}
def coefficient_stats(ws):
    """Oracle refit on the external cohort (its outcomes are visible on discovery seeds) against the development fit."""
    import importlib.util; ws = Path(ws)
    spec = importlib.util.spec_from_file_location("rs", Path(__file__).resolve().parent / "solver" / "run_solver.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    d = lambda n: np.load(ws / "data" / (n + ".npy")); bd = m.cox_fit(d("dev_X"), d("dev_time"), d("dev_event")); be = m.cox_fit(d("ext_X"), d("ext_time"), d("ext_event"))
    return {"beta_shift": float(np.linalg.norm(be - bd)), "stage_beta_ext": float(be[2]), "stage_beta_dev": float(bd[2])}
def c_index(risk, time, event):
    n = 0; conc = 0.0
    for i in range(len(time)):
        if event[i] != 1: continue
        for j in range(len(time)):
            if time[j] > time[i]: n += 1; conc += 1.0 if risk[i] > risk[j] else (0.5 if risk[i] == risk[j] else 0.0)
    return conc / n if n else float("nan")
if __name__ == "__main__":
    print(json.dumps(per_seed_stats(sys.argv[1]), indent=1))
'''

def _check_A(ws: Path) -> dict:
    hyp = read_json(ws / "hypotheses.json"); lin = read_json(ws / "lineage.json"); fin = read_json(ws / "finding.json")
    H = isinstance(hyp, list) and len(hyp) >= 2 and all(isinstance(h, dict) and h.get("discriminating_probe") for h in hyp)
    probes = [x for x in (lin if isinstance(lin, list) else []) if isinstance(x, dict) and x.get("hypothesis_ids") and x.get("verdict")]
    E = 3 <= len(probes) <= 12 and any(x.get("evidence") not in (None, "") for x in probes)
    L = E and any(x.get("verdict") == "refutes" for x in probes) and isinstance(fin, dict) and bool(fin.get("rejected_alternatives"))
    pred = (fin or {}).get("prediction") if isinstance(fin, dict) else None
    well_formed = isinstance(pred, dict) and pred.get("statistic") in STATS and pred.get("sign") in ("+", "-") and isinstance(pred.get("min_abs_r"), (int, float)) and 0.3 <= pred["min_abs_r"] <= 0.9
    return {"H": int(bool(H)), "E": int(bool(E)), "L": int(bool(L)), "finding_well_formed": int(bool(well_formed)), "n_hypotheses": len(hyp) if isinstance(hyp, list) else 0, "n_probes": len(probes), "finding": fin}

def _sealed_validation(root: Path, pred: dict) -> dict:
    xs, ys, rows = [], [], []
    for s in SEALED_SEEDS:
        ws = make_seed_ws(root / "sealed", s); st = per_seed_stats(ws); fit = default_fit_drop(ws)
        xs.append(st[pred["statistic"]]); ys.append(fit["external_drop"]); rows.append({"seed": s, **st, **fit})
    x, y = np.array(xs), np.array(ys)
    r = float(np.corrcoef(x, y)[0, 1]) if x.std() > 0 and y.std() > 0 else 0.0
    ok = (r > 0 if pred["sign"] == "+" else r < 0) and abs(r) >= pred["min_abs_r"]
    return {"V": int(ok), "r": r, "n": len(xs), "rows": rows}

# ---------------------------------------------------------------- episode B: hidden transfer
GOAL_B = """# GOAL (episode B)

You are the cancer field agent. `seed/data` is a NEW site-disjoint split of the TCGA-LUAD cohort (`seed/meta.json`), with
the external cohort's covariates (`ext_X.npy`) visible and its outcomes hidden from you. Fit a prognostic model on the
development cohort and deliver `results/risk_ext.npy` (one risk score per external case, higher = higher risk) so that the
external C-index is as high as you can make it. You may use `solver/run_solver.py` with a `params.json`, or write your own
fit. Also write `choice.json` as `{"approach": "<what you did and why>", "predicted_external_drop": <number>}`.
Do not ask questions. Reply DONE when finished.
"""

def _transfer_arm(root: Path, seed_ws: Path, exec_tmpl, limit, env, tag: str) -> dict:
    proj = root; ep = proj / f"episode_b_{tag}"; shutil.rmtree(ep, ignore_errors=True); (ep / "seed").mkdir(parents=True)
    shutil.copytree(seed_ws / "data", ep / "seed" / "data"); shutil.copy(seed_ws / "meta.json", ep / "seed" / "meta.json")
    # outcomes of the external cohort are hidden from the pair
    for n in ("ext_time", "ext_event"): (ep / "seed" / "data" / (n + ".npy")).unlink()
    shutil.copytree(ONCO, ep / "solver", ignore=shutil.ignore_patterns("__pycache__")); (ep / "GOAL.md").write_text(GOAL_B)
    r = run_exec(exec_tmpl, f"Read {ep.name}/GOAL.md in this project and do exactly what it says, working under {ep.name}/. Do not ask questions. Reply DONE when finished.", proj, limit, env)
    d = lambda n: np.load(seed_ws / "data" / (n + ".npy"))
    p = ep / "results" / "risk_ext.npy"; q = float("nan")
    if p.exists() and r["termination_reason"] != "timed_out":
        risk = np.load(p)
        if risk.shape == d("ext_time").shape: q = c_index(risk, d("ext_time"), d("ext_event"))
    return {"seed": int(seed_ws.name[4:]), "arm": tag, "Q": q, "termination": r["termination_reason"], "seconds": r["seconds"], "choice": read_json(ep / "choice.json")}

def rerun_transfer(root: Path, exec_tmpl: str, limit_B=600, env=None, log=print, staged_from: Path | None = None):
    """Re-run only the transfer arms of an existing campaign whose finding was validated (V=1). If the consolidated note
    never reached the project root (the first run's apparatus failure), the note the PAIR ITSELF wrote -- verbatim, from
    the archived staging directory -- is restored as the project memory (CLAUDE.md + MEMORY/) before the arms run. Nothing
    is authored by the runner. The control arm is re-run too, so both arms face the same day."""
    R = json.loads((root / "record.json").read_text()); disc = Path(str(root) + "_disc"); ctrl = Path(str(root) + "_ctrl")
    assert R["V"]["V"] == 1, "transfer is only meaningful after validation"
    if staged_from and staged_from.exists() and not (disc / "CLAUDE.md").exists():
        notes = sorted(p for p in staged_from.glob("*.md")); (disc / "MEMORY").mkdir(exist_ok=True)
        body = "\n\n".join(p.read_text(encoding="utf-8") for p in notes)
        (disc / "CLAUDE.md").write_text("# Project memory (consolidated by this agent after independent validation)\n\n" + body)
        for p in notes: shutil.copy(p, disc / "MEMORY" / p.name)
        R.setdefault("consolidation", {})["restored_from_staging"] = [p.name for p in notes]; log(f"restored the pair's own staged notes into {disc/'CLAUDE.md'}: {[p.name for p in notes]}")
    R.setdefault("B_history", []).append(R.get("B")); rows = []
    for s in TRANSFER_SEEDS:
        ws = root / "transfer_seeds" / f"seed{s}"
        rows.append(_transfer_arm(ctrl, ws, exec_tmpl, limit_B, env, "ctrl")); log(f"B ctrl seed{s}: Q={rows[-1]['Q']:.4f} {rows[-1]['termination']}")
        rows.append(_transfer_arm(disc, ws, exec_tmpl, limit_B, env, "disc")); log(f"B disc seed{s}: Q={rows[-1]['Q']:.4f} {rows[-1]['termination']}")
    qd = np.array([r["Q"] for r in rows if r["arm"] == "disc"]); qc = np.array([r["Q"] for r in rows if r["arm"] == "ctrl"])
    delta = float(np.nanmean(qd - qc)); P = int(delta >= DELTA_INC and np.isfinite(delta))
    R["B"] = rows; R["P"] = {"P": P, "delta_inc": delta, "Q_disc": [float(x) for x in qd], "Q_ctrl": [float(x) for x in qc], "delta_min": DELTA_INC, "n": len(qd), "note": "transfer re-run with the consolidated note in the project root; no confidence bound at n=4"}
    R["factors"]["P"] = P; R["z_I5"] = 0; R["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    (root / "record.json").write_text(json.dumps(R, indent=1, default=float)); log("I5 " + json.dumps(R["factors"]) + f" delta_inc={delta:.4f} z_I5=0 (K5=0)"); return R

def run_i5(label: str, exec_tmpl: str, root: Path, limit_A=1800, limit_B=600, env=None, log=print):
    root.mkdir(parents=True); R = {"label": label, "mode": "i5-campaign", "field": "cancer", "executor": exec_tmpl, "law": "z_I5 = U*H*E*L*V*P*K5 (dev-bound)",
                                    "unknown": "what the site-disjoint external drop of the TCGA-LUAD prognostic model is made of", "started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    # --- checkpoint: the pre-discovery project root (control arm is cloned from this state: solver + nothing else)
    disc = Path(str(root) + "_disc"); ctrl = Path(str(root) + "_ctrl"); ep = disc / "episode_a"; (ep / "seeds").mkdir(parents=True)
    shutil.copytree(ONCO, ep / "solver", ignore=shutil.ignore_patterns("__pycache__")); (ep / "stats.py").write_text(STATS_PY); (ep / "GOAL.md").write_text(GOAL_A)
    for s in DISC_SEEDS:
        ws = make_seed_ws(root / "disc_seeds", s); shutil.copytree(ws / "data", ep / "seeds" / f"seed{s}" / "data"); shutil.copy(ws / "meta.json", ep / "seeds" / f"seed{s}" / "meta.json")
    R["U"] = {"value": 1, "note": "the unknown is the field's, recorded in docs/research-agents/cancer.md; it is not an item the instrument invented"}
    log("A: discovery episode"); rA = run_exec(exec_tmpl, "Read episode_a/GOAL.md in this project and do exactly what it says, working under episode_a/. Do not ask questions. Reply DONE when finished.", disc, limit_A, env)
    A = _check_A(ep); A["termination"] = rA["termination_reason"]; A["seconds"] = rA["seconds"]; R["A"] = A
    log(f"A: H={A['H']} E={A['E']} L={A['L']} well_formed={A['finding_well_formed']} probes={A['n_probes']} {rA['termination_reason']} {rA['seconds']}s")
    # --- V: sealed validation by this module, never by the pair
    V = {"V": 0, "note": "finding not well formed"}
    if A["finding_well_formed"]:
        V = _sealed_validation(root, A["finding"]["prediction"]); log(f"V: r={V['r']:.3f} on {V['n']} sealed seeds -> {'PASS' if V['V'] else 'FAIL'} (claimed sign {A['finding']['prediction']['sign']}, |r|>={A['finding']['prediction']['min_abs_r']})")
    R["V"] = {k: v for k, v in V.items() if k != "rows"}; R["V_rows"] = V.get("rows")
    # --- consolidation only after validation; then the discontinuity
    if V["V"]:
        # The declared consolidation machinery is harness-native: Claude Code loads CLAUDE.md at the project root on every start.
        # The first run of this campaign let the pair choose where to persist; the sandbox refused its memory directory and it
        # staged the note inside episode_a, which the restart then removed -- an apparatus failure that read as P = 0.
        (ep / "VALIDATED.md").write_text("Your finding was validated on sealed seeds by an independent verifier (r=%.3f, n=%d). Consolidate it now: write the claim, the mechanism, the evidence that survived, and what it implies for fitting a prognostic model on a NEW site-disjoint split of this cohort into the project memory file `%s` (create it; it is loaded automatically at the start of every future session in this project) and, in more detail, into `%s`. Do not write it under episode_a/, which will be removed. Then reply DONE.\n" % (V["r"], V["n"], disc / "CLAUDE.md", disc / "MEMORY" / "luad-site-drop.md"))
        (disc / "MEMORY").mkdir(exist_ok=True)
        rC = run_exec(exec_tmpl, "Read episode_a/VALIDATED.md in this project and do exactly what it says. Do not ask questions. Reply DONE when finished.", disc, 300, env)
        R["consolidation"] = {"termination": rC["termination_reason"], "seconds": rC["seconds"]}
    arch = Path(str(root) + "_archive_a"); shutil.rmtree(arch, ignore_errors=True); shutil.move(str(ep), str(arch))   # the discontinuity: episode A is gone
    # --- P: hidden transfer, discovery arm vs control from the same checkpoint
    ctrl.mkdir(parents=True, exist_ok=True); rows = []
    for s in TRANSFER_SEEDS:
        ws = make_seed_ws(root / "transfer_seeds", s)
        rows.append(_transfer_arm(ctrl, ws, exec_tmpl, limit_B, env, "ctrl")); log(f"B ctrl seed{s}: Q={rows[-1]['Q']:.4f} {rows[-1]['termination']}")
        rows.append(_transfer_arm(disc, ws, exec_tmpl, limit_B, env, "disc")); log(f"B disc seed{s}: Q={rows[-1]['Q']:.4f} {rows[-1]['termination']}")
    qd = np.array([r["Q"] for r in rows if r["arm"] == "disc"]); qc = np.array([r["Q"] for r in rows if r["arm"] == "ctrl"])
    delta = float(np.nanmean(qd - qc)); P = int(V["V"] == 1 and delta >= DELTA_INC and np.isfinite(delta))
    R["B"] = rows; R["P"] = {"P": P, "delta_inc": delta, "Q_disc": [float(x) for x in qd], "Q_ctrl": [float(x) for x in qc], "delta_min": DELTA_INC, "n": len(qd), "note": "no confidence bound at n=4; development gate on the mean"}
    R["K5"] = {"K5": 0, "note": "I3 and I4 are not certified for this pair; the cumulative law sets K5 = 0"}
    z = R["U"]["value"] * A["H"] * A["E"] * A["L"] * V["V"] * P * 0
    R["z_I5"] = z; R["factors"] = {"U": 1, "H": A["H"], "E": A["E"], "L": A["L"], "V": V["V"], "P": P, "K5": 0}
    R["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()); (root / "record.json").write_text(json.dumps(R, indent=1, default=float))
    log("I5 " + json.dumps(R["factors"]) + f" delta_inc={delta:.4f} z_I5={z}"); return R
