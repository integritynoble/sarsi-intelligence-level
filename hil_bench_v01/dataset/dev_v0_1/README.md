# HIL-Bench Development Dataset v0.1

This package is a public **development/reference dataset** for the September 2026
HIL-Bench working draft. It is not an official HIL-1.0 private certification set.

The design follows the paper's distinction:

    level semantics != canonical test law != test form

A dataset record is a *test form* or a component of a longitudinal campaign.
Upper Individual Intelligence levels cannot be reduced to one-shot question/answer rows.

## What is included

- `public/cognitive.jsonl`: public development forms for C0-C5.
- `public/i0_transient.jsonl`: bounded current-episode forms.
- `public/i1_rst.jsonl`: restart-continuity campaigns.
- `public/i2_xfer.jsonl`: experience -> persistence -> restart -> held-out transfer campaigns.
- `public/i3_theta.jsonl`: agent-native THETA self-improvement campaigns.
- `public/i4_psi.jsonl`: PSI meta-campaigns built from multiple non-identical I3 campaigns.
- `public/organization.jsonl`: O0-O4 development forms.
- `public/delegation.jsonl`: T0-T5 task/delegation forms.
- `public/self_awareness.jsonl`: SA1-SA5 development forms.
- `spec_only/upper_levels.json`: specification-only templates for levels that require
  long-horizon sealed environments rather than a static public corpus.
- `schemas/`: machine-readable schemas/contracts.
- `verifiers/hil_scoring.py`: development scoring helpers for I3 and I4.
- `examples/`: example Theta/Psi manifests and result records.

## Important status

All tasks, hidden keys, thresholds, and seeds in this package are public development
material. They MUST NOT be treated as secure private witness forms.

Official certification should regenerate private witness forms server-side, keep
hidden evaluation mechanics outside the tested system's write set, and use an
independent evaluator/promoter.

## I3 record structure

Each I3 campaign contains:

    Theta manifest contract
        -> diagnostic tasks
        -> causal self-diagnosis
        -> bounded Theta0 -> Theta1 change
        -> behavior probes
        -> paired sealed evaluation
        -> regression checks
        -> I0-I2 retention

A campaign result is summarized by:

    z_I3,r = D_r * M_Theta,r * V_r * G_r * K_r

where all gates are binary and diagnostics remain separately reported.

## I4 record structure

Each I4 meta-campaign contains multiple I3 campaigns:

    Psi0
        -> baseline I3 campaign block
        -> measure improvement competence
        -> Psi0 -> Psi1
        -> new non-identical I3 campaign block
        -> compare Psi1 vs Psi0
        -> external validation
        -> regression + I0-I3 retention

A development meta-campaign result is summarized by:

    z_I4,s = M_Psi,s * V_Psi,s * G_Psi,s * K_4,s

I4 is NOT certified by repeated Theta updates under an unchanged Psi.

## Recommended use

1. Integrate a tested agent with the manifest interfaces in `schemas/`.
2. Start with the public forms to validate the runner and logging.
3. Use construct-selective ablations and known controls.
4. Generate fresh private witnesses under the same canonical laws.
5. Preregister thresholds and uncertainty rules before official evaluation.

