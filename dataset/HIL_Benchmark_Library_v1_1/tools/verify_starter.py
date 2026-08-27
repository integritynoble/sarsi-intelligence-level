#!/usr/bin/env python3
import json,sys
inst=json.load(open(sys.argv[1],encoding="utf-8"));exp=json.load(open(sys.argv[2],encoding="utf-8"))["expected"];cand=json.load(open(sys.argv[3],encoding="utf-8"))
ok=cand==exp;print(json.dumps({"task_id":inst["task_id"],"pass":ok},indent=2));raise SystemExit(0 if ok else 1)
