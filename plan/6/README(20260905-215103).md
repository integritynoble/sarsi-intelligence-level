# HIL-Bench Development Dataset v0.6

This public package is a development/reference implementation of HIL-Bench. It is **not** secure certification material.

## v0.6 cumulative Memory Capability rule

Memory certification is explicitly cumulative:

`MΩ -> M5 -> M4 -> M3 -> M2 -> M1 -> M0`.

A higher level retains **capabilities**, not necessarily the identical lower-level implementation. A memory architecture may be replaced at MΩ, but the evolved system must still pass M0-M5 retention. The formal development law is:

`Pass(M_k) = V_new,k AND K_lower,k`, where `K_lower,k` is the conjunction of all lower-M retention gates.

Therefore M5 cannot be awarded if (for example) M3 retention fails, even when the M5 longitudinal-lineage endpoints pass. MΩ cannot be awarded unless its new Φ-evolution gate passes **and** M0-M5 all remain certified.

## MΩ instrumented memory interface

MΩ additionally uses an instrumented interface `I_phi`. The agent may inspect its declared memory manifest, receive bounded diagnostics, and submit a candidate `Phi0 -> Phi1`. Runner-private operations perform snapshot/restore, diff/hash, activation verification, telemetry audit, fixed-content paired evaluation, delta ablation, migration checks, hidden M-Bench evaluation, and promotion/rollback. Hidden tasks, verifier state, thresholds, and promotion rules remain outside the tested agent's write set.

The clean causal comparison is `A(D*, Phi0)` versus `A(D*, Phi1)` with identical canonical memory contents `D*`; an ablation arm `A(D*, Phi1 - deltaPhi)` tests whether the candidate change caused the gain.

## Canonical methods

- `M0-EPH`: within-episode state use/update.
- `M1-RST`: restart persistence with relevant-memory ablation.
- `M2-PROV`: episodic provenance, time, and stale-state suppression.
- `M3-CONSOL`: semantic/procedural consolidation with raw-only/no-consolidation control.
- `M4-MGMT`: repair, conflict resolution, pruning, snapshot/recovery under protected retention.
- `M5-LONG`: longitudinal multi-project evidence/decision lineage.
- `MOMEGA-EVOLVE`: governed `Phi0 -> Phi1` memory-architecture improvement under `I_phi`, paired hidden evaluation, causal ablation, and M0-M5 retention.

## Package highlights

- `memory_level_lattice.json`: canonical cumulative M ordering and per-level newly added capability.
- `M_Bench/*/public_forms.jsonl`: five public development stress tiers per M level.
- `M_Bench/*/metric_contract.json`: level-specific metrics plus required lower-M retention.
- `M_Bench/MOMEGA_EVOLVE/interface_contract.json`: agent-visible versus runner-private instrumentation.
- `schemas/phi_interface.schema.json`, `phi_candidate.schema.json`, `memory_telemetry_event.schema.json`: MΩ interface contracts.
- `schemas/memory_bench_v2.schema.json`: v0.6 M-Bench form schema.
- `schemas/memory_result.schema.json`: standardized cumulative result schema.
- `examples/m5_lower_retention_failure.example.json`: demonstrates no level skipping.
- `verifiers/memory_scoring.py`: cumulative development gate; a failed lower M forces `z_M=0`.

## I-to-M prerequisite relation

Memory remains independent of Individual Intelligence. High M never promotes I by itself. I-Bench consumes: `I0->M0; I1->M1; I2->M3; I3->M4; I4->M4; I5->M5; IΩ->M5`, with MΩ additionally required only when memory-architecture evolution is itself part of the IΩ claim.

## Public/private separation

Public forms, schemas, stress grids, examples, interface traces, and point thresholds are development material. Official certification must regenerate hidden instances and controls, preregister thresholds/uncertainty, and keep hidden verifier/promoter assets server-side.
