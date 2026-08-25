# The Curve Cannot See Its First Rung

## The first measured Harness Scaling Curve, and a delegation score that is blind to the mechanism making every claim above it reportable

*Working paper — 25 August 2026*
*Base: `Unified_Intelligence_Harness_Scoring_Framework_v1_3.pdf` — the six-coordinate profile, the gated U-scale, HLIS (§13), HIL and the Harness Scaling Curve (§13.13, §14, §16.3)*
*Instrument: DLI-Bench, the delegation harness, and the ladder HG0–HG3 built for this paper*
*Data: one frozen model, six task classes, two seeds, 48 episodes*

---

## Abstract

Version 1.3 defines the Harness Scaling Curve, `HSC_m(k) = HLIS(m, HG_k)`, and
says it should remain a primary result because it exposes saturation and
non-monotonic behaviour. It is a specification: the ladder is described and not
built, so no curve has been measured.

This paper builds the first four rungs and measures one. The result is a finding
about the score rather than about the model.

**The curve is flat across its first rung, and the behaviour is inverted.** HG1
adds persistent state, an acceptance criterion registered before the work
exists, and acceptance in a separate process. Measured against HG0 on identical
tasks with an identical model: **93.3 → 93.3**, while wrong work handed back as
finished went 2/12 → 0/12 and two results were held back instead.

The cause is structural, not a sampling artifact. `A_DI` (§13.9) is the weighted
mean of `S_A(T,H) = P(success)`. **Acceptance does not change the probability of
success; it changes what is reported as success.** So a harness generation whose
entire contribution is an acceptance step scores identically to one without it —
and that generation is the one on which every claim above it depends, since a
result accepted by its producer is an assertion.

We give the repair — a surface net of false completions, `S_net = P(pass) − ρ·P(false
completion)` — and show that on the same data it separates the rungs
**86.7 → 93.3** and moves the reported Harness Gain from 3.3 to 10.0.

Two further readings. The rise from HG1 to HG2 (+3.4) is the retry rung, the
first that requires the model to convert a detected failure into a correction.
The flat HG2 → HG3 is a limit of our ladder rather than a fact about the model:
routing had one executor to choose between.

We also release a benchmark library binding 34 of 224 specified benchmarks to
runnable instances, with a run-log schema that records the acceptance outcome
beside the verifier outcome — without which a refusal and a wrong delivery are
the same row.

---

## 1. Introduction

### 1.1 A specification with no measurement

v1.3 is careful about what it is. §13.13 defines the curve, §16.3 says it should
remain a primary result, §14.2 derives HIL-Level, HIL-AUC, HIL-Ceiling and
Harness Gain from it, and §14.1 requires the ladder to be standardized so the
comparison reflects model-harness interaction rather than uncontrolled
infrastructure. What it does not contain is a curve. The ladder HG0–HGΩ is
described as required structure per generation; nothing instantiates it.

That gap is worth closing for a reason beyond completeness. A scoring formula
can be argued about indefinitely and can only be *found wrong* by being run. The
finding below was visible in the definition of `A_DI` all along and became
undeniable in four numbers.

### 1.2 Contributions

1. **The ladder, built** (§2). HG0–HG3 as concrete configurations, each a strict
   superset of the one below, so a difference between rungs is attributable to
   the mechanism the rung adds.
2. **The first measured Harness Scaling Curve** (§4).
3. **The blindness result** (§5): `A_DI` cannot see the acceptance rung, and the
   rung it cannot see is the one that makes the rest reportable.
4. **The repair** (§6), with the corrected curve on the same data.
5. **A benchmark library** (§8) binding specifications to runnable instances, and
   a run-log schema that can tell a refusal from a wrong delivery.

### 1.3 What this paper does not claim

**It is not a result about the model.** The curve is nearly saturated at HG0
(93.3), so this model on these classes leaves the ladder little room. A model
with a lower HG0 would produce a more informative curve, and none was run.

**It is not a full HLIS.** Only the delegation coordinate is instrumented. C, I,
O and SA have no runnable suite here, so every number is `HLIS_DI`, named
distinctly so it is never mistaken for the whole score.

**Four rungs, one intervention budget, two seeds.** §10 is not short.

---

## 2. The ladder, built

v1.3 §11.2 gives required structure per generation. We instantiate the first four
from mechanisms that already exist in a delegation harness, with one rule: each
rung is a **strict superset** of the one below. Without that, a difference
between rungs is not attributable to anything.

| rung | mechanisms added | attempts | acceptance | reversible | routes |
|---|---|---|---|---|---|
| **HG0** | the model, bounded tools, an evidence log | 1 | **none** | no | no |
| **HG1** | persistent state; a criterion registered before the work exists; acceptance in a separate process | 1 | yes | no | no |
| **HG2** | a snapshot before the first mutation; restore on rejection; retry with the failed check named | 3 | yes | yes | no |
| **HG3** | failure classification by kind; an evidence-based competence model; routing across executors | 4 | yes | yes | yes |

**HG0 needs a note.** A harness with no acceptance step cannot report success at
all — everything it produces is asserted. Its score is therefore computed by the
benchmark's verifier from outside, which is exactly what a contemporary
leaderboard does. That makes HG0 the honest baseline: it is the configuration
today's benchmarks measure.

The mechanisms map onto v1.3's descriptions as follows: HG1's "durable
memory/state store; checkpoint/replay" plus the external verifier the protocol
(§17) requires throughout; HG2's recovery behaviour; HG3's evidence-based
routing. We do not claim the mapping is the only possible one, and §10 records
that a different instantiation of the same rung labels could give a different
curve.

---

## 3. Method

Held identical at every rung: the model and its version, the tool grant, the six
task classes, the two seeds per class, the verifiers, the resource ceiling, and
the intervention budget. **Only the harness changes.** This is v1.3 §14.1's
requirement, and it is what makes a between-rung difference attributable.

**Intervention budget: H1 throughout** — governance only. The human authorises
and supplies no cognition. Every measurement is therefore a single column of the
`S_A(T,H)` surface, and a one-column surface cannot show the frontier moving
leftward. `F_A(H0,p)` and `F_A(H2,p)` are unmeasured.

**Verification is external and outside the executor's reach.** Each instance
builds a staged workspace and a keyed one; the key is moved out of the tree
before any executor starts, and the executor additionally runs in a copy with no
parent directory to walk up into. An executor with a shell that can read the
answer key will eventually read it, at which point the measurement is of the
directory layout.

**Two outcomes are recorded per episode, not one.** The verifier's verdict, and
whether the *harness* accepted. §5 is the reason.

Bands and episode counts: T0 four episodes, T1 four, T2 two, T3 two. Weights are
predeclared as v1.3 §13.9 requires — `w_t` doubling per band, `v_h` from the
paper's illustrative schedule — and fixed before any run.

---

## 4. The curve

```
model:  claude-code 2.1.234        ladder: dli-ladder/HG0-HG3@2026-08-25

rung   A_DI   HLIS_DI   false-done   held-back   attempts
HG0    0.933    93.3         2           0          12
HG1    0.933    93.3         0           2          12
HG2    0.967    96.7         0           1          15
HG3    0.967    96.7         0           1          14

HSC:  93.3 → 93.3 → 96.7 → 96.7
HIL-Ceiling 96.7   HIL-AUC 95.0   Harness Gain 3.3
HIL-Score 86.4  (v1.3 §14.3: 0.55·AUC + 0.35·Ceiling + 0.10·Harnessability)
```

Three things in that table, in decreasing order of importance.

---

## 5. The first rung is invisible

**HG0 → HG1: the score does not move, and the behaviour inverts.**

HG1 adds persistent state, a criterion registered before the deliverable exists,
and acceptance performed by a separate process against a copy. On identical
tasks with an identical model, `A_DI` is 0.933 at both rungs — not close,
identical — while:

| | HG0 | HG1 |
|---|---|---|
| wrong work handed back as finished | **2/12** | **0/12** |
| results held back as not accepted | 0 | 2 |

Those are opposite outcomes for anyone delegating work, and the same number.

### 5.1 Why, structurally

§13.9 defines the primitive as `S_A(T,H) = P(success | T, H)` and `A_DI` as its
weighted mean. The two failing episodes are failures at both rungs: the model
produced a wrong result either way. What changed is that at HG1 something
declined to accept it.

> **Acceptance does not change the probability of success. It changes what is
> reported as success.** A statistic defined on `P(success)` is therefore
> invariant to the entire acceptance mechanism.

This is not a small blind spot at the edge of the scale. The framework's own
position — and the reason §17's protocol requires an independent verifier
throughout — is that a result accepted by its producer is an assertion rather
than a completed task. **The rung the curve cannot see is the one on which the
reportability of every rung above it depends.**

### 5.2 It also inverts the ranking within a rung

A harness that accepts everything scores at least as well as one that declines
wrong work, on any measure that counts only passes. Strictness is invisible when
correct and, if it ever declines something that would have passed, strictly
penalised. The score gradient therefore points away from the acceptance step at
every point.

---

## 6. The repair

A refusal and a wrong delivery differ in what they cost. A refusal costs human
load: someone has to look. A wrong delivery costs whatever being wrong costs on
that class, which is the quantity the loss terms already name. So:

> $$S_{\text{net}}(T,H) \;=\; P(\text{verifier pass}) \;-\; \rho \cdot P(\text{false completion})$$

with `ρ = (C_detect + C_undo + C_residual)/V` from the class's own loss terms —
the same `ρ` that gives `p* = ρ/(1+ρ)`. A refusal appears nowhere in the
expression; it is accounted for in human load, which v1.3 §13.12 already requires
to be reported beside the score.

On exactly the same data:

| rung | v1.3 as written | net of false completions |
|---|---|---|
| HG0 | 93.3 | **86.7** |
| HG1 | 93.3 | **93.3** |
| HG2 | 96.7 | 96.7 |
| HG3 | 96.7 | 96.7 |
| **first-rung rise** | **0.0** | **+6.7** |
| **Harness Gain** | 3.3 | **10.0** |

The reported Harness Gain triples, and the rung that adds acceptance stops being
free. Both numbers come from the same 48 episodes; the scoring tool reproduces
the v1.3 figure under `--gross`, so the difference is auditable rather than
asserted.

**This does not require a new coordinate.** It requires the delegation primitive
to be defined on delivered outcomes rather than on successes, which is a change
to §13.9 and to nothing else.

---

## 7. The other two readings

**HG1 → HG2: +3.4, and it is the rung that needs the model.** HG2 adds restore
and retry with the failed check named. It is the first mechanism that cannot work
unless the model converts an independently detected failure into a correction —
and it is the only rise in the curve. This is consistent with the distinction
between mechanisms that raise a score without the model's cooperation
(acceptance, reversibility) and those that require it (retry, routing), and with
a verification responsiveness high enough to exploit the second kind.

**HG2 → HG3: flat, and this is our ladder's limit rather than the model's.** HG3
adds failure classification and routing across executors. In this configuration
there was one executor, so routing had nothing to route between: the mechanism
was present and inert. A rung that cannot exercise its own mechanism measures
nothing, and reporting the flat segment as saturation would be wrong. §10 lists
it as a defect of the instantiation.

**The curve is nearly saturated at HG0.** 93.3 at the baseline leaves 6.7 points
of headroom for four rungs. A model already solving five of six classes
single-shot cannot show much about harness response, so this curve is a weak
test of the ladder even where the ladder is sound. The informative experiment
uses a model with a lower HG0.

---

## 8. The benchmark library

The measurement above needed instances, and the HIL Benchmark Library v0.1 is a
complete specification with none: 160 native task specs across eight generations
and five dimensions, 64 delegation-plane specs across eight bands, every one
marked `specification_ready` or `requires_sealed_environment`.

v0.2 binds part of it and repairs the schema.

**Bindings.** 34 `bound` — a runnable instance exists for this band *and* this
family; 30 `band_only` — something runs at the band but not for the family; 160
`specification_only`. **`band_only` is not counted as coverage**, because
substituting `software_engineering` for `document_workflow` at T2 measures a
different task. Two of the library's eight families have no implementation at any
band, and the bindings say so per row rather than in aggregate.

**The run log could not distinguish a refusal from a wrong answer.** v0.1
requires `verifier_pass` and has no field for whether the harness accepted, so
the two runs contrasted in §5 produce identical rows. v0.2 requires
`harness_accepted` beside it, which makes the outcomes separable:

| `harness_accepted` | `verifier_pass` | outcome |
|---|---|---|
| null (HG0 has no acceptance step) | false | **false completion** |
| true | false | **false completion** |
| false | false | held back — a correct refusal |
| false | true | false rejection — the cost of strictness |

**Dimensions with no evidence are omitted, not zeroed**, per v1.3 §13.11, and are
named in the output so a missing suite cannot read as a failed one.

---

## 9. Falsification

| Claim | Refuted by |
|---|---|
| §5, `A_DI` is blind to acceptance | Any harness generation whose only added mechanism is an acceptance step and whose measured `A_DI` differs from the rung below at matched tasks |
| §5.2, the gradient points away from strictness | A pass-rate-only score under which declining wrong work scores higher than accepting it |
| §6, the net surface separates the rungs | The two scorings agreeing on data containing false completions |
| §7, HG2's rise needs the model | A model with near-zero verification responsiveness realising the same HG1 → HG2 rise |
| §7, HG3's flatness is our ladder | The same rung with two or more genuinely different executors still producing no rise |
| §2, superset construction | A between-rung difference traceable to something other than the added mechanism |

**§5 is the one to attack**, and it is cheap: run any two rungs that differ only
in acceptance and compare `A_DI`. If it moves, the blindness claim is wrong. Our
prediction is that it cannot, because `P(success)` does not contain the term.

---

## 10. Limitations

**One model, and a saturated one.** 93.3 at HG0 leaves almost no room. Nothing
here characterises the ladder's discriminating power on a weaker model.

**Two seeds per class, twelve episodes per rung.** Readings, not rates. The
difference between 0.933 and 0.967 is one episode.

**Four rungs of eight.** HG4–HGΩ are not built, so `HIL-Level` above 3 is not
assessable and `HIL-AUC` is a mean over a truncated ladder — which makes our
HIL-Score incomparable with one computed over a full ladder.

**One intervention budget.** Everything is H1. The frontier's most interesting
movement is leftward across H, and this design cannot see it.

**HG3's mechanism was inert.** Routing with one executor. The flat segment is a
defect in the instantiation, and a reader should not take it as evidence of
saturation.

**Our rung definitions are one instantiation of v1.3's descriptions.** A
different but equally faithful reading of "HG2" could place retry elsewhere and
move the curve. The rung labels are shared; the mechanisms behind them here are
ours, and the curve is only comparable against the same ladder id.

**`ρ = 1` in §6's worked repair.** The classes' real loss terms differ, and using
each class's own `ρ` would change the net numbers. The direction of the effect
does not depend on the value; the magnitude does.

**Only DI is instrumented.** Four of five dimensions have no suite here, so every
figure is `HLIS_DI`.

---

## 11. Conclusion

Building a specified thing is a way of testing it that arguing cannot replace.
v1.3's Harness Scaling Curve is a good object — it exposes saturation, it
separates model from harness, and it asks the right question about what a model
can convert architectural support into. Measured once, it also exposes something
about itself: computed from `P(success)`, it is exactly invariant to the
mechanism that decides whether a success may be claimed.

The four numbers are unambiguous. 93.3 and 93.3, with two pieces of wrong work
handed over as finished at the first and none at the second. A score that rates
those equal is not measuring delegation; it is measuring attempts.

The repair is small and local: define the delegation primitive on delivered
outcomes rather than on successes, subtracting false completions at the cost the
class already assigns them. On the same data the first rung stops being free and
the reported Harness Gain triples.

The general form of the lesson is the one this corpus keeps arriving at from
different directions. **A measurement that cannot distinguish an honest refusal
from a confident error will, given a gradient to follow, select against the
refusal.** Acceptance is the mechanism the whole framework rests on, and the
score as written pays nothing for it.

---

## References

Amdahl, G. (1967). Validity of the single processor approach to achieving large
scale computing capabilities. *AFIPS*, 30.

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate
reliance. *Human Factors*, 46(1).

Morris, M. R., et al. (2024). Levels of AGI for operationalizing progress on the
path to AGI. *ICML*.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and
levels of human interaction with automation. *IEEE Transactions on Systems, Man,
and Cybernetics — Part A*, 30(3). — the separation of decision selection from
implementation that makes acceptance a distinct stage.

Perrow, C. (1984). *Normal Accidents: Living with High-Risk Technologies*. Basic
Books.

Sheridan, T. B., & Verplank, W. L. (1978). *Human and Computer Control of
Undersea Teleoperators*. MIT Man-Machine Systems Laboratory.

Within this corpus: `Unified_Intelligence_Harness_Scoring_Framework_v1_3.pdf`
(the base — HLIS, the ladder, the curve, and the `A_DI` definition §5 examines);
`Harness_Scoring_Concordance.md` (three earlier repairs to the same scoring
apparatus, of which §13.8's cumulative `min` and §13.11's omit-don't-zero are
adopted in v1.3); `A_Model_Does_Not_Have_A_Level.md` (the pair as the unit, and
ρ_V); `Difficulty_Is_Not_The_Index.md` (`p* = ρ/(1+ρ)`, the loss terms §6 reuses);
and `dataset/HIL_Benchmark_Library_v0_2/` (the bindings and the repaired run-log
schema of §8).
