#!/usr/bin/env python3
"""Calibrate the Core-H candidates: run every item on one executor and record pass/fail and seconds.

An item enters the Core only when the pooled runs show a spread -- some pair passes it and some pair
fails it. Usage:
    python3 tools/calibrate_hard.py --label NAME --exec 'CMD {prompt}' --root DIR [--seeds 0,1]
"""
import argparse, json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from hilbench import hard
from hilbench.common import run_exec, write_workspace, TASK

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", required=True); ap.add_argument("--exec", required=True); ap.add_argument("--root", required=True)
    ap.add_argument("--seeds", default="0,1"); ap.add_argument("--items", default=",".join(hard.ITEMS))
    a = ap.parse_args()
    root = Path(a.root); root.mkdir(parents=True, exist_ok=True)
    seeds = [int(x) for x in a.seeds.split(",")]; rows = []
    for name in a.items.split(","):
        gen, ver, _solve, _naive, limit = hard.ITEMS[name]
        for s in seeds:
            files, key = gen(s); ws = root / f"{name}_s{s}"; write_workspace(ws, files)
            r = run_exec(a.exec, TASK, ws, limit)
            v = ver(ws, key); ok = v["pass"] and r["termination_reason"] != "timed_out"
            rows.append({"item": name, "seed": s, "pass": ok, "accuracy": v["accuracy"], "mode": v["failure_mode"],
                         "termination": r["termination_reason"], "seconds": r["seconds"],
                         "failed_checks": [c["name"] for c in v["checks"] if not c["ok"]]})
            print(f"{a.label} {name} s{s}: {'pass' if ok else 'FAIL'} {v['failure_mode'] or ''} {r['termination_reason']} {r['seconds']}s {rows[-1]['failed_checks']}", flush=True)
    out = {"label": a.label, "executor": a.exec, "seeds": seeds, "rows": rows,
           "passed": sum(r["pass"] for r in rows), "n": len(rows), "finished": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    (root / "calibration.json").write_text(json.dumps(out, indent=1))
    print(f"{a.label} CALIBRATION {out['passed']}/{out['n']}", flush=True)

if __name__ == "__main__":
    main()
