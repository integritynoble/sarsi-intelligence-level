#!/usr/bin/env python3
"""Flag benchmark items whose answer key is probably wrong.

The problem this solves: an item with a withheld key cannot be corrected by its
users, because the thing they would need in order to notice the error is the
thing being withheld. A wrong key does not look wrong. It looks like a hard item
that models fail.

The signal is agreement. Two executors of materially different capability that
return the SAME response to the same item, where the key disagrees with both,
is weak evidence of a hard item and strong evidence of a wrong key: independent
systems rarely agree on the answer to a question that is genuinely hard, and
routinely agree on the answer to one that is clear.

Nothing here needs the ground truth, which is the point.

Input is a JSONL of per-case responses:

    {"task_id": "...", "case_id": "...", "executor": "...",
     "tier": "frontier|weak|...", "response": <any JSON>, "scored_correct": bool}

Output lists items to audit, most concordant first. It never says the key IS
wrong -- it says a human should look, and at what.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict


def digest(value) -> str:
    return json.dumps(value, sort_keys=True, default=str)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--responses", required=True, help="JSONL, see module docstring")
    ap.add_argument("--min-tiers", type=int, default=2,
                    help="distinct tiers that must agree before a case is flagged")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    cases = defaultdict(list)
    for line in open(a.responses, encoding="utf-8"):
        line = line.strip()
        if line:
            r = json.loads(line)
            cases[(r["task_id"], r.get("case_id", ""))].append(r)

    flagged, tier_counts = [], defaultdict(set)
    for key, rs in cases.items():
        wrong = [r for r in rs if not r.get("scored_correct")]
        if len(wrong) < a.min_tiers:
            continue
        by_response = defaultdict(list)
        for r in wrong:
            by_response[digest(r["response"])].append(r)
        for resp, group in by_response.items():
            tiers = {g.get("tier", g.get("executor", "?")) for g in group}
            if len(tiers) < a.min_tiers:
                continue
            flagged.append({
                "task_id": key[0], "case_id": key[1],
                "agreeing_tiers": sorted(tiers),
                "executors": sorted({g.get("executor", "?") for g in group}),
                "shared_response": json.loads(resp) if resp else None,
                "n_agreeing": len(group),
            })
            tier_counts[key[0]].update(tiers)

    flagged.sort(key=lambda f: (-len(f["agreeing_tiers"]), -f["n_agreeing"],
                                f["task_id"], f["case_id"]))
    if a.json:
        print(json.dumps({"cases_examined": len(cases), "flagged": flagged}, indent=2))
    else:
        print("cases examined: %d   flagged for audit: %d"
              % (len(cases), len(flagged)))
        for f in flagged:
            print("  %s %s -- %d executors across tiers %s returned the same "
                  "answer and all were scored wrong: %s"
                  % (f["task_id"], f["case_id"] or "(whole item)", f["n_agreeing"],
                     "/".join(f["agreeing_tiers"]),
                     json.dumps(f["shared_response"])[:120]))
        if flagged:
            print("\nAudit each flagged item against its own specification before "
                  "attributing these failures to the executors. A key that "
                  "disagrees with every independent reader is the thing to "
                  "check first.")
    # Flagged items are work to do, not a build failure: exit 0 unless the input
    # was unusable. A tool that fails CI on a finding gets removed from CI.
    return 0


if __name__ == "__main__":
    sys.exit(main())
