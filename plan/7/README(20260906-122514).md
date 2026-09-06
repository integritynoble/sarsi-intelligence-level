# HIL-Bench Development Dataset v0.7

This public package is a development/reference implementation of HIL-Bench. It is **not** secure certification material.

## v0.7 Method B: GUI/screen inside Cognitive Intelligence

The original `C0 -> C1 -> C2 -> C3 -> C4 -> C5 -> C6 -> CΩ` semantics are preserved. GUI/screen understanding is now a first-class Cognitive Intelligence domain, written `C^GUI`, while `GP0-GP5` is a diagnostic perceptual subscale. There is **no one-to-one mapping** such as `GP3 = C3`, and GP does not independently promote the global C level.

Containment shorthand: `GP ⊂ C^GUI ⊂ C`.

The Cognitive domain panel is now: `general; science; mathematics; abstract; code; multimodal/spatial; GUI/screen; long-context`. Models without a native screen/image modality report the GUI domain as `N/A` unless the declared profile requires broad multimodal computer-screen cognition.

## GUI package

`C_Bench/GUI_SCREEN/` contains:
- synthetic public screenshot assets and oracle screen graphs;
- GP0-PIXEL through GP5-NOVEL diagnostic forms;
- C0-GUI-ATOM through COMEGA-GUI-REACH GUI-grounded C witnesses;
- `control_contract.json` for native screenshot, oracle-screen, perfect-actuator and optional oracle-strategy arms;
- `difficulty_grid.json` for within-level GUI headroom;
- `metric_contract.json` and `verifiers/gui_scoring.py`;
- schemas and result examples.

The core failure-attribution quantities are `delta_GP = Q(oracle_screen)-Q(native_screenshot)` and `delta_act = Q(perfect_actuator)-Q(native_actuator)`. Oracle-screen success is diagnostic only and cannot replace native `C^GUI` evidence when screen grounding is part of the claim. The same delivered-success endpoint must not be double-counted as both C and DI evidence.

## Cumulative Memory Capability rule

Memory certification remains explicitly cumulative: `MΩ -> M5 -> M4 -> M3 -> M2 -> M1 -> M0`. `Pass(M_k) = V_new,k AND K_lower,k`. A higher level retains capabilities, not necessarily the identical implementation.

## MΩ instrumented memory interface

MΩ continues to use the instrumented interface `I_phi`, fixed-content paired evaluation, delta ablation, migration checks, independent promotion/rollback, and M0-M5 retention.

## Public/private separation

Public screenshots, oracle graphs, forms, schemas, stress grids, examples and point thresholds are development material. Official certification regenerates hidden GUI layouts/states/transitions and all other hidden HIL witnesses server-side, preregisters thresholds/uncertainty, and keeps hidden verifiers/promoters outside the tested system's write set.
