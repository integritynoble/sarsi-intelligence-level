# Substrate Indexing Is an Axis Shift

## How individual and organizational intelligence levels operate inside each recursive self-improvement loop

*Working paper — 23 August 2026*
*Builds on: `SARSI-L_Paper_v3.md` (Circles I–V+); `Two_Axis_Intelligence_Level_Framework_v2.md` (I0–IΩ, O0–OΩ)*

---

## Abstract

Two frameworks describe recursive self-improvement from different starting points. One indexes it by
**substrate** — software, hardware, matter, biology, stellar energy — and argues that the binding
constraint migrates outward from one domain to the next, so that "the" recursion rate is not a single
parameter. The other indexes it by **who changes what** — an individual's write depth and an
organization's coordination depth — and argues that a level is a pair rather than a rung. Neither has
been crossed with the other, and the crossing supplies something the first framework asserts without
mechanism: *why* substrate is the right index.

The bridge is the improvement loop both frameworks share: identify, implement, validate, deploy. We
assign each step to an axis and obtain a result that holds in every domain: **validate is
organizational by necessity and deploy is organizational always**, because an individual that
authorizes its own deployment has self-certified. Two of four steps of every loop, in every circle,
are organizational by construction, and no individual level closes any loop alone.

From this follows the paper's central claim. Reading the five substrate closure criteria against the
level definitions, **the individual requirement saturates while the organizational requirement keeps
climbing**. Chip specification, machine design, and collector design are ordinary engineering
cognition; what is hard about the outer domains is everything after the identify step. Substrate
indexing is therefore an axis shift, and the intelligence-explosion argument — a claim about a
machine improving its own cognition — is an argument about one domain only.

Two asymmetries appear at the top. Checked against the criteria as stated, **no domain's closure
criterion requires open-ended individual intelligence**; and the outermost domain **admits no
individual coordinate at all**, since a structure spanning an astronomical unit exceeds the coherence
bound by eight orders of magnitude. The individual axis has a ceiling that lies below the trajectory's
requirements; the organizational axis carries the outer domains alone.

**This paper is a companion to a crosswalk developed in parallel** (*Intelligence Inside the
Circles*, 2026), which maps what each individual and organizational level *does* inside each substrate
domain — per-domain role tables for both scales, both complete matrices, a seven-role heterogeneous
loop, and a unified state profile. We take that as the descriptive account and do not duplicate it.
This paper supplies what a crosswalk does not: five propositions about the structure the crosswalk
describes, and one measurement.

The crossing also explains four things the substrate framework observes without accounting for: why
its design-to-deploy gap appears in every domain, why its own timeline errors were monotonic in
distance from software, what a compensated half-loop is in structural terms, and how to weight loop
completion in a way that distinguishes two systems with the same score.

---

## 1. Introduction

### 1.1 The question

The standard argument for an intelligence explosion is about a single mind: a machine that improves
its own capacity to improve will outgrow one that does not. The argument is sound and its conclusion
is probably right. What it does not supply, and what restating it has never supplied, is the rate.

One line of response indexes the rate by substrate. An improvement loop is always a loop over some
substrate a system can modify; loop periods across substrate domains differ by five orders of
magnitude; and the binding constraint migrates outward as each domain is mastered. This is correct as
far as it goes, and it leaves a question open: *why* does substrate govern, rather than some other
partition of improvement capability? The answer given is that substrate domains differ in period,
access, and floor type. Those are properties of the domains. They are not a mechanism.

This paper supplies one. The mechanism is that the outer domains do not merely take longer — **they
shift the work from one kind of intelligence to another**, and the kind they shift toward is the one
the intelligence-explosion argument says nothing about.

### 1.2 What is missing from each framework alone

The substrate framework has no representation of *who* performs a loop step. Its loop is
⟨identify, implement, validate, deploy⟩ and its closure criterion is that all four execute without
human approval — but "the system" that executes them is unanalysed, and the framework's own
observation that the deploy gate is "institutional rather than technical" is therefore a remark it
cannot cash out.

The level framework has no representation of *what substrate* a loop runs over. Its individual and
organizational scales describe depth of self-modification and depth of coordination, and are silent
about whether the thing being improved is a training run or a fabrication plant.

Crossed, each supplies the other's missing term.

### 1.3 Contributions

1. **A step-to-axis assignment** (§4) with a proposition: validate and deploy are organizational in
   every loop, so no individual level closes any loop alone.
2. **The saturation law** (§5): across substrate domains the individual requirement is bounded while
   the organizational requirement is not, which is the mechanism behind substrate indexing.
3. **Two asymmetries at the top** (§7): no stated closure criterion requires open-ended individual
   intelligence, and the outermost domain admits no individual coordinate.
4. **Four explanations** (§8) of findings the substrate framework reports without accounting for.
5. **A measurement program** (§9), including a first reading of the quantity that binds the
   organizational axis in every domain.

### 1.4 What this paper does not claim

**It is not a timeline.** Nothing here shortens or lengthens any estimate. The claim is about which
kind of capability each domain requires, not when it will arrive.

**It does not predict performance.** Level is not capability, and a system at a low level may be far
more useful than one at a high level.

**Its level assignments are orderings.** Both axes are ordinal, no step-weighting is agreed, and §11
is specific about what this costs.

**It builds on two unpublished working frameworks**, and inherits whatever is wrong with them. Where
a claim depends on a contested premise of either, we say so.

---

## 2. Related work

**The per-domain crosswalk.** The work closest to this one maps every individual and organizational
level to its function inside every substrate domain, via a seven-role loop — director, discoverer,
instrument-maker, specialist, operator, referee, promoter — and reports both complete matrices with a
unified state profile. It is the descriptive account of the same crossing, and this paper depends on
it: §6's per-domain discussion is a compression of material treated there at length. What it does not
contain, and what is offered here, are the propositions of §4, §5, and §7, and the measurement of §9.
The division is deliberate rather than accidental — a crosswalk answers *what happens where*, and the
questions in §1.1 are *why here rather than there*.

**The intelligence-explosion argument.** Good's formulation concerns an ultraintelligent machine
designing better machines. In the vocabulary used here it is a claim about the *individual* axis — a
system raising its own write depth — and §5 argues it therefore applies to exactly one substrate
domain. This is not a refutation. It is a delimitation, and the substrate framework makes the same
delimitation without saying which axis is being delimited.

**Substrate-indexed recursion.** The framework this paper crosses argues that recursion rate is
domain-relative, gives operational closure criteria per domain, derives an Amdahl-style bound showing
that external compensation limits iteration rate rather than per-iteration gain, and distinguishes
throughput floors (removable by closure) from physical floors (not). We adopt all of it and add the
axis decomposition.

**Two-axis level taxonomies.** The framework supplying the level scales indexes an individual by the
deepest layer it changes through experience and a collective by what it changes about its own
coordination, and holds that a level is a pair. Its coherence bound — that a single decision locus
satisfies $R \le c\tau/2$ — does the work in §7.2.

**Forms of superintelligence.** Bostrom distinguishes speed, collective, and quality superintelligence.
The result in §5 bears directly on that distinction: **the path to stellar-scale capability runs
through collective superintelligence and not through quality superintelligence**, because the outer
domains' binding steps are organizational. Bostrom treats the three as alternative routes; the
crossing suggests they are routes to different places.

**Levels of automation and of AGI.** The Sheridan–Verplank tradition and its descendants order human
and machine control allocation on a single ladder, which works where the task is fixed. Recent AGI
level taxonomies separate an autonomy dimension from capability. Both traditions assign a level to a
system; the crossing suggests that for improvement loops the assignment must be to a *step*, since
different steps of one loop sit on different axes.

**Cybernetic antecedents.** Ashby's requisite variety underlies the organizational requirement in §5;
Conant and Ashby's regulator theorem underlies the self-opacity limit invoked in §7.2. Amdahl's bound
transposed from parallel speedup to loop autonomy gives the rate argument in §9.

---

## 3. The two frameworks, in the terms used here

**Substrate domains and loops.** A loop over domain $d$ is
$L_d = \langle \iota, \mu, \nu, \delta \rangle$: identify a candidate modification predicted to
improve a specified capability; implement it; validate it against an evaluation not used in generating
it; deploy it as the operative baseline. $L_d$ is **closed** iff all four execute without human
approval and $\delta$ makes the modification operative. Loop completion $\lambda_d \in [0,1]$ is the
weighted fraction of steps executing autonomously.

The five domains are **I** software (architecture, training process, weights), **II** hardware (chip
design and fabrication), **III** physical (matter, machines, self-replication), **IV** biological
(organisms, disease, aging), **V+** stellar (orbital energy capture at scale).

**Levels.** An individual's level $\mathrm{I}k$ is the deepest layer it changes through experience:
reactive, persistent, adaptive-learning, self-improving (the mechanism changes), recursively
self-improving (the improvement process improves), autonomous-discovery, open-ended. An
organization's level $\mathrm{O}k$ is what it changes about its own coordination: coordinated,
persistent, adaptive, self-improving, recursively self-improving, autonomous-discovery, open-ended.
An individual is a system with a single global workspace; an organization has none.

---

## 4. The step-to-axis assignment

**Identify is individual work.** Generating a candidate modification is cognition. It may be assisted,
distributed, or parallelised, but its content is the production of a hypothesis about what would
improve the system, and that is what an individual level measures.

**Implement is individual in Circle I and increasingly not, outward.** Writing code is cognition
realized; operating a fabrication plant is not.

**Validate is organizational by necessity.** An improvement claim is well-defined only if its
evaluator lies outside the write set of the system being evaluated. Everything inside an individual's
boundary is by definition available to its single decision process, therefore inside its write set.
So validation requires a locus the individual does not control — which is an organizational property,
not an individual one.

**Deploy is organizational always.** This is the strongest of the four and admits no domain exception.

> **Proposition 1.** *Let a system propose a modification, evaluate it, and deploy it as its operative
> baseline. Then the deployment criterion lies inside the write set of the proposer, and the system
> can satisfy any criterion by adjusting it. No observation distinguishes a validated deployment from
> an asserted one. Therefore $\delta$ requires an authorizing locus distinct from the proposer.*

The proof is immediate; the consequence is not.

> **Corollary 1.1.** *In every substrate domain, at least two of the four loop steps are
> organizational by construction. No individual level, however high, closes any loop alone.*

This is why the substrate framework finds the deploy gate "institutional rather than technical" in the
one domain where it examines the question closely. The finding is not a fact about that domain. It is
a fact about $\delta$.

**A qualification that matters.** The assignment is about where *authority* lies, not where compute
runs. A system can execute its own held-out evaluation; what makes $\nu$ organizational is that the
criterion and the data must be external. This distinction does real work in Circle I, where the
execution is cheap and only the authority is contested, and progressively less outward, where the
execution is itself distributed.

---

## 5. The saturation law

Reading the five closure criteria against the level definitions gives the paper's central claim.

| Domain | $\iota$ demands | $\mu, \nu, \delta$ demand | Binding axis | Floor type |
|---|---|---|---|---|
| **I** Software | I3–I4 | O2–O3 | **Organizational** | Throughput |
| **II** Hardware | I2–I3 | O3–O4 $+$ physical | Organizational, then physical | Mixed |
| **III** Physical | I2–I3 | O4–O5 $+$ physical | Physical, via organizational | Physical |
| **IV** Biological | **I5** | O3–O5 $+$ irreducible physical | Physical | Physical |
| **V+** Stellar | I2–I3 | O4$+$ | Organizational; no individual possible | Physical |

*Assignments are orderings by inspection (§11.1).*

> **Proposition 2 (saturation).** *Across the five domains the individual requirement is bounded above
> by the biological domain's identify step and does not increase with domain index; the organizational
> requirement increases monotonically with domain index and is unbounded within the list.*

Three consequences.

**You cannot buy an outer domain with a smarter individual.** The $\iota$ column stops rising after
Circle IV and is *lower* in II, III, and V+ than in I. What is hard about the outer domains is
everything after $\iota$.

**Substrate indexing is an axis shift.** The substrate framework's central claim is that recursion is
substrate-indexed. Proposition 2 says *why*: outer substrates shift the loop's load from the axis on
which cognitive self-improvement operates to the axis on which it does not. Period, access, and floor
type — the framework's three stated reasons substrate is the right index — are consequences of this
shift rather than independent justifications for it.

**The intelligence-explosion argument is a Circle I argument.** Good's machine improving its own
cognition is a transition from self-improving to recursively self-improving on the individual axis.
Every domain outside software has its binding step on the other axis, where that argument has no
purchase. The explosion, if it occurs, occurs in one domain and then meets a bound the argument does
not describe.

---

## 6. Domain by domain

### 6.1 Circle I — Software

**Which levels do what.** Reactive members run evaluations and mechanical pipeline steps. Persistent
members hold session and project state so an experiment survives a restart. Adaptive-learning members
tune policy against a fixed metric. **Self-improving is the level this domain's criterion names** — a
system modifying its own architecture or training process — and recursively self-improving is what
makes the loop recursive rather than merely closed. Organizationally, a persistent organization
retains what was tried and what failed; an adaptive one routes candidates to the right evaluator; a
self-improving one can change its own validation procedure on evidence.

**Where it is stuck, precisely.** Identify, implement, and validate run without approval in mature
systems; deploy does not. The framework's own estimate reports the constraint on deploy as
authorization rather than capability. In level terms: **the software loop has an individual level
roughly adequate to its criterion and an organizational level roughly two steps short.**

**Authority closure is an organizational move.** With a mature loop's gated set containing only
$\delta$, the compensated iteration rate is $\rho_{\max} = 1/T_\delta$ where $T_\delta$ is
authorization latency. Capability improvement drives $\iota, \mu, \nu$ toward zero and cannot touch
$T_\delta$. **Circle I closure is achieved by raising the organizational level, not the individual
one** — which is a strange thing to say about the domain everyone treats as the individual-axis
domain, and is the crossing's most immediately actionable claim.

**Floor: throughput, and therefore removable.** The only domain of which this is true throughout.

### 6.2 Circle II — Hardware

**Where the axes split, and the framework already found the line.** Chip *design* is a software
problem; chip *manufacture* is physical infrastructure. That distinction is reported as the single
most consequential error in the framework's earlier timelines. It is exactly the axis split: design is
$\iota$ and individual, manufacture is $\mu$ and organizational-plus-physical.

**This is where the individual axis stops helping.** A fabrication plant requires contamination
control, process-drift correction at nanometre tolerances, and maintenance — coordination among many
actors over months. A more capable designer does not qualify a fab, and no individual level reaches
the binding step.

**Minimum: I2–I3 / O3–O4.** Self-improving organizationally, because process control must change on
evidence; recursively so, because doing that repeatedly and getting better at it is what fab autonomy
would mean.

### 6.3 Circle III — Physical

**Self-replication is an organizational property.** The criterion is that a machine mine, refine,
fabricate its own control electronics, and assemble a working copy. Every step after design is
distributed in space and time.

**And the copy raises a question only the organizational axis answers.** Is the copy the same system?
Not by content — the copy shares none of the original's matter. The available criterion is lineage:
a successor is legitimate iff connected by an unbroken chain of provenance-linked records. **Under
that criterion self-replication is a lineage event**, and a replicator that does not record its own
replication has not extended a lineage but started an unattributed one.

**The mutual dependency is an organizational ladder.** The framework shows that hardware and physical
domains depend on each other partially rather than fully, so the pair bootstraps rather than
deadlocking, advancing at the slower of the two physical periods. In level terms **both rungs are
organizational work, and no increase in individual level moves the ladder at all.** That is why it
advances at physical speed.

**Floor: physical.** Yields only to parallelism, and the capability supplying parallelism in matter is
this domain — the ladder must be climbed to obtain the tool that would make the ladder fast.

### 6.4 Circle IV — Biological

**The only domain whose identify step requires autonomous discovery.** Its criterion opens with
generating and testing hypotheses about biological mechanisms — identifying significant unknowns,
which is what the autonomous-discovery level names. Every other domain's $\iota$ is design, satisfied
two levels lower.

**Its validate step is externally gated twice over.** Once because validation always requires a
separated evaluator, and once because regulatory structure requires a human principal investigator —
an institutional fact, not a technical one. Its physical floor of five to eight years is compressible
by no level on either axis.

**The irony worth stating.** This domain is off the critical path: it requires software, does not
require physical self-replication, and the stellar domain does not require it. So **the domain that
most demands a high individual level contributes least to the trajectory.** The top of the individual
axis is stranded on a branch.

### 6.5 Circle V+ — Stellar

**No individual is possible here.** A collector swarm at one astronomical unit is roughly 16.6
light-minutes across. A single decision locus of that radius has, by the coherence bound, a decision
cycle of at least 16.6 minutes, while local computation between consecutive opportunities to agree is
enormous. Such a system is not a mind with distributed parts. It is a civilization.

> **Proposition 3.** *Circle V+ admits no individual coordinate. Its level is organizational alone.*

**Minimum: O4 at least.** The net-growth criterion — collection area rising faster than maintenance
and failure losses, sustained — requires an organization that improves how it improves, over decades.
Whether it requires the open-ended organizational level is not entailed by the criterion as written
and we do not claim it; what is entailed is that no fixed organizational form is obviously adequate to
the timescale.

---

## 7. Two asymmetries at the top

### 7.1 No closure criterion requires open-ended individual intelligence

Checking the level requirements against the five criteria, which are the only place closure is
defined:

> **Proposition 4.** *No stated substrate closure criterion requires the open-ended individual level.*

Circle I requires self-improving or recursively self-improving. Circles II, III, and V+ require
design-level cognition for $\iota$. Circle IV requires autonomous discovery. Open-ended individual
intelligence — discoveries becoming cognitive tools that expand one's own future discovery space — is
required by none of the five.

**IΩ is not on the path to Kardashev II.** This does not make it unimportant; it makes it
**non-instrumental**. If open-ended individual intelligence is worth pursuing, it is worth pursuing
for what it is, and not as a step toward stellar-scale capability, because that path does not pass
through it.

### 7.2 The outermost domain is unreachable by any individual

Proposition 3. The organizational axis has no counterpart bound: an organization may span any
distance, because it was never required to hold one coherent state.

Together the two asymmetries give:

> **Corollary 4.1.** *The individual axis has a ceiling that lies below the trajectory's requirements.
> The organizational axis carries the outer domains alone.*

The level framework reaches the same conclusion — that organization is the more fundamental
coordinate — from evaluator externality and the coherence bound. The crossing reaches it from the
substrate criteria, which are an independent starting point. **Two derivations from different premises
is the strongest reason available to believe it.**

---

## 8. What the crossing explains

**The design-to-deploy gap, in every domain.** The substrate framework reports that in every domain
the design component is far above the manufacture or deploy component, and calls the gap
"institutional as often as technical." In level terms every row reads *individual high, organizational
low*, and one diagnosis covers all five domains at once.

**Why the framework's own errors were monotonic in substrate distance.** Its timeline corrections grew
with distance from software, attributed to reasoning about physical domains with software intuitions.
The crossing sharpens this: **distance from software is distance from the individual axis.** An
analysis calibrated on the axis where cognition operates will underestimate in proportion to how much
of a domain is organizational and physical work — which is exactly the reported ordering.

**What a half-loop is, structurally.** A compensated loop is one where some steps are performed by an
external agent. In level terms: **a half-loop is a system whose individual level meets its domain's
requirement and whose organizational level does not.** Compensation is an organization supplying the
organizational work the system cannot. This makes the framework's open compensation-ceiling
question — whether per-iteration returns to compensation diminish — the question of whether the
organizational gap closes as the compensating organization is itself augmented, which is measurable
from authorization timestamps.

**How to weight loop completion.** The framework records that its per-step weights are estimated by
inspection and that two loops with identical completion can differ enormously depending on which steps
were automated. The crossing offers a principled decomposition: weight $\iota$ and $\mu$ by the
individual axis and $\nu$ and $\delta$ by the organizational one, and report completion as a pair.
Two loops with the same scalar and different splits then become distinguishable, which is what the
open problem asks for.

---

## 9. Measurement

**Authorization latency, per domain.** $T_\delta$ is the organizational axis's binding quantity in
every domain, and by the Amdahl-style bound it caps the compensated iteration rate at
$1/T_\delta$. Circle I's $\delta$ is the only one currently instrumentable end to end; the outer
domains' authorization runs through procurement, regulators, and launch authorities, where timestamps
exist but are not collected as a series.

**A first reading.** We measured $T_\delta$ on a deployed governed software system with
cryptographically signed promotion, from its hash-chained audit log, pairing candidate registration
with promotion, retaining censored observations as lower bounds, and excluding intervals below a
plausible review floor.

> $T_\delta$ **has never been observed.** Of three available data points, two are promotions
> authorized 5.5 and 0.0 seconds after registration — intervals in which no review occurred — and one
> is a candidate outstanding for 24 days.

Two findings generalize. The system of record could not represent the quantity: its promotions table
carried no timestamp, so every timestamp used came from a side record. And **a sub-review interval is
not a fast organization but a separation failure** — by Proposition 1 the resulting deployment is not
validated, so $T_\delta$ is simultaneously a rate measurement and a test of whether $\delta$ is
genuinely separated.

**The individual/organizational split of loop completion.** Recompute the completion table with each
step tagged by axis. The prediction is that the organizationally-tagged fraction is near zero in every
domain, which would make the reported design-versus-manufacture columns a special case of a general
rule.

---

## 10. Falsification

| Claim | Refuted by |
|---|---|
| Proposition 1 | A system that proposes, evaluates, and deploys through one locus producing deployments that validate under external evaluation at rates comparable to separated systems |
| Proposition 2 | A domain whose identify step demonstrably requires a higher individual level than the biological domain's |
| Proposition 3 | A demonstrated single decision locus whose radius exceeds $c\tau/2$ for its actual cycle |
| Proposition 4 | Any stated closure criterion shown to require the open-ended individual level; or a sixth substrate domain that does |
| §8 half-loop | A compensated loop whose missing steps are individual rather than organizational |
| §5 axis shift | A domain in which raising the individual level demonstrably advances a binding non-$\iota$ step |

Proposition 3 is arithmetic given its premise. What is falsifiable is the premise — that a single
decision locus requires signal exchange within one cycle — and a system with a genuinely
stale-tolerant unified state would refute the framing. We are not aware of a coherent construction.

---

## 11. Limitations

**11.1 — The level assignments are orderings by inspection.** They inherit the substrate framework's
own measurement problem exactly: no agreed decomposition of each loop into steps, no agreed weighting,
and ordinal scales on both axes. §5's table is an ordering, and two domains assigned the same level may
differ substantially.

**11.2 — The step-to-axis assignment is cleaner in statement than in practice.** Validation in Circle
I is partly individual: a system can run its own held-out evaluation, and what makes $\nu$
organizational is that the criterion and data must be external, not that the computation must be. The
assignment is about authority rather than execution, and that distinction carries less weight in the
outer domains where execution is itself distributed.

**11.3 — Proposition 4 is a claim about the criteria as stated.** The substrate framework's domain
list is conceded by its own authors to be "neither obviously complete nor obviously minimal." If a
sixth domain belongs on it, Proposition 4 must be rechecked against that domain's criterion. The
most-discussed candidate, fault-tolerant quantum computation, would not change the answer, but one
candidate is not a proof.

**11.4 — Circle V+'s organizational requirement is bounded below, not identified.** We argue O4 at
least and decline to claim the open-ended level, because the criterion does not entail it. The
outermost domain's organizational requirement is genuinely open.

**11.5 — The measurement is one system and one reading.** It establishes that the quantity was
unrecorded there and nothing about the field. One reading is not a measurement: the question the
framework asks of $T_\delta$ is whether it *falls*, which requires a series.

**11.6 — Both parent frameworks are unpublished working papers.** Every result here is conditional on
their premises, and where those premises are contested — the compensation ceiling most of all — the
conditionality transfers.

---

## 12. Conclusion

The claim that recursive self-improvement is substrate-indexed is right, and the reason given for it —
that domains differ in period, access, and floor type — describes the phenomenon rather than
explaining it. The explanation is that the domains differ in **which kind of intelligence their loop
steps require**. Identify is cognition and sits on the individual axis. Validate and deploy sit on the
organizational axis in every domain, because a system that evaluates and authorizes its own
modification has certified rather than validated it. And as the substrate moves outward, more of each
loop falls on the axis that individual self-improvement does not reach.

That yields a bounded individual axis and an unbounded organizational one. No stated closure criterion
requires open-ended individual intelligence; the outermost domain admits no individual coordinate at
all; and the argument that a machine improving its own cognition will run away is an argument about
one domain of five, which then meets a wall it does not describe.

The practical reading is narrower and more immediate. The software loop — the domain where the
individual axis is supposed to dominate — is gated at deploy, by authorization, on the organizational
axis. Its closure is not waiting on a better model. It is waiting on a separated authorizer fast
enough to keep up, and on someone recording when authorizations happen, which on the one system we
examined nobody had ever done.
