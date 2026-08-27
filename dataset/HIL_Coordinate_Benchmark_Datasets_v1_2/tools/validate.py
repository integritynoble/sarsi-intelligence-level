#!/usr/bin/env python3
import csv, sys, os, json
root=sys.argv[1] if len(sys.argv)>1 else "."
files=[
("C_Bench/c_bench.csv","C"),("I_Bench/i_bench.csv","I"),("O_Bench/o_bench.csv","O"),
("T_Bench/t_bench.csv","T"),("H_Bench/h_bench.csv","H"),("SA_Bench/sa_bench.csv","SA"),
("M_Bench/m_bench.csv","M")]
errors=[]; counts={}; all_ids=[]
for rel,coord in files:
    p=os.path.join(root,rel)
    with open(p,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    counts[coord]=len(rows)
    ids=[r["item_id"] for r in rows]; all_ids.extend(ids)
    if len(ids)!=len(set(ids)): errors.append(f"{coord}: duplicate ids")
    if any(r.get("coordinate")!=coord for r in rows): errors.append(f"{coord}: coordinate mismatch")
    if coord=="I" and any(not r.get("minimum_M_prerequisite") for r in rows):
        errors.append("I: missing minimum_M_prerequisite")
if len(all_ids)!=len(set(all_ids)): errors.append("cross-suite duplicate item ids")
print(json.dumps({"counts":counts,"total_core":sum(counts[c] for c in ["C","I","O","T","H","SA"]),
                  "total_with_supporting_M":sum(counts.values()),"errors":errors},indent=2))
raise SystemExit(1 if errors else 0)
