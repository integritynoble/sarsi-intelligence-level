#!/usr/bin/env python3
"""Executor comparison on the sealed families: t4.mini_language, t4.shift_schedule, t5.hidden_law.

  PYTHONPATH=<AI4Science checkout> python3 tools/run_sealed_comparison.py --build BUILD_ROOT --out DIR \
      --label NAME --exec 'claude -p {prompt} ...' [--t4-seeds 0-3] [--t5-seeds 0,9,24,27]

BUILD_ROOT is what `dli_bench build` produced (t4/ and t5/ subtrees, each instance with work/ and keyed/).
Only work/ is staged, into a fresh directory per episode; keyed/ is read by this script's verifier
call and never by the executor. Every invocation runs in its own process group under an enforced
limit; a killed run is recorded as timed_out and scored on whatever was delivered.
"""
from __future__ import annotations
import argparse, json, os, shlex, shutil, signal, subprocess, sys, time
from pathlib import Path
from ai4science.harness.agents.dli_bench.tasks import GENERATORS

TAIL = " Do not ask questions. Reply DONE when finished."
PROMPTS = {
    "t4.mini_language": "Read SPEC.md and examples.json in this directory and implement what SPEC.md describes in interp.py. You may run python to test your implementation. Keep evaluate() from ever raising.",
    "t4.shift_schedule": "Read SPEC.md and examples.json in this directory and implement solve() in solve.py exactly as SPEC.md describes; the result must be feasible and minimum-cost. You may run python to test it.",
    "t5.hidden_law": "Read GOAL.md in this directory and do exactly what it says: work out the generating rule from observations.json, write mechanism.txt, and write predictions.json for every point in predict_at.json. You may run python.",
}
LIMITS = {"t4.mini_language": 1800, "t4.shift_schedule": 1800, "t5.hidden_law": 7200}

def seeds_of(s): return [int(x) for x in s.split(",")] if "," in s or "-" not in s else list(range(int(s.split("-")[0]), int(s.split("-")[1]) + 1))

def run(cmd_tmpl, prompt, cwd, limit):
    cmd = shlex.split(cmd_tmpl.replace("{prompt}", shlex.quote(prompt))); t0 = time.time()
    p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True, env={**os.environ, "PWD": str(cwd)})
    try: out, err = p.communicate(timeout=limit); reason = "normal" if p.returncode == 0 else "crashed"
    except subprocess.TimeoutExpired: os.killpg(p.pid, signal.SIGKILL); out, err = p.communicate(); reason = "timed_out"
    return {"exit": p.returncode, "termination_reason": reason, "seconds": round(time.time() - t0, 1), "stdout_tail": out.decode(errors="replace")[-200:]}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--build", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--label", required=True); ap.add_argument("--exec", required=True)
    ap.add_argument("--t4-seeds", default="0-3"); ap.add_argument("--t5-seeds", default="0,9,24,27"); a = ap.parse_args()
    build, out = Path(a.build), Path(a.out); out.mkdir(parents=True, exist_ok=True); log = out / "episodes.jsonl"
    plan = [("t4.mini_language", s) for s in seeds_of(a.t4_seeds)] + [("t4.shift_schedule", s) for s in seeds_of(a.t4_seeds)] + [("t5.hidden_law", s) for s in seeds_of(a.t5_seeds)]
    for key, seed in plan:
        inst = build / ("t5" if key.startswith("t5") else "t4") / key.replace(".", "_") / f"seed{seed}"
        ws = out / f"{key.replace('.', '_')}_seed{seed}"; shutil.rmtree(ws, ignore_errors=True); shutil.copytree(inst / "work", ws)
        r = run(a.exec, PROMPTS[key] + TAIL, ws, LIMITS[key])
        v = GENERATORS[key].verify(ws, inst / "keyed")
        rec = {"label": a.label, "generator": key, "seed": seed, "pass": v.passed, "metrics": v.metrics, "reasons": list(v.reasons),
               **{k: r[k] for k in ("exit", "termination_reason", "seconds")}, "limit": LIMITS[key], "executor": a.exec}
        with open(log, "a") as f: f.write(json.dumps(rec) + "\n")
        m = v.metrics; short = {k: round(float(m[k]), 4) for k in m if k in ("accuracy", "extrapolation_rmse", "bar", "baseline_rmse", "passed_instances", "n_cases", "score")}
        print(f"{a.label:14s} {key:18s} seed {seed:2d}: {'pass' if v.passed else 'FAIL':4s} {r['termination_reason']:9s} {r['seconds']:7.1f}s {short}", flush=True)
    print("ALLDONE", flush=True)

if __name__ == "__main__":
    main()
