#!/usr/bin/env python3
import csv,sys
req=["task_id","suite","coordinate","target_level","title","objective","success_criterion","verifier_type","binding_status"]
rows=list(csv.DictReader(open(sys.argv[1],newline="",encoding="utf-8"))); ids=[r["task_id"] for r in rows]; err=[]
if len(ids)!=len(set(ids)):err.append("duplicate task_id")
for n,r in enumerate(rows,2):
    for k in req:
        if not r.get(k):err.append(f"row {n}: missing {k}")
    if r.get("binding_status") not in ("bound","band-only","specification-only","generator-bound"):err.append(f"row {n}: bad binding")
print(f"tasks={len(rows)} unique={len(set(ids))} errors={len(err)}")
for e in err[:50]:print(e)
raise SystemExit(1 if err else 0)
