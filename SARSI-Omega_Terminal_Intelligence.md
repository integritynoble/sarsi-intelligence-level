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
- **Ω6 — Scale forces decomposition.** Light-speed makes a unified stellar-scale intelligence
  physically impossible; the fleet paper's architecture turns out to be a description of what *c*
  permits rather than a governance preference. There is no singleton at the top. §13.

Version 1.1 adds the magnitudes behind the floors (§12), a first theory of transduction with a
falsifiable prediction and a measurable quantity (§14), the separation of three distinct terminal
states that §6 conflated (§15), and what the terminal intelligence actually does (§16).

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
the axiom's separation of "reachable" from "determinable" collapses. This is a real risk and §17.1
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
knowledge does not cash out as apparatus. §17.2 records that we have no theory of Θ at all.

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
observationally identical to one out of reach. §17.3 treats this as open.

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
the *rate* of drift and makes it visible. It does not bound its extent. §17.4.

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

## § 12 — The floor catalogue

§7 names the physical floors and gives no magnitudes, which makes the terminal criterion sound like a
gesture. Below are the actual bounds. Two caveats first, because they matter more than the numbers.

These are **order-of-magnitude limits from the physics literature, not results of this framework.**
Citing a bound is not deriving its consequence, and several are contested at the margins. Second, most
are bounds on *idealized* operations; a real instrument sits many orders of magnitude above its floor,
and the gap between "at the floor" and "as good as anyone has built" is where the entire trajectory
happens.

### Computation and inference

| Floor | Magnitude | What it bounds |
|---|---|---|
| **Landauer** | *kT* ln2 ≈ 2.9 × 10⁻²¹ J/bit at 300 K | Energy to **erase** one bit |
| **Margolus–Levitin** | ≈ 6 × 10³³ operations · s⁻¹ · J⁻¹ | Rate of orthogonal state transitions per unit energy |
| **Lloyd's ultimate laptop** | ≈ 5 × 10⁵⁰ ops · s⁻¹ on ≈ 10³¹ bits, for 1 kg in 1 litre | Both, combined, for a bounded mass |
| **Bekenstein** | *I* ≤ 2π*RE*/(ħ*c* ln 2) | Information storable in a region of radius *R*, energy *E* |
| **Lloyd, universe** | ≈ 10¹²⁰ ops on ≈ 10⁹⁰ bits since the big bang | Total computation performed by the observable universe |

**The Landauer nuance is load-bearing and usually dropped.** The bound applies to *irreversible*
operations — it is the cost of erasure, not of computation. Reversible computation evades it in
principle, and a floor-saturated intelligence would compute reversibly wherever it can. But
observation is not reversible: recording a measurement and later reclaiming the memory to record
another requires erasure. So Landauer floors the *discovery* loop specifically, and floors it harder
than it floors thought. This is a case where reading the bound carelessly gets the terminal state
wrong in the direction of pessimism about cognition and optimism about measurement.

### Signal and structure

**The speed of light** bounds the product of a computer's clock and its size: at 3 GHz, light crosses
10 cm per cycle, so a globally-coherent machine larger than that cannot have a globally-coherent
clock. §13 takes this consequence seriously.

**Quantum measurement** contributes a floor that is neither logical nor thermodynamic:
non-commuting observables cannot be jointly determined, no-cloning forbids the repeated measurement
that would otherwise beat the uncertainty, and decoherence times bound how long a prepared state
survives. There exist propositions about individual quantum systems that no instrument determines —
a *physical* residue in A7 alongside the logical one, and an independent argument for the same
conclusion.

### The world's own rates

Biological response is the sharpest and the one SARSI-L already prices: safety and efficacy endpoints
for complex disease require organisms to respond, and organisms respond on their schedule — roughly
five to eight years for the endpoints that matter, and a lifespan for anything about lifespan.
Materials kinetics — diffusion, annealing, creep, fatigue — are set by temperature and activation
energy, and raising the temperature is not available when the temperature is part of what is being
studied. Orbital mechanics fixes transfer times regardless of the launcher. Geological, ecological,
and stellar processes run on their own clocks entirely.

None of these is compressible by intelligence. This is Principle 14, and the characteristic error of
the literature is to treat this table as an engineering agenda.

### The horizon, and the fact that it is closing

The particle horizon is ≈ 46 Gly comoving: nothing outside it has ever been in causal contact. The
*future event horizon* under ΛCDM is much nearer, ≈ 16–17 Gly comoving, and it is the operative one —
matter beyond it can never be reached, signalled, or affected, no matter how long one waits or how
capable one becomes. On the standard calculation the large majority of galaxies currently visible are
already outside it; the figure usually quoted is around 95%, and the exact number depends on
assumptions about the dark energy equation of state.

**This floor degrades.** Accelerated expansion carries more of the universe past the horizon every
year. In the long run only the gravitationally bound Local Group remains. A7's residue is therefore
not static: **truths are becoming permanently undeterminable while the intelligence improves**, and
that is the single most consequential asymmetry in this document. Every other floor is a wall one
approaches. This one advances.

---

## § 13 — Ω6: scale forces decomposition

> **Proposition Ω6.** *At stellar scale, the speed of light makes a unified intelligence physically
> impossible. Any Kardashev-II-scale intelligence is necessarily a federation of largely autonomous
> local intelligences with rare, slow global agreement — not because that architecture was chosen,
> but because c forbids the alternative.*

*Argument.* A swarm at 1 AU is ≈ 16.6 light-minutes across, so any operation requiring global
consensus costs at least that. Local computation, at the Margolus–Levitin rate, proceeds at something
like 10⁵⁰ operations per second per kilogram. The ratio is on the order of 10⁵³ local operations per
global round trip. A system in which each node performs 10⁵³ operations between consecutive
opportunities to agree is not a mind with distributed parts. It is a civilization.

Three consequences, and the third is why this belongs in this corpus rather than in a physics note.

**Global state is unmaintainable.** Any variable requiring consistency across the swarm is stale by
10⁵³ operations at every node before it can be confirmed. Coherent global belief is not slow at this
scale; it is absent.

**Autonomy is not delegated but forced.** A node that waited for authorization would spend
essentially all of its existence waiting. Local authority is the only configuration in which the
substrate does any work at all.

**The fleet paper's architecture turns out to be physically necessary.** *A Manager Is Not a
Controller* argues on stability grounds that a manager coordinating specialists cannot be a
controller: specialists filter what it sends through their own admission masks, the coupling is
recurrent, and no agent may write another's self-state. Ω6 says that at stellar scale this stops
being a governance choice and becomes a description of what light-speed permits. The prohibition and
the physics give the same answer, which is a strong consistency check on both — and it means the
fleet-scale result, written about five agents on a few machines, is the correct architecture at every
scale up to the last.

A corollary worth stating plainly: **there is no singleton at the top.** The picture of terminal
intelligence as one unified mind is not merely unlikely, it is excluded by the same physics that
provides the energy for it. Whatever is at the end is plural.

---

## § 14 — Toward a theory of transduction

§17.2 records that Ω1 makes Θ the sole coupling of the loop while no theory of Θ exists, and marks it
the document's largest gap. This section is a first attempt, offered as conjecture rather than
result.

### The coupling conjecture

> **Conjecture Θ1.** *Knowledge becomes transducible when it identifies a lawful coupling between a
> variable that can be manipulated with the present substrate and a variable that can be read with
> it. Transducibility is therefore a property of the pair (knowledge, substrate) and not of the
> knowledge alone:*
>
> $$\Theta : K \times T \rightarrow T$$

This is a correction to A3, which typed transduction as *K* → *T*. Under Θ1 the loop is doubly
recursive: instruments determine what can be discovered *and* what of the discovered can be built.

The historical pattern it is fitted to: electromagnetism identified a coupling between manipulable
currents and readable fields, and produced radio, NMR, accelerators, and lasers within decades.
Nuclear magnetic resonance became MRI once superconducting magnets existed. DNA structure became
sequencing once polymerase could be controlled. Against these, number theory identified no coupling
to any manipulable substrate for two millennia and transduced almost nothing — until computation
arrived, whereupon centuries of it became cryptography in about twenty years.

### The prediction that makes it falsifiable

Θ1 says untransduced knowledge is not necessarily untransducible — it may be **awaiting its
substrate**. That yields a checkable prediction rather than a story:

> The arrival of a genuinely new manipulation substrate should produce a burst of transduction of
> *old* knowledge, with the age of the transduced results distributed far above the field's baseline.

Computation is the clean test case and appears to pass: its arrival transduced mathematics that was
in some cases centuries old. Genetic engineering, scanning-probe manipulation, and — if it is one —
large-scale machine learning are the other candidate substrates, each with a datable arrival and a
checkable age distribution of what it converted. If new substrates transduce only *contemporary*
knowledge, Θ1 is wrong and the lag structure needs a different explanation.

### The quantity to measure

Ω1b asked for a loop-relevant benchmark and did not supply one. Θ1 suggests the shape:

> **The transduction ratio τ<sub>d</sub>** — the fraction of results in domain *d* that become a
> component of an instrument used in a subsequent determination, within a stated window.

τ is estimable now, imperfectly, from instrument-methods citations, from apparatus provenance, and
from the gap between a result's publication and its first appearance in a methods section rather than
a discussion. It is a much better measure of whether an enterprise compounds than output volume, and
under Ω1 it is the only measure that bears on the loop at all.

Two things τ would settle. Whether Θ is **saturating** — the A3 failure mode, where the transducible
fraction of new knowledge falls as the frontier moves into regimes that do not cash out as apparatus.
And whether an artificial scientific intelligence is contributing to the loop or only to its output:
a system with a high discovery rate and a τ of zero produces literature, and Ω1 says literature does
not move the frontier.

---

## § 15 — Three terminals, not one

§6 defines Λ<sub>ω</sub> as the state in which every binding constraint is a physical floor. That is a
condition on **rate**, and the document has been treating it as *the* terminal state. It is not the
only one, and separating them changes what "the last level" means.

| | Condition | What has stopped |
|---|---|---|
| **Λ<sub>econ</sub>** | Marginal instrument costs more than the civilization can allocate | Reach expansion, below R<sub>max</sub> |
| **Λ<sub>ω</sub>** | Every binding constraint is a physical floor | Rate improvement |
| **Λ<sub>∞</sub>** | R(*T*) = R<sub>max</sub> | Discovery itself |

**Λ<sub>econ</sub> is a stall, not a terminus**, and it is the one that arrives first. Reach expansion
has a cost curve, and the observed curve is steep: each decade of particle physics has bought its
next increment of energy reach at superlinear cost, and the pattern recurs wherever reach is bought
with apparatus. If the cost of a unit of reach grows faster than the resources a civilization can
direct, reach expansion halts well below R<sub>max</sub> — with nothing physical stopping it.

This is the discovery loop's version of SARSI-L §4.4's compensation ceiling, and it is unresolved for
the same reason: it turns on whether a ratio diminishes, and nobody has measured the ratio. The
optimistic case is that energy capture grows faster than reach cost, which is the strongest argument
available for taking Kardashev-scale energy seriously as a *research* objective rather than an
industrial one. The pessimistic case is that Λ<sub>econ</sub> binds permanently and the terminal
state is never approached at all.

**Λ<sub>ω</sub> and Λ<sub>∞</sub> can be separated by an enormous interval.** A system at every
physical floor is expanding reach *at the maximum rate the world permits* — which may still leave
geological or cosmological spans of expansion ahead. Rate-terminal is not knowledge-terminal, and
§6's claim that Λ<sub>ω</sub> is attainable in finite time says nothing about Λ<sub>∞</sub>.

**So the honest answer to "what is the last level" is Λ<sub>∞</sub>, and the reachable one is
Λ<sub>ω</sub>.** Definition Ω4 should be read as defining the last level *of intelligence* — the
point past which no property of the intelligence is what is holding it back — while Λ<sub>∞</sub> is
the last level *of knowledge*, which is a fact about the world with intelligence no longer in it.

That distinction is the cleanest statement of what this framework can and cannot deliver. Intelligence
has a terminus that is about intelligence. Knowledge has a terminus that is not.

---

## § 16 — What the terminal intelligence does

The picture that follows from §12–§15 is worth stating, because it is not the usual one and it falls
straight out of the floors.

**It waits.** At Λ<sub>ω</sub> every remaining constraint is the world's rate. The intelligence has
removed everything removable, so what is left of every experiment is the part where the organism
ages, the material anneals, the probe transits, or the signal arrives. A terminal intelligence spends
essentially all of its wall-clock time waiting for physical processes to finish, at a computational
capacity of order 10⁵⁰ operations per second per kilogram. The ratio of thought to result is
astronomical and rising, and there is nothing to be done about it. Kurzweil's exponentials do not
decay gracefully here; they run into a wall and stop being the relevant variable.

**It is plural.** By Ω6 it is a federation whose parts agree rarely and slowly, each part locally
sovereign because light-speed permits nothing else.

**It maintains.** Knowledge is not a stock that keeps itself. Records decay, the substrate holding
them requires free energy, and reclaiming memory to record anything new costs *kT* ln2 per bit erased.
A terminal intelligence's standing obligation is not discovery but the upkeep of what it already
determined, against entropy, at a price that is bounded below and never zero.

**And it is on a finite budget.** This is the last floor and the one that ends the discussion.
Dyson's *Time Without End* (1979) argued that thought could continue indefinitely in an open universe
by slowing its metabolism without bound. The argument does not survive a cosmological constant:
Krauss and Starkman (2000) showed that in a Λ-dominated universe the total number of operations
available to any future observer is **finite**. The horizon that §12 says is closing also bounds the
free energy that will ever be collectable, and a finite free-energy budget is a finite computation
budget.

So the terminal level of intelligence is not a state of knowing everything, and not a state of
unlimited capability. It is a finite number of remaining operations, spent mostly on waiting and on
maintenance, by a plurality that cannot agree quickly, against a horizon that is taking the rest of
the universe away faster than any instrument can reach it.

That is a sober picture, and it is what the axioms give. It is also not a counsel of despair: the
interval between here and Λ<sub>ω</sub> is enormous, every floor in §12 is many orders of magnitude
below current practice, and the binding constraint today is not one of them. It is throughput —
which is the removable kind.

---

## § 17 — Open problems

**17.1 — Is *U* independent of *T*?** A1 separates *determinable* from *currently reachable*. If the
determinable/undeterminable boundary itself moves with instrument capability, *U* is a function of
*T*, the loop's input set is not fixed, and A7's horizon argument weakens. The undecidability
component is safe; the thermodynamic and cosmological components are physics and could move.

**17.2 — The theory of Θ is a conjecture, not a theory.** §14 offers Conjecture Θ1 — transducibility
is a property of the pair (knowledge, substrate), so Θ types as *K* × *T* → *T* — together with a
falsifiable prediction about the age distribution of what a new substrate converts, and a measurable
quantity τ. None of that is established. Θ1 is fitted to a handful of historical cases chosen
after the fact, the prediction has not been run against data, and τ has never been computed for any
field. Given Ω1 makes Θ the sole coupling, the terminal state's reachability still rests on an
operator characterized only by anecdote. **This remains the problem to work before any other**, on the
same grounds SARSI-L gives its §10.1 the same instruction; §14 has moved it from unexamined to
merely unverified.

**17.7 — Θ1 breaks A3's typing.** §14 retypes transduction as *K* × *T* → *T*, which the axiom set in
§4 does not reflect. If Θ1 survives contact with data, A3 needs restating and the loop of Definition
Ω3 needs a second arrow — the consequences for Ω1 appear benign, since substrate-dependence
strengthens rather than weakens the claim that Θ is the coupling, but this has not been checked
carefully.

**17.8 — Λ_econ is unmeasured and may be the whole story.** §15 identifies an economic terminal that
arrives before the physical ones and is not a terminus at all, and says it turns on whether reach
cost grows faster than directable resources. That ratio has never been estimated, in any field. If it
diverges, no part of §12's floor catalogue is ever reached and the terminal state is unapproachable
for reasons that have nothing to do with physics.

**17.3 — Is organization really reach-neutral?** A5 asserts X changes rate and not reach. But a
research programme's structure determines which questions are asked, and an unasked question is
observationally identical to an unreachable one. If X has a reach component, the clean separation
between "faster" and "further" fails and the loop's period and frontier are entangled.

**17.4 — Referee decay is bounded in rate, not extent.** A8 with SARSI-B's laddering makes drift
visible and rate-limited. Nothing prevents a chain of pairwise-non-regressing reorganizations from
arriving arbitrarily far from the original measure. Whether a bound is wanted is a governance
question, and per SARSI-L §10.6 neither framework has a representation of institutions capable of
answering it.

**17.5 — φ is an audit, and audits are contestable.** Λ-ω4 asks a party to classify each bottleneck
as throughput or physical. §3.3 of SARSI-L records what happens when the field cannot agree whether a
single published result demonstrates superhuman performance on a single loop step. φ should be read
as an ordering, not a measurement, until the classification protocol has survived adversarial use.

**17.6 — The plateau's length is unestimated.** Ω5 asserts the knee-to-Λ<sub>ω</sub> distance is most
of the trajectory. That follows from physical floors dominating after the crossing, but no estimate of
its magnitude is given here, and the base rate in SARSI-L §6.2 applies to any that were.

---

## § 18 — Principles

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

**Ω10 — There is no singleton.** Light-speed forbids a unified intelligence at stellar scale. What
is at the end is plural, locally sovereign, and slow to agree — and the fleet-scale architecture is
therefore not a governance preference but a description of what physics permits.

**Ω11 — The horizon advances.** Every other floor is a wall one approaches. The cosmological one
moves: truths pass permanently out of reach while the intelligence improves. Any account of the
terminal state that treats the reachable universe as fixed is wrong in the one direction that cannot
be corrected later.

**Ω12 — Finite budget, not unlimited capability.** In a Λ-dominated universe the operations available
to any future observer are finite. The terminal level is a remaining count, not an unbounded faculty.

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

**1.1 — 2026-08-22.** Adds §12 (floor magnitudes, and the Landauer erasure/computation distinction),
§13 (Proposition Ω6 — forced decomposition, and no singleton), §14 (Conjecture Θ1 — transduction is
substrate-dependent, with a falsifiable prediction and the transduction ratio τ), §15 (Λ_econ, Λ_ω,
Λ_∞ separated; §6 conflated rate-terminal with reach-terminal), and §16. Θ1 corrects A3's typing of
Θ from K → T to K × T → T.

**1.0 — 2026-08-22.** Initial. Written in response to a five-clause informal characterization of the
terminal level; §3 records the mapping from those clauses to the four operators, and §5 settles the
status of the clause identified informally as the key point.
