#!/usr/bin/env python3
"""Materialize the public testing dataset of every cell that has an instance generator: seeds 0..2 of each witness
family, as the files the executor would see plus the sealed key, under dataset/<ds>/generated/<cell>/<family>/s<seed>/.
A cell's dataset is then literally present, not a pointer.  Cells whose generator is a runner (a campaign, a probe, a
gate over records) point at their record instead."""
from __future__ import annotations
import json, shutil, sys
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(PKG))
from hilbench import c_items, hard, m1_restart, sa_probes, o_families, UAB  # noqa: F401 (UAB puts families on the path)
from families import FAMILIES, learning_t2

def th(fam): return lambda seed: FAMILIES[fam].generate(seed)
INSTANCE = {   # cell -> {family: generator(seed) -> (files, key)}
    "C0": {"c_items_C0": lambda s: c_items.generate(s, "C0")}, "C1": {"c_items_C1": lambda s: c_items.generate(s, "C1")},
    "C2": {"c_items_C2": lambda s: c_items.generate(s, "C2")}, "C3": {"c_items_C3": lambda s: c_items.generate(s, "C3")},
    "C4": {"hc_decoy": hard.hc_decoy_generate}, "C5": {"hc_rule": hard.hc_rule_generate},
    "I1": {"m1_restart": m1_restart.generate_pair}, "M1": {"m1_restart": m1_restart.generate_pair},
    "I2": {"learning_t2": learning_t2.generate_pair},
    "O0": {"o0_routing": o_families.o0_generate}, "O1": {"o1_orgmem": o_families.o1_generate_pair},
    "SA1": {"sa1": sa_probes.sa1_generate}, "SA2": {"sa2": sa_probes.sa2_generate},
    "T0": {f: th(f) for f in ("code_t0", "funding_t0", "job_t0", "paper_t0", "business_t0")},
    "T1": {"paper_t1": th("paper_t1"), "hc_contra": hard.hc_contra_generate, "hc_decoy": hard.hc_decoy_generate},
    "T2": {"hc_sched": hard.hc_sched_generate, "hc_rule": hard.hc_rule_generate},
    "I0": {"code_t0": th("code_t0")},
}
RECORD = {"H0": "records/*.json (every episode's ledger is empty by construction)", "DF": "records/*.json (the four-outcome record per episode; score.frontier_cumulative)",
          "HG0": "HG_Bench/hg_conform_public_seeds.json", "HG1": "HG_Bench/hg_conform_public_seeds.json", "HG2": "HG_Bench/hg_conform_public_seeds.json",
          "U0": "records/*.json -> index/profile (score.gate)", "U1": "records/*.json -> profile (score.gate)", "U2": "records/*.json -> profile (score.gate)",
          "I5": "records/i5_*.json (the cancer campaign: discovery, sealed validation, transfer arms)", "T3": "records/*extended*.json (AI4Science families)", "T4": "records/*extended*.json", "T5": "records/*extended*.json"}

def _write(files, key, d: Path):
    d.mkdir(parents=True, exist_ok=True)
    for name, text in (files or {}).items():
        p = d / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text if isinstance(text, str) else json.dumps(text, indent=1), encoding="utf-8")
    (d / "KEY.sealed.json").write_text(json.dumps(key, indent=1, ensure_ascii=False, default=str), encoding="utf-8")

def main(ds: Path, seeds=(0, 1, 2)) -> dict:
    out = ds / "generated"; shutil.rmtree(out, ignore_errors=True); index = {}
    for cell, fams in INSTANCE.items():
        for fam, gen in fams.items():
            for s in seeds:
                r = gen(s)
                if isinstance(r, tuple) and len(r) == 2: files, key = r; _write(files, key, out / cell / fam / f"s{s}")
                else:   # a pair: (files_a, key_a, files_b, key_b) or dict-shaped
                    parts = r if isinstance(r, (list, tuple)) else [r]
                    for i, part in enumerate(parts):
                        if isinstance(part, tuple) and len(part) == 2: _write(part[0], part[1], out / cell / fam / f"s{s}" / f"episode_{i}")
                        elif isinstance(part, dict): _write(part.get("files", {}), part.get("key", part), out / cell / fam / f"s{s}" / f"episode_{i}")
            index.setdefault(cell, []).append(f"generated/{cell}/{fam}/s0..s{seeds[-1]}")
    for cell, rec in RECORD.items(): index.setdefault(cell, []).append(rec)
    (out / "INDEX.json").write_text(json.dumps(index, indent=1, ensure_ascii=False))
    n = sum(1 for _ in out.rglob("KEY.sealed.json")); print("materialized", n, "instances for", len(INSTANCE), "cells; index for", len(index))
    return index

if __name__ == "__main__":
    main(Path(sys.argv[1]))
