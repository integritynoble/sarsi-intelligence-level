# HIL Benchmark Library v1.1

Benchmark library for Harness-Level Intelligence, aligned to HIL framework
**v1.6**. Derived from v1.0 (framework v1.5.1); everything in v1.0 is carried
forward.

## What v1.1 adds

v1.0 is a large, well-organised specification of what to measure. v1.1 adds the
part that checks whether the items can measure it.

**The items are audited now.** `tools/audit_items.py` run against v1.0 unchanged
reports five errors, all recorded in `docs/AUDIT_v1_0.md`. v1.0's own
`validate_library.py` passes the same tree with zero errors — it checks that
required columns are populated and ids are unique, which is real and is not the
same question. The headline finding: **16 bound instances, 12 distinct
payloads.** Three C0/C1 pairs and one T0/T1 pair were byte-identical, so those
level pairs carried no evidence that could tell them apart. Fixed in v1.1.

**Wrong answer keys are detectable without publishing the key.**
`tools/concordance_audit.py` flags items where executors of materially different
capability return the *same* response and the key disagrees with all of them.
Independent systems rarely agree on the answer to a genuinely hard question and
routinely agree on the answer to a clear one, so concordant error is weak
evidence of a hard item and strong evidence of a wrong key. This found two real
defects in the framework's own T4 items, each of which had passed a test suite
written for it and each of which had been scored as a model failure.

**Scores are graded, and failure modes are separated.** `item_score` in [0,1]
alongside the boolean, and a `failure_mode` enum, because "misread the
specification", "searched too shallowly", "crashed" and "timed out" need
different repairs and a single failed bucket reports them identically.

**Headroom is reported.** `score_hil.py` now emits the fraction of items on
which the best executor present is not already at maximum. Near zero, a
coordinate is reporting the suite's ceiling rather than the system's, and every
HLIS and HIL figure drawn from it is bounded above by the benchmark.

## Coverage

| Suite | Tasks | Measures |
|---|---|---|
| C-Bench | 128 | Cognitive Intelligence C |
| I-Bench | 98 | Individual Intelligence I, long-term memory embedded |
| O-Bench | 84 | Organizational Intelligence O |
| DI-Bench | 162 | T0–TΩ × H0–H5 delivered-and-correct delegation |
| SA-Bench | 96 | Evidence-grounded self-awareness |
| U-Bench | 32 | Cumulative U0–UΩ gates and retention |
| HIL-Ladder | 32 | One frozen model across HG0→HGΩ |
| VR-Bench | 24 | Verification responsiveness |
| HDS-Bench | 12 | Harness design gain under hidden external evaluation |

668 native task specifications: 16 bound, 2 generator-bound, 650
specification-only.

## Binding statuses

- **bound** — instance and answer staged in `starter/`. Development examples,
  not hidden certification tasks.
- **generator-bound** *(new)* — instances produced from a seed by a named,
  versioned generator named in `generator_ref`, which lives outside this
  archive. The generator is not copied in: a second home for it would drift
  from the first, and the drift would be invisible.
- **specification-only** — the task is specified and has no instances yet.

## Definitions

```
S_del(T,H) = P(delivered = 1 AND verifier_pass = 1)
F(H,p)     = max{ T : S_del(T,H) >= p }
HLIS       = 100 * exp( sum(alpha_d * ln A_d) / sum(alpha_d) )
HSC_m(k)   = HLIS(m, HG_k)
headroom   = fraction of items where the best executor is not at maximum
```

## Tools

| Tool | Purpose |
|---|---|
| `validate_library.py <catalog.csv>` | Columns populated, ids unique, binding vocabulary valid |
| `audit_items.py` | Items distinct across levels, bands not misfiled, generator refs resolvable |
| `concordance_audit.py --responses <jsonl>` | Items whose key is probably wrong |
| `score_hil.py --runs <csv> --tasks <catalog.csv>` | Surface, frontier, headroom, failure modes, concordance readiness |
| `verify_starter.py <instance> <answer> <candidate>` | Exact-match check for one bound instance |

`audit_items.py` and `validate_library.py` exit non-zero on findings and belong
in CI. `concordance_audit.py` exits zero and prints work to do: a tool that
fails the build on a finding gets removed from the build.

## What this library does not establish

- **Long context does not certify I1.** Formal I1 and above require genuine
  restart or context discontinuity. `I-I1-RESTART_CONT-A` simulates its restart
  inside one payload and is a development example only.
- **Bound starter tasks are development examples**, not hidden certification
  tasks.
- **650 rows are specification-only.** They have no answer key yet, so they can
  be neither validated nor found wrong.
- **The audit has unknown recall.** Items it did not flag are unaudited.
- **Concordance auditing at two tiers has an unquantified false-positive rate.**
  Two models from overlapping training distributions can share a misreading.
  Three independent lineages would separate that from a defective key.
- **HG3–HGΩ certification** requires sealed environments, longitudinal trials,
  independent verifier ownership and protected hidden assets. None of that is
  in this archive.
