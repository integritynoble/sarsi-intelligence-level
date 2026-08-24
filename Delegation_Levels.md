# Delegation Levels

## How much of a task an agent completes unattended, indexed by what kind of task

*2026-08-24*
*New axis. Relates to: `SARSI_Level_Map.md` (A0–A4 ceilings, λ loop completion), `Designing_Level_Agents.md` §2*

> **Superseded in part.** The material this note shares with
> [`Delegation_Is_A_Property_Of_The_Task.md`](Delegation_Is_A_Property_Of_The_Task.md) — the G0–G4
> grades, the four task coordinates, the acceptance proposition and the §4 illustration table — has
> its home in that paper, which states it with the related work, the cost identity and the
> falsification conditions. This note is retained as the record of how the axis was arrived at. **Edit
> the paper, not this file**; where the two differ, the paper is right.

---

## § 1 — Why this is a separate axis

The corpus already has two things that look like delegation and are not.

**The authority ceiling A0–A4** says what a system *may* do. It is a permission, granted in advance,
and a system may sit far below its ceiling because nobody trusts it yet.

**Loop completion λ** says how much of the *improvement* loop runs without approval. It is about a
system changing itself, not about it doing work someone asked for.

**Delegation is neither.** It asks: *the human states a task; how much of it comes back done, and how
often did they have to intervene?* That is the axis a person actually experiences, and it is not
determined by the other two. An I1 agent working on well-tested code can be delegated more than an I3
agent working on something nobody can check.

**So delegation is worth its own axis precisely because it is not implied by level.**

---

## § 2 — Delegation alone is meaningless; the pairing is the measurement

An agent that completes trivial tasks unattended is not more delegable than one that needs help on
hard ones. A single "delegation level" would hide exactly the thing that matters, which is the same
error as every other scalar this corpus has withdrawn.

> **Delegation is a function, not a level.** $D(\tau)$ is the intervention pattern an agent sustains
> on task class $\tau$. What is reportable is the **frontier**: for each intervention grade, the
> hardest class the agent holds it on.

### The grades

| | Name | What the human does | What comes back |
|---|---|---|---|
| **G0** | Instruction-bound | Specifies each step | The step, executed |
| **G1** | Task-bound, per-action | States the task; approves each action | A task done under continuous supervision |
| **G2** | Task-bound, by exception | States the task; acts only on exception | A task done, plus the exceptions it raised |
| **G3** | Goal-bound | States an outcome, not a method | A result, with the method chosen by the agent |
| **G4** | Mandate-bound | States a standing objective and constraints | Work selected by the agent within the mandate, ongoing |

**G2 is the interesting boundary**, not G4. It is where the *modal* path stops involving a person, and
where the human's cost changes from *per action* to *per surprise*. Everything below G2 scales with
task length; everything at or above it scales with exception rate.

### The task class

$\tau$ needs four coordinates, and the second and third do most of the work:

| | | Why it matters |
|---|---|---|
| **Horizon** | steps, or wall-clock, before a result exists | Long horizons multiply the chance of an unnoticed wrong turn |
| **Verifiability** | can success be checked, how cheaply, and how soon? | §4 |
| **Reversibility** | what does undoing a wrong result cost? | §4 |
| **Novelty** | distance from the agent's demonstrated distribution | Where its evidence stops applying |

Difficulty in the ordinary sense — how hard the thinking is — is mostly captured by horizon and
novelty, and is the *least* predictive of the four.

---

## § 3 — The ceiling: acceptance cannot be delegated to the doer

There is no G5 meaning "no human at all," and the reason is structural rather than cautious.

> **Proposition.** *Delegation of execution scales without limit. Delegation of acceptance does not
> scale — it only transfers. A task accepted by the party that performed it is not completed work but
> asserted work, whatever its quality.*

This is the same result that makes deploy organizational in every improvement loop. Applied here: you
can hand over all of the doing. The moment you also hand over the *accepting*, the loop closes on
itself and the report becomes a tautology.

**What this does not say.** It does not say a human must accept. Acceptance can go to a machine —
a declared test, a separate verifying process, an independent model call with criteria it did not
author. It says only that acceptance must go **somewhere other than the doer**.

So the honest top of the scale is:

> **G4 + independent acceptance.** The agent selects and performs work within a standing mandate; a
> locus that did not perform it decides whether it is done; a human sets the mandate and reviews
> outcomes rather than actions.

That is fully delegated in the sense anyone means it, and it contains no step where a thing grades
itself.

---

## § 4 — What actually caps delegation, and it is not capability

The common model is that delegation rises with capability: smarter agent, less supervision. That is
not what governs it.

> **Delegation is bounded by verifiability and reversibility, not by capability.** People supervise
> not because the agent is likely to be wrong, but because being wrong is expensive to *detect* and
> expensive to *undo*.

The evidence is that the same agent sits at wildly different grades depending only on the task class:

| Task class | Verifiability | Reversibility | Grade reached |
|---|---|---|---|
| Change code with a good test suite | immediate, cheap | `git revert` | **G2–G3** |
| Refactor code with no tests | late, expensive | hard once merged | **G1** |
| Draft a document | subjective, deferred | trivial | **G3** |
| Change production configuration | immediate but partial | costly, sometimes not | **G1**, often **G0** |
| Send an external message | none | **none** | **G0–G1**, correctly |

Capability is constant down that column. The grade moves by two or three steps.

**Three consequences.**

**Raising delegation is mostly an investment in the task class, not in the agent.** Add tests, and the
first row moves. Add a staging environment with a one-command rollback, and the fourth moves. Neither
requires the agent to get better at anything.

**Irreversible actions have a floor.** Where reversibility is zero, no amount of verification
substitutes, because verification after the fact is not a remedy. This is why an external message
belongs at G0–G1 permanently and not until agents improve.

**The measurement is per class and per grade.** Over a class, report the fraction of tasks completed
with no intervention, the number and kind of interventions on the rest, and their cost. Delegation is
measured, not declared — same as every other axis here.

---

## § 5 — How it relates to the other axes

| Axis | Question | Independent of delegation? |
|---|---|---|
| **A0–A4** ceiling | What may it do? | **Yes** — a ceiling is granted; a grade is achieved. A system may hold A3 and operate at G1. |
| **I-level** | What does it change about itself? | **Largely** — an I1 agent on verifiable work out-delegates an I3 agent on unverifiable work |
| **O-level** | What does the structure change about itself? | **Coupled** — independent acceptance is an organizational property, so G4-with-acceptance requires separation |
| **λ** loop completion | How much of the improvement loop runs unapproved? | **Analogous, different object** — λ is delegation of *self-change*, G is delegation of *work* |
| **T_δ** | How long does authorization take? | **Same currency** — the cost of an intervention is a latency, and G2's exception rate times T_δ is the human load |

The last row is the useful one operationally. **A grade plus an exception rate plus T_δ gives the
human cost of running an agent**, which is the number anyone deciding whether to delegate actually
wants.

---

## § 6 — Reporting form

```
G(τ)  = grade sustained on class τ
τ     = ⟨horizon, verifiability, reversibility, novelty⟩
rate  = interventions per task, on that class
kind  = what the interventions were (permission, ambiguity, error, rescue)
accept= who accepts — the doer, a declared test, a separate locus, a human
```

Reporting a grade without its class is the error §2 describes. Reporting a grade without saying who
accepts is the error §3 describes — and it is the one that makes an impressive number meaningless.

---

## § 7 — Open

**The grades are ordinal and the boundaries are soft.** G2 versus G3 depends on how a task was
phrased, and the same work can be stated as a task or as an outcome.

**Verifiability and reversibility are not measured here.** They are used as if they were scalars; they
are at best orderings, and probably multidimensional. A real version of §4's table would need both
quantified, and this document quantifies neither.

**Exception *kind* matters more than rate, and is not modelled.** One rescue from a destructive path
is not equivalent to twenty clarifying questions, and a rate that averages them is misleading in the
direction of comfort.

**Nothing here is measured on a real system.** The table in §4 is constructed from the pattern, not
from logged intervention data — which, per §4's own rule, makes it an illustration and not a finding.
