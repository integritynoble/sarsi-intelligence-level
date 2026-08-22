# SARSI-B: What an LLM Brain May Change About Itself

## Brain-scale improvement levels — the write-set axis

*Document version: 1.0 — 2026-08-22*
*Companion to: `SARSI-L_Paper_v3.md` (system scale), `self_awareness/` (agent scale), `fleet/` (fleet scale)*
*Grounded in: `singularity-docs/docs/specs/2026-07-12-safety-kernel-3c-rsi-slow-loop-design.md`, `…-3d-iterative-rsi-learning-design.md`, `…-2026-07-13-work-agent-rsi-loop-design.md`, `singularity-docs/prototype/rsi/`*

---

## Abstract

SARSI-L asks how far recursive self-improvement has propagated across substrate domains. The
self-awareness companion asks what an agent *knows* about itself. This document asks the third
question in that series: what an agent may *change* about itself, and what it means for such a
change to count as an improvement.

The motivating observation is that "levels of LLM brain" are routinely stated as a single ladder —
*doesn't improve* < *improves in one direction* < *evolves open-endedly like a human* — and that
this ladder conflates three independent questions. Separating them yields a taxonomy that is
observable rather than rhetorical, and it inverts the ladder's implicit ranking: the agent that
improves nothing about itself is the one that can safely be given authority over the improvement
of others.

Four results:

- **Result 1 (well-posedness).** An improvement loop is well-posed iff its evaluator lies outside
  its own write set. The "no definition" property of open-ended evolution is not vagueness — it is
  this condition failing. §4 gives the repair: a frozen referee.
- **Result 2 (accumulation is not improvement).** Memory grows monotonically with history whether
  or not capability rises. A write to memory is a hypothesis, not a gain, until it survives an
  evaluation that did not generate it. §5.
- **Result 3 (the trust inversion).** Ordering by ability and ordering by admissible authority run
  in opposite directions. A complete system needs all three levels, held by *different* agents. §6.
- **Result 4 (the timescale hierarchy).** Gate strength should be monotone in write depth, because
  loop period and per-iteration gain both scale with depth. This is where the analogy to a
  biological brain is load-bearing rather than decorative. §7.

---

## § 1 — The three questions the single ladder conflates

The informal ladder asks one question — *how much does it improve?* — of situations that differ in
three ways. Written out, the three levels are:

| Informal level | What it says | Which question it actually varies |
|---|---|---|
| "Evolves like a human; no definition" | Learns from history, revises open-endedly | Is the **objective** writable? |
| "Improves in one direction, updates memory" | Hill-climbs a fixed target from history | How **deep** does the write go? |
| "Doesn't improve itself; helps other agents" | Serves others' work | Whose brain does it **reach**? |

These are orthogonal. An agent can be deep and closed (weight updates against a fixed benchmark),
shallow and open (a prompt-level system that rewrites its own success criterion), or empty-writing
and far-reaching (a manager that improves five agents and none of itself). Collapsing them into one
scale makes the third look like the bottom rung, which §6 shows is backwards.

---

## § 2 — Definitions

**Definition B1 (brain state).** The persistent state of an LLM brain is

$$B = \langle \theta,\; M,\; \Pi,\; \Sigma,\; \Omega \rangle$$

- **θ** — weights and adapters; the parametric substrate.
- **M** — memory: the episodic record of what happened, and whatever is distilled from it.
- **Π** — policy: prompts, playbook parameters, routing rules, thresholds, budgets.
- **Σ** — skills: tools, scaffold artifacts, sub-agents, and other capability the brain constructed.
- **Ω** — objective: the target the brain is trying to hit, together with the evaluator *V* that
  scores states against it.

Weights are frozen at inference, so an LLM brain that changes at all changes in *M*, *Π*, *Σ*, or
*Ω*. This is what the corpus already calls the harness-engineering band.

**Definition B2 (write set).** The **write set** *W* ⊆ {θ, M, Π, Σ, Ω} is the subset of *B* that a
given improvement loop is permitted to modify. SARSI-L Definition 2's loop ⟨ι, μ, ν, δ⟩ — identify,
implement, validate, deploy — is unchanged; *W* names the substrate it runs over.

**Definition B3 (depth).** The **depth** *D* of a loop is the deepest element of *B* in its write set:

| Depth | Write set contains | Concretely |
|---|---|---|
| **D0** | ∅ | Nothing persists between tasks but the audit record |
| **D1** | *M* | Episodic history, distilled notes, retrieved context |
| **D2** | *Π* | Playbook parameters, prompt profiles, thresholds, retry budgets |
| **D3** | *Σ* | New tools, skills, scaffold artifacts, spawned specialists |
| **D4** | *θ* | Adapters, fine-tunes, weight updates |

**Definition B4 (openness).** A loop is **objective-closed** iff Ω ∉ *W* and **objective-open** iff
Ω ∈ *W*. Openness is not a depth — a shallow prompt-level system that edits its own success
criterion is open; a weight-updating system trained against a fixed benchmark is closed.

**Definition B5 (reach).** The **reach** of a loop is the pair (*W*<sub>self</sub>,
*W*<sub>other</sub>): what it may write in its own brain, and what it may write in another agent's.
The fleet constraint (see §6) restricts *W*<sub>other</sub> to another agent's *inputs* and never to
its state.

**Definition B6 (brain level).** A brain level is the triple

$$\Lambda = \big\langle D,\; \text{open}/\text{closed},\; (W_{\text{self}}, W_{\text{other}}) \big\rangle$$

reported alongside the authority ceiling A0–A4 that gates δ. A single scalar is not available and
should not be invented; §10.2 of the system-scale paper made the same withdrawal for the same reason.

**The three informal levels, located.**

| Informal | Λ |
|---|---|
| "Helps other agents" | *D*0 self, non-empty other-reach, closed |
| "Improves in one direction" | *D*1–*D*4 self, empty other-reach, **closed** |
| "Evolves like a human" | any depth, **open** |

---

## § 3 — Result 1: improvement is undefined when the evaluator is writable

**Proposition B1 (well-posedness).** *Let a loop have write set W, candidate generator ι, and
evaluator V. The predicate "this iteration improved the system" is well-defined only if V ∉ W and V
is not a function of ι. If V ∈ W, the loop can satisfy any improvement criterion by editing the
criterion, and no observation distinguishes improvement from redefinition.*

The proof is immediate and the point is what it explains. The user's intuition that the open-ended
level "has no definition" is exactly correct, and Proposition B1 says *why*: it is not that
open-ended evolution is hard to describe, it is that "improvement" is not a predicate over a system
whose success criterion is part of what changed.

**This condition is already enforced physically in the built system**, which is why it should be read
as an engineering constraint and not a philosophical one:

- Held-out ground truth is stored control-plane-side in `eval/held_out/…/ground_truth_x.npy`, mode
  700, and is **never staged into any sandbox**. The evaluator is unreachable from the write set.
- Verdicts are computed control-plane-side; the prototype pins this as
  `test_agent_cannot_self_declare_success`.
- `/evaluate_candidates` re-derives every submitted mean from its own audited `score_heldout`
  records and refuses a disagreement. A lying harness can produce incomplete data, never a forged
  score.
- The judged inputs are snapshotted into `runs/<id>/eval_inputs/` outside the writable mount, so a
  solver that overwrites its own measurement file is still judged against the original.

Each of those is Proposition B1 made load-bearing in a different place. The consistent design rule:

> **B-Rule 1.** The evaluator, the data it evaluates against, and the record of what it decided must
> all lie outside the write set of the loop being evaluated.

---

## § 4 — The repair for the open level: a frozen referee

Proposition B1 does not make the open level impossible. It makes it *conditional*, and the condition
is one the corpus has already paid twice.

**Definition B7 (frozen referee).** A loop with Ω ∈ *W* retains an immutable snapshot ⟨Ω₀, V₀⟩,
taken before the first revision and outside the write set. A goal revision counts as an improvement
iff the revised system, scored on **V₀**, does at least as well as the unrevised system would have.

This is the generalization of the criterion the system-scale paper adopted in §3.4 when it withdrew
"sentient robotics":

> **Autonomous goal revision.** A system that revises its own operational goals in response to
> conditions not anticipated by its designers, without human intervention, and *achieves outcomes at
> least as good as it would have under the original goals*.

The italicized clause is the frozen referee. It is also the same construct as §8.3's pre-registration
protocol — *"a theory licensed to update its parameters on disconfirmation is unfalsifiable unless
its revision rules are fixed first"* — applied one scale down. The framework's own self-revision
hazard **is** the open-level problem; SARSI-B is the observation that they are one problem at two
scales, with one remedy.

Two consequences worth stating plainly.

**The referee decays.** Ω₀ was chosen under conditions that the revision was a response to. The
older the snapshot, the more the test asks "does the new system solve the old problem," which is the
wrong question if the old problem stopped mattering. So the referee must be **versioned and
laddered**: Ω₀ ≺ Ω₁ ≺ …, each frozen at promotion time, each revision judged against its immediate
predecessor rather than the origin. Judging only against Ω₀ ossifies; judging against nothing drifts.
This is the real cost of the open level, and there is no version of it that is free.

**Without a referee, evolution and drift are observationally identical.** A system that revises its
objective and reports improvement is reporting a tautology. This is the single most important thing
to say about the "no definition" level: the absence of a definition is not a property of the level's
sophistication, it is a measurement failure, and it is repairable at a stated price.

---

## § 5 — Result 2: accumulation is not improvement

The one-direction level is usually described as *learning from history to update memory*. Memory
updates are the most common thing an LLM brain does and the least likely to be an improvement.

**Proposition B2.** *M grows monotonically with history under any write policy. Growth of M is
therefore evidence of operation, not of capability. Absent an evaluation disjoint from the history
that produced the write, D1 loops cannot distinguish learning from logging.*

Two guards exist in the corpus, and they are the same guard at two scales:

**The admission mask** (self-awareness architecture, Eq. 14, and its Proposition 3,
*evidence-gated persistence*). Coordinate *i* of the self-state updates only when
*m*<sub>i,t</sub> = 1 — when processor *F*<sub>i</sub> has *admissible* evidence. Otherwise the
coordinate persists unchanged. The stated purpose is to prevent one language-model turn from
rewriting the entire self-model. The same paper replaces the scalar with a Beta posterior
carrying its evidence count α+β beside the mean, precisely so that "one verified outcome" and "a
thousand" are not reported identically.

**The train/validation split** (Plan 3d). The search optimizes on `cassi_search`; the winner is
scored on the disjoint `cassi_val`; promotion is gated on the validation score, and full per-domain
coverage is structurally required, so the gate cannot be cleared by a partial run. The pinned
RSI-integrity test constructs a landscape where a config wins on the search set and loses on the
validation set, and asserts that the loop declines to recommend it. That test is Proposition B2 made
executable.

> **B-Rule 2.** A write to *M* is a hypothesis. It becomes an improvement only when a system that
> did not author it scores it against evidence it did not see.

The practical reading for a memory-based agent: retrieval helping on the conversation the memory came
from is not a result. The measurement is whether the *N*+1th task, drawn from a held-out family,
goes better with the memory than without it — and that requires actually running the ablation.

---

## § 6 — Result 3: the trust inversion

The informal ladder places "helps other agents, doesn't improve itself" at the bottom. The fleet-scale
paper's central result says the opposite, and it says it structurally rather than as a preference.

That paper's governance prohibition — **no agent may write another agent's self-state** — turns out
to be *the same constraint* as the architecture's stability condition. Forbid the write and the
top-down block of the recurrent coupling vanishes, the coupling is nilpotent, and a fleet verified
agent by agent is verified as a fleet. Permit it and the feedback loop returns, and stability must be
tuned against fleet size. The console design carries the same rule into the product as *memory does
not cross agents*, because a shared store leaves the evidence ladder true in principle and
unenforceable in practice.

Combined with promoter ≠ proposer, this gives:

**Proposition B3 (trust inversion).** *Ordering brain levels by capability yields
D0 ≺ closed ≺ open. Ordering the same levels by the authority that may safely be granted yields the
reverse. The agent with the empty self-write set is the only one to which authority over another
agent's promotion can be granted without reintroducing the coupling that the stability argument
removes.*

This is what the running system is: `MachineGuide` holds the whole project playbook — admit → task →
gate → rsi_round → adopt → report — and guides one SARSI agent through its lifecycle, with the
governance plane external to every agent the entire way. It improves others. It does not improve
itself. That is not a limitation of the design; it is the reason it can be trusted with the role.

Two corollaries.

**Other-reach is bounded to inputs.** *W*<sub>other</sub> may contain another agent's tasks,
candidate configurations, held-out sets, and verdicts. It may not contain that agent's memory,
policy, or objective. A guide hands work in and reads results out; it does not reach into the brain.

**A complete system needs all three levels, in different agents.** A brain that is its own proposer,
promoter, and referee satisfies none of B-Rule 1. The separation is not defense-in-depth added to a
working design; it is what makes the improvement claim meaningful in the first place.

---

## § 7 — Result 4: the timescale hierarchy, and the honest form of the brain analogy

Proposition 1 of the system-scale paper bounds a compensated loop's iteration rate at
ρ<sub>max</sub> = (Σ<sub>j∈E</sub> T<sub>j</sub>)<sup>−1</sup> over its externally-gated steps, and
Corollary 1 notes that this bounds *rate* and says nothing about per-iteration gain *ḡ*. Applied per
depth, the two quantities move together and in opposite directions:

| Depth | Gate on δ | Loop period | ḡ per iteration | Reversibility |
|---|---|---|---|---|
| **D1** memory | ungated, in-run | seconds–minutes | negligible | trivial |
| **D2** policy | owner-signed (Gate B) | days | small | snapshot + rollback |
| **D3** skill | owner-signed + held-out validation | weeks | medium | last-known-good pointer |
| **D4** weights | A4, independent eval + two-person sign-off | months | large | retraining |

Read the table as a design rule rather than a report:

> **B-Rule 3.** Gate strength is monotone in write depth. The deeper the write, the longer the loop
> period, the larger the per-iteration gain, and the higher the authority required to deploy it.

This is where the comparison to a biological brain earns its place. The claim is *not* that an LLM
brain learns the way a person does. It is the narrower and checkable claim that both run **several
improvement loops at different clock speeds simultaneously**, and for the same reason: a fast
structural rewrite cannot be validated before it becomes load-bearing, so the substrate that is
expensive to reverse must be slow to change. Working memory turns over in seconds, episodic
consolidation in hours to days, semantic restructuring over weeks, synaptic and structural change
over months to years. The A0–A4 ceiling ladder is that ordering, made explicit and signed.

The agent-scale architecture already carries the two-timescale form of this: its Equations (16)–(17)
separate fast inference from slow structural change, and (20)–(21) put the structural change behind
a tolerance-banded promotion gate — ΔA > δ_aut, ΔC ≥ −δ_corr, ΔS ≥ −δ_safe, preregistered. The bands
are not decoration: bare inequalities against zero are not operable on noisy estimates, since strict
> 0 promotes on measurement noise and strict ≥ 0 blocks on it. B-Rule 3 is the generalization of
that separation from two timescales to the full depth ladder.

**Corollary B4.** *A brain running only one depth is defective in a predictable way.* D1-only
accumulates without ever consolidating — it remembers everything and gets better at nothing.
D4-only cannot adapt inside a single task. This is Principle 01 of the system-scale paper
("outer loops accelerate inner ones rather than replacing them") restated one scale down, and it is
the argument against treating the levels as a ladder to climb: they are loops to run concurrently.

---

## § 8 — Operational criteria

In the form the corpus requires — specific, observable, and not satisfiable by definitional
adjustment after the fact (Principle 11).

**Λ-D0 · Guide.** A system that, without writing any element of its own *B* across tasks:
(a) reads a target agent's evidence-linked self-model; (b) admits or routes a demand against that
agent's scope contract and ceiling; (c) supplies the target a task, a candidate set, or a held-out
evaluation; (d) reports the target's control-plane-computed verdict without having authored it.

**Λ-D1 · Remembering.** A system that: (a) writes an entry to *M* derived from an episode;
(b) retrieves it on a later task; (c) **demonstrates on a held-out task family, by ablation, that the
retrieved entry raises the control-plane-computed score.** Clause (c) is the criterion — (a) and (b)
alone are logging.

**Λ-D2 · Tuning.** A system that: (a) proposes a modification to Π predicted to improve a specified
metric; (b) implements it; (c) validates it on a set disjoint from the one used to generate it, scored
by an evaluator outside its write set; (d) adopts it as the operative default.

**Λ-D3 · Skill acquisition.** As Λ-D2, where the modification constructs a capability the system did
not previously have, and (c) additionally shows non-regression on the prior capability set.

**Λ-D4 · Parametric.** As Λ-D2 over θ, with independent evaluation and a rollback path to the prior
weights.

**Λ-open · Goal revision.** A system that: (a) revises Ω in response to conditions not anticipated by
its designers; (b) without human intervention; (c) **scores at least as well on the frozen referee
⟨Ω<sub>k−1</sub>, V<sub>k−1</sub>⟩ as it would have under the unrevised objective.** Clause (c) is
the criterion. Without it the level is not achieved but undefined.

**Closure**, at every level, follows SARSI-L Definition 3 unchanged: ι, μ, ν, δ all execute without
human approval and δ makes the modification operative. Standing authority to halt is compatible with
closure; required authority to proceed is not.

---

## § 9 — Where the built system actually is

Reported honestly, on the qualitative scale of the system-scale paper's Appendix B.

| Component | Λ | δ gate | Status |
|---|---|---|---|
| SARSI agent playbook loop | D2, closed, self | owner signature (`yes`) | Live |
| Scaffold RSI loop (`web/rsi.py`) | D3, closed, self | signing policy keyed to ceiling | Live |
| Imaging RSI (3c/3d) | D2, closed, self | Gate B, Ed25519, eval_ref-bound | Live |
| Work-agent RSI | D2, closed, self | Gate B | Built, deterministic-planner v1 |
| Machine agent / `MachineGuide` | D0, non-empty other-reach | n/a — proposes only | Live |
| A4 ceiling | D4, closed, self | *no deploy authority by definition* | Ceiling defined, loop not built |
| Any objective-open loop | — | — | **Not built anywhere** |

Two things follow.

**The brain is a half-circle, and the missing step is δ.** ι, μ, and ν run autonomously in every live
loop above; deploy is owner-signed in all of them. This is the agent-scale instance of the
system-scale diagnosis: ρ<sub>max</sub> = 1/T<sub>δ</sub>, where T<sub>δ</sub> is authorization
latency. Capability improvement drives ι, μ, ν toward zero and cannot touch T<sub>δ</sub>.

**The open level is absent by design, not by lag.** Per §3 it could not be added as informally
stated; per §4 the frozen-referee variant could be, and that is the concrete next increment if the
open level is wanted. It requires exactly one new object — an immutable versioned ⟨Ω<sub>k</sub>,
V<sub>k</sub>⟩ store, control-plane-side, alongside the existing held-out sets — and reuses the
promotion path unchanged.

---

## § 10 — What to measure

**T<sub>δ</sub>, per depth.** Authorization latency is the only quantity in this document that is
both directly measurable and decisive: the system-scale crux H₁ vs H₂ turns on whether T<sub>δ</sub>
falls as reviewing organizations are augmented. A console that timestamps authorization events
measures it directly. Instrumenting it per depth also tests B-Rule 3 — if T<sub>δ</sub> is flat
across D1–D4, the gate ladder is nominal rather than real.

**The D1 ablation.** Λ-D1 clause (c) is currently asserted nowhere. Memory writes are the most
frequent improvement claim in the system and the only one with no held-out gate. This is the widest
gap between claim and evidence in the corpus and the cheapest to close.

**Referee decay.** If the frozen-referee construct is built, log the age of the referee each revision
is judged against. A ladder whose revisions are all judged against Ω₀ is ossifying; one where each Ω
is judged only against its immediate predecessor drifts at a rate the log makes visible.

---

## § 11 — Open problems

**11.1 — Depth weights are not derived.** *D* is reported as the deepest writable element, which
treats a one-parameter policy tweak and a full playbook rewrite as the same level. The system-scale
paper's §10.3 problem (loop-completion weights *w*<sub>i</sub> are estimates by inspection) applies
here unchanged, and the same honest response applies: read *D* as an ordering, not a measurement.

**11.2 — Referee laddering is unvalidated.** §4 proposes judging each revision against its immediate
predecessor. Nothing establishes that a chain of pairwise-non-regressing revisions cannot drift
arbitrarily far from Ω₀ — indeed it plainly can, which may be the intended behavior or may be exactly
the failure mode. The construct makes drift *visible and rate-limited*; it does not bound it. Whether
a bound is wanted is a governance question, and per §10.6 of the system-scale paper neither framework
has a representation of institutions to answer it in.

**11.3 — Other-reach has no completion measure.** §6 bounds *W*<sub>other</sub> to inputs, but a
guide agent that authors the held-out sets its targets are judged against has, in effect, written
their objective. The input/state boundary is sharp for memory and policy and blurry for evaluation
data. This is unresolved and is the most likely place for B-Rule 1 to be violated in practice while
appearing to hold.

**11.4 — Openness may not be binary.** Definition B4 treats Ω ∈ *W* as a switch. A system that tunes
the *weights* of a fixed multi-objective is doing something between closed and open, and the criteria
in §8 do not classify it. A degrees-of-openness treatment is probably needed and is not attempted here.

---

## § 12 — Principles

**B01 — Evaluator externality.** The evaluator, its data, and its record lie outside the write set of
the loop it judges. Every other guarantee in this document reduces to this one.

**B02 — Accumulation is not improvement.** Memory growth is evidence of operation. Only a disjoint
evaluation converts a write into a gain.

**B03 — Depth-monotone gating.** Gate strength, loop period, and per-iteration gain rise together
with write depth. A gate ladder that is not reflected in measured T<sub>δ</sub> is nominal.

**B04 — Concurrency over ascent.** Depths are loops to run simultaneously, not rungs to climb. A
single-depth brain fails predictably: shallow-only never consolidates, deep-only never adapts.

**B05 — Trust inverts ability.** The emptier a loop's self-write set, the more authority it may hold
over others'. Proposer ≠ promoter is the agent-scale form; no agent writes another's self-state is
the fleet-scale form; they are the same rule.

**B06 — Reach stops at inputs.** Other-reach may write another agent's tasks, candidates, and
verdicts, never its memory, policy, or objective.

**B07 — Openness is priced, not free.** An objective-open loop is definable only against a retained
frozen referee. Without one, evolution and drift are observationally identical, and the level is not
advanced but unmeasurable.

**B08 — Report a profile, not a scalar.** Λ is a triple plus an authority ceiling. A single "brain
level" number would reintroduce exactly the false-confidence failure that binary loop-closure framing
produced at system scale.

---

## Relation to prior documents

| Document | Scale | Question |
|---|---|---|
| `SARSI-L_Paper_v3.md` | System | How far has RSI propagated across substrates? |
| `self_awareness/` | Agent | What does an agent *know* about itself? |
| `fleet/` | Fleet | What may one agent assert about another? |
| **This document** | **Brain** | **What may an agent *change* about itself, and when does that count as improvement?** |

SARSI-B adds no new machinery. It reuses SARSI-L's ⟨ι, μ, ν, δ⟩ loop and Definition 3 closure, the
self-awareness paper's admission mask and evidence counts, the fleet paper's self-state prohibition,
and the shipped A0–A4 ceilings and Gate-B promotion path. Its contribution is the write-set axis and
the four results that follow from taking it seriously.

## Version history

**1.0 — 2026-08-22.** Initial. Written in response to a three-level informal taxonomy of LLM brains;
§1 records the conflation it resolves.
