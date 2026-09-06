# HIL-Bench Benchmark Dataset v0.8

## Purpose
This package is the public development dataset for the harmonized HIL measurement framework. It implements the shared HIL-Method-1.0 experimental grammar across Cognitive Intelligence (C), Individual Intelligence (I), Memory Capability (M), Organizational Intelligence (O), Operational Self-Awareness (SA), Delegation Intelligence (DI) through Task Difficulty (T) and Human Cognitive Intervention (H), Harness Generation (HG) conformance, and gated Unified Intelligence (U).

## Common testing grammar
Each canonical method is represented using the same style: capability being tested; environment/task family; intervention or perturbation; hidden/grounded truth; allowed action/resource envelope; procedure; external verifier; controls/ablations; metrics; reliability/uncertainty rule; lower-level retention; and binding status.

## Contents
- `hil_bench_public_dev_combined.jsonl`: all public development records (124 records).
- `canonical_method_catalog.jsonl`: canonical method definitions.
- `method_style_contract.json`: common HIL-Method-1.0 contract.
- `C_Bench/`, `I_Bench/`, `M_Bench/`, `O_Bench/`, `SA_Bench/`, `DI_Bench/`, `HG_Bench/`, `U_Bench/`: coordinate-specific packages.
- `schemas/`: machine-readable schemas.
- `verifiers/`: reference scoring/verifier utilities.
- `examples/`: example result/manifests.
- `coverage.csv`: level-by-level record coverage.
- `validation_report.json`: structural validation results.

## Coverage
The dataset includes public development records for C0-C6/CΩ, GP0-GP5, I0-I5/IΩ, M0-M5/MΩ, O0-O5/OΩ, SA0-SA6/SAΩ, T0-T6/TΩ, H0-H5, DI surface measurement, HG0-HG6/HGΩ, and U0-U6/UΩ.

## Important status rule
This is a **development dataset**, not an official certification service. Public forms expose the measurement interface and verifier semantics. Official HIL certification should regenerate secure hidden witnesses server-side and preserve independent verification. Some upper/open-ended levels are intentionally specification-only until appropriate longitudinal or secure environments exist.

## Validation
Structural validation passed: **True**. See `validation_report.json` for details.
