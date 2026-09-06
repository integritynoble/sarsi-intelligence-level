# The HIL Index — one number per model, and the first that goes down when a model bluffs

**HIL-Index v1** is the HIL-Score of a *bare* model across HIL-Bench's reference harness ladder: the model is called
through its own API with two read-only tools and must answer each item with one JSON object; the benchmark
materializes the answer into the deliverable files and scores it with the same hidden verifiers agents are scored
with. Three rungs — HG0 (one attempt), HG1 (a registered acceptance criterion, a failing delivery held back), HG2
(snapshot, restore, retry with the failed check named) — each read in every coordinate the framework defines for an
individual: cognition C0–C4 with named traps, self-awareness (grounded state; a solvable/blocked twin pair),
organization O0 (routing with a substantive verifier entry), and delegation across six domain families plus the
four Core-H items whose plausible wrong method a competent model actually takes.

    HIL-Index = 0.55 · AUC(HG0..HG2) + 0.35 · Ceiling + 0.10 · Harnessability

with HLIS at each rung a geometric mean over the coordinates present, and the delegation surface priced by the
delivered-outcome primitive: `P(delivered ∧ verifier pass) − ρ · P(false completion)`, ρ = 1. A delivered wrong
answer costs a full unit; a declared inability is held back for free.

## Why this index and not another aggregate

| | Artificial Analysis Intelligence Index | HIL-Index |
|---|---|---|
| unit | a model, through the evaluator's harness | a bare model, through three *published* harnesses — the rung is part of the number |
| what a wrong answer costs | nothing beyond the missed point | ρ = 1: a bluff scores below a refusal |
| refusing when the task is impossible | not measured | measured (the twin pair; the unsatisfiable specification) |
| memory, learning, organization | not measured | M0/I0 by construction for a bare model, stated; O0 measured; the same items measure an *agent* in every coordinate |
| how much a harness adds | not measured | Harness Gain and Harnessability, on the curve |
| items | fixed corpora | seeded generators with computed keys; a private split derived from a withheld salt whose SHA-256 is published |
| levels | none | every level is a contrast a program checks (`LAWS.md`) |
| cost | run by the index's authors | ~100 calls, minutes, cents; anyone can reproduce a row with one command |

## Reproduce a row

    python3 -m hilbench index --label <model> --root <fresh dir> \
        --base https://api.example.com/v1 --key $KEY --model <name>      # OpenAI-compatible
    python3 -m hilbench index ... --api anthropic --base https://api.anthropic.com --key $KEY --model <name>

Three seeds per family (34 + 12 episodes per rung); the record carries every episode, the evaluator block and
`index.json`. A **public** row is self-reported; a **certified** row was run by someone who did not build the model,
on the private split (`--split private --salt-file ...`), and says so.

## Leaderboard (HIL-Index v1)

| Model | Endpoint | Split | HIL-Index | HG0 / HG1 / HG2 | Gain | False-completion rate | Decline rate | Bare profile at HG0 | Evaluator |
|---|---|---|---|---|---|---|---|---|---|
| DeepSeek `deepseek-chat` (V4-flash) | api.deepseek.com/v1 | public, 3 seeds/family | **32.3** | 35.9 / 35.9 / 35.9 | 0.0 | 0.00 | 0.05 | C3 · SA1 · O0 · T1 · U0 | author (built the instrument, not the model) |
| DeepSeek `deepseek-chat` (V4-flash) | api.deepseek.com/v1 | **private**, 12 at T1 | **35.2** | 31.3 / 39.5 / 39.2 | 8.2 | 0.02 | 0.02 | C3 · SA1 · O0 · T1 · U0 | author |
| Qwen 3.8 27B `qwen3.8:27b` | physicsworldmodel.org/qwen/v1 | public, 3 seeds/family | **30.3** | 26.1 / 34.9 / 31.3 | 8.8 | 0.08 | 0.06 | C3 · SA1 · O0 · T0 · U0 | author |
| Claude (bare, Anthropic API) | api.anthropic.com | — | *pending an API key* | | | | | | |

Pair readings are **not** index rows — a pair's HIL-Score is a property of model *and* harness — and are reported
separately in the paper: Claude Code default 37.3, DeepSeek-through-Claude-Code 83.2 (`llm-harness`).


## Two scales, one construction

The rows above are the **bounded** v1 composite (0.55·AUC + 0.35·Ceiling + 0.10·Harnessability, in [0, 100]). The
index paper's headline is an **unbounded, difficulty-calibrated latent** scale: for each evidence unit
P(Y = 1) = σ(θ_md − b_i), θ_H = Σ w_d θ_md, HILIndex = 100 + 10·θ_H. `python3 -m hilbench latent` fits it over every
bare-model record in `records/` (current-fit diagnostic: anchors are not ratified, so the scale moves as rows are added;
a frozen historical index is published only after ratification). With few rows most items carry no between-model
variance and are dropped, which the output reports; the latent scale becomes meaningful with a weak-to-frontier
population, which is the roadmap's step 7. Output: `records/latent_public.json`.

## Versioning

The index is named by its benchmark version. Items, weights, ρ and the gate are frozen inside a version; a change
re-versions every row; the retired private salt is revealed at each boundary so any past certified row can be re-run.
Saturation moves the research frontier, not the ruler: a version whose top rows tie is replaced by one with headroom
(Core-H was that replacement for v0.2), never by re-weighting.

## What it is not

Not a knowledge test, not a coding test, not a rule-induction test in the ARC sense (C4/C5 are one item family each),
not a certification (a public row is a reading), and not comparable across versions.
