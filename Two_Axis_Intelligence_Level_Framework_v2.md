# A Two-Axis Intelligence Level Framework for AI Agents

## Version 2 — Gated Organization Levels, a Bounded Individual Axis, and First Measurements

*Working paper — 22 August 2026*
*Supersedes: `Two_Axis_Intelligence_Level_Framework_AI_Agents.pdf` (Version 1, 22 August 2026)*
*Markdown edition. No LaTeX source or submission package is built.*

---

## Abstract

Version 1 proposed a two-axis taxonomy for agentic AI: an **Individual Intelligence Evolution Scale**
(I0 reactive → I1 persistent → I2 adaptive-learning → I3 self-improving → I4 recursively
self-improving → I5 autonomous-discovery → IΩ open-ended) and an **Organizational Intelligence
Evolution Scale** (O0 → OΩ), with transition tests, anti-inflation evidence rules, and classifications
for contemporary systems. That structure is retained in full. This version corrects one internal
inconsistency, adds a bound the individual axis lacked, supplies referents for two terms the higher
levels presuppose, and reports a first measurement.

Five changes.

- **IΩ was undefined as stated, and is now defined.** §2.4 requires improvement to be measured under
  an *independent, predeclared* evaluation, while IΩ by construction revises the objective the
  evaluation encodes. A predeclared evaluation and a revisable objective cannot both hold. Version 2
  resolves this with a **frozen referee** — versioned criteria, each revision judged against its
  immediate predecessor. Without it, open-ended evolution and undirected drift are observationally
  identical. §3.8.
- **O-levels are gated, not merely ordered.** An organization can satisfy every behavioural
  description of O3 or O4 while proposing, evaluating, and adopting through a single locus, in which
  case its improvement claims are self-certified and its O-number is void. Separation becomes a
  precondition on the scale rather than a design recommendation, and an O-level is reported as a
  pair. §4.8.
- **The individual axis has a physical ceiling, and the two axes are not independent.** Coherence
  requires *R* ≤ *cτ*/2, so there is a largest possible individual at any decision speed. Past it the
  available direction is not a higher I but a higher O. The I-axis terminates and hands off. §3.9.
- **Two presupposed terms get referents.** "The same individual lineage" (§6.3 of Version 1) is
  defined as an unbroken provenance chain — necessarily, since at I3 and above every other candidate
  for identity is itself subject to change. And *reach* is added as a coordinate, because §5.4 and
  §8.2 both require a distinction between what a system may write in itself and in another. §5.5.
- **A first measurement.** Authorization latency *T*<sub>δ</sub> bounds any governed loop's iteration
  rate. Measured on a deployed governed system: **never observed** — its system of record has no
  timestamp for the event. §8.

The empirical section adds one finding that supports Version 1's §6.3 more strongly than that section
claims: four widely-compared coding agents are not merely *unproven* above I1 but **structurally
identical on every coordinate in this framework**, because none of them writes itself.

---

## 1. Introduction

Version 1's diagnosis stands and is restated here without change. Several distinct phenomena are
collapsed into the single word *intelligence*: responding intelligently, remembering across time,
learning persistently from experience, improving the mechanisms that generate cognition, improving the
mechanisms that generate future improvements, and autonomously discovering validated new knowledge.
A parallel ambiguity holds for groups, where running ten agents in parallel is routinely described as
collective intelligence.

The two-axis remedy also stands. What this version addresses is that a taxonomy meant to resist
inflation must first be internally consistent, must bound its own top, and must supply referents for
the terms its upper levels depend on. Three of the five changes below are of that kind — they are
repairs rather than extensions — and the framework is stronger for them being stated as repairs.

### 1.1 What is retained from Version 1

The I-scale and O-scale and their definitions; the four terms that should not be conflated (§2.4); all
six evidence rules (§6); the coexistence argument and cognitive compression (§5.2); bidirectional
upward and downward flows (§5.3); improvement competence as the operational metric for I4 (§3.5); the
transition-test tables (§9); and the system classifications (§7), which Version 2 does not revise
except to add coordinates.

### 1.2 What is new

§3.8 (frozen referee), §3.9 (coherence bound and axis hand-off), §4.8 (separation gate), §5.5 (lineage
and reach), §7.7 (the one-cell finding), §8 (measurement), and Proposition 3 in §4.9. Everything else
is Version 1's.

---

## 2. Scope and Core Concepts

Version 1's §2 is retained. Two of its definitions carry more weight in this version and are restated
with their consequences made explicit.

**Improvement means that a changed system performs better under an independent, predeclared
evaluation. Merely changing is not improving.**

Version 1 states this as a definition. It is derivable, and the derivation determines where the
framework's upper levels break.

> **Proposition 1 (well-posedness).** *Let a system have a set of persistent state it may modify — its
> write set W — a proposal process, and an evaluator V. The predicate "this change was an improvement"
> is well-defined only if V ∉ W and V is not a function of the proposal process. If V ∈ W, the system
> can satisfy any improvement criterion by editing the criterion, and no observation distinguishes
> improvement from redefinition.*

The proof is immediate. Its force is in the corollaries.

**Corollary 1a.** Self-certification is not weak evidence of improvement. It is none. A system that
proposes, evaluates, and adopts through one locus has reported a tautology, *regardless of its
capability*.

**Corollary 1b.** An individual cannot have a well-posed improvement loop over itself alone. Anything
inside its boundary is available to it and therefore inside its write set. **An external evaluator is
a condition of an improvement claim being defined, not a safeguard added to it.** This is the formal
content of Version 1's §5.4 — individual belief is not organizational truth — and it explains why that
principle is not merely prudent.

**Corollary 1c.** Since IΩ has its objective in its write set, Proposition 1 says IΩ as defined in
Version 1 has no well-formed notion of improvement. §3.8 repairs this.

---

## 3. Individual Intelligence Evolution Scale

I0 through I5 are Version 1's, unchanged, and are summarised here only to keep the paper
self-contained. §3.8 and §3.9 are new.

**I0 — Reactive.** Intelligent output from current input; no persistent evolving cognitive state.
I<sub>t+1</sub> ≈ I<sub>t</sub>. Says nothing about one-shot quality.
*Transition to I1: durable state from earlier interactions is recovered and correctly used.*

**I1 — Persistent.** Durable identity, memory, goals, or task state across interactions.
*Transition to I2: matched future performance improves because the agent learned, not because it
replayed stored instructions.*

**I2 — Adaptive learning.** Experience persistently updates knowledge, calibration, strategies, or
skills; the learning machinery Θ is fixed.
*Transition to I3: the agent improves a cognitive mechanism itself and validates it independently.*

**I3 — Self-improving.** Θ<sub>t+1</sub> ≠ Θ<sub>t</sub>: the machinery that interprets future
experience changes, survives into later operation, and passes independent evaluation.
*Transition to I4: the mechanism that generates and evaluates those improvements itself improves.*

**I4 — Recursively self-improving.** The improvement process A<sub>t</sub> → A<sub>t+1</sub> produces
*higher-quality validated* improvements. Evidence requires rising improvement competence
IC = validated downstream gain ÷ proposal and evaluation cost, not rising task score.
*Transition to I5: the individual autonomously expands validated knowledge.*

**I5 — Autonomous discovery.** Identifies significant unknowns, formulates questions and hypotheses,
designs discriminating evidence, and produces externally validated knowledge not contained in its
prior state. Requires representing structured ignorance, not only knowledge.
*Transition to IΩ: discoveries become cognitive tools that expand the individual's own future
discovery space.*

### 3.8 IΩ, repaired

Version 1 defines IΩ by the cycle

> Unknown → Discovery → Knowledge → Reorganization → Cognitive Tool → Better Intelligence → Deeper
> Unknown

and is careful that IΩ is *not* "knows everything" — it is sustained expansion of reachable cognition,
and a mature open-ended intelligence may find more structured unknowns as it grows. Both points are
correct and retained.

The difficulty is that IΩ, uniquely among the levels, revises the objective. §2.4 requires improvement
to be judged under an evaluation that is *predeclared*; an entity that rewrites what counts as better
cannot be judged under a criterion declared before the rewrite, because the rewrite is what is in
question. Version 1 therefore requires of IΩ something its own definition of improvement forbids.

The repair keeps both halves.

> **Definition (frozen referee).** An intelligence whose objective is in its write set retains an
> immutable snapshot ⟨Ω<sub>k</sub>, V<sub>k</sub>⟩, taken before each revision and held outside the
> write set. A revision counts as an improvement iff the revised system, scored on
> V<sub>k</sub>, does at least as well as the unrevised system would have.

Three properties make this the right form rather than a patch.

**It is already the shape of the I5 → IΩ transition test.** Version 1 asks whether new discoveries
enable *previously inaccessible* classes of discovery — a comparison against the prior state. The
frozen referee is that comparison made a standing requirement rather than an occasional observation.

**It must ladder, and the ladder is the cost.** Judging every revision against the original
Ω<sub>0</sub> asks forever whether the new system solves the old problem, which ossifies. Judging
against nothing drifts. So referees are versioned and each revision is judged against its immediate
predecessor. This bounds the *rate* of drift and makes it visible; it does not bound its extent, and
whether an extent bound is wanted is a governance question this framework does not answer.

**Without it the level is not achieved but unmeasurable.** An IΩ claim with no retained referee is
indistinguishable from undirected drift by any observation whatsoever. **Version 2 therefore treats a
versioned referee ladder as part of the IΩ criterion**, and adds to Table 2:

> **I5 → IΩ, additional evidence.** A retained, versioned referee record showing each objective
> revision scored against its immediate predecessor, with the comparison available to a party that did
> not perform the revision.

### 3.9 The individual axis has a ceiling, and hands off to the organizational axis

Version 1 treats the two axes as parallel scales that "constrain one another but are not
interchangeable" (§5.1). That is right about interchangeability and understates the relation at the
top, where the axes are joined by a physical fact.

An individual is a system with a single locus of decision — one state from which its actions are
selected. For that state to be *one* state, every part contributing to it must exchange signal with it
within one decision cycle, otherwise the parts act on stale information and there are two states, not
one.

> **Proposition 2 (coherence bound).** *With decision cycle τ and signal velocity v ≤ c, an
> individual's radius satisfies*
> $$R \le \frac{v\tau}{2} \le \frac{c\tau}{2}$$

A cycle of 1 ms permits a radius of 150 km; 1 ns permits 15 cm; 1 ps permits 0.15 mm. Three
consequences bear directly on the scale.

**There is a largest possible individual at every decision speed.** Not a practical limit — an
identity condition. Beyond it the object is a collective.

**The I-axis terminates and hands off to the O-axis.** Past the coherence radius the available
direction of development is not a higher I but a higher O. So (I, O) is **not a free product**: the
upper region of the I-axis is bounded, and growth continues only on the other coordinate. Version 1's
§10.1 — that IΩ is not scalar superintelligence — is correct and can now be stated more strongly:
there is no individual level above which an individual continues to grow as an individual.

**The optimum is interior.** Capacity rises with volume while rate falls with radius, so a
fast-narrow individual and a slow-wide one can both be maximal and neither dominates. This is a
second, independent argument for Version 1's §5.2 coexistence claim, and it is stronger than the
economic one in that it does not depend on cost: **heterogeneity is forced by the shape of the bound,
not only made efficient by compression.**

Two further bounds follow from the same construction and are noted without development. **Aperture**:
what an individual can bring to bear on one decision is bounded by integration completing within τ, so
an individual is limited not by what it knows but by how much can be present at once. **Self-opacity**:
a self-model is part of the system it models, so no individual holds a complete model of itself, and
the best available self-knowledge is a compression that states its own limits.

Biological cognition sits six to eight orders of magnitude below the coherence bound — held there by
neural signal velocities of metres per second rather than *c* — so the headroom for artificial
individuals is enormous while every qualitative bound survives.

---

## 4. Organizational Intelligence Evolution Scale

O0 through O5 and OΩ are Version 1's, unchanged. §4.8 and §4.9 are new.

**O0 — Coordinated.** Routes work among members; no substantial persistent organizational cognition.
**O1 — Persistent.** Durable shared memory, roles, task state, evidence, history.
**O2 — Adaptive.** Collective history persistently changes allocation, specialist selection, knowledge
sharing, or procedure; the organizational learning mechanism is fixed.
**O3 — Self-improving.** Changes and validates its own routing, communication, memory, verification,
or role structures.
**O4 — Recursively self-improving.** Improves the mechanisms by which it discovers, evaluates,
promotes, and disseminates future organizational improvements.
**O5 — Autonomous discovery.** Collectively identifies unknowns and produces externally validated
knowledge, with the organization contributing essential cognitive structure no single member holds.
**OΩ — Open-ended.** Discoveries repeatedly generate new tools and organizational forms that expand
future collective discovery space.

### 4.8 Separation is a gate on the scale, not a recommendation

Version 1 states the governing principle in §5.4 — individual belief is not organizational truth, and
the correct transition is *claim + evidence + independent verification → organizational knowledge* —
and again in §8.2, that cognitive evolution should be separated from authority evolution. Both are
right. Neither constrains the O-scale, and the scale is where the constraint has to live.

Consider an organization that maintains multiple candidate organizational policies, runs controlled
replay and canary evaluations, learns which redesigns generalize, and improves the meta-process that
generates future changes. That is the behavioural description of O4 in full. Now suppose the same
locus proposes the redesigns, judges the evaluations, and adopts the winners. By Corollary 1a every
improvement it reports is self-certified, and the O4 classification describes activity that has
produced no validated organizational knowledge at all.

The behavioural description is therefore not sufficient, and no amount of further behaviour makes it
sufficient.

> **Separation.** An organization satisfies separation iff proposer, evaluator, and promoter are
> distinct loci, and the evaluator's criteria and evidence are outside the proposer's write set.

> **Gating rule.** **O-levels above O1 are conditional on separation.** An organization is reported as
> a pair — behavioural level, and whether separation holds — and an unseparated organization at any
> behavioural level above O1 is recorded as **O1 + unverified claims at level *n***, not as O*n*.

O0 and O1 are exempt because coordination and persistence are observable directly and make no
improvement claim. From O2 upward every level asserts that something got better, and Proposition 1
applies to every such assertion.

This is a strict addition to Version 1 rather than a disagreement with it: the principle is Version
1's own, moved from the design-implications section into the scale, where it can prevent the inflation
§6 exists to prevent.

### 4.9 Organizational intelligence is not monotone in member level

Version 1's §10.2 observes that many highly capable individuals can form a weak organization if they
duplicate work, lose history, or cannot reconcile evidence, citing collective-intelligence research
that group performance is not a simple function of maximum member intelligence [1]. Version 2 states
the strong form, which follows from §4.8.

> **Proposition 3.** *An organization failing separation has no well-posed improvement loop regardless
> of its members' I-levels, while an organization of modest members satisfying separation does.
> Therefore an organization of IΩ individuals without separation of duties is **less** intelligent, in
> the sense this framework measures, than a mixed organization of I1–I3 individuals with it.*

Member level enters that argument nowhere, which is the point. **Member level determines the quality
of proposals; separation determines whether the organization can tell a good proposal from a bad one —
and an organization that cannot does not benefit from better ones.**

**Corollary 3a.** The recurring expectation that sufficiently capable members make process
unnecessary is exactly inverted. Process is what converts capability into a claim anyone can rely on.

**Corollary 3b.** A uniformly maximal organization is degenerate. Since separation requires distinct
loci with distinct write sets, a population of identical maximal individuals each holding every role
fails it. Version 1's §5.2 says all levels *can* coexist and usually should; Proposition 3 says
something sharper — **at any decision the participants must occupy different positions, or the
decision certifies itself.**

---

## 5. The Two-Axis Model, Coexistence, and What the Axes Do Not Carry

§5.1 through §5.4 are Version 1's and are retained: a system is (I<sub>i</sub>, O<sub>j</sub>); ten I1
agents in parallel are O1, not I10; all levels can and should coexist, because expensive discovery
becomes a validated procedure that cheap execution runs at scale; information flows upward from
observation to principle and downward from principle to routine; and individual belief is not
organizational truth.

Two amendments and one addition.

**Amendment to §5.1.** The coordinates are not independent at the top. By Proposition 2 the I-axis
terminates, and past the coherence radius development continues only on O. Report (I, O) as before,
noting that the upper I-range is physically bounded.

**Amendment to §5.2.** Coexistence has three grounds, not one. Version 1 gives cognitive compression,
which is economic. Proposition 2 gives the frontier shape, which is physical. Proposition 3 gives
separation, which is logical — and the third is the one that cannot be traded away, since an
organization that abandons it stops making meaningful claims rather than merely becoming inefficient.

### 5.5 Two terms the higher levels presuppose

**Lineage.** Version 1's §6.3 requires that an I3 change modify "the persistent cognitive mechanism of
the same individual lineage." At I3 and above, mechanism, memory, knowledge, and eventually the
improvement process itself are all subject to change, so no content-based criterion identifies the
lineage. Continuity of behaviour is worst of all: improvement *is* behavioural change, so a
behavioural criterion makes improving and dying indistinguishable.

Version 1 already contains the answer, in §8.3, as a list of questions a self-improving system should
be able to answer: what experience motivated the change, which mechanism changed, which version was
active before and after, what evaluation demonstrated improvement, what regressions occurred, and
whether the old version can be restored. That list is a provenance chain. Version 2 promotes it from
a design recommendation to the identity criterion:

> **Definition (lineage).** Two states belong to the same individual iff connected by an unbroken
> chain of provenance-linked evidence records, each change attributable to an admitted observation, an
> authorized promotion, or a recorded action, with no gap.

Identity so defined is preserved by every legitimate operation and broken by exactly those the
framework already rejects: an unattributed change, an adoption without independent evaluation, a
self-declared verdict, a restore with no record of the restore. Version 1's closing sentence in §8.3 —
that without this lineage self-improvement is indistinguishable from uncontrolled drift — is then not
a warning but a definition.

**Reach.** Version 1's §5.4 and §8.2 both require a distinction the coordinates do not carry: between
what a system may change in *itself* and what it may change in *another*. Without it, the entity that
verifies another's claim cannot be described, and it is precisely the entity the framework depends on.

> **Definition (reach).** A system's reach is the pair (W<sub>self</sub>, W<sub>other</sub>). Legitimate
> other-reach is bounded to another system's **inputs** — tasks, candidates, evaluations, verdicts —
> and never to its persistent cognitive state.

Two consequences. **An empty self-write set is what qualifies a system to hold authority over
another's promotion**, since such a system cannot be improving itself by the verdicts it issues; the
verifier role in §5.4's transition is therefore occupied by a *low* I-level entity, which is not a
deficiency of that entity but its qualification. And an authority ceiling — what a system is
*permitted* to do — should be reported alongside (I, O), because §8.2's principle that intelligence
must not automatically widen authority is unstatable if permission has no coordinate.

---

## 6. Evidence Rules

All six of Version 1's rules are retained without amendment: persistence is not learning; learning is
not self-improvement; code editing is not automatically self-improvement; parallel agents are not an
adaptive organization; novel hypotheses are not autonomous discovery; and recursive self-improvement
requires meta-level improvement evidence.

Two rules are added, following §3.8 and §4.8.

**6.7 — An objective-open claim requires a retained referee.** An IΩ claim without a versioned record
of objective revisions scored against their predecessors is not weakly supported; it is
unfalsifiable, because no observation separates open-ended development from drift.

**6.8 — An organizational level above O1 requires separation.** Behavioural evidence of adaptation,
redesign, or meta-redesign establishes the *activity* of that level. It establishes the *level* only
if proposer, evaluator, and promoter were distinct. Absent that, report O1 plus unverified claims.

---

## 7. Positioning Contemporary Agent Systems (August 2026)

Version 1's §7 classifications are retained: stateless call I0; Claude Code I1 / O0–O1; OpenAI Codex
I1 / O1; OpenClaw I1 / O0 basic, I1–I2 with active memory and promotion; Grok chat I1; Grok Bot I2 /
O1+; SARSI/BrainRSI developmental with I3 and I4 as targets; AI4Science a mixed-level O1–O2 substrate
with O4–O5 as long-term ambition and research agents at I4 target, I5 only on demonstrated discovery.

Version 2 adds coordinates and one finding.

### 7.7 The one-cell finding

Version 1's §6.3 argues that code editing is not automatically self-improvement, and that using an AI
to help build its successor is evidence of AI-assisted development rather than of a deployed I3
agent. An independent structural analysis of the same systems supports the rule more strongly than
§6.3 claims.

Adding the reach coordinate of §5.5 to the coding agents gives:

| System | I | O | W<sub>self</sub> | W<sub>other</sub> |
|---|---|---|---|---|
| Claude Code | I1 | O0–O1 | memory only | subagent inputs |
| OpenAI Codex | I1 | O1 | memory only | task inputs |
| OpenClaw (basic) | I1 | O0 | memory only | — |
| Grok chat | I1 | O0–O1 | memory only | — |

These systems are not merely *unproven* above I1. On every coordinate this framework carries — level,
reach, ceiling, separation — they are **the same system**. The reason is uniform and follows from
§6.3: each modifies external software, which is reach into the world, while its own persistent
cognitive state is a memory store it does not evaluate.

> Software an agent writes is not that agent's cognitive mechanism unless the agent subsequently runs
> on it.

What distinguishes these products in practice — patch quality, context handling, tool protocols,
long-horizon reliability — is *capability*, which §2.1 correctly excludes from level. The distinction
that would move any of them to I2 is Version 1's own I1→I2 test: matched future performance improving
because the agent learned. **None of them publishes that measurement**, and the framework's answer is
that they are I1 until one does.

We regard this as the strongest available support for §6.3 and for the framework generally: a
taxonomy that collapses four heavily-differentiated products into one cell, on the ground that the
differentiation is on an axis it declines to measure, is doing the work a taxonomy is for.

---

## 8. Measurement

Version 1's §8.4 correctly observes that evolution levels require longitudinal experiments rather than
fixed-model benchmarks. Two quantities make that concrete.

**Improvement competence** IC, from §3.5, is the I4 measure: validated downstream gain per unit of
proposal and evaluation cost. Its denominator matters — an improvement process that doubles gains
while quadrupling evaluation cost has got worse — and no current system reports it.

**Authorization latency** *T*<sub>δ</sub> is the organizational measure. In any governed loop, once
the automated steps are cheap the iteration rate is bounded by the steps that are not:
ρ<sub>max</sub> = 1/*T*<sub>δ</sub>, where *T*<sub>δ</sub> is the interval between a candidate being
available and its promotion being authorized. Under §4.8 every organization above O1 has such an
interval by construction, since separation requires the promoter to be distinct from the proposer.

### 8.1 First measurement

We measured *T*<sub>δ</sub> on a deployed governed system with owner-signed promotion, from its
hash-chained audit log, pairing candidate registration with promotion. The instrument keeps censored
observations — a candidate registered and never promoted is a lower bound, not an absence — and
excludes intervals below a plausible review floor from the estimate rather than averaging them in.

The result is that **T<sub>δ</sub> has never been observed.** Of three available data points, two are
promotions authorized 5.5 and 0.0 seconds after registration — intervals in which no review occurred,
so they measure a script rather than an authorization — and one is a candidate outstanding for 24
days. If the third is representative, ρ<sub>max</sub> is of order fifteen iterations per year.

Two structural findings accompany it, and they generalize beyond the system measured.

**The system of record cannot represent the quantity.** Its promotions table stores kind, name,
version, and metadata, with no timestamp. Every timestamp used came from a side record. A quantity
that bounds the loop's rate was not recorded by the table that records the event.

**Sub-review intervals are a separation failure, not a fast organization.** An interval too short for
review indicates the authorization was produced by the process that proposed. Under §4.8 this is
exactly the condition that voids an O-level, so **T<sub>δ</sub> is simultaneously a rate measurement
and a separation test** — a near-zero *T*<sub>δ</sub> is not good news, and a framework that read it
as good news would reward the failure it exists to detect.

We note the general lesson: the two measurements this framework most needs are both currently
unreported, and one is unreportable from the system that should hold it. Anti-inflation rules are
necessary but not sufficient; the events have to be recorded.

---

## 9. Falsifiable Transition Benchmarks

Version 1's Tables 2 and 3 are retained. Two rows are amended and one is added.

**Table 2 amendment (I5 → IΩ).** Add: a retained, versioned referee record showing each objective
revision scored against its immediate predecessor, available to a party that did not perform the
revision.

**Table 3 amendment (all transitions above O1).** Add to each: proposer, evaluator, and promoter were
distinct loci, and the evaluator's criteria lay outside the proposer's write set.

**New falsification targets** for the propositions added in this version:

| Claim | Refuted by |
|---|---|
| Proposition 1 | A system with its evaluator inside its write set producing improvement claims that replicate under external evaluation, at rates comparable to separated systems |
| Proposition 3 | Unseparated organizations reliably matching separated ones on held-out outcomes, controlling for member level |
| §4.8 gating | An unseparated organization demonstrating validated organizational improvement — which by Proposition 1 should be unobtainable |
| §3.9 hand-off | A demonstrated single decision locus whose radius exceeds *cτ*/2 for its actual cycle |
| §7.7 one-cell | Any of the listed systems publishing an I1→I2 measurement |

Proposition 2 is arithmetic given its premises and is not falsifiable as such; what is falsifiable is
its premise, that a single decision locus requires signal exchange within one cycle. A system with a
genuinely stale-tolerant unified state would refute the framing, and we are not aware of a coherent
construction.

---

## 10. Discussion

Version 1's §10.1–§10.4 are retained: IΩ is not scalar superintelligence; organizational intelligence
may outpace individual intelligence; coexistence is a feature rather than a transitional artifact; and
terminology inflation is the field's characteristic failure.

Two additions.

**10.5 — The framework's two halves are not symmetric.** Version 1 presents I and O as parallel
scales. Three results in this version break the symmetry in the same direction. The I-axis is
physically bounded and the O-axis is not (§3.9). An individual cannot verify itself, so the O-axis is
a precondition for the upper I-axis rather than a parallel to it (Corollary 1b). And an organization's
level is gated on a property no individual possesses (§4.8). **Organization is the more fundamental
coordinate**, which inverts the intuition that organizations are what you get by adding individuals
up.

**10.6 — The upper levels are currently unreachable for reasons of record-keeping, not capability.**
§8 finds that the two quantities gating I4 and O2+ are unmeasured, and one is unrecordable in the
system that should hold it. On present evidence, no system can be promoted above I2 or O1 — not
because none is capable enough, but because none produces the evidence its own architecture would need
to. That is a more tractable obstacle than a capability gap, and a more embarrassing one.

---

## 11. Limitations

Version 1's five limitations are retained in full: the framework is conceptual and unvalidated as a
measure; product classifications rely on public documentation and configuration can move a system
between levels; the I1/I2 boundary is difficult when memory systems auto-promote; I5 and IΩ demand
strong and domain-specific epistemic standards; and organizational intelligence is not necessarily
beneficial, since an adaptive organization can coordinate toward poor goals.

Four are added for this version.

**11.6 — Separation is treated as binary.** Real organizations separate partially: an evaluator
reporting to the promoter, a proposer selecting the evidence. §4.8's gate admits no degrees, and a
graded form is needed and not offered.

**11.7 — The referee ladder bounds drift rate, not extent.** A chain of pairwise-non-regressing
revisions can arrive arbitrarily far from the original objective. §3.8 makes drift visible and
rate-limited; whether an extent bound is wanted is a governance question outside this framework.

**11.8 — Aperture's growth rate is unknown.** §3.9's aperture bound requires integration cost to grow
superlinearly in the number of items integrated and uses no particular rate. A near-linear rate would
move the bound far without removing it.

**11.9 — The measurement is a single system and a single reading.** §8.1 is one audit log on one host.
It establishes that the quantity is unrecorded there; it establishes nothing about the field. And one
reading is not a measurement — the questions this framework asks of *T*<sub>δ</sub> concern whether it
falls, which requires a series.

---

## 12. Conclusion

Version 1 proposed that intelligence levels be assigned according to what a system can persistently
and validly change, rather than according to labels or raw task performance, and gave two scales, six
anti-inflation rules, and falsifiable transition tests. That structure is retained entirely.

This version repairs three things internal to it. IΩ required a predeclared evaluation of a system
that revises what the evaluation encodes, and is now defined against a versioned frozen referee. The
O-scale ranked organizational behaviour without requiring that the behaviour produce valid claims, and
is now gated on separation. And two terms the upper levels depend on — the lineage that makes a
changed system the same individual, and the reach that distinguishes writing oneself from writing
another — now have referents, the first drawn from Version 1's own §8.3.

It adds a ceiling. Coherence bounds an individual at *R* ≤ *cτ*/2, so the I-axis terminates and hands
off to the O-axis, and the two coordinates are not a free product. Together with the requirement that
an individual cannot verify itself, this makes organization the more fundamental of the two — the
opposite of the natural reading.

And it adds a measurement, whose result is the most useful thing in the paper. The quantity that
bounds every governed loop's rate has never been observed on the system we examined, and cannot be:
its system of record has no field for it. **The framework's upper levels are unreachable today for
reasons of evidence rather than capability.** Anti-inflation rules tell us what would count. They do
not make anyone record it, and until someone does, every claim above I2 or O1 remains a target rather
than a level.

---

## References

Version 1's reference list [1]–[20] is carried forward: collective-intelligence findings and their
critique (Woolley et al. 2010; Credé & Howardson 2017; Woolley et al. 2023); the lifelong-agent
roadmap (Zheng et al. 2025); Gödel machines (Schmidhuber 2006); the Darwin Gödel Machine (Zhang et al.
2025); Hyperagents (Zhang et al. 2026); the BrainRSI working paper (Yang 2026); and vendor
documentation for Claude Code, Codex and its system card, OpenClaw's memory architecture, Grok and
Grok Bot, together with the internal BrainRSI implementation plan and AI4Science specification.

Additional works bearing on the material new to this version:

Amdahl, G. (1967). Validity of the single processor approach to achieving large scale computing
capabilities. *AFIPS*. — the form of the ρ<sub>max</sub> = 1/*T*<sub>δ</sub> argument in §8.

Ashby, W. R. (1956). *An Introduction to Cybernetics*. — requisite variety, underlying §4's coverage.

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*; Dehaene & Changeux (2011), *Neuron* 70(2).
— the single-workspace construct used in §3.9.

Conant, R. C., & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system.
*Int. J. Systems Science* 1(2). — the ancestor of §3.9's self-opacity bound.

Lloyd, S. (2000). Ultimate physical limits to computation. *Nature* 406; Margolus & Levitin (1998),
*Physica D* 120. — the operation-rate magnitudes referenced in §3.9.

Morris, M. R., et al. (2024). Levels of AGI for operationalizing progress on the path to AGI. *ICML*.
— the closest published level taxonomy, and the prior separation of autonomy from capability.

Sheridan, T. B., & Verplank, W. L. (1978). *Human and Computer Control of Undersea Teleoperators*;
SAE International (2021), *J3016*. — the levels-of-automation tradition this framework departs from.
