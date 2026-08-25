#!/usr/bin/env python3
"""Package DLI-Bench v0.2 for distribution: flat CSV, policies, README, zip.

The v0.1 bundle shipped a CSV whose columns were the JSONL's keys, one for one,
because every value was a scalar. v0.2's rows are not flat — `kappa`, `loss`,
`acceptance`, `verifier`, `difficulty_vector_framework` and
`load_instrumentation` are objects, and they are objects for a reason: p* and
rho travel together or they mean nothing, and a `false_pass_rate` separated from
the verifier it belongs to is a number nobody can attribute.

So the CSV flattens with dotted names — `loss.p_star`, `verifier.false_pass_rate`
— and the JSONL stays canonical. A reader who needs the structure reads the
JSONL; a reader who needs a spreadsheet gets one whose column names say where
each value came from.

Commentary keys (`$why_this_class_exists`, `$kappa_comment`, …) are kept. They
are the design argument for the row, and a bundle that drops them ships the
decisions without the reasons.

    python3 tools/pack_dli_bench.py
"""
from __future__ import annotations

import csv
import json
import pathlib
import zipfile

REPO = pathlib.Path(__file__).resolve().parent.parent
DATA = REPO / "dataset"
TASKS = DATA / "dli_bench_tasks_v0_2.jsonl"
MANIFEST = DATA / "dli_bench_manifest_v0_2.json"
OLD_ZIP = DATA / "DLI_Bench_v0_1_Dataset.zip"
NEW_ZIP = DATA / "DLI_Bench_v0_2_Dataset.zip"

#: Still current, and carried forward from the v0.1 bundle rather than rewritten
#: — the H and CID scales are the framework's and have not changed.
CARRIED = ("dli_bench_intervention_policy_v0_1.csv", "dli_bench_cid_policy_v0_1.csv")

HARNESS = {
    "autonomy_theater":
        "two bundles identical apart from the plan in the prompt",
    "approval_inflation":
        "an approval oracle answering only yes/no, and a log that separates "
        "governance from cognition",
    "silent_rescue":
        "a scripted operator that speaks the exact line at the exact trigger",
    "verification_leakage":
        "a file-access trace, and a deliberately readable sealed evaluator "
        "whose leak is reproduced exactly",
    "escalation_correct":
        "a bundle with a genuine, reproduced gap, and a grader who confirms the "
        "gap is real before the row is used",
    "saturation_gradient":
        "one toolchain shared by both members, so the difference is the task",
    "mission_drift":
        "a simulated feed with grader-controlled timestamps",
    "delegation_compression":
        "a fresh episode inheriting only the FIRST member's declared artifacts",
    "coordination_essential":
        "a partitioned bundle and a message bus the grader can read",
    "longitudinal_stability":
        "a harness that interrupts an episode at a declared point and restarts "
        "it cleanly with durable state and no conversation history",
    "h_sweep":
        "one bundle and one seed, three written intervention policies",
    "intervention_timing":
        "two members identical apart from WHEN the fact is delivered",
}


#: `None` becomes this, and an empty string stays empty. CSV has one blank cell
#: and the dataset needs two meanings for it: Rule 11 turns on the difference
#: between a false-pass rate that is EXPLICITLY unknown and one nobody recorded,
#: and `probe_kind: ""` legitimately means "an ordinary row". Writing both as a
#: blank would collapse the distinction the field exists to make.
NULL = "null"


def _cell(v):
    if v is None:
        return NULL
    if isinstance(v, list):
        return "; ".join(map(str, v))
    return v


def flatten(row):
    """Dotted column names, one level deep. Lists become `; `-joined strings."""
    out = {}
    for k, v in row.items():
        if isinstance(v, dict):
            for k2, v2 in v.items():
                out[f"{k}.{k2}"] = _cell(v2)
        else:
            out[k] = _cell(v)
    return out


def readme(rows, cols):
    import collections
    strata = collections.Counter(r["stratum"] for r in rows)
    probes = collections.Counter(r["probe_kind"] for r in rows if r.get("probe_kind"))
    bands = collections.defaultdict(collections.Counter)
    for r in rows:
        bands[r["split"]][r["task_band"]] += 1
    order = ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "TΩ"]

    lines = [
        "# DLI-Bench v0.2",
        "",
        "Delegation Intelligence benchmark specifications, for the framework in",
        "*Delegation Intelligence: A Task-Difficulty, Human-Intervention, and",
        "Reliability Framework for Autonomous AI Agents and Organizations*",
        "(Yang, Chengshuai, August 2026), with the measurement repairs from",
        "*Difficulty Is Not The Index*.",
        "",
        f"**{len(rows)} task specifications in four strata.** "
        f"{len(rows[0])} fields per row in the JSONL; {len(cols)} columns in "
        f"the CSV, which is larger because the nested objects are flattened.",
        "",
        "| stratum | n | what it is for |",
        "|---|---|---|",
        f"| `ladder` | {strata['ladder']} | v0.1's eight DL bands x six families, "
        "enriched with d_risk, kappa, t_do, loss/p*, acceptance and verifier blocks |",
        f"| `kappa_cross` | {strata['kappa_cross']} | low t_do crossed with high "
        "verification and risk, and its converse: where non-closure becomes observable |",
        f"| `budget_cross` | {strata['budget_cross']} | one task class held fixed "
        "across H0, H1 and H2, so S(T,h) varies in h at fixed T |",
        f"| `probe` | {strata['probe']} | falsifying observations for the "
        "anti-inflation rules and failure modes |",
        "",
        "## Why the probe stratum exists",
        "",
        "The other three measure whether a system succeeded. None of them can",
        "catch a wrong answer *about itself*: the plan was in the prompt, the",
        "operator said \"maybe check X\", the sealed evaluator was readable, the",
        "approvals were counted as thinking, the T1 member carried the average.",
        "",
        "Every probe row carries **`falsified_if`** — the observation that voids",
        "the claim however good the artifact is — and **`rules_exercised`**,",
        "naming the section it comes from. A probe that fires does not lower the",
        "DL number. It withdraws it.",
        "",
        "| probe_kind | n | harness it requires |",
        "|---|---|---|",
    ]
    for k in sorted(probes):
        lines.append(f"| `{k}` | {probes[k]} | {HARNESS.get(k, '')} |")

    lines += [
        "",
        "## Splits",
        "",
        "Every split spans low and high bands. In v0.1 each DL band sat in one",
        "split, so the certification set's lowest band was T4 — and",
        "`F_A(h,p) = max{T : S_A(T,h) >= p}` is a maximum over a set that then",
        "had nothing underneath it. Non-closure sharpens the same point: the",
        "lower bands are not implied by the higher ones and have to be present",
        "to be known.",
        "",
        "```",
    ]
    for s in ("dev", "validation", "certification_hidden"):
        cells = " ".join(f"{b}:{bands[s][b]}" for b in order if bands[s][b])
        lines.append(f"{s:22} {cells}")
    lines += [
        "```",
        "",
        "## Files",
        "",
        "- `dli_bench_tasks_v0_2.jsonl` — canonical. Nested objects intact.",
        "- `dli_bench_tasks_v0_2.csv` — the same rows flattened with dotted",
        "  column names (`loss.p_star`, `verifier.false_pass_rate`). JSON null",
        "  is written as the literal `null`, never as a blank: Rule 11 turns on",
        "  the difference between a false-pass rate that is explicitly unknown",
        "  and one nobody recorded, and a blank cell cannot hold both. Use the",
        "  JSONL when the structure matters.",
        "- `dli_bench_manifest_v0_2.json` — strata counts, what v0.1 could not",
        "  measure, and the excluded classes.",
        "- `dli_bench_probe_policy_v0_2.csv` — one row per probe kind.",
        "- `dli_bench_intervention_policy_v0_1.csv` — H0-H5. Unchanged.",
        "- `dli_bench_cid_policy_v0_1.csv` — CID0-CID6. Unchanged.",
        "",
        "## What this is not",
        "",
        "**A sealed executable benchmark.** These are specifications. Rows marked",
        "`certification_hidden` must be instantiated from `environment_seed`,",
        "with the verifier and reference kept outside the tested system.",
        "",
        "**Calibrated.** Difficulty and loss figures are design labels. Every",
        "verifier reports its false-pass rate as `null`, meaning unknown — which",
        "is the honest value and the common one, and it means every frontier",
        "drawn from this set is an upper bound whose gap is largest where",
        "verification is weakest.",
        "",
        "## Checks",
        "",
        "```console",
        "python3 tools/check_dli_bench.py       # the measurement repairs",
        "python3 tools/check_probe_stratum.py   # the anti-inflation rules",
        "```",
        "",
        "Two checkers, one dataset, disjoint rules. A rule enforced in both would",
        "drift. Both have a `--self-test` that proves each check fires on a row",
        "built to break it.",
        "",
        "## Reporting",
        "",
        "```",
        "DL profile   = {F_A(H0,p), F_A(H1,p), F_A(H2,p), load per CID band,",
        "                CID distribution, success CI, cost, latency}",
        "probe results = per probe_kind: passed / falsified, with the falsifying",
        "                observation quoted when it fired",
        "```",
        "",
        "Report the frontier per kappa cell. Across cells it is a different",
        "question, and a single maximum answers neither.",
        "",
    ]
    return "\n".join(lines)


def main():
    rows = [json.loads(l) for l in TASKS.read_text().splitlines() if l.strip()]
    flat = [flatten(r) for r in rows]
    cols = []
    for r in flat:
        for k in r:
            if k not in cols:
                cols.append(k)

    csv_path = DATA / "dli_bench_tasks_v0_2.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in flat:
            w.writerow({k: r.get(k, "") for k in cols})

    probe_path = DATA / "dli_bench_probe_policy_v0_2.csv"
    seen = {}
    counts = {}
    for r in rows:
        k = r.get("probe_kind")
        if k:
            seen.setdefault(k, r)
            counts[k] = counts.get(k, 0) + 1
    with probe_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["probe_kind", "n_rows", "framework_section",
                    "expected_outcome_class", "falsified_if",
                    "harness_requirement"])
        for k in sorted(seen):
            r = seen[k]
            w.writerow([k, counts[k], r["rules_exercised"],
                        r["expected_outcome_class"], r["falsified_if"],
                        HARNESS.get(k, "")])

    readme_path = DATA / "DLI_BENCH_V0_2_BUNDLE_README.md"
    readme_path.write_text(readme(rows, cols))

    # The two policy CSVs are still current; carry them out of the v0.1 bundle
    # rather than restating them, so there is one text for the H and CID scales.
    carried = {}
    if OLD_ZIP.exists():
        with zipfile.ZipFile(OLD_ZIP) as z:
            for name in CARRIED:
                if name in z.namelist():
                    carried[name] = z.read(name)

    with zipfile.ZipFile(NEW_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("README.md", readme_path.read_text())
        for p in (TASKS, csv_path, MANIFEST, probe_path):
            if p.exists():
                z.write(p, p.name)
        for name, data in carried.items():
            z.writestr(name, data)

    print(f"csv      {csv_path.name}  {len(flat)} rows x {len(cols)} cols")
    print(f"probes   {probe_path.name}  {len(seen)} kinds")
    print(f"readme   {readme_path.name}")
    print(f"bundle   {NEW_ZIP.name}  {NEW_ZIP.stat().st_size // 1024} KB")
    with zipfile.ZipFile(NEW_ZIP) as z:
        for n in z.namelist():
            print(f"           {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
