# Open-Ended Evolving Organization (OΩ)

## Version 2 — Independent Axioms, a Coordination Bound, and Frontier Expansion Made Measurable

*Working paper — 23 August 2026*
*Supersedes: `Open_Ended_Evolving_Organization_OOmega.pdf` (Version 1, 22 August 2026)*
*Companion: `Open_Ended_Self_Evolving_Individual_Intelligence_IOmega.pdf` (IΩ), `Two_Axis_Intelligence_Level_Framework_v2.md`*

---

## Abstract

Version 1 proposed **Open-Ended Evolving Organization** (OΩ) as a distinct class of organizational
intelligence: a persistent collective that preserves identity across turnover, integrates distributed
observation into evidence-bearing memory, reallocates roles and topology, modifies its own
coordination mechanisms, improves the process that generates those modifications, identifies its own
unknowns, and converts discoveries into organizational tools that expand its future frontier. It gave
twelve axioms, twelve metrics, a falsifiable experimental program, a reference architecture, and a
survey of what current systems lack. That contribution is retained.

This version makes six changes, of which two are structural.

- **The twelve axioms are not independent, and six of them are theorems.** An axiom set with internal
  dependencies is a requirements list, and calling it an axiomatization obscures which commitments are
  actually load-bearing. Version 2 gives **six independent axioms** and derives the remaining six as
  propositions. §4, §5.
- **There is a coordination bound, and it is the reason OΩ must federate.** Promotion of local claims
  to organizational knowledge costs communication that grows superlinearly in the number of members
  who must be consulted, while marginal member value does not. There is therefore a **size beyond
  which adding members lowers organizational intelligence**, and growth past it must be structural —
  nested sub-organizations with local promotion — rather than numeric. Version 1 lists coordination
  overhead as a failure mode; here it is a bound with a maximizer. §7.
- **Frontier expansion becomes measurable, negatively.** `F^O_{t+1} ⊃ F^O_t` cannot be evaluated,
  because the reachable frontier cannot be enumerated. But a **retained registry of problem classes
  that failed under a stated budget** makes expansion observable as a transition from recorded failure
  to reproducible success. This adds one component to the reference architecture and converts
  Axiom 12 from an aspiration into a test. §8.
- **Epistemic promotion requires separation structurally, not optionally.** Version 1's Axiom 5 says
  promotion "may depend on" independent review. Proposition 1 shows it must: where the promoter is the
  proposer, promoted knowledge is self-certified and is not knowledge. §5.1.
- **Organizational identity gets a criterion.** Version 1 establishes by analogy that a successor
  organization remains "legitimate" without saying what makes it so. At OΩ every other candidate —
  members, structure, procedures, goals — is mutable by construction. §6.
- **The metrics are a frontier, not a scorecard**, with several in explicit tension and a wide split
  between those measurable today and those that are not. §9 orders them by cost and reports a first
  measurement of the cheapest: **authorization latency has never been observed on a deployed governed
  system**, and its system of record has no field for it.

---

## 1. Introduction

Version 1's diagnosis is retained without change: many agents, persistent memory, parallel execution,
and even self-modifying members do not constitute an intelligent organization. So is its central
thesis — that the highest organizational intelligence belongs not to the organization with the
smartest member or the most agents, but to the one that continually converts distributed experience
into collective knowledge, collective knowledge into better organizational machinery, and better
machinery into access to previously unreachable problems, while preserving evidence, continuity, and
governance.

What this version addresses is that a framework proposing to *measure* organizational intelligence
must first be minimal in what it assumes, bounded in what it permits, and operational in what it
claims to detect. Version 1 is strong on the third for eleven of its twelve criteria and weakest
exactly where its defining property lives.

**Retained in full:** the OΩ definition (§4.1 of Version 1) and its recursive loop; the distinction
between organizational and individual level; heterogeneous cognitive ecology and cognitive
compression; upward and downward flows; the organizational self-model and unknown-model; the reference
architecture; the experimental program; the twelve failure modes; the staged roadmap; and the survey
of prior work. Section numbering below is this version's.

---

## 2. Preliminaries

Version 1's state formulation is used unchanged. An organization is

$$O_t = \langle A_t,\; N_t,\; R_t,\; M^O_t,\; K^O_t,\; P^O_t,\; \Theta^O_t,\; \Gamma_t,\; C_t \rangle$$

— members, communication topology, roles, memory, knowledge, procedures, organizational cognitive
machinery, governance, and commitments — and capability is a function of all of them rather than a sum
over members. The OΩ cycle is Version 1's:

$$\text{Experience}_t \to \text{Evidence}_t \to K^O_{t+1} \to \{P^O, N, R, \Theta^O\}_{t+1} \to \text{COG}^O_{t+1} \to F^O_{t+1} \to \text{Experience}_{t+1}$$

---

## 3. Why the axiom set needs reducing

Version 1 offers twelve axioms. Several imply others, and one is of a different logical type from the
rest. This is not a defect of content — each states something true and useful — but it is a defect of
presentation, because an axiom set's purpose is to isolate the commitments that must be assumed from
the consequences that follow. Where they are mixed, a reader cannot tell which claims the framework
would lose if one commitment failed.

The dependencies:

| Version 1 axiom | Status | Depends on |
|---|---|---|
| A4 evidence-bearing communication | **Mechanism for A5**, not independent | A5 |
| A10 recursive organizational meta-learning | **Theorem** | A8 + A5 |
| A11 turnover resilience | **Theorem** | A1 + A3 |
| A12 open-ended frontier expansion | **Restates the definition** | A7 + A8 + A9 |
| A2 heterogeneous cognitive ecology | **Different type** — a permission, not a requirement | — |
| A6 dynamic specialization | **Theorem** | A5 + A8 |

Six commitments survive as genuinely independent.

---

## 4. Six axioms

**Ω1 — Persistent lineage.** The organization is causally continuous across changes of members,
models, tools, and machines, and retains memory, provenance, commitments, and a traceable record of
its own structural transformations.

**Ω2 — Organizational memory.** Knowledge, decisions and their rationale, evidence and provenance,
failed approaches, reliability histories, procedures, unresolved contradictions, and the measured
effects of past organizational changes are retained independently of any member.

**Ω3 — Separated epistemic promotion.** A member's belief becomes organizational knowledge only via
*claim + evidence + verification by a locus that did not produce the claim*. This strengthens Version
1's Axiom 5 from a schema into a structural requirement; §5.1 gives the reason.

**Ω4 — Institutional plasticity.** The organization can change its own topology, roles, memory rules,
aggregation procedures, reviewer separation, allocation, decomposition, escalation, and evaluation
procedures, on evidence.

**Ω5 — Knowledge-to-tool transformation.** Validated discoveries can become durable shared capability —
procedure, tool, role, benchmark, protocol, index, rule, or agent template — such that future members
benefit without rediscovering.

**Ω6 — Protected exploration.** Exploratory diversity is preserved against exploitation pressure by
mechanism rather than intention: protected branches, novelty budgets, maintained alternative
hypotheses, delayed selection.

Ω6 is retained as an axiom rather than derived because March's result gives no reason to expect
diversity to survive optimization: an adaptive organization that is not *constructed* to protect
exploration will converge, and no other axiom prevents it.

---

## 5. What follows

**Proposition 1 (promotion requires separation).** *Let a locus propose a claim, evaluate it, and
promote it. Then the promotion criterion is inside the write set of the proposer, and the locus can
satisfy any criterion by adjusting it. No observation distinguishes promoted knowledge from asserted
belief. Therefore Ω3's verification must be performed by a locus that did not produce the claim, and
the criteria and evidence must lie outside that producer's write set.*

### 5.1 Why this is stronger than Version 1's Axiom 5

Version 1 states the schema *Claim + Evidence + Appropriate Verification → Candidate → Promoted*, and
adds that promotion "may depend on domain-specific proof, replication, deterministic checks,
independent review, or calibrated evidence aggregation." Four of those five are compatible with the
proposer performing them. Deterministic checks and proof are self-executing and therefore safe;
replication, review, and aggregation are not, and are the ones that matter for non-formal domains.

Version 1 concedes the risk downstream, listing *evaluator contamination* among the governance
integrity signals to track (§12.12) and *authority drift* among failure modes (§16.10). Proposition 1
says these are not risks to monitor but conditions to enforce: an organization whose evaluator is
contaminated has not degraded its knowledge, it has stopped producing knowledge.

**Corollary 1.1.** *Organizational intelligence is not monotone in member level.* An organization
failing Ω3 has no well-posed improvement loop regardless of its members' individual levels, while an
organization of modest members satisfying Ω3 does. Member level determines proposal quality;
separation determines whether the organization can distinguish a good proposal from a bad one — and
one that cannot does not benefit from better ones. Version 1's §2.4 establishes that collective
intelligence can be negative; Corollary 1.1 identifies the specific structural cause, and it is not
coordination overhead.

**Corollary 1.2 (the verifier's qualification).** A locus qualified to verify another's claim must not
be improving *itself* by the verdicts it issues. The natural verifier is therefore a member with an
empty or narrow self-write set — a low individual level — and this is its qualification rather than
its deficiency. This supplies a functional reason for Version 1's Axiom 2 beyond cost: heterogeneity
is required because verification requires a *different kind* of member, not merely a cheaper one.

**Proposition 2 (dynamic specialization).** From Ω3 and Ω4: reliability histories are organizational
knowledge (Ω2), promotion of a competence claim requires separated verification (Ω3), and routing
rules are mutable (Ω4). Therefore the organization can route by measured competence rather than by
title, form roles, and retire them. Version 1's Axiom 6 follows rather than being assumed.

**Proposition 3 (turnover resilience).** From Ω1 and Ω2: if knowledge, provenance, and commitments are
retained independently of members, removal of a member does not remove them. Version 1's Axiom 11
follows. Its converse is the sharper statement: *an organization that loses capability when one member
departs has failed Ω2, not merely been unlucky.* This makes Version 1's hidden-single-member-dependence
failure mode (§16.8) a diagnosable violation rather than a hazard.

**Proposition 4 (recursive organizational meta-learning).** From Ω4 and Ω3: if organizational
mechanisms are mutable and changes to them are evaluated by a separated locus, the record of which
changes validated is itself organizational knowledge (Ω2), and the procedure generating changes is an
organizational mechanism, therefore mutable. Version 1's Axiom 10 follows.

**Proposition 5 (frontier expansion).** From Ω4, Ω5, Ω6: exploration surfaces problem classes the
current organization cannot address; discoveries become durable capability; structure adapts to use it.
Version 1's Axiom 12 follows and need not be assumed. §8 makes it measurable.

**Proposition 6 (evidence-bearing communication).** Ω3 requires verification against evidence the
verifier did not produce, which requires messages to carry provenance, uncertainty, scope, and source.
Version 1's Axiom 4 is the mechanism Ω3 demands, not an independent commitment.

---

## 6. Organizational identity

Version 1 establishes by analogy — a university, a laboratory — that an organization persists across
turnover, and states the condition as: members may change while $O_{t+1}$ remains a *legitimate
successor* of $O_t$. What makes a successor legitimate is not given, and at OΩ every candidate answer
fails.

Members change by assumption. Structure, roles, topology, and procedures are mutable by Ω4. Goals are
partly mutable, since an organization that revises what it pursues is the interesting case. Performance
continuity is worst of all: improvement *is* change in behaviour, so a behavioural criterion makes
improving and dissolving indistinguishable.

What remains is the record.

> **Definition (organizational lineage).** $O_{t+1}$ is a legitimate successor of $O_t$ iff connected
> to it by an unbroken chain of provenance-linked records — each promotion attributable to a claim,
> its evidence, and the verifying locus; each structural change attributable to a proposal, its
> evaluation, and the promoting authority; with no gap.

This is Ω1 and Ω2 doing work jointly, and it has three properties Version 1's formulation lacks. It is
**checkable**: a gap is a specific missing record. It is **broken by exactly the operations the
framework already rejects** — an unattributed structural change, a promotion with no evidence, a
restore with no record of the restore. And it **survives everything else changing**, which is the
requirement.

It also resolves a case Version 1 leaves open. Two organizations that merge have two chains; the
merged entity is a legitimate successor of neither unless the merge itself is recorded as a structural
change with its own evaluation. Absent that record, a merger is not organizational growth but the
termination of two lineages and the start of an unattributed third.

---

## 7. The coordination bound

Version 1 lists coordination overhead among failure modes (§16.9) and observes that the most advanced
organization may look simpler at the execution edge (§19.4). Both are right, and neither is derived.
There is a bound here, and it determines OΩ's shape.

**Setup.** Let $m$ be the number of members whose assent or verification a promotion requires. By Ω3
promotion requires a locus other than the proposer; in general it requires evidence to reach, and
verdicts to return from, a quorum. Let $T_p(m)$ be promotion latency and $c(m)$ the communication cost
per promotion. Both are non-decreasing in $m$, and where verification involves cross-checking among
verifiers, $c$ grows superlinearly.

The organization's rate of converting local claims into organizational knowledge is bounded by
$1/T_p(m)$. Its frontier expansion rate is bounded by that conversion rate, since by Proposition 5
expansion proceeds through validated knowledge becoming capability.

**Marginal member value is bounded.** An additional member contributes at most its own capability, and
by Version 1's §2.4 may contribute negatively through integrative dilution of a better answer.

> **Proposition 7 (coordination bound).** *Since frontier expansion rate is bounded above by
> $1/T_p(m)$ with $T_p$ non-decreasing, while marginal member contribution is bounded and may be
> negative, there exists $m^*$ maximizing organizational frontier expansion rate. Growth beyond $m^*$
> reduces organizational intelligence in the sense this framework measures.*

Three consequences.

**Federation is forced, not chosen.** Growth past $m^*$ must be structural rather than numeric: nested
sub-organizations, each promoting locally with its own separated verifier, with only cross-cutting
claims escalated. This is why OΩ is hierarchical, and it is a derivation rather than a design
preference. Version 1's §19.4 observation — that the most advanced organization looks *simpler* at the
execution edge — follows: the edge is where local promotion happens under small $m$.

**Cognitive compression has a structural rationale beyond cost.** Version 1 motivates compression
economically: expensive discovery becomes cheap execution. Proposition 7 adds that compression
*reduces the number of members who must be consulted*, because a validated procedure needs execution
rather than verification. Compression is therefore a mechanism for staying below $m^*$ while growing,
and an organization that discovers but does not compress will hit the bound sooner.

**$m^*$ is domain-dependent and measurable.** It depends on how much verification a domain's claims
need — formal domains have self-executing checks and a large $m^*$; empirical domains needing
replication have a small one. Measuring $T_p$ against $m$ across an organization's sub-units estimates
it directly, and §9 argues this is among the cheapest measurements available.

**Limitation.** Proposition 7 establishes that a maximizer exists, not where it is, and gives no
functional form for $T_p$ or the marginal contribution. It also assumes verification load scales with
promotion volume; an organization that promotes rarely can be large and slow without penalty, which is
a real configuration and not obviously a bad one.

---

## 8. Frontier expansion, measured negatively

Axiom 12 of Version 1 and Proposition 5 here both state the defining property as

$$F^O_{t+1} \supset F^O_t$$

and Version 1's O-FEI metric asks for "the growth of problem classes on which the organization can make
reliable progress under a fixed or normalized resource budget." The difficulty is that $F^O$ cannot be
enumerated. An organization does not know which problems it could solve, and a metric requiring the
containment of one unknown set in another is not evaluable.

The same difficulty has a standard resolution: **measure the boundary, not the set.**

> **Definition (failure registry).** A retained, append-only record of problem classes the organization
> attempted and failed to make reliable progress on, each with the resource budget under which it
> failed, the structural configuration at the time, and the reason recorded at the time rather than
> reconstructed.

> **Definition (frontier expansion episode).** An entry that transitions from recorded failure to
> reproducible success under a comparable budget, where the organization can attribute the transition
> to a specific promoted knowledge item, tool, role, or structural change.

Three things this buys.

**Axiom 12 becomes a test.** Not "did the frontier grow" but "which registry entries flipped, under
what budget, attributable to what." O-FEI becomes a count over a finite recorded set rather than a
statement about an unknown one.

**Attribution is enforced.** An entry that flips with no attributable cause is recorded as an
*unexplained* flip — which is useful information, since it usually means the budget was not in fact
comparable or the original failure was misdiagnosed.

**Version 1's own ingredients are already present but unconnected.** Its Axiom 3 requires organizational
memory to preserve *failed approaches*; its Axiom 12 requires frontier expansion. The failure registry
is the connection: the record of what failed is the instrument that makes expansion observable.

**Architectural consequence.** Version 1's reference architecture (§10) has ten components. This adds
an eleventh — the failure registry — and it belongs beside the organizational unknown-model rather than
inside general memory, because it needs the budget and configuration fields that general memory does
not carry, and because it must be append-only for the comparison to mean anything.

**Limitation.** A registry records only what was attempted. Problem classes never attempted are absent,
so measured expansion is a lower bound on real expansion, biased by what the organization thought worth
trying. This is a real limitation and preferable to the alternative, which is not measuring at all.

---

## 9. Metrics: a frontier, ordered by cost

Version 1's twelve metrics are retained. Two amendments.

**They trade against each other and should be reported jointly.** Version 1 notes individual tensions —
diffusion latency against false-knowledge propagation (§12.4), diversity against convergence (§12.6).
The tensions are general. Collective synergy rises with integration while exploration diversity falls;
compression ratio rises as diversity of method falls; turnover resilience rises with redundancy while
synergy per unit cost falls. **A high score on all twelve simultaneously is not an achievable target
but a sign of metric capture**, which Version 1 lists as failure mode §16.6. The metrics define a
frontier and an organization occupies a point on it.

**They differ enormously in measurement cost, and the framework should say so.**

| Cost | Metric | Why |
|---|---|---|
| **Cheap now** | Governance integrity, knowledge-diffusion latency, promotion latency $T_p$ | Timestamps and counts on events the system already emits |
| **Cheap now** | Turnover resilience | Ablation: remove a member, re-run a held-out task set |
| Moderate | Collective synergy gain, expert-leverage efficiency, exploration diversity | Need a strongest-member baseline and a task distribution |
| Moderate | Institutional improvement competence, topology adaptation gain | Need a counterfactual frozen configuration |
| **Expensive** | Cognitive compression ratio, false-knowledge propagation rate | Need correctness-preserving scope tracking and ground truth on promoted claims |
| **Expensive** | Organizational frontier expansion | Needs the §8 registry, maintained over long horizons |

The ordering matters because Version 1 presents twelve criteria as a set, and an organization reading
it does not know where to start. **It should start with promotion latency**, for three reasons: it
bounds the frontier expansion rate by Proposition 7, it estimates $m^*$, and it is a separation test —
§9.1.

### 9.1 A first measurement, and what it found

We measured promotion latency $T_p$ — the interval between a candidate being available and its
promotion being authorized — on a deployed governed multi-agent system with cryptographically signed
promotion, from its hash-chained audit log. The instrument pairs candidate registration with
promotion, retains censored observations as lower bounds rather than discarding them, and excludes
intervals below a plausible review floor from the estimate.

> **$T_p$ has never been observed.** Of three available data points, two are promotions authorized 5.5
> and 0.0 seconds after registration, and one is a candidate outstanding for 24 days.

Two findings generalize beyond the system measured.

**The system of record could not represent the quantity.** Its promotions table carried kind, name,
version, and metadata, with no timestamp. Every timestamp used came from a side record. **A quantity
that bounds the organization's frontier expansion rate was not recorded by the table that records the
event.**

**A sub-review interval is a separation failure, not a fast organization.** An interval too short for
review indicates the authorization was produced by the process that proposed. By Proposition 1 the
resulting promotion is not knowledge, so $T_p$ is simultaneously a rate measurement and a test of Ω3 —
and a framework that read a near-zero $T_p$ as good news would reward the failure it exists to detect.
This is the concrete form of Version 1's evaluator-contamination signal, and it is detectable from
timestamps alone, without inspecting the organization's intentions.

The general lesson: Version 1's anti-inflation criteria state what would count as evidence. They do not
cause anyone to record it. On present evidence the binding constraint on demonstrating OΩ is
**record-keeping rather than capability**, which is a more tractable obstacle and a more embarrassing
one.

---

## 10. Falsification

Version 1's experimental program is retained. Targets for the claims added here:

| Claim | Refuted by |
|---|---|
| Proposition 1 | An organization whose promoter and proposer coincide producing promoted knowledge that replicates under external verification at rates comparable to separated organizations |
| Corollary 1.1 | Unseparated organizations reliably matching separated ones on held-out outcomes, controlling for member level |
| Proposition 7 | Frontier expansion rate rising monotonically with member count across a domain, with no maximizer, at constant promotion policy |
| §6 lineage | A successor organization universally accepted as legitimate whose provenance chain has a recorded gap |
| §8 registry | Frontier expansion demonstrated to independent satisfaction with no record of prior failure — i.e. a positive-only demonstration that survives scrutiny |
| §4 minimality | A demonstration that one of Ω1–Ω6 is derivable from the others, which would reduce the set further |

The last is an invitation rather than a hazard. An axiom set is improved by being cut down, and Version
2's claim is only that six are independent, not that fewer could not be.

---

## 11. Limitations

Version 1's limitations are retained. Four are added.

**11.1 — Proposition 7 has no functional form.** It establishes that $m^*$ exists, not where. Without a
model of $T_p(m)$ for a given verification regime it cannot be used prospectively, only measured
retrospectively.

**11.2 — The failure registry measures a lower bound.** It records only attempted problem classes, so
expansion measured through it is biased by what the organization thought worth trying — and an
organization whose imagination narrows will appear to expand while its real frontier contracts.

**11.3 — Separation is treated as binary.** Real organizations separate partially: a verifier reporting
to the promoter, a proposer selecting which evidence the verifier sees. Ω3 admits no degrees, and a
graded form is needed and not offered here.

**11.4 — The measurement is one system and one reading.** §9.1 is a single audit log on a single host.
It establishes that the quantity was unrecorded there and nothing about the field. And one reading is
not a measurement: the questions this framework asks of $T_p$ concern whether it *falls*, which
requires a series.

---

## 12. Conclusion

Version 1 established OΩ as a class and gave it criteria, an architecture, failure modes, and a
research program. This version does not dispute it. It reduces twelve axioms to six independent
commitments and derives the rest, so that a reader can see which assumptions carry the framework;
strengthens epistemic promotion from a schema into a structural requirement, on the ground that a
promotion whose verifier is its proposer is not weak knowledge but none; supplies a checkable criterion
for the organizational identity Version 1 establishes by analogy; and turns the defining property from
a statement about an unenumerable set into a count over a retained record of failures.

It adds one result. Because promotion requires separated verification, and verification costs
communication that grows with the number of members consulted, while marginal member value does not,
**there is a size beyond which adding members lowers organizational intelligence.** Growth past it must
be federation rather than accumulation. That is why an OΩ organization is hierarchical, why it looks
simplest where it executes, and why cognitive compression is structurally necessary rather than merely
economical.

And it reports that the cheapest of the twelve metrics — the one that bounds the rate of everything
else — has never been recorded on the deployed system we examined, because the table that records
promotions has no field for when they happened. The criteria tell us what would count. Until the events
are recorded, OΩ remains a specification rather than an observation.

---

## References

Version 1's reference list is carried forward: collective-intelligence findings and their critique;
organizational learning and the exploration–exploitation result; organizational memory and knowledge
creation; LLM multi-agent systems, group-evolving agents, and multi-agent discovery; institution
design; and the expert-utilization results showing that teams can identify an expert and still dilute
its answer.

Works bearing on the material new to this version:

Ashby, W. R. (1956). *An Introduction to Cybernetics*. — requisite variety, underlying §4's minimality
argument and §7's coordination bound.

Amdahl, G. (1967). Validity of the single processor approach to achieving large scale computing
capabilities. *AFIPS*. — the form of the rate bound in §7 and §9.1.

Brooks, F. P. (1975). *The Mythical Man-Month*. — the classical statement that communication cost
grows with team size, of which Proposition 7 is the epistemic analogue.

Popper, K. (1959). *The Logic of Scientific Discovery*. — the boundary-not-the-set move underlying §8.

Yang, C. (2026). *A Two-Axis Intelligence Level Framework for AI Agents, Version 2*. — the individual
axis, the separation gate on organizational levels, and the coherence bound of which §7 is the
organizational counterpart.
