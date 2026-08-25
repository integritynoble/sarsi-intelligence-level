#!/usr/bin/env python3
"""Check the library against its own claims.

v0.1's validator counted rows. This also checks the claims that can be wrong in
a way a count cannot see:

  * every binding names a benchmark that exists;
  * a binding claiming `bound` names at least one implementation, and one
    claiming `specification_only` names none — a library that says it can run
    something it cannot is worse than one that says nothing;
  * `band_only` is a distinct status and is not reported as coverage, because
    substituting a different family at the same difficulty band reports
    coverage the suite does not have;
  * the run-log schema requires `harness_accepted`, without which a held-back
    result and a wrongly-delivered one are the same row.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]


def rows(p: Path) -> List[dict]:
    out, seen = [], set()
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        o = json.loads(line)
        bid = o.get("benchmark_id")
        if bid in seen:
            raise ValueError("duplicate benchmark_id %s in %s" % (bid, p.name))
        seen.add(bid)
        out.append(o)
    return out


def main() -> int:
    problems: List[str] = []
    native = rows(ROOT / "data" / "hil_native_tasks.jsonl")
    deleg = rows(ROOT / "data" / "delegation_plane_tasks.jsonl")
    binds = rows(ROOT / "bindings" / "bindings.jsonl")

    known = {r["benchmark_id"] for r in native} | {r["benchmark_id"] for r in deleg}
    for b in binds:
        if b["benchmark_id"] not in known:
            problems.append("binding names an unknown benchmark: %s" % b["benchmark_id"])
        if b["status"] == "bound" and not b.get("implementations"):
            problems.append("%s is marked bound with no implementation" % b["benchmark_id"])
        if b["status"] != "bound" and b.get("implementations"):
            problems.append("%s is not bound but names one" % b["benchmark_id"])

    missing = known - {b["benchmark_id"] for b in binds}
    if missing:
        problems.append("%d benchmarks have no binding row at all" % len(missing))

    schema = json.loads((ROOT / "schemas" / "run_log.schema.json").read_text())
    for field in ("harness_accepted", "false_completion", "held_back"):
        if field not in schema.get("properties", {}):
            problems.append("run_log schema lacks %r" % field)
    if "harness_accepted" not in schema.get("required", []):
        problems.append("run_log schema does not REQUIRE harness_accepted; without "
                        "it a refusal and a wrong delivery are indistinguishable")

    counts: Dict[str, int] = {}
    for b in binds:
        counts[b["status"]] = counts.get(b["status"], 0) + 1

    print("HIL Benchmark Library — validation")
    print("=" * 34)
    print("  native task specifications      %d" % len(native))
    print("  delegation-plane specifications %d" % len(deleg))
    print("  binding rows                    %d" % len(binds))
    print()
    for k in sorted(counts):
        print("  %-20s %d" % (k, counts[k]))
    runnable = counts.get("bound", 0)
    print()
    print("  RUNNABLE TODAY: %d of %d (%.0f%%)"
          % (runnable, len(binds), 100.0 * runnable / max(1, len(binds))))
    print("  band_only is not counted as runnable: a different family at the same")
    print("  band is a different task, and counting it would report coverage the")
    print("  suite does not have.")
    if problems:
        print()
        print("PROBLEMS")
        for p in problems:
            print("  - %s" % p)
        return 1
    print()
    print("no problems found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
