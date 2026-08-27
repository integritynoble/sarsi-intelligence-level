#!/usr/bin/env python3
import json, sys, math

def bbox_iou(a,b):
    x1=max(a[0],b[0]); y1=max(a[1],b[1]); x2=min(a[2],b[2]); y2=min(a[3],b[3])
    inter=max(0,x2-x1)*max(0,y2-y1)
    aa=max(0,a[2]-a[0])*max(0,a[3]-a[1])
    bb=max(0,b[2]-b[0])*max(0,b[3]-b[1])
    return inter/(aa+bb-inter) if aa+bb-inter else 0.0

expected=json.load(open(sys.argv[1],encoding="utf-8"))
candidate=json.load(open(sys.argv[2],encoding="utf-8"))
scores=[]
for k,v in expected.items():
    if k.endswith("bbox") and isinstance(v,list) and isinstance(candidate.get(k),list):
        scores.append(1.0 if bbox_iou(v,candidate[k])>=0.5 else 0.0)
    else:
        scores.append(1.0 if candidate.get(k)==v else 0.0)
score=sum(scores)/len(scores) if scores else 0.0
print(json.dumps({"score":score,"passed":score>=0.8,"components":len(scores)},indent=2))
