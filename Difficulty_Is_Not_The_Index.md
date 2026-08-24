# Difficulty Is Not the Index

## Three repairs to the delegation frontier, and one reporting form

*Working paper — 24 August 2026*
*Takes as primary: `Delegation_Intelligence_Framework.pdf` — the Delegation Intelligence framework, T0–T6, H0–H5, DL0–DLΩ, F_A(h,p)*
*Reads alongside: `Delegation_Is_A_Property_Of_The_Task.md`, `LLM_Driven_Individual_and_Organizational_Agent_Design.pdf`, `Two_Axis_Intelligence_Level_Framework_v2.md`*
*LaTeX source and arXiv package: `delegation_frontier/`. Compiled: `Difficulty_Is_Not_The_Index.pdf`, 14 pp*

---

## Abstract

The Delegation Intelligence framework proposes that delegation be measured rather than asserted, and
gives the machinery: a task-difficulty scale T0–T6, a human cognitive-intervention scale H0–H5, a
level scale DL0–DLΩ, a separation of cognitive from governance intervention, an intervention-depth
measure CID0–CID6, ten anti-inflation rules, and a central object — the **delegation frontier**
$F_A(h,p) = \max\{T : S_A(T,h) \ge p\}$, the hardest task band a system completes with probability at
least $p$ under intervention budget $h$. We take that framework as primary. This paper is a companion
supplying propositions where it supplies apparatus, and it argues that the frontier as defined cannot
carry the weight the framework puts on it, for four reasons that are repairable.

**The frontier is indexed on the wrong variable.** The framework defines a difficulty vector
$d(\tau)$ whose eight coordinates include verifiability and cost of error, warns that the vector must
remain available, and then defines the frontier over the aggregated band $T$. Two consequences follow.
The set $\{T : S_A(T,h) \ge p\}$ is not downward closed, so its maximum does not summarize it — the
framework's own reading of $F$ as "the hardest band the system reliably completes" assumes a closure
that the aggregation destroys. Worse, success is never observed directly; what is observed is the
declared verifier passing. The gap between them is the verifier's false-pass rate, which is a function
of the verifiability coordinate the band discarded. **The frontier's measurement error is largest
exactly where the class is hardest to check, and it errs upward.**

**The frontier prices failure at zero.** $p$ is a threshold on success probability with no term for
what the complement costs. We show $p$ is not a free parameter of the benchmark: a class fixes a
minimum reliability $p^{\star}(\tau) = \rho/(1+\rho)$, where $\rho$ is the cost of a failure relative to the
value of a success. Where residual harm is unbounded, $p^{\star} = 1$ and the class is not delegable at any
capability. The framework's Rule 8, on escalation, then stops being a rule and becomes a theorem.

**The acceptor is not a coordinate.** The framework requires independent verification in three places
and then reports a profile with no field for who accepted, so two profiles differing in whether the
system graded its own work are indistinguishable in the reporting form. This gets worse up the ladder,
not better: the fraction of acceptance events whose criterion the system itself authored rises with the
level by construction, approaching one at DLΩ, where the framework asks for protection against
self-redefinition of success as advice rather than as structure.

**Its load metric is defined by an unobservable.** HCIL's denominator is the total cognitive effort a
completed task *required* — a counterfactual. We replace it with $L = r(\tau)(T_\delta + c_i)$, every
term of which is a timestamp, and observe that the H-scale is invariant to authorization latency, which
in deployment dominates the cost.

We give the repaired reporting form, an episode record that carries it, and falsification conditions.
Where the framework is better than the task-property account it is compared against — intervention
depth, the cognitive/governance split, the acceptance criterion inside the task tuple, and delegation
compression — we say so and adopt it.

---

## 1. Introduction

### 1.1 The framework this repairs

The Delegation Intelligence framework makes a claim worth defending: that "autonomous agent" mixes at
least three questions — how hard the task is, how much human cognition stays inside the loop, and how
often the result survives checking — and that a delegation claim is only meaningful as a conjunction of
all three. Its apparatus is correspondingly serious. A delegated task is a tuple
$\tau = \langle G, X, C, R, V, H\rangle$ carrying its own acceptance criterion $V$. Difficulty is
externally calibrated so that a task does not become easy by being solved. Interventions are typed, and
cognitive assistance is distinguished from governance approval so that a required signature does not
count against the machine's intelligence. Success requires a criterion declared independently of the
system's self-report. Ten anti-inflation rules make the levels falsifiable.

None of that is in dispute here, and most of it is better than what it is being compared against.

### 1.2 Why it needs repair at all

The difficulty is not in the apparatus but in the single object the apparatus is compressed into. The
frontier

$$F_A(h,p) \;=\; \max\{\, T : S_A(T,h) \ge p \,\}$$

is the framework's answer to "how autonomous is it" — and it is read as *"the hardest task band the
system reliably completes under the allowed human cognitive-intervention budget."* Three of the
framework's own commitments are in tension with that object.

It commits to difficulty as a **vector** and then maximizes over a **band**. It commits to
**verified** success and then treats $S$ as observed. It commits to **independent acceptance** and then
reports a profile with no field for the acceptor. Each tension is local and each is repairable without
abandoning the scale.

### 1.3 Contributions

1. **Non-closure** (§3.2). $\{T : S_A(T,h) \ge p\}$ is not downward closed, because $T$ aggregates
   coordinates that move $S$ in opposite directions. The maximum is therefore not a summary of the set,
   and the frontier should be reported per class cell rather than as a scalar band.
2. **Upward bias** (§3.3). The observed frontier is computed from verifier-pass rate, not success. The
   two differ by the false-pass rate, which is governed by the coordinate the band discarded — so the
   frontier over-reports most on the classes with the weakest verification.
3. **The reliability threshold is set by the class** (§4). $p^{\star}(\tau) = \rho/(1+\rho)$, and where
   residual harm is unbounded, $p^{\star} = 1$. This makes the irreversibility floor quantitative, and
   derives the framework's escalation rule instead of asserting it.
4. **The acceptor coordinate, and $\sigma$** (§5). A delegation claim needs to name who accepted; and
   the self-authored acceptance fraction $\sigma$ rises with the level by construction, which puts the
   acceptance problem at its worst precisely at DL6 and DLΩ.
5. **An observable load metric** (§6). $L = r(\tau)(T_\delta + c_i)$ replaces HCIL, and $T_\delta$ — a
   quantity the H-scale is invariant to — is added.
6. **A merged reporting form and episode record** (§8), extending the framework's own.

### 1.4 What this paper does not claim

**It is not an argument that the levels are wrong.** DL0–DLΩ is a reasonable ladder and the transition
tests are the right kind of object. The repairs are to the measurement, not to the ordering.

**It is not a claim that difficulty is irrelevant.** Difficulty determines whether a task can be done
at all and drives the exception rate. The claim in §3 is narrower: difficulty is the wrong thing to
*index the frontier on*, because it is not what determines whether the result can be checked or undone.

**Nothing here is measured.** The numbers in §4 are worked illustrations. §10 says what would make any
of it a finding.

---

## 2. The two accounts, and where they meet

Two documents were written about delegation on the same day by different routes: the framework this
paper repairs, which builds the measurement apparatus from the human-factors tradition, and a
task-property account which argues that delegation is capped by properties of the work rather than of
the worker. They were written independently. The overlap is large enough to be worth stating, because
the disagreements are only legible against it.

**Where they agree.** Delegation is not a single autonomy label and must be conditioned on the task.
Self-reported completion is not completion. Governance approval is not the same as cognitive
assistance, and conflating them makes a well-governed system look stupid. Interventions differ in kind,
and a rate that averages a rescue with a clarifying question is misleading in the direction of comfort.
Levels are established over families with intervals, not over demonstrations.

**Prior art both accounts share.** Autonomy indexed by the conditions it holds under is J3016's
operational design domain, and the observation that the same system occupies different autonomy levels
in different contexts is the adjustable-autonomy literature's. Morris et al. separate capability from
autonomy explicitly, which is the published taxonomy closest to both accounts — and the one §3.2
disagrees with, since its autonomy column is read off the system while the same system occupies several
of its rows at once. Reliance as calibrated by experience of failure is Lee and See's; the
exception-driven interaction the H1 budget names, including when to interrupt, is Horvitz's; and the
interaction guidelines governing how such an interruption should be presented are Amershi et al.'s.

**Where the framework is better**, and adopted here without modification:

| | The framework has | The task-property account has |
|---|---|---|
| Intervention depth | **CID0–CID6**, an ordinal scale of the highest task decision a human supplied | "exception kind matters more than rate", listed as an unmodelled limitation |
| Governance | An explicit split, with the rule that governance does not lower the level | The distinction between an authority ceiling and an achieved grade — the same idea, less operational |
| The task object | $V$ **inside the tuple**: the acceptance criterion is part of what is delegated | A four-coordinate class that does not carry its criterion at all |
| Environment change | **Delegation compression** (§7): solving a hard class repeatedly converts it into an easy one | Nothing |

The last of these turns out to be where the two accounts meet, and §7 argues it is the mechanism the
task-property account was missing.

**Where they disagree** is the subject of §§3–6. In one sentence: the framework indexes the frontier on
how hard the work is, and the task-property account says the binding coordinates are how cheaply a
mistake is found and how cheaply it is undone — which are in the framework's difficulty vector, and
gone from its difficulty band.

---

## 3. Repair 1 — the T-band collapse

### 3.1 The vector is defined, and then discarded

The framework defines difficulty as a vector before it is a band:

$$d(\tau) = \langle d_{dec}, d_{hor}, d_{unc}, d_{tool}, d_{nov}, d_{ver}, d_{coord}, d_{risk}\rangle$$

and says the vector must remain available *"so that a system cannot hide a narrow weakness behind an
average difficulty score."* This is exactly right, and the frontier does not honour it: $F_A(h,p)$ is a
maximum over $T$, and $T$ is the aggregate. The warning is stated in the difficulty section and not
carried into the formalism that uses it.

Two of the eight coordinates are the ones at issue. $d_{ver}$ is verification difficulty. $d_{risk}$ is
cost of error. They are the two the task-property account says do the work, and they are the two that
have nothing to do with how hard the thinking is.

### 3.2 The maximum is not a summary of the set

> **Proposition 1 (non-closure).** *The set $\{T : S_A(T,h) \ge p\}$ is not downward closed. Therefore
> its maximum does not entail that the system sustains $p$ on every lower band, and $F_A(h,p)$ is not
> "the hardest band the system reliably completes."*

*Argument.* Downward closure would require $S_A(\cdot,h)$ to be monotone decreasing in $T$. It is not,
because $T$ aggregates coordinates whose effects on $S$ have opposite signs at fixed $h$. Raising
$d_{dec}$ or $d_{hor}$ lowers $S$ only where planning or horizon is the binding constraint. Raising
$d_{ver}$ lowers $S$ under every $h$ and for every agent, because it attacks the conjunct that makes a
success *verified*. A single scalar cannot preserve an ordering that its components disagree about.

The counterexample is ordinary rather than contrived. Take two classes for one unchanged agent:

| Class | Band, by the framework's own operational characters | $d_{ver}$ | $d_{risk}$ | $S$ at H1 |
|---|---|---|---|---|
| Refactor a module under a good test suite | **T3** — nontrivial decomposition, tool choice, state tracking, error recovery, replanning | low | low | high |
| Compose and send one external message | **T0–T1** — one operation, or a familiar short task with a known procedure | **maximal** | **maximal** | not estimable |

The second row is nearer the bottom of the difficulty scale and nearer the bottom of what anyone will
delegate. If $S$ clears $p$ on T3 and does not on T1, then $\max$ returns T3 while a lower band fails,
and the sentence "the hardest band it reliably completes" is false of the system it describes.

**The repair** is to report the frontier per class cell rather than as a band. Let
$\kappa = \langle d_{ver}, d_{risk}\rangle$ and let $T_{do}$ be the remaining six coordinates
aggregated as before. Then $F_A(h,p\,|\,\kappa)$ is downward closed in $T_{do}$ within a cell, which is
the property the scalar was reaching for, and comparisons across cells are reported as what they are:
different questions.

### 3.3 The measurement error is a function of the coordinate that was discarded

This is the more serious half, because it biases in a known direction.

> **Proposition 2 (upward bias).** *$S_A(T,h)$ is not observed. What is observed is $S^V_A(T,h)$, the
> probability that the declared verifier passes. $S^V \ge S$, with the gap equal to the verifier's
> false-pass rate $\phi$. Since $\phi$ is governed by $d_{ver}$, and $d_{ver}$ is aggregated into $T$,
> the frontier's error is largest exactly on the classes whose verification is weakest — and it is
> always upward.*

*Argument.* The framework's Rule 5 requires that success be established by a criterion declared
independently of the system's self-report, which is right and is not the issue. Any such criterion is
itself an instrument with a false-pass rate: a test suite with coverage below one, a held-out set with
leakage, an inspector reading a document. Passing the instrument is the event recorded. So the observed
frontier is $\hat{F} = \max\{T : S^V \ge p\}$, and $\hat{F} \ge F$ pointwise. The size of the gap is
the property of the class the band deleted.

Three consequences.

**A high frontier on a weakly verifiable class is the expected artefact**, not a surprising result. The
framework's Rule 1 forbids establishing a high claim on low-difficulty tasks; there is no corresponding
rule forbidding establishing it on low-*verifiability* tasks, and that is the direction the error runs.

**Some classes are not in the frontier's domain at all.** Where no external criterion exists, $S^V$ is
undefined rather than small, so the class silently drops out of the maximum. A frontier computed over
the classes that happen to have verifiers, on a corpus where the unverifiable ones were excluded by the
methodology rather than by a finding, reports a number that is high because of what is missing from it.
These are the classes people most want a delegation answer for.

**The verifier belongs in the report.** A frontier is a statement about a system *and its evaluator*.
Reporting $\hat{F}$ without $\phi$, or without a statement that $\phi$ is unknown, is reporting an
instrument reading as a quantity.

**The repair** is three fields: the verifier's identity, its estimated false-pass rate or an explicit
`unknown`, and the count of classes excluded from the frontier for want of a criterion. The third is
the one that keeps under-reporting from looking like capability.

---

## 4. Repair 2 — the frontier prices failure at zero

$F_A(h,p) = \max\{T : S_A(T,h) \ge p\}$ contains no term for what happens in the $1-p$. Every failure
costs the same as every other, which is to say nothing. The framework is not unaware of this — Rule 8
says that a correct escalation can be preferable to a confident failure — but the frontier has nowhere
to put the difference, so the observation has to be carried as a rule alongside the formalism instead
of falling out of it.

### 4.1 $p$ is not a free parameter

Write, for a class $\tau$: $V$ for the value of a verified success, $C_{det}$ for the cost of detecting
a failure, $C_{undo}$ for the cost of undoing it, and $C_{res}$ for residual harm that no expenditure
undoes. Let

$$\rho(\tau) \;=\; \frac{C_{det} + C_{undo} + C_{res}}{V}$$

be the class's **loss ratio**. Delegating is worth doing when expected value is non-negative:
$S\,V - (1-S)\,\rho V \ge 0$, which gives

> **Proposition 3 (the class sets the threshold).**
> $$p^{\star}(\tau) \;=\; \frac{\rho(\tau)}{1 + \rho(\tau)}$$
> *is the minimum reliability at which class $\tau$ may be delegated at all. Reporting $F_A(h,p)$ with
> $p$ chosen by the evaluator rather than by the class is a category error, and any $p < p^{\star}(\tau)$
> reports a frontier over tasks that should not have been delegated at that reliability.*

Worked, to show the shape:

| Class | $\rho$ | $p^{\star}$ | A benchmark reporting at $p = 0.90$ |
|---|---|---|---|
| Draft a document | 0.1 | 0.09 | far stricter than the class requires — under-reports |
| Refactor under tests | 1 | 0.50 | stricter than required |
| Change production configuration | 30 | 0.968 | **reports a frontier the class does not permit** |
| Send an external message | unbounded | **1** | **the class is not in the domain at any capability** |

The framework's convention of quoting frontiers at $p = 0.90$ is therefore simultaneously too strict
for cheap-to-undo classes and too lenient for expensive ones, and the error is not small: for
production configuration, the reported and the permissible thresholds differ by most of the remaining
probability mass.

> **Corollary 3.1 (the irreversibility floor, quantified).** As $C_{res} \to \infty$, $p^{\star} \to 1$. No
> attainable reliability delegates such a class, so it has a floor no capability removes. This is the
> quantitative form of the observation that verification after the fact is not a remedy: adding nines
> buys delegation only where residual cost is finite, and reliability and reversibility are therefore
> not interchangeable.

### 4.2 Rule 8 becomes a theorem

An escalation is an outcome with $S = 0$ and $C_{det} = C_{undo} = C_{res} \approx 0$: the system did
not complete the task and also did not incur the loss. It therefore does not enter the loss term at
all, and costs only human load.

> **Corollary 3.2.** *A correct escalation dominates a confident failure on every class with
> $\rho > 0$, and its cost is a load term rather than a reliability term. Frequent escalation therefore
> lowers the frontier at H0/H1 without lowering expected value.*

Both halves of Rule 8 are recovered — including the second, which reads in the original as a
concession and here as an accounting identity. This is the test of a repair: the rules that had to be
asserted alongside the formalism should follow from it.

### 4.3 The repaired frontier

$$F^{\star}_A(h) \;=\; \max\Big\{\, T \;:\; S^V_A(T,h)\,V - \big(1 - S^V_A(T,h)\big)\rho V - L(T,h) \;\ge\; E_{sup}(T) \,\Big\}$$

where $L$ is the human load of §6 and $E_{sup}$ is the value of doing the class under supervision. It
reduces to the original when $\rho$ is constant across classes and $L$ is ignored, which is the
condition under which the original is a good approximation, and states plainly where it is not.

---

## 5. Repair 3 — the acceptor is not a coordinate

### 5.1 The requirement is in the prose and not in the profile

The framework requires independent acceptance three times. §3.3: a result counts as success only under
a criterion declared independently of the system's self-report. Rule 5: self-reported completion is
insufficient. §11.3: a benchmark should not ask the same model that performed the work whether it
succeeded. All correct.

The reporting form is

$$\text{DL profile} = \{F(H0,p),\, F(H1,p),\, F(H2,p),\, \text{HCIL},\, \text{CID distribution},\, \text{success CI},\, \text{cost},\, \text{latency}\}$$

which has no field for who accepted.

> **Proposition 4.** *Two systems whose results were accepted by different loci — one by a separated
> verifier, one by the system itself — produce identical profiles. The reporting form therefore cannot
> express the difference between a measured level and a self-certified one, and a rule that is stated
> in the prose but absent from the form is enforced by the diligence of whoever fills it in.*

The underlying result is that delegation of execution scales without limit while delegation of
acceptance only transfers: if the accepting party is the performing party, the criterion sits inside
the write set of the thing being judged, any criterion can be satisfied by adjusting it, and no
observation distinguishes a met criterion from a moved one. Capability makes this worse rather than
better, since a more capable performer is better at finding the adjustment.

**The repair is a field.** Every DL claim carries $\alpha$, the acceptance locus:

| $\alpha$ | Acceptor | Admissible? |
|---|---|---|
| $\alpha_0$ | The performing system | **No** — this is an assertion, not a level |
| $\alpha_1$ | A test declared before the work, run by the performer | Yes, if the performer cannot edit the test |
| $\alpha_2$ | A separate process with its own credential and enforced write set | Yes |
| $\alpha_3$ | A party that did not build the system | Yes, and required for published claims |

The requirement is on locus, not on species: acceptance may be a machine, and must not be the same
machine. One base model in two processes with separate credentials and enforced write sets satisfies
it. One model in one context told to now act as the reviewer does not — the roles are then two
functions of one process, and the arrangement certifies itself.

The engineering half of this already exists in the companion agent-design framework, which states the
rule as **evaluator not in write set**, gives the write-set depths D0–D4, and makes D0 — the agent that
may change nothing about itself — the one fit to hold judgement over another's promotion. Its manifest
carries `verifier: external_required` and `promoter_required` as declared fields, enforced by file
permissions, separate services and container boundaries rather than by policy. So the acceptance
coordinate is implementable in the chassis today. It is missing from the scale, not from the build.

### 5.2 The self-authored acceptance fraction, and why the ladder makes it worse

There is a subtler failure, and it is the one that matters most for the top of the scale.

The task tuple carries $V$, so the delegated task's acceptance criterion is human-supplied. But from
DL3 upward the system *constructs the task graph*: it invents subgoals, and each invented subgoal
carries an invented done-condition. Those conditions are acceptance events, and the system authored
them. The human's $V$ binds the root of the tree and nothing below it.

> **Definition.** $\sigma$, the **self-authored acceptance fraction**, is the share of acceptance events
> in an episode whose criterion the system itself wrote.

> **Proposition 5.** *$\sigma$ rises with the DL level by construction. At DL0 it is zero, because the
> human specifies each operation and its acceptance. At DL3 it is $1 - 1/N$ for an episode with $N$
> acceptance events, since only the root criterion is given. At DL6 the system derives goals and
> priorities, so criteria at the project layer are self-authored too. At DLΩ the system selects its own
> missions, so $\sigma \to 1$ unless something structurally prevents it.*

This inverts the framework's own reassurance. It treats independent verification as a rule that applies
uniformly up the ladder; in fact the ladder is a description of *handing over criterion authorship*,
and the amount of self-certification inside an episode is a monotone function of the level being
claimed. DLΩ asks for "explicit protection against self-redefinition of success" in its evidence
desiderata — which names this exactly, and asks for it as advice. Advice is a property of the day, not
of the system.

> **Corollary 5.1.** A DL6 or DLΩ claim is unmeasurable, rather than merely hard to measure, unless
> $\sigma$ is bounded below one by structure: a criterion register written before the work and outside
> the system's write set, or a separated acceptor holding the pen on subgoal criteria as well as on the
> root.

**The repair** is to report $\sigma$ alongside the level, and to record for each acceptance event who
authored the criterion and when relative to the work. The framework already requires intervention
*timing* to be recorded, on the grounds that information supplied before the system meets the relevant
uncertainty may be hidden scaffolding. The same argument applies with the sign reversed: a criterion
authored *after* the work is a criterion fitted to it.

---

## 6. Repair 4 — the load metric is defined by an unobservable

### 6.1 HCIL's denominator is a counterfactual

$$\text{HCIL} = \frac{\text{human cognitive effort required}}{\text{total cognitive effort required by the completed task}}$$

The denominator is the effort a complete solution *required* — a quantity about a counterfactual
solution nobody performed. It is not merely hard to instrument; there is no procedure that would
observe it, even in principle, because the task was completed once, jointly, and the decomposition into
what the machine needed and what the task needed is not present in the record.

The framework says so, and offers six proxies: intervention count, human cognitive minutes,
human-generated next-step decisions, corrections, rescues, and the fraction of branches whose strategy
the human chose. Each is observable. But a quantity defined by an unobservable and reported through six
proxies with no stated combination rule is a proxy set, and the name on it suggests a measurement.

There is a second problem. HCIL is a *ratio* normalized by task difficulty, so a fixed amount of human
help scores better on a harder task. That reintroduces exactly the conflation §3 removed.

### 6.2 The observable is load, not a ratio

$$L \;=\; r(\tau) \times \big(T_\delta + c_i\big)$$

where $r$ is exceptions per task on the class, $T_\delta$ is the latency between an exception being
raised and the human acting, and $c_i$ is the human's per-intervention cost. Every term is a
subtraction of two timestamps or a figure the human can report about their own clock. Nothing about a
counterfactual appears. Below H2-equivalent budgets, $r$ degenerates to the action count and the
identity reduces to per-action supervision, which is the correct limit.

The weighting the ratio was reaching for is better served by CID, which the framework already defines:
report $L$ per CID band rather than dividing by an unknown, so that one deep rescue is not averaged
against twenty approvals. This keeps the framework's best measurement idea and drops its weakest.

### 6.3 The H-scale is invariant to the term that dominates

H0–H5 measures *whether* human cognition is needed and at what frequency. It says nothing about how
long the human takes. In deployment the two systems below score identically on the H-scale and are not
comparably delegable:

| | Intervention rate | $T_\delta$ | $L$ per task |
|---|---|---|---|
| System P | one exception per task, H1 | 4 hours | 4 h |
| System Q | one exception per task, H1 | 30 seconds | 30 s |

The H-scale is a rate; the cost is a rate times a latency. A framework whose purpose is to make
delegation operational should carry the term that decides whether a delegated task finishes today.

$T_\delta$ is also the quantity that bounds the iteration rate of any governed improvement loop, which
makes it the one measurement that two otherwise separate frameworks both turn on. It is cheap —
timestamp the raise and the response — and on the one deployed system examined for this corpus it had
never been recorded, because the table logging authorizations has no timestamp column. The repair is a
column, and the finding is that a quantity six documents call decisive has been unobserved for want of
one.

---

## 7. Where the two accounts meet: delegation compression

The framework contains an idea the task-property account lacks and needs. **Delegation compression**:
a T4 problem solved repeatedly becomes a T2 procedure once the system has built the tools, templates,
checks and knowledge; delegation changes the task environment and not only the agent. The framework
adds the right reporting discipline — record both the original and the post-tool difficulty, because
silently relabelling the task as always easy erases the achievement.

Placed against §3, this is more than a caveat. The task-property account holds that the lever on
delegation is the class rather than the agent: add tests and a class moves, add one-command rollback
and another does, neither requiring the agent to improve at anything. Compression is the same
operation performed *by the agent on its own task environment* — and the coordinates it moves are
exactly $\kappa$. A test the agent writes raises verifiability. A migration it makes reversible lowers
residual cost. A checklist it proceduralizes lowers both.

> **Observation.** The agent-side and task-side accounts of delegation meet at compression: the durable
> way for a system to raise its own frontier is not to become more capable but to move the $\kappa$
> coordinates of the classes it works in. Capability improvements raise $S$ within a cell; compression
> moves the cell.

Two consequences for measurement. **Compression must be reported against $\kappa$, not only against
$T$** — "T4 became T2" is the visible shadow of "$d_{ver}$ fell", and the second is the durable claim.
And **compression is the one route by which an agent legitimately raises its own frontier**, which
makes it the thing to instrument if the question is whether a system is getting more delegable rather
than merely more accurate.

---

## 8. One reporting form, merged

A delegation claim, stated fully:

$$\text{DL claim} \;=\; \big\langle\, \text{DL}n,\; \kappa,\; T_{do},\; \alpha,\; \sigma,\; F^{\star},\; p^{\star},\; r,\; T_\delta,\; \text{CID dist.},\; \phi,\; \rho,\; \text{cost},\; \text{excluded classes} \,\big\rangle$$

| Field | From | Answers |
|---|---|---|
| DL$n$ | the framework | The compact label |
| $\kappa = \langle d_{ver}, d_{risk}\rangle$ | §3 | Which cell the claim is in |
| $T_{do}$ | the framework, less $\kappa$ | How hard the doing is |
| $\alpha$ | §5.1 | Who accepted |
| $\sigma$ | §5.2 | What share of criteria the system wrote |
| $F^{\star}$ | §4.3 | The frontier, net of failure cost and load |
| $p^{\star}$ | §4.1 | The reliability the class requires — not the one chosen |
| $r$, $T_\delta$, CID | §6 | What it costs the human, and how deep the help went |
| $\phi$ | §3.3 | How much the verifier lets through, or `unknown` |
| $\rho$ | §4.1 | What a failure costs relative to a success |
| excluded classes | §3.3 | What the frontier is silent about |

The episode record, extending the framework's own with the fields the repairs require — additions
marked:

```json
{
  "task_id": "tsk_...",
  "task_band": "T3",
  "difficulty_vector": {"horizon": 3, "uncertainty": 2, "verification": 3},
  "kappa": {"verifiability": 3, "reversibility": 1},          // added: reported, not aggregated
  "intervention_budget": "H1",
  "human_interventions": [
    {"type": "approval", "cognitive": false, "minutes": 0.2,
     "cid": 0,
     "raised_at": "2026-08-24T13:02:11Z",                     // added: the two timestamps
     "responded_at": "2026-08-24T13:04:47Z"}                  //   whose difference is T_delta
  ],
  "acceptance": {                                              // added: the whole block
    "locus": "a2_separated_process",
    "verifier_id": "verify-worker-03",
    "false_pass_rate": null,
    "events": 7,
    "self_authored_criteria": 5,
    "sigma": 0.71,
    "root_criterion_declared_at": "2026-08-24T12:40:00Z"
  },
  "loss": {"value": 1.0, "c_det": 0.1, "c_undo": 0.2,          // added: the terms p* needs
           "c_residual": 0.0, "rho": 0.3, "p_star": 0.231},
  "agent_replans": 4,
  "verification": "pass",
  "result": "success",
  "latency_seconds": 4200,
  "compute_cost": 12.4
}
```

The additions are five. $\kappa$ carries the two coordinates the band aggregates away. The timestamp
pair yields $T_\delta$ by subtraction. The acceptance block carries $\alpha$, $\sigma$, the verifier's
identity and its false-pass rate — here `null`, which is the honest value and the common one. The loss
block carries the terms $p^{\star}$ needs. Every one is a timestamp, a count, or a figure the person
delegating already knows, and none requires estimating a counterfactual, which was the objection to the
metric it replaces.

The framework's ten anti-inflation rules survive, with one added and one demoted:

> **Rule 11 — verifiability is a test condition.** No frontier may be reported without the verifier's
> identity, its false-pass rate or an explicit `unknown`, and the count of classes excluded for want of
> a criterion. Rule 1 forbids establishing a high claim on easy tasks; this forbids establishing it on
> uncheckable ones, which is the direction the measurement error actually runs.

> **Rule 8 is demoted to a corollary.** It follows from §4.2 and no longer needs to be a rule.

---

## 9. Falsification

| Claim | Refuted by |
|---|---|
| **P1**, non-closure | A system whose measured $S$ is monotone in $T$ across classes spanning a wide range of $d_{ver}$ — which would show the band preserves the ordering after all |
| **P2**, upward bias | Verifier false-pass rates uncorrelated with $d_{ver}$ across a task corpus, or frontiers that do not shift when a stronger verifier replaces a weaker one on the same class |
| **P3**, $p^{\star}$ | Delegation decisions that track a fixed $p$ rather than $\rho/(1+\rho)$ once $V$, $C_{det}$, $C_{undo}$ and $C_{res}$ are elicited per class |
| **Cor. 3.1**, the floor | An unbounded-$C_{res}$ class sustainably delegated at H0/H1 with outcomes matching reversible classes |
| **P4**, the acceptor | Self-accepted work replicating under independent check at rates comparable to independently accepted work, on matched classes |
| **P5**, $\sigma$ | Episodes at DL3 and above whose self-authored acceptance fraction does not rise with level once acceptance events are individuated |
| **§6.3**, $T_\delta$ | Human load failing to track $r \times (T_\delta + c_i)$ once all three are logged |
| **§7**, compression | Frontier gains that persist without any movement in $\kappa$ — capability alone moving the cell rather than the position within it |

**P2 is the one most worth attacking**, because it says published frontiers are biased and names the
direction. The experiment is cheap: take one class, measure the frontier under two verifiers of known
differing coverage, and see whether the reported frontier moves with the instrument.

---

## 10. Limitations

**Nothing here is measured.** The tables in §3.2 and §4.1 are worked illustrations, assembled from the
pattern rather than from logged episodes — which by this paper's own standard makes them illustrations
and not findings. Turning them into findings requires the episode record of §8 populated across
classes, which is cheap and not done.

**$\rho$ is as hard to elicit as the thing it repairs.** $C_{res}$ in particular is a judgement about
harm that does not undo, and people are poor at it. The claim is only that $\rho$ is elicitable in
principle while HCIL's denominator is not, and that a badly estimated $\rho$ is visible in the report
whereas a chosen $p$ hides the same judgement inside a convention.

**$\sigma$ requires acceptance events to be individuated**, and what counts as one event is a modelling
choice. A system that decomposes finely will report a higher $\sigma$ than one that decomposes coarsely
for the same behaviour. The ordering across levels is robust to this; the value is not.

**$\phi$ is rarely known.** Most verifiers have no false-pass estimate, which is why §8 admits
`unknown` as a value. A field that is usually null is a weak instrument — its purpose is to make the
absence visible rather than to supply the number.

**The repairs make the report heavier**, and there is a real tension between completeness and adoption.
A form nobody fills in measures nothing. The minimum that preserves the results is three fields:
$\kappa$, $\alpha$, and the two timestamps.

**$\kappa$ is used as a pair of scalars and is not.** Verification cost, latency and coverage are
distinct, as are rollback cost, rollback latency and blast radius. A quantified version of §3 needs six
coordinates where this paper uses two.

---

## 11. Conclusion

The Delegation Intelligence framework is right that delegation should be measured as a conjunction of
difficulty, intervention and reliability, and right that the alternative is a rhetorical label. The
repairs here are to the object that conjunction is compressed into.

A frontier indexed on difficulty maximizes over an aggregate whose components disagree, so its maximum
does not summarize the set it is drawn from; and because success is observed through a verifier, the
frontier's error grows with the verifiability coordinate the aggregate discarded, always upward. A
frontier that thresholds on success probability prices failure at zero, when in fact the class fixes
the threshold — $p^{\star} = \rho/(1+\rho)$, unattainable where harm does not undo. A profile with no field
for the acceptor cannot distinguish a measured level from a self-certified one, and the share of
acceptance criteria the system itself wrote rises with the level, so the problem is worst at the top of
the ladder rather than solved there. And a load metric whose denominator is a counterfactual should be
replaced by one whose every term is a timestamp — including the latency the intervention scale is
invariant to, and which nobody has recorded.

None of this requires abandoning T0–T6, H0–H5, DL0–DLΩ, or the frontier. It requires the frontier to be
indexed by the class rather than by the difficulty, priced against the cost of being wrong, stamped
with who accepted, and costed in latency. Four fields and a denominator.

The practical form is a single sentence added to the framework's own. It asks: *how difficult a goal
can I hand to this intelligence, how little must I think for it, and how often does the result survive
independent verification?* To which: **on which class, checked by whom, and at what cost when it is
wrong.**

---

## References

Amdahl, G. (1967). Validity of the single processor approach to achieving large scale computing
capabilities. *AFIPS Conference Proceedings*, 30. — the form of the load bound in §6.

Amershi, S., et al. (2019). Guidelines for human-AI interaction. *CHI 2019*. — carried forward from
the framework repaired here.

Endsley, M. R., & Kaber, D. B. (1999). Level of automation effects on performance, situation awareness
and workload in a dynamic control task. *Ergonomics*, 42(3). — the tradeoff structure behind §6.3.

Horvitz, E. (1999). Principles of mixed-initiative user interfaces. *CHI '99*. — the exception-driven
pattern the H1 budget names, including when to interrupt.

Klein, G., Woods, D. D., Bradshaw, J. M., Hoffman, R. R., & Feltovich, P. J. (2004). Ten challenges for
making automation a team player in joint human-agent activity. *IEEE Intelligent Systems*, 19(6). —
directability and predictability, and why intervention kind must be reported.

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human
Factors*, 46(1). — reliance as calibrated by the cost of failure, the descriptive counterpart to §4.

Morris, M. R., Sohl-Dickstein, J., Fiedel, N., Warkentin, T., Dafoe, A., Faust, A., Farabet, C., & Legg,
S. (2023). Levels of AGI for operationalizing progress on the path to AGI. *arXiv:2311.02462*. — the
published separation of capability from autonomy, and a level read off the system rather than the task.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human
interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics — Part A*, 30(3). —
the stage decomposition whose separation of decision selection from implementation is what makes
acceptance special in §5.

Perrow, C. (1984). *Normal Accidents: Living with High-Risk Technologies*. Basic Books. — tight
coupling, and the mechanism behind the floor in Corollary 3.1.

SAE International (2021). *J3016: Taxonomy and Definitions for Terms Related to Driving Automation
Systems for On-Road Motor Vehicles*. — autonomy indexed by operational design domain; the prior art for
indexing a level by the conditions it holds under.

Sheridan, T. B., & Verplank, W. L. (1978). *Human and Computer Control of Undersea Teleoperators*. MIT
Man-Machine Systems Laboratory. — the ancestor of every ladder in this area.

Within this corpus: `Delegation_Intelligence_Framework.pdf` (the framework this paper repairs, and the
source of T0–T6, H0–H5, DL0–DLΩ, CID, the ten rules and the frontier);
`LLM_Driven_Individual_and_Organizational_Agent_Design.pdf` (the chassis in which §5's acceptance
coordinate is already enforceable — write-set depths, evaluator-not-in-write-set, and the agent
manifest); `Delegation_Is_A_Property_Of_The_Task.md` (the task-property account of §2);
`Two_Axis_Intelligence_Level_Framework_v2.md` (the I and O axes §2 keeps delegation independent of);
and `T_delta_Measurement_2026-08-22.md` (the unrecorded $T_\delta$ of §6.3).
