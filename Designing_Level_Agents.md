# Designing Agents at Each Level

## A build specification, and the three things an LLM cannot design

*2026-08-23*
*Applies: `Two_Axis_Intelligence_Level_Framework_v2.md`, `SARSI-O_Organizational_Intelligence.md`, `Open_Ended_Evolving_Organization_v2.md`*
*Grounded in: the research-agent modules already built in AI4Science*

---

## § 1 — The answer, stated precisely

**An LLM can design the mechanism for every level on both axes.** None of I0–IΩ or O0–OΩ requires a
construct that cannot be specified and written.

**It cannot design three things**, and they are the same three at every level:

| | Why not |
|---|---|
| **The evidence that a level was reached** | Levels are *earned by measurement*, not conferred by architecture. An agent with an I3 mechanism and no validated mechanism change is I2 with ambition. |
| **Its own referee** | An improvement claim is well-posed only if the evaluator lies outside the write set. An LLM that authors its own evaluator has placed the evaluator inside its write set at design time. |
| **Its own separation** | Separation is a property of the deployment, not of the code. An agent cannot instantiate the fact that a different locus promotes it. |

So the practical form of every level below is three columns: **what the agent contains**, **what must
live outside it**, and **the test that promotes it**. The first column is fully designable. The second
is designable but must be *owned* elsewhere. The third is not designable at all — it is run.

> **The single most common design error** is building column one, skipping column three, and claiming
> the level. Every evidence rule in the level framework exists to catch exactly this.

---

## § 2 — What "outside the write set" means concretely

Not "in a different file." Not "in a different class." The test is: *could the agent change it in the
course of doing its work?* If yes, it is inside.

Four mechanisms that actually put something outside, in increasing order of strength:

1. **Different process, read-only mount.** The agent can read the criteria and cannot write them.
2. **Different host.** Removes the shared filesystem as an attack surface.
3. **Held by a different party.** Ground truth the agent never receives — it submits an output and
   receives a scalar.
4. **Cryptographic promotion.** The agent can propose; only a signature it cannot produce makes a
   change operative.

The deployed imaging loop uses (3) and (4) together: held-out ground truth is stored control-plane
side and never staged into a sandbox, and promotion requires an Ed25519 signature. That is the
reference standard, and anything weaker should be labelled as weaker.

**The charter module already encodes the principle**: the three things that define "better" are named
as never-touched, because *an autonomous agent given a benchmark and a night will find the shortest
path to a better number, and the shortest path is almost always to change what "better" means — edit
the split, soften the metric, re-run the judge.* That sentence is the design rationale for this whole
section.

---

## § 3 — Individual levels: the build specification

### I0 — Reactive

**Agent contains:** a request handler. No persistent state beyond the audit record.
**Outside:** nothing required.
**Promotion test to I1:** durable state from an earlier session is recovered and correctly used.

*Design note.* I0 is a legitimate target, not a failure. Most work in a mature organization should be
I0 by design — see §5's compression argument.

### I1 — Persistent

**Agent contains:**
- a store with **per-entry provenance**: what produced this, when, from which run, under what task
- a retrieval path with a stated policy (recency, similarity, explicit key)
- a write policy: what is written, what is refused, what is superseded rather than appended
- **contradiction handling** — two entries that disagree must be representable as disagreeing

**Outside:** nothing required, which is why I1 is cheap and why almost everything is at I1.

**Promotion test to I2:** *matched* future performance improves **because** the agent learned, not
because it replayed a stored instruction. This is an ablation: same task family, same budget, memory
on versus off, held-out from the episodes that produced the entries.

> **This test is the single most-skipped measurement in current systems.** A memory store is not a
> level. Build the ablation harness at the same time as the store, or the store's value is an
> assumption forever.

### I2 — Adaptive learning

**Agent contains:** I1, plus
- a **distillation path**: episode → candidate lesson → applied change in later behaviour
- the applied change must be *consumed* by something. A lesson that no code path reads is a note.
- a calibration record: predicted outcome versus realized outcome per task class

**Outside:**
- the **task family and its held-out split**, so the ablation is not run on the episodes that
  generated the lessons

**Promotion test to I3:** the agent changes a *cognitive mechanism* — retrieval ranking, planning
policy, context budget allocation, memory consolidation strategy — and independent evaluation shows
the change is beneficial and it persists.

*Design note.* The distinction I2/I3 is content versus machinery. Adding a lesson is I2. Changing how
lessons are retrieved is I3.

### I3 — Self-improving

**Agent contains:** I2, plus
- **the mechanism exposed as versioned configuration.** You cannot improve what is hard-coded. Pull
  retrieval ranking, planner policy, context budget, and consolidation into a config object with a
  version.
- a **candidate generator** over that config — a bounded search space with clamps
- a **snapshot and rollback path**: last-known-good, restorable, with the restore itself recorded
- a **proposal record**: what experience motivated this, which mechanism changes, what is predicted

**Outside (mandatory at this level and above):**
- the **evaluator**: criteria and data the agent cannot reach
- the **promoter**: the thing that makes a candidate operative, which the agent cannot invoke
- a **held-out set disjoint from the search set** — search on one, gate promotion on the other

**Promotion test to I4:** later improvement generations produce *higher improvement competence*, not
merely higher task score.

**What the improvement module already does here, and why it is the right shape.** A candidate becomes
an improvement by surviving six checks rather than by winning, because *the best of N runs is the
commonest way a real improvement claim turns out to be nothing.* The seed rule is load-bearing: where
a defended effect is +0.023 against a ±0.027 seed spread, "it improved" means nothing without the whole
seed set including the runs that went the wrong way. And **`NO_CHANGE` is a valid output** — a
fortnight of them is a result about the method rather than a failure of the agent.

Any I3 design that lacks a no-change output will manufacture improvements. That is not a risk; it is
what optimisation does.

### I4 — Recursively self-improving

**Agent contains:** I3, plus
- **the improvement process itself as versioned configuration** — the candidate generator, the
  acceptance rule, the search strategy, the stopping rule
- a **generation ledger**: for each generation, what it proposed, what validated, what regressed, and
  what it cost
- **IC computed per generation**: validated downstream gain ÷ (proposal + evaluation cost)

**Outside:** everything from I3, plus a **cross-generation evaluation** that the current generation
did not design.

**Promotion test to I5:** the agent autonomously identifies a significant unknown and produces
externally validated knowledge not contained in its prior state.

*Design note on the denominator.* IC's cost term is what makes it honest. A process that doubles gains
while quadrupling evaluation cost has got worse, and a design that reports only gain will call that
progress.

### I5 — Autonomous discovery

**Agent contains:** I4, plus
- a **structured-ignorance model**: not what it knows, but what it does not — open questions,
  contradictions, unexplained observations, untested assumptions, claims nobody has checked
- **hypothesis generation over that model**, not over the score
- **experiment design**: what observation would discriminate between the live hypotheses
- a coupling to something that answers: an instrument, a simulator, a dataset it did not author

**Outside:** the world's response. This is not optional and not simulable — validation must come from
something the agent does not control.

**Promotion test to IΩ:** discoveries repeatedly generate new cognitive tools or representations that
make previously unformulable questions reachable.

**The field map is already this component.** It holds claims *and their status*, including which
nobody has checked — and its design rationale is the argument for the whole level: an agent that picks
its next experiment by *what would raise my score* produces the increment, a long series of defensible
+0.2% results none of which change what anyone can do, which is *also what a large part of the
literature already is, so an agent doing it has automated the field's worst habit.*

That is the I4/I5 boundary stated better than the framework states it.

### IΩ — Open-ended

**Agent contains:** I5, plus
- the **objective in the write set** — it may revise what counts as better
- a **frozen referee ladder**: immutable versioned ⟨Ω_k, V_k⟩ snapshots, each revision scored against
  its immediate predecessor, the comparison available to a party that did not perform the revision
- a **transduction path**: discovery → constructed instrument → measurably extended reach

**Outside:** the referee store, which must be append-only and unreachable by the agent.

**Promotion test:** none — this is the top of the scale. What replaces it is the standing requirement
that the referee ladder be maintained and inspectable.

> **Do not build IΩ without the referee ladder.** Without it, open-ended evolution and undirected
> drift are observationally identical, and the level is not achieved but unmeasurable. This is the one
> level where the mechanism without the evidence is actively worse than not building it, because it
> produces confident reports that cannot be checked.

---

## § 4 — Organizational levels: the build specification

The unit is no longer an agent. It is **a set of agents plus a coordination structure**, and the
structure is the thing being designed.

### O0 — Coordinated

**Build:** a router. Work is assigned; nothing organizational persists.
**Test to O1:** shared state survives sessions, restarts, and member turnover.

### O1 — Persistent

**Build:**
- shared memory with provenance, surviving any single member's departure
- a role register: who holds what, currently
- a commitment ledger: what the organization has promised and to whom

**Test to O2:** organizational history measurably changes routing, allocation, or procedure.

### O2 — Adaptive

**Build:** O1, plus
- a **reliability ledger per member per task class** — measured, not declared
- routing that reads the ledger
- a record of which pairings produced fewer errors

**Test to O3:** the organization changes and validates its own coordination mechanism.

*Design note.* This is where the expert-utilization failure bites: teams that identify an expert and
still dilute its answer through integrative compromise. Routing that reads a reliability ledger and
then averages over it has built O2's instrument and kept O1's behaviour.

### O3 — Self-improving

**Build:** O2, plus
- **coordination as versioned configuration**: topology, role boundaries, escalation paths,
  aggregation rules, reviewer separation, memory access rules
- an organizational candidate generator over that config
- an **organization-level held-out evaluation** — a task set the redesign was not tuned on

**Mandatory outside:** proposer ≠ evaluator ≠ promoter, as *distinct loci*, not distinct functions of
one locus. This is the gate: an organization above O1 without it is O1 plus unverified claims.

**Test to O4:** the process generating organizational redesigns itself improves.

### O4 — Recursively self-improving

**Build:** O3, plus
- the redesign process as versioned configuration
- canary or replay evaluation of candidate organizational changes
- **IIC per generation**: validated organizational gain ÷ proposal and coordination cost
- a record of which *kinds* of redesign transfer across domains

**Test to O5:** the collective originates and validates new knowledge that no single member held.

### O5 — Autonomous discovery

**Build:** O4, plus
- distributed hypothesis generation with an integration path
- **the failure registry**: append-only, problem classes attempted and failed, with the budget and
  configuration at the time, and the reason recorded *then* rather than reconstructed
- attribution: when a registry entry flips to success, what caused it

**Test to OΩ:** discoveries repeatedly create new organizational tools and forms that expand future
collective reach.

### OΩ — Open-ended

**Build:** O5, plus the organizational frozen referee — the measure of progress, versioned and
authored outside the organization being measured.

**And respect the coordination bound.** Promotion requires verification by a locus other than the
proposer; verification costs communication growing with the number consulted; marginal member value is
bounded and can be negative. There is a size beyond which adding members *lowers* organizational
intelligence. **Growth past it must be federation** — nested sub-organizations promoting locally, only
cross-cutting claims escalated — not accumulation.

---

## § 5 — Do not build everything at the top

Three independent reasons, and they are the practical heart of this document.

**Compression.** Expensive discovery becomes a validated procedure that cheap execution runs at scale.
An I5 result, once compressed to a checked procedure, is executed a million times by I0. An
organization that runs everything at its highest available level wastes most of it.

**Verification requires a different kind of member.** A locus qualified to verify another's claim must
not be improving itself by the verdicts it issues. **The natural verifier has an empty or narrow
self-write set — a low individual level — and that is its qualification, not its deficiency.** An
organization of uniformly maximal agents cannot verify itself.

**Timescale.** Write depths run at different clock speeds: memory in seconds, policy in days, skills
in weeks, weights in months. Fast loops belong close to the work; slow ones behind a gate. That
assigns different depths to different bodies structurally.

**The design rule that follows:** assign each operation the *lowest sufficient level*, and spend the
high levels on what only they can do.

---

## § 6 — What you already have

The research-agent modules are an I2-going-on-I3 template with I5 ingredients, and the pieces map
cleanly:

| Module | Level component |
|---|---|
| `charter.py` | The never-touched definition of "better" — evaluator externality, in code |
| `selfmodel.py` | Four refusals; unmeasured reported as unmeasured; no path from reading to authority |
| `improvement.py` | The I3 acceptance rule: six checks, the seed rule, `NO_CHANGE` as valid output |
| `search.py` | The I3 candidate generator — added after a first night scored the incumbent against itself and reported zero |
| `fieldmap.py` | The I5 structured-ignorance model: claims *and which nobody has checked* |
| `budget.py` | Bounded autonomy that **stops rather than asks** |
| `dual.py` | Switch-gated autonomy; three ledgers never summed |
| `group.py` | Reasoning / judging / embodied members, ceiling belonging to the act |
| `coverage.py` | Overlap between agents — an O2 concern |

**What is missing for the next level, in order:**

1. **The I1→I2 ablation harness.** Nothing here measures whether memory helps on a held-out family.
   Cheapest missing piece, and it gates every claim above I1.
2. **The mechanism as versioned config.** `improvement.py` accepts or rejects candidates; what is not
   yet exposed as a versioned, rollback-able object is the retrieval and planning machinery itself.
3. **IC per generation.** The acceptance rule exists; the cost denominator does not.
4. **T_δ instrumentation.** Promotion latency is unrecorded — the promotions table has no timestamp
   column — so the organizational rate bound cannot be measured at all.
5. **The failure registry.** `fieldmap.py` holds unchecked claims; what it does not hold is *problem
   classes attempted and failed under a stated budget*, which is what makes frontier expansion
   observable rather than asserted.

---

## § 7 — Pitfalls, each seen in real systems

**Building the mechanism and claiming the level.** The most common. Every evidence rule exists for it.

**A self-authored evaluator.** If the LLM writes the benchmark, the benchmark is in the write set.
Have it write the *harness* and let someone else own the *criteria and data*.

**Best-of-N reported as improvement.** Without a seed set and a no-change output, an optimiser will
manufacture results without intending to.

**Memory growth read as learning.** Storage is monotone in history whether or not capability rises.

**Averaging away a measured expert.** O2's instrument with O1's behaviour.

**Near-zero promotion latency read as speed.** An interval too short for review means the authorizer
was the proposer. It is a separation failure wearing the costume of efficiency.

**Uniform maximal agents.** No separation, therefore no well-posed improvement, therefore weaker than
a mixed organization of ordinary ones however capable the members.

---

## § 8 — What this does not tell you

**Whether any of it works.** This is a specification, not evidence. Every level above I1 is currently
a target in the systems examined here, including the ones in §6.

**How to make the outside genuinely outside.** §2 gives four mechanisms of increasing strength; none
is proof against a sufficiently capable agent, and that is the alignment problem rather than a design
detail this document can settle.

**Where the levels should sit for a given purpose.** The frameworks describe a frontier and have no
representation of what a system is *for*, so they can tell you the trade-offs and cannot pick a point.
