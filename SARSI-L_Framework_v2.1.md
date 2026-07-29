# SARSI-L: Self-Aware Recursively Self-Improving Intelligence Levels
## Framework v2.1 — Critical Revision

*Document version: 2.1 — 2026-07-22*
*Supersedes: SARSI-L_Framework_v2.md*
*References: SARSI-L_Critical_Revision.md (audit workpaper), SARSI-L_Framework_v2.md (prior version)*
*Interactive: https://claude.ai/code/artifact/2169dd14-8c49-4a99-808c-11ff5894dd9a*

---

## Abstract

SARSI-L maps the progression of recursive self-improvement from current LLM capabilities to Kardashev Type II civilization (Dyson swarm). The framework defines five nested circles, each representing a substrate domain whose autonomous recursive loop, when closed, multiplies the effective self-improvement rate accessible to the system.

This v2.1 revision identifies and corrects five structural problems in v2.0: (1) loop closure had no operational definition, (2) speed/degree percentage metrics were invented, (3) timelines were anchored to a scenario document rather than derived from mechanism, (4) mutually dependent circles were presented as sequential, and (5) "sentient robotics" was a category error. Each problem is corrected in-place. The result is a more honest, more falsifiable, and more useful framework.

---

## § I — Critical Preface: What Changed and Why

The original SARSI-L circle structure survives this revision. The progression from software loops to hardware, physical, biological, and stellar domains captures something real about how recursive self-improvement compounds across substrate domains. What does not survive scrutiny is the operationalization.

### Five Problems Corrected

**Problem 1: "Loop closure" had no operational definition.**
The v2.0 framework classified systems as "open" or "closed" without specifying what behavior constitutes closure. This allowed any sufficiently capable system to be classified post-hoc. A falsifiable criterion now specifies exactly what behavior constitutes closure for each circle.

**Problem 2: Speed/degree percentages were invented.**
The figures 8%, 22%, 45%, 62%, 89% had no derivation — they were plausible-looking numbers. They have been replaced with qualitative loop-completion estimates (Negligible / Early / Meaningful / Near-Complete / Closed) and honest acknowledgment that quantitative precision is not currently achievable.

**Problem 3: Timelines were anchored to a scenario, not a mechanism.**
AI 2027 is a thought experiment exploring AI safety dynamics, not a forecast. Its authors assign large uncertainty to the 2027 ASI claim itself. Every date derived from AI 2027 carries the same epistemic weight as the scenario's own uncertainty — which is very large. Using it as an anchor for a 2100 Dyson swarm timeline compounds uncertainty multiplicatively. Four-scenario ranges (Fast / Central / Slow / Blocked) replace point estimates; each scenario's timeline is derived from explicit critical-path conditions.

**Problem 4: Mutually dependent circles were presented as sequential.**
Circle II (hardware autonomy) and Circle III (physical self-replication) are coupled: fab autonomy requires robotic physical operation (Circle III problem), while robotic hardware requires chip design (Circle II problem). They must co-evolve, not sequence. Additionally, Circle IV (biological mastery) is largely independent of Circle III — not downstream from it. Biological research advances with human-operated, AI-directed infrastructure.

**Problem 5: "Sentient Robotics" is a category error.**
We have no scientific theory of consciousness adequate to predict when artificial systems become sentient. Replacing this with a behavioral proxy: *autonomous goal revision under conditions unanticipated by designers* — observable, behaviorally defined, not conflated with consciousness.

---

## § II — Circular Assumption Audit

Five circular assumptions in v2.0 are named, analyzed, and corrected or flagged.

---

### Assumption 1 — The Attractor Circularity

**Claim:** Speed and degree are measured as percentage of progress toward Type II civilization.

**Problem:** The Type II attractor is defined as the state reached after all circles close. Measuring progress as a percentage toward Type II requires knowing where Type II is in capability space. The attractor's location is defined by the framework as its own endpoint. The framework measures progress toward a goal it defines as the endpoint of the measurement. The percentage figures (8%, 22%, 45%...) carry no derivation.

**Correction:** Replace percentage-of-attractor with qualitative capability shifts — what specific things can a system do at each circle that it cannot do at the prior circle? Capability descriptions are falsifiable; percentage-of-attractor is not.

---

### Assumption 2 — The Self-Awareness Prerequisite

**Claim:** Circle I requires self-awareness / Circle I = Self-Aware LLM.

**Problem:** The prerequisite and the definition are the same claim stated twice. "Self-awareness" is used as though its threshold is obvious — when it is one of the central unsolved problems in philosophy of mind. Current LLMs produce language about their own reasoning, which looks like metacognition from outside. Whether this constitutes genuine metacognition or merely the statistical pattern of metacognitive language is not distinguishable from behavioral output alone.

**Correction:** Define Circle I by a behavioral criterion: a system that — without human approval at any step — (a) identifies a self-modification likely to improve performance, (b) implements it, (c) validates improvement on held-out benchmarks, (d) deploys the modified system as baseline. "Self-awareness" is not a prerequisite; this behavioral sequence is.

---

### Assumption 3 — The Timeline Chain

**Claim:** 2027 → 2030 → 2035 → ... is derived from one circle opening the next.

**Problem:** Each circle's opening date in v2.0 is partly derived from the previous circle's date with an implicit assumption that transitions are fast. The 3-year gap between Circle I and Circle II assumes hardware development immediately follows software loop closure. But chip design and chip manufacture are separated by 5–10 years of physical construction and process development even when designs are ready. The mechanism bridging this gap is never specified.

**Correction:** Each circle specifies a critical path — the actual physical and institutional steps required to close the loop — and timelines derive from that path. Four scenarios replace the single date.

---

### Assumption 4 — The Superiority Window Mechanism

**Claim:** The half-circle superiority window closes as the full circle matures.

**Problem:** This is true by definition (eventually a mature recursive system outperforms a non-recursive one), not by any specific dynamic. What prevents the LLM half-circle from improving indefinitely through better and better compensatory mechanisms? The framework asserts a ceiling exists without deriving it.

**Status:** Flagged as an open problem. The SARSI-L prediction that full circles ultimately win may be wrong if compensatory mechanisms scale faster than expected. No correction applied — honest acknowledgment of uncertainty is the appropriate stance.

---

### Assumption 5 — Binary Loop Closure

**Claim:** Each circle is either open or closed.

**Problem:** All evidence suggests loop closure is a gradient. NAS run by human teams is partial software self-improvement. RLHF is partial self-direction. AI-assisted EDA is partial hardware self-improvement. There is no identifiable point at which "partial" becomes "closed." The binary framing creates the illusion of discrete circle events when what actually happens is a slow shift along a continuum.

**Correction:** Replace binary open/closed with loop completion percentage — a qualitative estimate of what fraction of required loop steps are currently autonomous. Expressed as: Negligible / Early / Meaningful / Near-Complete / Closed.

---

## § III — Revised 5-Circle Taxonomy

Each circle carries: an operational closure criterion (falsifiable), a loop-completion estimate (qualitative, honest), a critical path bottleneck (mechanistic), four timeline scenarios (Fast / Central / Slow / Blocked), and flagged circular assumptions.

---

### Half-Circle — LLM Baseline

**Temporal range:** 2020–present and extending  
**Status:** Active and dominant

**What this is:** Not a circle — the baseline. A system that improves intelligence through external mechanisms (human RLHF, externally-manufactured hardware) without autonomous modification of its own weights, architecture, or training process.

**This is not a circle to close** — it is the reference state from which circles are measured.

#### Loop Completion

| Component | Completion | Note |
|---|---|---|
| Software autonomy | Early (~22%) | RLHF, RLAIF, inference scaling |
| Full loop | N/A | No loop to close — this is the baseline |

#### AI 2027 Reference

The AI 2027 scenario plays out entirely within the half-circle: mid-2025 agents → superhuman coders (March 2027) → superhuman AI researchers (August 2027) → ASI approach (December 2027). All of this is capability improvement through scale and compensatory mechanisms, not loop closure.

Critically: AI 2027's misalignment discovery (October 2027) creates conditions that make verifying Circle I closure harder, not easier. It is the most relevant AI 2027 prediction for SARSI-L timing.

#### Open Question

What prevents the LLM half-circle from improving indefinitely through better compensatory mechanisms? There is no known hard ceiling — only economic and physical limits on compute. The framework assumes the ceiling exists; this assumption is not derived and may be wrong (see Assumption 4 above).

#### Capabilities

RLHF/RLAIF · Inference-time scaling · Tool use · Multi-agent orchestration · Long context · Constitutional AI

---

### Circle I — Autonomous Software Self-Improvement

**Central timeline:** 2030–2035  
**Loop domain:** Software architecture, training, and deployment

#### Operational Closure Criterion

A system that — without human approval at any step — (a) identifies a self-modification likely to improve performance, (b) implements it, (c) validates improvement on held-out benchmarks, (d) deploys the modified system as baseline. **All four steps must be autonomous.** A system that can do (a)–(c) but requires human approval for (d) has not closed this loop.

#### Loop Completion

| Component | Completion | Note |
|---|---|---|
| Design autonomy | Early (~25%) | NAS partial; interpretability limited |
| Deploy autonomy | Negligible (~5%) | Human approval required at step (d) |

The gap between design autonomy and deploy autonomy is the institutional bottleneck — not the technical one.

#### 4-Scenario Timelines

| Scenario | Range | Key Condition |
|---|---|---|
| **Fast** | 2027–2029 | Alignment breakthrough by 2026 permits trusted self-modification concurrent with capability threshold |
| **Central** (revised) | 2030–2035 | Capability arrives at AI 2027 timescale; trusted autonomy lags 3–8 years as alignment advances |
| **Slow** | 2035–2042 | Alignment remains unsolved; regulatory frameworks require human approval in loop |
| **Blocked** | Indefinite | International treaty or safety incident prohibits autonomous AI self-modification; ~15–20% probability |

#### Critical Path Bottleneck

Not capability — **trusted autonomy**. The technical and institutional conditions under which autonomous self-modification is permitted. The institutional bottleneck (who authorizes AI to modify itself, and under what oversight?) may bind longer than the technical one (alignment).

AI 2027's October 2027 misalignment scenario is precisely the event that would trigger the Slow or Blocked path.

#### Flagged Circular Assumption

The claim that Circle I will "immediately recognize hardware as the bottleneck" and drive toward Circle II assumes a level of strategic self-direction that is itself evidence of Circle I being open — the strategic awareness is part of what Circle I means. Self-referential.

#### Capabilities

Architecture search · Autonomous training · Self-modification · Metacognitive evaluation · Interpretability

---

### Circle II — Autonomous Chip Design and Manufacture

**Central timeline:** 2038–2047  
**Loop domain:** Hardware design and fabrication

#### Operational Closure Criterion

A system that — without human design decisions — (a) generates chip specifications optimized for its own computational needs, (b) produces production-ready physical design output, (c) controls a fabrication process yielding functional chips at yield > 50%, (d) integrates new chips into its own training infrastructure.

**Critical distinction:** Steps (a)–(b) = chip *design*. Steps (c)–(d) = chip *manufacture*. These are different activities separated by ~10 years of feasibility. The v2.0 framework conflated them into a single milestone. Circle II is not closed until both are autonomous.

#### Loop Completion

| Component | Completion | Note |
|---|---|---|
| Chip design autonomy | Early–Meaningful (~35%) | AI-assisted EDA significant; synthesis optimization advancing rapidly |
| Fab autonomy | Negligible (~8%) | Highly automated but thousands of human operators required; AI directs but does not run fab |

#### 4-Scenario Timelines

| Scenario | Range | Key Condition |
|---|---|---|
| **Fast** | 2032–2037 | Design loop closes ~2030–32; alternative substrate (photonic/neuromorphic) achieves sufficient scale with simpler fab process operable without full Circle III |
| **Central** (revised) | 2038–2047 | Design autonomous ~2032–35; fab autonomy requires partial Circle III robotic systems (~2038–42); full loop closes 2–5 years after robotic fab demonstrated |
| **Slow** | 2045–2058 | Geopolitical fragmentation of semiconductor supply chains (export controls, Taiwan conflict risk, ASML nationalization) creates institutional block that AI capability cannot overcome |
| **Blocked** | Indefinite | Permanent human oversight requirement for fab + geopolitical supply chain restriction; ~20–25% probability |

#### Critical Path Bottleneck

**Physical fab autonomy.** Chip design can be AI-automated within 5 years; that problem is largely solved. Chip fabrication requires either (a) fully autonomous robotic fab operation — itself a Circle III problem — or (b) a shift to alternative substrates with simpler fab processes. This creates a dependency inversion: Circle II's hardest problem depends on Circle III's problem, and Circle III's hardware depends on Circle II chip design. The two circles must co-evolve.

#### Original Timeline Error

The v2.0 claim of Circle II opening ~2030 is too early by 10–15 years for the *full* loop. It is plausible for the design component only. The framework conflated chip design (a software problem approaching maturity) with chip manufacture (a physical infrastructure problem requiring Circle III). This is the most significant factual error in the original timeline.

#### Capabilities

AI-designed chips · Automated EDA · Custom silicon · Fab automation · Process optimization

---

### Circle III — Autonomous Physical World Manipulation

**Central timeline:** 2048–2060  
**Loop domain:** Physical self-replication and resource manipulation

#### Operational Closure Criterion

A system that — without human oversight — (a) identifies a physical resource need, (b) designs robots to fulfill it, (c) manufactures those robots from available materials, (d) operates them handling novel failure modes, (e) repairs/replaces components using in-situ materials. **Steps (c)–(e) constitute self-replication. Self-replication is the closure criterion — not merely useful robotic deployment.**

#### Loop Completion

| Component | Completion | Note |
|---|---|---|
| Navigation / manipulation | Meaningful (~40%) | Structured environments ~70%; unstructured environments ~25% |
| Self-replication | Negligible (~3%) | No demonstrated autonomous self-replication at required scale |

#### 4-Scenario Timelines

| Scenario | Range | Key Condition |
|---|---|---|
| **Fast** | 2040–2048 | Rapid humanoid robotics progress + energy density breakthrough (solid-state battery at scale ~2032–35) + Circle II partial closure enabling chip manufacture |
| **Central** (revised) | 2048–2060 | Dexterity and navigation improve at current trajectory; energy density improves but not dramatically; self-replication demonstrated in resource-rich environment (lunar/asteroid) before terrestrial generalization |
| **Slow** | 2060–2080 | Moravec Paradox harder than expected; energy density hits physical chemistry limits; in-situ materials processing proves fundamentally difficult robotically |
| **Blocked** | Indefinite | Terrestrial general self-replication never achieved; partial closure in space (asteroid mining) but no general Earth-based loop |

#### Critical Path Bottleneck

**Self-replication at the electronics level** requires solving Circle II for robotic hardware specifically. The circles are coupled: Circle II fab autonomy enables Circle III electronics self-manufacture; Circle III robotic systems enable Circle II fab autonomy. The correct model is mutual co-evolution, not sequencing.

Additionally: mobile robot energy density (battery technology) is a hard physical constraint independent of AI progress. Current lithium-ion at ~250 Wh/kg cannot power sustained autonomous factory-floor operations without frequent recharge interruptions. Solid-state batteries at 500+ Wh/kg would materially change this constraint.

#### Category Error Corrected: Sentient Robotics → Autonomous Goal Revision

"Sentient Robotics by 2035–2040" is not a predictable milestone. We have no scientific theory of consciousness adequate to predict when artificial systems become sentient. This has been replaced with:

**Behavioral criterion:** A robotic system that revises its own operational goals in response to conditions not anticipated by its designers, without human intervention, and achieves comparable or better outcomes than it would have with the original goals. This is observable and falsifiable.

#### Capabilities

Humanoid robots · Dexterous manipulation · Self-replicating factories · Autonomous goal revision · In-situ manufacturing

---

### Circle IV — Autonomous Biological Mastery

**Central timeline:** 2050–2065  
**Loop domain:** Biological mechanism discovery, therapeutic design, and deployment

#### Operational Closure Criterion

A system that — without human researcher direction — (a) generates and tests biological mechanism hypotheses, (b) designs therapeutic interventions, (c) validates through autonomous experimental pipeline (in vitro → in vivo → clinical), (d) deploys at population scale, (e) monitors outcomes and iterates. **Note: step (c) has an irreducible clinical floor of ~5–8 years imposed by biology, not by compute.**

#### Loop Completion

| Component | Completion | Note |
|---|---|---|
| AI-directed discovery | Meaningful (~45%) | AlphaFold, drug discovery AI — advancing rapidly |
| Autonomous clinical pipeline | Negligible (~5%) | Regulatory frameworks require human principal investigator |

#### 4-Scenario Timelines

| Scenario | Range | Key Condition |
|---|---|---|
| **Fast** | 2040–2050 | Regulatory frameworks adapt to AI-directed clinical research by ~2030; preclinical AI radically reduces non-clinical time; cancer mortality 95%+ reduced by 2042; meaningful biological aging reversal by 2048 |
| **Central** (revised) | 2050–2065 | Human-AI collaboration through ~2040; cancer largely manageable by 2045; significant aging reversal (10–20 years biological age) by 2055–60; full autonomous loop by 2060–65 |
| **Slow** | 2065–2085 | Regulatory frameworks permanently require human PI for life-affecting interventions; biological complexity reveals new mechanisms as fast as existing ones are solved |
| **Blocked** | Indefinite | Permanent human clinical oversight requirement prevents autonomous loop; ~30% probability (biological mastery achieved but loop never formally closes) |

#### Critical Path Bottleneck + Definitional Corrections Required

**"Cancer cured" ≠ a single event.** Cancer is ~200+ distinct diseases with different biology. "Cured" could mean:
- All cancer deaths eliminated — requires solving glioblastoma and pancreatic cancer; realistically 2050+
- 95%+ 5-year survival across major types — plausible 2038–2048
- First AI-designed cure for one specific cancer type — plausible 2028–2032

The v2.0 claim "cancer cured 2030–35" implies the first definition and is wrong by 15–20 years. The second definition is the most practically significant and is 8–13 years beyond v2.0's central estimate.

**"Aging reversed" ≠ a single mechanism.** Aging has 12 distinct identified hallmarks. "Reversed" could mean:
- Partial reversal of one hallmark (senolytics — in early clinical trials now)
- Biological age reduced 10+ years on epigenetic clocks — feasible 2040–2055
- Full reset to specified young-adult state — beyond current predictability

The v2.0 claim "aging reversed 2035–2045" is wrong by 10–20 years for meaningful reversal (second definition above).

#### Independence Note

Circle IV does **not** depend on Circle III. Biological mastery requires Circle I (AI reasoning capability) but not self-replicating robotics. Biological research advances with human-operated, AI-directed experimental infrastructure. Circle IV runs in parallel to Circle V+ after Circle III closes — they are independent, not sequential.

#### Capabilities

AI drug discovery · Protein design · Senolytic therapy · Epigenetic reprogramming · Autonomous clinical trials

---

### Circle V+ — Self-Replicating Orbital Manufacturing

**Central timeline:** 2080–2120  
**Loop domain:** Stellar-scale energy capture and self-replication

#### Operational Closure Criterion

A system that (a) autonomously designs, constructs, and operates orbital solar collectors, (b) uses harvested energy to power further construction (net-growth self-replication in space), (c) increases collection area at a rate outpacing maintenance and failure losses. **The net-growth condition is the closure criterion — not merely the deployment of orbital collectors.**

Note: "Dyson swarm" at any meaningful solar fraction is a 2100–2200 phenomenon in the central scenario, not 2055.

#### Loop Completion

| Component | Completion | Note |
|---|---|---|
| Launch infrastructure | Negligible–Early (~12%) | Starship cost reduction relevant; still far from required scale |
| In-space self-replication | Negligible (~2%) | Entirely speculative; depends on full Circle III |

#### 4-Scenario Timelines

| Scenario | Range | Key Condition |
|---|---|---|
| **Fast** | 2060–2080 | Circle III closes by 2045; lunar manufacturing bootstrapped by 2050; orbital self-replicating seed deployed 2060; Dyson coverage reaches 0.001% by 2080 |
| **Central** (revised) | 2080–2120 | Circle III closes by 2055–65; in-space manufacturing bootstrap 15–20 years; meaningful Dyson coverage (0.01% solar) by 2100–2120. This is a 2100 milestone, not 2055. |
| **Slow** | 2120–2200 | Physical self-replication harder than expected in space environment; regulatory frameworks limit autonomous orbital operations; orbital debris governance fails |
| **Blocked** | Indefinite | Space self-replication never achieved; large-scale solar collection via ground/lunar alternatives — Dyson swarm proper not achieved |

#### Critical Path Bottleneck

Circle III must close first, and Circle III is 15–30 years away by central estimates. Circle V+ cannot begin meaningful orbital self-replication until terrestrial self-replication is demonstrated.

**Circle IV is independent of Circle V+.** You do not need to solve aging to build a Dyson swarm. The correct critical path is: I → (II ↔ III) → V+, with IV parallel.

#### Original Timeline Error — Most Severe

The v2.0 claim of Circle V+ opening ~2055 is aggressive by 25–65 years depending on scenario. The claim corresponds to the Fast scenario only. The central estimate is 2080–2120 for the beginning of meaningful Dyson swarm construction. The 2055 date would require Circle III closing by ~2042 — which is the Fast scenario for Circle III, not the central. Stacking fast-scenario assumptions compounds optimism multiplicatively.

#### Kardashev Reference Point

Meaningful Dyson coverage is defined as >0.01% of solar output captured (~3.8 × 10²² W), exceeding Earth's current total energy consumption by ~10,000 times. This remains plausible within the 21st century in the Fast scenario and within the 22nd century in the Central scenario.

#### Capabilities

Orbital manufacturing · Space self-replication · Dyson swarm · Von Neumann probes · Computronium

---

## § IV — Gradient vs. Threshold Analysis

Not all circles are appropriately modeled as binary events. The following table classifies each circle by the nature of its closure and identifies where the binary framing is most misleading.

| Circle | Closure nature | Gradient components | Threshold components | Binary framing risk |
|---|---|---|---|---|
| **Half-Circle** | Entirely gradient | RLHF quality, inference scaling, tool use depth | None — no loop to close | Medium — "best half-circle" disguises wide capability range |
| **Circle I** | Partial threshold | Human oversight sliding from constant → exceptional → none | Autonomous deploy without approval is reasonably crisp | Low — if deployment autonomy is defined as the criterion |
| **Circle II** | Primarily gradient | Design autonomy 35% → 100% continuous; fab sub-processes automate incrementally | Net-positive yield from autonomous fab is threshold-ish | **High** — "design" and "manufacture" look like one thing but are decades apart |
| **Circle III** | Primarily gradient | Dexterity, navigation, energy density all gradient | Net-growth self-replication has threshold character | **High** — "sentient robotics" is either threshold or category error; the rest is gradient |
| **Circle IV** | Entirely gradient | Biological understanding, therapeutic capability accumulate continuously | "Cancer cured" / "aging reversed" are policy/definition thresholds, not natural ones | **Very high** — definitional work concealed by milestone language |
| **Circle V+** | Partial threshold | Dyson coverage fraction is continuous (0.001% → 1% → 100%) | Net-growth orbital self-replication is threshold-ish | Low — if net-growth is defined as the criterion |

For Circles II, III, and IV — the three highest-gradient circles — the framework should track loop completion percentage as a qualitative running estimate, not binary status.

---

## § V — Interdependence Matrix

The original framework presented circles as strictly sequential. The actual dependency structure is more complex.

**Key:**
- **P** = Hard prerequisite (must precede)
- **A** = Soft accelerant (helps but not required)
- **I** = Independent (no meaningful coupling)

|  | → Circle I | → Circle II | → Circle III | → Circle IV | → Circle V+ |
|---|---|---|---|---|---|
| **Circle I depends on** | — | A | A | A | A |
| **Circle II depends on** | P | — | A (mutual) | A | A |
| **Circle III depends on** | A | P (mutual) | — | A | A |
| **Circle IV depends on** | P | A | A | — | I |
| **Circle V+ depends on** | A | A | P | I | — |

*Reading: row "depends on" column. "Circle II depends on: Circle I (P)" = Circle I is a hard prerequisite for Circle II.*

### Key Structural Findings

**II ↔ III mutual dependency:** Circle II's hardest problem (fab autonomy) requires Circle III robotic physical operation. Circle III's robotic hardware requires Circle II chip design. They must co-evolve. The sequential narrative "II opens then III begins" is structurally incorrect.

**IV is largely independent of III:** Biological mastery requires Circle I (AI reasoning) but not self-replicating robotics. Circle IV does not need to wait for Circle III to close.

**IV and V+ are independent:** Solving aging is not required for building a Dyson swarm. The correct critical path is: I → (II ↔ III) → V+, with IV parallel. These two can proceed simultaneously after Circle III closes.

---

## § VI — Revised Dominance Dynamics

Dominance function per circle:

```
D_n(t) = floor_n + (100 − floor_n) · σ(k_rise · (t − t_rise)) · (1 − σ(k_decay · (t − t_decay)))
where σ(x) = 1 / (1 + e^−x)
```

### Parameter Comparison: v2.0 (Original) vs. v2.1 (Revised Central)

| Circle | v2.0 t_rise | v2.1 t_rise | Shift | v2.0 t_decay | v2.1 t_decay | Shift |
|---|---|---|---|---|---|---|
| Half-circle | 2022 | 2022 | — | 2028 | 2031 | +3 |
| Circle I | 2027 | 2032 | **+5** | 2033 | 2038 | +5 |
| Circle II | 2032 | 2042 | **+10** | 2040 | 2052 | +12 |
| Circle III | 2039 | 2053 | **+14** | 2048 | 2064 | +16 |
| Circle IV | 2047 | 2057 | **+10** | 2062 | 2076 | +14 |
| Circle V+ | 2058 | 2095 | **+37** | — | — | — |

The rightward shift is most dramatic for Circles III, IV, and V+ because v2.0 stacked fast-scenario assumptions multiplicatively. Each circle's fast path was treated as the central estimate, and the errors compounded.

### Dominance Periods (Central Estimate)

| Phase | Dominant Circle | Period |
|---|---|---|
| Current | Half-circle | 2020–2033 |
| Near-term | Circle I | 2033–2043 |
| Mid-term | Circle II | 2043–2055 |
| Long-term | Circle III | 2055–2068 |
| Extended | Circle IV | 2058–2080 |
| Future | Circle V+ | 2095+ |

Note: overlapping ranges reflect co-dominance periods where two circles simultaneously contribute significantly.

---

## § VII — Timeline Skepticism: Historical Base Rate

Every major AI timeline prediction since 1956 has been wrong in the optimistic direction by 10–30 years. The reliable prior before applying any new prediction: subtract 5–20 years of structural optimism from the central estimate.

### Historical Reference Points

| Year | Prediction | What happened |
|---|---|---|
| 1956 | McCarthy/Minsky: AGI within 20 years | Off by 70+ years (still unresolved) |
| 1982 | Expert systems revolution by 1990 | AI winter followed |
| 1997 | Deep Blue → AGI imminent | 15 years of limited progress |
| 2016 | AlphaGo → AGI by 2025 | Still uncertain |
| 2021 | GPT-3 → AGI within 2 years | 4 years later, question is more complex |

Pattern: AI predictions that extrapolate from a single capability breakthrough typically overestimate speed of generalization by 5–20 years.

### AI 2027 Is a Scenario, Not a Forecast

The AI 2027 document does not predict cancer cures, aging reversal, or Dyson swarms. AI 2027's timeline ends in 2027. Everything after that in SARSI-L is extrapolation from extrapolation. The scenario was written to explore AI safety dynamics, not to map a civilization trajectory. Using it as an anchor for a 2100 Dyson swarm timeline compounds uncertainty multiplicatively — each step in the chain inherits the prior step's uncertainty.

What AI 2027 does explicitly show: the misalignment scenario (October 2027) is precisely the kind of event that extends trusted-autonomy timelines significantly. This is the single most relevant AI 2027 prediction for Circle I timing.

### Revised Timeline Comparison

| Milestone | v2.0 claim | Fast | Central (revised) | Slow | Central shift |
|---|---|---|---|---|---|
| Circle I | ~2027 | 2027–29 | 2030–2035 | 2035–2042 | +3–8 yr |
| Circle II | ~2030 | 2032–37 | 2038–2047 | 2045–2058 | +8–17 yr |
| Circle III | ~2035 | 2040–48 | 2048–2060 | 2060–2080 | +13–25 yr |
| Circle IV | ~2040 | 2040–50 | 2050–2065 | 2065–2085 | +10–25 yr |
| Cancer substantially addressed | 2030–35 | 2028–35 | 2038–2048 | 2048–2060 | +8–13 yr |
| Meaningful aging reversal | 2035–45 | 2040–50 | 2055–2070 | 2070–2090 | +20–25 yr |
| Meaningful Dyson coverage | ~2055 | 2070–85 | 2090–2130 | 2140–2200+ | +35–75 yr |

---

## § VIII — What Would Change the Estimates

The following observations, if made, would materially update the timeline estimates in either direction.

| Observation | Direction | Magnitude |
|---|---|---|
| AI system verifiably closes software self-modification loop before 2028 | All timelines compress | Large (5–10 yr) |
| Major AI safety incident triggers global regulation of autonomous AI self-modification | I, II, III extend or blocked | Large (10–20 yr) |
| Geopolitical fragmentation of semiconductor supply chains (Taiwan conflict, ASML export controls) | II severely delayed or blocked | Large (10–30 yr) |
| Solid-state battery achieves 5× current energy density at commercial scale | III compresses | Moderate (5–10 yr) |
| AlphaFold-class breakthrough for protein-protein interaction networks (in vivo fidelity) | IV compresses | Moderate (5–10 yr) |
| FDA creates AI-directed clinical trial pathway before 2030 | IV compresses | Moderate (3–8 yr) |
| Fault-tolerant quantum computing at commercial scale | New Circle I.5 inserted; all renumbered | Uncertain (reshuffles framework) |
| SpaceX Starship achieves $10/kg to LEO operational by 2030 | V+ compresses | Moderate (5–10 yr) |
| Self-replication demonstrated in controlled terrestrial environment before 2040 | III and V+ compress | Large (10–15 yr) |
| LLM half-circle compensatory mechanisms scale faster than full-circle recursive loops | Half-circle ceiling revised upward; full-circle advantage window delayed | Uncertain (challenges Assumption 4) |
| International alignment treaty bans autonomous AI self-modification by 2030 | I blocked; all subsequent severely extended | Very large |

---

## § IX — Revised SARSI-L Principles

The original 10 principles are preserved. Three new principles are added addressing problems identified in this critical review. Revised principles are marked [REVISED].

---

**Principle 01 — The Nesting Principle**

Every circle of degree n contains all circles of degree < n as active inner loops. Higher circles accelerate rather than replace lower ones. A system operating at Circle III still uses and accelerates Circles I and II internally.

**Principle 02 — The Bottleneck Dominance Principle**

At any epoch, one circle is the primary intelligence driver. Identifying and accelerating this circle is the highest-leverage action available. Misidentifying the bottleneck — investing in Circle V+ when Circle II is the binding constraint — wastes capability proportional to the gap in circle degree.

**Principle 03 — The Half-Circle Superiority Window**

Finite time windows exist where a highly compensated half-circle outperforms a newly-opened full circle in specific metrics. These windows should be exploited — they are not compromises but the correct strategy during the window. *Note: the mechanism by which these windows close remains an open problem (see Assumption 4). The window may be longer than the framework currently models.*

**Principle 04 — The Speed–Degree Trade-off**

Inner circles iterate faster but have lower degree ceilings. Outer circles have higher ceilings but longer cycles. Optimal growth maintains all inner circles at peak efficiency while investing in the next outer circle.

**Principle 05 — The Leading-Edge Spillover Principle**

Groups at higher circles generate outputs that accelerate advancement for all groups. The leading group effectively subsidizes global intelligence growth — its open research, published models, and available infrastructure shorten time to circle closure for later groups.

**Principle 06 — The Attractor Invariance Principle**

The ultimate attractor (Type II civilization) does not change as circles advance. All circles should be evaluated against this fixed terminal state — while acknowledging that the attractor's precise location in capability space is itself a construction of the framework, not a derived property of reality.

**Principle 07 — The Compensatory Compression Principle**

Strong half-circles accelerate full circle development by demonstrating its value and generating economic surplus that funds closure research. The LLM era's productivity gains fund the capital investments required for Circle II fab infrastructure.

**Principle 08 — The Behavioral Milestone Principle** [REVISED]

Milestones must be defined by observable behavior, not by philosophical categories. "Sentient Robotics" is replaced with autonomous goal revision under unanticipated conditions. "Cancer cured" requires specification of which definition applies (all deaths eliminated vs. 95%+ survival vs. first AI-designed cure). "Aging reversed" requires specification of mechanism and magnitude. Milestones without behavioral definitions produce false timelines.

**Principle 09 — The Meta-Adaptive Principle**

SARSI-L updates its own parameters as empirical evidence arrives. Each application of the framework to practical work generates observations that can be compared against predictions; deviations are data for revision. A theory that accurately predicts its own revision conditions is stronger than one that doesn't anticipate obsolescence. This v2.1 revision is itself an exercise of this principle.

**Principle 10 — The Compression Principle**

Each new circle compresses the timeline to all subsequent circles. Early circle closure is disproportionately valuable because its benefits compound forward through every subsequent circle. Investment in Circle I closure now has higher expected value than equivalent investment in any higher circle.

**Principle 11 — The Operational Criterion Principle** [NEW]

Every circle must carry a falsifiable closure criterion — a specific, observable behavior that constitutes loop closure and that cannot be satisfied post-hoc by definitional adjustment. Criteria that can be satisfied by any sufficiently capable system, at any time, without independent verification, are not operational criteria. A framework without operational criteria is a narrative, not a theory.

**Principle 12 — The Gradient Principle** [NEW]

Most circle transitions are gradient, not threshold. Loop completion should be tracked as a qualitative continuous estimate (Negligible / Early / Meaningful / Near-Complete / Closed), not as binary open/closed. Binary framing creates false confidence about which circle we are "in" and implies smooth stasis followed by sudden transition, when reality shows gradual shift throughout. The practical consequence: strategies appropriate for "Early" completion differ from strategies appropriate for "Near-Complete" completion of the same circle.

**Principle 13 — The Critical Path Principle** [NEW]

Timelines must derive from the mechanism of transition — the specific physical and institutional steps on the critical path — not from narrative adjacency to the prior circle's opening date. Any timeline that cannot be derived from a stated critical path is an extrapolation, not a prediction, and should be presented as a scenario range with explicit uncertainty. The scenario format (Fast / Central / Slow / Blocked) is the minimum required for honest timeline presentation.

---

## Appendix A — Dominance Function Parameters (v2.1 Central)

```
D_n(t) = floor_n + (100 − floor_n) · σ(k_rise · (t − t_rise)) · (1 − σ(k_decay · (t − t_decay)))
σ(x) = 1 / (1 + e^−x)

Half-circle: floor=3,  t_rise=2022, k_rise=2.2, t_decay=2031, k_decay=1.6
Circle I:    floor=8,  t_rise=2032, k_rise=1.6, t_decay=2038, k_decay=1.2
Circle II:   floor=14, t_rise=2042, k_rise=1.4, t_decay=2052, k_decay=1.0
Circle III:  floor=21, t_rise=2053, k_rise=1.1, t_decay=2064, k_decay=0.8
Circle IV:   floor=29, t_rise=2057, k_rise=0.9, t_decay=2076, k_decay=0.6
Circle V+:   floor=40, t_rise=2095, k_rise=0.6  (no modeled decay)
```

---

## Appendix B — Loop Completion Qualitative Scale

| Level | Description | Operational meaning |
|---|---|---|
| **Negligible** | <10% | Specific sub-tasks can be AI-assisted; no autonomous pipeline exists |
| **Early** | 10–35% | Some pipeline stages autonomous; human review required at most decision points |
| **Meaningful** | 35–65% | Majority of pipeline stages autonomous; human oversight at critical decisions only |
| **Near-Complete** | 65–90% | Human oversight exceptional rather than routine; system can run for extended periods autonomously |
| **Closed** | >90% | Operational closure criterion met; full loop autonomous as defined |

---

## Appendix C — Critical Path Summary by Circle

| Circle | Rate-limiting bottleneck | Type | Circle dependency |
|---|---|---|---|
| I | Trusted autonomy: institutional permission to deploy self-modification | Institutional | None |
| II (design) | Architecture search quality + validation rigor | Technical | Circle I |
| II (fab) | Robotic physical operation of fab process | Physical + Circle III | Circle III (mutual) |
| III | Self-replication at electronics level; mobile energy density | Physical + Circle II | Circle II (mutual) |
| IV | Autonomous clinical pipeline; regulatory frameworks; biological complexity | Institutional + Complexity | Circle I |
| V+ | Terrestrial self-replication first; launch economics; in-space manufacturing bootstrap | Physical + Circle III | Circle III |

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-07-22 | Initial framework: 5 circles, half-circle concept, SARSI-L naming |
| 2.0 | 2026-07-22 | 4-spec analysis per circle, dominance chart, meta-adaptive mechanism, comparison matrix, 10 principles |
| 2.1 | 2026-07-22 | **Critical Revision**: 5 circular assumptions audited and corrected; operational closure criteria added per circle; speed/degree metrics replaced with qualitative loop completion; 4-scenario timelines replacing point estimates; gradient analysis; interdependence matrix; historical base rate skepticism; 3 new principles; central timelines shifted +5–37 years across circles |

*See also: SARSI-L_Critical_Revision.md (full audit workpaper with extended analysis)*

---

*SARSI-L Framework v2.1 · 2026-07-22*
*Kurzweil, The Singularity Is Near (2005) & The Singularity Is Nearer (2024) · AI 2027 Scenario (ai-2027.com) · Kardashev, 1964 · Dyson, 1960*
