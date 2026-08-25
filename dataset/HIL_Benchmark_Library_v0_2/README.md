# HIL Benchmark Library v0.2

A benchmark library for **Harness-Level Intelligence (HIL)** and the **Harness-LLM
Intelligence Score (HLIS)**. v0.1 specified the suite; v0.2 binds part of it to
runnable instances and repairs two places the apparatus could not see what it
measures. See [`CHANGES_v0_2.md`](CHANGES_v0_2.md).

## What is included

- **24 external benchmark registry entries** mapped into HIL.
- **160 HIL-native task specifications**:
  - 8 harness generations: HG0, HG1, HG2, HG3, HG4, HG5, HG6, HGΩ
  - 5 intelligence dimensions at every generation: C, I, O, DI, SA
  - 4 benchmark families per dimension per generation.
- **64 Delegation-Plane task specifications**:
  - T0, T1, T2, T3, T4, T5, T6, TΩ
  - 8 application families per task band.
- Harness ladder and U0→UΩ cumulative certification gates.
- Run-log and human-intervention schemas.
- HLIS/HIL scoring configuration and executable scoring utilities.
- Application profiles for general HIL, AI4Science, software engineering,
  multi-agent research organizations, and computer-use agents.

## Core measurement objects

For a harnessed agent A=(m,h):

`S_A(T,H) = P(success | task difficulty T, human cognitive intervention H)`

`F_A(H,p) = max{T : S_A(T,H) >= p}`

One concrete model+harness pair is summarized by:

`HLIS(m,h) = 100 * exp( sum(alpha_d * ln(A_d)) / sum(alpha_d) )`

The same frozen model is then tested across a standardized harness ladder:

`HSC_m(k) = HLIS(m, HG_k)`

From the Harness Scaling Curve, report HIL-Level, HIL-AUC, HIL-Ceiling,
Harness-Gain, and (optionally) the provisional HIL-Score.

## Important validity rule

A higher harness generation **does not automatically certify a higher intelligence level**.
Architecture makes a level possible; benchmark evidence certifies it.

The candidate agent/harness must not own or modify:
- hidden benchmark assets,
- external verifier,
- promotion thresholds,
- authority kernel,
- audit ownership,
- or the declared resource envelope.

## Status of v0.1

This package is a **benchmark library and specification framework**, not a claim that
all high-level tasks are already fully instantiated certification environments.

HG0-HG2 specifications can often be instantiated as deterministic local tasks.
HG3-HGΩ require sealed environments, repeated trials, independent verifier ownership,
and stronger anti-leakage controls before formal certification.

## Package layout

- `HIL_Benchmark_Library_v0_1.xlsx` — primary workbook/dashboard
- `data/` — CSV/JSONL benchmark registries and task specs
- `configs/` — harness/scoring/resource configurations
- `schemas/` — JSON schemas for tasks, harnesses, runs, interventions
- `templates/` — task, harness, verifier, and agent-adapter templates
- `tools/` — validation and scoring scripts
- `docs/` — methodology notes and workbook previews

## Recommended evaluation workflow

1. Lock model version, harness version, benchmark version, resource envelope, and verifier.
2. Start with the Delegation-Plane suite and estimate the T×H success surface.
3. Run the native HIL coordinate suites required for the target U-level.
4. Enforce cumulative retention: U_n requires all lower levels.
5. Compute component achievements A_C, A_I, A_O (organizations only), A_DI, A_SA.
6. Compute HLIS for the concrete model+harness pair.
7. Repeat with the same frozen model on HG0→HGΩ to obtain the Harness Scaling Curve.
8. Report HIL metrics and the full component profile.
9. Add application-specific benchmark suites only after the general protocol is frozen.

## External benchmark policy

The library **does not redistribute third-party benchmark questions, answers, or hidden
test data**. It stores metadata, official links, HIL mappings, and version-lock guidance.
Run each external benchmark under its own license and official evaluation rules.
