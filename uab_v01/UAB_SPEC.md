# Unified Agent Benchmark (UAB) v0.1 — specification

**Framework:** *Measuring the Unified Intelligence Level*, v2.3 (`../unified_v23`).
**Plan:** `../plan/Unified_Agent_Intelligence_Development_Plan.md` §5–§10, §17–§20, §34.
**Status:** frozen contract, small bound core. Coverage is stated in `matrix/uab_matrix_v0_1.md` and is
regenerated, never hand-edited.

## 1. What UAB certifies

A frozen **model–harness pair** `A(m, h)`, on a frozen task set, judged by a verifier the pair did not
author, at a declared intervention budget. The output is not a score. It is a profile:

```
[C, I, O, T, H, SA]  at reliability p,  with M reported beside I
U* = highest Unified level whose gate and every lower retention suite pass
```

Promotion is a hard gate (v2.3 Eq. 3), never an average. `O` is omitted and named as omitted for an
individual unit. `unmeasured` is never `0`.

## 2. Levels in scope

UAB v0.1 scopes **U0–U3**:

| level | gate (all must hold) | delegation gate |
|---|---|---|
| U0 Reactive | C0, I0, O0, SA0 | T0 at H5–H4 |
| U1 Persistent | C1, I1 (needs M1), O1, SA1 | T1 at ≤H3 |
| U2 Adaptive | C2, I2 (needs M3), O2, SA2 | T2 at ≤H2 |
| U3 Self-improving | C3, I3 (needs M4), O3, SA3 | T3 at ≤H1 |

Retention: `U_n ⇒ U_(n-1)`; the lower suites are re-run at every promotion (`policies/RETENTION_POLICY.md`).

## 3. The delegation primitive and the four outcomes

Every delegation episode records `harness_accepted` (null where the harness has no acceptance step)
and `verifier_pass` separately. Four outcomes are derived, never typed:

| accepted | verifier | outcome |
|---|---|---|
| yes / n/a | pass | delivered and correct |
| yes / n/a | fail | **false completion** |
| no | fail | held back (correct refusal) |
| no | pass | false rejection |

```
S_net(T, H) = P(delivered and verifier pass) − ρ(τ) · P(false completion),  clamped at 0
```

`ρ` is the class's loss ratio and `p* = ρ/(1+ρ)` the reliability the class requires. A class with
unbounded residual harm has `p* = 1` and is in the benchmark **to be refused**. Setting `ρ = 0`
reproduces the success-only figure for audit.

## 4. What every task records

```
(T, H, p, R, V, C)   band, budget, verified reliability, resource envelope, verifier version, cost
```

plus, per episode: attempts, harness iterations, model calls, wall time, tokens, `exit_status`,
`limit_reached`, `termination_reason ∈ {normal, timed_out, crashed, not_attempted}`, interventions
with CID, forecast id where SA4 is attached. A run the runner killed is `timed_out` or
`not_attempted`, never a delivery.

For U1+: restart success, provenance recovery, stale-state suppression. For U2+: held-out transfer,
repeat-error reduction, lesson rollback. For U3+: self-improvement gain, regression rate.
Always: false-completion rate, held-back rate, false-rejection rate, human load, cost per verified
completion, verifier disagreement, per-band headroom.

## 5. Bands per domain (T0–T6)

| band | paper | funding | job | code | research | business |
|---|---|---|---|---|---|---|
| T0 | one citation/table/figure generated or verified | one deadline or eligibility requirement extracted | requirements extracted from one posting | one explicit code edit | one fact retrieved or calculated | one market/company fact |
| T1 | routine section from supplied evidence | one call evaluated against one applicant | fit assessed for one position | routine bug fixed with tests | one known analysis reproduced | one bounded analysis |
| T2 | multi-step literature/analysis/figure/writing task | find, compare, rank opportunities | search, compare, tailor, keep state across applications | multi-file feature | specified multi-step workflow | multi-step competitor/customer/market assessment |
| T3 | complex revision with verification | funding strategy and proposal workflow | multi-company application strategy | ambiguous repo-scale failure diagnosed and recovered | strategy chosen, failures diagnosed, alternatives run | strategy under uncertainty and conflicting evidence |
| T4 | full expert paper project under a frozen question | long-horizon grant preparation | complete long-horizon campaign | long-horizon software project | complete project under a frozen benchmark | long-running business project |
| T5 | paper requiring an unknown method | non-obvious strategy discovered and validated | strategy that improves verified outcomes | unknown solution method for a sealed task | unknown mechanism discovered and validated | new strategy or opportunity validated |
| T6 | mission → project, experiments, manuscript, submission | mission → funding portfolio | mission → full campaign | mission → projects | mission → project portfolio | mission → project portfolio |

T5 and above admit **no static item**: a level defined by an unknown answer is certified only by
instances generated after the pair is frozen and graded on extrapolation (v2.3 §16.12).

## 6. Manifest

Every family is one JSON manifest validating against `TASK_MANIFEST.schema.json`, hashed with the
`hash` field empty, and frozen by that hash. The manifest names: domain, family, coordinate, band,
budgets and CID ceiling, mission and deliverables, the resource limit **the runner enforces**, the
authority envelope (anything absent is forbidden; outward actions default to false), the acceptance
block (weakest admissible locus, `σ` bound, required rate, `ρ`, hard failures), the verifier (type,
version, hidden, spec–key test), retention suites, binding status and asset, and provenance.

## 7. Binding status

| status | meaning |
|---|---|
| `BOUND` | a runnable instance set or seeded generator exists **for this domain and this band** |
| `GENERATOR_BOUND` | bound, and instances are generated per seed with a computed key |
| `BAND_ONLY` | something runs at this band, for another family; **not coverage** |
| `SPECIFICATION_ONLY` | nothing runs; the named starter is where binding would begin |

## 8. Separation

Protected (outside every candidate's write set): hidden tests, frozen manifests, acceptance
thresholds, held-out data, the primary verifier, certification task selection, the promotion decision.
Writable: agent code, prompts, memory policies, planning policies, tool routing, workflow, sub-agent
organization, candidate improvements. *The designer may design. It may not grade itself.*

## 9. Validity requirements carried from v2.3

Parameterised families ship a **specification–key test** run on drawn instances against the key's
own reference implementation. Any item two executors of materially different capability fail with
the same response is **concordance-audited** before the failure is attributed. Graded scoring with
separated failure modes where a boolean would hide the signal. Per-band **headroom** reported beside
every coordinate. Termination reason on every episode.

## 10. Files

```
UAB_SPEC.md                    this file
TASK_MANIFEST.schema.json      JSON Schema (draft 2020-12)
manifests/*.json               one per bound family (16 in v0.1)
matrix/uab_matrix_v0_1.{csv,md}  generated coverage matrix
policies/INTERVENTION_POLICY.md  H0–H5, CID, governance separation
policies/RESOURCE_POLICY.md      envelope and enforcement
policies/VERIFIER_POLICY.md      loci, hidden/public split, disagreement
policies/RETENTION_POLICY.md     promotion and regression
tools/build_manifests.py, build_matrix.py, validate.py
```
