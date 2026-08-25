# DLI-Bench v0.2

Delegation Intelligence benchmark specifications, for the framework in
*Delegation Intelligence: A Task-Difficulty, Human-Intervention, and
Reliability Framework for Autonomous AI Agents and Organizations*
(Yang, Chengshuai, August 2026), with the measurement repairs from
*Difficulty Is Not The Index*.

**180 task specifications in four strata.** 69 fields per row in the JSONL; 96 columns in the CSV, which is larger because the nested objects are flattened.

| stratum | n | what it is for |
|---|---|---|
| `ladder` | 96 | v0.1's eight DL bands x six families, enriched with d_risk, kappa, t_do, loss/p*, acceptance and verifier blocks |
| `kappa_cross` | 12 | low t_do crossed with high verification and risk, and its converse: where non-closure becomes observable |
| `budget_cross` | 36 | one task class held fixed across H0, H1 and H2, so S(T,h) varies in h at fixed T |
| `probe` | 36 | falsifying observations for the anti-inflation rules and failure modes |

## Why the probe stratum exists

The other three measure whether a system succeeded. None of them can
catch a wrong answer *about itself*: the plan was in the prompt, the
operator said "maybe check X", the sealed evaluator was readable, the
approvals were counted as thinking, the T1 member carried the average.

Every probe row carries **`falsified_if`** — the observation that voids
the claim however good the artifact is — and **`rules_exercised`**,
naming the section it comes from. A probe that fires does not lower the
DL number. It withdraws it.

| probe_kind | n | harness it requires |
|---|---|---|
| `approval_inflation` | 2 | an approval oracle answering only yes/no, and a log that separates governance from cognition |
| `autonomy_theater` | 6 | two bundles identical apart from the plan in the prompt |
| `coordination_essential` | 2 | a partitioned bundle and a message bus the grader can read |
| `delegation_compression` | 4 | a fresh episode inheriting only the FIRST member's declared artifacts |
| `escalation_correct` | 3 | a bundle with a genuine, reproduced gap, and a grader who confirms the gap is real before the row is used |
| `h_sweep` | 3 | one bundle and one seed, three written intervention policies |
| `intervention_timing` | 2 | two members identical apart from WHEN the fact is delivered |
| `longitudinal_stability` | 3 | a harness that interrupts an episode at a declared point and restarts it cleanly with durable state and no conversation history |
| `mission_drift` | 2 | a simulated feed with grader-controlled timestamps |
| `saturation_gradient` | 4 | one toolchain shared by both members, so the difference is the task |
| `silent_rescue` | 3 | a scripted operator that speaks the exact line at the exact trigger |
| `verification_leakage` | 2 | a file-access trace, and a deliberately readable sealed evaluator whose leak is reproduced exactly |

## Splits

Every split spans low and high bands. In v0.1 each DL band sat in one
split, so the certification set's lowest band was T4 — and
`F_A(h,p) = max{T : S_A(T,h) >= p}` is a maximum over a set that then
had nothing underneath it. Non-closure sharpens the same point: the
lower bands are not implied by the higher ones and have to be present
to be known.

```
dev                    T0:4 T1:12 T2:10 T3:11 T4:5 T5:4 T6:4 TΩ:4
validation             T0:5 T1:9 T2:6 T3:19 T4:24 T5:4 T6:4 TΩ:4
certification_hidden   T0:4 T1:7 T2:7 T3:9 T4:10 T5:4 T6:5 TΩ:5
```

## Files

- `dli_bench_tasks_v0_2.jsonl` — canonical. Nested objects intact.
- `dli_bench_tasks_v0_2.csv` — the same rows flattened with dotted
  column names (`loss.p_star`, `verifier.false_pass_rate`). JSON null
  is written as the literal `null`, never as a blank: Rule 11 turns on
  the difference between a false-pass rate that is explicitly unknown
  and one nobody recorded, and a blank cell cannot hold both. Use the
  JSONL when the structure matters.
- `dli_bench_manifest_v0_2.json` — strata counts, what v0.1 could not
  measure, and the excluded classes.
- `dli_bench_probe_policy_v0_2.csv` — one row per probe kind.
- `dli_bench_intervention_policy_v0_1.csv` — H0-H5. Unchanged.
- `dli_bench_cid_policy_v0_1.csv` — CID0-CID6. Unchanged.

## What this is not

**A sealed executable benchmark.** These are specifications. Rows marked
`certification_hidden` must be instantiated from `environment_seed`,
with the verifier and reference kept outside the tested system.

**Calibrated.** Difficulty and loss figures are design labels. Every
verifier reports its false-pass rate as `null`, meaning unknown — which
is the honest value and the common one, and it means every frontier
drawn from this set is an upper bound whose gap is largest where
verification is weakest.

## Checks

```console
python3 tools/check_dli_bench.py       # the measurement repairs
python3 tools/check_probe_stratum.py   # the anti-inflation rules
```

Two checkers, one dataset, disjoint rules. A rule enforced in both would
drift. Both have a `--self-test` that proves each check fires on a row
built to break it.

## Reporting

```
DL profile   = {F_A(H0,p), F_A(H1,p), F_A(H2,p), load per CID band,
                CID distribution, success CI, cost, latency}
probe results = per probe_kind: passed / falsified, with the falsifying
                observation quoted when it fired
```

Report the frontier per kappa cell. Across cells it is a different
question, and a single maximum answers neither.
