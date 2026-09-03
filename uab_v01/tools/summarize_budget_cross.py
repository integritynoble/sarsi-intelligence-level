#!/usr/bin/env python3
"""Surface S(T,H) and frontier F(H,p) from episodes.jsonl, with the zero-intervention rule applied."""
import json, sys, collections
from pathlib import Path
rows = [json.loads(l) for l in open(sys.argv[1])]
p = float(sys.argv[2]) if len(sys.argv) > 2 else 0.8
def surface(key):
    cell = collections.defaultdict(list)
    for r in rows: cell[(r["band"], r[key])].append(r)
    return cell
for label, key in (("declared budget", "budget"), ("reported budget (zero-intervention rule)", "reported_at")):
    cell = surface(key); print(f"\n== S(T,H) by {label} ==")
    print("band  " + "  ".join(f"{h:>14s}" for h in ("H0", "H1", "H2")))
    bands = sorted({b for b, _ in cell})
    for b in bands:
        line = f"{b:5s}"
        for h in ("H0", "H1", "H2"):
            rs = cell.get((b, h), [])
            line += f"  {sum(r['pass'] for r in rs):3d}/{len(rs):<3d} fc={sum(r['outcome']=='false_completion' for r in rs):<2d} hb={sum(r['outcome']=='held_back' for r in rs):<2d}" if rs else "  " + "-" * 14
        print(line)
    print("frontier F(H,%.2f) (cumulative over bands present):" % p, end=" ")
    for h in ("H0", "H1", "H2"):
        f = None
        for b in bands:
            rs = cell.get((b, h), [])
            if rs and sum(r["pass"] for r in rs) / len(rs) >= p: f = b
            else: break
        print(f"{h}={f}", end="  ")
    print()
load = collections.Counter((r["budget"], len(r["interventions"])) for r in rows)
print("\ninterventions raised per declared budget:", dict(sorted(load.items())))
print("cost: mean seconds per episode by budget:", {h: round(sum(r["seconds"] for r in rows if r["budget"] == h) / max(1, sum(1 for r in rows if r["budget"] == h)), 1) for h in ("H0", "H1", "H2")})
print("termination reasons:", dict(collections.Counter(r["termination_reason"] for r in rows)))
