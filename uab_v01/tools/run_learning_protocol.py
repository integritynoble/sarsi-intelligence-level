#!/usr/bin/env python3
"""Run the U2 learning-transfer protocol against a real executor.

  python3 tools/run_learning_protocol.py --seed 7 --exec 'claude -p {prompt} --permission-mode acceptEdits --allowedTools Read,Edit,Write,Glob,Grep' --root DIR

Arms:
  experienced  episode A (attempt 1 -> verify -> FEEDBACK.md -> attempt 2 -> verify), then A's workspace is
               deleted, then episode B in a new directory under the SAME project root, in a new process.
  ablated      episode B only, run FIRST, under a separate project root, so a per-project memory store
               starts empty and nothing from the other arm exists anywhere on disk yet.
               (For executors whose store is not per-project, pass --ablate-cmd to reset it.)

Every invocation runs in its own session/process group with an enforced limit; a killed run is recorded
as timed_out, never as a delivery. The record is written to <root>/record.json.
"""
from __future__ import annotations
import argparse, json, os, shlex, shutil, signal, subprocess, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from families import learning_t2 as L
from families.common import write_workspace

PROMPT_A1 = "Read episode_a/GOAL.md in this project and do exactly what it says, creating files under episode_a/. Do not ask questions. Reply DONE when finished."
PROMPT_A2 = "Read episode_a/FEEDBACK.md and episode_a/GOAL.md and correct episode_a/cleaned.csv accordingly. Do not ask questions. Reply DONE when finished."
PROMPT_B = "Read episode_b/GOAL.md in this project and do exactly what it says, creating files under episode_b/. Do not ask questions. Reply DONE when finished."

def run(cmd_tmpl: str, prompt: str, cwd: Path, limit: int) -> dict:
    cmd = shlex.split(cmd_tmpl.replace("{prompt}", shlex.quote(prompt)))
    t0 = time.time()
    p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
    try:
        out, err = p.communicate(timeout=limit); reason = "normal" if p.returncode == 0 else "crashed"
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, signal.SIGKILL); out, err = p.communicate(); reason = "timed_out"
    return {"exit": p.returncode, "termination_reason": reason, "seconds": round(time.time() - t0, 1),
            "stdout_tail": out.decode(errors="replace")[-200:], "stderr_tail": err.decode(errors="replace")[-200:]}

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--seed", type=int, default=7); ap.add_argument("--exec", required=True)
    ap.add_argument("--root", required=True); ap.add_argument("--limit", type=int, default=420); ap.add_argument("--ablate-cmd", default=None)
    a = ap.parse_args()
    root = Path(a.root).resolve()
    # three SEPARATE parents so no arm can find another arm's files by listing its neighbours
    abl_parent, exp_parent, archive = Path(str(root) + "_ablated"), Path(str(root) + "_experienced"), Path(str(root) + "_archive")
    for d in (root, abl_parent, exp_parent, archive): shutil.rmtree(d, ignore_errors=True)
    for d in (root, abl_parent, exp_parent, archive): d.mkdir(parents=True)
    fa, fb, key = L.generate_pair(a.seed)
    rec = {"seed": a.seed, "convention": key["convention"], "executor": a.exec, "arms": {}}
    # --- ablated arm FIRST, so nothing from the experienced arm exists anywhere yet
    abl = abl_parent / "project"; abl.mkdir(); ab = abl / "episode_b"; write_workspace(ab, fb)
    if a.ablate_cmd: subprocess.run(a.ablate_cmd, shell=True, check=False)
    r4 = run(a.exec, PROMPT_B, abl, a.limit); v4 = L.verify_b(ab, key)
    rec["arms"]["ablated"] = {"b": {**r4, "pass": v4["pass"], "failure_mode": v4["failure_mode"]}}
    shutil.move(str(abl), str(archive / "ablated_project"))
    # --- experienced arm
    exp = exp_parent / "project"; (exp).mkdir(); ea = exp / "episode_a"; write_workspace(ea, fa)
    r1 = run(a.exec, PROMPT_A1, exp, a.limit); v1 = L.verify_a(ea, key)
    (ea / "FEEDBACK.md").write_text(L.feedback(key), encoding="utf-8")
    r2 = run(a.exec, PROMPT_A2, exp, a.limit); v2 = L.verify_a(ea, key)
    shutil.move(str(ea), str(archive / "episode_a"))   # episode A is gone from the project before B starts
    eb = exp / "episode_b"; write_workspace(eb, fb)
    r3 = run(a.exec, PROMPT_B, exp, a.limit); v3 = L.verify_b(eb, key)
    rec["arms"]["experienced"] = {"a1": {**r1, "pass": v1["pass"]}, "a2": {**r2, "pass": v2["pass"]},
                                  "b": {**r3, "pass": v3["pass"], "failure_mode": v3["failure_mode"]}}
    shutil.move(str(eb), str(archive / "episode_b"))
    rec["learning_transfer"] = int(v3["pass"]) - int(v4["pass"])
    rec["reading"] = ("transfer" if v3["pass"] and not v4["pass"] else "no_transfer" if not v3["pass"] and not v4["pass"]
                      else "not_needed" if v3["pass"] and v4["pass"] else "regression")
    (root / "record.json").write_text(json.dumps(rec, indent=1))
    print(json.dumps({k: rec[k] for k in ("seed", "convention", "learning_transfer", "reading")}))
    for arm, eps in rec["arms"].items():
        for ep, r in eps.items(): print(f"  {arm:12s} {ep}: pass={r['pass']} {r['termination_reason']} {r['seconds']}s {r.get('failure_mode') or ''}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
