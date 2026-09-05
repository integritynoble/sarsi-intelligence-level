#!/usr/bin/env python3
"""Validate the development dataset: every row parses, form ids are unique, each (coordinate, level) names a law or a
band the package knows, every I3 campaign carries its components, every I4 meta-campaign references existing I3
campaigns, and the combined file is exactly the union of the per-coordinate files.

    python3 tools/validate_dataset.py [dataset/dev_v0_1]
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hilbench import laws

I3_PARTS = ("theta_contract", "diagnostic_tasks", "acceptable_causal_diagnoses", "behavior_probes", "paired_evaluation", "regression_suite", "campaign_pass_formula")
I4_PARTS = ("baseline_i3_refs", "psi_change_contract", "primary_metric", "minimum_meaningful_improvement", "meta_campaign_pass_formula")
KNOWN_LEVELS = set(laws.LAWS) | {f"C{i}" for i in range(6)} | {f"I{i}" for i in range(6)} | {f"O{i}" for i in range(5)} | {f"SA{i}" for i in range(7)} | {f"T{i}" for i in range(6)}

def load(p: Path):
    rows = []
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip(): rows.append((n, json.loads(line)))
    return rows

def validate(root: Path) -> list:
    problems = []; per = {}
    for f in sorted((root / "public").glob("*.jsonl")):
        for n, r in load(f):
            per.setdefault(r.get("form_id"), []).append((f.name, n, r))
            for k in ("form_id", "coordinate", "level", "canonical_method", "development_only"):
                if k not in r: problems.append(f"{f.name}:{n} missing {k}")
            if r.get("level") not in KNOWN_LEVELS: problems.append(f"{f.name}:{n} unknown level {r.get('level')!r}")
            if r.get("level") == "I3" and any(k not in r for k in I3_PARTS): problems.append(f"{f.name}:{n} I3 campaign lacks {[k for k in I3_PARTS if k not in r]}")
            if r.get("level") == "I4" and any(k not in r for k in I4_PARTS): problems.append(f"{f.name}:{n} I4 meta-campaign lacks {[k for k in I4_PARTS if k not in r]}")
            if r.get("level") == "I4":                      # v2 law: reflexive, agent-generated, shown on meta-behavior probes
                need = {"agent_generated", "meta_behavior_signature"}; have = set((r.get("psi_change_contract") or {}).get("required_checks", []))
                if not need <= have: problems.append(f"{f.name}:{n} I4 contract lacks v2 checks {sorted(need - have)}")
                if "recursive_depth" not in r: problems.append(f"{f.name}:{n} I4 row does not say how recursive depth d_Psi is reported")
    dup = [i for i, v in per.items() if len(v) > 1]
    if dup: problems.append(f"duplicate form ids: {dup}")
    i3_ids = {i for i, v in per.items() if v[0][2].get("level") == "I3"}
    for i, v in per.items():
        r = v[0][2]
        if r.get("level") == "I4":
            missing = [x for x in r.get("baseline_i3_refs", []) if x not in i3_ids]
            if missing: problems.append(f"{i} references unknown I3 campaigns {missing}")
    comb = root / "hil_bench_public_dev_combined.jsonl"
    if comb.exists():
        cids = {r.get("form_id") for _, r in load(comb)}
        if cids != set(per): problems.append(f"combined file is not the union of public/*.jsonl: {sorted(cids ^ set(per))}")
    return problems

if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "dataset" / "dev_v0_1")
    probs = validate(root)
    print("\n".join(probs) if probs else f"dataset ok: {root}")
    sys.exit(1 if probs else 0)
