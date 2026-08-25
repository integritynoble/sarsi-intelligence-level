#!/usr/bin/env python3
import argparse, json

def normalized_auc(scores):
    if not scores:
        return 0.0
    if len(scores)==1:
        return float(scores[0])
    area=sum((scores[i]+scores[i+1])/2 for i in range(len(scores)-1))
    return area/(len(scores)-1)

def metrics(scores):
    auc=normalized_auc(scores)
    ceiling=max(scores) if scores else 0.0
    gain=ceiling-scores[0] if scores else 0.0
    harnessability=max(0.0,min(100.0,gain))
    hil_score=0.55*auc+0.35*ceiling+0.10*harnessability
    return {"HIL-AUC":auc,"HIL-Ceiling":ceiling,"Harness-Gain":gain,
            "Harnessability":harnessability,"HIL-Score-provisional":hil_score}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--scores", required=True, help="JSON list of HLIS values ordered HG0..")
    a=p.parse_args()
    print(json.dumps(metrics(json.loads(a.scores)), indent=2))
