# HIL-Bench Development Dataset v0.5

This public package is a development/reference implementation of HIL-Bench. It is **not** secure certification material.

## v0.5 memory benchmark upgrade

M-Bench is independently measured as `M0, M1, M2, M3, M4, M5, MΩ`. Each level now has five parameterized development-bound forms (35 memory forms total), a difficulty grid, metric contract, common Memory Manifest, result schema, and construct-selective controls/ablations.

Canonical methods:

- `M0-EPH`: within-episode state use/update.
- `M1-RST`: restart persistence with relevant-memory ablation.
- `M2-PROV`: episodic provenance, time, and stale-state suppression.
- `M3-CONSOL`: semantic/procedural consolidation with raw-only/no-consolidation control.
- `M4-MGMT`: repair, conflict resolution, pruning, snapshot/recovery under protected retention.
- `M5-LONG`: longitudinal multi-project evidence/decision lineage.
- `MOMEGA-EVOLVE`: governed `Phi0 -> Phi1` memory-architecture improvement with paired hidden evaluation and M0-M5 retention.

Memory levels are cumulative. High M never promotes I by itself. I-Bench consumes the prerequisite mapping `I0->M0; I1->M1; I2->M3; I3->M4; I4->M4; I5->M5; IΩ->M5`, with MΩ additionally required only if memory-architecture evolution is part of the IΩ claim.

## Public/private separation

Public files contain schemas, stress grids, runner-validation forms, example results, and illustrative development thresholds. Official certification must regenerate hidden instances/perturbations/queries and keep thresholds, uncertainty rules, verifier, and promoter outside the tested system's write set.

## Package highlights

- `public/*.jsonl`: public development forms for all coordinates.
- `M_Bench/*/public_forms.jsonl`: level-specific memory forms.
- `M_Bench/*/difficulty_grid.json`: level-preserving stress grids.
- `M_Bench/*/metric_contract.json`: metric and retention contracts.
- `schemas/memory_manifest.schema.json`: declared memory architecture manifest.
- `schemas/memory_bench_v2.schema.json`: v0.5 M-Bench form schema.
- `schemas/memory_result.schema.json`: standardized result record.
- `examples/*memory*_result.example.json`: level-specific result examples.
- `verifiers/memory_scoring.py`: development point-gate implementation.

## Binding status

`development-bound` means the public form is sufficiently specified to validate a runner and verifier contract, but cannot be treated as a secure hidden witness. Formal certification requires privately bound forms.
