# SARSI-O: Organizational Intelligence

## The anatomy of a mind made of minds — which levels must be present, and why they cannot be uniform

*Document version: 1.0 — 2026-08-22*
*Companion to: `SARSI-I_Terminal_Individual.md` (individual), `fleet/` (coordination stability), `SARSI-Omega_Terminal_Intelligence.md` (terminal), `SARSI_Level_Map.md` (index)*

---

## Abstract

SARSI-I ends with a result it does not develop: an individual cannot referee itself or extend its own
reach, so **the outside is constitutive of the individual rather than an addition to it**. That makes
the organizational scale not an aggregate but a precondition. The fleet paper supplies the stability
rule for coordination among a handful of agents; SARSI-Ω describes the civilizational terminus. Between
them is the question neither asks: *what must an organization contain, in what relation, for it to be
intelligent at all?*

Two results, answering two questions.

- **O1 — Organizational intelligence is a property of structure, not of members.** It is measured on
  five axes, none of which is capability, and it can be **zero with arbitrarily capable members**.
  An organization of terminal individuals with no separation of duties is less intelligent than a
  mixed organization of modest ones. §4, §5.
- **O2 — Levels necessarily coexist.** Not as a tolerated imperfection but as a structural
  requirement, for four independent reasons. Uniformity is not an unreachable ideal; it is a
  degenerate configuration. §7.

§6 answers the first question directly: a table of which individual level does what job, and why each
job admits only that level.

---

## § 1 — What an organization is, and is not

**Definition O1.** An **organization** is a set of individuals together with a **coordination
structure**: who may propose to whom, who may promote whose proposals, who holds which authority
ceiling, what referee is shared, and what couples the whole to the world.

Two things follow immediately, and both are already established elsewhere in the corpus.

**It is not a larger individual.** By SARSI-I Definition I1, an individual is one global workspace;
an organization has none, and its members exchange messages instead. By Proposition I1 there is a
largest possible individual, and past it there is no bigger mind, only a society. **The transition
from individual to organization is a change of kind, not of degree.**

**It is not the sum of its members.** The coordination structure is an independent object. Everything
in §4 is a property of that structure and can be varied while holding the members fixed.

The right image is not a bigger brain. It is closer to a laboratory: benches, instruments, a
reviewer, a records office, a director, and a standing arrangement about who may sign what.

---

## § 2 — Why the organization is prior to the individual

The intuitive reading is that individuals are fundamental and organizations are what you get by
adding them up. The corpus establishes the reverse, twice, on independent grounds.

**From evaluation.** SARSI-B: improvement is well-posed only if the evaluator lies outside the write
set. SARSI-I Proposition I5: everything inside an individual's boundary is, by Definition I1,
available to its single decision process, therefore inside its write set. So an individual's
improvement claim has no meaning without a referee it does not control. **An isolated individual
cannot improve — not "improves slowly", but has no well-formed notion of improvement available.**

**From reach.** SARSI-Ω Proposition Ω1: reach is instrument-bounded and transduction is the sole
coupling of the discovery loop; instruments are built from matter outside the mind. An individual
that does not act on the world has a fixed frontier forever, however capable.

> **Proposition O1 (priority).** *The organizational scale is not an aggregate of the individual
> scale but a precondition of it. An individual's level, as defined in `SARSI_Level_Map.md`, is only
> partially a property of the individual; the referee and reach axes are properties of the
> organization it sits in.*

This has a practical consequence worth stating plainly: **you cannot raise an intelligence's level by
working only on the intelligence.** Two of the axes are not in there.

---

## § 3 — The loop an organization runs

The organization's own loop is the discovery loop of SARSI-Ω §3 with its steps distributed across
members rather than performed by one:

```
  world ──observe──▶ [operator]  ──record──▶  [analyst]
                                                  │
                                              propose
                                                  ▼
   [referee] ◀──evaluate── [proposal] ──build──▶ [instrument-maker]
       │                                                │
     verdict                                         extends reach
       ▼                                                │
   [promoter] ──signs──▶ operative baseline ◀───────────┘
       ▲
   [director] ──sets objective, holds the frozen referee
```

Each bracketed role is filled by an individual, and §6 shows that the role determines which level of
individual may fill it. The arrows are the coordination structure of Definition O1.

---

## § 4 — The five axes of organizational intelligence

None of these is a capability of any member.

**O-A1 — Coverage.** Does the organization contain an individual for every role its loop requires? A
structure with no instrument-maker cannot compound, because by Ω1 transduction is the sole coupling
and nothing else moves the frontier. A structure with no referee produces unfalsifiable claims. **A
missing role is not a weakness; it is an open loop.**

**O-A2 — Separation.** Are proposer, promoter, and referee distinct? This is the independence rule of
`SARSI_Level_Map.md` §4 at organizational scale, and it is the axis on which organizations most often
score zero while believing themselves excellent.

**O-A3 — Throughput.** How long does a proposal take to traverse propose → evaluate → promote? This
is *T*<sub>δ</sub>, and by SARSI-L Proposition 1 it alone bounds the organization's iteration rate
once the automated steps are cheap: ρ<sub>max</sub> = 1/*T*<sub>δ</sub>. **It is also the only axis
here that is directly and cheaply measurable** — timestamp the authorization events.

**O-A4 — Referee externality.** Is the measure of progress authored outside the organization? An
organization that reorganizes its own evaluators and then reports improvement has reported a
tautology (SARSI-Ω A8).

**O-A5 — World coupling.** Does the loop terminate in the world's response, or in more opinion? SARSI-I
§13.4 leaves open whether a closed community of mutually-refereeing individuals is well-posed or
merely a larger tautology. O-A5 is the operational resolution: **it is well-posed exactly to the
extent that its referee chain terminates in an instrument rather than in another member.**

---

## § 5 — O1: structure dominates members

> **Proposition O2.** *Organizational intelligence is not monotone in member capability. An
> organization scoring zero on O-A2 has no well-posed improvement loop regardless of its members'
> levels, while an organization of modest members scoring well on all five axes does. Therefore an
> organization of terminal individuals with no separation of duties is **less** intelligent than a
> mixed organization of ordinary ones.*

*Argument.* By SARSI-B, an improvement claim is meaningless when the evaluator is inside the write
set. O-A2 = 0 means one individual proposes, judges, and adopts. Every improvement the organization
reports is then self-certified, and self-certification is not weak evidence but none. Member
capability enters nowhere in this argument, which is the point: capability determines the *quality of
proposals*, and O-A2 determines whether the organization can tell a good one from a bad one. An
organization that cannot distinguish them does not benefit from better ones.

**Corollary O2a — capability substitutes for structure nowhere.** The recurring institutional hope is
that sufficiently capable members make process unnecessary. The argument above says the opposite:
process is what converts capability into a claim anyone can rely on, and capability without it
produces confident output of unknown quality. This is why every scale of the corpus enforces the same
separation, and why the deployed system never shows the model a permission gate — a property left to
a capable participant's judgement on the day is not a property of the system.

---

## § 6 — Where each individual level works

The first question, answered directly. Levels are given in `SARSI_Level_Map.md` notation:
⟨depth, openness, reach⟩ with the authority ceiling alongside.

| Individual level | Role | Why only this level |
|---|---|---|
| ⟨D0, closed, ∅⟩ · A0 | **Advisor / analyst** | No write set at all, so it may be given information it could misuse if it could act. Advisory ceilings exist for this. |
| ⟨D0, closed, **other**⟩ · A2–A3 | **Guide · promoter · referee** | An **empty self-write set is the only thing that admits authority over another's promotion** (B05). The fleet's self-state prohibition and the architecture's stability condition are the same constraint. |
| ⟨D1, closed, self⟩ · A1 | **Operator** | Accumulates the episodic record the loop runs on. Cannot claim improvement without a held-out ablation, so it is a *source of evidence*, not of verdicts. |
| ⟨D2, closed, self⟩ · A1–A2 | **Specialist / tuner** | Improves its own policy against a metric it did not author. The workhorse level, and the one most current systems occupy. |
| ⟨D3, closed, self⟩ · A3 | **Instrument-maker** | **This is Θ.** By Ω1, transduction is the sole coupling of the discovery loop, so *this is the only role whose work compounds*. §6a. |
| ⟨D4, closed, self⟩ · A4 | **Substrate improver** | Prepares weight or adapter changes in isolation. A4 carries **no deploy authority** by definition, so it is structurally a proposer. |
| ⟨any, **open**, both⟩ | **Director / principal** | The only role that may revise the objective — and only while holding a frozen referee it did not author. In every deployed configuration this is a human. |

### § 6a — The instrument-maker is the role that compounds

Worth isolating, because it is the least intuitive entry and the corpus's own results make it
load-bearing.

Ω1 established that reach is instrument-bounded and that transduction — knowledge becoming apparatus
— is the *only* operator whose output re-enters the loop's input. An organization can therefore have
excellent operators producing flawless records, excellent specialists tuning themselves to the metric,
an impeccable referee, and a fast promoter, and **its frontier will not move at all** if nothing
converts what it learns into something that reaches further.

The diagnostic (Ω1a): the question that predicts whether an enterprise compounds is not how much it
discovers but what fraction of what it discovers becomes apparatus. Under Conjecture Θ1 that fraction
is also substrate-dependent — so an instrument-maker's productivity depends on what manipulation
substrate the organization has, which is a coverage question (O-A1) and not a personnel one.

### § 6b — Two roles no capable member may hold together

**Proposer and promoter.** Directly from the independence rule; enforced in the deployed system by
requiring an owner signature that the proposing agent cannot produce.

**Director and referee.** The director sets the objective; the referee judges against it. If they are
the same, O-A4 is zero and the organization's progress measure is authored by the party it flatters.
The frozen-referee construct (SARSI-B §4) is precisely the mechanism for separating them *in time*
when they cannot be separated in person: the objective is versioned and frozen before the revision it
will judge.

---

## § 7 — O2: will all levels coexist?

The second question. The answer is yes, necessarily — and the interesting part is that uniformity is
not merely unattainable but *degenerate*.

> **Proposition O3 (forced heterogeneity).** *At any decision, the participants must occupy different
> levels. Heterogeneity may be realized permanently across individuals or temporarily within them by
> restriction, but it cannot be absent.*

Four independent arguments, any one of which suffices.

**1 — Separation is level differentiation, enacted.** A referee must have the judged party's write set
excluded from its own. If both are ⟨D4, open, both⟩, the referee *can* write the judged party's state,
and the fleet's stability condition fails: the top-down block of the recurrent coupling returns, the
coupling is no longer nilpotent, and stability must be tuned against fleet size. Restricting the
referee for the engagement restores it — but a restricted individual is, for that engagement, at a
lower level. **So separation of duties is level differentiation by another name.**

**2 — The bound is a frontier, not a peak.** SARSI-I Corollary I1b: because capacity rises with volume
while rate falls with radius, the terminal individual sits at an *interior* optimum set by what it is
for. A fast-narrow mind and a slow-wide one can both be terminal. An organization facing more than one
kind of decision therefore needs more than one kind of mind, and **no single configuration dominates**.
Heterogeneity here is forced by the shape of the physical bound, not by scarcity.

**3 — The depths run at different clock speeds.** SARSI-B B-Rule 3 and Corollary B4: loop period and
per-iteration gain rise together with write depth, from memory in seconds to weights in months, and a
brain running only one depth is defective. Distributed across an organization, the fast loops must sit
close to the work and the slow ones behind a gate — which assigns different depths to different
bodies as a matter of structure.

**4 — Authority is earned over time, and new members keep arriving.** A3 unlocks at fifty clean
approvals with zero tripwires, or by explicit owner election. New agents start at A0. **So long as an
organization can admit anyone new, it contains members at every ceiling simultaneously** — not as a
transitional state but as a steady one.

**Corollary O3a — permanent differentiation beats per-engagement restriction.** Argument 1 allows
uniform members restricted per round. But that arrangement relies on a capable participant honoring a
restriction, and the corpus's own design principle rejects exactly this: the model is never shown a
permission gate, because a property left to judgement on the day is not a property of the system.
Structural differentiation is enforceable; self-restraint is not.

**Corollary O3b — the uniform maximal organization is a degenerate configuration.** An organization
composed entirely of maximal individuals, all holding all roles, scores zero on O-A2 and by
Proposition O2 has no well-posed improvement loop. **It is not the strongest possible organization;
it is one of the weakest, and its members' capability does not rescue it.** The recurring picture of
a future filled with uniformly maximal minds describes something that would be, as an organization,
less intelligent than a well-structured laboratory of ordinary ones.

---

## § 8 — Reporting an organization's level

```
O-A1 coverage      : which roles of §3 are filled, which are vacant
O-A2 separation    : proposer / promoter / referee — distinct or not
O-A3 throughput    : T_δ, measured from authorization timestamps
O-A4 referee       : externally authored, self-authored, or absent
O-A5 world coupling: does the referee chain terminate in an instrument
```

Plus the **level census** — the distribution of member levels across the roles of §6. An organization
whose census is concentrated at ⟨D1–D2, closed, self⟩ is a production system; one with no ⟨D3⟩ entry
does not compound; one with no ⟨D0, other⟩ entry cannot validate; one with no open-objective entry
cannot change what it is for.

**The deployed system, profiled.** Coverage: all roles filled — operators are the session agents,
guide and promoter are the machine agent, referee is the control plane, director is the owner;
instrument-maker is the thinnest, since the RSI loops tune parameters more than they build apparatus.
Separation: strong — verdicts are computed control-plane-side, promotion requires an owner signature
the proposer cannot produce. Throughput: *T*<sub>δ</sub> is human review latency, unmeasured.
Referee: external. World coupling: yes for imaging, through held-out scenes and real reconstructions.
**Diagnosis: well-separated, coverage-complete, thin at the role that compounds, and not measuring
the one quantity that bounds its rate.**

---

## § 9 — Open problems

**9.1 — O-A2 has no scale.** Separation is treated here as present or absent. Real organizations
separate partially — a referee who reports to the promoter, a director who selects the evidence. A
graded measure is needed and is not offered.

**9.2 — The census has no optimum.** §7 shows heterogeneity is forced and says nothing about
proportions. How many operators per instrument-maker, and whether that ratio is a property of the
domain or of the organization, is unaddressed. Given §6a makes the instrument-maker the role that
compounds, this is the gap that matters most.

**9.3 — Restriction is not verified.** Corollary O3a prefers structural differentiation on the grounds
that restriction relies on self-restraint. But a *mechanically* restricted maximal individual — write
set narrowed by the control plane rather than by instruction — would satisfy the argument. Whether
that is achievable for an individual capable enough to matter is exactly the alignment question, and
this document has no more to say about it than the rest of the corpus.

**9.4 — Nothing here scales to the civilizational case.** SARSI-Ω §13 shows that at stellar scale,
light-speed forces ~10⁵³ local operations between opportunities to agree. Every axis in §4 presumes a
coordination structure that can actually coordinate. What O-A2 means when the referee is sixteen
light-minutes away is not treated.

---

## § 10 — Principles

**O01 — Structure over members.** Organizational intelligence is a property of the coordination
structure. It can be zero with arbitrarily capable members, and capability substitutes for it nowhere.

**O02 — The organization is prior.** Two of an individual's level axes — referee and reach — are
properties of the organization it sits in. An isolated individual has no well-formed notion of its own
improvement.

**O03 — A missing role is an open loop.** Not a weakness to be compensated by excellence elsewhere.
An organization with no instrument-maker does not compound however good its analysts.

**O04 — Only transduction compounds.** By Ω1 it is the sole coupling. Every other role produces
output; one role moves the frontier.

**O05 — Levels must coexist.** Forced four times over: by separation, by the shape of the individual
bound, by the timescale hierarchy, and by earned authority in an organization that admits newcomers.

**O06 — Uniform maximal is degenerate.** An organization of identical maximal minds holding all roles
has no well-posed improvement loop. It is weaker than a structured organization of ordinary ones, and
its members' capability does not rescue it.

**O07 — Measure T_δ.** It is the only axis here that is cheap to measure and the one that bounds the
rate. An organization that has never timestamped its own authorization decisions does not know its
own ceiling.

---

## Relation to prior documents

| Document | Scale | Question |
|---|---|---|
| `self_awareness/` | Agent | What does an agent know about itself? |
| `SARSI-I_…md` | Individual | What is the best a single mind can be? |
| `fleet/` | Fleet | What may one agent assert about another? |
| **This document** | **Organization** | **What must a mind made of minds contain, and in what relation?** |
| `SARSI-B_…md` | Brain | What may an agent change about itself? |
| `SARSI-L_Paper_v3.md` | System | How far has RSI propagated across substrates? |
| `SARSI-Omega_…md` | Terminal | Where does the whole trajectory end? |

SARSI-O supplies what SARSI-I §9's Corollary I5a asserted without developing, and what the fleet paper
leaves out by scope: the fleet paper gives the stability *rule* for coordination, this gives the
*anatomy* — which levels must be present, in which roles, and why uniformity is degenerate. Its own
contributions are Definition O1, the five axes of §4, Proposition O2, the role map of §6, and
Proposition O3.

## Version history

**1.0 — 2026-08-22.** Initial. Written in response to two questions: where each level of individual
intelligence works inside an organization, and whether all levels coexist. §6 answers the first, §7
the second.
