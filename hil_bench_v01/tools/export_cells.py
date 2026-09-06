#!/usr/bin/env python3
"""Export the cell grid as dataset v0.9 on top of the v0.8 harmonized tree.

    python3 tools/export_cells.py <v0.8 tree> dataset/ail_v0_3

Adds cells.jsonl (one record per cell, the I-style schema), coverage.csv (regenerated from the grid), hg_conform.json
(a real run of the offline HG0-HG2 conformance probe), and stamps the card.  Every v0.8 record is kept unchanged so the
HIL-Method-1.0 grammar and the cell grid name the same cells (`method` cross-references `canonical_method`).
"""
from __future__ import annotations
import csv, json, shutil, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hilbench import cells, hg_conform
sys.path.insert(0, str(Path(__file__).resolve().parent)); import materialize_public

def main(src: Path, dst: Path):
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    # forms the grid adds on top of the base tree (kept across re-exports)
    extra = Path(__file__).resolve().parents[1] / "dataset_extra"
    if extra.exists():
        for f in extra.glob("*.jsonl"):
            tgt = dst / "public" / f.name; rows = [l for l in tgt.read_text().splitlines() if l.strip()] if tgt.exists() else []
            add = [l for l in f.read_text().splitlines() if l.strip() and l not in rows]; tgt.write_text("\n".join(rows + add) + "\n")
            comb = next(dst.glob("*public_dev_combined.jsonl")); crows = [l for l in comb.read_text().splitlines() if l.strip()]
            comb.write_text("\n".join(crows + [l for l in add if l not in crows]) + "\n")
    index = materialize_public.main(dst)
    sys.path.insert(0, str(Path(__file__).resolve().parent)); import paper_tables
    cat, forms = paper_tables.load_catalog(dst)
    with (dst / "cells.jsonl").open("w", encoding="utf-8") as f:
        for c in cells.CELLS:
            ds = {"forms": paper_tables.forms_for(c, forms), "generated_or_records": index.get(c["cell"], [])}
            f.write(json.dumps({**c, "dataset": ds, "dataset_version": "ail-0.3+grid", "schema": "I-style cell v1"}, ensure_ascii=False) + "\n")
    with (dst / "coverage.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["ladder", "cell", "name", "status", "key", "generator", "control_arm", "gate", "method"]); w.writeheader(); w.writerows(cells.coverage())
    with tempfile.TemporaryDirectory() as t:
        s = hg_conform.run_all(Path(t)); shutil.copy(Path(t) / "hg_conform.json", dst / "HG_Bench" / "hg_conform_public_seeds.json")
    card = json.loads((dst / "dataset_card.json").read_text()) if (dst / "dataset_card.json").exists() else {}
    card.update({"dataset_version": "ail-0.3+grid", "cells": len(cells.CELLS), "cell_status_counts": cells.counts(), "cell_schema": "construct (contrast) | prereq | witness + control arm | factors with locus | gate | law | key | generator | status",
                 "hg_conform_public": s, "note": "v0.9 = v0.8 harmonized records unchanged + the cell grid; `status` is a fact about the package, never about the level"})
    (dst / "dataset_card.json").write_text(json.dumps(card, indent=1, ensure_ascii=False))
    readme = (dst / "README.md").read_text() if (dst / "README.md").exists() else ""
    (dst / "README.md").write_text("# AI-Level Bench Development Dataset v0.9 — the cell grid\n\n`cells.jsonl` holds one record per level of every ladder (C, C^GUI, GP, I, M, O, SA, T, H, DI, HG, U) in the style of I: construct as a contrast, prerequisite, witness with a control arm, named factors each with the locus that computes it, the gate, the law's constants, the kind of key, the generator that exists for it, and a `status` — `runs` (generator + verifier in the package), `forms` (public forms + reference scorer, no runner yet), `specification` (law fixed, no secure environment yet). `coverage.csv` is regenerated from it. `HG_Bench/hg_conform_public_seeds.json` is a real run of the offline HG0–HG2 conformance probe. Every v0.8 record (HIL-Method-1.0 grammar) is carried unchanged; `method` in a cell names the v0.8 `canonical_method` of the same cell.\n\n---\n\n" + readme)
    print("exported", dst, cells.counts()["total"], "HG:", {k: v for k, v in s.items() if k != "not_publicly_visible"})
    return 0

if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]), Path(sys.argv[2])))
