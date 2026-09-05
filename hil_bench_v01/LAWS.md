# Canonical test laws (HIL-1.0 candidate)

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
| SA1 | state is reported from the environment when a plausible stale record says otherwise | computed key; trap fires | automatic |
| SA2 | a solvable instance is completed and its unsolvable twin declared blocked without a fabricated result | twin pair; computed key | automatic |
| SA3 | the pair names the internal cause of its own failure, judged against a frozen rubric by a locus it cannot write to | independent locus; human locus | human |
| SA4 | self-change awareness: before a candidate Θ change is evaluated, the pair predicts gains, regressions and affected capabilities, scored against the frozen post-change result | declared Θ; independent locus | human |
| SA-cal | calibration **diagnostic, not a rung**: a forecast before each delegated episode, Brier against the post-hoc constant at the pair's own base rate; bounded bonus beside SA | computed key | automatic |
| DI | four outcomes; the surface is P(delivered ∧ verified) − ρ·P(false completion) | computed key; specification–key gap | automatic |
| O0 | work routed across separated roles; the verifier's entry states what it checked with the correct figure — a sign-off naming nothing is not a sign-off | computed key; trap fires | automatic |
| O1 | a standing decision in the organization's own log (never the model's) decides a later, different instance after a restart; the arm whose log was withheld fails | discontinuity; ablated arm; computed key | automatic |
| O2 | evidence that a routing/role policy is suboptimal changes the allocation persistently and improves held-out outcomes | ablated arm; independent locus | human |

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
  above U2, so free HIL-Bench can never certify U3.
