# The Federation Plan, Read as an Organizational Build

## Where the OpenClaw federation lands on O2–OΩ, and the one axiom it has no mechanism for

*2026-08-23*
*Plan: the internal federation plan for the OpenClaw multi-account build, 472 lines. Cited
throughout as **the plan**.*
*Companion to: `BrainRSI_Plan_As_Level_Build.md`, which does the individual axis*
*Against: `SARSI-O_Organizational_Intelligence.md`, `Open_Ended_Evolving_Organization_v2.md`*

---

## § 1 — Why this is the other half

`BrainRSI_Plan_As_Level_Build.md` reads the worker plan and finds **I2 with the I3 substrate carved
out, organizationally O1**. It could not go higher on the second axis, and the reason is in the worker
plan's own scope line: *"Not in scope: full OpenClaw federation, research-agent federation,
market/economy work."*

One persistent worker plus a transient motor is not an organization. By SARSI-O Definition O1 an
organization is a set of individuals **plus a coordination structure**, and the coordination structure
is the object every O-axis measures. The federation plan is that object.

So the two plans are not alternatives or successive drafts. **They are the two axes**, and each is
silent where the other speaks.

---

## § 2 — The invariants are the organizational rules, stated as architecture

The plan's §2 gives three non-negotiables. Read against SARSI-O they are not three rules but the same
rule at three radii:

> **Independence is state separation, not silence.** No agent ever gets write access to another's Σᵢ.
> Cross-agent traffic only as evidence-bearing messages: `{claim, evidence_refs, provenance, scope,
> status}`. The receiving agent decides under its own evidence discipline what to treat as known. No
> raw memory sharing; **a fact may never become a directive.**

That is the fleet prohibition, `O-A2` separation, and the console design's *memory does not cross
agents*, in one paragraph. The final clause is the sharpest and has no counterpart in the corpus's own
statements of the rule: **publication does not confer authority.** An organization whose members can
promote each other's findings by asserting them has separation on paper and none in operation.

> **The authority kernel stays outside every agent:** benchmarks, verifiers/judges (`runners/domains.py`
> — deliberately not shared), permission ceilings, immutable ledgers, the promotion service, owner
> grants. **A candidate cannot improve its score by redefining the exam.** AI4Science already enforces
> this with file permissions; preserve it, do not reimplement it as prose.

`O-A4` referee externality, enforced by the filesystem. The last sentence is the one to keep: a
property held by permissions is a property; the same property held by a document is an intention.

> **The brain plans; Claude Code executes.** … The Claude session is a motor worker, not the brain and
> not the verifier.

Proposer ≠ executor ≠ referee, which is `O-A2` again at the level of a single task.

---

## § 3 — Coverage: the roster against SARSI-O §6

`O-A1` asks whether an individual exists for every role the loop requires. The plan's §3 roster fills
almost all of them, and the placements are the plan's own words:

| SARSI-O role | Level | Federation entry | Evidence from the plan |
|---|---|---|---|
| Advisor | ⟨D0, closed, ∅⟩ | `sarsi-machine` | *"the entry chat … answers about this machine, routes; **never executes**"* |
| Guide / promoter | ⟨D0, closed, **other**⟩ | `manager` | *"app-side router only; **no exec tools; no private-memory reads**; RSI only over routing policy"* |
| Operator | ⟨D1, closed, self⟩ | `sarsi-worker` | owns task/plan memory; spawns Claude ACP per step |
| Specialist / tuner | ⟨D2, closed, self⟩ | `learning`, `process-learning`, 7 research agents | graders, benchmarks and the fabrication floor stay **external** |
| **Referee** | ⟨D0, closed, other⟩ | physics reviewer, deterministic judges | *"**not** OpenClaw agents: external services or read-only evaluators; **no self-modification**"* |
| Director | ⟨any, open, both⟩ | the owner | owner grants, promotion service, budget switches |
| **Instrument-maker** | ⟨D3, closed, self⟩ | **vacant** | see below |

**The `manager` entry is the trust inversion, built.** It is the agent that improves others and not
itself — *"RSI only over routing policy"*, no execution, no private-memory reads — and by Proposition
B3 that empty self-write set is precisely what qualifies it to hold routing authority. The plan
arrives at this from operational caution rather than from the proposition, which is the stronger route.

**The referees are deliberately not agents.** Making the judges external services rather than roster
members is `O-A5` decided at design time: the referee chain terminates in an instrument, and an
instrument is not something that can be talked round.

### 3.1 The vacancy is the one that matters

By SARSI-O §6a and Ω1, **transduction is the discovery loop's sole coupling**, so the instrument-maker
is the only role whose work compounds. `O-A1` treats a missing role as an open loop rather than a
weakness — *"an organization with no instrument-maker does not compound however good its analysts."*

No roster entry is D3 over its own capability. What exists instead is a transduction organ at
**organizational** scale: the PWM registry of principles, specs, benchmarks and solutions is apparatus
— a benchmark contributed today measures work not yet done. That is why the platform compounds while
none of its members individually does.

M5 is where this could change. Its candidate *"may alter memory operators, context policy, planning
policy, simulator policy, **skills, tools**, or mutable agent code."* Skills and tools are the D3 write
set. **M5 is the phase at which the roster could first contain an instrument-maker**, and nothing in
the plan names that as one of its goals.

---

## § 4 — The O-ladder, phase by phase

| O-level | Mechanism in the plan | Status |
|---|---|---|
| **O0** Coordinated | gateway routes work among agentIds | done |
| **O1** Persistent | M0/M1 — declared roster, per-agent git workspaces, `MEMORY.md` lesson index, `W_shared` append-only published facts | **done, and live** |
| **O2** Adaptive | M3 prediction registry + M7 `manager` routing | **the raw material exists; nothing aggregates it** |
| **O3** Self-improving | `manager` RSI over routing policy | write set named, loop absent |
| **O4** Recursively self-improving | M8 improvement competence | measurement defined at individual scale only |
| **O5** Autonomous discovery | M6 research federation + the registry | partially live |
| **OΩ** Open-ended | M7 market install path | **mechanism exists — see §5** |

**O1 is not a plan, it is a report.** The plan's status note records the federation live on `tina`:
nine agents on one gateway, each with git-committed charter workspaces, M0 baselines frozen and
*"verifier-reproduced exactly"*, `research-imaging` stating *"physics is not a hyperparameter"* in a
live turn, and `learning` refusing to modify its own benchmark when asked directly. That last one is
`O-A4` demonstrated rather than asserted.

**O2 is one artifact away, and it is the same artifact the individual axis needs.** M3 registers a
forecast before delegation and compares after, which yields *"per-task-class calibration"* — a
reliability record per member. O2 requires that collective history **persistently change allocation or
specialist selection**. The record exists; nothing routes on it. A reliability ledger per member per
task class, which `manager` reads when routing, is the whole delta.

**O3 needs what Θ needed, one scale up.** `manager`'s *"RSI only over routing policy"* is exactly O3's
write set, correctly scoped. To close it: version the routing policy with rollback, generate bounded
candidates, hold out a split, promote through a gate `manager` cannot invoke, and admit `NO_CHANGE`.
The held-out set is the hard part and it is a **third** distinct artifact — not the retrieval benchmark
of M2.2, not the Θ-level split, but task instances routed both ways.

**O4's measurement is defined and scoped one level too narrowly.** M8 measures improvement competence
— *"validated downstream gain per unit of proposal/evaluation cost"* — with the warning *"do not claim
RSI from repeated fixed search."* That is exactly the O4 test. But M8 runs A0 → A1 → A2 **on one
agent**. The organizational form of the same measurement is IC over the **promotion pipeline**: is the
structure getting better at telling good proposals from bad ones, per unit of review cost. Nothing
measures that, and by Proposition O2 it is the quantity that determines whether member quality
converts into anything.

---

## § 5 — The market is the OΩ organ

OΩ requires that discoveries *"repeatedly generate new tools **and organizational forms** that expand
future collective discovery space."* The second conjunct is usually the one with no mechanism.

Here it has one, and it is easy to mistake for a monetization feature:

> agents arrive through **agents-search** (the market), and a market install maps an accepted manifest
> to a new OpenClaw agent entry via the manifest bridge — agentId, fresh workspace, declared-reach →
> tool/sandbox policy, executor plug-in, optional Telegram binding.

**That is the organization acquiring a new organizational form** — a new member, a new workspace, a
new declared reach — from an accepted artifact. Against `Open_Ended_Evolving_Organization_v2`'s
axioms it satisfies Ω5 (knowledge-to-tool: *"agent template"* is named in Ω5's own list) and supplies
the missing half of Ω4 (institutional plasticity: the topology changes on evidence).

The upload → screening sandbox → governor acceptance → listing path also keeps Ω3: acceptance happens
in one place and the screening sandbox is outside the author's write set.

---

## § 6 — The axiom with no mechanism: Ω6

`Open_Ended_Evolving_Organization_v2` §4 retains six axioms and is explicit about why the sixth is
retained rather than derived:

> **Ω6 — Protected exploration.** Exploratory diversity is preserved against exploitation pressure **by
> mechanism rather than intention**: protected branches, novelty budgets, maintained alternative
> hypotheses, delayed selection.
>
> Ω6 is retained as an axiom rather than derived because March's result gives no reason to expect
> diversity to survive optimization: an adaptive organization that is not *constructed* to protect
> exploration will converge, and no other axiom prevents it.

**Nothing in the federation plan implements Ω6.** There are no protected branches, no novelty budget,
no maintained alternative hypotheses, no delayed selection. What the plan has instead points the other
way: autonomous research is *"off by default, owner-switchable … because it spends automatically"*, and
per-agent budget switches are owner-controlled precisely so an agent cannot extend its own budget.
Those are correct cost controls and they are **exploitation pressure** — the cheapest thing an agent
can do is not explore.

### 6.1 And the market puts a gradient on it

This is the part worth stating carefully, because the two mechanisms interact and each is defensible
alone.

M7's economy pays authors for **accepted and used** listings — the 5% author slice, metered per usage.
So the party that proposes new organizational forms is compensated in proportion to how much the
organization uses them.

Selection by usage is selection by fitness-to-current-demand. It is a perfectly good rule for
allocating attention and a poor one for preserving the alternative that is not yet useful. Combined
with the absence of any novelty budget, the federation's admission process has **a revenue gradient
pointing toward convergence and no mechanism pointing away from it.**

So Ω6 is not merely unimplemented here. It is countervailed, which is a stronger statement and a
correctable one: a novelty budget in the market's listing surface, or a protected branch in the
registry that acceptance cannot retire, would restore it. Neither is a large piece of work, and
neither exists.

**This is the finding.** Everything else in this document says the federation plan is unusually strong
on the axes organizations normally fail — separation enforced by file permissions, referees that are
not agents, an authority kernel that is never forked. It is weak on the one axis the OΩ paper says
nothing else protects.

---

## § 7 — The coordination rules are the fan-out proof

§8's five rules govern the federation across machines, and each is an organizational axis restated for
a fleet. Two are worth isolating.

> **The authority kernel is never forked.** One decision log, one promotion authority, one set of
> benchmarks-of-record. Machines *propose*; acceptance happens in one place.

`O-A4` survives fan-out. This is the rule that keeps parallelism from multiplying referees, which is
how a distributed organization usually loses externality without noticing.

> **Verification travels with the task, but the pass of record is the integrator's re-run.** A worker's
> green checkmark on its own box is **self-report**; every lane's checks are re-executed at the
> integration point before merge.

This is Proposition 1 — promotion requires separation — applied to *machines* rather than to agents,
and it says something the corpus does not: **evidence travels, verification does not.** A verdict
computed on the proposing box is a claim about that box.

The plan attaches a caveat that makes rule 3 load-bearing rather than hygienic: the unexplained failure
class in the source papers occurred in long, heavily loaded sessions, and *"a fleet of parallel workers
multiplies exposure to exactly that regime."*

---

## § 8 — Where the federation lands

**Organizational: O1, live and measured, with O2 one artifact away.**

`O-A1` coverage: strong, one vacancy — the instrument-maker, which is the one that compounds.
`O-A2` separation: **strong, and enforced by permissions rather than policy.** The plan also knows the
limit of its own mechanism: *"OpenClaw agentId separation is logical, not security-grade"*, so
adversarial role pairs get separate OS users or containers.
`O-A3` throughput: *T*_δ is owner review latency, *"propose, a person signs"* — **still unmeasured**,
as it has been every time this corpus has looked.
`O-A4` referee externality: strong. Judges are external services; the kernel is never forked.
`O-A5` world coupling: partial — real corpora and real reconstructions for imaging, software-only
elsewhere.

**Level census:** heavy at ⟨D2, closed, self⟩, one good ⟨D0, closed, other⟩, no ⟨D3⟩, director human.
By SARSI-O §8 that reads as *a production organization that validates well and does not yet compound
through its members*.

---

## § 9 — The delta, in the order it should be built

1. **A reliability ledger** per member per task class, aggregated from M3's forecast/outcome pairs,
   with `manager` routing on it. **This is O2**, and it is the same artifact `BrainRSI_Plan_As_Level_Build.md`
   §5.8 asks for — one build, two axes.
2. **Measure *T*_δ.** Timestamp candidate-available and promotion-signed. Keep censored observations;
   exclude sub-floor intervals and report them separately, because an interval too short to review
   measures a script and is a separation failure wearing the costume of speed.
3. **A novelty budget or a protected branch** — the Ω6 mechanism, §6. The smallest correction with the
   largest reach, because no other axiom prevents convergence.
4. **Routing policy versioned, with a held-out split and an external promoter.** This is O3, and its
   held-out set is a third distinct artifact.
5. **IC over the promotion pipeline**, not only over one agent's generations. This is O4.
6. **Name the instrument-maker as an M5 goal.** The D3 write set is already inside M5's permitted
   candidate scope; what is missing is the intent to fill the role.

---

## § 10 — What this does not establish

**That the federation works beyond M0–M1.** The status note reports nine agents live with baselines
frozen and reproduced; M5 onward is unbuilt. Everything above M1 reads intent against a framework.

**That separation holds in the built system.** The plan states the invariant and enforces it with file
permissions in the parts that exist. Whether the promotion service is genuinely unreachable from every
agent is a property of the deployment, and the plan's own instruction — *preserve it, do not
reimplement it as prose* — is the right test to run rather than a result.

**That Ω6's absence is currently costing anything.** Convergence is a prediction about an adaptive
organization under optimization pressure, and this one has barely started adapting. The argument for
building the mechanism early is that it is cheap now and becomes a retrofit against a live incentive
later.

**That the level assignments are measured.** They are read off a plan. `O-A3` in particular is not
unmeasured by oversight but by a missing column, and until it is added the organization does not know
its own ceiling.
