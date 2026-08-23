# The BrainRSI Plan, Read as a Level Build

## Where `sarsi-worker` v3 lands on the individual and organizational axes, and what the remaining delta is

*2026-08-23*
*Plan: `singularity/docs/plans/2026-08-20-sarsi-worker-sarsi-claude-brainrsi-plan.md` (v3, 1367 lines)*
*Against: `Designing_Level_Agents.md`, `Two_Axis_Intelligence_Level_Framework_v2.md`*

---

## § 1 — The answer

**They do not merely combine. The plan is the level specification instantiated for one agent**, and on
three points it is ahead of the specification rather than behind it.

The design spec says an LLM can build the mechanism for any level but cannot design three things: the
evidence a level was reached, its own referee, or its own separation. **The plan supplies all three
from the architecture rather than from the agent**, and states them as a non-negotiable invariant:

> The brain plans; Claude Code executes; an independent mechanism verifies.
> A task executor does not decide that its own artifact satisfies the phase criterion.
> The authority kernel remains outside mutable cognition.
> Cross-agent communication is evidence-bearing: `{claim, evidence_refs, provenance, scope, status}`.
> Raw private memory is not shared across agents.

Those five lines are, in order: separation of proposal from execution from verification; proposer ≠
referee; evaluator outside the write set; evidence-bearing promotion; and memory does not cross agents.
The framework arrives at each of them by argument. The plan asserts them as invariants and builds
around them, which is the correct relationship — a level is conferred by the harness, not claimed by
the agent.

---

## § 2 — The state vector is a write-set decomposition

The plan's target state is

```
Σ_worker = { O, E, S, P, I, Q, M, Θ }
```

and it maps onto the level axes without adjustment:

| Plan | What it is | Level component |
|---|---|---|
| `E` episodic | event/decision episodes, fast append | **I1** — persistence |
| `S` semantic | promoted facts and lessons, **slow and versioned** | **the I1→I2 boundary**; promotion is what makes it learning rather than logging |
| `P` procedural | **verified callable** workflows and skills | **D3 skill** — and cognitive compression, in the sense that a verified workflow is expensive cognition made cheap to execute |
| `I` intentional | goal, plan, phase, dependencies, checkpoints | I1 task state |
| `Q` self model | capability, authority view, calibration, freshness, health | the self-state coordinates, with the no-self-promotion invariant preserved |
| `M` world model | environment and task expectations, calibration | the predictive half of I2 |
| **`Θ`** | **mutable cognitive instrument: gate / retrieval / consolidation policy** | **the I3 write set, already carved out** |

Two things about this are worth stating plainly.

**`Θ` is the I3 object, named and separated before it is used.** The design spec says the I3
prerequisite is that the cognitive mechanism be pulled out of hard-coded logic into versioned
configuration, because *you cannot improve what is hard-coded*. The plan does that in its target state
— retrieval, gating, and consolidation policy are one named object distinct from the memory they
operate on. The separation of `Θ` from `S`, `E`, `P` is exactly the separation of mechanism from
content, which is the I2/I3 line.

**The context is a bounded projection, not the state.** `W_t = Gate_B(...)` with mode-awareness means
what reaches the model is selected, and long-term memory is inert until selected. This is the aperture
constraint of the individual axis, implemented: an individual is bounded not by what it knows but by
how much can be present at once, and the plan budgets that explicitly rather than letting the store
grow into the prompt.

---

## § 3 — The phases are a level trajectory, in the right order

| Phase | What it builds | Level position |
|---|---|---|
| **M1** | Event-sourced `assert/revoke/supersede`, scope, secret refusal | **I1 made sound** — provenance and supersession, not just storage |
| **M2** | Self staleness, gated workspace, hybrid retrieval, replay | I1 complete, **plus the evaluator built first** |
| **M3** | Forecast registered *before* delegation; durable plan executive | **I2 calibration** — the prediction ledger |
| **M4** | ACP motor path; criterion-specific deterministic verification | **the ν infrastructure** |
| **M5** | Event-driven episodic learning, semantic consolidation, proceduralization | **I2 achieved** |
| *(absent)* | `Θ` as the write set of a governed loop | **I3** |

Three details in that ordering are better than the specification.

**M2.2 builds the benchmark before the thing it benchmarks.** *"Build a frozen retrieval benchmark
before enabling semantic embeddings."* The design spec names the missing ablation as the most-skipped
measurement in current systems and says to build the harness at the same time as the store. The plan
goes further and builds it **first**, which is the only ordering that cannot be rationalized after the
fact. Freezing it is what makes it an evaluator rather than a scoreboard.

**M3 registers the forecast before the delegation, not after.** A prediction recorded after the
outcome is a rationalization; the plan requires registration to occur before `ses.assign()`. That is
the difference between a calibration record and a story.

**M4 executes an explicit criterion declared before execution**, whitelisted and small, and the plan
is emphatic that it is *not* a generic "scan and declare pass" helper. Predeclared criteria are the
framework's definition of improvement — *better under an independent, predeclared evaluation* — turned
into a code path.

**And M5 draws the I2/I3 line itself.** The plan says: *"This is pre-RSI learning. It changes memory
content, not the mechanism that evaluates self-modification."* That is the I2/I3 boundary stated
exactly, by the plan, without the framework's vocabulary. **The plan knows where it stops**, which is
rarer and more valuable than reaching further.

---

## § 4 — Where it lands

**Individual: I2, with the I3 substrate carved out and not yet loopable.**

Complete on the plan's own terms: persistence with provenance and supersession (M1), a self model with
staleness and no self-promotion (M2), calibration through pre-registered forecasts (M3), deterministic
verification against predeclared criteria (M4), and learning that changes content (M5). `Θ` exists as
a named object; nothing yet proposes changes to it, scores them, or promotes them.

**Organizational: O1, structured to go higher.**

The roster is proposer (`sarsi-worker`), executor (`sarsi-claude`), verifier (independent mechanism),
promoter (owner). **Separation holds**, which is the gate — a structure without it is O1 plus
unverified claims regardless of what else it does, and this one has it architecturally. What is
present is persistence: shared state, roles, commitments, evidence-bearing messages. What is absent is
the O2 instrument — a **reliability ledger per member per task class**, measured rather than declared,
with routing that reads it.

---

## § 5 — The delta

### To reach I3, five pieces on top of M5

1. **Version `Θ`, with snapshot and rollback.** It is named; it must also be a versioned object with a
   last-known-good and a restore path, and the restore itself recorded.
2. **A candidate generator over `Θ`** — bounded, clamped, deterministic. The research agents' history
   is the warning here: a first autonomous night ran correctly and found nothing because nothing
   proposed a variant, and every round scored the incumbent against itself.
3. **A held-out set disjoint from the search set.** M2.2's frozen retrieval benchmark is the right
   shape and the wrong scope for this — it benchmarks retrieval, not `Θ`'s contribution to task
   outcome. A `Θ`-level split is a second artifact.
4. **A promotion gate the worker cannot invoke.** The owner signature path already exists elsewhere in
   the system; wire `Θ` promotion through it.
5. **`NO_CHANGE` as a valid outcome.** Without it the loop manufactures improvements — not from
   malice, but because that is what optimisation does when the shortest path to a better number runs
   through the definition of better.

### To reach I4, two more

6. **The improvement process itself versioned** — the candidate generator, acceptance rule, and
   stopping rule as configuration.
7. **IC per generation** — validated downstream gain divided by proposal and evaluation cost. The
   denominator is what makes it honest.

### To reach O2, one

8. **A measured reliability ledger** per member per task class, with routing that reads it. The
   forecast machinery in M3 already produces the raw material: registered expectation versus realized
   outcome is a calibration record per member, and a reliability ledger is that record aggregated.

### And the one that is not optional

9. **The I1→I2 ablation.** Same task family, same budget, memory on versus off, held out from the
   episodes that produced the entries. The plan's M5 will produce learning; nothing currently measures
   whether it helped. Until it is run, I2 is a design claim.

---

## § 6 — One tension worth flagging

The plan's §2.8 requires that *a brain architecture must not make simple chat expensive*, and adds a
mode-aware fast path where ordinary conversation bypasses long-term retrieval and action machinery.
This is correct as engineering and it interacts with the level claims.

**Levels are earned on the slow path, and most turns take the fast one.** An agent whose `CHAT` mode
skips retrieval, forecasting, and verification is operating at I0–I1 for those turns regardless of
what its `ACTION` mode is capable of. That is the right design — the alternative is paying I3 costs to
answer *why?* — but it means the agent's level is **mode-indexed**, and a single figure describing it
would be wrong in both directions.

The honest reporting form is per mode: `CHAT` at I1, `ACTION` at I2 heading to I3. This is not a
defect in the plan. It is a place where the framework, which assigns one level per agent, is coarser
than the system it is describing.

---

## § 7 — What this does not establish

**That the plan will work.** It is a plan; M0–M5 are unbuilt. Everything above reads intent against a
framework, which is the same category of evidence as an architecture diagram.

**That the level assignments are measured.** They are read off the design. Every one of them is a
target until the corresponding test in §5 is run, and §5.9 exists precisely because the cheapest of
those tests gates all the others.

**That separation holds in the built system.** The invariant is stated; whether the verifier is
genuinely outside the worker's write set is a property of the implementation, and the plan's own
§3 requires the current-state assumptions to be re-audited before coding. That audit is where the
question gets answered.
