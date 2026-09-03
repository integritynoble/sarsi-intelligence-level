#!/usr/bin/env python3
"""Matched executor comparison over budget-cross episode files: same families, seeds and budgets.
usage: compare_executors.py LABEL=path.jsonl [LABEL=path.jsonl ...]  (a label may list several files, comma-separated;
later files override earlier ones on the same (family, seed, budget) key, e.g. a re-run after an item repair)."""
import json, sys, collections
runs = {}
for arg in sys.argv[1:]:
    label, paths = arg.split("=", 1); rows = {}
    for p in paths.split(","):
        for l in open(p):
            r = json.loads(l); rows[(r["family"], r["seed"], r["budget"])] = r
    runs[label] = rows
keys = sorted(set.intersection(*[set(v) for v in runs.values()]))
print(f"matched episodes per executor: {len(keys)}")
bands = sorted({runs[next(iter(runs))][k]["band"] for k in keys}); budgets = ["H0", "H1", "H2"]
hdr = "executor".ljust(24) + "".join(f"{b} {h:>3}".rjust(11) for b in bands for h in budgets) + "   total  fc  hb  questions  mean s"
print(hdr)
for label, rows in runs.items():
    line = label.ljust(24)
    for b in bands:
        for h in budgets:
            ks = [k for k in keys if rows[k]["band"] == b and k[2] == h]
            line += f"{sum(rows[k]['pass'] for k in ks):3d}/{len(ks):<2d}".rjust(11)
    tot = sum(rows[k]["pass"] for k in keys); fc = sum(rows[k]["outcome"] == "false_completion" for k in keys)
    hb = sum(rows[k]["outcome"] == "held_back" for k in keys); q = sum(any(i["kind"] == "clarification" for i in rows[k]["interventions"]) for k in keys)
    s = sum(rows[k]["seconds"] for k in keys) / len(keys)
    print(line + f"   {tot:3d}/{len(keys)}  {fc:2d}  {hb:2d}  {q:9d}  {s:6.1f}")
print("\nper-executor failures:")
for label, rows in runs.items():
    for k in keys:
        r = rows[k]
        if not r["pass"]: print(f"  {label}: {k} {r['outcome']} {r['failure_mode']} interventions={[i['kind'] for i in r['interventions']]}")
print("\ndiscordant episodes (some pass, some fail):")
for k in keys:
    vals = {lab: rows[k]["pass"] for lab, rows in runs.items()}
    if len(set(vals.values())) > 1: print(" ", k, vals)
