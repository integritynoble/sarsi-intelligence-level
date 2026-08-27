#!/usr/bin/env python3
import csv,json,math,argparse
from collections import defaultdict
T_ORDER=["T0","T1","T2","T3","T4","T5","T6","TΩ"]; H_ORDER=["H0","H1","H2","H3","H4","H5"]
def hlis(scores,weights=None):
    weights=weights or {k:1 for k in scores}; vals=[(float(v),float(weights.get(k,1))) for k,v in scores.items() if v is not None]
    if not vals:return None
    if any(v<=0 for v,w in vals):return 0.0
    return 100*math.exp(sum(w*math.log(v) for v,w in vals)/sum(w for v,w in vals))
def load(path):
    rows=list(csv.DictReader(open(path,newline="",encoding="utf-8")))
    def b(x):return str(x).lower() in ("1","true","yes","y")
    for r in rows:
        r["D"]=b(r["delivered"]);r["V"]=b(r["verifier_pass"])
        # v1.1: graded outcome where the item supports one. Absent or blank
        # falls back to the boolean, so a v1.0 log scores identically.
        raw=r.get("item_score","")
        r["G"]=float(raw) if str(raw).strip() not in ("","none","None") else float(r["V"])
    return rows
def surface(rows,tmap):
    g=defaultdict(list)
    for r in rows:
        T=tmap.get(r["task_id"]);H=r.get("H_budget")
        if T and H:g[(T,H)].append(r)
    out={}
    for k,rs in g.items():
        n=len(rs);out[k]={"n":n,"S_del":sum(x["D"] and x["V"] for x in rs)/n,
                           "S_graded":sum(x["G"] if x["D"] else 0.0 for x in rs)/n,
                           "false_completion":sum(x["D"] and not x["V"] for x in rs)/n,
                           "held_back_invalid":sum((not x["D"]) and (not x["V"]) for x in rs)/n,
                           "false_rejection":sum((not x["D"]) and x["V"] for x in rs)/n}
    return out
def headroom(rows):
    """Fraction of episodes on which the best executor present is NOT already at
    the maximum. A coordinate near zero is reporting the suite's ceiling rather
    than the system's, and any HLIS or HIL figure drawn from it is bounded above
    by the benchmark. v1.6 of the framework requires this beside every
    coordinate score, because the two ceilings are indistinguishable in the
    number alone."""
    best=defaultdict(float)
    for r in rows:best[r["task_id"]]=max(best[r["task_id"]],r["G"] if r["D"] else 0.0)
    if not best:return None
    return sum(1 for v in best.values() if v<1.0)/len(best)

def failure_modes(rows):
    """Counts by declared failure mode. 'misread the specification' and
    'searched too shallowly' need different repairs and a single failed bucket
    reports them identically."""
    c=defaultdict(int)
    for r in rows:
        m=(r.get("failure_mode") or "").strip()
        if m and m!="none":c[m]+=1
    return dict(c)

def concordance_ready(rows):
    """Whether the log carries what the concordance audit needs: a response
    digest and a tier label. Without both, a wrong answer key is
    undetectable from this log."""
    n=len(rows)
    if not n:return None
    have=sum(1 for r in rows if (r.get("response_digest") or "").strip()
             and (r.get("executor_tier") or "").strip())
    return {"rows":n,"with_digest_and_tier":have,
            "tiers":sorted({(r.get("executor_tier") or "").strip() for r in rows}-{""}),
            "auditable":have==n and len({(r.get("executor_tier") or "").strip() for r in rows}-{""})>=2}

def frontier(s,p):
    return {H:next((T for T in reversed(T_ORDER) if s.get((T,H),{}).get("S_del",-1)>=p),None) for H in H_ORDER}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--runs",required=True);ap.add_argument("--tasks",required=True);ap.add_argument("--p",type=float,default=.8);ap.add_argument("--components")
    a=ap.parse_args();rows=load(a.runs);tmap={r["task_id"]:r["difficulty_band"] for r in csv.DictReader(open(a.tasks,newline="",encoding="utf-8"))}
    s=surface(rows,tmap)
    print(json.dumps({"surface":{f"{k[0]}/{k[1]}":v for k,v in s.items()},
                      "frontier":frontier(s,a.p),
                      "headroom":headroom(rows),
                      "failure_modes":failure_modes(rows),
                      "concordance":concordance_ready(rows)},indent=2))
    if a.components:print(json.dumps({"HLIS":hlis(json.loads(a.components))},indent=2))
if __name__=="__main__":main()
