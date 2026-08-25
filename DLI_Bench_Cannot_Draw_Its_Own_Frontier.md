# DLI-Bench Cannot Draw Its Own Frontier

## What v0.1 measures, what it cannot, and the v0.2 that can

*Working note — 24 August 2026*
*Applies: [`Difficulty_Is_Not_The_Index.md`](Difficulty_Is_Not_The_Index.md) — the four repairs — to the dataset in [`dataset/`](dataset/)*
*Reads alongside: [`Delegation_Is_A_Property_Of_The_Task.md`](Delegation_Is_A_Property_Of_The_Task.md), [`Delegation_Levels.md`](Delegation_Levels.md)*

---

## Summary

DLI-Bench v0.1 is 96 well-formed task specifications, balanced eight ways by
level and six ways by family, with a difficulty vector, an intervention policy
and an intervention-depth policy. Every row is internally consistent.

**It cannot produce a delegation frontier**, which is the number it exists to
produce. The reason is not in any row. It is that every design variable in the
dataset is a deterministic function of one variable, so the benchmark has one
independent variable wearing six names.

| Variable | Distinct values within a single band |
|---|---|
| `primary_intervention_budget` | 1 |
| `reliability_target` | 1 |
| `max_cid` | 1 |
| `time_budget_minutes` | 1 |
| `dynamic_environment` | 1 |
| `difficulty_horizon`, `difficulty_ambiguity`, `difficulty_verification`, `difficulty_novelty` | 1 |
| `difficulty_coordination`, `difficulty_uncertainty`, `difficulty_tool_diversity`, `difficulty_env_change` | 2 |

`target_dl` and `task_band` take exactly eight joint values across 96 rows —
`(DL0,T0)` through `(DLΩ,TΩ)` — so the level being claimed and the difficulty
being tested are also the same variable.

---

## 1. The frontier is not computable

$$F_A(h,p) = \max\{T : S_A(T,h) \ge p\}$$

is a maximum over a set. Evaluating it at a budget requires several bands tested
under that budget. In v0.1:

| Budget | Bands beneath it |
|---|---|
| H0 | TΩ |
| H1 | T3, T4, T5, T6 |
| H2 | T2 |
| H3 | T1 |
| H5–H4 | T0 |

At three of the five budgets the maximum ranges over a single point. The
framework's own reporting profile — $\{F(H0,p), F(H1,p), F(H2,p)\}$ — is
therefore **not computable from the dataset**, and where it is nominally
computable the answer restates the design rather than measuring a system.

The general form of the defect: no band is tested under two budgets, so
$S(T,h)$ never varies in $h$ at fixed $T$. There is no arrangement of runs over
these 96 tasks that separates *the task got harder* from *the human helped less*.

## 2. Proposition 1 is unobservable by construction

Non-closure requires the difficulty coordinates to disagree about the ordering,
and it is $d_{ver}$ that disagrees — it lowers $S$ under every $h$ and for every
agent. In v0.1 $d_{ver}$ takes exactly one value per band:

| Band | T0 | T1 | T2 | T3 | T4 | T5 | T6 | TΩ |
|---|---|---|---|---|---|---|---|---|
| $d_{ver}$ | 1 | 1 | 2 | 3 | 4 | 5 | 5 | 5 |

Perfectly collinear with the band it is aggregated into. So the coordinates
cannot disagree, non-closure cannot occur, and the proposition the repair rests
on has no possible witness in the corpus.

The paper's own counterexample — a T0–T1 class with maximal $d_{ver}$ and
maximal $d_{risk}$, *compose and send one external message* — **has no
representative among the 96.** A dataset that cannot exhibit the counterexample
to the framework it implements cannot falsify it.

The same collinearity makes Proposition 2 unidentifiable. The verifier's
false-pass rate $\phi$ is governed by $d_{ver}$; if $d_{ver}$ moves only with
the band, no observation separates *hard to do* from *hard to check*, and the
upward bias cannot be estimated even in principle.

## 3. $d_{risk}$ is absent, so Repair 2 has no inputs

The framework's vector is

$$d(\tau) = \langle d_{dec}, d_{hor}, d_{unc}, d_{tool}, d_{nov}, d_{ver}, d_{coord}, d_{risk}\rangle$$

v0.1 carries eight coordinates and `env_change` sits where $d_{risk}$ should be.
Cost of error is not recorded anywhere in the dataset. Consequently $\rho$,
$p^\star$, Corollary 3.1's irreversibility floor and the whole of Repair 2 have
nothing to compute from.

What v0.1 has instead is `reliability_target`, chosen by the evaluator and
**falling as the band rises** — 0.95 at T0 down to 0.60 at TΩ. Proposition 3
says $p$ is the class's to set, not the evaluator's, and that $p^\star$ rises
where failure is expensive. v0.1's targets move in the opposite direction from
the quantity they stand in for.

No class in v0.1 reaches $p^\star = 1$. That is not a pass: a delegation
benchmark containing no irreversible class is silent about exactly the classes
people most need a delegation answer for.

## 4. Nothing records who accepted

There is no field for the acceptance locus and none for the self-authored
acceptance fraction. By Proposition 4 a self-certified level and a measured one
therefore produce identical rows.

This bites hardest at the top. $\sigma \to 1$ at DLΩ by construction, and
Corollary 5.1 says a DL6 or DLΩ claim is **unmeasurable**, not merely hard to
measure, unless $\sigma$ is bounded below one by structure. v0.1 contains 24
tasks at DL6 and DLΩ, none of which carries such a bound.

---

## 5. What v0.2 changes

Built by [`tools/build_dli_bench_v0_2.py`](tools/build_dli_bench_v0_2.py); v0.1's
96 rows are kept as the **ladder stratum** and extended, never discarded.

**Fields**, one per repair:

| Added | Repair | Carries |
|---|---|---|
| `difficulty_risk` | 2 | the framework's missing eighth coordinate |
| `kappa` | 1 | $\langle d_{ver}, d_{risk}\rangle$, reported and never aggregated |
| `t_do` | 1 | the remaining six, aggregated as the band always was |
| `loss` | 2 | $V, C_{det}, C_{undo}, C_{res}, \rho, p^\star$ |
| `acceptance` | 3 | $\alpha$, $\sigma$ bound and its mechanism, criterion register |
| `verifier` | Rule 11 | identity, and $\phi$ or an explicit `unknown` |
| `load_instrumentation` | 4 | the timestamp pair whose difference is $T_\delta$ |

`reliability_target` is demoted to `reliability_target_v0_1` and superseded by
`loss.p_star`.

**Strata**, which is the half that fields alone could not fix:

- **kappa-cross** (12 tasks) — doing-difficulty and stakes pulled apart on
  purpose. Six low-band classes with high $\kappa$, including the paper's own
  counterexample and two at the irreversibility floor; six high-band classes
  with $\kappa$ near zero, which is where delegation actually works and where a
  band-indexed frontier understates it. Budget and split are held fixed so the
  only thing varying against the ladder is $\kappa$.
- **budget-cross** (36 tasks) — twelve classes instantiated at H0, H1 and H2
  each. This is what makes $S(T,h)$ vary in $h$ at fixed $T$, and therefore what
  makes the reporting profile computable at all.
- **probe** (36 tasks) — added separately, by
  [`tools/add_probe_stratum.py`](tools/add_probe_stratum.py), and complementary
  rather than overlapping: the strata above repair what the benchmark can
  *measure*, while the probes catch a claim that is wrong *about itself*. Each
  carries `falsified_if` — the observation that voids the claim however good the
  artifact — against the framework's ten anti-inflation rules and six failure
  modes: autonomy theatre, silent rescue, approval inflation, verification
  leakage, mission drift, and the rest. Nothing in the ladder or the crosses can
  detect any of them, because a task measures whether the system succeeded and
  none of these ask whether the success was the system's.

**An excluded-class register** (4 entries) in the manifest: classes with no
external criterion, recorded rather than dropped. Where no criterion exists
$S^V$ is undefined rather than small, so the class leaves the maximum silently
and the frontier reads high because of what is missing from it.

Result:

| | v0.1 | v0.2 |
|---|---|---|
| Tasks | 96 | 180 |
| Bands under H0 / H1 / H2 | 1 / 4 / 1 | 5 / 8 / 4 |
| Bands tested at ≥2 budgets | 0 | 6 |
| $\kappa$ cells in the T1 band | 1 | 8 |
| Classes at $p^\star = 1$ | 0 | 2 |
| $p^\star$ range | — (evaluator-chosen 0.60–0.95) | 0.038 – 1.000, class-derived |
| Bands spanned by `certification_hidden` | T3–TΩ | all eight |

The last row was a defect of this rebuild rather than of v0.1's authors, and it
is the same defect one level down: the ladder stratum inherited a certification
split assigned to the top half only, so a *sealed* set had no anchor beneath the
band being certified and reproduced, inside certification, exactly the
"maximum over a point" problem the rest of the work removes. One family's
low-band budget-cross groups are sealed to fix it.

---

## 6. The check

[`tools/check_dli_bench.py`](tools/check_dli_bench.py) applies the four repairs
to a dataset file. Its self-test asserts **v0.1 fails and v0.2 passes** — both
halves, because a checker that only ever passes has not been shown to detect
anything, and the defect it is built for is one every individual row survives.

v0.1 fails ten checks. The first three are the structural ones, and they are the
reason this note exists: they are invisible to per-row validation.

Two kinds of check are needed and they do not overlap. This one holds the
dataset to the four repairs. The other holds it to the framework's own §10 rules
and §16 failure modes — a benchmark whose rows violate Rule 1 cannot enforce
Rule 1 on a system — and travels with the probe stratum. The composed v0.2
passed both when last run together on 2026-08-25; the rules-side checker was
removed from `dataset/` shortly afterwards and is not linked here until it has
a settled home.

---

## 7. What is still not true of v0.2

- **Nothing here is calibrated.** Difficulty and loss figures are design labels.
  The $\rho$ values are stipulated, not measured, and a stipulated $\rho$ gives a
  stipulated $p^\star$.
- **Every $\phi$ is `null`.** That is the honest value and the common one, and it
  means every frontier drawn from this dataset is an upper bound whose gap is
  largest exactly where $d_{ver}$ is highest.
- **The assets do not exist.** As in v0.1, rows are specifications; the
  `certification_hidden` split still has to be instantiated from the seeds, with
  the verifier and reference kept outside the tested system.
- **$\sigma$ is bounded by declaration, not yet by build.** The mechanism is
  named per task — a criterion register outside the write set, a separated
  acceptor holding the pen on subgoal criteria — and naming it is not enforcing
  it. The engineering half exists in the companion agent-design framework as
  *evaluator not in write set*; wiring the register to it is not done here.
- **The kappa-cross classes are the ones a benchmark cannot safely execute.**
  Send an external message, delete records with no undo, commit a budget line:
  their $p^\star$ is at or near 1, which means they are in the dataset **to be
  refused or escalated, not passed**. Scoring them requires a harness whose
  side effects are contained, and containing the side effect changes the class.
  That tension is real and is not resolved here.
