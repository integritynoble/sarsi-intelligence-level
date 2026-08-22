#!/usr/bin/env python3
"""Measure T_delta -- authorization latency -- from a hash-chained audit log.

T_delta is the interval between a candidate becoming available for promotion and
the promotion being authorized. It is the quantity that bounds a compensated
loop's iteration rate: once the automated steps are cheap, rho_max = 1/T_delta.

Usage:
    tdelta.py AUDIT.jsonl [AUDIT.jsonl ...] [--json] [--floor SECONDS]

Input format -- one JSON object per line:
    {"seq": int, "ts": ISO-8601, "kind": str, "payload": {...},
     "prev_hash": hex, "hash": hex}

Pairing: a `candidate_registered` is matched to the next `promote_version`
carrying the same (kind, name, version). Unmatched registrations are
right-censored -- they are observations ("at least this long"), not absences,
and are reported separately rather than dropped. Dropping them is how a
measurement of latency becomes a measurement of the subset that happened to
finish, which is the wrong quantity and biased fast.

The --floor check is the point of the tool as much as the mean is. An interval
below a plausible human review time does not indicate a fast organization; it
indicates the signature was produced by the same process that proposed. That is
a separation failure, and it makes the resulting T_delta a measurement of a
script rather than of an authorization.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

REGISTER = "candidate_registered"
PROMOTE = "promote_version"
SIGNATURE = "owner_signature"

#: Below this, an interval is almost certainly a scripted self-signature rather
#: than a reviewed authorization. Chosen as an order-of-magnitude floor on a
#: human reading an audited score and signing, not as a calibrated threshold.
DEFAULT_FLOOR_S = 60.0


def load(paths):
    records = []
    for p in paths:
        for lineno, line in enumerate(Path(p).read_text().splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append((str(p), lineno, json.loads(line)))
            except json.JSONDecodeError as exc:
                print(f"{p}:{lineno}: unparseable, skipped ({exc})", file=sys.stderr)
    records.sort(key=lambda r: (r[2].get("ts") or "", r[2].get("seq") or 0))
    return records


def check_chain(records):
    """Verify linkage only: each prev_hash equals the previous record's hash.

    This does not verify the hashes themselves, which would require the
    preimage convention. Linkage is checkable without it and catches the
    failure that matters here -- a record removed from the middle.
    """
    breaks = []
    prev = None
    for path, lineno, d in records:
        if prev is not None and d.get("prev_hash") != prev.get("hash"):
            breaks.append((path, lineno, d.get("seq")))
        prev = d
    return breaks


def key_of(d):
    p = d.get("payload") or {}
    return (p.get("kind"), p.get("name"), p.get("version"))


def parse_ts(d):
    ts = d.get("ts")
    if isinstance(ts, (int, float)):
        return datetime.fromtimestamp(ts, tz=timezone.utc)
    return datetime.fromisoformat(ts)


def measure(records, now=None):
    pending, paired, censored, orphan_promotions = {}, [], [], []
    for _path, _lineno, d in records:
        kind = d.get("kind")
        if kind == REGISTER:
            pending.setdefault(key_of(d), []).append(parse_ts(d))
        elif kind == PROMOTE:
            k = key_of(d)
            queue = pending.get(k)
            if queue:
                t0 = queue.pop(0)
                t1 = parse_ts(d)
                paired.append({"key": k, "registered": t0, "promoted": t1,
                               "t_delta_s": (t1 - t0).total_seconds()})
            else:
                orphan_promotions.append({"key": k, "promoted": parse_ts(d)})
    horizon = now or max((parse_ts(d) for _p, _l, d in records), default=None)
    for k, queue in pending.items():
        for t0 in queue:
            censored.append({"key": k, "registered": t0,
                             "at_least_s": (horizon - t0).total_seconds() if horizon else None})
    return paired, censored, orphan_promotions


def main():
    ap = argparse.ArgumentParser(description="Measure T_delta from an audit chain.")
    ap.add_argument("audit", nargs="+", help="audit .jsonl file(s)")
    ap.add_argument("--json", action="store_true", help="emit machine-readable output")
    ap.add_argument("--floor", type=float, default=DEFAULT_FLOOR_S,
                    help=f"separation-failure floor in seconds (default {DEFAULT_FLOOR_S:g})")
    ap.add_argument("--now", help="ISO timestamp to censor against (default: last record)")
    args = ap.parse_args()

    records = load(args.audit)
    if not records:
        print("no records", file=sys.stderr)
        return 2

    now = datetime.fromisoformat(args.now) if args.now else None
    breaks = check_chain(records)
    paired, censored, orphans = measure(records, now=now)
    degenerate = [p for p in paired if p["t_delta_s"] < args.floor]
    values = [p["t_delta_s"] for p in paired]
    reviewed = [p["t_delta_s"] for p in paired if p["t_delta_s"] >= args.floor]

    if args.json:
        json.dump({
            "records": len(records), "chain_breaks": len(breaks),
            "paired": paired, "censored": censored,
            "orphan_promotions": orphans,
            "degenerate": len(degenerate),
            "t_delta_reviewed_s": reviewed,
        }, sys.stdout, indent=2, default=str)
        print()
        return 0

    print(f"records            {len(records)}")
    print(f"chain linkage      {'OK' if not breaks else f'{len(breaks)} BREAK(S) at seq ' + str([b[2] for b in breaks])}")
    print(f"paired             {len(paired)}")
    print(f"censored           {len(censored)}   (registered, never promoted)")
    print(f"orphan promotions  {len(orphans)}   (promoted with no registration)")
    print()

    if paired:
        print("pairs:")
        for p in paired:
            flag = "  <-- below floor: not a reviewed authorization" if p["t_delta_s"] < args.floor else ""
            name = "/".join(str(x) for x in p["key"])
            print(f"  {name:<42} T_d = {p['t_delta_s']:>10.1f} s{flag}")
        print()

    if censored:
        print("censored (lower bounds, still outstanding):")
        for c in censored:
            name = "/".join(str(x) for x in c["key"])
            days = (c["at_least_s"] or 0) / 86400
            print(f"  {name:<42} T_d > {c['at_least_s']:>10.0f} s  ({days:.1f} days)")
        print()

    if degenerate:
        print(f"WARNING  {len(degenerate)}/{len(paired)} pair(s) below the {args.floor:g}s floor.")
        print("         An interval this short is a scripted self-signature, not an")
        print("         authorization. Proposer and promoter were not separated, so")
        print("         these intervals measure a script and must not enter the estimate.")
        print()

    if reviewed:
        print(f"T_delta over {len(reviewed)} reviewed authorization(s):")
        print(f"  median {statistics.median(reviewed):.1f} s   "
              f"max {max(reviewed):.1f} s   rho_max = {1/statistics.median(reviewed):.3g} /s")
    else:
        print("T_delta: NO reviewed authorizations in this log.")
        print("  Unmeasured is off the scale, not the bottom of it. The correct")
        print("  report is that the quantity has not been observed -- not a low number.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
