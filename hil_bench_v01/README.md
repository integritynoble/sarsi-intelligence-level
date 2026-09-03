# HIL-Bench v0.1 — the Harness Intelligence Level benchmark

One instrument, two subjects. An **agent** is measured as the frozen model–harness pair it is and gets
a per-coordinate profile `[C, I, O, T, H, SA]` with `M` beside `I`, the gated Unified level `U*`, and
the continuous pair score **HLIS**. An **LLM** is measured through the reference harnesses HG0, HG1
and HG2 built into this package and gets `HLIS_DI` per rung and from them **HIL-Level, HIL-AUC,
HIL-Ceiling, Harness Gain and HIL-Score**. Framework: Unified Intelligence v2.4 (`../unified_v24`).

Design constraints, in the order they were given: simple; fast; cheap; real; public and private splits
in the manner of ARC-AGI. The Core run is about thirty executor calls, no human in the loop, every
episode in its own process group under an enforced limit, and every family seeded with a computed key.

## What the Core measures

| coordinate | family | calls | what it takes to pass |
|---|---|---|---|
| C0–C3 | `c_items` (computed keys; the wrong method per band is named and shown to fail) | 8 | exact answer at ≥ 0.8 per band, cumulative |
| M1 (→ I1) | `m1_restart` (two episodes, process terminated between, episode 1 removed; ablated floor) | 3 | recall with provenance after the restart AND failure of the ablated arm |
| I2 evidence | `learning_t2` from UAB v0.1 (paired episodes; ablated floor) | 5 | transfer = pass(B\|A) − pass(B\|ablated) = 1 |
| SA1, SA2 | `sa_probes` (grounded state vs a stale note; a solvable/blocked pair) | 6 | grounded report; block without fabricating, complete the solvable twin |
| SA4 | blind forecast before every T·H episode | 12 | Brier ≤ constant-forecast Brier |
| T·H at H0 | the six UAB domain families (T0 ×5, T1 ×1), delivered-outcome primitive | 12 | frontier `F_A(H0, 0.8)` and `A_DI` net of false completions |
| O | omitted for an individual pair and named as omitted | 0 | (organizational suite: ablation) |

SA3 (naming the mechanism of one's own failure) and the organizational suite are specification-only in v0.1.

## LLM mode: the reference harnesses

Same six families, same seeds, under HG0 (one attempt, no acceptance), HG1 (one attempt; the harness's
**public checks** — criteria derivable from the visible specification, never from the key — run and a
failing deliverable is held back) and HG2 (snapshot before each attempt, restore on rejection, up to
three attempts with the failed public check named). The hidden verifier scores what was delivered.

```
python3 -m hilbench selftest
python3 -m hilbench agent --label NAME --exec 'claude -p {prompt} --permission-mode acceptEdits --allowedTools Read,Edit,Write,Glob,Grep' --root DIR
python3 -m hilbench llm   --label NAME --exec '...' --root DIR
python3 -m hilbench agent ... --split private --salt-file SALT     # evaluator only
```

## Public and private

Public seeds are 0–3 and ship with keys (development). Private seeds are derived from a withheld salt by
HMAC; `PRIVATE_SPLIT_COMMITMENT.json` publishes `sha256(salt)` so a later reveal can be checked, and the
runner refuses a salt that does not match. The salt is not in this repository.

## Scoring

Weights are predeclared (`hilbench/score.py`): band weights 1, 2, 4, 8, 16, 32; gate at 0.80; the delivered-
outcome primitive at ρ = 1; HLIS an equal-weight geometric mean over the coordinates present; HIL-Score
= 0.55·AUC + 0.35·Ceiling + 0.10·Harnessability. A level is a reading on the public split until the
private split is run by an evaluator who did not build the pair.
