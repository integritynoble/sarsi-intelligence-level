#!/usr/bin/env python3
"""Validate every manifest against the schema, check hashes, and check that the
matrix agrees with the manifests. Exit 1 on any failure. Asset paths under the
public corpus checkout are checked for existence when the checkout is present."""
from __future__ import annotations
import csv, hashlib, json, sys
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parents[1]
schema = json.load(open(ROOT / "TASK_MANIFEST.schema.json"))
errors = []
manifests = {}
for p in sorted((ROOT / "manifests").glob("*.json")):
    m = json.load(open(p)); manifests[p.name] = m
    try:
        jsonschema.Draft202012Validator(schema).validate(m)
    except jsonschema.ValidationError as e:
        errors.append(f"{p.name}: schema: {e.message}")
    body = json.dumps({**m, "provenance": {**m["provenance"], "hash": ""}}, sort_keys=True, separators=(",", ":")).encode()
    if m["provenance"]["hash"] != "sha256:" + hashlib.sha256(body).hexdigest():
        errors.append(f"{p.name}: hash does not match content")
    if p.stem != m["task_id"]:
        errors.append(f"{p.name}: filename != task_id")
    if m["binding"]["status"] in ("BOUND", "GENERATOR_BOUND") and not m["binding"].get("asset"):
        errors.append(f"{p.name}: bound without an asset")
    if m["acceptance"]["locus_required"] in ("a0_performing_system", "a1_same_process_persona"):
        errors.append(f"{p.name}: inadmissible acceptance locus")
# matrix consistency
rows = list(csv.DictReader(open(ROOT / "matrix" / "uab_matrix_v0_1.csv")))
for r in rows:
    if r["binding_status"] in ("BOUND", "GENERATOR_BOUND"):
        for tid in r["source"].split("; "):
            m = manifests.get(tid + ".json")
            if not m: errors.append(f"matrix {r['domain']}/{r['T_band']}: names missing manifest {tid}")
            elif m["domain"] != r["domain"] or m["difficulty"]["T_band"] != r["T_band"]:
                errors.append(f"matrix {r['domain']}/{r['T_band']}: manifest {tid} is for {m['domain']}/{m['difficulty']['T_band']}")
# local asset existence, where the corpus checkout is present
lib = ROOT.parent / "dataset" / "HIL_Benchmark_Library_v1_1"
for name, m in manifests.items():
    a = m["binding"].get("asset", "")
    if "HIL_Benchmark_Library_v1_1/starter/instances/" in a and lib.exists():
        rel = a.split("HIL_Benchmark_Library_v1_1/")[1]
        if not (lib / rel).exists(): errors.append(f"{name}: asset not found locally: {rel}")
for e in errors: print("ERROR", e)
print(f"{len(manifests)} manifests, {len(rows)} matrix cells, {len(errors)} errors")
sys.exit(1 if errors else 0)
