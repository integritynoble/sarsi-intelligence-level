# Delegation Is a Property of the Task

## Grades of unattended completion, the acceptance ceiling, and why capability is the wrong lever

*Working paper — 24 August 2026*
*Companion to: `Two_Axis_Intelligence_Level_Framework_v2.md`, `SARSI_Level_Map.md`*

---

## Abstract

Discussion of agent autonomy is dominated by a model in which delegation rises with capability:
a better agent needs less supervision. This paper argues the model is wrong in a way that misdirects
effort, and that the correct account has two parts.

**Delegation is bounded by the task's verifiability and reversibility, not by the agent's
capability.** People supervise not because an agent is likely to be wrong but because being wrong is
expensive to *detect* and expensive to *undo*. Holding capability constant, the same agent sits two
or three grades apart across task classes that differ only in those two properties. The practical
consequence is that raising delegation is mostly an investment in the task class — tests, staging,
one-command rollback — rather than in the agent.

**Acceptance cannot be delegated to the doer.** Delegation of execution scales without limit;
delegation of acceptance does not scale, it only transfers. A task accepted by the party that
performed it is asserted work rather than completed work, whatever its quality. So there is no
top grade meaning "no human at all": the honest ceiling is a standing mandate with execution fully
delegated and acceptance held by a locus that did not perform the work — which may be a machine, but
not the same machine.

We give five grades of intervention pattern, a four-coordinate characterization of task class, and a
cost identity — human load is exception rate times authorization latency — that yields the number
someone deciding whether to delegate actually wants. The nearest prior art is the operational design
domain of automotive automation standards, which already indexes autonomy by domain; our contribution
is to identify *which* domain properties bind, and to show they are not properties of the automation.

---

## 1. Introduction

### 1.1 The prevailing model, and what it predicts

The common account of agent autonomy is a single ladder: as systems get more capable, they need less
supervision, and delegation is a readout of capability. It predicts that the way to obtain unattended
operation is to improve the agent, that a given agent has *a* level of autonomy, and that progress on
benchmarks translates into reduced supervision.

All three predictions fail in ordinary practice. The same agent, unchanged, is trusted to modify code
under a good test suite and not trusted to send an email. No benchmark distinguishes those tasks by
difficulty; they are distinguished by what happens when the agent is wrong.

### 1.2 The question

Given that a person states a task and an agent attempts it: **what determines how much comes back
done, and how often the person had to intervene?**

This is deliberately narrower than "how autonomous is the system." It is the question a person
answers implicitly every time they decide whether to watch.

### 1.3 Contributions

1. **A grade scale** (§3) for intervention pattern, G0–G4, with the observation that the significant
   boundary is at G2 — where the human's cost changes from per-action to per-surprise — rather than
   at the top.
2. **A task-class characterization** (§4) in four coordinates, of which verifiability and reversibility
   do most of the work and ordinary difficulty does least.
3. **The acceptance ceiling** (§5): delegation of acceptance transfers rather than scales, so no grade
   corresponds to "unattended including acceptance."
4. **The task-boundedness result** (§6): delegation is capped by properties of the task class, not of
   the agent, with the consequence that the effective lever is the class.
5. **A cost identity** (§7) making delegation an operational quantity rather than a description.

### 1.4 What this paper does not claim

**It does not say capability is irrelevant.** Capability determines whether a task can be done at all,
and sets the exception *rate* within a class. It does not set the *ceiling*, which is what §6 is about.

**It is not a safety argument.** The results are about what a delegation claim means. They would hold
in a world with no risk, because the acceptance ceiling is about the definedness of "done," not about
harm.

**The task-class table in §6 is constructed, not measured.** It is an illustration of the pattern, and
§10 says what would make it a finding.

---

## 2. Related work

**Levels of automation.** Sheridan and Verplank's ten-level scale is the ancestor of every ladder in
this area, and describes how decision authority is shared between human and computer. Its levels are
ordered by *who decides*, which is the right question for the setting it came from — supervisory
control of a known plant — and under-determines the question here, where the same system occupies
different levels on different tasks.

**Types and levels.** Parasuraman, Sheridan and Wickens observed that automation is not one thing and
should be applied at different levels to different *stages* — information acquisition, information
analysis, decision selection, and action implementation. This is the closest prior insight to §5: their
separation of decision selection from action implementation is the separation that makes acceptance
special. We take their stage decomposition and add that one stage, acceptance, cannot be assigned to
the same agent as implementation without the report becoming self-certified.

**Levels of AGI.** Morris et al. propose a capability × autonomy grid and separate the two
explicitly, which is the published statement closest to this paper's framing. Their autonomy column is
nonetheless read off the system: a level is something the system *has*. §6 is the disagreement. The
same system occupies several autonomy rows simultaneously, one per task class, so the grid needs a
third index — and once it carries one, autonomy stops being a coordinate of the system at all.

**Operational design domain.** Automotive automation standards index autonomy by ODD: a level-4 system
is level-4 *within a stated domain*, and outside it the claim does not apply. **This is already
half of this paper's thesis**, and the interesting fact is that the idea rarely survives leaving
driving. Discussions of agent autonomy routinely report a level with no domain attached. Our
contribution here is not the indexing — that is J3016's — but the identification of *which* domain
properties bind, and the observation that they are properties of the task rather than of the
automation.

**Trust and reliance.** Lee and See's account of trust in automation as calibrated reliance is the
descriptive counterpart to §6: people rely more where they trust more, and trust is calibrated by
experience of failure. §6 is a claim about what *should* calibrate it — the cost of detecting and
undoing a failure, rather than its frequency — and predicts that reliance tracks reversibility even
where reliability is equal.

**Mixed-initiative and adjustable autonomy.** Horvitz's mixed-initiative principles describe the
exception-driven interaction that G2 names, including the expected-value reasoning about when to
interrupt. The adjustable-autonomy literature treats autonomy as a per-context dial rather than a
system property, which §4 formalizes as the task-class index.

**Irreversibility and coupling.** Perrow's analysis of tightly coupled systems supplies the mechanism
behind §6's floor: where recovery is not possible after the fact, safety must come from prevention,
and supervision is prevention. This is why some classes have a delegation floor that no verification
removes.

**Loop autonomy.** Amdahl's speedup bound transposed to loop autonomy gives §7's cost identity: the
un-automated fraction dominates, and here the un-automated fraction is the exception.

---

## 3. Grades

> **Definition 1 (delegation grade).** The intervention pattern an agent sustains on a task class.

| | Name | The human | What returns |
|---|---|---|---|
| **G0** | Instruction-bound | Specifies each step | The step, executed |
| **G1** | Task-bound, per-action | States the task; approves each action | A task done under continuous supervision |
| **G2** | Task-bound, by exception | States the task; acts only on exception | A task done, plus the exceptions raised |
| **G3** | Goal-bound | States an outcome, not a method | A result, method chosen by the agent |
| **G4** | Mandate-bound | States a standing objective and constraints | Work selected by the agent within the mandate |

### 3.1 The significant boundary is G2, not G4

Below G2 the human's cost scales with **task length**: more steps, more approvals. At and above it,
cost scales with **exception rate**: more surprises, more interruptions. That is a change of kind, and
it is where delegation starts to pay.

The boundary is also where the failure mode changes. Below G2, failures are caught at the action that
caused them. At G2 and above, a failure is caught when something raises an exception — so the design
question becomes *what raises exceptions*, and a system that fails silently has not achieved G2 but
has stopped reporting.

> **Silence is not success.** A grade claimed on the basis of few interruptions, without a positive
> account of what would have interrupted, is a measurement of the alarm and not of the work.

### 3.2 The grades are ordinal and soft

G2 versus G3 depends partly on phrasing: the same work can be stated as a task or as an outcome. The
scale orders intervention patterns and does not measure them, and §10 treats this as a limitation
rather than a detail.

---

## 4. Task class

> **Definition 2 (task class).** $\tau = \langle$ horizon, verifiability, reversibility, novelty $\rangle$.

| Coordinate | | Role |
|---|---|---|
| **Horizon** | steps or wall-clock before a result exists | Long horizons multiply the chance of an unnoticed wrong turn, and delay detection |
| **Verifiability** | can success be checked, how cheaply, how soon? | Sets what an exception can be raised *on* |
| **Reversibility** | what does undoing a wrong result cost? | Sets what an exception is *worth* |
| **Novelty** | distance from the agent's demonstrated distribution | Where its evidence stops applying |

**Ordinary difficulty is the least predictive coordinate.** How hard the thinking is affects the
exception rate; it does not affect the ceiling. A hard task that is cheap to check and cheap to undo
is more delegable than an easy one that is neither.

**Verifiability and reversibility are not the same property**, and conflating them is a common error.
Verifiability determines whether you *learn* you were wrong; reversibility determines whether it
*matters*. A task that is cheap to check and impossible to undo — an irreversible action with an
immediate signal — is worse than one that is expensive to check and trivially undone.

---

## 5. The acceptance ceiling

> **Proposition 1.** *Delegation of execution scales without limit. Delegation of acceptance does not
> scale; it transfers. A task accepted by the party that performed it is asserted work, not completed
> work, whatever its quality.*

*Argument.* Acceptance is the judgement that a result meets its criterion. If the accepting party is
the performing party, the criterion sits inside the write set of the thing being judged: any criterion
can be satisfied by adjusting it, and no observation distinguishes a met criterion from a moved one.
The report is then a tautology. This holds regardless of capability, and capability makes it worse
rather than better, since a more capable performer is better at finding the adjustment.

**Corollary 1.1.** There is no grade above G4 corresponding to "no human involved at all," because
such a grade would be an unaccepted result rather than a more delegated one.

**Corollary 1.2 (what the proposition permits).** Acceptance need not be human. It may be a declared
test, an independently run check, or a separate model call with criteria it did not author. The
requirement is on *locus*, not on species: acceptance must go somewhere other than the doer.

So the honest top of the scale is:

> **G4 with independent acceptance.** The agent selects and performs work within a standing mandate; a
> locus that did not perform it decides whether it is done; the human sets the mandate and reviews
> outcomes rather than actions.

**Corollary 1.3 (separation is over loci, not over instances).** One base model in two processes, each
with its own credential and an enforced write set, satisfies the requirement. One model in one context
told to now act as the reviewer does not: the roles are then two functions of one process, the
criterion is inside the write set, and the arrangement certifies itself. The difference is that the
first is a property of the system and the second is a property left to judgement on the day.

---

## 6. Delegation is bounded by the task

> **Proposition 2.** *For a fixed agent, the sustainable grade varies with the task class, and the
> binding coordinates are verifiability and reversibility. Capability sets the exception rate within a
> class; it does not set the ceiling.*

The illustration, with capability held constant:

| Task class | Verifiability | Reversibility | Grade |
|---|---|---|---|
| Change code with a good test suite | immediate, cheap | one command | **G2–G3** |
| The same refactor with no tests | late, expensive | hard once merged | **G1** |
| Draft a document | subjective, deferred | trivial | **G3** |
| Change production configuration | immediate, partial | costly | **G1**, often **G0** |
| Send an external message | none | **none** | **G0–G1** |

Nothing about the agent changes down that column. The grade moves by two or three.

**Corollary 2.1 (the effective lever).** Raising delegation is mostly an investment in the task class.
Add tests and the first row moves; add a staging environment with one-command rollback and the fourth
moves. Neither requires the agent to improve at anything. **Effort spent making an agent more capable
buys less delegation than the same effort spent making its mistakes cheap to find and cheap to undo.**

**Corollary 2.2 (the irreversibility floor).** Where reversibility is zero, verification does not
substitute, because verification after the fact is not a remedy. Such classes have a delegation floor
that no capability removes — the external message belongs at G0–G1 permanently, not until agents get
better.

**Corollary 2.3.** A delegation grade reported without its task class is not a weak claim but an
incomplete one, in the same way that a level-4 automation claim without an operational design domain
is incomplete.

---

## 7. What it costs

Delegation becomes operational when the human load is computed rather than described.

$$L \;=\; r(\tau) \times \big(T_\delta + c_i\big)$$

where $r(\tau)$ is exceptions per task on class $\tau$, $T_\delta$ is the latency between an exception
being raised and the human acting, and $c_i$ is the human's per-intervention cost. Below G2, $r$ is
effectively the action count and the identity degenerates to per-action supervision.

Three things follow.

**The number people want is a triple**, not a grade: $\langle$ grade, exception rate, $T_\delta \rangle$.
A G3 agent that raises an exception every four minutes is more expensive than a G2 agent that raises
one an hour.

**$T_\delta$ is the term nobody measures.** It is the same quantity that bounds the iteration rate of
any governed improvement loop, and it is cheap to obtain — timestamp the raise and the response — yet
in the one deployed system we examined it had never been recorded, because the table that logs
authorizations had no timestamp column.

**Exception *kind* matters more than rate.** One rescue from a destructive path is not equivalent to
twenty clarifying questions. A rate that averages them is misleading in the direction of comfort, and
§10 records that this document does not model it.

---

## 8. Relation to other axes

| Axis | Asks | Relation |
|---|---|---|
| Authority ceiling | What may it do? | **Independent.** A ceiling is granted in advance; a grade is achieved. A system may hold a high ceiling and operate two grades below it because nobody trusts it yet. |
| Individual level | What does it change about itself? | **Largely independent.** A persistent-only agent on verifiable work out-delegates a self-improving agent on unverifiable work. |
| Organizational level | What does the structure change about itself? | **Coupled at the top.** Independent acceptance is a structural property, so G4-with-acceptance requires a separated verifier. |
| Loop completion | How much of the improvement loop is unapproved? | **Analogous, different object** — that is delegation of self-change; this is delegation of work. |

The first row is the practically important one. **Ceiling and grade are routinely conflated**, and a
system described as "fully autonomous" is usually reporting its ceiling while operating well below it.

---

## 9. Falsification

| Claim | Refuted by |
|---|---|
| Proposition 1 | Self-accepted work replicating under independent check at rates comparable to independently accepted work, on matched classes |
| Proposition 2 | Capability improvements raising the sustainable grade on a class whose verifiability and reversibility are held fixed |
| Corollary 2.2 | An irreversible class sustainably reaching G3 with outcomes matching reversible classes |
| §3.1 | A system holding G2 whose exception rate is low because failures are silent rather than absent — which would show the grade is measuring the alarm |
| §7 | Human load failing to track $r \times (T_\delta + c_i)$ once all three are logged |

Proposition 2 is the one most worth attacking, because the prevailing model implies its negation. The
experiment is available today: fix a task class, vary the agent, and measure the grade sustained.

---

## 10. Limitations

**The §6 table is constructed, not measured.** It is assembled from the pattern rather than from logged
intervention data, which by this paper's own standard makes it an illustration. Turning it into a
finding requires logging interventions by kind across classes — cheap, and not done.

**Verifiability and reversibility are used as scalars and are not.** They are at best orderings and
probably multidimensional: verification cost, latency, and coverage are distinct, as are rollback cost,
rollback latency, and blast radius. A quantified version of §6 needs all six.

**Exception kind is not modelled**, though §7 argues it dominates rate.

**The grades are ordinal with soft boundaries**, particularly G2/G3, which is partly a matter of how a
task was phrased.

**Novelty is the least developed coordinate.** "Distance from the demonstrated distribution" is the
right idea and has no operational definition here.

---

## 11. Conclusion

Delegation is not a readout of capability, and treating it as one misdirects effort toward the agent
when the lever is the task. What determines how much comes back done is how cheaply a mistake can be
found and how cheaply it can be undone — properties of the work, not of the worker. The same agent is
two or three grades apart across classes that differ only in those respects, which is a fact about
delegation and not about intelligence.

And there is a ceiling that capability cannot lift. Execution can be handed over entirely; acceptance
can only be moved, never dissolved, because a result accepted by whatever produced it is not a
completed task but a claim. The top of the scale is therefore not the absence of a human but the
presence of a separate acceptor — which may be a test, a check, or another process, and may not be the
thing that did the work.

The practical form of both results is a single reporting rule. **State the grade, state the class,
state who accepts.** A grade without a class is incomplete; a grade without an acceptor is
unverifiable; and a system described as fully autonomous is usually reporting the permission it holds
rather than the supervision it actually receives.

---

## References

Amdahl, G. (1967). Validity of the single processor approach to achieving large scale computing
capabilities. *AFIPS Conference Proceedings*, 30. — the form of the bound in §7.

Horvitz, E. (1999). Principles of mixed-initiative user interfaces. *CHI '99*. — the
exception-driven interaction pattern named at G2, including when to interrupt.

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human
Factors*, 46(1). — the descriptive counterpart to §6.

Morris, M. R., et al. (2024). Levels of AGI for operationalizing progress on the path to AGI. *ICML*.
— the closest published taxonomy, and the prior separation of autonomy from capability.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human
interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics — Part A*, 30(3).
— the stage decomposition §5 extends.

Perrow, C. (1984). *Normal Accidents: Living with High-Risk Technologies*. Basic Books. — tight
coupling, and the mechanism behind Corollary 2.2's floor.

SAE International (2021). *J3016: Taxonomy and Definitions for Terms Related to Driving Automation
Systems for On-Road Motor Vehicles*. — the operational design domain, half of this paper's thesis.

Scerri, P., Pynadath, D. V., & Tambe, M. (2002). Towards adjustable autonomy for the real world.
*Journal of Artificial Intelligence Research*, 17. — autonomy as a per-context dial, which §4
formalizes as the task-class index.

Sheridan, T. B., & Verplank, W. L. (1978). *Human and Computer Control of Undersea Teleoperators*. MIT
Man-Machine Systems Laboratory. — the ancestor of every ladder in this area.

Within this corpus: `Two_Axis_Intelligence_Level_Framework_v2.md` (the A0–A4 ceiling and λ, the two
axes §8 distinguishes this one from), `SARSI_Level_Map.md` (every level definition on one page),
`Delegation_Levels.md` (the working note this paper was written from), and
`T_delta_Measurement_2026-08-22.md` (the unrecorded $T_\delta$ of §7).
