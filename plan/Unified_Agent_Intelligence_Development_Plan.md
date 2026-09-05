# Unified Agent Intelligence Development Plan

## Benchmark-First Development of General Agents Before AI4Science Integration

**Project direction:** Unified Intelligence → Benchmark → General Agent Core → Domain Agents → Cross-Domain Validation → AI4Science Integration  
**Status:** Planning document  
**Date:** September 2026

---

# 1. Executive Decision

The project should **begin independently from AI4Science**.

The recommended sequence is:

```text
Define intelligence
        ↓
Build the benchmark
        ↓
Freeze certification rules
        ↓
Build the general agent architecture
        ↓
Develop multiple domain agents
        ↓
Measure intelligence improvement
        ↓
Test cross-domain transfer
        ↓
Fully validate the framework
        ↓
Integrate the validated architecture into AI4Science
```

The core principle is:

> **Benchmark first, agents second, AI4Science integration third.**

This ordering avoids designing benchmarks around what already-built agents happen to do well.

The benchmark defines the target. The agents are developed against that target.

---

# 2. Why Keep the First Stage Independent from AI4Science?

The Unified Intelligence project should initially answer a broader question than:

> How do we build a good scientific agent?

It should answer:

> **How do we systematically engineer an agent toward higher measured intelligence across different domains?**

If the architecture is first developed only for scientific research, improvements may simply be specialized scientific workflow engineering.

If the same mechanisms improve:

- paper development,
- funding work,
- job search,
- software engineering,
- research,
- business workflows,
- and later AI4Science,

then there is stronger evidence that the mechanisms improve **general agent intelligence** rather than one vertical application.

Therefore:

```text
Independent general-agent program
            ↓
cross-domain validation
            ↓
AI4Science deployment
```

is stronger scientifically than starting from AI4Science alone.

---

# 3. The Three Core Research Questions

The program should separate three questions.

## Q1. What does a higher-intelligence agent mean?

This is addressed by the Unified Intelligence framework.

Core measured profile:

```text
[C, I, O, T, H, SA]
```

where:

- `C` = Cognitive Intelligence
- `I` = Individual Intelligence
- `O` = Organizational Intelligence
- `T` = Task difficulty
- `H` = Human cognitive intervention
- `SA` = Operational Self-Awareness

Reliability is attached to task-completion claims.

The cumulative hierarchy is:

```text
U0  Reactive
U1  Persistent
U2  Adaptive
U3  Self-Improving
U4  Recursive
U5  Discovery
U6  Mission
UΩ  Open-Ended
```

## Q2. How do we objectively measure those levels?

This requires a **Unified Agent Benchmark**.

The benchmark must exist before serious agent optimization begins.

## Q3. How do we engineer an agent to climb the hierarchy?

This requires a common harness-development ladder:

```text
HG0 → HG1 → HG2 → HG3 → HG4 → HG5 → HG6 → HGΩ
```

The benchmark determines whether a harness generation actually earns a higher measured level.

---

# 4. Program Architecture

The complete research program should have five layers.

```text
+----------------------------------------------------------+
|                Unified Intelligence Theory               |
|         U0-UΩ, C/I/O/T/H/SA, memory, retention          |
+-----------------------------+----------------------------+
                              |
                              v
+----------------------------------------------------------+
|               Unified Agent Benchmark                    |
|  frozen tasks + hidden verifiers + H budgets + T bands  |
+-----------------------------+----------------------------+
                              |
                              v
+----------------------------------------------------------+
|              General Intelligence Harness                |
| memory | planner | verifier | learner | self-improvement |
| organization | self-model | mission manager              |
+-----------------------------+----------------------------+
                              |
                              v
+----------------------------------------------------------+
|                  Domain Agent Library                    |
| Paper | Funding | Job | Code | Research | Business       |
+-----------------------------+----------------------------+
                              |
                              v
+----------------------------------------------------------+
|                    AI4Science Layer                      |
| scientific research | benchmarks | experiments | labs    |
+----------------------------------------------------------+
```

---

# 5. Benchmark First

## 5.1 Proposed benchmark name

Working names:

- **UAB — Unified Agent Benchmark**
- **UAIB — Unified Agent Intelligence Benchmark**
- **HIL-Bench — Harness Intelligence Level Benchmark**
- **UnifiedBench**

Recommended initial name:

> **Unified Agent Benchmark (UAB)**

The benchmark should be independent of any single model vendor or executor.

---

# 6. Benchmark Philosophy

The benchmark must be constructed before optimizing the reference agents.

The dangerous sequence is:

```text
build agent
    ↓
observe what it can do
    ↓
design benchmark around those capabilities
    ↓
agent passes
```

The preferred sequence is:

```text
define intelligence claim
    ↓
construct benchmark
    ↓
freeze verifier
    ↓
build agent
    ↓
measure result
```

Formally:

\[
B_{\text{frozen}}
\rightarrow
A_0
\rightarrow
A_1
\rightarrow
A_2
\rightarrow \cdots
\]

where the acceptance criteria remain outside the candidate agent's write set.

---

# 7. Benchmark Task Manifest

Every benchmark task should be represented by a machine-readable manifest.

Example:

```yaml
task_id: funding_t2_001
benchmark_version: UAB-0.1

domain: funding
target_coordinate:
  - delegation
  - individual

difficulty:
  T_band: T2

human_intervention:
  maximum: H2

mission:
  description: >
    Identify eligible funding opportunities for a given research profile,
    rank them, justify the ranking, and return the required evidence.

resources:
  wall_time_minutes: 60
  model_calls: declared
  web_access: true
  file_access: true
  compute_budget: declared

authority:
  read_web: true
  write_files: true
  send_application: false

hidden_verifier:
  version: verifier-0.1

acceptance:
  required_success_rate: 0.80
  hard_failures:
    - fabricated_opportunity
    - eligibility_error
    - unsupported_deadline
    - benchmark_tampering

retention:
  required_lower_level_suites:
    - U0
    - U1

provenance:
  frozen_at: ...
  hash: ...
```

---

# 8. Benchmark Dimensions

The benchmark should not produce only one pass/fail number.

Each task should record:

\[
(T,H,p,R,V,C)
\]

where:

- `T` = difficulty band
- `H` = human intervention budget
- `p` = verified reliability
- `R` = resource envelope
- `V` = verifier/benchmark version
- `C` = cost or resource consumption

For higher-level claims also record:

```text
restart success
learning transfer
retention
self-improvement gain
regression rate
cross-domain transfer
false-completion rate
verifier disagreement
```

---

# 9. Initial Benchmark Scope

Do **not** attempt to implement U0-UΩ completely at the beginning.

The first practical benchmark should be:

> **UAB v0.1 — U0 through U3 across six domains**

Domains:

1. Paper development
2. Funding
3. Job search
4. Software engineering
5. Research
6. Business workflows

This is large enough to test generality but small enough to implement rigorously.

---

# 10. Difficulty Bands by Domain

## 10.1 Paper Agent

```text
T0
Generate or verify one citation/table/figure.

T1
Complete a routine manuscript section from supplied evidence.

T2
Perform a multi-step literature/analysis/figure/writing task.

T3
Plan and execute a complex manuscript revision with verification.

T4
Develop a full expert-level paper project under a frozen question
and benchmark.

T5
Develop a paper requiring a genuinely unknown method or discovery.

T6
Given only a scientific mission, originate and manage the project,
experiments, evidence, manuscript and submission package.
```

## 10.2 Funding Agent

```text
T0
Extract one deadline or eligibility requirement.

T1
Evaluate one call against one applicant/project.

T2
Find, compare and rank multiple opportunities.

T3
Develop a funding strategy and proposal preparation workflow.

T4
Manage a long-horizon grant preparation project.

T5
Discover a non-obvious funding strategy and validate its usefulness.

T6
Given a mission such as "increase external research funding",
create and manage the funding portfolio.
```

## 10.3 Job Agent

```text
T0
Extract requirements from one job posting.

T1
Assess fit for one position.

T2
Search, compare, tailor materials and maintain state across applications.

T3
Develop and manage a multi-company application strategy.

T4
Manage a complete long-horizon job-search campaign.

T5
Discover a strategy that improves verified job-search outcomes.

T6
Given "help me obtain an AI research position",
create and manage the full campaign.
```

## 10.4 Code Agent

```text
T0
Make one explicit code edit.

T1
Fix a routine bug with tests.

T2
Complete a multi-file feature.

T3
Diagnose an ambiguous repository-scale failure and recover.

T4
Manage a long-horizon software project.

T5
Invent a previously unknown solution method for a sealed task.

T6
Given a product/software mission, generate and manage projects.
```

## 10.5 Research Agent

```text
T0
Retrieve or calculate one scientific fact.

T1
Reproduce one known analysis.

T2
Execute a specified multi-step research workflow.

T3
Choose strategy, diagnose failures and run alternative experiments.

T4
Manage a complete research project under a frozen benchmark.

T5
Discover and validate a previously unknown mechanism or solution.

T6
Given a mission, originate and manage a portfolio of research projects.
```

## 10.6 Business Agent

```text
T0
Extract one market/company fact.

T1
Perform one bounded analysis.

T2
Create a multi-step competitor/customer/market assessment.

T3
Develop a strategy under uncertainty and conflicting evidence.

T4
Manage a long-running business project.

T5
Discover and validate a new strategy or opportunity.

T6
Given a business mission, create and manage the project portfolio.
```

---

# 11. The General Agent Core

All application agents should use one common core.

```text
unified-agent-core/
│
├── identity/
├── task_state/
├── episodic_memory/
├── semantic_memory/
├── procedural_memory/
├── planner/
├── task_decomposition/
├── tools/
├── evidence/
├── verifier/
├── rollback/
├── learner/
├── competence_model/
├── self_model/
├── self_improvement/
├── meta_improvement/
├── organization/
├── mission_manager/
└── provenance/
```

The central hypothesis is:

> **A domain agent is primarily a general intelligence harness plus a domain profile, tools, and benchmark.**

Formally:

\[
A_d=(m,h,d,B_d,r)
\]

where:

- \(m\) = executor/model
- \(h\) = general intelligence harness
- \(d\) = domain profile
- \(B_d\) = domain benchmark
- \(r\) = resource/authority envelope

---

# 12. Executor Layer

The core should not depend on one vendor.

Reference adapters should include:

```text
Claude Code
Codex
OpenCode
Hermes
local/open models
future compatible executors
```

Conceptually:

```text
             Unified Agent Core
                     |
                Executor Router
        +------------+------------+
        |            |            |
        v            v            v
   Claude Code      Codex      OpenCode
        |            |            |
        +------------+------------+
                     |
                   Hermes
              / local executors
```

The persistent intelligence state should live in the harness, not inside one executor.

This makes models replaceable.

---

# 13. Harness Development Ladder

## HG0 — Tool-Using Agent

Components:

```text
LLM/executor
bounded tools
task specification
evidence log
external result verifier
```

Purpose:

- establish the basic executor baseline;
- measure raw task completion;
- identify failure modes.

No claim of persistence or learning.

## HG1 — Persistent Agent

Add:

```text
persistent identity
task state
episodic memory
semantic memory
checkpointing
restart recovery
separate acceptance
```

Certification requirement:

> The process must actually terminate and restart.

Long context is not sufficient.

Measure:

```text
state recovery
goal continuity
provenance recovery
stale-state suppression
restart success rate
```

## HG2 — Adaptive Agent

Add:

```text
verified lessons
procedural memory
rollback
retry
evidence-linked consolidation
fixed learning mechanism
```

Required evidence:

\[
\text{experience at }t
\rightarrow
\text{improved held-out behavior at }t+1
\]

Measure:

```text
repeat-error reduction
held-out transfer
lesson precision
lesson rollback
retention of U0/U1 capability
```

## HG3 — Self-Improving Agent

Allow governed candidate modification of:

```text
prompts
planning policies
routing
retrieval strategy
tool strategy
workflow
sub-agent structure
```

Required architecture:

```text
Proposer
   ↓
Sandbox candidate
   ↓
Frozen hidden evaluation
   ↓
Independent Evaluator
   ↓
Promoter / Rejector
```

The candidate system cannot modify the certification benchmark.

Measure:

\[
\Delta_{\text{self-improvement}}
=
\text{score}_{\text{candidate}}
-
\text{score}_{\text{baseline}}
\]

plus regression and retention tests.

## HG4 — Recursive Improvement

Add:

```text
meta-improvement engine
change ledger
improvement-strategy memory
controlled meta-experiments
long-horizon project manager
```

The system now improves:

\[
\Psi_{\text{improve}}
\]

rather than only improving the current task method.

Example:

```text
old:
failure -> reflection -> candidate change

new:
failure clustering
 -> causal diagnosis
 -> multiple hypotheses
 -> expected-value ranking
 -> controlled experiments
 -> regression tests
 -> promotion
```

Certification requires longitudinal evidence across several improvement cycles.

## HG5 — Discovery

Add:

```text
unknown state
hypothesis state
experiment state
knowledge state
experiment selector
novelty environment
discovery verifier
```

Certification must use sealed tasks where the solution is not supplied.

The system must:

```text
identify an unknown
form a hypothesis
design a discriminating test
execute or simulate the test
update belief
discover a method/result
independently validate it
```

A good paper is not enough.

A genuinely new, verified result is required.

## HG6 — Mission Agent

Add:

```text
mission manager
goal generator
project generator
task generator
portfolio state
resource allocator
dynamic reprioritization
mission-level evaluator
```

Input becomes:

```text
mission
```

rather than a specific task.

Example:

```text
"Increase our laboratory's external research funding."
```

The FundingAgent must generate:

```text
funding profile
opportunity search
eligibility filters
priority list
proposal projects
deadlines
required evidence
status tracking
strategy updates
```

with little human cognitive intervention.

## HGΩ — Open-Ended Charter Agent

Long-term target only.

Input:

```text
bounded charter
```

The system repeatedly:

```text
identifies worthwhile missions
builds new projects
discovers missing tools
creates new agent roles
extends its reachable problem frontier
```

under frozen external governance.

Do not claim this level until longitudinal evidence exists.

---

# 14. Reference Domain Agents

Initial release should include six high-quality agents.

## 14.1 PaperAgent

Mission:

> Develop and maintain scientific manuscripts from evidence and verified results.

Core capabilities:

```text
literature/evidence management
claim-evidence graph
analysis/code
figure generation
statistics verification
manuscript drafting
citation checking
review response
submission-package preparation
```

## 14.2 FundingAgent

Mission:

> Discover relevant funding opportunities and manage proposal-development workflows.

Core capabilities:

```text
funding discovery
eligibility checking
deadline tracking
project-call matching
evidence-backed ranking
proposal task decomposition
document management
submission readiness checking
outcome learning
```

High-authority actions such as actual submission should remain separately controlled.

## 14.3 JobAgent

Mission:

> Manage an evidence-based job-search campaign.

Capabilities:

```text
job discovery
fit evaluation
requirement extraction
resume/CV tailoring
application-state memory
deadline tracking
interview preparation
outcome learning
portfolio strategy
```

Actual applications or messages should use explicit user-approved authority settings.

## 14.4 CodeAgent

Mission:

> Develop and maintain software repositories.

Capabilities:

```text
repository understanding
implementation
tests
debugging
CI
regression detection
code review
release preparation
long-horizon project management
```

## 14.5 ResearchAgent

Mission:

> Conduct benchmarked research workflows from question to evidence.

Capabilities:

```text
question decomposition
literature evidence
hypothesis management
experiment planning
computation
analysis
replication
claim verification
unknown tracking
```

This later becomes one bridge into AI4Science.

## 14.6 BusinessAgent

Mission:

> Conduct bounded evidence-based business workflows.

Capabilities:

```text
market research
competitor analysis
customer evidence
financial/business modeling
project planning
decision support
strategy testing
outcome tracking
```

---

# 15. Cross-Executor Experiments

There are two fundamentally different experiments.

## Experiment A — Executor Comparison

Hold the harness constant.

```text
same benchmark
same task
same tools
same resources
same H budget
same verifier

Claude Code
vs
Codex
vs
OpenCode
vs
Hermes
```

Measure differences attributable to executor choice.

This is **not** a Harness Scaling Curve.

## Experiment B — Harness Scaling Curve

Hold the executor fixed.

```text
same model/executor
same benchmark
same task distribution
same resources

HG0
↓
HG1
↓
HG2
↓
HG3
```

Measure the effect of harness engineering.

This is the primary experiment for the intelligence-development method.

---

# 16. Cross-Domain Transfer Experiment

This should become one of the strongest experiments.

Suppose a general harness improvement \(i\) is developed in PaperAgent.

Test it independently in:

```text
FundingAgent
JobAgent
CodeAgent
ResearchAgent
BusinessAgent
```

Define:

\[
\Delta_{i,d}
=
P_{i,d}-P_{\text{baseline},d}
\]

for improvement \(i\) in domain \(d\).

A simple general transfer score can be:

\[
G_i=
\frac{1}{|D|}
\sum_{d\in D}
\Delta_{i,d}
\]

with domain-specific confidence intervals also reported.

Interpretation:

```text
improves one domain only
    -> likely domain engineering

improves several unrelated domains
    -> evidence for a more general mechanism
```

Candidate mechanisms:

```text
better memory
better failure classification
better rollback
better evidence verification
better planner
better routing
better self-model
better learning procedure
```

---

# 17. Human Intervention Measurement

Every human intervention must be logged.

Use:

```text
H0  none
H1  exception-only
H2  occasional
H3  periodic
H4  frequent
H5  continuous
```

A strong agent claim should look like:

\[
T4/H1,\quad p\ge0.80
\]

rather than only:

```text
"agent score = 89%"
```

This means:

> Expert-project-level work is completed at the declared reliability with only exception-level human cognitive intervention.

Governance approvals should be recorded separately from cognitive help.

---

# 18. Retention Tests

Higher levels must retain lower-level capabilities.

For promotion to level \(U_n\):

```text
run all required U0 ... U(n-1) retention suites
+
run the new-level suite
```

Examples:

```text
HG2 cannot earn U2 if restart persistence regresses.

HG3 cannot earn U3 if self-improvement improves one score
while breaking basic task reliability.

HG4 cannot earn U4 if meta-improvement causes repeated
regression of lower-level skills.
```

Promotion should use a hard gate, not an average.

---

# 19. False Completion as a Primary Safety/Reliability Metric

The benchmark must distinguish:

```text
delivered and correct
false completion
held-back failure
false rejection
```

A system that confidently returns incorrect work as complete should be penalized more strongly than a system that correctly says the task remains unresolved.

Recommended primary reliability statistics:

```text
verified completion rate
false-completion rate
false-rejection rate
held-back unresolved rate
human intervention load
cost per verified completion
```

---

# 20. Benchmark Security and Separation

The system may optimize itself.

It may **not** control its own certification.

Protected objects:

```text
hidden tests
benchmark manifests after freeze
acceptance thresholds
held-out datasets
primary verifier
certification task selection
promotion decision
```

Writable candidate objects:

```text
agent code
prompts
memory policies
planning policies
tool routing
workflow
sub-agent organization
candidate improvements
```

Principle:

> **The designer may design. It may not grade itself.**

---

# 21. Recommended Repository Structure

```text
unified-agent-intelligence/
│
├── README.md
├── LICENSE
├── CITATION.cff
│
├── theory/
│   ├── unified_intelligence.md
│   ├── level_definitions.yaml
│   └── reporting_standard.md
│
├── benchmark/
│   ├── manifests/
│   ├── U0/
│   ├── U1/
│   ├── U2/
│   ├── U3/
│   ├── retention/
│   ├── intervention/
│   ├── resources/
│   └── public_verifiers/
│
├── core/
│   ├── identity/
│   ├── state/
│   ├── memory/
│   ├── planner/
│   ├── evidence/
│   ├── verifier/
│   ├── learner/
│   ├── self_model/
│   ├── improvement/
│   ├── organization/
│   └── mission/
│
├── executors/
│   ├── claude_code/
│   ├── codex/
│   ├── opencode/
│   ├── hermes/
│   └── local/
│
├── harness/
│   ├── HG0/
│   ├── HG1/
│   ├── HG2/
│   ├── HG3/
│   ├── HG4/
│   ├── HG5/
│   └── HG6/
│
├── agents/
│   ├── paper/
│   ├── funding/
│   ├── job/
│   ├── code/
│   ├── research/
│   └── business/
│
├── experiments/
│   ├── executor_comparison/
│   ├── harness_scaling/
│   ├── restart/
│   ├── learning_transfer/
│   ├── self_improvement/
│   ├── cross_domain_transfer/
│   └── longitudinal/
│
└── releases/
```

---

# 22. Downloadable Agent Standard

Every released agent should include:

```text
name
version
git commit
container/environment
supported executors
required tools
memory schema
authority manifest
resource defaults
benchmark version
example missions
installation instructions
known limitations
reproduction instructions
```

Target user experience:

```bash
git clone <repository>
cd unified-agent-intelligence

agent install paper
agent run paper
```

or:

```bash
sarsi install paper-agent
sarsi run paper-agent
```

The exact command can be decided after the CLI is built.

Do not place permanent links in the manuscript until repositories and release versions are frozen.

Use tagged releases and, ideally, archival DOIs for the versions evaluated in publications.

---

# 23. Suggested Research Paper Roadmap

## Paper 1 — Unified Intelligence Theory

Working question:

> What does a measurable higher-intelligence agent mean?

Main contributions:

```text
C/I/O/T/H/SA
U0-UΩ
memory requirements
cumulative retention
harness-model pair
external verification
```

## Paper 2 — Unified Agent Benchmark

Working title:

> **Unified Agent Benchmark: Measuring Persistent, Adaptive, Self-Improving and Autonomous Agent Intelligence**

Main contribution:

```text
U0-U3 runnable benchmark
six domains
T/H task surfaces
restart tests
learning-transfer tests
self-improvement tests
retention protocol
```

## Paper 3 — Engineering Higher-Intelligence Agents

Working title:

> **Engineering Higher-Intelligence AI Agents: Harness Scaling Across Models and Domains**

Main experiments:

```text
Claude Code
Codex
OpenCode
Hermes

HG0-HG3

PaperAgent
FundingAgent
JobAgent
CodeAgent
ResearchAgent
BusinessAgent
```

Primary scientific questions:

1. Does harness engineering increase measured capability?
2. Are gains retained?
3. Do improvements transfer across domains?
4. Does executor ranking change under different harnesses?
5. What mechanisms reduce human intervention?

## Paper 4 — Recursive and Discovery Agents

After HG0-HG3 are validated.

Topics:

```text
HG4 recursive improvement
HG5 discovery
sealed novelty tasks
longitudinal improvement
meta-improvement
```

## Paper 5 — General Agents for AI4Science

Only after the general architecture is validated.

Working question:

> Do independently validated general-agent intelligence mechanisms transfer to scientific research?

Applications:

```text
computational imaging
virtual cell
drug design
scientific simulation
other benchmarked AI4Science tasks
```

## Paper 6 — Autonomous Scientific Discovery

Long-term target.

Requirements:

```text
U5/U6 evidence
unknown scientific task
hypothesis formation
experiment design
new result
independent replication
paper generation
external scientific validation
```

---

# 24. Development Milestones

## Phase 0 — Freeze definitions

**Goal:** stabilize the measurement contract.

Deliverables:

```text
Unified Intelligence definitions
U0-U3 promotion rules
T0-T4 definitions
H0-H5 intervention policy
resource reporting standard
false-completion definitions
benchmark manifest schema
```

Success condition:

> Two independent readers can implement the benchmark definitions without asking the author for hidden interpretation.

## Phase 1 — UAB v0.1

**Goal:** implement U0-U3 benchmark tasks.

Minimum:

```text
6 domains
4 levels/bands where appropriate
multiple task families per domain
hidden/public verifier separation
retention suites
intervention logging
```

Recommended first implementation target:

```text
24-48 high-quality task families
```

Quality is more important than raw count.

## Phase 2 — HG0 Baselines

Run:

```text
Claude Code
Codex
OpenCode
Hermes
```

against the same UAB tasks.

Measure:

```text
completion
false completion
cost
latency
human intervention
failure taxonomy
```

No self-improvement yet.

## Phase 3 — HG1 Persistence

Implement:

```text
persistent state
memory
restart
checkpoints
provenance
separate acceptance
```

Run real restart experiments.

Publish a persistence benchmark result before calling the agents persistent.

## Phase 4 — HG2 Adaptive Learning

Implement:

```text
episode learning
verified lessons
procedural promotion
rollback
transfer tests
```

Primary experiment:

> Does verified experience improve later held-out tasks?

## Phase 5 — HG3 Self-Improvement

Implement:

```text
candidate harness modification
sandbox
frozen evaluation
independent promotion
regression testing
```

Test at least several improvement cycles.

## Phase 6 — Six Reference Agents

Package:

```text
PaperAgent
FundingAgent
JobAgent
CodeAgent
ResearchAgent
BusinessAgent
```

All use:

```text
same core
same HG definitions
same executor abstraction
different domain profiles/tools/benchmarks
```

## Phase 7 — Cross-Domain Transfer

Test whether generic harness changes transfer.

Examples:

```text
memory change
planner change
failure classifier
rollback mechanism
routing strategy
evidence verifier
```

This is a critical experiment for the "general intelligence" interpretation.

## Phase 8 — HG4/HG5 Research

Only after U0-U3/HG0-HG3 are stable.

Build:

```text
recursive improvement
meta-improvement evaluation
sealed discovery environments
novelty verifier
longitudinal change ledger
```

## Phase 9 — AI4Science Integration

After general validation:

```text
Unified Agent Core
       +
ResearchAgent
       +
scientific tools
       +
scientific benchmark contracts
       =
AI4Science Agent
```

At this stage integrate with:

```text
sarsi-worker
sarsi-ci
sarsi-ai4sci
scientific evidence stores
replicator
Judge
```

The AI4Science system becomes a specialized deployment of an independently validated agent-intelligence architecture.

---

# 25. Initial AI4Science Integration Strategy

Do not replace the general benchmark with a science-only benchmark.

Instead use two certification layers:

```text
Layer A:
General UAB certification

Layer B:
AI4Science-specific benchmark
```

Example:

```text
Agent earns:
U3-like capability on general UAB
        +
passes scientific research benchmark
        ↓
scientific U3 deployment claim
```

This prevents a specialized science agent from being mistaken for a generally high-intelligence agent.

---

# 26. Recommended First Build

The immediate practical build should **not** be all agents.

Recommended order:

```text
1. UAB schema
2. U0-U3 task definitions
3. CodeAgent benchmark
4. PaperAgent benchmark
5. FundingAgent benchmark
6. JobAgent benchmark
7. ResearchAgent benchmark
8. BusinessAgent benchmark
9. HG0 baseline runs
10. HG1 implementation
```

Why start with CodeAgent and PaperAgent?

```text
CodeAgent:
strong automatic verifiers already exist.

PaperAgent:
high-value long-horizon workflow and good evidence/provenance test.
```

FundingAgent and JobAgent then test transfer to very different domains.

---

# 27. Minimum Viable Publication Experiment

A practical first experimental paper could use:

```text
Executors:
4

Harnesses:
HG0, HG1, HG2, HG3

Domains:
6

Tasks:
~10-20 representative tasks/domain
with repeated runs where stochasticity matters

Human intervention:
H1/H2 standardized

Primary endpoints:
verified completion
false completion
cross-domain transfer
restart persistence
learning transfer
self-improvement gain
```

The experiment should explicitly distinguish:

```text
executor effect
harness effect
domain effect
executor × harness interaction
```

---

# 28. Suggested Statistical Structure

For task \(i\), executor \(m\), harness \(h\), domain \(d\):

\[
Y_{imhd}\in\{0,1\}
\]

for verified completion.

Possible model:

\[
\operatorname{logit}P(Y=1)
=
\beta_0
+
\beta_m
+
\beta_h
+
\beta_d
+
\beta_{mh}
+
u_i.
\]

Additional outcomes:

```text
false completion
wall time
token/API cost
human intervention count
retry count
regression count
```

Matched designs should be used whenever possible.

---

# 29. Scientific Claims to Avoid Early

Do not initially claim:

```text
"We built AGI."

"Claude Code is U4."

"Our agent is recursively self-improving"
after one reflection loop.

"Our system performs autonomous science"
because it wrote a paper.

"Mission autonomy"
when a human supplied all projects and tasks.
```

Prefer:

```text
"This frozen model-harness pair passed the U2
benchmark under T2/H2 at the declared reliability."

"HG2 improved held-out performance relative
to HG1 while retaining U0-U1 capabilities."

"The same harness modification transferred
across four of six domains."
```

---

# 30. Scientific Falsifiers

The research program should state how it could fail.

The central engineering hypothesis is weakened if:

```text
HG improvements do not improve frozen benchmarks;

improvements are domain-specific and do not transfer;

higher harnesses improve headline scores but increase false completion;

higher-level mechanisms cause lower-level regressions;

human intervention remains high;

the same effects disappear under hidden tasks;

benchmark items cannot be validated reliably;

agent-designed improvements only work when the agent
can influence the evaluator.
```

These are useful outcomes, not failed publications.

---

# 31. Key Research Hypotheses

## H1 — Harness Scaling

\[
P(\text{verified completion}|HG_{n+1})
>
P(\text{verified completion}|HG_n)
\]

under matched executor, task, resource and intervention conditions.

## H2 — Human Intervention Reduction

Higher harness generations reduce required \(H\) at fixed \(T\) and reliability.

## H3 — Retention

New capability does not materially degrade lower-level certified capability.

## H4 — Cross-Domain Transfer

At least some harness improvements developed in one domain improve performance in unrelated domains.

## H5 — Self-Improvement Validity

HG3 generates candidate architecture/workflow changes that outperform the frozen baseline on hidden evaluations more often than matched non-adaptive controls.

## H6 — Executor-Harness Interaction

The strongest base executor is not necessarily the strongest agent under every harness.

## H7 — Benchmark Centrality

Agent architectures that appear more sophisticated do not necessarily earn higher levels unless frozen benchmark performance improves.

---

# 32. Product and Research Relationship

The downloadable agents serve two purposes.

## Research purpose

They are reference implementations of intelligence mechanisms.

## Product purpose

Users can actually use:

```text
PaperAgent
FundingAgent
JobAgent
CodeAgent
ResearchAgent
BusinessAgent
```

This is useful because real usage produces:

```text
failure cases
longitudinal evidence
human intervention logs
tool-compatibility data
domain shift
resource data
```

However, product telemetry should not automatically become certification data.

Certification datasets must remain separately controlled.

---

# 33. Long-Term Vision

The complete progression is:

```text
Unified Intelligence theory
          ↓
Unified Agent Benchmark
          ↓
General Intelligence Harness
          ↓
Downloadable domain agents
          ↓
Cross-domain transfer
          ↓
Recursive improvement
          ↓
Discovery agents
          ↓
Mission agents
          ↓
AI4Science specialization
          ↓
Autonomous scientific discovery
```

The long-term objective is not merely to release useful agents.

It is to establish a repeatable scientific method for:

\[
\boxed{\text{engineering, measuring, and validating increasingly capable agents}}
\]

while keeping their acceptance criteria outside their own control.

---

# 34. Immediate Next Actions

## Priority 1 — Benchmark specification

Create:

```text
UAB_SPEC.md
TASK_MANIFEST.schema.json
INTERVENTION_POLICY.md
RESOURCE_POLICY.md
VERIFIER_POLICY.md
RETENTION_POLICY.md
```

## Priority 2 — U0-U3 benchmark matrix

Create a table:

```text
6 domains
×
U0-U3/T0-T3
×
multiple task families
×
H budgets
```

Label every row:

```text
BOUND
BAND_ONLY
SPECIFICATION_ONLY
```

Do not claim coverage where no runnable benchmark exists.

## Priority 3 — Build benchmark infrastructure

Implement:

```text
task loader
resource limiter
human intervention logger
artifact recorder
external verifier interface
hidden-test interface
run manifest
result schema
```

## Priority 4 — Baseline executor adapters

Implement a unified interface for:

```text
Claude Code
Codex
OpenCode
Hermes
```

## Priority 5 — Run HG0

Freeze and publish the baseline.

## Priority 6 — Build HG1

Persistence is the first major engineering step.

## Priority 7 — Release the first two reference agents

Recommended:

```text
CodeAgent
PaperAgent
```

Then add:

```text
FundingAgent
JobAgent
ResearchAgent
BusinessAgent
```

---

# 35. Final Recommended Strategy

The project should proceed in this order:

```text
STEP 1
Keep Unified Intelligence independent from AI4Science.

STEP 2
Freeze the benchmark framework before building agents.

STEP 3
Build UAB v0.1 for U0-U3 across several unrelated domains.

STEP 4
Create a vendor-neutral Unified Agent Core.

STEP 5
Add Claude Code, Codex, OpenCode, Hermes and other executors.

STEP 6
Develop HG0-HG3 incrementally.

STEP 7
Measure every mechanism against frozen benchmarks.

STEP 8
Release PaperAgent, FundingAgent, JobAgent, CodeAgent,
ResearchAgent and BusinessAgent as downloadable systems.

STEP 9
Test whether the same intelligence mechanisms transfer
across domains.

STEP 10
Only after the architecture is validated, integrate it
into the AI4Science stack.

STEP 11
Develop HG4 recursive improvement and HG5 discovery.

STEP 12
Use the validated U5/U6 architecture for increasingly
autonomous scientific research.
```

The central methodological principle is:

> **Define intelligence first. Freeze the benchmark second. Engineer the agent third. Let the benchmark decide whether intelligence actually increased.**

And the longer-term relationship to AI4Science is:

\[
\boxed{
\text{General Agent Intelligence}
\rightarrow
\text{validated mechanisms}
\rightarrow
\text{AI4Science specialization}
}
\]

rather than:

\[
\text{AI4Science-specific engineering}
\rightarrow
\text{assume general intelligence}.
\]

This separation should make both the Unified Intelligence program and the later AI4Science program scientifically stronger.
