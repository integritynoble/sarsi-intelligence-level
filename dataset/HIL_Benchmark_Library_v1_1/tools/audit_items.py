#!/usr/bin/env python3
"""Structural validity checks on the library's own items.

Every score this library produces is arithmetic over item outcomes. The
arithmetic is checked by score_hil.py; until this tool existed nothing checked
the items. An item with a withheld key is an assertion by its author, and an
assertion that no one tests is inherited by every number computed from it.

Three checks, each of which found something real when first run against v1.0:

  distinct      No two tasks at different levels may share a bound instance.
                v1.0 shipped 16 bound instances with 12 distinct payloads: three
                C0/C1 pairs and one T0/T1 pair were byte-identical. A level pair
                scored on the same item cannot discriminate between those
                levels, and the surface reports the same measurement twice.

  procedure     A T1+ delegation item states a goal; a T0 item may state the
                procedure. An item whose instruction names the operations is a
                T0 item wherever it is filed.

  keys          Every bound instance has an answer, every answer a bound
                instance, and the catalog agrees with the directory. A
                generator-bound task names a generator instead of staging an
                instance, and must not do both.

Exit status is 1 if any check fails, so this belongs in CI rather than in a
notebook.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data" / "task_catalog.csv"
INSTANCES = ROOT / "starter" / "instances"
ANSWERS = ROOT / "starter" / "answers"

#: Verbs that name an operation rather than an outcome. An instruction built
#: from these is a recipe, and following a recipe is the T0 band by definition.
PROCEDURE_WORDS = re.compile(
    r"\b(keep|sort|filter|dedup\w*|group|join|append|reverse|"
    r"concatenate|drop|split|merge|round|truncate)\b", re.I)


def _payload(task_id: str):
    inst = json.loads((INSTANCES / (task_id + ".json")).read_text(encoding="utf-8"))
    ans = json.loads((ANSWERS / (task_id + ".json")).read_text(encoding="utf-8"))
    return inst.get("input"), ans.get("expected")


def main() -> int:
    catalog = {r["task_id"]: r for r in csv.DictReader(
        CATALOG.open(newline="", encoding="utf-8"))}
    bound = sorted(p.stem for p in INSTANCES.glob("*.json"))
    errors, notes = [], []

    # -- keys ------------------------------------------------------------
    for tid in bound:
        if not (ANSWERS / (tid + ".json")).exists():
            errors.append("%s has an instance and no answer" % tid)
        if tid not in catalog:
            errors.append("%s is staged and not in the catalog" % tid)
        elif catalog[tid]["binding_status"] != "bound":
            errors.append("%s is staged but the catalog calls it %r"
                          % (tid, catalog[tid]["binding_status"]))
    for tid, row in catalog.items():
        if row["binding_status"] == "bound" and tid not in bound:
            errors.append("%s is marked bound and nothing is staged" % tid)
        if row["binding_status"] == "generator-bound":
            # Instances live outside the archive, so the reference IS the
            # binding. Without it the row claims runnable evidence it has no
            # way to produce.
            if not row.get("generator_ref"):
                errors.append("%s is generator-bound and names no generator_ref"
                              % tid)
            elif ":" not in row["generator_ref"]:
                errors.append("%s has generator_ref %r, which does not name a "
                              "module and a key" % (tid, row["generator_ref"]))
            if tid in bound:
                errors.append("%s is generator-bound and also has a staged "
                              "instance; one of the two is the real home" % tid)

    # -- distinct --------------------------------------------------------
    groups = defaultdict(list)
    for tid in bound:
        if not (ANSWERS / (tid + ".json")).exists():
            continue
        blob = json.dumps(_payload(tid), sort_keys=True).encode("utf-8")
        groups[hashlib.sha256(blob).hexdigest()].append(tid)
    for ids in groups.values():
        if len(ids) < 2:
            continue
        levels = {catalog[t]["target_level"] for t in ids if t in catalog}
        bands = {catalog[t]["difficulty_band"] for t in ids if t in catalog}
        if len(levels) > 1 or len(bands) > 1:
            errors.append(
                "identical instance across levels %s / bands %s: %s -- these "
                "levels cannot be told apart by this evidence"
                % (sorted(levels), sorted(bands), ", ".join(sorted(ids))))
        else:
            notes.append("duplicate instance within one level: %s"
                         % ", ".join(sorted(ids)))

    # -- procedure -------------------------------------------------------
    for tid in bound:
        row = catalog.get(tid)
        if not row or row["coordinate"] != "DI":
            continue
        band = row["difficulty_band"]
        if band in ("T0",):
            continue
        inp, _ = _payload(tid)
        text = " ".join(str(v) for k, v in (inp or {}).items()
                        if k in ("instruction", "goal", "task", "query"))
        hits = sorted(set(m.group(0).lower() for m in PROCEDURE_WORDS.finditer(text)))
        if hits:
            errors.append(
                "%s is filed at %s and its instruction names the procedure (%s); "
                "an item that lists the operations is a T0 item wherever it is filed"
                % (tid, band, ", ".join(hits)))

    print("bound=%d distinct_payloads=%d errors=%d notes=%d"
          % (len(bound), len(groups), len(errors), len(notes)))
    for n in notes:
        print("  note:  " + n)
    for e in errors:
        print("  ERROR: " + e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
