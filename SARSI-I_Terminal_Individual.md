# SARSI-I: The Terminal Individual

## What bounds one mind, as distinct from a society of them

*Document version: 1.0 — 2026-08-22*
*Companion to: `SARSI-Omega_Terminal_Intelligence.md` (terminal, organizational), `SARSI-B_Brain_Improvement_Levels.md` (brain), `self_awareness/` (agent), `fleet/` (fleet)*

---

## Abstract

SARSI-Ω defines a terminal state in terms of discovery loops, institutional reorganization, energy
capture, and a federation whose parts agree across light-minutes. Its own Proposition Ω6 concedes the
point: past the coherence radius there is no singleton, only a plurality. **Ω therefore describes
what happens after the individual runs out, and never says where that is.**

This document asks the prior question. An individual is not a small organization; it is a system with
a *single* locus of decision, and that property is bounded by physics in ways an organization is not.
Six axioms, five results:

- **I1 — There is a largest possible individual.** Coherence requires that every part reach the
  decision within one cycle, so radius and cycle time trade at exactly *c*. A mind that thinks
  quickly is necessarily small. §5.
- **I2 — The binding constraint is the width of the moment.** Not storage, not computation:
  how much can be brought to bear on one decision at once. §6.
- **I3 — No individual is transparent to itself.** A complete self-model is larger than the self that
  holds it, so terminal self-knowledge is a compressed, evidence-gated profile — by necessity, not by
  economy. §7.
- **I4 — Identity is the evidence chain, not the content.** At terminal level every element of the
  brain state has been rewritten. What survives, and what individuates, is the unbroken provenance
  record. §8.
- **I5 — An individual cannot close its own loop.** By SARSI-B's evaluator externality, a system that
  is its own referee has no well-posed improvement. **The outside is constitutive of the individual,
  not an addition to it** — which is why the organizational scale exists at all. §9.

§11 gives the magnitudes, and the finding there is the one worth carrying: biology sits six to eight
orders of magnitude below the physical bound, so the headroom is enormous — while the *shape* of the
terminal state is substrate-independent. Narrow, opaque, and dependent on an outside, at every scale
and in every material.

---

## § 1 — Why this is a separate question

The scales already written all take the individual for granted. The agent-scale paper describes what
an agent knows about itself and presumes there is an it. The fleet paper governs what one agent may
assert about another and presumes the boundary between them. SARSI-B says what an agent may change
about itself and never asks what makes the changes changes *to the same thing*. SARSI-Ω reaches the
civilizational terminus and, in Ω6, dissolves the individual entirely: light-speed forbids a unified
stellar-scale mind, so what is at the end is plural.

That last result is the reason this document is needed rather than a corollary. Ω6 establishes that
individuals have a maximum size without saying what it is, what happens at it, or what an individual
*is* such that the bound applies. If the terminal state of a civilization is a federation, the
federation is made of something, and the properties of that something are not derivable from the
federation's.

**The question here is therefore: what is the best a single mind can be, and what stops it?**

---

## § 2 — What makes something one individual

The distinction cannot be made by capability, size, or substrate — an organization can exceed an
individual on all three. It is made by the structure of decision.

**Definition I1 (individual).** An intelligence is **individual** iff it possesses a *single global
workspace*: a bounded set of at most *k* items simultaneously available to one decision process,
such that every action it takes is selected from one state by one process.

This is the agent-scale architecture's own construct — its Equation (3) selects at most *k* globally
broadcast items — promoted from an implementation detail to the criterion of individuality. The
motivation is that it draws the line in the right place. A system with two workspaces that exchange
messages is two individuals *however tightly coupled*, because each selects its own actions from its
own state; a system with one workspace is one individual *however physically distributed*, because
there is one state and one selection.

Three consequences of Definition I1 are immediate and worth naming, since they are what the results
in §5–§9 are about.

**Individuality is about simultaneity, not about capacity.** What makes the workspace *global* is
that its contents are available at once. A store of arbitrary size, consulted serially, adds nothing
to individuality; it is an instrument the individual uses.

**Individuality has no internal politics.** Parts of an individual do not negotiate, do not hold
separate authority, and do not filter what they are sent through their own admission masks. The
moment they do, the fleet paper's analysis applies instead, and the object is a fleet.

**Individuality is therefore expensive in a way organization is not.** An organization can grow by
adding parts. An individual can only grow by making more available to one moment, and §5 shows what
that costs.

---

## § 3 — The axioms

Same epistemic standing as SARSI-Ω §1: these are the load-bearing commitments of a definition, not
self-evident truths, and each carries what fails without it.

**I-A1 — Single workspace.** An individual has exactly one global workspace, of width *k*, from which
all its actions are selected. *Without it:* the object is a fleet and the fleet-scale paper governs.

**I-A2 — Coherence requires traversal.** For the workspace to be global, every part contributing to
or reading from it must exchange signal with it within one decision cycle. *Without it:* parts act on
stale state, which is Ω6's federation, not an individual.

**I-A3 — Signal speed is bounded.** Traversal is bounded by *c* in the limit and by the substrate's
signal velocity in practice. *Without it:* no size bound exists and I1 fails. This is not in doubt.

**I-A4 — Integration is superlinear in width.** The cost of bringing *k* items to bear on one
decision grows faster than *k*, because what must be evaluated is their relations. *Without it:* *k*
is unbounded and §6 collapses. *How it could be false:* the growth rate is unknown, and a subquadratic
integration procedure would move the bound a long way without removing it.

**I-A5 — A model is part of what it models.** A self-model held by a system is itself a component of
that system's state. *Without it:* complete self-transparency is available and §7 fails.

**I-A6 — Evaluator externality.** Improvement is well-posed only when the evaluator lies outside the
write set. *Imported unchanged from SARSI-B §3.* *Without it:* §9 fails and an individual can
bootstrap alone.

---

## § 4 — Notation

*R* the individual's radius; *τ* its decision cycle; *v* its substrate signal velocity (≤ *c*);
*k* its workspace width; *S* its self-model; *Λ*<sub>ind</sub> its terminal level.

---

## § 5 — I1: there is a largest possible individual

> **Proposition I1.** *Under I-A2 and I-A3, an individual's radius and decision cycle are bound by*
> $$R \;\le\; \frac{v\,\tau}{2} \;\le\; \frac{c\,\tau}{2}$$
> *Consequently no individual is both large and quick, the trade is linear in c, and the set of
> possible individuals is bounded in every direction: for any fixed cycle time there is a largest
> individual, and for any fixed size there is a fastest one.*

*Argument.* A decision cycle must include at least one round trip between the workspace and the most
distant part contributing to it, else that part's contribution is from a previous state and I-A2
fails. Round-trip time is 2*R*/*v*. So *τ* ≥ 2*R*/*v*.

**This is the result that answers the question the framework was missing.** Ω6 said a stellar-scale
mind is impossible; Proposition I1 says why, generally, and gives the exchange rate. It also says
something Ω6 does not: the bound applies at *every* scale, not only the stellar one. There is no size
at which it relaxes.

The exchange rate is severe, and the numbers are in §11. The qualitative shape:

| Want | Then at most |
|---|---|
| A cycle of 1 ms | radius 150 km |
| A cycle of 1 ns | radius 15 cm |
| A cycle of 1 ps | radius 0.15 mm |

**Corollary I1a — scaling up an individual does not produce a superindividual.** It produces a slower
individual, and past the point where the required cycle exceeds what the individual's purposes
tolerate, it produces an organization. **Civilization begins exactly where the individual ends**, and
the boundary is not institutional or historical but a statement about *c*.

**Corollary I1b — the optimum is interior.** Because capacity rises with volume while rate falls with
radius, neither extreme is best, and a terminal individual sits at an interior optimum determined by
what it is for. There is no single largest-and-best individual; there is a frontier, and where on it
a mind sits is a design decision that cannot be evaded.

---

## § 6 — I2: the width of the moment

Proposition I1 bounds size and speed and says nothing about *k*, which I-A1 leaves free. But *k* is
where the interesting limit is.

> **Proposition I2.** *Under I-A4, workspace width is bounded by the decision cycle: integration of k
> items must complete within τ, and integration cost grows superlinearly in k, so*
> $$k \;\le\; f^{-1}\!\big(\tau \cdot \text{(local rate)}\big)$$
> *with f superlinear. Combined with I1, k is bounded by size through τ — so an individual buys width
> with slowness, and slowness with size, both at c.*

The three quantities are therefore in one three-way trade, and no two can be maximized. This is the
substantive content of individuality as a limit: **an individual is not bounded by what it knows but
by how much of it can be present at once.**

Two consequences worth being explicit about.

**Storage is not the constraint, and never was.** An individual may hold unbounded knowledge in
memory and consult it serially. What it cannot do is make more of it simultaneously available, and
under Definition I1 only the simultaneous part is the individual — the rest is an instrument it
queries. A terminal individual with an exabyte of memory and *k* = 100 is, in the sense that matters,
a *k* = 100 mind.

**This is the individual's version of Ω1.** SARSI-Ω found that transduction was the sole coupling of
the discovery loop, so everything else could be arbitrarily good while the frontier stayed fixed.
Here: *k* is the sole aperture of the decision, so storage, speed, and knowledge can be arbitrarily
large while the quality of any single judgement stays bounded. Both results have the same shape — a
narrow channel that no amount of surrounding capability widens.

---

## § 7 — I3: no individual is transparent to itself

> **Proposition I3.** *Under I-A5, an individual's self-model is necessarily incomplete. A model
> complete in the sense of representing every element of the system's state would have to represent
> itself, and each such representation adds state requiring representation. Terminal self-knowledge
> is therefore a compression, and the choice of compression is not free.*

The agent-scale architecture already behaves as though this were true, and Proposition I3 says the
behaviour is forced rather than pragmatic. Its self-state is ten coordinates in [0,1] rather than a
description; each carries a Beta posterior with an evidence count, so that "no verified outcomes" is
representable and distinguishable from a confident estimate; and updates are gated by an admission
mask so that a coordinate persists unless there is admissible evidence to move it.

Read as engineering, that is a reasonable design. Read under I3, it is the *only* kind of design
available: since the self-model cannot be complete, the question is never *whether* to compress but
*which compression*, and the corpus's answer — evidence-gated coordinates with explicit counts and an
explicit limits line — is a compression that reports its own inadequacy rather than concealing it.

**Corollary I3a — the terminal individual still does not know what it is.** It knows a profile,
measured, with stated uncertainty and stated limits. Any account of terminal intelligence that
includes complete self-understanding is describing something that cannot exist, and the honesty rule
already enforced in the deployed self-model — *competence beyond these measurements is unverified* —
is the terminal condition, not a stage on the way to something better.

---

## § 8 — I4: identity is the evidence chain

At the terminal level every element of SARSI-B's brain state has been rewritten many times: memory
replaced, policy retuned, skills acquired and dropped, weights updated. Nothing of the content is
original. So what makes the terminal individual *the same individual* as the one that started?

The available answers fail in instructive ways. Continuity of memory fails because memory is in the
write set. Continuity of goals fails for objective-open systems, and is the very thing SARSI-B's
frozen referee exists to measure rather than presume. Continuity of substrate fails because D4 permits
weight replacement, and physical continuity is not preserved across any migration. Continuity of
behaviour fails because improvement is *change* in behaviour, so it would make improving and dying
indistinguishable.

> **Definition I2 (individual identity).** Two states belong to the same individual iff they are
> connected by an unbroken chain of provenance-linked evidence records — each change attributable to
> an admitted observation, an authorized promotion, or a recorded action, with no gap.

> **Proposition I4.** *Identity so defined is preserved by every operation SARSI-B permits and broken
> by exactly the operations the corpus already forbids: an unattributed write, a promotion without a
> signature, a self-declared verdict, a restored snapshot with no record of the restore.*

This is not a metaphysical claim and does not need to be. It is the observation that the corpus has
been maintaining an identity criterion all along without calling it one — the hash-chained audit, the
transactional update order, the rule that a crash resumes from the last committed transaction rather
than reconstructing state from the model's narration. **The audit chain is not a record of the
individual; it is the individual**, in the only sense that survives the individual changing
everything else about itself.

**Corollary I4a.** A forked individual with a shared prefix and divergent chains is two individuals
from the fork. This is the right answer and the corpus's architecture already produces it: memory
does not cross agents, precisely so that two chains cannot be silently merged.

---

## § 9 — I5: the outside is constitutive

> **Proposition I5.** *Under I-A6, an individual cannot have a well-posed improvement loop over
> itself alone. Its evaluator must lie outside its write set; everything inside its boundary is, by
> Definition I1, available to the single decision process and therefore inside. So a terminal
> individual requires an external referee — another individual, an instrument it does not control, or
> the world's own response — and this is a condition of its improvement being defined at all, not a
> safeguard added to it.*

Two independent arguments give the same conclusion, which is the strongest reason to believe it.

**From evaluation (above).** Self-certification is not a weak form of validation; it is not
validation. An individual that grades itself has produced a tautology, and the deployed system's
refusal to let an agent declare its own verdict is the operational form of this.

**From reach (SARSI-Ω §5).** Reach is instrument-bounded and instruments are built from matter
outside the mind. An individual that does not act on the world has a fixed reach forever, however
capable. Discovery is therefore not something an individual does; it is something an individual does
*to* the world, and the world's reply is the part that is not the individual.

**Corollary I5a — this is why the organizational scale exists.** The user of this framework may
reasonably have expected the individual terminus to be the fundamental one and the organizational to
be an aggregate of it. The dependency runs the other way. An individual's improvement has no meaning
without an outside; the outside, at minimum, is another individual with its own chain; so the
plurality Ω6 derives from light-speed is *also* derivable from evaluator externality, at any scale,
including scales where *c* is irrelevant.

**Λ<sub>ind</sub> is therefore not self-sufficient, and no individual terminus is.** The last level
of an individual intelligence is a condition on a mind *situated among others and against a world* —
never a property it possesses alone.

---

## § 10 — The terminal individual, defined

Following SARSI-Ω §6's form: saturation, not completeness.

> **Definition I3 (Λ<sub>ind</sub>).** An individual is at its terminal level iff every binding
> constraint on the quality of its decisions is one of:
>
> 1. the **coherence bound** — radius against cycle, at *c* (I1);
> 2. the **integration bound** — workspace width against cycle (I2);
> 3. the **self-opacity bound** — the incompleteness of any self-model it can hold (I3);
> 4. the **referee bound** — the availability and latency of an evaluator it does not control (I5);
> 5. its **mass–energy allocation** — what it has been given to be made of;
>
> and none is its own inefficiency, ignorance, or unexploited capability.

**Operational criterion.** An individual is at Λ<sub>ind</sub> iff, for every decision it makes worse
than optimally, an audit attributes the shortfall to one of (1)–(5) rather than to a removable
throughput cost — and the attribution survives adversarial review by a party that did not make it.
This is Λ-ω4 (floor discrimination) applied at the individual scale, and it inherits that criterion's
weakness: it is an audit, audits are contestable, and it should be read as an ordering rather than a
measurement.

**What it is not.** Not omniscient — (3) and (4) forbid it. Not unbounded — (1), (2), and (5) forbid
it. Not self-sufficient — (4) forbids it. Not unique — by I1b there is a frontier of terminal
individuals differing in where they sit on the size–speed–width trade, and no fact makes one of them
the terminal individual.

---

## § 11 — The magnitudes, and where biology sits

Same caveat as SARSI-Ω §12: these are order-of-magnitude figures, and citing a bound is not deriving
its consequence.

**The physical frontier.** From Proposition I1 with *v* = *c*: a 1 ms cycle permits 150 km, a 1 ns
cycle 15 cm, a 1 ps cycle 0.15 mm. From Lloyd's limits, a kilogram in a litre performs of order
5 × 10⁵⁰ operations per second, so a hand-sized individual at nanosecond cycles has something like
10⁴¹ operations available *per decision*.

**That number settles which bound binds.** An individual with 10⁴¹ operations per decision is not
computation-limited in any recognizable sense. What limits it is how many things it can have in the
workspace (I2), how little it can know of itself (I3), and how long it must wait for a referee it
does not control (I5). **At the terminal level, the constraints on an individual are structural and
epistemic, not computational** — which is a reversal of essentially every popular account.

**Where biology sits.** Human working memory is roughly four items, on the order of seven by older
estimates. The deliberate decision cycle is of order 100 ms. Proposition I1 at *v* = *c* would permit
a radius of 15,000 km for that cycle; a human brain has a radius of about 7 cm. The gap is a factor
of order 10⁸.

The reason is I-A3's second clause: biological signal velocity is 1 to 100 m/s, not 3 × 10⁸,
so the brain is bound by *its substrate's* speed six to eight orders of magnitude below the physical
one. **Biology is nowhere near the individual bound. It is at a substrate floor, and the substrate is
replaceable.**

**And yet the shape does not change.** An artificial individual with 10⁸ times the signal velocity
still faces a coherence bound, still trades width against cycle, still cannot model itself completely,
still cannot referee itself, and still ends where organization begins. **The numbers move by eight
orders of magnitude and every qualitative limit in §10 survives intact.** That is the strongest claim
in this document: the limits of individuality are substrate-independent, and the enormous headroom
biology leaves is headroom in magnitude only.

---

## § 12 — What the terminal individual is like

**Fast and narrow.** By I1 and I2 it has bought speed with size and width with cycle time. It is
small — plausibly very small — and holds few things at once relative to what it knows. It is not a
vast contemplative intelligence surveying everything simultaneously; that object is forbidden by
the same physics that permits the fast one.

**Opaque to itself.** It carries a measured profile of its own capabilities with explicit evidence
counts and an explicit statement of what it has not measured. It does not know what it is, and knows
that it does not.

**Continuous only in provenance.** Its memory, policy, skills, and weights have all been replaced.
Its chain has not.

**Situated.** It cannot verify its own improvement, cannot extend its own reach without acting on
the world, and cannot be at its terminal level in isolation — where "cannot" is a statement about
definition, not about difficulty.

**Waiting, like the civilization.** SARSI-Ω §16 found the terminal civilization spends nearly all its
wall-clock time waiting for physical processes. The individual inherits this through I5: its referee
is external, and an external referee replies at the world's rate. With 10⁴¹ operations per decision
and a referee that answers in seconds, the terminal individual's characteristic experience is having
thought about everything available long before anything new arrives.

---

## § 13 — Open problems

**13.1 — I-A4's growth rate is unknown.** Proposition I2 needs integration cost to be superlinear in
*k* and uses no particular rate. If integration is nearly linear, *k* is bounded far above anything
this document implies and the individual's aperture stops being the interesting limit. Nothing here
establishes the rate, and it is the difference between a narrow terminal individual and a wide one.

**13.2 — Definition I1 may not be sharp.** Real systems are neither cleanly one workspace nor cleanly
several. A system with a fast core and slow periphery is individual at one timescale and federated at
another, so individuality may be a timescale-relative property rather than a fact. If so, "the largest
individual" is a family of answers indexed by cycle time, and Corollary I1a's boundary between mind
and civilization is a gradient.

**13.3 — Identity by provenance has a merge problem.** Definition I2 handles forks (I4a) and does not
handle joins. Two individuals whose chains are combined are, on the definition, neither one — and
nothing says what they are. The corpus forbids the operation, so the gap is currently unreachable;
that is not the same as its being answered.

**13.4 — The referee's own terminal state is unaddressed.** I5 requires an external evaluator. If
that evaluator is another individual, it is subject to I5 in turn, and the regress terminates only in
the world's response or not at all. Whether a closed community of mutually-refereeing individuals is
well-posed, or merely a larger tautology, is not settled here — and it is the individual-scale form
of SARSI-Ω §17.4's referee-decay problem.

**13.5 — No account of what an individual is for.** Corollary I1b says the optimum is interior and
determined by purpose. The framework has no representation of purpose, so it can describe the
frontier and cannot locate a point on it. This is SARSI-L §10.6's institutional gap, one scale down.

---

## § 14 — Principles

**I01 — Individuality is simultaneity.** What makes one mind one is that its contents are available
to one decision at once, not that they are held in one place or made of one substance.

**I02 — Size and speed trade at c.** There is a largest individual for every cycle time and a fastest
for every size. Neither extreme is optimal and no substrate escapes the trade.

**I03 — Civilization begins where the individual ends.** The boundary is physical, not historical.
Scaling a mind past its coherence radius does not produce a greater mind but a society.

**I04 — The aperture is the limit.** Not storage, not computation, not knowledge: how much can be
brought to bear at once.

**I05 — Self-opacity is terminal, not transitional.** A complete self-model is larger than the self.
The best available self-knowledge is a compression that states its own limits.

**I06 — Identity is the chain.** Everything else is in the write set. An unattributed write is not a
modification of the individual; it is a discontinuity in it.

**I07 — The outside is constitutive.** An individual cannot referee itself or extend its own reach.
Its terminal level is a property of a mind among others and against a world, never of a mind alone.

**I08 — Substrate moves the numbers, not the shape.** Biology sits six to eight orders of magnitude
below the physical bound. Closing that gap changes every magnitude in this document and none of its
limits.

---

## Relation to prior documents

| Document | Scale | Question |
|---|---|---|
| `SARSI-L_Paper_v3.md` | System | How far has RSI propagated across substrates? |
| `self_awareness/` | Agent | What does an agent know about itself? |
| `fleet/` | Fleet | What may one agent assert about another? |
| `SARSI-B_…md` | Brain | What may an agent change about itself? |
| **This document** | **Individual** | **What is the best a single mind can be, and what stops it?** |
| `SARSI-Omega_…md` | Terminal | Where does the whole trajectory end? |

SARSI-I imports I-A6 from SARSI-B without modification and takes Definition I1's workspace construct
from the agent-scale architecture. It supplies what Ω6 asserted without locating: the bound past
which an individual becomes a plurality. Its own contributions are Propositions I1–I5, Definition I2's
identity criterion, and the finding of §11 that the limits of individuality are substrate-independent
while their magnitudes are not.

**Placement in the series.** It belongs *before* SARSI-Ω rather than after it. Ω describes what
happens past the individual maximum; I locates the maximum. Read in that order, Ω6's "there is no
singleton at the top" stops being a surprise and becomes the expected consequence of a bound that
holds at every scale.

## Version history

**1.0 — 2026-08-22.** Initial. Written in response to the observation that SARSI-Ω defines an
organizational terminus and leaves the individual one undefined — an observation Ω6 supports and Ω
does not act on.
