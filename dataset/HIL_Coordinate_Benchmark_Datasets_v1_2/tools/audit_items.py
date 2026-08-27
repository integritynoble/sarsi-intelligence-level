#!/usr/bin/env python3
"""Item-validity checks on the library's own contents.

`validate.py` checks that ids are unique and coordinates match their file. Both
are real checks, and neither asks whether an item can do the job it is filed
under. This asks that.

  ladder_distinct   No two items at different target levels may share a payload.
                    v1.1 shipped a causal-reasoning family of 32 items with ONE
                    distinct payload: the same three-node graph question was
                    filed at C0 and at COmega. A system that answers it is
                    certified at every level of that family at once, and the
                    coordinate cannot discriminate levels at all.

  key_recomputable  Where a family ships a reference implementation, every key
                    must be reproduced by it. A key that is asserted rather than
                    computed is an unverified claim, and four such claims in a
                    sibling suite were all eventually found wrong.

  static_ceiling    Discovery and open-ended levels (C5 and above, and their
                    equivalents) may not be certified by a static exact-match
                    item. If the answer can be written down in advance, the item
                    is not measuring discovery -- whatever level it is filed at.
                    GUI-perception items are exempt and separately checked: GP
                    is a subscale of C whose levels are NOT C levels, so a GP5
                    item may legitimately be static, and must carry gp_level so
                    that its C number is not read as a discovery claim.

Exit status is 1 on any finding, so this belongs in CI.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ("C_Bench/c_bench.csv", "C_Bench/gp_gui_perception_subset.csv",
         "I_Bench/i_bench.csv", "O_Bench/o_bench.csv", "T_Bench/t_bench.csv",
         "H_Bench/h_bench.csv", "SA_Bench/sa_bench.csv", "M_Bench/m_bench.csv")

#: Levels whose definition is discovery or open-ended expansion. A fixed
#: question with a fixed answer cannot supply evidence for these, because the
#: answer existing in advance is the thing they deny.
DISCOVERY_LEVELS = {"C5", "C6", "CΩ", "COmega", "I5", "IΩ", "IOmega",
                    "O5", "OΩ", "OOmega", "M5", "MΩ", "MOmega",
                    "SA5", "SAΩ", "SAOmega"}


def _load():
    rows = []
    for rel in FILES:
        p = ROOT / rel
        if not p.exists():
            continue
        for r in csv.DictReader(p.open(newline="", encoding="utf-8")):
            r["_file"] = rel
            rows.append(r)
    return rows


def _payload(r):
    if not r.get("input_json") or not r.get("expected_json"):
        return None
    return hashlib.sha256(
        (r["input_json"] + "||" + r["expected_json"]).encode("utf-8")).hexdigest()


def main() -> int:
    rows = _load()
    errors, notes = [], []

    # -- ladder_distinct --------------------------------------------------
    groups = defaultdict(list)
    for r in rows:
        h = _payload(r)
        if h:
            groups[h].append(r)
    for ids in groups.values():
        levels = {r["target_level"] for r in ids}
        if len(levels) > 1:
            fam = sorted({r["family"] for r in ids})
            errors.append(
                "one payload is filed at %d different levels (%s) in family %s: "
                "%d items including %s -- these levels cannot be told apart by "
                "this evidence"
                % (len(levels), ", ".join(sorted(levels)), "/".join(fam),
                   len(ids), ids[0]["item_id"]))
        elif len(ids) > 1:
            notes.append("%d items share a payload within %s: %s"
                         % (len(ids), sorted(levels)[0], ids[0]["item_id"]))

    # A family whose whole ladder collapses is worth naming on its own, because
    # the per-payload message above understates it.
    per_family = defaultdict(lambda: [0, set()])
    for r in rows:
        h = _payload(r)
        if h:
            key = (r["coordinate"], r["family"])
            per_family[key][0] += 1
            per_family[key][1].add(h)
    for (coord, fam), (n, hs) in sorted(per_family.items()):
        if n >= 8 and len(hs) * 4 <= n:
            errors.append("%s/%s has %d items and %d distinct payloads"
                          % (coord, fam, n, len(hs)))

    # -- static_ceiling ---------------------------------------------------
    for r in rows:
        if r.get("binding_status") != "bound":
            continue
        if r.get("family") == "gui_perception":
            # GP is a subscale of C and its levels are not C levels. A
            # previously unseen layout IS legitimate static evidence for GP5;
            # nothing static is evidence for C5. The row must say which it is,
            # or a reader will take the C number at face value.
            if not r.get("gp_level"):
                errors.append("%s is a gui_perception item filed at %s with no "
                              "gp_level; GP levels are not C levels and the row "
                              "does not say which claim it supports"
                              % (r["item_id"], r["target_level"]))
            continue
        if r["target_level"] in DISCOVERY_LEVELS and \
                r.get("scoring_type") in ("exact", "exact_match"):
            errors.append(
                "%s is a bound exact-match item at %s, a discovery or "
                "open-ended level; if the answer can be written down in "
                "advance the item is not measuring discovery"
                % (r["item_id"], r["target_level"]))

    # -- key_recomputable -------------------------------------------------
    ref = ROOT / "tools" / "c_ladder.py"
    if ref.exists():
        sys.path.insert(0, str(ROOT / "tools"))
        import c_ladder                                    # noqa: E402
        checked = 0
        for r in rows:
            fn = c_ladder.KEY_FUNCTIONS.get(r.get("family"))
            if not fn or not r.get("input_json"):
                continue
            checked += 1
            want = json.loads(r["expected_json"])
            got = fn(json.loads(r["input_json"]))
            if got != want:
                errors.append("%s: the key says %s, the reference computes %s"
                              % (r["item_id"], json.dumps(want),
                                 json.dumps(got)))
        notes.append("%d keys recomputed from the shipped reference" % checked)

    print("items=%d payloads=%d errors=%d notes=%d"
          % (len(rows), len(groups), len(errors), len(notes)))
    for n in notes[:10]:
        print("  note:  " + n)
    for e in errors[:40]:
        print("  ERROR: " + e)
    if len(errors) > 40:
        print("  ... and %d more" % (len(errors) - 40))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
