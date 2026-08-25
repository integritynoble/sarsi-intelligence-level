# Concordance: Harness Scoring

## Two documents reached the same construct within a day. This makes v1.1 primary on naming, and supplies three repairs to its arithmetic

*Working note — 25 August 2026*
*Primary: `Unified_Intelligence_Harness_Scoring_Framework_v1_1.pdf` (§11.1, §12, §13, §14 — the pair as experimental unit, the three-stage strategy, HLIS, and HIL)*
*Reconciled: `A_Model_Does_Not_Have_A_Level.md`, written the same day and before v1.1 was available*

---

## 0. What happened

Two documents were written independently within a day of each other, from opposite ends. v1.1 extends
the six-coordinate framework downward into scoring. `A_Model_Does_Not_Have_A_Level.md` started from a
measurement — one solver going 0/15 to 15/15 by being placed in a harness — and worked upward to what
a benchmark can then say about the model.

They converged on the same construct, including the name. Both define a score for one frozen
(model, harness) pair and a separate characterization of a base model across a ladder of harnesses.
Both call the second one HIL.

**v1.1 is primary on naming and on apparatus.** It has HLIS, HIL-Level, HIL-AUC, HIL-Ceiling, Harness
Gain, Harness Design Score, the standardized ladder requirement, and the scorecard table. The other
paper should adopt those names, and the corrections it owes are listed in §4.

What follows is what the two agree on, three places the scoring arithmetic does not do what v1.1's own
design requirements ask of it, and one measurement that is missing from both.

---

## 1. Nine agreements, reached separately

| | Both hold |
|---|---|
| 1 | **The pair is the basic experimental unit.** v1.1 §11.1; the other paper's §2. Neither factor has a level on its own. |
| 2 | **Delegation first, unified second, application panels third.** v1.1 §12; §4 there. Same order, same reason: delegation is measurable now and needs no longitudinal evidence. |
| 3 | **A mechanism does not earn a level; a dataset does.** v1.1's dataset-coupling requirement and §12.4; §3.1 there. |
| 4 | **A model can climb by designing its harness**, and that ability is separately scorable. v1.1 §11.3 and HDS; §8 there. |
| 5 | **Harness gain is worth reporting on its own.** v1.1 §14.2; `G` there. |
| 6 | **The ladder must be standardized** or the comparison measures infrastructure. v1.1 §14.1. The other paper says the harness must be *named*, which is the weaker form of the same requirement. |
| 7 | **Cost, latency and safety are reported beside the score, not folded into it.** v1.1 §13.1; §9 there. |
| 8 | **The frontier is always reported beside any scalar** so the T/H tradeoff is never hidden. v1.1 §13.2. |
| 9 | **A high score is a broader validated envelope, not a universal performance ordering.** Both, explicitly. |

Independent convergence on nine points is worth more than either document's internal argument for any
of them. The disagreements below are narrow by comparison, and all three are arithmetic rather than
conceptual.

---

## 2. Three repairs

### 2.1 The weighted geometric mean still conceals, and it is undefined at zero

v1.1 §13.1 chooses the geometric mean over the arithmetic one **because "a very weak dimension cannot
be completely hidden by an exceptional one."** That is the right requirement — it is design requirement
*bottleneck sensitivity* from §2 — and the geometric mean satisfies a weaker version of it than the
sentence claims.

Run v1.1's own §9 example, `[C5, I4, O2, T4/H1, SA4]`, gated at U2 with bottleneck O2, coordinates
normalized as fractions of their declared scales:

| change | HLIS | bottleneck |
|---|---|---|
| as written | 65.9 | O2 |
| raise C5 → C6 | 68.4 (**+2.4**) | still O2 |
| raise I4 → I5 | 68.9 (**+3.0**) | still O2 |
| raise SA4 → SA6 | 71.5 (**+5.6**) | still O2 |

The score moves 5.6 points on a coordinate that was already three levels past the bottleneck, while the
thing blocking promotion does not move at all. "Cannot be *completely* hidden" is true; the framework's
requirement is that a strong dimension must not *conceal* a weakness, and a 5.6-point rise on a system
whose certified level is unchanged is concealment at a smaller coefficient.

There is also a boundary problem. `A_d = 0` makes the product zero and the logarithm undefined, so a
singleton agent — legitimately `O0`, because it is not an organization — has no HLIS at all rather than a
low one. v1.1 §10 is careful to say organizational intelligence should not cap an individual; §13.1's
formula caps it at zero.

**Repair.** Keep HLIS as the continuous pair score and let its fractional part come **only from the
bottleneck**:

> `HLIS = 100 × (n + m) / n_max`, where `n` is the gated unified level, and `m ∈ [0,1)` is the fraction of
> the distance from gate `n` to gate `n+1` covered **by the bottleneck coordinate alone**, in that
> coordinate's own units.

Every non-bottleneck coordinate contributes exactly zero. On the example above, raising C, I or SA moves
the score by 0.000 and the report reads `U2.1 [b=O]`. This is v1.1 §9 made arithmetic rather than
editorial, and it removes the zero-boundary problem: a coordinate that is not required for the current
gate cannot zero the score.

The cost is real and should be stated: a bottleneck-only score discards information about how far ahead
the other coordinates are. That information belongs in the profile, which v1.1 already requires to be
published beside the scalar.

### 2.2 The composite HIL-Score re-averages what the pair score just refused to average

§14.3 proposes `HIL-Score = 0.55 × HIL-AUC + 0.35 × HIL-Ceiling + 0.10 × Harnessability`.

This is an arithmetic mean of three terms, one level up. Whatever argument rejects the arithmetic mean
at the pair level applies here: a weak component is fully compensable by a strong one, and at these
weights a model with no harnessability at all loses at most 10 points for it.

Worse, **AUC and Ceiling are computed from the same series** — Ceiling is the maximum of the values AUC
averages — so their correlation is structural, not empirical, and `0.55 + 0.35 = 0.90` of the weight sits
on two views of one quantity. The single term that is not derivable from the others, Harnessability,
carries `0.10`.

### 2.3 HIL-AUC measures "works in weak harnesses", which is not harnessability

Two models on a five-rung standardized ladder:

| model | HLIS at HG0…HG4 | AUC | Ceiling | Harnessability | composite |
|---|---|---|---|---|---|
| flat | 55, 55, 55, 55, 55 | **55.0** | 55 | 0 | 49.5 |
| steep | 20, 35, 55, 75, 92 | **55.4** | 92 | 72 | 69.9 |

AUC ranks these **essentially equal**. They are not remotely equal for anyone deciding which model to
build a harness around: the steep model converts architectural support into verified intelligence and the
flat one does not, which is precisely the property §14.1 says HIL exists to measure.

The composite does separate them (49.5 against 69.9) — but it does so through Ceiling and
Harnessability, the two terms carrying 0.45 of the weight between them. **The heaviest-weighted term is
the least discriminating one.**

AUC is not useless; it answers "does this model work across harness complexities", which matters when
the deployment harness is not yet chosen. It is a different construct from harness-expressible ability and
should be labelled as one rather than weighted as its main component.

**Repair.** Report HIL as a profile with the shape of its curve, not a blend:

> `HIL(m) = ⟨ HIL-Level, HLIS(m, HG0), HIL-Ceiling, Harness Gain, ladder id ⟩`

The first and last are the ordinal statements, the middle three are the curve's start, top, and rise. Any
weighted composite over these should be published as a secondary, application-specific score with its
weights fixed in advance — exactly the rule v1.1 §13.1 already applies to `alpha_d`.

---

## 3. One measurement neither document has

v1.1's Harness Gain is a *difference of two scores*. It says how much the harnessing was worth and not
why, so it cannot distinguish two models with the same gain arising from different mechanisms — and
those two models should be built around differently.

A harness raises two things, and **only one of them requires the model to cooperate**:

- **Acceptance and reversibility** remove false completions and unrecoverable actions. These work on a
  model that contributes nothing beyond its first attempt. In one measurement a capable model's pass
  rate did not move at all (8/10 both arms) while work handed back as done and wrong went 2/10 → 0/10.
- **Retry, routing and replanning** require the model to convert an independently detected failure into a
  correction. A model that cannot do this gains nothing from them.

> **Verification responsiveness.** Over episodes where the acceptor rejected attempt `k`,
> `ρ_V = #{accepted at k+1 with no help deeper than CID1} / #{rejected at k}`.

`ρ_V` is cheap — it needs one extra attempt on rejected episodes, not a whole ladder — it is defined on
the model's behaviour rather than on a score difference, and it predicts which part of Harness Gain a
model can realise. It is invisible to every single-attempt benchmark, because it is defined on the second
attempt.

It also has a failure mode worth recording, found in measurement: `ρ_V` computed over **coarse criteria
understates the model**. On one class a model failed twice because the rejection named a rule that was
not the one it had broken; splitting that criterion in two, and changing nothing else, moved the class
from 0/2 to 2/2. The rejection has to be accurate about *what* failed, not only *that* something did.

---

## 4. Corrections the other paper owes v1.1

- **Adopt v1.1's names.** HLIS for the pair score, HIL for the model characterization, HIL-Level /
  HIL-Ceiling / Harness Gain / HDS for its parts. The other paper's `⟨U_null, U_best, G⟩` is v1.1's
  `⟨HLIS(m,HG0), HIL-Ceiling, Harness Gain⟩` with worse names and no ladder.
- **"Name the harness" is too weak.** v1.1 §14.1 requires a *standardized ladder* with standardized
  tools, resource ceilings, authority and hidden benchmarks. Naming the harness makes a result
  reproducible; standardizing the ladder makes results comparable across models, which is the whole
  purpose.
- **HDS is the better treatment of harness design.** The other paper's §8 gives the rule that keeps
  harness design from becoming self-certification, which v1.1 should adopt; but v1.1 additionally makes
  the ability *scorable*, which is the more useful move.
- **The scorecard in §14.4 is the right output format**, and better than anything in the other paper: it
  names, for each score, the subject being measured. Most disputes about AI benchmark numbers are
  disputes about that column.

---

## 5. What is settled and what is not

**Settled between the two documents.** The pair is the unit; delegation is measured first; a level needs a
dataset and not just a mechanism; harness gain is reportable; harness design is a scorable ability that
must be certified against a frozen external set; the frontier is reported beside any scalar.

**Not settled.** Whether the fractional part of a pair score should come from the bottleneck alone (§2.1)
or from a weighted geometric mean; whether AUC belongs in a composite at all (§2.3); and whether
`ρ_V` earns a place on the scorecard or stays a diagnostic.

**Not measured by either.** Every number in both documents outside the delegation coordinate is an
illustration. C, I, O and SA have no instrument here yet, the ladder HG0–HGΩ has not been built, and no
model has been run across it. Until it is, HIL is a specification.
