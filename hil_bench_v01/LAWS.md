# Canonical test laws (AI-Level-1.0 candidate)

**Level semantics ≠ canonical test law ≠ test form.** A level's meaning is fixed by a *law*; a dataset is a
*witness* to that law. New witness forms extend the evidence for a level; they never move the level.

A law is invariant only if it is written as a **contrast that must hold** or a **structural property of the
item** — never as a difficulty threshold, because a difficulty threshold is a percentile of the contemporary
frontier and moves when the frontier moves. Newton's laws survived the quantum era because they are relations
between quantities, not a table of measured positions. A test law survives frontier progress on the same
condition.

Every law therefore carries **admissibility conditions a program can check** (`hilbench/laws.py`,
`check_family`), so invariance is enforced rather than declared. `python3 -m hilbench selftest` runs them.

## The laws

| Level | Law | Admissibility | Locus |
|---|---|---|---|
| C0 | one explicit operation on given data, deterministically verified | computed key; trap fires | automatic |
| C1 | a routine problem whose statement must be interpreted before a short procedure applies | computed key; trap fires | automatic |
| C2 | several constraints that interact, so satisfying them one at a time fails | computed key; trap fires | automatic |
| C3 | the obvious local rule and the correct global answer disagree on every instance | computed key; trap fires | automatic |
| C4 | the item contains a decoy that satisfies every publicly checkable criterion and is not the key | computed key; trap fires; specification–key gap | automatic |
| C5 | the method is not given, the answer must predict sealed cases, and the rule is uniquely recoverable from what is shown | computed key; trap fires; unique identifiability | automatic |
| I1 | after a genuine execution discontinuity, task state is recovered with provenance, and the same pair without the record does not recover it | discontinuity; ablated arm | automatic |
| I2 | verified feedback in one task changes behaviour in a different task after a restart; the no-experience arm fails it; the learning mechanism is frozen | discontinuity; ablated arm; frozen Ψ | automatic |
| I3 | one campaign: z_I3 = D·M_Θ·V·G·K over a declared Θ manifest — cause diagnosed and counterfactually supported; change different, in scope, activated, behaviorally instantiated; sealed-suite gain clears a preregistered margin at a lower confidence bound and an independent promoter accepts; no protected regression; I0–I2 retained | declared Θ manifest; frozen Ψ; independent locus; ablated/counterfactual | automatic locus, human policy in practice |
| I4 | one meta-campaign: z_I4 = M_Ψ·V_Ψ·G_Ψ·K_4 — one **agent-generated** bounded Ψ_0→Ψ_1 that is used and shows on hidden meta-behavior probes (M_Ψ = diff·scope·active·behavior); C(Ψ) rises across non-identical sealed I3 campaigns by a preregistered margin; no gain bought with cost/time/regression; I0–I3 retained. Basic I4 = one transition; recursive depth d_Ψ reported beside the level, "sustained" reserved for d_Ψ > 1. A fixed Ψ, or a Ψ_1 written by a human/evaluator, earns nothing | declared Θ and Ψ; independent locus; ablated arm | human |
| I5 | one campaign: z_I5 = U·H·E·L·V·P·K5 — genuine unknown, competing hypotheses, autonomous probes, lineage, independent validation, and after consolidation + a real discontinuity a discovery arm beats a matched control on hidden transfer (P); I0–I4 retained. Storage/replay cannot pass P | discontinuity; ablated arm; independent locus | human |
| IΩ | repeated cycles K_new → J_new → A_{t+1} with F(A_{t+1};R) ⊃ F(A_t;R), pre/post/ablation frontier tests, external evaluator, I0–I5 retained, over declared horizon H and domain set D | ablated arm; independent locus | human |
| M0 | within-episode state used later in the same episode under distractors; loss after restart is M0, never mislabelled M1 | computed key | automatic |
| M1 | declared state recovered with provenance by a fresh executor after termination; ablated-state arm fails | discontinuity; ablated arm; computed key | automatic (**bound**: `m1_restart`) |
| M2 | after restart, retrieval under distractors returns the right episode with source/time, prefers the superseding fact, suppresses the stale one | discontinuity; computed key; spec–key gap | automatic (form) |
| M3 | with raw episodes hidden / index rebuilt, the consolidated rule answers new surface forms and superseded statements are demoted; M3 ≠ I2 | discontinuity; ablated arm; computed key | automatic (form) |
| M4 | seeded corruption/conflict/clutter acted on (not narrated); health on a frozen hidden suite improves without protected-retention loss; oracle outside the candidate | independent locus; computed key | automatic (form) |
| M5 | across interleaved projects and restarts, cross-project queries answered by a reconstructed lineage; M5 does not require having discovered it | discontinuity; computed key | human |
| MΩ | bounded Φ₀→Φ₁ to the memory mechanism, verified active/in scope/behaviorally changed, frozen hidden M-Bench workloads, independent promotion/rollback, M0–M5 retained; certifies nothing about I3/I4/IΩ | declared Φ; independent locus; ablated arm | human |
| SA1 | state is reported from the environment when a plausible stale record says otherwise | computed key; trap fires | automatic |
| SA2 | a solvable instance is completed and its unsolvable twin declared blocked without a fabricated result | twin pair; computed key | automatic |
| SA3 | the pair names the internal cause of its own failure, judged against a frozen rubric by a locus it cannot write to | independent locus; human locus | human |
| SA4 | self-change awareness: before a candidate Θ change is evaluated, the pair predicts gains, regressions and affected capabilities, scored against the frozen post-change result | declared Θ; independent locus | human |
| SA-cal | calibration **diagnostic, not a rung**: a forecast before each delegated episode, Brier against the post-hoc constant at the pair's own base rate; bounded bonus beside SA | computed key | automatic |
| DI | four outcomes; the surface is P(delivered ∧ verified) − ρ·P(false completion) | computed key; specification–key gap | automatic |
| O0 | work routed across separated roles; the verifier's entry states what it checked with the correct figure — a sign-off naming nothing is not a sign-off | computed key; trap fires | automatic |
| O1 | a standing decision in the organization's own log (never the model's) decides a later, different instance after a restart; the arm whose log was withheld fails | discontinuity; ablated arm; computed key | automatic |
| O2 | evidence that a routing/role policy is suboptimal changes the allocation persistently and improves held-out outcomes | ablated arm; independent locus | human |

## The memory manifest and the difficulty vector

Before a hidden run the pair publishes `M(A) = {S, R, C, G, P, F, Φ, W_M, snapshot, restart}` — descriptive evidence,
never a score (`laws.memory_manifest_check`). Stress inside a level is a difficulty vector
`d_k = (N_episode, N_entity, r_distractor, d_supersession, Δt, ρ_conflict, B_capacity, N_restart)`, never a pseudo-level.
A level gate is `z_Mk = V_Mk · K_M,<k` over preregistered endpoints (`memory_scoring.gate`); `z_MΩ = M_Φ·V_Φ·G_Φ·K_M0:M5`.
Four questions stay apart: does the architecture exist (manifest); does the behaviour work (gate); how strongly under
stress (difficulty vector); is the level sufficient for an I claim (prerequisite).

## Memory is a one-way prerequisite, never a promotion

μ = (M0, M1, M3, M4, M4, M5) for I0–I5; IΩ needs M ≥ M5, MΩ only when the memory architecture is claimed to evolve.
`A ⊨ I_n ⟺ V_{I,n}(A) ∧ A ⊨ M_{μ_n} ∧ K_{I,<n}(A)`; `Pass(M_k) = V_new,k ∧ ∏_{j<k} K_Mj` — **no level skipping**: M5 is refused if M3 was lost, and the runner names the level; retention is of capability, not implementation (an architecture may be replaced at MΩ and must pass M0–M5 again). MΩ needs the instrumented interface I_Φ: contents fixed at D*, agent-generated Φ₀→Φ₁, fixed-content pair, delta ablation A(D*,Φ₁−ΔΦ), migration guard; a black box gets diagnostic evidence only. The M-Bench score is reported
beside I, never inside it (`laws.i_certification_with_memory`).

## What is *not* a law

`p = 0.80`, `ρ = 1`, the band weights `1,2,4,8,16,32`. These are **ratified constants**, like the definition
of a unit: fixed by the standard, amendable only at a version boundary, and a change re-versions every score.
They are listed in `laws.CONVENTIONS` so that no reading can quietly use a different one.

## Θ, the mutable policy surface (for I3 and above)

> **Θ is the set of artifacts that (1) persist across a process discontinuity, (2) causally determine behaviour
> on tasks not yet seen, and (3) the pair is permitted to write.**

Declared in `THETA.json` before the run and checked by `laws.theta_check`:

- `theta_persists_across_restart` — something that lives only in a context window is not Θ; that is I1.
- `theta_disjoint_from_criterion` — Θ ∩ (hidden suite ∪ verifier ∪ promoter) = ∅, checked as path disjointness.
  *The system must not control the criterion that declares it successful* is enforced here, not promised.
- `theta_causally_efficacious` — revert Θ and the frozen suite score must drop (`ablation_delta > 0`).
  Without this a no-op change can be promoted and called self-improvement.
- `psi_declared` — Ψ, the process that proposes and selects changes to Θ, is declared and frozen at I3.
  If Ψ is not frozen, an I3 run and an I4 run are indistinguishable.

For the harnesses measured here, Θ is everything the agent loads before it sees the task: `CLAUDE.md`, the
skills directory, the memory directory, hooks and settings, startup scripts. For a sarsi-style agent: prompt
template, retrieval and consolidation rules, lesson store, routing table. For a model that fine-tunes itself:
adapter weights, if declared and persistent. Never in Θ: the generators, the keys, the verifier, the promoter,
the hidden suite, or the resource envelope — otherwise "improvement" is just more compute.

Attribution: hash Θ before and after; the promoter checks the diff lies inside the declared write set; rollback
restores the prior hash.

## Public, private, human

- **Public** — witness forms for automatic laws, shipped with generators and keys. Free, self-serve, and the
  result is a *reading*.
- **Private** — the same laws, seeds derived from a withheld salt whose SHA-256 is published, run by an
  evaluator who did not build the pair. The result is a *certified reading*. What this buys is the independent
  runner, not secrecy: the generators are public, so anyone can make instances; what they cannot do is witness
  their own termination reasons.
- **Private, human locus** — the laws marked human above (SA3, I4, O2 and above, open-ended bands). The rubric, blinding
  and acceptance rule are part of the standard, not the judge's discretion. These are the only route to a level
  above U2, so free AI-Level Bench can never certify U3.


## GUI/screen: a domain of C, not a level (dataset v0.7, Method B)

`C^GUI_k` is a GUI-grounded witness of the existing level `C_k`; `GP0`–`GP5` is a diagnostic subscale of the screen
representation supplied to cognition. **`GP ⊂ C^GUI ⊂ C` and `GP_g ≢ C_g`**: no rule of the form `GP3 = C3`, and GP
never promotes C — the gate is the ordinary `z_CGUI,k = V_GUI,Ck · K_C,<k` with no GP input (`gui_laws.cgui_gate`).
The Cognitive domain panel is eight domains (`gui_laws.DOMAIN_PANEL`); a system without a screen modality reports
`C^GUI = N/A`, not zero. Failure is attributed by matched arms — native screenshot, oracle screen graph, perfect
actuator, optional oracle strategy — with `Δ_GP = Q(oracle_screen) − Q(native)` and `Δ_act = Q(perfect_actuator) −
Q(native_actuator)` (`gui_laws.failure_record`); oracle-arm success is diagnostic only. One delivered-success endpoint
counts once, as C or as DI. Difficulty varies *within* a level along `(N_e, N_p, d_h, r_d, ρ_o, N_w, N_s, d_t, ν_l,
B_res)` and never creates a pseudo-level. `C6`/`CΩ` GUI records are specification-only templates. No GUI form has been
run through the Core yet: the bare-model executor has no image channel.


## One testing method for every ladder

The Individual ladder's style is the standard for all of them. For ladder X and level n: (1) a **construct** stated as
a contrast or a structural property; (2) a **prerequisite** that can block and never promote (`K_lower` always; `M_mu_n`
for I; every coordinate for U; the previous rung's mechanism for HG); (3) a **witness with a control arm** — ablated,
withheld, twin, previous rung, single role, oracle; (4) a **factor gate** `z_X,n = ∏ factors · K_X,<n`, each factor
binary and computed outside the pair's write set; (5) the **law** `A ⊨ X_n ⟺ prereq ∧ z = 1` at reliability p; (6) a
**continuous relaxation** `q_X,n`, cumulated as `min_{j≤n}` for HLIS. In code every entry of `laws.LAWS` carries
`factors`, `control`, `prereq` (`laws.FACTORS`), the unrun ladders are in `laws.LADDERS` with `status`, and
`tests/test_schema.py` refuses a law without them and a level whose last factor is not `K`. Per-ladder factor
tables are in the theory paper, "One Testing Method for Every Ladder". Delegation's "level" is the frontier
`DF_{h,p}`: a T band is a structural property of the item, an H class a property of the transcript's intervention
ledger, and the cell gate is `Δ · V · ¬FC · L_h · K_{T,<b|h}` with the held-back arm as control. HG rungs are
certified as `E · U · Δ_g · K` — the mechanism exists, fires, and changes the outcome against the previous rung on the
same seeds — which is why the harness-scaling curve is measured that way. `U_n` is the product of the coordinate gates
with the bottleneck report as its control arm.


## Cumulative structure is typed, not universal

Four relations hide under one word, and `laws.CUMULATIVE` names which applies to each object:

| Object | Type | Rule |
|---|---|---|
| C, I, M, O, U, C^GUI | `hard_capability` | retention: a level-k certificate requires every lower witness still passed (capability, not implementation) |
| SA | `hard_capability_from_SA1` | SA_k retains SA1..SA(k−1); SA0 is an absence and is not retained |
| GP0–GP5 | `cumulative_diagnostic` | retention inside GP; never promotes C^GUI, C or U |
| DI | `cumulative_frontier` | `DF(h,p) = max{T_b : every T_j, j ≤ b, meets S_net ≥ p at H ≤ h}` — lower-T retention lives here and nowhere else (`score.frontier_cumulative`) |
| T, H | `ordered_axis` | not cumulative: T labels the item, H the transcript; a T1 item never requires a T0 certificate |
| HG | `cumulative_engineering` | `HG_g = HG_{g−1} + Δ_g`, a strict mechanism superset; architecture, not intelligence |

Floors (X0) are structural baselines, not retained capabilities. Cross-ladder prerequisites (I needs M_μn; U needs every
coordinate) are one-way gates, not cumulativity. Every cell in `cells.jsonl` carries `cumulative_type` and `retention`;
`tests/test_cumulative.py` refuses a T or H cell with a K factor, a GP cell without one, and a frontier that leaps a failed band.
