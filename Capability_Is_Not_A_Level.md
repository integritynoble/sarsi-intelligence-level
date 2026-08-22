# Capability Is Not a Level

## A Structural Taxonomy of Individual and Organizational Intelligence, with Placements for Current AI Agents

*Draft 1.0 — 2026-08-22*
*Markdown edition. No LaTeX source or arXiv package is built for this paper.*

---

## Abstract

Taxonomies of machine intelligence are almost universally ladders: ordered levels along which a
system advances as it becomes more capable. We argue this is the wrong object. The level of an
intelligence is jointly determined by what persistent state it is permitted to modify, who evaluates
the modification, and the structure it is embedded in — and the second and third of these are not
properties of the system at all.

We develop the consequences at two scales. For an **individual** — defined as a system with a single
global workspace, which draws the individual/organizational boundary physically rather than by
convention — we give a taxonomy indexed by *write set* rather than by capability, and a well-posedness
condition: an improvement loop is defined only if its evaluator lies outside the write set. Five
physical bounds on individuality follow, including a coherence bound *R* ≤ *cτ*/2 that establishes a
largest possible individual for any decision speed, so that scaling a mind past it yields a society
rather than a greater mind.

For an **organization** we give five axes, none of which is a capability of any member, and two
results. Organizational intelligence is **not monotone in member capability**: a structure that does
not separate proposer from promoter from referee has no well-posed improvement loop however capable
its members. And levels **necessarily coexist**, forced by four independent arguments — so a
hypothetical organization of uniformly maximal minds is not the strongest configuration but a
degenerate one.

We place five current agent systems and one platform on the resulting map. The principal empirical
finding is that four widely-compared coding agents — differing substantially in capability — occupy
**the same cell on every axis**, because none of them writes itself: they modify external software,
which is reach into the world rather than depth into the self. The difference that would move any of
them is a held-out evaluation of their own configuration, which none ships.

We are explicit that the map does not predict performance. It is a semantics for improvement claims,
not a benchmark, and §8 states what it therefore cannot do.

**This paper is a companion to a two-axis (I, O) taxonomy developed independently and in parallel**
(*A Two-Axis Intelligence Level Framework for AI Agents*, 2026), which we take as the primary scale.
That framework indexes an individual by the deepest layer it changes through experience and a
collective by what it changes about its own coordination. We adopt its coordinates and supply four
things it does not carry: a derivation of why an external evaluator is required rather than advisable,
physical bounds that give its individual axis a ceiling, an identity criterion for the lineage its
higher levels presuppose, and a measurement of the quantity that bounds every compensated loop's rate.
`Two_Axis_Concordance.md` maps the two in full, including two substantive disagreements.

---

## 1. Introduction

### 1.1 The question

"How intelligent is this system?" is asked of AI systems continuously and answered with a scalar or a
rung: a benchmark score, a tier, a generation number. The practice is old and mostly imported. It
works well in the settings it came from, and this paper is about why those settings are not this one.

The question we ask instead is narrower and, we will argue, prior: **when a system says it has
improved, what has to be true for that to mean anything?** The answer turns out to constrain what a
level can be, and the constraint is severe enough to rule out the ladder.

### 1.2 What single-ladder taxonomies assume

Every ordered-level taxonomy of automation or intelligence makes three assumptions, usually silently.

**That the task is fixed.** SAE J3016's driving levels work because the task — get the vehicle from A
to B safely — does not change between levels. Only the division of labour does. Where the task is not
fixed, "more automated" has no single meaning.

**That capability and permission move together.** A higher rung means both *can do more* and *is
allowed to do more*. In a certified, regulated setting this is reasonable, because the certification
is what couples them. In an unregulated one it is an assumption, and §3.4 argues it is a harmful one.

**That the system is the unit.** A level is assigned to the artifact. This presumes that everything
relevant to the assignment is inside the artifact's boundary. §4.2 shows that at least two of the
determinants are not.

The first assumption fails for general-purpose agents by construction. The second and third fail
whenever the system is embedded in an organization that evaluates it, which is every deployed case.

### 1.3 Contributions

1. **A physical criterion of individuality** (§3.1). An individual is a system with one global
   workspace. This draws the individual/organizational line by a property rather than by convention,
   and yields the coherence bound *R* ≤ *cτ*/2 (§3.5): there is a largest possible individual at any
   decision speed, and past it there is no greater mind but a society.
2. **A write-set taxonomy** (§3.2–3.3) indexed by which persistent state a loop may modify —
   depth D0–D4, objective openness, and reach — replacing capability as the index.
3. **A well-posedness condition** (§3.4). An improvement loop is defined only if its evaluator lies
   outside its write set. This is what makes "improvement" a predicate rather than a report, and it
   is the paper's load-bearing claim.
4. **Five organizational axes and two results** (§4). Organizational intelligence is non-monotone in
   member capability (§4.3), and levels necessarily coexist (§4.5).
5. **An empirical placement** (§6) of five agent systems and one platform, with a provenance table
   stating what was inspected for each, and the finding that four heavily-compared systems occupy one
   cell.
6. **A first measurement** (§6.6) of authorization latency on a deployed system, which finds the
   quantity has never been observed and that its system of record cannot represent it.

### 1.4 What this paper does not claim

**It does not predict performance.** Two systems in the same cell can differ enormously in output
quality. The map measures what an improvement claim means, not how good the system is. Treating it as
a benchmark would be a category error and §8 returns to this.

**It offers no measurement.** Every axis here is ordinal. None has a validated protocol, and §8.1 is
specific about which are worst.

**It says nothing about consciousness, sentience, or moral status.** The individuality criterion in
§3.1 is functional and deliberately so; whether a system with one global workspace has experiences is
a real question and not this one.

**It is not a safety proposal.** Several results have safety implications and we note them, but the
arguments are about definedness, not about risk, and would hold in a world with no risk at all.

---

## 2. Related work

**Levels of automation.** Sheridan and Verplank (1978) introduced the canonical ten-level scale for
human–computer control allocation, and SAE J3016 is its best-known descendant. These are ladders in
the strict sense and appropriate to their settings, which satisfy §1.2's first assumption. Our
disagreement is about scope, not about correctness.

**Levels of AGI.** Morris et al. (2024) is the closest prior work and the most careful. It replaces
the single ladder with a matrix of performance against generality, and — importantly for us —
separates a *Levels of Autonomy* dimension from capability, observing that the two need not advance
together. We adopt that separation and push it further: their autonomy dimension is indexed by the
human–AI interaction mode, whereas ours is indexed by the write set and the location of the evaluator.
The difference is consequential. Interaction mode is observable from the interface; write set and
evaluator location are observable only from the architecture, and it is those that determine whether
an improvement claim is well-posed.

**Two-axis level taxonomies.** The framework closest to this one is a two-axis (I, O) scale
developed in parallel with it, which classifies an individual by the deepest layer it can change
through experience — reactive, persistent, adaptive-learning, self-improving, recursively
self-improving, autonomous-discovery, open-ended — and a collective by what it changes about its own
coordination and discovery. We treat it as primary and this paper as its companion. Its
persistent/adaptive-learning boundary is finer than the write-set depth used in §3.2, and its
transition test for that boundary — *does matched future performance improve because the agent
learned, rather than merely replaying stored instructions* — is the ablation §3.4 identifies as
missing, stated as a level boundary rather than as a complaint. We adopt it. Its *improvement
competence* metric, validated downstream gain per unit of proposal and evaluation cost, is the
operational measure §3.2 lacks for whether a deeper loop earns its cost.

**Formal definitions of intelligence.** Legg and Hutter (2007) define universal intelligence as
expected performance across a weighted class of environments — an explicitly scalar quantity. Chollet
(2019) argues that skill is the wrong measure and relocates it to skill-acquisition efficiency. We are
sympathetic to Chollet's move and differ in kind: he relocates the scalar, we argue that for *levels*
there is no scalar to relocate, because two of the determinants are outside the system. Both prior
definitions are answers to "how capable," and §1.1's question is not that.

**Forms of superintelligence.** Bostrom (2014) distinguishes speed, collective, and quality
superintelligence. Our individual/organizational split is a sharpening of the quality/collective
distinction, with the boundary made physical rather than descriptive: §3.5's coherence bound says
where quality superintelligence must become collective superintelligence, and that it must.

**Recursive self-improvement.** Good (1965) established the intelligence-explosion argument;
subsequent treatments largely restate it. Amdahl's (1967) parallel-speedup bound transposes to loop
autonomy and is used in §4.2. Von Neumann (1966) supplies the self-replication criterion referenced in
§3.2's deepest level.

**Cognitive architecture.** The global workspace construct is Baars' (1988), developed experimentally
by Dehaene and colleagues. Working-memory capacity estimates come from Miller (1956) and Cowan (2001).
We use the construct functionally and make no claim about its adequacy as a theory of consciousness.

**Regulators and models.** Conant and Ashby (1970) — every good regulator of a system must be a model
of that system — is the ancestor of §3.5's self-opacity bound, and Ashby's (1956) law of requisite
variety is the ancestor of §4's coverage axis.

**Physical limits.** Landauer (1961), Bekenstein (1981), Margolus and Levitin (1998), and Lloyd (2000,
2002) supply the magnitudes in §3.5. Dyson (1979) and Krauss and Starkman (2000) bound the total
computation available to any future observer; we use the latter only to note that the terminal state
is a finite budget, and do not develop it.

**Civilizational scales.** Kardashev (1964) indexes civilizations by energy. §4.6 argues energy is an
indicator of a terminal state rather than constitutive of it.

---

## 3. Individual intelligence

### 3.1 What makes something one individual

The distinction between an individual and an organization cannot be drawn by capability, size, or
substrate: an organization can exceed an individual on all three. We draw it by the structure of
decision.

> **Definition 1 (individual).** An intelligence is **individual** iff it possesses a *single global
> workspace*: a bounded set of at most *k* items simultaneously available to one decision process,
> such that every action it takes is selected from one state by one process.

Two systems exchanging messages are two individuals **however tightly coupled**, because each selects
its own actions from its own state. One workspace is one individual **however physically
distributed**, because there is one state and one selection.

Three consequences. Individuality is about *simultaneity*, not capacity — a store of arbitrary size
consulted serially is an instrument the individual uses, not part of the individual. Individuality has
no internal politics: parts of an individual do not negotiate or hold separate authority, and the
moment they do the object is an organization. And individuality is therefore expensive in a way
organization is not: an organization grows by adding parts, an individual only by making more
available to one moment.

### 3.2 The write-set axis

Let the persistent state of an intelligence be *B* = ⟨θ, M, Π, Σ, Ω⟩ — weights, memory, policy
(prompts, parameters, thresholds), skills (tools and constructed capability), and objective (the
target together with the evaluator *V*). An improvement loop over *B* is the standard ⟨identify,
implement, validate, deploy⟩, and its **write set** *W* ⊆ *B* is what it may modify.

> **Definition 2 (depth).** The **depth** *D* of a loop is the deepest element of *B* in its write
> set: **D0** nothing persists · **D1** memory · **D2** policy · **D3** skills · **D4** weights.

Depth is **coarse at D1**, and the two-axis scale's persistent/adaptive-learning split is the better
construction there: writing memory and behaving measurably differently because of it are separate
states, and only the second is learning. D1 as defined here covers both, and where the distinction
matters we use the finer boundary.

Otherwise depth is not a ranking of sophistication. It is a statement about which substrate a change reaches,
and it has a direct consequence for gating: loop period and per-iteration gain both rise with depth,
from memory in seconds through policy in days to weights in months. A well-formed system therefore
runs **all depths concurrently**, at different clock speeds, with gate strength monotone in depth. A
system running only one depth fails predictably — shallow-only accumulates without consolidating,
deep-only cannot adapt within a task.

We note the correspondence to biological memory consolidation timescales without leaning on it. The
argument for the ordering is that a substrate expensive to reverse must be slow to change, which holds
regardless of substrate.

### 3.3 Openness and reach

> **Definition 3 (openness).** A loop is **objective-closed** iff Ω ∉ *W*, **objective-open** iff
> Ω ∈ *W*.

Openness is not a depth. A prompt-level system that edits its own success criterion is open; a
weight-updating system trained against a fixed benchmark is closed.

> **Definition 4 (reach).** The **reach** of a loop is (*W*<sub>self</sub>, *W*<sub>other</sub>): what
> it may write in its own state, and in another intelligence's.

Other-reach is bounded to another intelligence's *inputs* — tasks, candidates, evaluations, verdicts —
and never to its state. §4.4 gives the reason, which is that permitting the state write reintroduces a
feedback coupling whose removal is what makes a multi-agent system verifiable agent by agent.

**A level is the triple** ⟨*D*, open/closed, reach⟩, reported alongside the authority ceiling that
gates deployment. Not a rung.

### 3.4 The well-posedness condition

> **Proposition 1.** *Let a loop have write set W, candidate generator ι, and evaluator V. The
> predicate "this iteration improved the system" is well-defined only if V ∉ W and V is not a function
> of ι. If V ∈ W, the loop can satisfy any improvement criterion by editing the criterion, and no
> observation distinguishes improvement from redefinition.*

The proof is immediate; what matters is what it explains and forbids.

**It explains why objective-open systems resist definition.** Not vagueness: "improvement" is not a
predicate over a system whose success criterion is part of what changed. The condition can be
recovered, at a price — retain an immutable ⟨Ω₀, *V*₀⟩ outside the write set and require the revised
system to score at least as well on *V*₀ as the unrevised one would have. This *frozen referee* makes
goal revision measurable. It also decays: the older the referee, the more the test asks whether the
new system solves the old problem, so referees must be versioned and laddered, each revision judged
against its immediate predecessor. That bounds the *rate* of drift and makes it visible; it does not
bound its extent.

**It forbids self-certification, and self-certification is not weak evidence but none.** A system that
proposes, judges, and adopts has reported a tautology regardless of its capability.

**It implies memory growth is not improvement.** *M* grows monotonically with history under any write
policy, so growth of *M* is evidence of operation. A write to memory is a hypothesis until an
evaluation that did not generate it scores it on evidence it did not see. §6 finds this is the most
frequently made and least frequently evidenced claim in current systems.

**And it makes the individual dependent.** Everything inside an individual's boundary is, by
Definition 1, available to its single decision process, therefore inside its write set. So:

> **Corollary 1.** *An individual cannot have a well-posed improvement loop over itself alone. A
> referee it does not control is a condition of its improvement being defined, not a safeguard added
> to it.*

A second, independent argument gives the same conclusion. Discovery is instrument-bounded, and
instruments are constructed from matter outside the mind; an intelligence that does not act on the
world has a fixed frontier however capable. Both routes make **the outside constitutive of the
individual**, which §4.1 turns into the reason the organizational scale exists.

### 3.5 Physical bounds on an individual

Definition 1 has consequences that are not about design.

> **Proposition 2 (coherence).** *For the workspace to be global, every part contributing to or
> reading from it must exchange signal with it within one decision cycle. With cycle τ and signal
> velocity v ≤ c:*
> $$R \;\le\; \frac{v\tau}{2} \;\le\; \frac{c\tau}{2}$$

A cycle of 1 ms permits a radius of 150 km; 1 ns permits 15 cm; 1 ps permits 0.15 mm. **There is a
largest possible individual at every speed, and scaling past it does not produce a greater mind but a
society** — so the boundary between mind and civilization is physical rather than historical. Because
capacity rises with volume while rate falls with radius, the optimum is *interior* and set by purpose:
a fast-narrow mind and a slow-wide one can both be maximal, and no single configuration dominates.

Four further bounds. **Aperture**: *k* is limited by integration completing within τ, and integration
cost grows superlinearly in *k* because what must be evaluated is relations — so an individual is
bounded not by what it knows but by how much can be present at once. **Self-opacity**: a model is part
of what it models, so a complete self-model is larger than the self; terminal self-knowledge is a
compression, and the only honest compression is one that reports its own inadequacy. **Referee**:
Corollary 1. **Mass–energy allocation.**

We observe that a 1 kg individual at Lloyd's limits performs of order 5 × 10⁵⁰ operations per second,
so a hand-sized individual at nanosecond cycles has ~10⁴¹ operations per decision. **At the limit an
individual is not computation-bound**; it is bound by aperture, self-opacity, and waiting on a
referee. This reverses the usual picture. Biology sits six to eight orders of magnitude below the
coherence bound, held there by neural signal velocities of metres per second rather than *c* — so the
headroom is enormous while every qualitative bound survives intact.

> **Proposition 3 (identity).** *At depth D4 every element of B is eventually replaced, so identity
> cannot be continuity of memory, goals, substrate, or behaviour — the last would make improving and
> dying indistinguishable. Two states belong to the same individual iff connected by an unbroken chain
> of provenance-linked evidence records.*

Identity so defined is preserved by every permitted operation and broken by exactly those that are
already forbidden: an unattributed write, a promotion without authorization, a self-declared verdict,
a restore with no record of the restore.

---

## 4. Organizational intelligence

### 4.1 An organization is not a larger individual

> **Definition 5 (organization).** A set of individuals together with a **coordination structure**:
> who may propose to whom, who may promote whose proposals, who holds which authority, what referee is
> shared, and what couples the whole to the world.

By Definition 1 an organization has no global workspace, and by Proposition 2 there is no size at which
one could be restored. **The transition is a change of kind.**

> **Proposition 4 (priority).** *The organizational scale is not an aggregate of the individual scale
> but a precondition of it. By Corollary 1 an individual's referee and reach axes are properties of
> the organization it sits in, not of the individual.*

The practical consequence: **an intelligence's level cannot be raised by working only on the
intelligence.** Two of its determinants are not in there.

### 4.2 Five axes

None is a capability of any member.

**Coverage.** Does the structure contain an individual for every role its loop requires? A missing role
is not a weakness to be offset by excellence elsewhere; it is an open loop. This is Ashby's requisite
variety applied to roles.

**Separation.** Are proposer, promoter, and referee distinct? This is Proposition 1 at organizational
scale, and the axis on which organizations most often score zero while believing themselves excellent.

**Throughput** *T*<sub>δ</sub>. How long does a proposal take to traverse propose → evaluate →
promote? By an Amdahl-style argument, once the automated steps are cheap the iteration rate is bounded
by the un-automated ones: ρ<sub>max</sub> = 1/*T*<sub>δ</sub>. **This is the only axis in this paper
that is directly and cheaply measurable** — timestamp the authorization events.

**Referee externality.** Is the progress measure authored outside? An organization that reorganizes
its own evaluators and reports improvement has reported a tautology.

**World coupling.** Does the referee chain terminate in an instrument or in another member? A closed
community of mutually-refereeing individuals is well-posed exactly to the extent that it does not.

### 4.3 Organizational intelligence is not monotone in member capability

> **Proposition 5.** *An organization scoring zero on separation has no well-posed improvement loop
> regardless of its members' levels, while an organization of modest members scoring well on all five
> axes does. Therefore an organization of maximal individuals with no separation of duties is **less**
> intelligent than a mixed organization of ordinary ones.*

*Argument.* Zero separation means one individual proposes, judges, and adopts; by Proposition 1 every
improvement it reports is self-certified. Member capability enters the argument nowhere, and that is
the point. **Capability determines the quality of proposals; separation determines whether the
organization can tell a good proposal from a bad one — and one that cannot does not benefit from
better ones.**

The recurring institutional hope is that sufficiently capable members make process unnecessary. The
argument says the reverse: process is what converts capability into a claim anyone can rely on.

### 4.4 Which level fills which role

| Level | Role | Why only this level |
|---|---|---|
| ⟨D0, closed, ∅⟩ | Advisor | No write set, so it may hold information it could misuse if it could act |
| ⟨D0, closed, **other**⟩ | **Guide · promoter · referee** | An empty self-write set is the only thing that admits authority over another's promotion |
| ⟨D1, closed, self⟩ | Operator | A source of evidence, not of verdicts |
| ⟨D2, closed, self⟩ | Specialist | Improves its own policy against a metric it did not author |
| ⟨D3, closed, self⟩ | **Instrument-maker** | Converts knowledge into apparatus — see below |
| ⟨D4, closed, self⟩ | Substrate improver | Structurally a proposer; deployment authority is separate by construction |
| ⟨any, **open**, both⟩ | Director | The only role that may revise the objective, and only holding a frozen referee |

**The instrument-maker is the role that compounds.** Discovery is instrument-bounded (§3.4), so the
conversion of knowledge into apparatus is the only operator whose output re-enters the loop's input.
An organization can have flawless operators, self-tuning specialists, an impeccable referee and a fast
promoter, and **its frontier will not move at all** if nothing converts what it learns into something
that reaches further. The diagnostic is not how much an enterprise discovers but what fraction of what
it discovers becomes apparatus.

### 4.5 Levels necessarily coexist

> **Proposition 6.** *At any decision the participants must occupy different levels. Heterogeneity may
> be realized permanently across individuals or temporarily within them by restriction, but it cannot
> be absent.*

Four independent arguments.

**Separation is level differentiation enacted.** A referee that can write the judged party's state
reintroduces the feedback coupling whose absence makes a multi-agent system verifiable agent by agent.
Restricting it restores verifiability — but a restricted individual is, for that engagement, at a
lower level.

**The bound is a frontier, not a peak.** By §3.5 the individual optimum is interior and purpose-set, so
an organization facing several kinds of decision needs several kinds of mind. Forced by the shape of
the physical bound, not by scarcity.

**The depths run at different clock speeds.** §3.2: fast loops must sit close to the work and slow ones
behind a gate, which assigns different depths to different bodies structurally.

**Authority is earned and newcomers arrive.** Any organization that can admit anyone contains members
at every ceiling as a *steady* state, not a transitional one.

> **Corollary 2.** *An organization composed entirely of maximal individuals all holding all roles
> scores zero on separation and by Proposition 5 has no well-posed improvement loop. Uniformity at the
> maximum is not the strongest configuration but one of the weakest, and its members' capability does
> not rescue it.*

We note this contradicts a common picture of an advanced future as populated by uniformly maximal
minds. As an *organization*, such a population would be less intelligent than a well-structured
laboratory of ordinary ones.

### 4.6 On energy

Energy capture is an indicator of a terminal state and not constitutive of one. Terminal implies high
energy capture, since instruments consume energy and reach is instrument-bounded. The converse fails:
an energy-rich civilization with a slow review process is throughput-bound and epistemically stalled,
and no point on an energy scale would reveal it. This is Proposition 5 at civilizational scale.

---

## 5. What to report

For an intelligence: loop completion per substrate; authority ceiling; the self-state profile with
per-coordinate evidence counts; the triple ⟨*D*, open/closed, reach⟩; which of the five individual
bounds binds, if any.

For an organization: ⟨coverage, separation, *T*<sub>δ</sub>, referee externality, world coupling⟩ plus
the **level census** — the distribution of member levels across roles, and in particular whether a
⟨D3⟩ instrument-maker is present.

**Unmeasured is off the scale, not the bottom of it.** A coordinate with no verified outcomes reported
as a low number is read as *measured and bad* rather than *never run*; those are opposite facts and
only one is true. Reporting confidence without evidence fails the axis rather than scoring low on it.

---

## 6. Where current agents sit

### 6.1 Method and provenance

Placements are orderings by inspection. Evidence quality varies greatly and we state it rather than
averaging over it.

| System | Inspected | Confidence |
|---|---|---|
| A research-agent platform (full source, incl. its improvement and self-model modules) | Fully | High |
| Claude Code | From inside; harness behaviour observed, not source | Medium |
| Codex | Present in the study corpus, not read in depth | Low–Medium |
| OpenClaw | Only a billing wrapper; the agent itself not inspected | Low |
| Grok bot | Not inspected; classified by product category alone | Very low |

The last two rows should be read as *what a system of that description would score*.

### 6.2 Results

| System | Object | Level | Ceiling |
|---|---|---|---|
| Claude Code | Individual | ⟨D1, closed, self + other-inputs⟩ | Allowlisted operator → proposer |
| Codex | Individual | ⟨D0–D1, closed, self⟩ | Isolated runner → allowlisted |
| OpenClaw | Individual | ⟨D0–D1, closed, self⟩ | Isolated runner → allowlisted |
| Grok bot | Individual | ⟨D0, closed, ∅⟩ | Advisory → allowlisted |
| Research agents | Individual | ⟨D2, closed, self⟩ | Switch + budget + charter |
| The platform hosting them | **Organization** | Coverage strong · separation strong · *T*<sub>δ</sub> **unmeasured** · referee external · coupling partial | — |

A note on a common confound: **provider or billing wrappers change no axis.** A shim that routes an
agent's traffic through a different endpoint alters neither depth, ceiling, reach, nor self-state. Such
wrappers are easy to mistake for products with levels of their own.

### 6.3 The one-cell finding

**None of the coding agents writes itself.** They modify external software — reach into the world,
which the taxonomy does not confuse with depth into the self:

> Software an agent writes is not that agent's brain unless the agent then runs on it.

An agent refactoring a repository operates at D0 *on itself* while doing arbitrarily large work on an
external substrate. Nothing in the loop feeds a validated change back into the agent that made it:
there is no validation over its own behaviour, no held-out evaluation of whether last month's memory
writes made this month's sessions better, and no promotion step.

Consequently Claude Code, Codex, and OpenClaw **occupy the same cell on every axis in this paper**.
What distinguishes them — patch quality, context handling, tool protocol — is proposal quality, which
§1.4 says this map deliberately does not measure. The differences that dominate public comparison are
intra-cell. **The difference that would move any of them a cell is a held-out evaluation of their own
configuration, and none ships one.**

Claude Code is a half-step ahead on two axes: a memory store with per-entry provenance and typed
categories, which is a genuine D1 write set rather than a human-authored instruction file; and bounded
other-reach, since it spawns subagents and hands them tasks — inputs only, never their state, which is
exactly the bound §3.3 requires. Both are *structurally* present and *evidentially* unsupported,
because the ablation in §3.4 is not run.

For every system in §6.2 except the research agents, most self-state coordinates are **unmeasured**.
These systems describe their capabilities fluently and hold no evidence ledger, so capability
self-report is a claim rather than a coordinate. Resource state — context, budget, latency — is the one
coordinate well supported across all of them.

### 6.4 The research agents, and what puts them higher

They are the strongest individuals in the study, and not because of capability. They carry internally
what the coding agents leave to their harness.

**Validation that can refuse.** A candidate becomes an improvement by surviving six checks rather than
by winning, on the stated ground that the best of *N* runs is the commonest way a real improvement
claim turns out to be nothing. The seed rule is load-bearing: in one of the target fields a defended,
statistically corrected effect is *+0.023 against a ±0.027 seed spread*, so a claim without the whole
seed set — including the runs that went the wrong way — means nothing. **No-change is a valid output**,
and a fortnight of them is a result about the method rather than a failure of the agent.

**A self-model with refusals.** Every line traces to a run; unmeasured is reported as unmeasured and
never as zero; the limits line is always present and cannot be suppressed; and there is no path from
reading to authority. This is §5's reporting rule implemented rather than asserted.

**Ledgers that are never summed.** Owner-set work, benchmark scores, and self-directed research are
kept as three lines, because an agent that wrote its own benchmark, passed it, and counted the pass
toward its record would have published its own reputation. This is Proposition 1, derived
independently by practitioners under implementation pressure — which we take as modest evidence for it.

**Autonomy that stops rather than asks.** Ordinary user tasks run with the autonomy switch off, since a
person asking for help is not the agent deciding to spend their money. The autonomous round ends on the
switch, the budget, or the work running dry, and none of those produces a request for more.

Placement: ⟨D2, closed, self⟩; role, specialist moving toward instrument-maker.

### 6.5 What none of them has

No individual studied is objective-open — correctly, since by §4.4 that is the director's role and in
every one of these systems the director is a human. No individual is at D3 over its own capability, so
by §4.4 the role that compounds is the thinnest in the picture. Nobody is near any of the five
individual bounds; **the binding constraint on every system studied is authorization latency**, which
is a removable throughput cost rather than a physical floor. And nobody runs the memory ablation: every
system here that claims memory helps has not measured whether it does.

---

## 7. Falsification

**Proposition 1 fails** if a system with its evaluator inside its write set produces improvement claims
that replicate on evidence it did not author, at a rate comparable to systems with external evaluators.
This is testable now, on any system that self-scores.

**Proposition 5 fails** if organizations with no separation of duties reliably match or exceed
separated ones on held-out outcomes, controlling for member capability.

**Proposition 6 fails** if a mechanically restricted uniform organization — write sets narrowed by
infrastructure rather than by instruction — achieves separation without level differentiation. We
regard this as the most likely of the three to fail, and §8.3 says why.

**Proposition 2 does not fail**; it is arithmetic given the premises. What could fail is Definition 1's
sharpness: if individuality is timescale-relative (a fast core with a slow periphery is individual at
one timescale and federated at another), the bound holds at each timescale and the mind/organization
boundary becomes a gradient rather than a line.

**The one-cell finding fails** the moment any of the systems in §6.2 ships a held-out evaluation over
its own configuration with a promotion gate. We expect this and regard it as the paper's most likely
obsolescence.

---

## 8. Limitations

**8.1 — Nothing here is a measurement.** Depth is reported as the deepest writable element, which
treats a one-parameter tweak and a full policy rewrite alike. Separation is treated as present or
absent, when real organizations separate partially — a referee reporting to the promoter, a director
selecting the evidence. Aperture's integration-cost growth rate is unknown, and a near-linear rate
would move that bound far without removing it. Every axis is an ordering.

**8.2 — The map does not predict performance,** and the temptation to use it as though it did is the
main way it could do harm. A system at D0 may be far more useful than one at D2. The map says what a
system's improvement claims mean, not how good it is, and a low placement is not a criticism of a
product.

**8.3 — Restriction is not verified.** Proposition 6 prefers permanent differentiation on the ground
that per-engagement restriction relies on self-restraint. A mechanically restricted capable individual
would satisfy the argument without differentiation. Whether that is achievable for an individual
capable enough to matter is the alignment problem, and this paper has nothing to add to it.

**8.4 — Placements date.** §6 describes systems on one day. The frameworks in §3–§4 state constraints;
§6 states a snapshot, and only the first is intended to survive.

**8.5 — Coverage has no optimum.** §4.5 shows heterogeneity is forced and says nothing about
proportions. Given §4.4 makes the instrument-maker the role that compounds, the ratio of operators to
instrument-makers is the gap that matters most, and it is not addressed.

**8.6 — No representation of purpose.** §3.5 says the individual optimum is interior and set by what a
mind is for; we have no representation of what anything is for, so we can describe the frontier and
cannot locate a point on it.

---

## 9. Conclusion

The ladder is the wrong shape because two of the three things that determine a level are not inside the
system being levelled. What an intelligence may write is a property of it. Who evaluates the write, and
what structure the evaluation sits in, are properties of an organization — and by Proposition 1 an
improvement claim without them is not weakly supported but undefined.

Taking that seriously produces a taxonomy in which the interesting distinctions are structural. It
places a largest possible individual at every decision speed, past which there is a society and not a
greater mind. It makes an organization's intelligence non-monotone in its members' capability, so that
uniform maximality is degenerate rather than optimal. And applied to current systems it finds that
agents whose relative merits are debated continuously occupy one cell, differing on an axis the
taxonomy declines to measure, while the axis that would separate them — an evaluation of their own
configuration by something that did not author it — is one none of them has yet built.

That last point is the practical one. The step from where these systems are to the next cell is not a
larger model. It is a held-out set, a promotion gate, and someone other than the system holding the pen.

---

## References

Amdahl, G. (1967). Validity of the single processor approach to achieving large scale computing
capabilities. *AFIPS Conference Proceedings*.

Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall.

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Bekenstein, J. D. (1981). Universal upper bound on the entropy-to-energy ratio for bounded systems.
*Physical Review D*, 23(2).

Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press.

Chaitin, G. J. (1975). A theory of program size formally identical to information theory. *Journal of
the ACM*, 22(3).

Chollet, F. (2019). On the measure of intelligence. *arXiv:1911.01547*.

Conant, R. C., & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system.
*International Journal of Systems Science*, 1(2).

Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences*, 24(1).

Dehaene, S., & Changeux, J.-P. (2011). Experimental and theoretical approaches to conscious processing.
*Neuron*, 70(2).

Dyson, F. J. (1979). Time without end: Physics and biology in an open universe. *Reviews of Modern
Physics*, 51(3).

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I.
*Monatshefte für Mathematik und Physik*, 38.

Good, I. J. (1965). Speculations concerning the first ultraintelligent machine. *Advances in
Computers*, 6.

Kardashev, N. S. (1964). Transmission of information by extraterrestrial civilizations. *Soviet
Astronomy*, 8.

Krauss, L. M., & Starkman, G. D. (2000). Life, the universe, and nothing: Life and death in an
ever-expanding universe. *The Astrophysical Journal*, 531(1).

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of
Research and Development*, 5(3).

Legg, S., & Hutter, M. (2007). Universal intelligence: A definition of machine intelligence. *Minds and
Machines*, 17(4).

Lloyd, S. (2000). Ultimate physical limits to computation. *Nature*, 406.

Lloyd, S. (2002). Computational capacity of the universe. *Physical Review Letters*, 88(23).

Margolus, N., & Levitin, L. B. (1998). The maximum speed of dynamical evolution. *Physica D*, 120.

Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2).

Morris, M. R., Sohl-Dickstein, J., Fiedel, N., Warkentin, T., Dafoe, A., Faust, A., Farabet, C., &
Legg, S. (2024). Levels of AGI for operationalizing progress on the path to AGI. *ICML*.

SAE International (2021). *J3016: Taxonomy and Definitions for Terms Related to Driving Automation
Systems for On-Road Motor Vehicles*.

Sheridan, T. B., & Verplank, W. L. (1978). *Human and Computer Control of Undersea Teleoperators*. MIT
Man–Machine Systems Laboratory.

Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem.
*Proceedings of the London Mathematical Society*, 42.

von Neumann, J. (1966). *Theory of Self-Reproducing Automata* (A. W. Burks, Ed.). University of
Illinois Press.
