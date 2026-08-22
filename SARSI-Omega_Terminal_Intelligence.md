# SARSI-Ω: The Terminal Level of Intelligence

## An axiomatic definition of the discovery loop and its saturation

*Document version: 1.0 — 2026-08-22*
*Companion to: `SARSI-L_Paper_v3.md` (system), `self_awareness/` (agent), `fleet/` (fleet), `SARSI-B_Brain_Improvement_Levels.md` (brain)*
*Repairs: SARSI-L §10.2 (attractor circularity) and Principle 06 (attractor invariance)*
*Supersedes for this purpose: `Civilizational_Transcendence_Paper.md` §1 (withdrawn)*

---

## Abstract

SARSI-L measures progress as distance to a Type II civilization, and defines that terminal state as
the condition reached when all substrate loops close. Its own §10.2 records the problem: the
framework measures progress toward a goal it defines as the measurement's endpoint. The withdrawn
transcendence paper made the same move in a different vocabulary — "the point at which intelligence
growth becomes self-sustaining" — and was withdrawn partly for it.

This document defines the terminal level without that circularity, by taking as primitive a loop the
existing framework does not represent: not the improvement of a substrate, but the conversion of the
unknown into the known, and of the known into the instruments that reach further unknown.

Eight axioms are given. From them:

- **Ω1 — Transduction is the sole coupling.** Knowledge extends reach only by becoming an
  instrument. Every other faculty can be arbitrarily good while the frontier stays fixed. §5.
- **Ω2 — The terminal state is saturation, not completeness.** Omniscience is excluded by logic,
  thermodynamics, and cosmology, so the terminal level must be defined as a condition on
  *bottlenecks* rather than on coverage. §6.
- **Ω3 — Saturation is externally anchored.** Its criterion references the speed of light, Landauer's
  bound, organism response times, and undecidability — none defined by this framework. §7.
- **Ω4 — Kardashev is an indicator, not a definition.** Terminal ⟹ high energy capture; high energy
  capture ⇏ terminal. The implication runs one way only. §8.
- **Ω5 — The singularity is the knee, not the terminus.** It is the crossing where throughput floors
  stop binding — the *entry* to SARSI-L's matter-bottleneck plateau, not its exit. §9.

§11 replaces the withdrawn progress scalar with a three-component vector, adding the component the
existing two do not capture.

---

## § 1 — Epistemic status of what follows

These are called axioms because they function as one: they are the load-bearing commitments a
definition of the terminal level rests on, and the definition is meaningless without them. They are
**not** axioms in the mathematical sense. None is self-evident, the system is not formalized enough
to derive theorems in the strict sense, and each could be false.

Accordingly every axiom below carries three things: the statement, **what fails if it is false**, and
**how it could be false**. An axiom set presented without those is a narrative with numbered
paragraphs. The corpus withdrew a set of metrics for less (Principle 11).

The propositions in §5–§9 are consequences of the axioms in the ordinary sense — if the axioms hold,
they follow. They inherit the axioms' uncertainty and do not exceed it.

---

## § 2 — Why a new loop is needed

SARSI-L's five domains are indexed by **substrate**: software, hardware, matter, biology, stellar
energy. A domain earns its place iff closing a loop over it removes a constraint binding on every
inner loop. That index is right for the question SARSI-L asks — *how fast does capability compound* —
and it is silent on a different question that the terminal state actually turns on: *how much of what
is true can be found out at all.*

These come apart. A system can close every substrate loop and be reach-bounded — able to modify its
own software, chips, matter, and energy supply, and still unable to determine a proposition because
no instrument it can construct interacts with the relevant part of the world. Conversely a system can
extend reach enormously with substrate loops wide open, which is what the last four centuries of
instrument-building were.

So the terminal state needs a loop indexed by **epistemic reach**, running across all five substrates
rather than within any one of them. That loop is the object of this document.

---

## § 3 — The discovery loop

**Definition Ω1 (the sets).**

- **U** — the *determinable unknown*: propositions about the world that are true, not currently
  known, and whose truth value is fixable by some finite physical interaction. §4/A1 explains what
  this excludes and why the exclusion is load-bearing.
- **K** — the known: propositions held with evidence, together with their provenance.
- **T** — the instrument set: apparatus, methods, materials, computation, and organizational
  procedure. Anything that participates in fixing a truth value.
- **C** — the organization hosting the loop: institutions, division of labour, review, funding,
  authority.

**Definition Ω2 (the operators).**

| Operator | Type | Name | Plain reading |
|---|---|---|---|
| **R** | *T* → 2<sup>U</sup> | **reach** | which unknowns the current instruments can touch |
| **D** | R(*T*) → *K* | **discovery** | converting a reachable unknown into knowledge |
| **Θ** | *K* → *T* | **transduction** | turning knowledge into an instrument |
| **X** | *K* × *T* → *C* | **reorganization** | restructuring the host so the loop runs faster |

**Definition Ω3 (the loop).** The discovery loop is

$$T \;\xrightarrow{\;R\;}\; R(T) \;\xrightarrow{\;D\;}\; K \;\xrightarrow{\;\Theta\;}\; T' \;\xrightarrow{\;R\;}\; R(T') \;\supsetneq\; R(T)$$

with **X** acting on *C* to set the loop's period rather than its reach. Its period is
*P*<sub>Ω</sub> = *t*<sub>R</sub> + *t*<sub>D</sub> + *t*<sub>Θ</sub>, and its rate is
ρ<sub>Ω</sub> = 1/*P*<sub>Ω</sub>.

This is the loop stated informally as: *find unknown truth → use it to reorganize → build tools from
it → reach more unknown truth*. Written this way the four clauses become four operators, and the one
identified informally as "the key point" — that new knowledge can be transformed into tools —
becomes Θ, whose status §5 settles.

**Relation to ⟨ι, μ, ν, δ⟩.** SARSI-L's loop improves a substrate; this one extends a frontier. They
compose: D's inner machinery is a ⟨ι, μ, ν, δ⟩ loop over the experiment, and Θ's output is a
substrate modification. SARSI-L's Definition 3 closure applies unchanged to each step, and the
throughput/physical floor distinction (Proposition 2, Principle 14) is what §7 runs on.

---

## § 4 — The axioms

### A1 — Determinable unknown

> There exists a nonempty set *U* of propositions that are true, not currently known, and whose truth
> value is fixable by finite physical interaction. Discovery operates on *U* and only on *U*.

*Why it is needed.* "Explore the unknown truth" needs a referent, and not every unknown has one.

*What the restriction does.* A1 deliberately excludes three classes from *U* at the outset: formally
undecidable propositions (Gödel, Turing, Chaitin's Ω), propositions about regions beyond the
cosmological particle horizon, and propositions requiring more information storage than the
Bekenstein bound permits in the available volume. These are not hard problems awaiting better
instruments; they are outside the domain of the operator. Building the exclusion into A1 rather than
apologizing for it later is what allows §6's terminal definition to be a state rather than an
unreachable direction.

*What fails without it.* The terminal level becomes omniscience, which A7 shows is unreachable, so
the framework would again define a terminus it cannot approach.

*How it could be false.* If the determinable/undeterminable line is not fixed — if it moves with
instrument capability in ways not currently anticipated — then *U* is itself a function of *T*, and
the axiom's separation of "reachable" from "determinable" collapses. This is a real risk and §12.1
treats it as open.

### A2 — Instrument-bounded reach

> Past a threshold of cognitive capability, which frontier propositions are determinable is set by
> the available instruments, not by the intelligence applying them: D is defined on R(*T*), and
> R(*T*) is a property of *T*.

*Why it is needed.* It is the empirical core, and it is what makes the loop a loop. If reach were
cognition-bounded, a sufficiently capable mind would reach everything by thinking, and no recursion
through instruments would be required.

*What fails without it.* Θ becomes optional, Ω1 fails, and the terminal state reduces to "sufficiently
intelligent" — unmeasurable and, per §10, exactly the error the withdrawn paper made.

*How it could be false.* Partly, and interestingly. Large tracts of the frontier are theory-bound
rather than instrument-bound; there are periods where the data exist and the interpretation does not.
A2 should be read as: instruments bound reach *at the margin, in the limit, and increasingly* — not
that theory never binds. If theory-boundedness is dominant and durable, A2 weakens and Ω1 weakens
with it.

### A3 — Transduction

> There exists a map Θ: *K* → *T* that is not trivial: some knowledge, once held, can be built into
> an instrument.

*Why it is needed.* It is the only operator whose input is the loop's output and whose output is the
loop's input.

*What fails without it.* Knowledge accumulates and reach never moves. The system becomes a library:
it can answer what it already knows and cannot find out anything new that its founding instruments
could not already reach.

*How it could be false.* Not wholly — the historical record is unambiguous (optics → telescope →
astronomy → better optics; solid-state physics → transistor → computation → semiconductor physics;
molecular biology → sequencing → genomics → better sequencers). But Θ could be *saturating*: the
transducible fraction of new knowledge may be falling, if the frontier moves toward regimes whose
knowledge does not cash out as apparatus. §12.2 records that we have no theory of Θ at all.

### A4 — Non-degenerate amplification

> There exists *k* ∈ D(R(*T*)) with R(*T* ∪ Θ(*k*)) ⊋ R(*T*): discovery sometimes strictly expands
> its own reach.

*Why it is needed.* A3 gives instruments; A4 gives instruments that reach *further*. Without the
strictness the loop is a treadmill — new apparatus, same frontier.

*What fails without it.* The loop is not recursive. It is a production process with constant returns,
and there is no explosion of any kind to discuss.

*How it could be false.* If reach expansion is asymptotic and the asymptote is near, A4 holds
formally and vacuously. The observable is whether the *cost* of a unit of reach expansion is rising
faster than the resources available — the discovery-loop analogue of the compensation-ceiling
question in SARSI-L §4.4, and unresolved for the same reasons.

### A5 — Organization sets rate, not reach

> The loop's period *P*<sub>Ω</sub> is a function of *C*, the organization hosting it. X can change
> *P*<sub>Ω</sub> by orders of magnitude while leaving R(*T*) unchanged.

*Why it is needed.* It separates *knowing more* from *knowing faster*, and it is where the informal
clause "reorganize science and civilization to promote progress" lives. Peer review latency, funding
cycles, replication practice, the division of labour between specialists, and who is permitted to
authorize an experiment are all *C*, and none of them changes what is physically reachable.

*What fails without it.* Reorganization gets conflated with discovery, and a civilization that has
made itself efficient is mistaken for one that has learned something.

*How it could be false.* Organization may not be cleanly separable from reach — a research
programme's structure determines which questions get asked, and a question never asked is
observationally identical to one out of reach. §12.3 treats this as open.

### A6 — Two kinds of floor

> Every step of the loop has a lower bound on its period, of exactly two kinds. **Throughput floors**
> are set by the finite capacity of an agent performing the step and are removable by automation or
> by closure. **Physical floors** are set by the world and are not removable by any amount of
> cognition.

*Why it is needed.* This is the entire content of the terminal definition, and it is imported
unchanged from SARSI-L (Proposition 2, Principle 14) rather than invented here.

*What fails without it.* No criterion for the terminal state exists that is not circular, because
every alternative criterion is phrased in terms of the system's own capability.

*How it could be false.* If a floor believed physical turns out to be throughput in disguise. The
history of such reclassifications is real but one-directional and slow; the reverse error — treating
a physical floor as compressible by intelligence — is, per Principle 14, the characteristic error of
this literature.

### A7 — Horizon

> R<sub>max</sub>, the union of reach over all physically constructible instrument sets, is a proper
> subset of the propositions about the world. No instrument set attains completeness.

*Why it is needed.* It is what forces §6's definition to be about bottlenecks rather than coverage.

*The three independent sources.* Logical: undecidable propositions have no finite decision procedure,
so no apparatus decides them. Thermodynamic: computation and measurement have energy costs (Landauer),
and a finite region holds finite information (Bekenstein), so an unbounded inference is not physically
instantiable. Cosmological: the particle horizon bounds what has ever been in causal contact, and
accelerated expansion is *removing* regions from future contact — the reachable universe is shrinking,
so some truths are becoming permanently undeterminable while the intelligence improves.

*What fails without it.* Omniscience returns as the terminus, and the framework once again names an
endpoint it cannot approach — the exact failure §10.2 records.

*How it could be false.* The cosmological component depends on the dark energy equation of state; the
thermodynamic component on the applicability of the bounds to the relevant class of inference. Both
are live physics. A7 is the axiom most likely to be revised and least likely to be overturned.

### A8 — External referee for progress

> "Promoting progress" is defined only against a measure of progress that the reorganizing
> intelligence did not author. X is admissible only when judged against a retained referee.

*Why it is needed.* Directly from SARSI-B §3: an improvement loop is well-posed only if its evaluator
lies outside its write set. X writes *C*, and *C* contains the institutions that evaluate. A system
that reorganizes the evaluator and then reports improvement is reporting a tautology, and every
result about goal revision applies unchanged one scale up.

*What fails without it.* Reorganization becomes self-certifying, and there is no observation that
distinguishes a civilization that improved from one that redefined improvement. This is not a remote
hazard; the base rate for totalizing reorganizations judged by their own authors is a matter of
record.

*How it could be false.* The referee decays: a measure retained from before the reorganization
increasingly asks whether the new arrangement solves the old problem. SARSI-B §4's laddering —
each revision judged against its immediate predecessor, every referee versioned and logged — bounds
the *rate* of drift and makes it visible. It does not bound its extent. §12.4.

---

## § 5 — Ω1: transduction is the sole coupling

> **Proposition Ω1.** *Under A2 and A3, Θ is the only operator whose output enters the loop's own
> input. Consequently, if Θ is empty or non-reach-extending, the loop is open regardless of the
> capability of D, the quality of X, or the intelligence of the system — and its frontier is fixed at
> R(T₀) for the founding instrument set T₀.*

*Argument.* By A2, D is defined on R(*T*), so the input to discovery is determined by *T* alone. The
operators are R, D, Θ, X. R is a property of *T*, not a producer of it. D produces *K*. X produces
*C*, which by A5 changes period and not reach. Θ alone produces *T*. So the only path from the loop's
output back to its input runs through Θ. Sever it and R(*T*) is constant; the system converts
R(T₀) into knowledge, exhausts it, and stops.

**This is the formal content of the informal claim that turning knowledge into tools is the key
point, and it is stronger than the informal version.** The informal reading is that transduction is
*important*. Ω1 says it is *the whole coupling*: an intelligence with a perfect D, a perfect X, and
no Θ is not a slower version of a recursive discoverer, it is a non-recursive one. Arbitrarily large
improvements in reasoning, in speed, in organization, and in the ability to derive consequences from
what is already known move the frontier by exactly zero.

Two corollaries worth stating.

**Ω1a — the diagnostic.** For any research enterprise, the question that predicts whether it
compounds is not how much it discovers but what fraction of what it discovers becomes apparatus. An
enterprise with a high D and a near-zero Θ produces literature; the same enterprise with a modest D
and a live Θ produces a frontier that moves.

**Ω1b — where an intelligence should be measured.** Under Ω1, evaluating a scientific intelligence on
its ability to answer questions measures D and is silent on the loop. The loop-relevant measurement
is whether the artifacts it produces extend what the next round can reach. This is a different
benchmark than any currently run, and §11's third component is an attempt at it.

---

## § 6 — Ω2: the terminal state is saturation

By A7, completeness is unreachable. A terminal level defined as "knows all truths" would be a
direction that no trajectory attains, and a framework whose endpoint is unattainable cannot measure
distance to it — which is how the current attractor became circular in the first place.

The available alternative is to define the terminal state as a condition on *what is stopping it*.

> **Definition Ω4 (the terminal level, Λ<sub>ω</sub>).** An intelligence is at the terminal level iff,
> for every step of its discovery loop, the binding constraint on that step's period is a **physical
> floor** and not a **throughput floor**.
>
> Equivalently: no further automation, no further loop closure, no further reorganization of *C*, and
> no further instrument construction can raise ρ<sub>Ω</sub>, because everything removable has been
> removed and what remains is the world's own rate.

> **Proposition Ω2.** *Λ<sub>ω</sub> is a state and not merely a direction: it is attainable in
> finite time under A1–A7, whereas completeness is not attainable at all.*

*Argument.* The set of throughput floors in a loop is finite at any time, each is removable by A6,
and removal does not create new throughput floors except by adding steps, which A4 bounds. Physical
floors are not removable and not created by the system. So the process of removal terminates. It
terminates at a state in which the remaining constraints are all physical — which is Λ<sub>ω</sub>.

Three things follow that are worth being explicit about, because each contradicts a common reading of
"terminal intelligence."

**Λ<sub>ω</sub> is not omniscient.** It knows what its instruments reached. A7's residue —
undecidable, beyond-horizon, over-bound — is permanently outside it, and the cosmological part is
*growing*.

**Λ<sub>ω</sub> is not fast.** It is as fast as the world permits and no faster. If a question
requires an organism to age, Λ<sub>ω</sub> waits for the organism. SARSI-L's matter bottleneck says
this plateau is where most of the trajectory is spent.

**Λ<sub>ω</sub> is domain-indexed.** A system can be floor-saturated in one domain and
throughput-bound in another, and almost certainly will be for a long time. Λ<sub>ω</sub> is reported
as a vector over domains, exactly as loop completion is (§11).

---

## § 7 — Ω3: why this is not circular

> **Proposition Ω3.** *Definition Ω4 references only quantities defined outside this framework, and
> therefore measures progress toward an endpoint the framework does not itself construct.*

The physical floors that constitute the criterion are: the speed of light; Landauer's bound and the
thermodynamic cost of measurement; decoherence and quantum measurement limits; the response times of
organisms and ecosystems; materials kinetics, diffusion, and annealing; orbital mechanics and transfer
times; the cosmological horizon; and, on the logical side, undecidability. Not one of them is defined
by SARSI-L, by this document, or by any property of the intelligence being measured. They are what
the world does.

This is what the old formulation could not say. "The condition reached when all loops close" is
defined by the framework's own loop taxonomy, so distance to it is a statement about the framework.
"The condition in which every binding constraint is a physical floor" is defined by physics, so
distance to it is a statement about the world.

**The measurement is negative, and this is a feature.** One cannot enumerate *U*, so reach cannot be
measured by counting truths. But Λ<sub>ω</sub> does not require enumerating anything. It requires
auditing bottlenecks: for each step of a real discovery loop, ask whether what makes it slow is an
agent's finite capacity or the world's own rate. *Is this clinical trial slow because of IRB
scheduling or because the endpoint takes five years?* Both answers are available today, for real
loops, without any theory of *U*.

---

## § 8 — Ω4: Kardashev relocated

The Kardashev scale is a good reference for the terminal state and a bad definition of it, and the
distinction matters for what gets measured.

> **Proposition Ω4.** *Λ<sub>ω</sub> ⟹ energy capture at its own physical floor. The converse does
> not hold.*

*Forward.* Instruments consume energy, and by A2 reach is instrument-bounded, so an intelligence that
has removed every throughput constraint on instrument construction has pushed energy capture until
energy capture itself is physically floored. A floor-saturated intelligence is therefore high on the
Kardashev scale, and the scale is a legitimate *indicator*.

*Converse fails.* A Type II civilization with a slow review process, a poor division of scientific
labour, or an authority structure that gates experiments is throughput-bound and not terminal. Energy
is one input to reach; it is not the binding constraint at every step, and Kardashev level is silent
about all the other steps. A civilization can be enormously powerful and epistemically stalled, and
nothing in the Kardashev scale would show it.

The practical consequence: **watts are a component of the progress vector, not the vector.** SARSI-L
§10.2 already proposed energy-plus-closure for exactly this reason; Ω4 says why the pair is still
incomplete and §11 adds the missing third.

---

## § 9 — Ω5: the singularity is the knee

Kurzweil's singularity and the withdrawn paper's "boundary condition at which growth becomes
self-sustaining" are the same object, and in this vocabulary it is neither the terminal state nor a
date.

> **Proposition Ω5.** *The singularity is the crossing at which throughput floors cease to be the
> binding constraint on the majority of the discovery loop's steps. It is a transition interior to
> the trajectory, and it is the entry to SARSI-L's matter-bottleneck plateau rather than the exit
> from it.*

Before the crossing, most of what is slow is slow because a finite agent is doing it, and the returns
to automation and to loop closure are correspondingly large — which is what produces the observed
acceleration and Kurzweil's curves. After the crossing, the remaining constraints are increasingly
the world's, the returns to further automation collapse toward zero, and the trajectory flattens onto
the physical floors. SARSI-L §5.5 already predicts this shape from an independent argument: rapid
acceleration through the software loop, then a long plateau regulated by the slowest physical process
on the critical path.

So the two frameworks agree on the shape and disagree on the label. The singularity is not the end of
the story; it is the moment the story stops being about us and starts being about the world's rate
limits. **The distance from the knee to Λ<sub>ω</sub> is the plateau, and by every physical-floor
estimate available it is the overwhelming majority of the trajectory.** Treating the knee as the
terminus is the single most consequential error available in this area, and it is the error the
withdrawn paper made.

---

## § 10 — Operational criteria

In the form Principle 11 requires: observable, and not satisfiable by definitional adjustment after
the fact.

**Λ-ω1 · Reach extension.** A system that, without human direction at any step: (a) identifies a
proposition outside the reach of its current instruments; (b) designs an instrument predicted to
bring it within reach; (c) constructs it; (d) determines the proposition with it; (e) where the
determination is negative, revises the instrument rather than the proposition. Clause (e) is the
criterion — (a)–(d) without it is apparatus-building toward a foregone conclusion.

**Λ-ω2 · Transduction.** A system that: (a) takes a result it discovered rather than was given;
(b) constructs from it an artifact used as an instrument in a subsequent discovery; (c) demonstrates
that the subsequent discovery was outside the reach of the prior instrument set. Clause (c) is the
criterion, and it is what distinguishes Θ from ordinary engineering.

**Λ-ω3 · Reorganization.** A system that: (a) identifies a step of its own discovery loop whose
binding constraint is a throughput floor; (b) restructures *C* to remove it; (c) shows
ρ<sub>Ω</sub> rose; (d) shows the rise on a retained referee it did not author (A8). Clause (d) is
the criterion.

**Λ-ω4 · Floor discrimination.** A system that, for each step of its loop, classifies the binding
constraint as throughput or physical, and whose classifications survive adversarial review by a party
that did not make them. Without this the terminal criterion cannot be evaluated at all — this is the
instrument for §11's third component.

**Λ<sub>ω</sub> · Terminal.** A system for which Λ-ω4 returns *physical* on every step of every
discovery loop it runs. Reported per domain; a scalar is not available.

---

## § 11 — The progress vector

SARSI-L §10.2 withdrew the progress scalar and proposed a two-component replacement, both externally
anchored: energy captured and directed in watts, and the closure vector (λ<sub>I</sub> …
λ<sub>V+</sub>). Ω1 and Ω4 show the pair is incomplete — it measures power and autonomy, and is
silent on reach.

**Proposed three-component vector:**

| # | Component | Anchor | Measured by |
|---|---|---|---|
| 1 | Energy captured and directed (W) | Kardashev; physics | Direct |
| 2 | Closure vector (λ<sub>I</sub> … λ<sub>V+</sub>) | SARSI-L §3.2 criteria | Step audit |
| 3 | **Floor saturation φ<sub>d</sub>** | Physical floors (§7) | Λ-ω4 audit |

where **φ<sub>d</sub> ∈ [0,1] is the fraction of the discovery loop's steps in domain *d* whose
binding constraint is a physical rather than a throughput floor.** Λ<sub>ω</sub> is φ<sub>d</sub> = 1
for all *d*.

Three properties. It is externally anchored, so Ω3 holds. It is measurable now, negatively and per
step, without any theory of *U*. And it is not implied by the other two: a system can be high on
energy and closure and low on φ, which is precisely the case Ω4's failed converse describes and
which the two-component vector cannot express.

**On φ and Principle 06.** Attractor Invariance currently asserts that the terminal state does not
change as loops close, while admitting the attractor is a construction of the framework. Under
Definition Ω4 the invariance is *derived* rather than asserted: the terminal state is fixed because
physical floors are properties of the world and do not move when the system improves. Principle 06
can be restated as a consequence, and its parenthetical admission removed.

---

## § 12 — Open problems

**12.1 — Is *U* independent of *T*?** A1 separates *determinable* from *currently reachable*. If the
determinable/undeterminable boundary itself moves with instrument capability, *U* is a function of
*T*, the loop's input set is not fixed, and A7's horizon argument weakens. The undecidability
component is safe; the thermodynamic and cosmological components are physics and could move.

**12.2 — There is no theory of Θ.** A3 asserts transduction exists; nothing says which knowledge is
transducible, at what rate, or whether the fraction is stable. Given Ω1 makes Θ the sole coupling,
this is the largest gap in the document — the terminal state's reachability depends entirely on an
operator we can exhibit historically and cannot characterize. **This problem should be worked before
any other**, on the same grounds SARSI-L gives its §10.1 the same instruction.

**12.3 — Is organization really reach-neutral?** A5 asserts X changes rate and not reach. But a
research programme's structure determines which questions are asked, and an unasked question is
observationally identical to an unreachable one. If X has a reach component, the clean separation
between "faster" and "further" fails and the loop's period and frontier are entangled.

**12.4 — Referee decay is bounded in rate, not extent.** A8 with SARSI-B's laddering makes drift
visible and rate-limited. Nothing prevents a chain of pairwise-non-regressing reorganizations from
arriving arbitrarily far from the original measure. Whether a bound is wanted is a governance
question, and per SARSI-L §10.6 neither framework has a representation of institutions capable of
answering it.

**12.5 — φ is an audit, and audits are contestable.** Λ-ω4 asks a party to classify each bottleneck
as throughput or physical. §3.3 of SARSI-L records what happens when the field cannot agree whether a
single published result demonstrates superhuman performance on a single loop step. φ should be read
as an ordering, not a measurement, until the classification protocol has survived adversarial use.

**12.6 — The plateau's length is unestimated.** Ω5 asserts the knee-to-Λ<sub>ω</sub> distance is most
of the trajectory. That follows from physical floors dominating after the crossing, but no estimate of
its magnitude is given here, and the base rate in SARSI-L §6.2 applies to any that were.

---

## § 13 — Principles

**Ω01 — Reach before capability.** At the frontier, what can be found out is set by what can be
built, not by how well one thinks. Capability that does not become apparatus does not move the
frontier.

**Ω02 — Transduction is the coupling.** Knowledge that cannot become an instrument does not compound.
Measure a scientific intelligence by what fraction of its output the next round can use as a tool.

**Ω03 — Saturation, not completeness.** The terminal state is the removal of every removable
constraint, not the knowledge of every truth. Completeness is excluded by logic, thermodynamics, and
cosmology, and a terminus that cannot be approached cannot measure anything.

**Ω04 — Floors are the anchor.** Define the endpoint by the world's rate limits, never by the
system's own capability. The second is how the attractor became circular.

**Ω05 — Rate is not reach.** Reorganization makes the loop faster; only instruments make it further.
A civilization that has optimized itself has not thereby learned anything.

**Ω06 — Progress is a vector.** Watts, closure, and floor saturation. None implies the others; a
powerful, autonomous, epistemically stalled civilization is a coherent state that a scalar cannot
express.

**Ω07 — Kardashev indicates, it does not define.** Terminal implies high energy capture. High energy
capture implies nothing.

**Ω08 — The knee is not the end.** The singularity is where throughput floors stop binding — the
entry to the plateau. Most of the trajectory lies after it, and treating it as the terminus is the
characteristic error.

**Ω09 — No self-certified progress.** An intelligence that reorganizes the institutions that judge it
and then reports improvement has reported nothing. The referee is retained, versioned, and external,
or the claim is void.

---

## Relation to prior documents

| Document | Scale | Question |
|---|---|---|
| `SARSI-L_Paper_v3.md` | System | How far has RSI propagated across substrates? |
| `self_awareness/` | Agent | What does an agent know about itself? |
| `fleet/` | Fleet | What may one agent assert about another? |
| `SARSI-B_…md` | Brain | What may an agent change about itself? |
| **This document** | **Terminal** | **What is the endpoint, defined without reference to the framework's own loops?** |

SARSI-Ω imports A6 from SARSI-L (Proposition 2, Principle 14) and A8 from SARSI-B (evaluator
externality, the frozen referee) without modification. Its own contributions are the discovery loop
of §3, the transduction result Ω1, the saturation definition Ω4, and the third component of the
progress vector.

**What it repairs.** §10.2's attractor circularity, by Proposition Ω3. Principle 06, which becomes
derived rather than asserted (§11). And the withdrawn transcendence paper's §1 boundary-condition
definition, which is replaced by Proposition Ω5.

## Version history

**1.0 — 2026-08-22.** Initial. Written in response to a five-clause informal characterization of the
terminal level; §3 records the mapping from those clauses to the four operators, and §5 settles the
status of the clause identified informally as the key point.
