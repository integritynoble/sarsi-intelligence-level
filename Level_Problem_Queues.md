# The Level Problem Queues

## Every individual level, every organizational level, and every circle — as rungs, in the order they must be solved

*2026-08-23*
*Format: the research-agent problem queue of `AI4Science/docs/research-agents/drug-design.md`*
*Levels from: `Two_Axis_Intelligence_Level_Framework_v2.md`, `SARSI-O_Organizational_Intelligence.md`, `Circles_and_Levels.md`*
*Current state from: `BrainRSI_Plan_As_Level_Build.md`, `Federation_Plan_As_Organizational_Build.md`, `SARSI_Applied_Profiles.md`*

---

## Why the levels are a queue

A research agent's problem queue states its field's open problems **in the order
they must be solved**, each with a backticked `solved when` that would settle it.
The levels have exactly that shape and are usually not written that way: a level
is described, and then a system is said to be at it.

Putting them in queue form forces the thing the corpus asks for everywhere else.
**A level with no measurement that would settle it is a research interest.** The
`solved when` column is where each rung becomes something a system can be wrong
about in public.

Three queues follow, and they are **not parallel**. The individual queue
saturates; the organizational queue does not; and the circles are indexed by
which of the two binds. That relation is §4.

> **A rung is closed by measurement, not by architecture.** "Solved" means the
> stated observation has been made by a party that did not perform the work.
> A system may propose that a rung is closed; the closing is evidence.

---

## Queue A — the individual ladder

| # | problem | **solved when** | why it is placed here | state |
|---|---|---|---|---|
| A1 | **I0 → I1 · durable state that is used** | `state written in an earlier session is recovered and demonstrably changes behaviour in a later one` | persistence is the only rung observable without a measurement, because it makes no improvement claim. It is first because everything above it operates on the record it accumulates | **done** — every shipping coding agent |
| A2 | **I1 → I2 · the memory ablation** | `matched tasks drawn from a held-out family score better with memory on than off, scored by a party that did not author the memory` | memory grows monotonically with history whether or not capability rises, so accumulation is evidence of operation. Placed second because it is the cheapest measurement on the entire map and it gates every claim above | **open — and nobody ships it.** The one-cell finding is this rung unclimbed |
| A3 | **I2 → I3 · mechanism separated from content, then changed** | `Θ_t+1 ≠ Θ_t, the change survives into later operation, and it passes an evaluation the agent did not run` | you cannot improve what is hard-coded, so the mechanism must first be pulled out of logic into versioned configuration. Needs A2, because a mechanism change judged against unablated memory is judged against noise | open — `Θ` is named and carved out in the BrainRSI plan; nothing proposes changes to it |
| A4 | **I3 → I4 · improvement competence rises** | `IC = validated downstream gain ÷ proposal-and-evaluation cost rises across generations, with the denominator reported` | the rung most often claimed from the wrong evidence. A rising task score is consistent with the improvement machinery staying exactly as good as it was; the denominator is what makes it honest. Needs A3 | open — the measurement is defined at M8 and has not been run |
| A5 | **I4 → I5 · structured ignorance represented** | `the agent identifies an unknown nobody handed it, designs discriminating evidence, and the resulting knowledge is validated by an instrument rather than by another member` | requires representing what is *not* known, not only what is. An agent with no model of its own ignorance can notice a retrieval gap and cannot identify a significant unknown | open |
| A6 | **I5 → IΩ · a frozen referee ladder** | `a retained, versioned record of objective revisions, each scored against its immediate predecessor, readable by a party that did not perform the revision` | last because it is the only rung that moves the objective, and without the ladder open-ended development and undirected drift are indistinguishable by any observation whatsoever | open — the director role is a human in every deployed configuration |
| — | **The coherence bound** | `R ≤ cτ/2` — **not a rung.** Nothing solves it | the individual axis terminates here and the available direction becomes O. Listed so that a reader does not treat A6 as the top of a ladder that continues | **bound** |

> **Blocked by, and unblocks.** The order *is* the dependency graph, and it is a
> chain rather than a lattice: each rung's evaluation is meaningless until the
> one below it has been measured. A2 is the exception worth naming — it is
> cheap, it is unclimbed, and **four heavily-compared products sit below it**.

> **Evidence that would reorder it.** A demonstration that mechanism changes can
> be validated without a clean memory baseline would move A3 above A2. Nothing
> currently suggests it, and the ordering is the corpus's weakest-argued claim
> because no one has tried to violate it.

---

## Queue B — the organizational ladder

| # | problem | **solved when** | why it is placed here | state |
|---|---|---|---|---|
| B1 | **O0 → O1 · persistence that survives turnover** | `shared state, roles, evidence and commitments survive sessions, restarts, and the departure of any single member` | first for the same reason A1 is: it makes no improvement claim and is directly observable | **done** — the OpenClaw federation is live with git-committed charter workspaces |
| B2 | **The separation gate** | `proposer, evaluator and promoter are distinct loci, and the evaluator's criteria and evidence lie outside the proposer's write set` | **placed before B3 rather than between levels, because it is not a level — it is the precondition on all of them.** An organization above O1 without it is recorded as *O1 plus unverified claims*, however rich its behaviour | **done, and enforced by file permissions rather than policy** — the strongest thing in the federation plan |
| B3 | **O1 → O2 · a measured reliability ledger** | `allocation changes on measured per-member per-task-class reliability, and the change improves outcomes against the previous allocation` | O2 requires collective history to *persistently change* allocation. Needs B2, or the improvement it reports is self-certified. The raw material already exists as registered-forecast-versus-outcome pairs | open — **one artifact away**, and the same artifact the individual queue needs |
| B4 | **O2 → O3 · routing policy versioned and improvable** | `the routing policy is versioned with rollback, candidates are generated over it, scored on a split held out from the candidates, and promoted through a gate the router cannot invoke` | the organizational form of A3, and it needs its own held-out set — a **third** distinct artifact, being task instances routed both ways | open — `manager` carries *"RSI only over routing policy"*, which is the write set correctly scoped and the loop absent |
| B5 | **O3 → O4 · improvement competence over the pipeline** | `the structure gets better at distinguishing good proposals from bad, per unit of review cost, measured across generations` | the organizational form of A4. Needs B4. This is the quantity that determines whether member capability converts into anything, and by Proposition O2 it is not a function of member level | open — M8 defines the measurement and scopes it to one agent |
| B6 | **O4 → O5 · knowledge no member holds** | `externally validated knowledge is produced that no single member could have produced, with the organizational contribution identified rather than assumed` | the identification clause is the whole rung. An organization whose output is its best member's output has coordinated, not discovered | partial — the research federation on real corpora, and the registry as shared apparatus |
| B7 | **O5 → OΩ · new organizational forms from discoveries** | `an accepted artifact repeatedly creates a new member with its own workspace and declared reach, and the additions expand what the organization can discover` | last because it presupposes the organization can already tell a good addition from a bad one, which is B2 through B5 | **the mechanism exists** — the market's manifest bridge — and the *repeatedly expands* clause is unmeasured |
| B8 | **Ω6 · protected exploration** | `exploratory diversity is preserved by mechanism — a protected branch, novelty budget, or maintained alternative that acceptance cannot retire` | **not above B7 but beside it.** The OΩ paper retains Ω6 as an axiom rather than deriving it, because nothing else prevents an adaptive organization from converging under optimization | **open, and countervailed** — the economy pays authors for accepted *and used* listings, which is a revenue gradient toward convergence with nothing pointing away |
| B9 | **T_δ · the rate** | `authorization latency computed from timestamps, censored observations kept, sub-floor intervals excluded and reported separately` | **not a rung and gates nothing — it bounds the rate of every rung above.** Placed last because it is orthogonal, and stated because ρ_max = 1/T_δ once the automated steps are cheap | **open. Never observed** — six documents ask for it; the promotions table has no timestamp column |

> **Blocked by, and unblocks.** B2 is the gate: every rung above it is void
> without it, which is why it is written as a gate and not as a level. B8 and B9
> are the two entries that are not rungs, and both are placed deliberately —
> one because nothing else protects it, the other because nothing else bounds
> the rate.

> **Evidence that would reorder it.** A working demonstration that a
> mechanically restricted capable member satisfies separation as well as
> structural differentiation would move B2 from a precondition to a design
> choice. That is the open problem at `SARSI-O` §9.3 and it is the alignment
> question wearing organizational clothes.

---

## Queue C — the circles

The substrate domains, with each circle's rung being the closure of its own loop
⟨ι identify, μ implement, ν validate, δ deploy⟩. What differs between them is
**which axis binds**, and the answer is rarely the individual one.

| # | problem | **solved when** | why it is placed here | state |
|---|---|---|---|---|
| C1 | **Circle I · software** | `ι, μ, ν and δ all run without approval, with δ included and non-negotiable` | first because every other circle requires it and it requires none of them. Its ι is satisfied at I3–I4 and its binding step is δ, which is **authorization rather than capability** — so closure here is an O-move, not an I-move | open. **The only circle whose floor is throughput and therefore removable across the board** |
| C2 | **Circle II · hardware** | `a fab process is qualified and its drift corrected without human coordination` | the design half is I2–I3 and approaching maturity; the manufacture half is a building, a supply chain and contamination control at nanometre tolerances — coordination among many actors over months, which is O-work by definition. **A more capable designer does not qualify a fab** | open — minimum I2–I3 / O3–O4, plus a physical floor |
| C3 | **Circle III · physical** | `a machine mines, refines, fabricates its own control electronics and assembles a working copy, with the replication recorded as a lineage event with provenance` | placed after C2 because the II↔III dependency is a bootstrap rather than a deadlock, advancing at the slower of the two physical periods. **Both rungs are O-work, so no increase in individual level moves the ladder at all** | open — minimum I2–I3 / O4–O5. **Floor: physical. Not removable** |
| C4 | **Circle IV · biological** | `a hypothesis about a biological mechanism is generated, tested, and validated to an endpoint` | **the only circle whose ι genuinely requires I5**, and its ν is irreducibly external twice over — once for evaluator separation and once because the regulatory structure requires a human principal investigator | open. Physical floor of 5–8 years, compressible by no level on either axis |
| C5 | **Circle V+ · stellar** | `collection area rises faster than maintenance and failure losses, sustained` | last, and **it has no I-coordinate at all.** A swarm at 1 AU is ~16.6 light-minutes across, so by R ≤ cτ/2 no single decision locus of that radius exists. It is not a mind with distributed parts; it is a civilization | open — minimum O4. **Purely an O-problem, by physics** |

> **The ι column stops rising and then falls.** Circles II, III and V+ demand a
> *lower* individual level than Circle I. Chip specification, machine design and
> collector design are ordinary engineering cognition; what is hard about those
> circles is everything after ι. **You cannot buy an outer circle with a smarter
> individual.**

> **C4 is off the critical path.** It requires Circle I, does not require Circle
> III, and Circle V+ does not require it. So the circle that most demands a high
> individual level contributes least to the trajectory — **the top of the I-axis
> is stranded on a branch.**

---

## § 4 — How the three queues relate

They are usually drawn as parallel ladders. They are not.

**Queue A saturates and Queue B does not.** Reading the circles' closure
criteria against the level definitions, the individual requirement peaks at
Circle I and then *declines*, while the organizational requirement climbs
monotonically to the outermost domain. That asymmetry is why substrate is the
right index: **outer substrates shift the load from the individual axis to the
organizational one.**

**No circle's closure criterion requires IΩ.** Not one. The top of Queue A is
not on the path to the top of Queue C.

**Two of four loop steps are organizational in every circle.** Validate is
organizational by necessity — an evaluator inside the write set is not an
evaluator — and deploy is organizational always. So **no individual level closes
any circle alone**, at any point on Queue A.

**The intelligence-explosion argument is a Circle I argument.** A machine
improving its own cognition is A3 → A4, an individual-axis claim. It is silent
about circles whose binding steps are organizational and physical.

### 4.1 The two cheapest unclimbed rungs

Worth isolating, because the queues are long and these two are not expensive.

**A2, the memory ablation.** Same task family, same budget, memory on versus
off, held out from the episodes that produced the entries. It is an afternoon of
evaluation engineering. It gates every rung above it on Queue A, and four
heavily-compared products sit below it because none of them publishes it.

**B9, T_δ.** Timestamp candidate-available and promotion-signed. It bounds the
rate of every rung on Queue B. Six documents in this corpus ask for it and it
has never been observed — not because it is hard but because the promotions
table has no timestamp column.

> **The failure these queues are built against is a programme that climbs the
> ladder it can climb alone.** Queue A can be worked by one team on one system;
> Queue B needs a structure and Queue C needs the world. Given a free hand, the
> cheapest defensible year is spent on Queue A — and by §4 that is the queue
> that saturates, on the axis that stops binding after the first circle.

---

## § 5 — What these queues do not tell you

**Where any system currently sits.** The `state` columns are read off designs
and reports, not measured. Every axis in this corpus is an ordering and not one
is a measurement, and these queues inherit that entirely.

**How long a rung takes.** No rung here carries an estimate. The corpus's
timelines are four-scenario ranges conditioned on stated critical-path
conditions, and a queue that attached durations to rungs would be asserting
something the framework declines to assert.

**Whether the rungs should be climbed.** The frameworks describe a frontier and
have no representation of purpose or of institutions, so they can state the
trade-offs and cannot pick a point. Queue C in particular describes capabilities
whose desirability is not a question any measurement in this corpus answers.

**Whether the orderings are right.** Each queue states the evidence that would
reorder it, which is the most that can be offered for a ladder nobody has yet
tried to violate. **A ladder nobody can argue with is a ladder nobody checked.**
