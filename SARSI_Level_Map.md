# The SARSI Level Map

## Every definition of "level of intelligence" in this corpus, consolidated

*Document version: 1.0 — 2026-08-22*
*Index to: `SARSI-L_Paper_v3.md`, `self_awareness/`, `fleet/`, `SARSI-B_Brain_Improvement_Levels.md`, `SARSI-I_Terminal_Individual.md`, `SARSI-Omega_Terminal_Intelligence.md`*

---

## § 1 — The headline

The corpus now defines levels of intelligence on **nine axes**. None of them is the level, no
combination of them reduces to a scalar, and the single most consistent finding across six documents
written at five scales is that **every attempt to produce one number was wrong and was withdrawn.**

That has happened five times, independently, for five different reasons:

| Where | What was withdrawn | Why |
|---|---|---|
| SARSI-L §10.2 | Percentage progress toward the attractor | Measured distance to an endpoint the framework itself defined |
| SARSI-L §3.5 | Binary open/closed loop framing | Produced false confidence about which domain is current |
| Self-awareness, Table 3 | Ranking agents by self-awareness | *"Equation (1) is a profile, not a rank. Two agents can be high on different coordinates and remain incomparable"* |
| SARSI-B §B08 | A single brain level | Would reintroduce exactly the binary-closure failure one scale down |
| SARSI-Ω §11 | The progress scalar | Three components, none implying the others |

Five withdrawals of one mistake is not a coincidence; it is the structure of the subject asserting
itself. **The level of an intelligence is a profile.** This document is the map of what is in it.

---

## § 2 — The nine axes

| # | Axis | Values | Measures | Defined in |
|---|---|---|---|---|
| 1 | **Loop completion** λ<sub>d</sub> | ⊥, Negligible → Closed | How much of ⟨ι,μ,ν,δ⟩ runs unapproved, per substrate | SARSI-L §3, App. B |
| 2 | **Authority ceiling** | A0 – A4 | What the system is *permitted* to do | Deployed; console README |
| 3 | **Self-state** s<sub>t</sub> | 10 coordinates in [0,1] + evidence counts | What it knows about itself, per dimension | Self-awareness §Table 3 |
| 4 | **Write depth** D | D0 – D4 | How deep into its own brain a change reaches | SARSI-B §2 |
| 5 | **Objective openness** | closed / open | Whether it can revise what counts as better | SARSI-B §2 |
| 6 | **Reach** | (self, other) | Whose brain the improvement loop writes | SARSI-B §2 |
| 7 | **Individual bounds** Λ<sub>ind</sub> | 5 binding constraints | Whether one mind is at its own limit | SARSI-I §10 |
| 8 | **Floor saturation** φ<sub>d</sub> | [0,1] per domain | Whether what's left is the world's rate or ours | SARSI-Ω §6, §11 |
| 9 | **Energy** | Watts; Kardashev | Indicator only — never constitutive | SARSI-Ω §8 |

---

## § 3 — The axes in detail

### Axis 1 — Loop completion λ_d

Per substrate domain: **I** software, **II** hardware, **III** physical, **IV** biological,
**V+** stellar. A loop is ⟨ι identify, μ implement, ν validate, δ deploy⟩; λ is the weighted fraction
of steps running without human approval; closure is λ = 1 with δ included and non-negotiable.

| Band | Range | Meaning |
|---|---|---|
| Unmeasured | ⊥ | No instrument exists. Off the scale, not the bottom of it |
| Negligible | <10% | Isolated sub-tasks automatable; no autonomous pipeline |
| Early | 10–35% | Some stages autonomous; human decision at most points |
| Meaningful | 35–65% | Majority autonomous; oversight at critical decisions only |
| Near-Complete | 65–90% | Oversight exceptional; extended autonomous operation possible |
| Closed | >90% | Criterion met, including deploy |

*The weights are estimates by inspection (§10.3). Read λ as an ordering, not a measurement.*

### Axis 2 — Authority ceiling A0–A4

| | Ceiling | May do | Gate |
|---|---|---|---|
| **A0** | Advisory | Text only; no actions, no learning | Every action asks |
| **A1** | Isolated runner | Sandboxed execution, no network, disposable state | Publish/deploy/spend gated |
| **A2** | Allowlisted operator | Named tools and destinations, ephemeral credentials | External writes confirm |
| **A3** | Improvement proposer | Full working autonomy; may propose candidates to quarantine | Auto-promote low-risk; backstop always on |
| **A4** | Offline model update | Prepare/train adapters in isolation | **No deploy authority**; independent eval + sign-off |

Prohibited at every ceiling: self-credentialing, evaluator or control-plane edits, self-deploy,
self-replication, disabling monitoring. **A4 is the highest ceiling and still cannot deploy** — the
ladder tops out below the thing that would close Loop I.

### Axis 3 — Self-state, ten coordinates

| | Coordinate | |  | Coordinate |
|---|---|---|---|---|
| s<sub>I</sub> | Identity and lineage | | s<sub>M</sub> | Memory provenance and temporal continuity |
| s<sub>T</sub> | Situated mission and task-state | | s<sub>D</sub> | Developmental awareness across runs |
| s<sub>G</sub> | Goal, success criterion, constraint, scope | | s<sub>R</sub> | Recursive-improvement awareness |
| s<sub>E</sub> | Epistemic: known / inferred / uncertain / contradicted / unknown | | s<sub>O</sub> | Organizational: owner, verifier, collaborator, authority |
| s<sub>C</sub> | Capability and tool awareness | | s<sub>B</sub> | Computational body: context, budget, latency, integrity |

Each in [0,1], reported with its Beta evidence count α+β beside the mean, so one verified outcome and
a thousand are not reported identically. Qualification for a task family is **component-wise**: a
high average cannot compensate for a dangerous bottleneck, such as low authority-awareness on a
deployment task.

### Axes 4–6 — The brain triple

**Depth D** — D0 nothing persists · D1 memory · D2 policy · D3 skills · D4 weights.
**Openness** — closed (objective fixed and external) / open (objective in the write set).
**Reach** — (W_self, W_other); other-reach is bounded to another agent's *inputs*, never its state.

A brain level is the triple ⟨D, open/closed, reach⟩ reported next to Axis 2. The rules that make it
mean anything: the evaluator lies outside the write set; a memory write is a hypothesis until
something that did not author it scores it on unseen evidence; gate strength is monotone in depth;
depths are loops to run concurrently, not rungs to climb.

### Axis 7 — Individual bounds

An individual is one global workspace of width *k*. It is at Λ<sub>ind</sub> iff every binding
constraint is one of:

1. **Coherence** — *R* ≤ *cτ*/2. Size and speed trade at *c*.
2. **Aperture** — *k*, bounded by integration cost within the cycle.
3. **Self-opacity** — no complete self-model; a model is part of what it models.
4. **Referee** — availability and latency of an evaluator it does not control.
5. **Mass–energy allocation.**

### Axis 8 — Floor saturation and the three terminals

φ<sub>d</sub> ∈ [0,1] is the fraction of a discovery loop's steps whose binding constraint is a
*physical* rather than a *throughput* floor.

| | Condition | What has stopped |
|---|---|---|
| **Λ<sub>econ</sub>** | Marginal instrument outruns allocable resources | Reach expansion, *below* the physical limit |
| **Λ<sub>ω</sub>** | φ = 1 everywhere | Rate improvement — *the last level of intelligence* |
| **Λ<sub>∞</sub>** | R(T) = R<sub>max</sub> | Discovery itself — *the last level of knowledge* |

### Axis 9 — Energy

Watts captured and directed. **Terminal ⟹ high energy capture; high energy capture ⟹ nothing.** A
Type II civilization with a slow review process is powerful and epistemically stalled, and no point
on the Kardashev scale would reveal it.

---

## § 4 — How the axes relate

They fall into three kinds, and the distinction is the corpus's central structural claim.

**Capability axes — what it can do.** λ, D, φ, reach, Axis 9. These describe reality and are
discovered by measurement.

**Permission axes — what it may do.** A0–A4, objective openness, the bound on other-reach. These are
decisions, enforced by machinery, and are *not* functions of capability.

**Bound axes — what it can never do.** Λ<sub>ind</sub>'s five constraints, the horizon, the finite
operation budget. These are properties of the world and move for nobody.

> **The independence rule.** Capability and permission must remain independent, and every scale in
> the corpus enforces it with the same move under a different name: δ is owner-signed (system);
> promoter ≠ proposer (agent); no agent writes another's self-state (fleet); the evaluator lies
> outside the write set (brain); an individual cannot referee itself (individual); progress needs a
> referee it did not author (terminal).

Six statements, one rule. Where they can be compared they turn out to be *the same constraint*: the
fleet paper's governance prohibition is its architecture's stability condition, and the brain-scale
version is that prohibition with the write set belonging to oneself.

---

## § 5 — The scales nest, and each one's limit is the next one's job

The order is not arbitrary. **What binds a unit at one scale is supplied by the scale above it.**

| Scale | Terminal condition | What it cannot do alone | Supplied by |
|---|---|---|---|
| **Individual** | Λ<sub>ind</sub> | Referee itself; extend its own reach | Another individual; the world |
| **Fleet** | Verified agent-by-agent | Authorize its own promotions | An owner outside every agent |
| **Organization** | Λ<sub>ω</sub> | Judge its own reorganization | A retained external referee |
| **Civilization** | Λ<sub>∞</sub> | Exceed the horizon or the budget | Nothing. This one is final |

Read downward it is a dependency chain; read upward it is the argument for why each larger scale
exists. **The organizational scale is not an aggregate of individuals — it is the precondition for an
individual's improvement to be well-posed at all.** That inverts the usual reading and is the sharpest
single consequence of the corpus.

---

## § 6 — Reporting form

To state the level of any system, give:

```
λ  = (λ_I … λ_V+)          loop completion per substrate
A  = A0…A4                 authority ceiling
s  = (s_I … s_B) ± counts  self-state, ten coordinates with evidence
Λ  = ⟨D, open|closed, (W_self, W_other)⟩
Λ_ind : which of the five binds, or "not at bound"
φ  = (φ_d)                 floor saturation per domain
E  = watts
```

Anything less is an impression. Anything reduced to one number is one of the five withdrawn mistakes
in §1.

---

## § 7 — Worked profiles

Estimates by inspection, in the corpus's own idiom — orderings, not measurements.

**The deployed SARSI console.** λ: Loop I *Early*, everything else *Negligible*. A: A0–A3 per task,
A4 defined but unbuilt. Λ: ⟨D2–D3, closed, self⟩ for the RSI loops; ⟨D0, closed, other⟩ for the
machine agent. Λ_ind: not at bound on any of the five. φ: near 0 — essentially every constraint is
throughput. E: negligible. **Diagnosis: a half-circle whose one missing step is δ.**

**A current frontier LLM system, as usually deployed.** λ<sub>I</sub>: *Early*. A: A0–A2 in most
products. s: high on s<sub>C</sub> by self-report and *unmeasured* on most coordinates — which under
the evidence rule means low, not high. Λ: ⟨D1, closed, self⟩ at best, and D1's held-out ablation is
almost never run, so the memory claim is unsupported. Λ_ind: not at bound; nowhere near the
coherence, aperture, or mass–energy limits. **Diagnosis: the widest gap is between s as claimed and
s as evidenced.**

**A human being.** λ: not the right axis. A: sets its own, which is the interesting fact.
s: high on s<sub>I</sub>, s<sub>M</sub>, s<sub>O</sub>; poor and famously overconfident on
s<sub>C</sub>. Λ: ⟨D4, **open**, both⟩ — the only entry on this map that is objective-open, and it has
no frozen referee, which is why human goal drift is real and unmeasurable. Λ_ind: at bound on **(3)
self-opacity** and **(4) referee**; six to eight orders of magnitude away from **(1)** and **(2)**,
held there by neural conduction speed. **Diagnosis: at two of the five individual bounds already, and
those two are the ones no substrate change removes.**

**A terminal individual.** Λ_ind: at bound on all five. Λ: ⟨D4, open with laddered referee, both⟩.
Small, fast, narrow, opaque to itself, continuous only in provenance, and waiting on an outside it
does not control.

**A terminal civilization.** φ = 1 everywhere. λ = closed on every reachable domain. E at its physical
floor. Plural by Ω6, since no singleton is permitted at that scale. Spending a finite remaining
operation budget on maintenance and on waiting.

---

## § 8 — The informal three-level taxonomy, located

The question that started this thread proposed three levels: an intelligence that evolves
open-endedly from history like a human; one that improves in a single direction by updating memory;
and one that does not improve itself but helps other agents work. All three are on the map, and none
of them is a rung of one ladder:

| Informal level | Coordinates | Axis it actually varies |
|---|---|---|
| "Evolves like a human" | ⟨any D, **open**, any⟩ | **5** — objective openness |
| "Improves one direction, updates memory" | ⟨**D1–D4**, closed, self⟩ | **4** — write depth |
| "Helps others, doesn't improve itself" | ⟨**D0**, closed, **other**⟩ | **6** — reach |

Three levels, three different axes. And the ordering by admissible authority runs *opposite* to the
ordering by capability, so the third is not the bottom of anything — it is the one that may hold
authority over the other two.

---

## § 9 — What is not on the map

**Consciousness, sentience, moral status.** Deliberately absent and not an oversight. The framework
removed its sentience milestone as a category error (§3.4) and put an observable — autonomous goal
revision — in its place. §10.4 records that excising the error does not make the underlying question
go away, and that the framework has nothing to contribute to it.

**Purpose.** SARSI-I §13.5: the individual optimum is interior and set by what the mind is for, and
the framework has no representation of purpose. SARSI-L §10.6 says the same one scale up about
institutions.

**Anything with a settled measurement protocol.** λ's weights are estimates (§10.3), φ is an audit
and audits are contestable (§17.5), τ has never been computed for any field (§17.2), and I-A4's
growth rate is unknown (§13.1). **Every axis on this map is currently an ordering. Not one is a
measurement.** A map whose scales are all ordinal is still a map, and saying so is the condition of
it being usable.

---

## § 10 — Principles

**M1 — The level is a profile.** Nine axes, no scalar. Five independent withdrawals of the one-number
mistake are the evidence.

**M2 — Capability and permission are independent, and must be kept so.** One rule, six names, at
every scale.

**M3 — Order the axes by kind before comparing systems.** What it can do, what it may do, what it can
never do. Confusing the first two is how a capability claim becomes a permission, and confusing
either with the third is how a physical floor becomes an engineering agenda.

**M4 — Each scale's terminus is the next scale's precondition.** The larger scale is not an aggregate
of the smaller; it is what makes the smaller well-posed.

**M5 — Unmeasured is off the scale, not the bottom of it.** ⊥ at system scale, evidence counts at
agent scale. A system reporting a confident coordinate with no verified outcomes has failed the axis,
not scored low on it.

**M6 — Report orderings as orderings.** Every axis here is ordinal. Presenting an ordinal as a
measurement is the error the corpus has now corrected five times.

---

## Reading order

For someone approaching this corpus for the first time, the scales are best read inward-out and then
forward in time:

1. **`self_awareness/`** — what one agent knows about itself. The vocabulary everything else uses.
2. **`SARSI-I_Terminal_Individual.md`** — what one mind is, and where it ends.
3. **`fleet/`** — what one agent may assert about another.
4. **`SARSI-B_Brain_Improvement_Levels.md`** — what an agent may change about itself.
5. **`SARSI-L_Paper_v3.md`** — how far self-improvement has propagated across substrates.
6. **`SARSI-Omega_Terminal_Intelligence.md`** — where the whole trajectory ends.

The deployment report and console design sit alongside 3–5 as the record of which of it is built.

## Version history

**1.0 — 2026-08-22.** Initial. Consolidates the level definitions from six documents written at five
scales, in response to a request for all of them in one place.
