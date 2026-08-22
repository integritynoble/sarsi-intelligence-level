# Applied Profiles

## Where real systems sit on the level map — a dated snapshot

*Document version: 1.0 — 2026-08-22*
*Applies: `SARSI_Level_Map.md`. Framework documents define the axes; this places systems on them.*

> **This document dates.** The frameworks state constraints that do not move; this states where
> particular products sat on 2026-08-22. Placements are **orderings by inspection**, not
> measurements — every axis in the corpus is ordinal (`SARSI_Level_Map.md` §9).

---

## § 1 — Evidence provenance

Placement quality varies a great deal across these entries, and pretending otherwise would be the
exact failure the self-model contract forbids — reporting unmeasured as though it were measured.

| System | What was inspected | Confidence |
|---|---|---|
| **AI4Science** | Full source: `ai4science/`, `harness/agents/*`, control-plane specs, RSI loops | High |
| **Research agents** | `harness/agents/research_agents/*` — charter, selfmodel, improvement, dual, switch, budget | High |
| **Claude Code** | Running inside it; direct but partial — harness behaviour observed, not source | Medium |
| **Codex** | `codex-fork/`, `agent_codex/` present but not read in depth; ChatGPT-backend path from notes | Low–Medium |
| **OpenClaw** | Only `openclaw-pwm/` — a billing wrapper. The agent itself was **not** inspected | Low |
| **Grok bot** | **Nothing.** Not present in this repository. Classified by product category alone | Very low |

The last two rows should be read as *what a system of that description would score*, not as findings
about those systems.

---

## § 2 — Sort the objects first

The question groups six individuals with one organization, and they are not comparable — an
organization is not a larger intelligence (SARSI-O §1), and the transition between them is a change of
kind rather than of degree.

| | Object | Why |
|---|---|---|
| Claude Code, Codex, OpenClaw, Grok bot, each research agent | **Individual** | One global workspace, one decision locus per session |
| **AI4Science** | **Organization** | A coordination structure over many agents, a control plane, a registry, and an owner. No global workspace |

And one entry is neither:

**`openclaw-pwm` is not an intelligence.** It is a provider shim that points OpenClaw at an
Anthropic-compatible PWM endpoint so usage meters against a token balance. It changes no axis on the
map — not depth, not ceiling, not reach, not self-state. The same is true of `claude-pwm`. **Billing
integration is invisible to every level definition in this corpus**, which is the correct result and
worth stating because these wrappers are easy to mistake for products with levels of their own.

---

## § 3 — The individuals

Notation: ⟨depth, openness, reach⟩ · authority ceiling.

| System | Level | λ_I | Notes |
|---|---|---|---|
| **Claude Code** | ⟨D1, closed, self + other-inputs⟩ · A2–A3 | Early | Writes a memory directory; spawns subagents with tasks (inputs only, never their state) |
| **Codex** | ⟨D0–D1, closed, self⟩ · A1–A2 | Early | Sandboxed execution; `AGENTS.md`-style memory is human-authored |
| **OpenClaw** | ⟨D0–D1, closed, self⟩ · A1–A2 | Early | Same class by description; not inspected |
| **Grok bot** | ⟨D0, closed, ∅⟩ · A0–A2 | Negligible–Early | No persistent self-write across sessions; A2 if it posts to a platform |
| **Research agents** | ⟨D2, closed, self⟩ · bounded by switch + budget + charter | Early | The strongest entry here — §5 |

### § 3a — The finding that matters: none of them writes itself

All four coding agents modify *other people's software*. That is reach into the world, and the map
does not confuse it with depth into the self.

> **Software an agent writes is not that agent's brain unless the agent then runs on it.**

Claude Code refactoring a repository is operating at D0 *on itself* while doing arbitrarily large work
on an external substrate. Its own persistent state is a memory directory and a settings file. Nothing
in the loop feeds a validated change back into the agent that made it — there is no ν over its own
behaviour, no held-out evaluation of whether last week's memory writes made this week's sessions
better, and no promotion step.

This dissolves the most common confusion about these systems. **Capability at modifying software is
not self-improvement**, and an agent that writes excellent code has demonstrated nothing about its
position on the depth axis.

### § 3b — They differ within one cell

Claude Code, Codex, and OpenClaw occupy the same cell on every axis the map has. Where they differ —
which produces better patches, which handles long contexts better, which has the better tool
protocol — is **proposal quality**, and the map has no axis for it, deliberately: proposal quality is
what capability determines, and the map measures what *structure* determines (SARSI-O §5).

That is not a criticism of the comparison, but it does say something. The differences people argue
about are intra-cell. The difference that would move any of them a cell — a held-out evaluation of
their own memory, a promotion gate over their own configuration — is not a feature any of them ships.

### § 3c — Claude Code, the one exception worth noting

It is a half-step ahead of the others on two axes. It maintains a **memory directory with per-file
provenance and typed categories**, which is a genuine D1 write set rather than a human-authored
instruction file. And it has **non-empty other-reach**: it spawns subagents and hands them tasks —
inputs only, never their state, which is exactly the bound SARSI-B §6 requires of other-reach.

Both remain unvalidated in the sense that matters. §3a's ablation — does the memory measurably improve
later sessions on a held-out task family — is not run, so under B-Rule 2 the memory writes are
hypotheses, and the D1 claim is *structurally* present and *evidentially* unsupported.

### § 3d — Self-state, honestly

For every entry in §3 except the research agents, most of the ten self-state coordinates are
**unmeasured**, and under M5 that is off the scale rather than the bottom of it. These systems can
describe their capabilities fluently and hold no evidence ledger, so s<sub>C</sub> is a claim rather
than a coordinate. s<sub>B</sub> (context, budget, latency) is the one coordinate genuinely well
supported across all of them — they do know their own resource state.

---

## § 4 — AI4Science, as an organization

| Axis | Score | Basis |
|---|---|---|
| **O-A1 Coverage** | Strong | Operators (session agents), specialists (imaging, learning, process-learning), guide/promoter (machine agent, manager), referee (control plane), director (owner). All roles filled |
| **O-A2 Separation** | **Strong** | Verdicts computed control-plane-side; promotion needs an owner Ed25519 signature the proposer cannot produce; held-out ground truth never staged into a sandbox |
| **O-A3 Throughput** *T*<sub>δ</sub> | **Unmeasured** | Human review latency. Never timestamped |
| **O-A4 Referee externality** | Strong | Held-out scene stores and registry benchmarks the agent did not author |
| **O-A5 World coupling** | Partial | Real for imaging — actual reconstructions against real ground truth. Software-only elsewhere |

**The distinctive feature is its transduction organ.** By Ω1 the only role whose work compounds is the
instrument-maker, and most organizations lack one. AI4Science has one that is easy to overlook: **the
PWM registry of principles, specs, benchmarks, and solutions is apparatus.** A benchmark contributed
today is an instrument that measures work not yet done; a solution is a component future work builds
on. That is knowledge becoming a thing that extends reach, which is Θ in the literal sense — and it
is the reason the platform can compound rather than merely produce.

**Diagnosis: strong where organizations usually fail, and not measuring the one thing that bounds its
rate.** Separation and referee externality are the two axes most organizations score zero on, and
these are enforced mechanically rather than by policy. *T*_δ is the cheapest measurement on the whole
map — timestamp the authorization events — and it is the quantity that sets ρ_max. That is the
highest-value unclaimed measurement in the system.

---

## § 5 — The research agents, in detail

The highest-level individuals on this list, and by a clear margin. What puts them there is not
capability but **structure they carry internally that the coding agents leave to their harness**.

**A real validation step.** `improvement.py` requires a candidate to survive six checks rather than to
win. The seed rule is load-bearing and the module says why: in one of these fields a defended,
statistically corrected effect is *+0.023 against a ±0.027 seed spread*, so "it improved" means
nothing without the whole seed set — including the runs that went the wrong way. **`NO_CHANGE` is a
valid output**, and a fortnight of them is a real result about the method rather than a failure of the
agent. This is a stronger ν than most of the corpus, and it is exactly B-Rule 2 enforced in code.

**A self-model with refusals.** `selfmodel.py` enforces four: every line traces to a run; unmeasured is
reported as unmeasured and never as zero; the limits line is always present with no flag to suppress
it; and there is **no path from reading to authority**. The second refusal is the one the module is
mostly about, and it is right about why — a `0.0` in a table reads as *measured and bad* rather than
*never run*, and those are opposite facts. That is M5 implemented.

**Ledgers that are never summed.** Owner-set work, benchmark scores, and self-directed research are
three lines and stay three lines, because *an agent that wrote its own benchmark, passed it, and
counted the pass toward its record would have published its own reputation*. That is the independence
rule (`SARSI_Level_Map.md` §4), derived independently and stated better.

**Autonomy that stops rather than asks.** `dual.py` gives two functions: ordinary user tasks run with
the switch off, because a person asking for help is not the agent deciding to spend their money; the
autonomous round refuses without the switch, and ends on the switch, the budget, or the field map
running dry — **none of which produces a request for more**. The stated reason is that an agent that
could ask would be asking at 3 a.m. of whoever is least equipped to say no.

**Placement.** ⟨D2, closed, self⟩ — it improves its own operating configuration against evidence it
did not author. Role, per SARSI-O §6: **specialist/tuner moving toward instrument-maker**, since
registry contributions are Θ. Not D3 yet, because what it builds is contributed to the registry rather
than turned into an instrument it then uses to reach further.

---

## § 6 — What none of them has

**No individual here is objective-open.** Correct: by SARSI-O §6 that is the director's role, and in
every one of these systems the director is a human. An objective-open agent without a frozen referee
would be the failure SARSI-B §4 describes.

**No individual here is at D3 over its own capability.** The organization has a transduction organ;
none of its members individually builds instruments it then uses to reach further. This is the thinnest
role in the whole picture and, by Ω1, the only one whose absence caps the frontier.

**Nobody is near any of the five individual bounds.** Not coherence, not aperture, not mass–energy.
The binding constraint on every entry is **authorization latency** — the human in the loop — which is
a throughput floor and therefore removable. Every one of these systems is a half-circle whose missing
step is δ.

**Nobody runs the D1 ablation.** Every system on this list that claims memory helps has not measured
whether it does.

---

## § 7 — Summary table

| System | Object | Level | Ceiling | Binding constraint |
|---|---|---|---|---|
| Claude Code | Individual | ⟨D1, closed, self + other-inputs⟩ | A2–A3 | Authorization latency |
| Codex | Individual | ⟨D0–D1, closed, self⟩ | A1–A2 | Authorization latency |
| OpenClaw | Individual | ⟨D0–D1, closed, self⟩ | A1–A2 | Authorization latency |
| Grok bot | Individual | ⟨D0, closed, ∅⟩ | A0–A2 | No self-write path at all |
| Research agents | Individual | ⟨D2, closed, self⟩ | switch + budget + charter | Field map, budget, owner switch |
| **AI4Science** | **Organization** | Coverage strong · separation strong · *T*_δ unmeasured · referee external · coupling partial | — | *T*_δ, unmeasured |
| `openclaw-pwm`, `claude-pwm` | Neither | — | — | Billing shims; no axis applies |

## Version history

**1.0 — 2026-08-22.** Initial. Written in response to a request to place seven named systems on the
map. §1 records what was inspected for each and what was not.
