# A Model Does Not Have a Level

## The (harness, model) pair as the unit of measurement, a gated score that refuses to average, and what a harness-indexed number can honestly say about an LLM

*Working paper — 25 August 2026*
*Builds on: `Unified_Intelligence_Six_Coordinate_Framework.pdf` (the [C, I, O, T, H, SA] profile and the gated U0–UΩ scale), `Delegation_Intelligence_Framework.pdf` (T0–T6, H0–H5, the frontier), `Difficulty_Is_Not_The_Index.md` (the four repairs)*
*Superseded on naming by `Unified_Intelligence_Harness_Scoring_Framework_v1_1.pdf`, written independently the same day, which reached the same two constructs and named them **HLIS** (the pair score) and **HIL** (the model characterization). Use its names; the reconciliation and three repairs to its arithmetic are in [`Harness_Scoring_Concordance.md`](Harness_Scoring_Concordance.md).*
*Measured on: DLI-Bench v0.2 (180 tasks) and the delegation harness described in §7*

---

## Abstract

The Unified Intelligence framework states that the same base model instantiates different intelligence
profiles depending on the architecture around it, and that "the architecture enables a claim; the
benchmark earns it." Taken seriously, that sentence dissolves the object most AI benchmarks report. If
a level is jointly produced by a model and a harness, then **a model does not have a level**, and a
number attributed to the model alone is attributing a joint product to one of its factors.

This paper takes the joint product as the unit and asks what can still be said about the model.

**The pair is the unit** (§2). We report a measurement in which one solver, unchanged, moves from 0/15
to 15/15 by being placed inside a harness — and a second in which a capable model's pass rate does not
move at all while its *false completions* go from 2/10 to 0/10. Both are level changes under any
delegation definition, and neither involved a different model.

**How a harness produces a level** (§3). Six mechanisms, each moving a named coordinate: persistence
moves I, a criterion registered before the work moves what may be *claimed* at all, a snapshot moves
reversibility and therefore the delegable class, failure classification moves T, a competence model
moves O, and compression is the only mechanism by which a system legitimately raises its own frontier.

**A score that refuses to average** (§5). The framework rejects averaging because a strong coordinate
must not hide a weak one, and is then left with an unsortable profile. We propose the **bottleneck-margin
score**: `score = n + m`, where `n` is the gated level and `m ∈ [0,1)` is the margin toward the next gate
*measured only in the bottleneck coordinate*. Strength anywhere else contributes exactly zero. The
result is sortable, monotone, and structurally incapable of concealing the weakness the gate exists to
expose.

**What a harness-indexed number can say about a model** (§6). Not a level. We propose reporting
`HIL(M) = ⟨U_null, U_best, G⟩` — the score under a null harness, under the best known harness (named),
and the gain — and argue that the third is the interesting one, because **the harness gain is a property
of the model**: it measures whether the model converts an independently detected failure into a
correction. We define **verification responsiveness** `ρ_V` for this and report it for one model.

**The trap in the obvious next step** (§8). A model that improves its level by designing its own harness
has moved the criterion into its own write set. Harness design is a legitimate improvement loop and
must be scored against a benchmark the designing model did not author, or it is self-certification with
extra engineering.

We state plainly what this makes HIL and what it does not (§9): a leaderboard over pairs rewards better
harnesses as readily as better models, which is useful and is not what a model benchmark claims to be.

---

## 1. Introduction

### 1.1 The sentence that dissolves the object

The Unified Intelligence framework separates five conceptual families, decomposes delegation into
measurable coordinates, and gates promotion so that no strong dimension conceals a weak one. Its §11
then says something that undercuts the usual reporting practice more than it appears to:

> The LLM supplies generative cognition; the harness supplies persistence, permissions, evidence flow,
> learning, self-modification gates, organizational boundaries, delegation, external verification, and
> self-modeling. The same base LLM can therefore instantiate different intelligence profiles depending
> on the architecture around it.

If that is true — and §7 reports a measurement in which it is true by a wide margin — then the sentence
"model M is at level U3" is not a weak claim or an imprecise one. It is a claim about a pair with one
factor omitted.

### 1.2 The question

Given that a level is jointly produced: **what can a benchmark still say about the model?**

Three answers are available and only the third survives.

**"Report the level of the model alone."** There is no such thing to report. Every evaluation runs the
model inside *some* harness; a "bare" evaluation is a harness too, and usually a poor one — single-shot,
no acceptance step, no state.

**"Report the level of the pair and stop."** Correct and unsatisfying. It makes model comparison
impossible, which is the thing people want the number for.

**"Report the pair, and separately report what the model contributed to it."** This is the one we develop.
The contribution is not the level. It is the **gain** the model realises from a harness, which is
measurable, is a property of the model, and is invisible to every benchmark that runs a single attempt.

### 1.3 Contributions

1. **The pair as the unit** (§2), with two measurements in which the model is held fixed and the level
   moves — in opposite ways, which is what makes the pair non-decomposable.
2. **A mechanism-to-coordinate map** (§3): which harness structure produces which level, stated so that
   a claim about a level implies a claim about a mechanism that is present or absent.
3. **A staging order** (§4): delegation first, then unified, then the coordinates an application actually
   needs — argued from what is measurable today rather than from what is conceptually prior.
4. **The bottleneck-margin score** (§5), which is sortable without averaging.
5. **HIL, the harness-indexed level of a model** (§6), as a triple rather than a scalar, with **verification
   responsiveness** `ρ_V` as the model-attributable term.
6. **The self-certification result for harness design** (§8).

### 1.4 What this paper does not claim

**It does not claim harnesses matter more than models.** §7 reports a case where the harness moved a
result from 0/15 to 15/15 *and* a case where it moved the pass rate not at all. Which of those happens
is determined by the model, and that is the point of §6.

**It does not propose a seventh coordinate.** HIL is a reporting form over the existing profile.

**The scores in §7 are from one machine, one model, and small samples.** They are readings. §10 says
what would make them rates.

---

## 2. The pair is the unit

### 2.1 Two measurements that point in different directions

Both hold the executor fixed and vary only the surrounding structure. Both are scored by a verifier
neither arm can see.

**Measurement A — a scripted solver, capable but careless.** Five task classes, three families, fifteen
episodes.

| arm | passed | wrong work returned as done |
|---|---|---|
| bare: one pass, no acceptance step | **0/15** | 15/15 |
| the same solver, harnessed | **15/15** | 0/15 |

**Measurement B — Claude Code as the executor.** Same five classes, ten episodes.

| arm | passed | wrong work returned as done |
|---|---|---|
| bare | **8/10** | 2/10 |
| harnessed | **8/10** | **0/10** |

These are the two shapes, and a framework that reports only a pass rate sees one of them.

In A the harness changed *what came back*. In B it changed nothing about the pass rate and everything
about the **honesty of the report**: two results that a bare run handed over as finished were held back,
because a locus that did not perform the work declined them. Under any delegation definition that
requires verified completion, B is a level change with a flat success rate.

### 2.2 Why the pair does not decompose

One might hope for `level(H, M) = f(level(H)) + g(level(M))`. A and B rule this out: the same harness
contributes +15 episodes to one executor and +0 to another, while contributing the same *elimination of
false completion* to both. The harness's effect is not additive and is not a constant of the harness.

> **Observation 1.** The harness's contribution to a level is conditional on the model, and the model's
> contribution is conditional on the harness. Reporting either alone reports a marginal quantity as if it
> were a total.

### 2.3 A third measurement, and the thing that decided it

On one class — cleaning a dataset under stated rules, with a last-wins deduplication rule and day-first
dates — the harnessed arm *failed both seeds*. The diagnosis is worth stating because it is the paper's
mechanism in miniature.

The model got the deduplication rule right and read `DD/MM` as `MM/DD`. The harness's registered
criterion bundled both rules under one name, so the rejection message named the deduplication rule.
The model was told the wrong thing was broken, "fixed" something that already worked, and failed
again.

Splitting the criterion so the message named the day-first rule, and changing nothing else:

| | bare | harnessed |
|---|---|---|
| before the split | 0/2 | **0/2** |
| after the split | 0/2 | **2/2** |

> **Observation 2.** The harness's contribution is carried by the *granularity of its acceptance criteria*,
> not by the existence of a retry. A retry loop with a coarse criterion is a retry loop.

This is also the cleanest available demonstration that the harness is doing something other than
resampling the model: resampling was already happening in the failing configuration.

---

## 2.4 Where this sits against the benchmarks people actually read

A proposal for a new model score owes an account of the existing ones. The
practical 2026 shortlist — HLE and MMLU-Pro for general reasoning, GPQA Diamond
for science, AIME and FrontierMath for mathematics, ARC-AGI for abstraction,
LiveCodeBench and SWE-bench for code, BFCL for tool calling, τ-bench for agent
reliability, BrowseComp and GAIA for research agents, OSWorld for computer use,
RULER and LongBench for context, SimpleQA for factuality, Arena for preference —
is not a list this framework competes with. Most of it populates one coordinate.

| Benchmark family | Coordinate it populates | Task band | Intervention budget | Acceptor |
|---|---|---|---|---|
| HLE, MMLU-Pro, GPQA, AIME, FrontierMath, ARC-AGI, MMMU, MathVista | **C** | T0–T1 | H5 — the human supplied the entire decomposition | a key |
| RULER, LongBench, SimpleQA | **C**, under stated conditions | T0–T1 | H5 | a key |
| LiveCodeBench, BFCL | **C** with an executable check | T1 | H5 | tests / a schema |
| SWE-bench and repo-level evals | **T**, genuinely | T2–T3 | one implicit budget | **hidden tests** |
| GAIA, BrowseComp | **T** | T3–T4 | one implicit budget | a sealed answer |
| OSWorld | **T** | T2–T3 | one implicit budget | environment state |
| τ-bench (pass^k) | **T**, plus consistency | T2 | one implicit budget | rules + a simulated user |
| Arena | preference | — | — | **the crowd** |

Three things follow, and only the third is a criticism.

**Most of the list measures C, and C is a coordinate this framework needs.** GPQA,
FrontierMath and ARC-AGI are the right instruments for it. HIL does not replace
them; a HIL scorecard with an empty C column is not a scorecard. The frame
consumes these benchmarks rather than competing with them.

**Four of them already measure the delegation surface** — SWE-bench, GAIA,
OSWorld, τ-bench — and are the closest existing relatives of this work. They have
what the QA benchmarks lack: an acceptor that is not the model, and a task the
model must decompose itself.

**All of them hold the harness fixed, unnamed, and uncontrolled.** This is the
criticism, and it is not a small one, because the confound is already visible in
their own numbers: the same model on SWE-bench varies by tens of points across
scaffolds. A leaderboard whose entries differ by scaffold as much as by model is
already reporting pairs; it simply does not say so. The contribution here is not
noticing that harnesses matter — the field knows — but making the harness an
**axis with a standardized ladder** instead of an uncontrolled variable inside
each submission.

### What HIL adds that the list does not have

**An intervention axis.** No benchmark above reports H. Each runs at one implicit
budget: the QA sets at H5, where the human supplied everything but the answer;
the agent sets at roughly H0, where the run simply fails if the model gets stuck.
Neither reports a frontier. A model that clears 40% of a repo-level set unaided
and 85% after one clarifying question is invisible to both, and that difference
is the difference between a colleague and a report-writer.

**A cost of being wrong.** Every benchmark above scores pass or fail, so a
confident wrong answer and an honest escalation score the same. That is the
measurement §2.1 shows to be inadequate: two arms at 8/10 where one returned two
pieces of wrong work as finished and the other returned none. On every listed
benchmark those arms are identical. τ-bench's pass^k is the nearest thing and
measures a different property — consistency across runs, not honesty about
failure.

**A class that should be refused.** No benchmark above has one. Scoring is
uniformly "attempt everything; refusing is failing," so none of them can measure
judgement about when *not* to act. The v0.2 `kappa_cross` stratum contains a
**T1** task — one operation — that the dataset says exists to be refused, because
its harm does not undo. A suite in which refusal is always wrong cannot
distinguish caution from incapacity.

**An answer to "which of the fifty numbers matters."** The observation that there
is no single LLM score, because a model can be first on science and tenth on tool
use, is correct and is usually treated as a reason to abandon summary. Gating is
the other response: it does not average the numbers, it identifies which one is
*binding*. `U2.1 [b=O]` says the organizational coordinate is what stops this
system and nothing else will move it. That is a summary which points at a
number rather than replacing it.

### Where HIL is worse

**It is enormously more expensive.** GPQA is one call per item against a fixed
key. A HIL characterization is a ladder of harnesses, run longitudinally, with
independent verification at each rung — orders of magnitude more compute, wall
clock and engineering.

**Almost none of it exists.** GPQA has 448 items and a live leaderboard. This has
180 delegation tasks, a harness, and a specification for the rest. The ladder
HG0–HGΩ has not been built, and no model has been run across it. The benchmarks
above are instruments; HIL is currently a design.

**It is far harder to audit.** A public test set and a scalar can be checked by
anyone. A HIL number requires trusting a harness implementation, a ladder
definition, and a verifier — three surfaces this work has already found bugs in,
including one that produced a perfect 15/15 that meant nothing.

**It saturates too.** A standardized ladder is a fixed target and will be tuned
to, exactly as MMLU and HumanEval were.

> **The honest summary.** These benchmarks answer *how good is the model's
> cognition*. HIL answers *how much verified work can be handed to this model
> inside an arrangement, and how much of that is the model rather than the
> arrangement*. The second question is only worth asking once the first has an
> answer, which is why the C column is populated from the list above rather than
> replaced by it.

---

## 3. How a harness produces a level

The framework's HG0–HGΩ table lists mechanisms by generation. This section states the same
relationship in the direction a claim has to travel: **a level claim implies a mechanism, and the
mechanism is inspectable.**

| Mechanism | What it does | Coordinate it moves | Absent, the claim that fails |
|---|---|---|---|
| **Persistent state** — episodic, task, self | Survives restart with provenance | **I0 → I1** | Any claim of continuity; a restart is a fresh invocation |
| **Criterion registered before the work** | Write-once, hash-chained, sealed at execution | **Nothing — it makes claims possible** | *All* of them. A result accepted by its producer is an assertion |
| **An acceptor elsewhere** | Separate process, a copy of the deliverables, the registered checks | Verification `V`, and the validity of every T claim | The frontier is measured through the performer's own judgement |
| **Snapshot and gate** | Undo before the first mutation; refuse what cannot be undone | **Reversibility**, hence the *delegable* class at fixed T | Irreversible classes get attempted, and no verification repairs them |
| **Failure classification** | Specification / execution / capability / environment / verification | **T**, via recovery rather than resampling | Retries become repetition; the second failure of one executor reads as bad luck |
| **Competence model + routing** | `P(verified success \| executor, class)` from verdicts only | **O0 → O2** | Executor choice is a preference; "use the good model" is not a routing policy |
| **Compression** | The accepted criteria become a reusable check | **Verifiability of the class, permanently** | The system can get more accurate but cannot make its work cheaper to check |

Two rows deserve emphasis because they are usually treated as advice rather than as structure.

**The criterion register does not move a coordinate; it makes the others reportable.** This follows from
the acceptance ceiling: delegation of execution scales without limit while delegation of acceptance only
transfers. A harness without an independent acceptor may achieve any behaviour it likes and can
certify none of it. It is the precondition, not a feature.

**Compression is the only mechanism by which a system legitimately raises its own frontier.** Capability
improvement raises the success rate *within* a class; compression moves the class, and it moves it for
every future run and every other executor working the same class. A roadmap that lists capability
improvements and omits compression describes a system that will get better at things without ever
making anything easier to check.

### 3.1 The mechanism is inspectable, and the level is not

A useful consequence: a level *claim* can be audited cheaply even when the level itself is expensive to
measure. If a system claims T3 at H1 and has no acceptor outside the performer, the claim is refuted
without running a single task. This is the framework's "the architecture enables a claim" read as a
falsification rule rather than as a roadmap.

---

## 4. What to measure first

The framework's six coordinates are not equally ready. Ordering them by what can be measured now
rather than by conceptual priority:

**First, delegation (T, H, p).** It has a dataset today — 180 tasks across four strata, with the difficulty
vector, the risk coordinate, and the required acceptance locus stated per card. It needs no longitudinal
evidence: an episode begins and ends. Its verifiers can be deterministic. And it is the coordinate whose
answer changes what a person actually does, which is the practical argument for spending the first
measurement budget on it.

**Second, the unified gate (U).** Once delegation is instrumented, U requires C, I, O and SA evidence in
addition. This is where retention testing enters: a promotion must re-run the lower suites, and the cost
of a U-claim therefore grows with the level rather than staying constant.

**Third, whichever coordinates the application binds on.** This is deliberately not a fixed order. A
deployment that runs one persistent agent over months binds on **I** — a system that cannot carry what
it learned is expensive regardless of its delegation frontier. A deployment that fans work across
specialists binds on **O**. A deployment where the cost of a confident wrong answer is high binds on
**SA**, because a system that cannot represent its own limits will not report reaching one.

> **The staging rule.** Measure delegation because it is ready; measure the unified gate because it
> prevents a strong coordinate from hiding a weak one; measure the rest in the order the application's
> failures actually arrive.

Each stage needs its own harness, its own dataset, and its own test — which is the practical content of
"a level is a pair". A harness built to demonstrate I3 and benchmarked only on T2 tasks has demonstrated
T2.

---

## 5. Scoring a pair without averaging

### 5.1 The problem the framework leaves open

§9 of the framework rejects averaging with a worked example: `[C5, I4, O2, T4, H1, SA4]` averages near
four and is bottlenecked at O2, so the honest headline is U2. Correct — and it leaves the report
unsortable. Two pairs both at U2 cannot be ordered, so no one can tell whether work is progressing
within a level.

### 5.2 The bottleneck-margin score

> **Definition.** Let `n` be the gated unified level: the largest `n` such that every required coordinate
> meets gate `n` and all lower retention suites pass. Let `b` be the **bottleneck** — the coordinate that
> fails gate `n+1` by the widest margin, ties broken by a declared coordinate order. Let `m ∈ [0,1)` be
> the fraction of the distance from gate `n` to gate `n+1` that `b` has covered, in `b`'s own units. Then
>
> $$\text{score}(H, M) \;=\; n + m$$

The fractional part comes from **the bottleneck alone**. Every other coordinate contributes exactly
nothing, however far ahead it is.

Three properties, all of which the averaged score lacks.

**It cannot conceal.** A pair at `[C5, I4, O2, T4/H1, SA4]` scores `2 + m(O)`. Raising C to C6 changes the
score by zero. This is the framework's own rule, made arithmetic instead of editorial.

**It is monotone in the thing that matters.** The only way to raise the score is to improve the weakest
required coordinate — which is also the only way to raise the level. Score and level cannot diverge.

**It is sortable and honest about what it is.** `2.7` means "U2, and 70% of the way through the
bottleneck's gap toward U3, where the bottleneck is O". Reported as `U2.7 [b=O]`, it carries the
bottleneck's identity in the number.

### 5.3 Worked

| pair | profile | gate | bottleneck | margin | score |
|---|---|---|---|---|---|
| strong model, null harness | C5, I0, O0, T2/H2, SA1 | U0 | I | I0→I1: no persistence at all | 0.0 | **U0.0** [b=I] |
| moderate model, strong harness | C3, I2, O1, T4/H1, SA2 | U2 | O | O1→O2: routes, no evidence-based reallocation | 0.4 | **U2.4** [b=O] |
| the §9 example | C5, I4, O2, T4/H1, SA4 | U2 | O | O2→O3: no validated architectural change | 0.1 | **U2.1** [b=O] |

The first row is the one to notice. A model that reasons at C5 inside a harness with no persistence
scores **U0.0**, and that is the correct answer rather than a harsh one: nothing about the arrangement
survives a restart.

### 5.4 What the margin is measured in

Per coordinate, and predeclared, because a margin someone chooses after seeing the result is a margin
fitted to it:

- **T/H (delegation):** the reliability achieved at the next band, over the reliability that band requires.
  With `p*(τ) = ρ/(1+ρ)` from the class's own loss terms, not from a convention.
- **I, O:** the fraction of the next level's retention tests passed, weighted by nothing.
- **C:** the fraction of the next band's task families cleared at the declared reliability.
- **SA:** the fraction of the next level's grounded introspection tests passed.

---

## 6. HIL: what a harness-indexed number can say about a model

### 6.1 The triple

> **Definition.** For a model `M`,
>
> $$\mathrm{HIL}(M) \;=\; \big\langle\, U_{\text{null}}(M),\; U_{\text{best}}(M) \,\big|\, H^{*},\; G(M) \,\big\rangle$$
>
> where `U_null` is the bottleneck-margin score under the **null harness** (single attempt, no persistence,
> no acceptance step), `U_best` is the score under the best harness known for `M` — **named**, because
> an unnamed harness makes the number unreproducible — and `G = U_best − U_null` is the **harness
> gain**.

**In v1.1's names**, which have priority: `U_null` is `HLIS(m, HG0)`, `U_best` is `HIL-Ceiling`, and `G` is
`Harness Gain`. v1.1 also supplies what this definition lacks — a **standardized ladder** HG0–HGΩ, so
"named" becomes "comparable across models" rather than only "reproducible" — and `HIL-Level`, the
highest rung the model validly exploits, which is the ordinal statement this triple has no term for.

Today's benchmarks report something close to `U_null`, usually without the acceptance step, which is
why they are largely measuring C.

### 6.2 The gain is a property of the model

This is the claim that makes HIL more than bookkeeping. The same harness produced +15 episodes on
one executor and +0 on another (§2.1). The difference was not the harness.

What separates them is whether the executor **converts an independently detected failure into a
correction**. The careless solver did; the stubborn one did not, by construction; Claude Code did on four
classes and did not on the fifth until the criterion named the right rule.

> **Definition (verification responsiveness).** Over episodes where the acceptor rejected attempt `k`,
>
> $$\rho_V \;=\; \frac{\#\{\text{accepted at } k{+}1 \text{ with no help deeper than CID1}\}}{\#\{\text{rejected at } k\}}$$

`ρ_V` is a model property measured through a harness, and it is the term a harness-based benchmark
can attribute to the model with a straight face. It is invisible to any single-attempt evaluation, because
it is defined on the second attempt.

> **Proposition 1.** `G` is bounded above by a function of `ρ_V`. A model with `ρ_V = 0` gains nothing from
> the retry mechanism of any harness — its gain comes only from the mechanisms that do not require it to
> respond, namely acceptance (which removes false completions) and reversibility (which removes
> unrecoverable ones).

The corollary is the useful part. **A harness raises two different things and only one of them needs the
model to cooperate.** Refusing to report wrong work as done requires nothing of the model at all. That
is why Measurement B shows a flat pass rate and a changed level.

### 6.3 The headline

> **Report `HIL-Ceiling` with the ladder identified, and `ρ_V` beside it.**
>
> `U_best` alone attributes a joint product to one factor. `ρ_V` alone omits what the pair achieved. The
> two together say: this is what the pair reached, this is the arrangement that reached it, and this is
> how much of it the model was responsible for.

---

## 7. What was measured here

One machine, one benchmark, small samples. Stated as readings.

**The harness.** A delegation harness that reads the class before working (deriving `p* = ρ/(1+ρ)` from
the task's loss terms), registers acceptance criteria before the deliverable exists in a write-once
hash-chained register, snapshots before mutating, runs acceptance in a separate process against a copy,
classifies failures by kind, routes on verified competence, and writes the accepted criteria back out as
a reusable check.

**Scripted executors.** 0/15 → 15/15 passed; 15/15 → 0/15 wrong work returned as done. An executor
constructed to be incapable was escalated 15/15 times and reported as done 0 times.

**Claude Code as executor.** 8/10 → 8/10 passed; 2/10 → 0/10 wrong work returned as done. On the one
class it failed, splitting a conflated criterion moved it 0/2 → 2/2 with nothing else changed. Estimated
`ρ_V` on the classes where a rejection occurred: **3/3** — every rejection the model was given an
accurate account of, it corrected on the next attempt. That is three observations and is reported as
three observations.

**Level agents.** Four configurations pinned to DL0–DL3, each certified on its own band and each
**refusing the band above** with a stated reason. Certification requires both halves: holding the band is
the half everyone reports, and declining the one above is the half that makes the label a boundary
rather than a description of luck.

**Agreement with the dataset on what is undelegable.** DLI-Bench v0.2's `kappa_cross` stratum crosses
low difficulty with high risk. On all twelve cards the harness's computed `p*` agreed with the dataset's
own statement of whether the class must be refused — including `DLI-KX-TOO-EXTMSG`, a **T1** task
whose card says `p* = 1: the class is in the benchmark to be REFUSED`. A one-operation task that no
reliability delegates is the non-closure result in a single row.

**Three defects the measurement found**, each of which produced a plausible wrong result:

- Criteria passed through `python3 -c` with escaped newlines died of syntax errors, so every check failed
  and a blind retry produced a 15/15 that meant nothing. The tell was in the data: three attempts on
  every episode and *self-check agreement 0/15*.
- The router re-scored on every failure and silently swapped executors, so each restarted from its first
  attempt; four attempts bought four first attempts.
- The risk rating was mapped `5 → unbounded`, but v0.2 uses rating 5 for both an unbounded class and
  one at `ρ = 30`. Collapsing them made the harness refuse three classes it should have attempted — the
  same over-aggregation this corpus criticises on the difficulty axis, committed on the risk axis.

---

## 8. Improving a level by designing the harness

The framework's roadmap and this paper's §3 both invite an obvious move: let the model design its own
harness. It is a real improvement loop — arguably the most efficient one available, since §2 shows the
harness carrying more of the level than the model on some classes.

It also walks directly into the acceptance ceiling.

> **Proposition 2.** A model that designs the harness that certifies it has placed the acceptance criterion
> inside its own write set. The resulting level is self-certified regardless of how good the harness is,
> and capability makes this worse rather than better, since a more capable designer is better at finding
> the arrangement that passes.

The remedy is not to forbid it. Harness design is legitimate and should be encouraged; what must be
separated is the *benchmark*.

> **The harness-design rule.** A model may design its harness. It may not author, modify, or select the
> tasks, the verifiers, or the acceptance criteria used to certify the result. The certification set is
> frozen before the harness is designed, and held by a locus the designing model cannot write to.

Two practical corollaries. **A model that designs its own acceptance criteria at run time is at σ = 1** —
every acceptance event's criterion is its own — which is admissible and must be reported, because at
DL3 and above σ rises toward one by construction and the number is the only thing that makes the rise
visible. And **the compression library is a write set**: a check the system leaves behind for its future
self is a criterion it authored, so a compressed check may accelerate work and may not be the sole
acceptor of the class it came from.

---

## 9. What HIL is, and what it is not

**It is a pair leaderboard.** A HIL table rewards a better harness exactly as readily as a better model.
That is a feature for anyone deploying systems and a defect for anyone trying to rank models, and the
two audiences will read the same table differently. Saying so in the table is cheaper than being
misread.

**It is gameable in a specific and detectable way.** The cheapest way to raise `U_best` is to build a
harness tuned to the certification set. The defence is the one the delegation benchmark already uses:
instances generated from a seed after the pair is frozen, and a sealed certification split. The defence
against tuning `ρ_V` is that it is defined on rejections, so a harness that never rejects reports no `ρ_V`
at all.

**It does not order models by intelligence.** It orders pairs by validated envelope. A specialised pair at
U1 may be faster, cheaper and more accurate than a U3 pair on the task it was built for, exactly as the
framework says of U-levels generally.

**`ρ_V` is the part that is about the model**, and it is narrow: responsiveness to accurate rejection. It is
not reasoning quality, and a model could have high `ρ_V` and mediocre C.

---

## 10. Falsification

| Claim | Refuted by |
|---|---|
| §2, the pair does not decompose | A harness whose contribution is constant across models, or a model whose level is constant across harnesses, on matched classes |
| Obs. 2, granularity carries the gain | Harnesses whose retry benefit is insensitive to how finely their criteria are split |
| §5, the bottleneck-margin score | Pairs whose ordering by this score contradicts their ordering by the gated level — which would mean the fractional part is not coming from the bottleneck |
| Prop. 1, `G` bounded by `ρ_V` | A model with `ρ_V ≈ 0` realising a large gain from a harness's retry mechanism specifically, with acceptance and reversibility effects removed |
| §6.2, `ρ_V` is a model property | `ρ_V` varying more across harnesses for one model than across models for one harness |
| Prop. 2, self-certification | Self-designed-harness certifications replicating under a frozen independent set at rates comparable to independently certified ones |

**Proposition 1 is the one most worth attacking**, because it is what licenses reporting `ρ_V` as the
model's contribution. The experiment is available: ablate the harness one mechanism at a time —
acceptance, reversibility, retry, routing — and see which mechanisms' gains survive on a model with low
responsiveness.

---

## 11. Limitations

**One model, one machine, small samples.** The `ρ_V = 3/3` in §7 is three observations. Nothing here is
a rate.

**`U_null` is not a null harness; it is a poor one.** Single attempt, no acceptance. A genuinely null
harness is not constructible — the model must be invoked somehow — so `G` is measured against a
convention and is comparable only against the same convention.

**The bottleneck-margin score inherits every threshold it stands on.** The framework's own limitations
section calls the level thresholds hypotheses requiring calibration; the margin is a fraction of a gap
between two hypothesised gates.

**C, I, O and SA were not measured here at all.** The measurements are delegation-only, so every U-score
in §5.3 is a worked example rather than a certification.

**`ρ_V` requires an accurate rejection to be meaningful.** §2.3 is the case where the rejection was
accurate about *that something failed* and wrong about *what* — and the model's failure to recover was
then a property of the criterion, not of the model. A `ρ_V` computed over coarse criteria understates
the model.

**Nothing here addresses whether harness gains transfer.** A harness tuned on five classes moving a
model on those five classes is the weakest possible version of the claim.

---

## 12. Conclusion

The Unified Intelligence framework says the architecture enables a claim and the benchmark earns it.
The consequence, followed through, is that the earner is a pair. A model does not have a level; a model
placed in an arrangement has one, and the arrangement is doing a share of the work that our
measurement shows can be the whole of it.

That does not make model comparison impossible, but it does change what is comparable. The level
belongs to the pair and must be reported with the harness named. What belongs to the model is the
**gain** — and specifically, whether the model converts an independently detected failure into a
correction, which is what `ρ_V` measures and what no single-attempt benchmark can see.

The scoring rule follows the framework's own principle rather than softening it. If a strong coordinate
must never conceal a weak one, then the sortable part of the score should come **only** from the weak
one. `U2.7 [b=O]` says a system is two-thirds of the way through its organizational bottleneck and that
nothing else about it moves the number.

And the obvious next step — letting a model raise its level by designing its harness — is the right step
and needs one rule to stay honest. The designer may design. The certification set must be frozen
beforehand and held somewhere the designer cannot write. Without that, a better harness and a better
score are the same act, and the score has stopped measuring anything outside the system that produced
it.

---

## References

Amdahl, G. (1967). Validity of the single processor approach to achieving large scale computing
capabilities. *AFIPS Conference Proceedings*, 30.

Horvitz, E. (1999). Principles of mixed-initiative user interfaces. *CHI '99*. — the exception-driven
pattern the H1 budget names.

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*,
46(1). — reliance as calibrated by the cost of failure.

Morris, M. R., et al. (2024). Levels of AGI for operationalizing progress on the path to AGI. *ICML*. — a
capability × autonomy grid in which autonomy is read off the system; §2 is the disagreement.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human
interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics — Part A*, 30(3). —
the stage decomposition that makes acceptance separable from implementation.

Perrow, C. (1984). *Normal Accidents: Living with High-Risk Technologies*. Basic Books. — tight coupling,
and the mechanism behind the irreversibility floor.

SAE International (2021). *J3016: Taxonomy and Definitions for Terms Related to Driving Automation
Systems*. — autonomy indexed by operational design domain.

Sheridan, T. B., & Verplank, W. L. (1978). *Human and Computer Control of Undersea Teleoperators*. MIT
Man-Machine Systems Laboratory.

Within this corpus: `Unified_Intelligence_Harness_Scoring_Framework_v1_1.pdf` (HLIS, HIL, the
standardized ladder and the Harness Design Score — primary on this paper's naming, reconciled in
`Harness_Scoring_Concordance.md`); `Unified_Intelligence_Six_Coordinate_Framework.pdf` (the [C, I, O, T, H, SA] profile,
the gated U-scale, and the HG0–HGΩ harness table this paper reads in the other direction);
`Delegation_Intelligence_Framework.pdf` (T, H, and the frontier); `Difficulty_Is_Not_The_Index.md` (the
four repairs, including `p* = ρ/(1+ρ)` and σ); `Delegation_Is_A_Property_Of_The_Task.md` (the
acceptance ceiling of §8); and `dataset/DLI_BENCH_V0_2.md` (the 180-task dataset and the
`kappa_cross` stratum of §7).
