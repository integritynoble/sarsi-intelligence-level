# What Level `sarsi-claude` Needs

## And where a test it supplies is legitimate, where it is self-certification

*2026-08-24*
*Reads: the internal engineering overview of the `sarsi-claude` layer, and the v3 implementation
plan behind it — cited as **the overview** and **the plan***
*Against: `Designing_Level_Agents.md` §2b, `Two_Axis_Intelligence_Level_Framework_v2.md`*

---

## § 1 — "sarsi-claude" is three roles, and they need different levels

The question *what level does sarsi-claude need* has no single answer because the name covers three
things with different write sets. Separating them is most of the answer.

| Role | What it is | Level it needs | Why that level and not higher |
|---|---|---|---|
| **The motor** | the Claude Code session doing one bounded step | **I0–I1** | It receives a step and returns artifacts. The workspace carries history, so the session need not. |
| **The supervisor** | the composer that detects, steers, error-checks, types the next step | **I1–I2** | Persistent within a run; learns from `resultcheck` findings across rounds |
| **The verifier** | the independent call that issues the verdict | **D0 — empty self-write set** | This *is* its qualification |

**The motor's low level is correct, not a deficiency.** The BrainRSI invariant makes it a *transient*
motor session precisely so that nothing accumulates in it: the brain owns goals, plan state, memory,
budgets and predictions. An executor that learned across sessions would be an executor with a write
set, and the point of the split is that it has none.

**The verifier's low level is the load-bearing one.** A locus qualified to judge another's work must
not be improving itself by the verdicts it issues. The guide states this as *the agent that did the
work never grades it*; the framework states it as an empty self-write set being the only thing that
admits authority over another's promotion. Same rule.

> **So: nothing in `sarsi-claude` needs to be high-level.** The level requirement sits in
> `sarsi-worker` — the brain, at I2 heading to I3 — and the motor's job is to be *reliable and
> forgettable*.

---

## § 2 — What the guide already has

Worth stating before the gap, because most systems have none of it.

**Three tools check, one rules.** `resultcheck`, the declared suite, and `site_parity` produce
evidence and may not issue a verdict; only the verifier may. **Silence is never success** — no tool
can produce a positive verdict by not complaining.

**An evidence ladder.** `L2` is a real exit code, a literal string match on real output, a real
`curl`. `L3` is an independent model call. The distinction between *evidence* and *judgement* is
already typed.

**Declared, never inferred.** `Test command: pytest -q` is declared in the plan and run for real, and
its exit code outranks anything on screen. **This is already the pattern the answer in §3 asks for.**

**Verification ordered above the work.** Step 3 sits before steps 4 and 5, and the guide records why:
a session that kept receiving typed prompts consumed every pass at step 4, so verification starved for
23 consecutive passes while an already-finished session went on being guided. That is the ordering
rule earned rather than assumed.

**Criteria from the plan the owner reviewed** — never from the composer, never from what the session
said about itself. And a stale plan's criteria are withheld rather than applied.

---

## § 3 — Your proposal, split

*`sarsi-claude` should provide the testing method that ensures Claude Code's results are correct and
reliable.*

Right in one reading, and self-certification in another. The distinction is §2b of the design spec:
**a write set includes whatever determines what the evaluation sees.**

| Reading | Verdict |
|---|---|
| The motor **writes test code as an artifact** | **Legitimate.** That is implementation — the μ step. Tests are a deliverable like any other. |
| The motor or composer **proposes a test method, declared before the work and frozen for the run** | **Legitimate, and what you want.** This is exactly the existing `Test command:` pattern extended to per-phase criteria. |
| The motor **selects which test runs after seeing its own results** | **Self-certification.** Nothing edits the criterion; what moves is which evidence reaches the judge. §2b. |
| The composer **decides a phase is done** in the same call that chooses what to type next | **Self-certification** — and the guide already says so. |

That last row is not hypothetical. The guide names it plainly:

> *which phases are done is still decided by the composer, in the same call that chooses what to type
> next. That is the agent grading its own progress, and true per-phase verification remains unbuilt.*

**So the answer to your question is yes, with an ordering constraint that does all the work:**

> A test `sarsi-claude` supplies is trustworthy exactly when it is **declared before the work it will
> judge, and cannot be changed by the party doing that work.** A test proposed after seeing results,
> or selected from among several by the executor, measures the executor's judgement rather than the
> artifact.

The mechanism already exists for the suite level. What it does not yet cover is per-phase completion,
which is where the hole is.

---

## § 4 — The concrete fix, in the system's own idiom

**Move phase completion out of the composer call.** Today one call chooses the next instruction *and*
decides which phases are done. Split it: the composer proposes `phase_k complete`, and the verifier —
which already exists, already has a fixed contract, already receives `plan_criteria()` — returns the
verdict per phase. The composer never writes `done`.

**Let the motor propose a phase's test, and freeze it at plan time.** Extend the `Verified when:` line
so a phase may carry a machine-checkable command alongside the human-readable criterion. The motor may
*draft* it — that is useful, it knows the codebase — but it enters the plan the owner reviews, and
from that point neither the motor nor the composer may alter it for the run. Declared, never inferred,
applied per phase rather than once per project.

**Keep the L2/L3 split at the phase level.** The declared per-phase command yields an exit code (`L2`)
that outranks anything on screen; the verifier's independent call (`L3`) rules on whether the
criterion is met. Neither replaces the other, and the ordering already established at project scope
carries down unchanged.

**And test the guard by breaking it.** Construct a phase whose declared test passes while the phase
criterion is unmet — a test that asserts nothing, or asserts on a file the phase did not produce — and
confirm the verifier still refuses. §2b's rule applies here directly: a guard that has only ever
passed is one nobody has reason to trust.

---

## § 5 — What this changes about levels

Nothing about the motor. It stays I0–I1, and should.

**The verifier's independence becomes load-bearing at a finer grain.** At project scope one verdict
per run is one opportunity to self-certify. At phase scope it is one per phase, so the same guard is
exercised far more often — which is an argument for the fix and also the reason to test it
adversarially first.

**The composer moves from I2 toward the operator role proper.** Stripped of the completion verdict it
proposes and never rules, which is what an operator is: a source of evidence, not of verdicts.

**And the organizational reading improves.** The roster is brain (proposer), motor (executor),
verifier (referee), owner (promoter). Separation currently holds at project scope and leaks at phase
scope. Closing the leak is what takes this structure from *separated in principle* to *separated where
the decisions actually happen* — which, per the framework's gating rule, is the difference between an
organizational level and a claim to one.
