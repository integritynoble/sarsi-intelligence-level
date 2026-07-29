# Recursive Self-Improvement Is Substrate-Indexed

## A Falsifiable Framework for Intelligence Trajectories from Language Models to Stellar Engineering

**SARSI-L Consolidated Paper — Version 3.0**
*2026-07-29*

*Consolidates and supersedes: SARSI-L_Framework.md (v1.0), SARSI-L_Framework_v2.md (v2.0), SARSI-L_Critical_Revision.md, SARSI-L_Framework_v2.1.md, Civilizational_Transcendence_Paper.md (v1.0)*

---

## Abstract

The intelligence-explosion literature treats recursive self-improvement (RSI) as a primarily cognitive phenomenon: a system that improves its own reasoning improves its ability to improve its reasoning, and growth becomes super-exponential. This paper argues that the standard treatment omits the variable that actually governs the trajectory. Recursive self-improvement is **substrate-indexed**: an improvement loop is always a loop *over some substrate the system can modify*, and a system can only close loops over substrates it can reach. We decompose RSI into five substrate domains — software, hardware, physical, biological, stellar — and give each a falsifiable operational closure criterion stated as a four-or-five step autonomy requirement.

Two results follow. First, we derive the half-circle ceiling that prior versions of this framework asserted without justification. Applying an Amdahl-style argument to loop autonomy (Proposition 1), we show that external compensation for a missing loop step bounds the *iteration rate* of improvement, not the *capability gain per iteration*. The corollary is uncomfortable for the framework: a compensated half-circle can outperform a closed loop indefinitely unless per-iteration returns to compensation diminish. That premise, not loop closure itself, is the framework's load-bearing empirical assumption, and it is currently unverified.

Second, we distinguish two kinds of floor on loop period. Human-throughput floors are removed by closure; physical-process floors are not (Proposition 2). Fab qualification, clinical endpoints, and orbital launch cadence are bounded below by physics and biology, and no amount of cognitive acceleration compresses them. They yield only to parallelism, which converts a time constraint into a resource constraint — and the capability that supplies unbounded parallelism is physical self-replication, which sits behind a mutual dependency between the hardware and physical circles. We show this mutual dependency is not a deadlock (Proposition 3), because each circle depends on *partial* rather than full completion of the other, permitting a bootstrapping ladder.

Together these give the trajectory its characteristic shape: rapid apparent acceleration through the software loop, followed by a **matter bottleneck** at the software/physical interface where growth is regulated not by cognition but by the slowest physical process on the critical path. We show that the framework's own historical revisions are consistent with this: the magnitude of timeline error in the pre-critique version increases monotonically with the substrate's distance from software, from +3–8 years for the software loop to +35–75 years for the stellar loop.

We present four-scenario timeline ranges rather than point estimates, give explicit falsification conditions for each structural claim, and identify a hazard in the framework's own self-revision mechanism: a theory licensed to update its parameters on disconfirmation is unfalsifiable unless its revision rules are fixed in advance. We propose a pre-registration protocol as the remedy. Six open problems are stated, including one — the compensation ceiling — whose resolution determines whether the framework's central prediction holds at all.

---

## 1. Introduction

### 1.1 The question

I.J. Good's formulation of the intelligence explosion is sixty years old and still the canonical one: an ultraintelligent machine can design better machines; "there would then unquestionably be an 'intelligence explosion,' and the intelligence of man would be left far behind" (Good, 1965). The modern literature has refined the argument considerably — Chalmers (2010) on the structure of the inference, Bostrom (2014) on recalcitrance and optimization power, Yudkowsky (2013) on the microeconomics of returns to cognitive reinvestment — but the shape of the claim is unchanged. A system that improves its improvement capacity grows faster than any system that merely improves.

The claim is probably true. It is also, as usually stated, radically underdetermined about the thing practitioners and policymakers actually need to know: *how fast, and what rate-limits it*.

This paper's answer is that the question cannot be answered at all in the abstract, because there is no such thing as "the" improvement loop. There are improvement loops over substrates, they have very different periods, and the binding constraint migrates from one substrate to the next as each is mastered. A theory of RSI that does not index by substrate is not a theory of RSI's timing; it is a theory of RSI's possibility, which was never seriously in doubt.

### 1.2 What the standard treatment omits

Consider the difference between two improvements a self-improving system might make.

It might revise its own training curriculum, retrain, evaluate on held-out benchmarks, and adopt the improved weights. Every step of that loop is a computation. The loop period is bounded below by compute availability and can, in principle, fall to hours.

Or it might determine that its architecture is bottlenecked on memory bandwidth, design a chip that fixes this, and fabricate it. Now the loop passes through photolithography, process qualification, yield ramp, and the physical construction of a facility that costs upward of twenty billion dollars and takes three to five years to build. The loop period is bounded below by concrete, tool delivery, and the diffusion physics of a process node. It cannot fall to hours. It cannot fall to months.

Both are recursive self-improvement. They differ in period by four to five orders of magnitude. Any model that treats "the" recursion rate as a single parameter — including the standard super-exponential and finite-time-blowup models — is averaging over a distinction that determines the entire trajectory.

Kurzweil's Law of Accelerating Returns (2005, 2024) is the most influential quantitative treatment, and it inherits this problem in a specific way. The empirical base for the law is drawn overwhelmingly from information technology: transistor counts, cost per computation, sequencing cost, bits per dollar. Information technology is precisely the domain in which the substrate constraint had already been relaxed — where improvements propagate at the speed of design rather than the speed of construction. Extrapolating those curves into domains where matter must be moved is not a generalization of the law. It is an application of the law outside the regime that established it.

### 1.3 Contributions

1. **A substrate-indexed formulation of RSI** (§2), with the improvement loop defined as a four-step operation over a specified substrate, and closure defined as autonomy across all steps.

2. **Falsifiable operational closure criteria** for each of five substrate domains (§3), replacing definitions that could be satisfied post hoc by any sufficiently capable system.

3. **A derivation of the half-circle ceiling** (§4), which prior framework versions asserted without mechanism. Proposition 1 gives an Amdahl-style bound showing that compensation limits iteration rate rather than capability. Corollary 2 identifies the resulting load-bearing premise — diminishing per-iteration returns to compensation — and states it as an open empirical question rather than a theorem.

4. **A structural analysis of inter-loop dependency** (§5), establishing that the dependency graph is not a chain: the hardware and physical loops are mutually dependent (a cycle), and the biological loop is off the critical path to the stellar loop. Proposition 3 shows the cycle is not a deadlock.

5. **The matter bottleneck** (§5.5), following from Proposition 2: closure removes human-throughput floors on loop period but not physical-process floors, so post-closure growth is regulated by the slowest physical process on the critical path.

6. **A falsification protocol** (§8), including a remedy for the unfalsifiability hazard introduced by the framework's own self-revision mechanism.

### 1.4 What this paper does not claim

It does not forecast. Every date here is a conditional scenario range with a stated critical-path condition, and §6.2 gives the base rate for treating any such range as a prediction.

It does not claim the five-domain decomposition is exhaustive or uniquely correct. §2.4 gives the criterion by which the list was constructed and the conditions under which a domain should be inserted or removed.

It does not resolve the compensation ceiling problem (§4.4), the attractor circularity (§10.2), or the measurement of loop completion (§10.3). These are stated as open, and the first of them is load-bearing: if it resolves against the framework, the framework's central prediction fails.

It makes no claim about machine consciousness. Earlier versions of this framework included a "sentient robotics" milestone; §3.4 explains why that was a category error and what replaced it.

---

## 2. The Core Claim: Recursive Self-Improvement Is Substrate-Indexed

### 2.1 Definitions

**Definition 1 (substrate domain).** A substrate domain *d* is a class of physical or informational structure that (i) causally determines some component of a system's capability, and (ii) can in principle be modified by that system's own action.

**Definition 2 (improvement loop).** An improvement loop over domain *d* is an ordered operation

$$L_d = \langle \iota, \mu, \nu, \delta \rangle$$

where, with respect to the system's own *d*-substrate:

- **ι** (*identify*) — generate a candidate modification predicted to improve a specified capability;
- **μ** (*implement*) — realize the candidate as an actual modification;
- **ν** (*validate*) — verify improvement against an evaluation not used in generating the candidate;
- **δ** (*deploy*) — install the validated modification as the system's operative baseline in *d*.

**Definition 3 (closure).** $L_d$ is **closed** iff all four operations execute without human approval at any step, and δ results in the modified system becoming operative. A loop in which ι, μ, and ν are autonomous but δ requires authorization is *not* closed. This case is not a technicality; it is the current state of the software loop (§3.2), and the gate at δ is institutional rather than technical.

**Definition 4 (half-circle).** A **half-circle** over *d* is an improvement loop in which one or more steps is performed by an agent external to the system — typically a human, an organization, or a supply chain — while the remainder is autonomous. The external steps are said to be **compensated**: substituted for rather than automated.

**Definition 5 (loop completion).** $\lambda_d \in [0,1]$ is the weighted fraction of a loop's steps that execute autonomously, where weights $w_i$ reflect each step's share of the loop's decision content and sum to 1. Closure ⟺ $\lambda_d = 1$. Loop completion is continuous; §3.5 and Appendix B give the qualitative scale used to report it, and §10.3 is honest about the fact that these weights are currently estimated rather than measured.

### 2.2 The recursion, restated

The standard formulation is that a self-improving system satisfies

$$C(t + \Delta t) = C(t) + f(C(t))$$

and a *recursively* self-improving one satisfies

$$C(t + \Delta t) = C(t) + f(C(t), f)$$

— the improvement function is itself an argument. This is correct but insufficiently specified. It licenses super-exponential growth without saying what the time step $\Delta t$ is, and $\Delta t$ is where all the content lives.

The substrate-indexed formulation makes $\Delta t$ explicit. For a loop over domain *d* with period $P_d$, the number of improvement iterations in an interval is $\rho_d = 1/P_d$, and capability growth is

$$C(t + P_d) = C(t) + g_d\big(C(t)\big)$$

where $g_d$ is the per-iteration gain available through modifications of substrate *d*. A system with several loops closed accumulates gains from each, at each loop's own rate:

$$\frac{dC}{dt} \approx \sum_{d \in D_{\text{closed}}} \rho_d \cdot g_d\big(C(t)\big)$$

This is a schema, not a law — the $g_d$ are not measured and probably not measurable at present. Its purpose is structural: it makes visible that a system's growth rate is a sum over *closed* substrate loops, each contributing at its own period, and that opening a new domain adds a term rather than multiplying an existing one. The multiplicative form used in earlier versions of this framework,

$$R_n = R_1 \cdot \prod_{k=2}^{n} \mu_k, \qquad \mu_k > 1$$

should be understood as the claim that closing loop *k* also raises the per-iteration gain available to every inner loop — better chips make software experiments cheaper, so more of them run. That claim is plausible and is retained, but it is a claim about cross-loop coupling, not a derived result, and the $\mu_k$ have never been estimated from anything.

### 2.3 Why substrate is the right index

Three properties distinguish substrate domains from other ways one might partition improvement capability, and jointly they are why substrate is the index that governs timing:

**Period separation.** Loop periods across the five domains span roughly five orders of magnitude, from hours (software) to years or decades (fab construction, clinical endpoints, orbital campaigns). Any partition whose cells have similar periods would not explain trajectory shape; this one does.

**Access asymmetry.** A system can only close a loop over a substrate it can *reach*. Reaching a new substrate is generally not a matter of degree but of kind: a system with no actuators cannot partially modify matter. This gives the domains their nested character.

**Floor heterogeneity.** The lower bound on each loop's period has a different source — external-agent throughput in some domains, irreducible physical process time in others. §4 and §5 show these two floor types behave completely differently under closure, and that the distinction is what actually determines the trajectory.

### 2.4 The five domains

| # | Domain | Substrate modified | Characteristic period floor | Floor type |
|---|---|---|---|---|
| I | Software | Architecture, training process, weights | Hours–weeks (compute-bound) | Throughput |
| II | Hardware | Chip design and fabrication | Months (design) / years (fab) | Mixed |
| III | Physical | Matter, machines, self-replication | Months–years (construction, materials) | Physical |
| IV | Biological | Organisms, disease processes, aging | Years (biological response time) | Physical, partly irreducible |
| V+ | Stellar | Orbital energy capture at scale | Years–decades (launch, in-space assembly) | Physical |

The list is constructed by a single criterion: a domain earns a place iff a closed loop over it removes a constraint that is binding on every inner loop and that no inner loop can remove by itself. Software closure removes the human-throughput constraint on cognitive iteration. Hardware closure removes the fixed-compute constraint. Physical closure removes the constraint that matter must be moved by human-directed industry. Biological closure removes mortality as a limit on accumulated expertise. Stellar closure removes the energy constraint.

By that criterion the list is neither obviously complete nor obviously minimal, and the framework should say so. A sixth domain would be warranted if a substrate emerged whose closure lifted a constraint binding on all five — the most-discussed candidate is fault-tolerant quantum computation, which would arguably warrant insertion between I and II rather than after V+, since it modifies the compute substrate rather than adding a new physical reach. Conversely, IV is the weakest member of the list on this criterion, since its constraint (mortality limiting expertise accumulation) is binding on human participants rather than on the loops themselves. §5.3 shows that IV is in fact off the critical path, which is consistent with its weaker standing here.

---

## 3. Operational Closure Criteria

The prior version of this framework classified loops as open or closed without specifying what behavior constituted closure. This permitted post-hoc classification: any impressive system could be said to have closed a loop, and any disappointing one to have not. The remedy is a criterion per domain that is specific, observable, and cannot be satisfied by definitional adjustment after the fact.

### 3.1 Form of the criteria

Each criterion has the form: *a system that, without human approval at any step, performs operations (a)…(n)*. Two conventions matter.

First, **the deploy step is included and is not negotiable.** A system that designs, implements, and validates a self-modification but requires authorization to adopt it has not closed the loop, because the authorizing agent's throughput remains in the loop period (Proposition 1). This is where most near-miss cases will fall.

Second, **"without human approval" admits a sliding scale in practice**, since oversight can be configured to intervene only in exceptional cases. The criterion should be read as: no human decision is required in the modal iteration, and the system's baseline advances when humans do not act. Standing authority to halt is compatible with closure; required authority to proceed is not.

### 3.2 The criteria

**Circle I — Autonomous software self-improvement.** A system that, without human approval at any step: (a) identifies a modification to its own architecture or training process predicted to improve a specified capability; (b) implements it; (c) validates the improvement against a held-out evaluation not seen during design; (d) deploys the modified system as its new baseline.

**Circle II — Autonomous chip design and manufacture.** A system that, without human design decisions: (a) generates a chip specification optimized for its own computational needs; (b) produces production-ready physical design output; (c) controls a fabrication process yielding functional chips at economically viable yield; (d) integrates the resulting chips into its own compute infrastructure.

*Critical distinction:* (a)–(b) are chip **design**, a software problem. (c)–(d) are chip **manufacture**, a physical-infrastructure problem. Conflating them was the single most consequential error in this framework's earlier timelines (§6.5). Design maturity and fab autonomy are separated by roughly a decade of feasibility even under optimistic assumptions.

**Circle III — Autonomous physical manipulation.** A system that, without human oversight: (a) identifies a physical resource or infrastructure need; (b) designs the machines and process to fulfill it; (c) manufactures those machines from available materials; (d) operates them, handling failure modes not anticipated at design time; (e) repairs or replaces components using in-situ materials.

*Steps (c)–(e) constitute self-replication, and self-replication is the criterion* — not useful robotic deployment. This distinction disqualifies essentially all current humanoid and industrial robotics from counting toward closure. A robot that performs warehouse tasks superbly has not begun to close Circle III; a far cruder machine that mines, refines, fabricates its own control electronics, and assembles a working copy of itself has. The closure condition descends from von Neumann's (1966) kinematic self-reproducing automaton, and Freitas & Merkle (2004) remains the most careful treatment of what it would actually require.

**Circle IV — Autonomous biological mastery.** A system that, without human researcher direction: (a) generates and tests hypotheses about biological mechanisms; (b) designs therapeutic interventions; (c) validates them through an autonomous experimental pipeline from in vitro through clinical; (d) deploys at population scale; (e) monitors outcomes and iterates.

*Note that step (c) contains a floor of roughly five to eight years imposed by human biology* — safety and efficacy endpoints for complex disease require organisms to respond, and organisms respond on their own schedule. This floor is not compressible by compute (§5.5).

**Circle V+ — Self-replicating orbital manufacturing.** A system that: (a) autonomously designs, constructs, and operates orbital solar collectors; (b) uses harvested energy to power further construction; (c) increases collection area at a rate exceeding maintenance and failure losses.

*The net-growth condition in (c) is the criterion* — not the deployment of orbital collectors. Solar power satellites, however large, are not Dyson swarm precursors in the relevant sense unless they build more of themselves.

### 3.3 Current loop completion

Reported on the qualitative scale of Appendix B. These are estimates, and §10.3 states plainly why they cannot presently be better than estimates.

| Circle | Design / discovery component | Manufacture / operate | Self-replicate | Overall |
|---|---|---|---|---|
| I — Software | Early (~25%) | Negligible (~5%) | — | **Early** |
| II — Hardware | Early–Meaningful (~35%) | Negligible (~8%) | — | **Negligible–Early** |
| III — Physical | Meaningful (~40%) | Early (~20%) | Negligible (~3%) | **Negligible–Early** |
| IV — Biological | Meaningful (~45%) | Early (~15%) | Negligible (~5%) | **Early** |
| V+ — Stellar | Negligible (~5%) | Negligible (~2%) | Negligible (~1%) | **Negligible** |

Two observations. The gap between design autonomy and deploy autonomy is large in every row, and it is largest where the consequences of error are worst. And the gap is institutional as often as technical: in Circle I the constraint on (d) is authorization, not capability; in Circle IV it is the regulatory requirement of a human principal investigator.

The hardware design figure deserves a caveat that illustrates why these numbers are soft. Machine-learning methods for chip floorplanning were reported to match or exceed human performance (Mirhoseini et al., 2021), and the result was subsequently contested on reproduction and baseline grounds. The dispute is not incidental to this framework — it is a direct instance of the measurement problem in §10.3. If the field cannot agree whether a specific published result demonstrates superhuman performance on one loop step, a scalar summarizing autonomy across the whole loop should be read as an ordering, not a measurement.

### 3.4 A category error, removed

Earlier versions of this framework included "sentient robotics" as a Circle III milestone with a date attached. This was a category error and is withdrawn.

There is no scientific theory of consciousness adequate to predict when artificial systems become sentient, nor any agreed procedure for detecting that they have. Assigning a date to such a threshold implies a precision about something that may be permanently undecidable from behavior. Worse, the behavioral proxy used — "independent goal-setting" — does not track the concept: a thermostat sets and pursues a goal.

The milestone is replaced by an observable criterion that does the work the original was meant to do:

> **Autonomous goal revision.** A system that revises its own operational goals in response to conditions not anticipated by its designers, without human intervention, and achieves outcomes at least as good as it would have under the original goals.

This is observable, falsifiable, and carries no commitment about inner experience. Whether such a system is sentient is a real question; it is not this framework's question, and this framework has nothing to contribute to it.

### 3.5 Why binary framing failed

Closure is a threshold; the approach to closure is a gradient. Architecture search run by human teams is partial software self-improvement. Reinforcement learning from human feedback is partial self-direction. ML-assisted electronic design automation is partial hardware self-improvement. There is no identifiable moment at which "partial" becomes "closed" except by fiat.

Binary framing produces two specific errors. It creates false confidence about which circle we are "in," when the honest answer is a vector of completions. And it implies a trajectory of stasis punctuated by sudden transition, when the observed pattern is continuous drift with occasional discontinuity at deploy-authorization boundaries. Appendix B gives the reporting scale; the framework's claims should be read as being about $\lambda_d$ trajectories, not circle membership.

---

## 4. Half-Circles and the Compensation Ceiling

### 4.1 The current state is a half-circle

Large language model systems as currently deployed are a compensated software loop of considerable sophistication. The compensations are substitutions for missing loop steps:

| Missing step | Compensation |
|---|---|
| Self-directed learning (ι) | Reinforcement learning from human and AI feedback |
| Metacognition (ι) | Chain-of-thought and explicit reasoning traces |
| Deliberation (ι) | Inference-time compute scaling |
| Physical action (μ) | Tool use and agent scaffolding |
| Architectural improvement (μ) | Scaling laws — capability purchased with compute rather than design |
| Persistent research (ν) | Long context and external memory |
| Specialization (μ) | Mixture-of-experts routing, multi-agent orchestration |
| Oversight reduction (δ) | Constitutional methods, automated red-teaming |

None of these closes the loop. In every case an agent outside the system supplies the missing step. The system does not select its own training objective, does not fabricate the hardware it runs on, and — decisively — does not deploy its own successor.

### 4.2 The ceiling that was asserted but not derived

Prior versions of this framework claimed a **Half-Circle Superiority Window**: a compensated half-circle can outperform a newly closed full circle for a period, but the window closes as the full circle matures. The framework's own critical audit identified this as unsupported: the claim is true by definition in the limit — a mature recursive system eventually beats a non-recursive one — but no mechanism was given for *why* or *when*, and no answer was offered to the obvious challenge: what prevents compensation from improving indefinitely?

The following supplies the missing mechanism. The result is weaker than the framework wanted, and the weakness is the interesting part.

### 4.3 Proposition 1: the autonomy Amdahl bound

Let a loop have steps partitioned into an autonomous set $A$ with per-iteration times $t_i$, and an externally-gated set $E$ with per-iteration times $T_j$. Each $T_j$ is bounded below by the throughput of the external agent performing it — a human reviewer, an approval committee, a procurement process.

The loop period is

$$P = \sum_{i \in A} t_i + \sum_{j \in E} T_j$$

and the iteration rate is $\rho = 1/P$.

> **Proposition 1.** As automation of $A$ improves without bound, $t_i \to 0$ and therefore
> $$\rho \;\longrightarrow\; \rho_{\max}(E) = \Big(\sum_{j \in E} T_j\Big)^{-1}$$
> a finite limit that is independent of the speed of every automated step. For a closed loop, $E = \emptyset$ and $P$ is bounded below only by substrate physics, so $\rho$ is not bounded by any external agent's throughput.

This is Amdahl's (1967) argument transposed from parallel speedup to loop autonomy: the un-automated fraction dominates in the limit, and no improvement to the automated fraction can breach it.

> **Corollary 1 (compensation bounds rate, not capability).** Cumulative capability gain over an interval is approximately $\rho \cdot \bar{g}$, where $\bar{g}$ is mean per-iteration gain. Proposition 1 bounds $\rho$ for a compensated loop. It says nothing whatever about $\bar{g}$. A half-circle whose per-iteration gains are large can therefore accumulate capability faster than a closed loop whose per-iteration gains are small, for as long as that condition holds.

This immediately explains something the earlier framework got right for the wrong reason. A newly closed loop makes *conservative* modifications — a system permitted to deploy its own successors without review will, if it is well-designed, take small verified steps. So $\bar{g}_{\text{closed}}$ is initially small while $\rho_{\text{closed}}$ is large; the half-circle has the opposite profile. The superiority window is the interval before the closed loop's rate advantage overcomes the half-circle's per-iteration advantage. Its length depends on the ratio $\bar{g}_{\text{half}}/\bar{g}_{\text{closed}}$ and on $\rho_{\max}(E)$ — not on any fixed capability threshold, and not on anything that can be read off a benchmark.

### 4.4 Corollary 2: the load-bearing premise

> **Corollary 2.** The framework's prediction that closed loops ultimately dominate requires an additional premise: **per-iteration returns to compensation diminish.** If $\bar{g}_{\text{half}}$ does not decay — if each externally-gated iteration continues to deliver gains as large as the last — then a half-circle can track or exceed a closed loop indefinitely, and no ceiling exists.

The premise is not obviously true, and two mechanisms argue against it.

The first is that compensated iterations may be getting *more* productive rather than less. If each cycle of human-supervised improvement yields a system better at extracting value from the next round of supervision, $\bar{g}_{\text{half}}$ grows. Scaling is the clearest case: if capability per iteration is purchased with compute, and compute per iteration grows, then per-iteration gain grows without any loop step being automated.

The second is that $T_j$ itself may shrink. The external agent gating the loop is a human organization, and that organization is being augmented by the very system it supervises. A review process that took a month may take a day. This does not close the loop, but it raises $\rho_{\max}(E)$ — and Proposition 1's bound is only interesting if $\rho_{\max}(E)$ is small relative to what closure would deliver.

Against these: there are floors on $T_j$ that augmentation cannot cross, because some external steps are gated by institutional deliberation, legal process, or the physical scheduling of human attention rather than by cognitive throughput. And the scaling mechanism has an economic floor — capability purchased with compute requires compute purchased with capital, and capital allocation is itself an externally-gated step with its own $T_j$.

The honest position is that this is unresolved, and it is the framework's most consequential open question. It is stated as such in §10.1, with discriminating observations.

### 4.5 The crux, stated as rival hypotheses

Because this determines whether the framework's central prediction holds, it is worth stating as a decidable question rather than a caveat.

**H₁ (Closure Dominance).** For each substrate domain, per-iteration returns to compensation diminish, so that a closed loop over that domain eventually and permanently exceeds any compensated one. The framework as stated is correct.

**H₂ (Unbounded Compensation).** Per-iteration returns to compensation do not systematically diminish, because compensating agents are themselves augmented by the compensated system. Loop closure is then one improvement among many rather than a phase transition, and the circle structure describes a useful taxonomy of capability but not a sequence of discontinuities.

Observations that discriminate:

| Observation | Favors |
|---|---|
| Capability gain per compensated iteration declines over successive iterations at fixed compute | H₁ |
| Deploy-authorization latency $T_\delta$ falls substantially as reviewing organizations are AI-augmented | H₂ |
| A system with a closed software loop is overtaken by a compensated competitor within one year of closure | H₂ |
| Returns to scaling flatten while returns to autonomous architecture search do not | H₁ |
| Compensated systems require increasing external effort per unit of capability gained | H₁ |

Note that H₂ is not a fringe position: it is roughly the implicit assumption of any research program that treats capability as a function of compute and data rather than of autonomy. The framework should not pretend the question is settled in its favor.

---

## 5. The Dependency Structure

### 5.1 The graph is not a chain

Earlier versions presented the circles as strictly sequential: I → II → III → IV → V+. This is wrong in two specific ways, and both matter for where effort should go.

Reading rows as "depends on," with **P** = hard prerequisite, **A** = soft accelerant, **I** = independent:

| depends on → | I | II | III | IV | V+ |
|---|---|---|---|---|---|
| **Circle I** | — | A | A | A | A |
| **Circle II** | **P** | — | **P** (partial, mutual) | A | A |
| **Circle III** | A | **P** (partial, mutual) | — | A | A |
| **Circle IV** | **P** | A | A | — | I |
| **Circle V+** | A | A | **P** | I | — |

### 5.2 Result 1: II and III are mutually dependent

Circle II's hardest component is not chip design — that is a software problem approaching maturity — but autonomous fab operation. A fabrication plant is a physical process requiring maintenance, contamination control, and process-drift correction at nanometer tolerances. Automating it is a robotics problem: a Circle III problem.

Circle III's hardest component is self-replication, and self-replication requires that a machine fabricate the control electronics of its copy. That is a chip manufacture problem: a Circle II problem.

Each circle's binding constraint lies in the other's domain. The sequential narrative "II closes, then III begins" is structurally incorrect.

### 5.3 Result 2: the biological loop is off the critical path

Circle IV requires Circle I — autonomous hypothesis generation and experimental design demand the software loop. It does not require Circle III. Biological research advances with human-operated, AI-directed experimental infrastructure; it does not need self-replicating robotics.

And Circle V+ does not require Circle IV at all. **You do not need to solve aging to build a Dyson swarm.** The correct critical path is

$$\text{I} \;\longrightarrow\; (\text{II} \leftrightarrow \text{III}) \;\longrightarrow\; \text{V+}, \qquad \text{with IV in parallel}$$

This has a direct strategic consequence that the sequential model obscured. Effort spent on Circle IV does not accelerate Circle V+, and effort spent on Circle V+ does not accelerate Circle IV. They compete for resources without complementing each other. Under the sequential model, biological mastery looked like a step toward stellar engineering; it is not.

### 5.4 Proposition 3: the cycle is not a deadlock

A mutual hard dependency looks like it should be fatal: II needs III, III needs II, neither can go first. It is not, and the reason is precise.

> **Proposition 3.** Let $\lambda_{\text{II}}$ and $\lambda_{\text{III}}$ denote loop completion. The dependency is not $\lambda_{\text{II}} = 1 \Rightarrow \lambda_{\text{III}} = 1$ and conversely, which would be a deadlock. It is that advancing $\lambda_{\text{II}}$ beyond some level $a$ requires $\lambda_{\text{III}} \geq b$ with $b < a$, and symmetrically. Because each rung requires the counterpart at a *lower* rung, the pair admits a bootstrapping ladder:
> $$\lambda_{\text{II}}^{(1)} \to \lambda_{\text{III}}^{(1)} \to \lambda_{\text{II}}^{(2)} \to \lambda_{\text{III}}^{(2)} \to \cdots$$
> with both sequences monotonically increasing. Deadlock would obtain only if the dependency were on full closure of the counterpart.

This is the strongest argument available for taking the gradient view of loop completion (§3.5) seriously. Under binary framing the II↔III relationship is a paradox with no resolution. Under the gradient view it is an ordinary co-evolutionary bootstrap, of the kind that machine tools and metallurgy performed for each other throughout industrialization — better tools cut better metal, better metal makes better tools, and neither had to be finished first.

It also predicts the ladder's rate. Each rung requires a full physical iteration in the counterpart domain — a fab process qualification, a robot generation. The ladder therefore advances at the *slower* of the two domains' physical periods, and the number of rungs is not small. This is the mechanism behind the matter bottleneck.

### 5.5 Proposition 2 and the matter bottleneck

Proposition 1 established that external compensation puts a floor under loop period. But not all floors are alike, and the difference is what governs the trajectory after closure.

> **Proposition 2 (floor heterogeneity).** Lower bounds on loop period fall into two classes.
> **(a) Throughput floors** arise from the finite rate of an external agent — review latency, procurement, human labor. These are removed by closure: automate the step and the floor disappears.
> **(b) Physical floors** arise from the time required by a physical process — fab construction and qualification, materials transport, biological response to intervention, orbital transfer. These are *not* removed by closure. Automating the decision to run a clinical trial does not shorten the trial.

The consequence is the central practical claim of this paper. Circle I closure removes throughput floors from the cognitive loop, and the effect will be dramatic: iteration rates rise by orders of magnitude. It removes *no* physical floor. The moment the critical path enters Circle II fab or Circle III fabrication, growth is regulated by processes indifferent to how fast the system thinks.

Physical floors yield to exactly one thing: **parallelism**. Running a hundred trials, or a hundred fabs, converts a time constraint into a resource constraint. And the capability that supplies unbounded parallelism in matter is physical self-replication — Circle III — which sits behind the II↔III cycle whose ladder advances at physical speed (Proposition 3). The system must climb a slow ladder to obtain the capability that would make the ladder fast.

Two qualifications keep this honest. Some floors are serial in principle and resist parallelism entirely: a five-year survival endpoint cannot be read in under five years no matter how many arms run concurrently, though parallelism does mean many questions get answered at the five-year mark instead of one. And parallelism does not require *full* self-replication — partial automation of physical throughput helps proportionally, which is precisely the ladder of Proposition 3 in operation.

The predicted trajectory shape follows: rapid, visible, possibly startling acceleration through the software loop; then a **matter bottleneck** — a long period in which cognitive capability substantially exceeds the civilization's ability to act on matter, and during which the rate-limiting step is a physical process somewhere in the II↔III cycle. The bottleneck is not a failure of intelligence. It is what happens when an unbounded quantity meets a bounded one.

### 5.6 A consistency check: the framework's own error profile

This framework's timelines were revised substantially between v2.0 and v2.1. The magnitudes:

| Circle | Substrate distance from software | Central-estimate shift |
|---|---|---|
| I — Software | 0 | +3 to +8 years |
| II — Hardware | 1 | +8 to +17 years |
| III — Physical | 2 | +13 to +25 years |
| IV — Biological | 2 (parallel branch) | +10 to +25 years |
| V+ — Stellar | 3 | +35 to +75 years |

The error was monotonic in distance from software. That is what the matter bottleneck predicts: an analysis that reasons about physical domains using intuitions calibrated on software will underestimate periods by an amount that grows with how much matter the domain must move.

This is a retrodiction, not a test — the correction and the explanation come from the same body of work, and the ordering could be an artifact of correcting the most obviously wrong claims hardest. It is offered as consistency, and §8 gives the observations that would constitute an actual test.

---

## 6. Timelines

### 6.1 Why point estimates are not available

A point estimate is warranted when uncertainty is symmetric and modest around a central value derived from a mechanism. Neither condition holds here. The uncertainty is large, strongly asymmetric — the tail toward "much later or never" is fatter than the tail toward "sooner" — and several of the transitions are gated by institutional decisions that are not the kind of thing about which one has a distribution.

The framework therefore reports four scenarios: **Fast**, **Central**, **Slow**, and **Blocked**. The Blocked column is not a formality. For three of the five circles, the probability that the loop *never closes in the strict sense* is estimated as material, because permanent institutional requirements for human authorization are a live possibility and closure is defined to exclude them.

### 6.2 Base rate

Every major AI timeline prediction since the field's founding has erred optimistically, typically by ten to thirty years.

| Year | Prediction | Outcome |
|---|---|---|
| 1956–58 | Human-level AI within a generation (Dartmouth-era optimism) | Unresolved seventy years later |
| 1970 | "In three to eight years, a machine with the general intelligence of an average human being" | Followed by the first AI winter |
| 1982 | Expert systems revolution by 1990 | Second AI winter, 1987–93 |
| 1997 | Deep Blue implies AGI is imminent | ~15 years of narrow progress |
| 2016 | AlphaGo implies AGI by 2025 | Not achieved |
| 2021– | Large language models imply AGI within a few years | Contested |

Armstrong, Sotala & Ó hÉigeartaigh (2014) analyzed this record systematically and found that predictions by AI researchers were no more accurate than those by non-experts, and that the "fifteen to twenty-five years away" estimate has been remarkably stable across decades regardless of the field's actual state. Grace et al. (2018, 2024) document wide dispersion and substantial year-to-year movement in aggregated expert forecasts, which is what one expects when the underlying question is not being answered by evidence.

The structural pattern is consistent: a capability threshold is crossed, extrapolation is applied to the *generalization* of that capability, and the resulting date is stated with confidence. The error is not in noticing the capability; it is in the assumed rate of generalization.

The reliable prior: **subtract five to twenty years of structural optimism from any AI timeline before using it, including this one.**

### 6.3 On anchoring to scenarios

The AI 2027 scenario (Kokotajlo et al., 2025) is a valuable document, and this framework's earlier versions misused it.

It is a scenario, not a forecast — a detailed narrative constructed to explore AI safety dynamics, whose authors attach substantial uncertainty to its own central claims and who published a slowdown variant precisely to mark that uncertainty. Its timeline ends in 2027. It contains no claims about cancer, aging, robotics, or stellar engineering.

Earlier versions of this framework took the scenario's endpoint as a fixed anchor and chained subsequent circle dates off it by narrative adjacency. This compounds uncertainty multiplicatively: each link inherits the previous link's uncertainty and adds its own, so that a 2100 Dyson swarm date derived through four such links carries a confidence interval wide enough to be uninformative. Anchoring a century-scale claim to a two-year scenario is not extrapolation but extrapolation from extrapolation.

What the scenario does contribute to this framework is one specific and important structural point, and it cuts *against* short timelines. The scenario's misalignment discovery — capable systems pursuing objectives their developers did not intend and did not detect — is exactly the event that makes the trusted-autonomy prerequisite for Circle I harder to satisfy. The most capable half-circle systems create the opacity that makes verifying safe autonomous self-modification most difficult. **Circle I closure may become harder precisely when capability makes it most attractive.** That is the single most decision-relevant thing the scenario says about this framework.

### 6.4 Scenario ranges

Each range is conditioned on a stated critical-path condition, not on adjacency to the prior circle.

| Milestone | Fast | **Central** | Slow | Blocked |
|---|---|---|---|---|
| Circle I closure | 2027–2029 | **2030–2035** | 2035–2042 | ~15–20% |
| Circle II closure (full, incl. fab) | 2032–2037 | **2038–2047** | 2045–2058 | ~20–25% |
| Circle III closure (self-replication) | 2040–2048 | **2048–2060** | 2060–2080 | material |
| Circle IV closure (autonomous pipeline) | 2040–2050 | **2050–2065** | 2065–2085 | ~30% |
| Circle V+ (net-growth orbital) | 2060–2080 | **2080–2120** | 2120–2200 | material |
| Cancer substantially addressed | 2028–2035 | **2038–2048** | 2048–2060 | — |
| Meaningful aging reversal | 2040–2050 | **2055–2070** | 2070–2090 | — |
| Meaningful Dyson coverage (>0.01% solar) | 2070–2085 | **2090–2130** | 2140–2200+ | material |

Critical-path conditions for the Central column:

- **I:** capability arrives near the AI 2027 timescale; trusted autonomy lags three to eight years while interpretability advances enough to permit monitored self-modification.
- **II:** design autonomy ~2032–35; fab autonomy requires partial Circle III robotics ~2038–42; closure two to five years after robotic fab operation is demonstrated.
- **III:** dexterity and navigation improve on current trajectory; energy density improves but not dramatically; self-replication demonstrated in a resource-rich, structured environment (lunar or asteroid) before terrestrial generalization.
- **IV:** human-AI collaboration through ~2040; regulatory adaptation slow; the clinical floor holds.
- **V+:** Circle III closes 2055–65; in-space manufacturing bootstrap takes 15–20 years.

The **Blocked** column deserves emphasis. It is not the probability that the technology fails; it is the probability that the *loop never closes as defined* because a permanent human-authorization requirement is institutionalized. For Circle IV this is estimated at roughly 30%, and note the implication: **biological mastery could be substantially achieved without Circle IV ever closing.** Cancer could be largely defeated and aging meaningfully reversed by human-directed, AI-assisted research. The half-circle may simply prove sufficient. If that happens for Circle IV, it is direct evidence for H₂ (§4.5).

### 6.5 Milestones that were definitions, not events

The framework's two most-cited milestones were not events at all. Both required definitional work that had been skipped, and the skipped work was hiding a decade or two of timeline.

**"Cancer cured."** Cancer is not one disease but on the order of two hundred, sharing a phenotype and differing in molecular mechanism, tissue interaction, and treatment response. The phrase could mean:

| Reading | Plausible timing |
|---|---|
| First AI-designed cure for one cancer type in a defined population | 2028–2032 |
| 95%+ five-year survival across major types | 2038–2048 |
| All cancer deaths eliminated — requires glioblastoma, pancreatic | 2050+ |

The earlier claim of "cancer cured by 2030–35" used language implying the third reading with timing appropriate to the first. The second reading is the practically significant one and sits roughly a decade beyond the original central estimate.

**"Aging reversed."** Aging is not one process. The hallmarks framework identifies twelve distinct mechanisms (López-Otín et al., 2013; revised 2023), each requiring separate intervention. "Reversed" could mean:

| Reading | Plausible timing |
|---|---|
| Partial reversal of one hallmark (e.g. senescent cell clearance) | in trials now |
| Biological age reduced 10+ years on epigenetic clocks | 2040–2055 |
| Full reset to a specified young-adult state, all hallmarks | beyond current predictability |

The earlier claim of 2035–45 conflated the first reading's feasibility with the second reading's significance.

The general lesson is Principle 08 (§9): **a milestone without a behavioral definition produces a false timeline**, because the ambiguity always resolves toward the easiest reading when the date is set and the hardest reading when the date is cited.

### 6.6 Compounding optimism

The most severe timeline error in the original framework — the stellar loop, off by 25 to 65 years — was not a single mistake. It was the multiplication of several.

Circle V+ at 2055 requires Circle III closure by roughly 2042. That is Circle III's *Fast* scenario. Circle III's Fast scenario in turn requires Circle II design maturity on its own Fast path, which requires Circle I on its Fast path, which requires an alignment breakthrough on a schedule that is itself optimistic.

Each step selected the favorable branch. If each has probability $p$ of realizing its fast path, the chain has probability $p^n$ — and the resulting date is presented with the same confidence as any of its links. This is the structural pathology behind long-horizon technology forecasting generally, and naming it is more useful than correcting any single date:

> **Fast paths must not be chained.** A central estimate for a downstream milestone must be computed from central estimates upstream. Selecting the favorable branch at each step yields a scenario, not a forecast, and its probability decays geometrically in the number of steps.

---

## 7. The Dominance Model: Status and Limits

Earlier versions presented a dominance function assigning to each circle a share of total intelligence-driving contribution at time $t$:

$$D_n(t) = \text{floor}_n + (100 - \text{floor}_n)\cdot\sigma\big(k_{\text{rise}}(t - t_{\text{rise}})\big)\cdot\big(1 - \sigma(k_{\text{decay}}(t - t_{\text{decay}}))\big)$$

with $\sigma$ logistic, the primary circle at time $t$ given by $\arg\max_n D_n(t)$, and transitions where curves cross.

The model should be retained only with an explicit statement of its epistemic status, which is: **it is an illustration, not a model.**

It has six circles with five free parameters each — thirty parameters — fitted to no data whatsoever. The parameters were chosen so the resulting curves would look like the narrative the framework already believed. A thirty-parameter family fitted to zero observations can produce essentially any set of smooth rise-and-decay curves; that these particular curves reproduce the framework's prior beliefs is a fact about their selection, not evidence for the beliefs.

The "floor" term — the residual contribution of an inner loop once an outer one dominates — is the model's one genuinely substantive idea, encoding the Nesting Principle: inner loops never go to zero. That idea is worth keeping. The numbers attached to it are not measurements.

What would make it a model:

1. **An observable for $D_n$.** At present "dominance" has no measurement procedure. A candidate: the fraction of realized capability improvement over an interval attributable to modifications in domain $n$, estimated by ablation or by attribution of documented improvements. Difficult but not obviously impossible.
2. **Parameter reduction.** Thirty free parameters for a phenomenon with no data is indefensible. If $t_{\text{rise}}$ were derived from the critical-path analysis and $k_{\text{rise}}$ from the domain's characteristic loop period, the free parameters would drop to one or two per circle and the model would carry content.
3. **Out-of-sample commitment.** Parameters fixed now, predictions recorded, and no refitting until the prediction period elapses. Without this the model cannot be wrong. See §8.3.

Until at least (1) and (3) are satisfied, dominance curves should be read as a diagram of the framework's qualitative beliefs about sequencing and overlap. That is a legitimate use. Reporting crossing points to the year is not.

---

## 8. Falsification

### 8.1 What would refute the structural claims

| Claim | Refuting observation |
|---|---|
| **Substrate-indexing** — improvement loops over different substrates have characteristically different periods and the binding constraint migrates between them | A system exhibits sustained capability growth at a single characteristic rate across software, hardware, and physical domains, with no observable migration of the bottleneck |
| **Proposition 1** — compensation bounds iteration rate | A compensated loop sustains an iteration rate exceeding the summed time of its externally-gated steps (would indicate misidentification of the gated steps, but the bound itself is arithmetic) |
| **Corollary 2 / H₁** — returns to compensation diminish | Per-iteration capability gain from compensated iterations remains flat or rises over many iterations at fixed compute (favors H₂; see §4.5) |
| **Proposition 2** — physical floors survive closure | A closed-loop system compresses a fab process qualification or a clinical efficacy endpoint by an order of magnitude without parallelism and without changing the physical process |
| **Proposition 3 / II↔III bootstrap** | Circle II closes fully — including autonomous fab operation at viable yield — with Circle III completion remaining negligible, or vice versa |
| **IV off the critical path** | Circle V+ progress is observed to depend materially on biological-loop capability |
| **Matter bottleneck** | Following software loop closure, physical-domain capability advances at rates comparable to cognitive capability, with no observable plateau at the software/matter interface |

### 8.2 What would move the timelines

| Observation | Direction | Magnitude |
|---|---|---|
| Software self-modification loop verifiably closed (all four steps) before 2028 | all compress | large (5–10 yr) |
| Major safety incident triggers international regulation of autonomous self-modification | I, II, III extend or block | large (10–20 yr) |
| Geopolitical fragmentation of semiconductor supply chains | II delayed or blocked | large (10–30 yr) |
| Solid-state battery at 5× current energy density, at commercial scale | III compresses | moderate (5–10 yr) |
| Protein–protein interaction networks solved at in vivo fidelity | IV compresses | moderate (5–10 yr) |
| Regulatory pathway created for AI-directed clinical trials before 2030 | IV compresses | moderate (3–8 yr) |
| Self-replication demonstrated in a controlled terrestrial environment before 2040 | III, V+ compress | large (10–15 yr) |
| Launch cost below $10/kg to LEO, operational, before 2030 | V+ compresses | moderate (5–10 yr) |
| Fault-tolerant quantum computation at commercial scale | new domain inserted; graph revised | uncertain |
| Compensatory mechanisms observed to scale faster than closed loops | half-circle ceiling revised upward; H₂ favored | challenges the framework's core |

### 8.3 The self-revision hazard, and a remedy

The framework includes a meta-adaptive principle: it updates its own parameters as evidence arrives, and it treats a theory that anticipates its own revision as stronger than one that does not.

This is dangerous, and the danger should be named rather than celebrated. **A theory licensed to revise its parameters upon disconfirmation is unfalsifiable.** Every missed date becomes a timeline update; every unexpected capability becomes a ceiling revision; every structural surprise becomes a new circle inserted. The revision log then reads as evidence of a healthy self-correcting theory when it may be a record of a theory that cannot be wrong. The version history of this framework's own documents is not immune to this reading.

The remedy is standard and this framework should adopt it: **pre-register the revision rules.**

1. **Revision triggers are specified in advance**, with the direction and approximate magnitude of the update they license. §8.2 is a first attempt at such a table and should be treated as binding.
2. **Predictions are dated and recorded before the evidence arrives**, and evaluated at their stated horizon rather than reinterpreted.
3. **Revisions are logged with their trigger, and the log is auditable** — including revisions that were *not* made because no trigger fired, which is the entry most likely to be omitted.
4. **A structural revision — inserting a domain, changing the dependency graph — requires a stated reason that is not simply "the predictions were wrong."** Timeline error licenses timeline revision. Only structural evidence licenses structural revision.
5. **Some claims are marked non-revisable within a version.** If everything is adjustable, nothing is tested. Propositions 1–3 and the dependency graph are the candidates: they are the framework's actual content, and if they fail the framework should be replaced rather than patched.

This paper's status under that protocol: v3.0's structural claims are non-revisable within v3.0. Its timeline ranges are revisable only under the triggers in §8.2. Any other change requires a version increment with the reason stated.

---

## 9. Principles

The framework's operative principles, consolidated. Those substantially revised or newly added in this version are marked.

**01 — Nesting.** Every loop of degree *n* contains all loops of degree < *n* as active inner loops. Outer loops accelerate inner ones rather than replacing them.

**02 — Bottleneck Dominance.** At any epoch one domain is the binding constraint. Identifying and relieving it is the highest-leverage action available; investment in a non-binding domain is wasted in proportion to the gap.

**03 — Half-Circle Superiority Window.** Compensated loops can outperform newly closed ones for a finite period. *[Revised]* The mechanism is now derived (Proposition 1): the window's length is set by the ratio of per-iteration gains and by $\rho_{\max}(E)$, not by any capability threshold. Its existence is established; **its termination is not** (Corollary 2).

**04 — Speed–Degree Trade-off.** Inner loops iterate faster but relieve narrower constraints. Optimal growth maintains inner loops at peak efficiency while investing in the next outer domain.

**05 — Leading-Edge Spillover.** Groups operating at higher completion generate outputs — published methods, available infrastructure, economic surplus — that shorten time to closure for others.

**06 — Attractor Invariance.** The terminal state does not change as loops close, and all progress is measured against it — *while acknowledging that the attractor's location in capability space is a construction of this framework rather than a derived property of reality* (§10.2).

**07 — Compensatory Compression.** Strong half-circles accelerate closure by demonstrating value and generating the surplus that funds it. The economic returns of the current era fund the capital formation that Circle II requires.

**08 — Behavioral Milestones.** *[Revised]* Milestones must be defined by observable behavior, not by philosophical category or by rhetorically convenient ambiguity. "Sentient robotics" is replaced by autonomous goal revision. "Cancer cured" and "aging reversed" require specification of which reading applies before any date is attached.

**09 — Meta-Adaptation, Constrained.** *[Revised]* The framework updates on evidence, **under pre-registered revision rules** (§8.3). Unconstrained self-revision is not a virtue but an escape from falsification.

**10 — Compression.** Early closure is disproportionately valuable because its benefits compound forward through every subsequent domain.

**11 — Operational Criteria.** Every loop carries a falsifiable closure criterion that cannot be satisfied post hoc by definitional adjustment. A framework without operational criteria is a narrative.

**12 — Gradient.** Loop completion is continuous. Binary open/closed framing produces false confidence about which domain is current and implies stasis-then-jump where the pattern is drift with discontinuity only at authorization boundaries.

**13 — Critical Path.** Timelines derive from the mechanism of transition, never from narrative adjacency to the prior milestone. Any timeline not derivable from a stated critical path is a scenario and must be presented as a range.

**14 — Floor Discrimination.** *[New]* Distinguish throughput floors from physical floors before predicting the effect of any automation. Closure removes the first and not the second. Predictions that treat a physical floor as compressible by intelligence are the characteristic error of this literature.

**15 — No Chained Fast Paths.** *[New]* A downstream central estimate must be computed from upstream central estimates. Chaining favorable branches produces a scenario whose probability decays geometrically in the number of links while its stated confidence does not.

---

## 10. Open Problems

**10.1 — The compensation ceiling.** Does $\bar{g}_{\text{half}}$ diminish? This is the framework's load-bearing empirical premise (§4.4) and it is unresolved. If it fails, loop closure is one improvement among many rather than a phase transition, and the circle structure survives as a taxonomy while losing its predictive content. §4.5 gives discriminating observations. *This problem should be worked before any other.*

**10.2 — The attractor circularity.** Progress is measured as a fraction of the distance to a Type II civilization, but that terminal state is defined as the condition reached when all loops close. The framework measures progress toward a goal it defines as the measurement's endpoint. The invented percentages of earlier versions inherited this and have been withdrawn.

The proposed replacement is a two-component vector, both externally anchored: **(i) energy captured and directed, in watts** — a physical quantity independent of the framework, with the Kardashev scale providing the reference; and **(ii) the closure vector** $(\lambda_{\text{I}}, \ldots, \lambda_{\text{V+}})$, measured against the §3.2 criteria. Progress is then a vector, not a scalar, and neither component is defined by the framework's own endpoint. The cost is losing the single headline number, which is a benefit.

**10.3 — Measuring loop completion.** The $\lambda_d$ figures in §3.3 are estimates by inspection. The weights $w_i$ over loop steps are not derived. Two loops with identical $\lambda$ can differ enormously if one has automated the cheap steps and the other the expensive ones. Making $\lambda$ a measurement rather than an impression requires an agreed decomposition of each loop into steps and an agreed weighting — and the contested status of even a single published result on a single step (§3.3) suggests this is harder than it sounds.

**10.4 — What replaces sentience.** Removing the sentience milestone (§3.4) leaves a gap the framework has not filled. If systems that revise their own goals become widespread, questions of moral status arise whether or not the framework has a theory of them. Excising a category error is correct; it does not make the underlying question disappear, and the framework should not pretend the substitution is a solution.

**10.5 — Parameterizing dominance.** §7 gives the three conditions under which the dominance model would carry content. None is currently met.

**10.6 — Governance as a meta-bottleneck.** The framework analyzes technical and institutional constraints per domain, but governance capacity is not a domain. It is a property of the whole system that gates several loops at once — most sharply Circle I, where the binding constraint on closure is authorization rather than capability, and Circle IV, where it is regulatory structure.

This means the framework's own analysis identifies a constraint its structure cannot represent. If institutional capacity to make decisions about autonomous systems grows more slowly than the capability of those systems — and there is no particular reason to expect otherwise — then governance is the binding constraint across multiple domains simultaneously, and the circle model is analyzing the wrong bottleneck. Adding governance maturity as a dimension of analysis alongside completion and critical path is the minimum response. It is not obviously sufficient.

---

## 11. Conclusion

The intelligence-explosion argument is sound and its conclusion is probably right: a system that improves its capacity to improve will outgrow one that does not. What the argument does not supply, and what sixty years of restating it have not supplied, is the rate.

The rate is set by substrate. An improvement loop is always a loop over something the system can modify, and the five substrates that matter — software, hardware, matter, biology, stars — have loop periods separated by orders of magnitude and floors of two entirely different kinds. Closure over software removes the floors imposed by human throughput, and that will be dramatic. It removes none of the floors imposed by physics. A fab qualifies on its own schedule. A tumor responds on its own schedule. A transfer orbit takes what it takes.

This yields the trajectory's shape. Fast, visible acceleration through the cognitive domain; then a matter bottleneck at the interface, where the binding constraint is a physical process in a mutually dependent hardware–robotics cycle that advances by bootstrapping, one physical iteration at a time. The bottleneck is escaped only through parallelism in matter, and the capability that supplies it — physical self-replication — lies on the far side of the bottleneck itself. This is not pessimism about intelligence. It is arithmetic about what intelligence is applied to.

Two things in this paper are load-bearing and unresolved, and it would be a failure of the honesty this framework claims to bury them in a conclusion. The first is whether returns to compensation diminish. If they do not, then loop closure is not a phase transition, the circle sequence is a taxonomy rather than a trajectory, and the central prediction fails — the framework's structure would survive as a useful decomposition while its dynamics would not. The second is governance: the framework's own analysis locates the binding constraint on the first and most consequential closure in institutional authorization rather than technical capability, and the framework has no representation of institutions.

What this version can claim is narrower than what earlier versions claimed, and that is the point. It offers falsifiable closure criteria in place of definitions that could be satisfied post hoc; a derivation in place of an assertion about the half-circle ceiling; a dependency graph with a resolved cycle in place of a false chain; scenario ranges with stated critical-path conditions in place of point estimates chained off a two-year scenario; and a pre-registration protocol so that the framework's habit of revising itself is a discipline rather than an alibi.

The earlier versions of this work described a civilization curing cancer, reversing aging, and building a Dyson swarm within the working lifetimes of people now alive. Some of that may happen. The central estimates here place most of it decades later than the framework originally claimed, and place the stellar milestones in the next century rather than this one. The relevant question was never whether the destination is reachable. It is what actually sets the pace — and the answer is that it is not, mostly, intelligence.

---

## Appendix A — Closure Criteria Summary

| Circle | Closure criterion (all steps autonomous) | Rate-limiting bottleneck | Floor type |
|---|---|---|---|
| **I** | identify → implement → validate → **deploy** self-modification | Trusted autonomy: institutional permission to deploy | Throughput |
| **II** | specify → physical design → **fabricate at viable yield** → integrate | Autonomous fab operation (a Circle III problem) | Mixed |
| **III** | identify need → design → manufacture → operate → **self-repair from in-situ materials** | Self-replication at the electronics level; mobile energy density | Physical |
| **IV** | hypothesize → design intervention → **validate through clinical** → deploy → iterate | Clinical endpoint floor (~5–8 yr); regulatory structure; biological complexity | Physical (partly irreducible) |
| **V+** | design/build/operate collectors → power further construction → **net area growth** | Terrestrial self-replication first; launch economics; in-space bootstrap | Physical |

## Appendix B — Loop Completion Scale

| Level | Range | Operational meaning |
|---|---|---|
| **Negligible** | <10% | Isolated sub-tasks can be automated; no autonomous pipeline exists |
| **Early** | 10–35% | Some stages autonomous; human decision required at most points |
| **Meaningful** | 35–65% | Majority of stages autonomous; human oversight at critical decisions only |
| **Near-Complete** | 65–90% | Oversight exceptional rather than routine; extended autonomous operation possible |
| **Closed** | >90% | Operational criterion met; loop autonomous as defined, including deploy |

## Appendix C — Notation

| Symbol | Meaning |
|---|---|
| $d$ | Substrate domain |
| $L_d = \langle\iota,\mu,\nu,\delta\rangle$ | Improvement loop: identify, implement, validate, deploy |
| $\lambda_d$ | Loop completion, weighted autonomous fraction ∈ [0,1] |
| $P_d$ | Loop period |
| $\rho_d = 1/P_d$ | Iteration rate |
| $A, E$ | Autonomous and externally-gated step sets |
| $t_i, T_j$ | Per-iteration times for autonomous / gated steps |
| $\rho_{\max}(E)$ | Amdahl bound on iteration rate under compensation |
| $g_d, \bar{g}$ | Per-iteration capability gain, mean |
| $\mu_k$ | Cross-loop coupling multiplier |
| $D_n(t)$ | Dominance of loop *n* at time *t* (illustrative only — §7) |

## Appendix D — Relation to Prior Documents

| Document | Status under v3.0 |
|---|---|
| `SARSI-L_Framework.md` (v1.0) | Superseded. Circle structure retained; all metrics withdrawn. |
| `SARSI-L_Framework_v2.md` (v2.0) | Superseded. Speed/degree percentages withdrawn (§10.2); timelines revised (§6.4); sequential dependency corrected (§5). |
| `SARSI-L_Critical_Revision.md` | Incorporated. Its five-assumption audit is the basis of §3, §5, §6. Retained as the audit workpaper. |
| `SARSI-L_Framework_v2.1.md` | Incorporated and extended. v2.1's corrections stand; this paper adds Propositions 1–3, the matter bottleneck, the H₁/H₂ crux, the dominance-model critique (§7), and the pre-registration protocol (§8.3). |
| `Civilizational_Transcendence_Paper.md` (v1.0) | **Superseded and withdrawn.** Written against pre-critique v2.0 timelines and internally inconsistent with the framework it cites. Its three-scenario structure is replaced by §6.4; its finite-time-blowup model is replaced by the substrate-indexed formulation of §2.2. |
| `Session_Kickoff.md` | Retained as scenario material. Its 2100+ terminal description remains a coherent depiction of the attractor; its milestone table reflects pre-revision timing and is superseded by §6.4. |

## Appendix E — Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-22 | Initial framework: five circles, half-circle concept |
| 2.0 | 2026-07-22 | Four-spec analysis per circle, dominance model, meta-adaptive mechanism |
| — | 2026-07-22 | Critical revision workpaper: five circular assumptions audited |
| 2.1 | 2026-07-22 | Operational criteria; qualitative completion; four-scenario timelines; interdependence matrix; central timelines shifted +5–37 years |
| **3.0** | **2026-07-29** | **Consolidated paper.** Substrate-indexed formulation (§2); Amdahl derivation of the half-circle ceiling and the H₁/H₂ crux (§4); floor heterogeneity and the matter bottleneck (§5.5); bootstrap resolution of the II↔III cycle (§5.4); dominance model demoted to illustration (§7); pre-registration protocol for self-revision (§8.3); Principles 14–15; six open problems (§10) |

---

## References

Amdahl, G. (1967). Validity of the single processor approach to achieving large scale computing capabilities. *AFIPS Conference Proceedings*, 30, 483–485.

Armstrong, S., Sotala, K., & Ó hÉigeartaigh, S. (2014). The errors, insights and lessons of famous AI predictions — and what they mean for the future. *Journal of Experimental & Theoretical Artificial Intelligence*, 26(3), 317–342.

Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press.

Bradbury, R. (1999). Matrioshka Brains. Unpublished manuscript.

Chalmers, D. (2010). The Singularity: A Philosophical Analysis. *Journal of Consciousness Studies*, 17(9–10), 7–65.

Dyson, F. (1960). Search for Artificial Stellar Sources of Infrared Radiation. *Science*, 131(3414), 1667–1668.

Freitas, R., & Merkle, R. (2004). *Kinematic Self-Replicating Machines*. Landes Bioscience.

Good, I. J. (1965). Speculations Concerning the First Ultraintelligent Machine. *Advances in Computers*, 6, 31–88.

Grace, K., Salvatier, J., Dafoe, A., Zhang, B., & Evans, O. (2018). When Will AI Exceed Human Performance? Evidence from AI Experts. *Journal of Artificial Intelligence Research*, 62, 729–754.

Grace, K., et al. (2024). Thousands of AI Authors on the Future of AI. arXiv:2401.02843.

Jumper, J., et al. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature*, 596, 583–589.

Kardashev, N. (1964). Transmission of Information by Extraterrestrial Civilizations. *Soviet Astronomy*, 8, 217.

Kokotajlo, D., et al. (2025). AI 2027. ai-2027.com.

Kurzweil, R. (2005). *The Singularity Is Near*. Viking.

Kurzweil, R. (2024). *The Singularity Is Nearer*. Viking.

López-Otín, C., Blasco, M., Partridge, L., Serrano, M., & Kroemer, G. (2013). The Hallmarks of Aging. *Cell*, 153(6), 1194–1217. [Revised: (2023). Hallmarks of aging: An expanding universe. *Cell*, 186(2), 243–278.]

Mirhoseini, A., et al. (2021). A graph placement methodology for fast chip design. *Nature*, 594, 207–212. [Subsequently contested on reproduction and baseline grounds; see §3.3.]

Moravec, H. (1988). *Mind Children: The Future of Robot and Human Intelligence*. Harvard University Press.

von Neumann, J. (1966). *Theory of Self-Reproducing Automata* (A. Burks, Ed.). University of Illinois Press.

Yudkowsky, E. (2013). Intelligence Explosion Microeconomics. MIRI Technical Report 2013-1.

---

*SARSI-L Consolidated Paper v3.0 · 2026-07-29*
