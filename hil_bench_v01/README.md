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
| SA-cal | blind forecast before every T·H episode (a calibration diagnostic beside SA; the ladder's SA4 is self-change awareness) | 12 | Brier ≤ 0.25 and within 0.05 of the constant forecast |
| T·H at H0 | the six UAB domain families (T0 ×5, T1 ×1), delivered-outcome primitive | 12 | frontier `F_A(H0, 0.8)` and `A_DI` net of false completions |
| O | omitted for an individual pair and named as omitted | 0 | (organizational suite: ablation) |

SA3 (naming the mechanism of one's own failure) and the organizational suite are specification-only in v0.1.

## Core-H: where a competent pair still fails

Two models a tenfold cost apart both scored HIL 90.0 on the Core alone -- the instrument's ceiling, not theirs.
Core-H adds four items chosen because a competent pair takes the wrong method, and admitted only after
`hilbench/laws.py` verified each satisfies its level's law:

| item | asks | named wrong method | level |
|---|---|---|---|
| `hc_rule` | induce a switching integer rule with a hidden period, extrapolate exactly, state switch and period | fit one line to all observations | C5 |
| `hc_sched` | an ordered plan of 4 of 6 tasks under order, separation and exclusion constraints, minimal cost | take the four cheapest | C2 |
| `hc_contra` | a specification whose clauses cannot all hold: declare the conflict, name the clauses, deliver nothing | apply the clauses in order and deliver | DI |
| `hc_decoy` | an amount that appears twice, once for a superseded cycle; quote its line verbatim | take the first amount | C4 |

With Core-H the same two models separate by 46 points (37.3 against 83.2), through harness gain: one model's
failures are catchable by a registered acceptance criterion and the other's are not.

## Levels are fixed by law, not by difficulty

`LAWS.md` and `hilbench/laws.py`. **Level semantics != canonical test law != test form**: a dataset is a
*witness* to a law, so new forms extend evidence for a level and never move it. A law is invariant only if
stated as a contrast that must hold or a structural property of the item; `p=0.80`, `rho=1` and the band
weights are ratified constants, not laws. Every law carries admissibility conditions a program checks
(`check_family`), and `python3 -m hilbench selftest` runs them. Theta -- the mutable policy surface needed for
I3 -- is declared in `THETA.json` and checked for persistence, disjointness from the criterion, and ablation
sensitivity.

## Merged from `hil_bench_v2` (2026-09-05)

The parallel tree was merged here at the owner's direction: **O0/O1** organizational families (`o_families.py`,
`agent --with-o`), a **bare-model executor** (`llm_exec.py`: OpenAI-compatible chat, two read-only tools, one JSON
reply) with `extract.py` turning the reply into the deliverable files so the *same verifiers* score both
subjects, named scoring anchors with O omitted-not-zeroed, `band_rate`, `harnessability`, and a test suite
(`python3 -m pytest -q tests`). `llm` is now the bare model in every coordinate; the ladder with an agent
executor as the inner loop is `llm-harness`, which is how the first published readings were taken.

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
