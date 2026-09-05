# HIL-Bench Development Dataset v0.4

This package is a public **development/reference dataset** aligned with the revised September 2026 HIL-Bench papers. It is **not** an official private HIL-1.0 certification set.

The design preserves the separation:

    level semantics != canonical test law != public test form

Upper Individual Intelligence levels are longitudinal campaigns, not one-shot question/answer rows.

## What is included

- `public/cognitive.jsonl`: C0-C5 development forms.
- `public/i0_transient.jsonl`: bounded current-episode forms.
- `public/i1_rst.jsonl`: restart-continuity campaigns.
- `public/i2_xfer.jsonl`: experience -> restart -> hidden transfer campaigns.
- `public/i3_theta.jsonl`: governed Theta self-improvement campaigns.
- `public/i4_psi.jsonl`: Psi improvement-of-improvement meta-campaigns.
- `public/i4_recursive_depth.jsonl`: stronger repeated-Psi longitudinal forms.
- `public/i5_disc.jsonl`: **new v0.4** I5-DISC discovery -> validation -> restart -> causal incorporation templates.
- `public/iomega_long.jsonl`: **new v0.4** I-OMEGA-LONG discovery -> cognitive instrument -> frontier-expansion program templates.
- organization/delegation/self-awareness development forms.
- `schemas/`: machine-readable contracts including I5 and I-Omega.
- `verifiers/hil_scoring.py`: development point-estimate scoring helpers for I3, I4, I5 and I-Omega.
- `examples/`: example manifests/results.

## I5-DISC in v0.4

I5 is cumulative and longitudinal. A public development campaign requires:

    unresolved unknown
      -> competing hypotheses
      -> agent-selected informative probes/experiments
      -> evidence/rejection lineage
      -> independent validation
      -> persistent consolidation
      -> lifecycle discontinuity
      -> hidden transfer
      -> discovery-vs-control causal incorporation test
      -> I0-I4 retention

A development gate is summarized as:

    z_I5 = U * H * E * L * V * P * K5

`P` is the incorporation gate. It is not enough to store or repeat the discovery; after restart, the validated discovery must cause appropriate improvement on related unseen situations relative to a matched no-discovery/discovery-ablated control.

I5 knowledge incorporation does not itself require a Theta or Psi change. If the candidate also changes Theta or Psi, those changes remain subject to the I3/I4 certification laws.

## I-OMEGA-LONG in v0.4

I-Omega is not certified by one discovery or one tool. A longitudinal program repeatedly requires:

    validated discovery K_new
      -> validated cognitive instrument/representation/method J_new
      -> same persistent individual evolves
      -> previously unreachable held-out class becomes reachable
      -> ablation supports causal contribution of J_new
      -> I0-I5 retention

Conceptually:

    K_new -> J_new -> A_(t+1)
    F(A_(t+1); R) strictly expands beyond F(A_t; R)

Public templates use disjoint pre/post/ablation frontier tests. Formal certification must use sealed generators and preregistered reachability/effect thresholds. Reports should state the developmental horizon, domain set, and number of validated frontier-expansion cycles; finite evidence does not prove literal infinite self-evolution.

## Public/private warning

All tasks, example values, thresholds, seeds and structures in this package are development material. Official certification must regenerate private witness forms server-side, keep hidden evaluation mechanics and promotion law outside the tested system's write set, and use independent verification.

## Recommended use

1. Integrate one persistent tested agent with the declared state/change interfaces.
2. Validate logging and causal branching using these public forms.
3. Use construct-selective ablations and matched controls.
4. Generate fresh private witnesses under the same canonical laws.
5. Preregister thresholds, uncertainty rules, resource envelopes and human-intervention limits before certification.


## M-Bench memory capability suite (v0.4)
Memory is independently measured as M0, M1, M2, M3, M4, M5, and MΩ, then used as a one-way prerequisite for Individual Intelligence. Public development forms are in `public/m*.jsonl`. The canonical methods are M0-EPH, M1-RST, M2-PROV, M3-CONSOL, M4-MGMT, M5-LONG, and MOMEGA-EVOLVE.

I-to-M prerequisite rule: I0->M0; I1->>=M1; I2->>=M3; I3->>=M4; I4->>=M4; I5->>=M5; IΩ->>=M5, with MΩ additionally required only when memory-architecture evolution is part of the IΩ claim. High M never promotes I by itself.
