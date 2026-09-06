# HIL-Bench Development Dataset v0.8

Status: public development and runner-validation package. It is **not** official hidden certification material.

## v0.8 harmonization

This release applies one experimental reporting grammar (`HIL-Method-1.0`) across the HIL measurement system. Each level/band/rung record declares: capability being tested, canonical method, evaluator intervention, hidden/grounded state, ordered procedure, controls/ablations, primary metrics, certification/conformance gate, lower-level retention, resource envelope, and binding status.

The harmonization covers:
- Cognitive Intelligence C0-C6/C-Omega, including the existing C^GUI domain;
- Individual Intelligence I0-I5/I-Omega (existing detailed runnable forms retained);
- Memory M0-M5/M-Omega (existing M-Bench retained);
- Organizational Intelligence O0-O5/O-Omega;
- Operational Self-Awareness SA0-SA6/SA-Omega;
- Task Difficulty T0-T6/T-Omega;
- Human Cognitive Intervention H0-H5;
- Delegation Intelligence as the derived T x H reliability surface;
- Harness Generation HG0-HG6/HG-Omega as **engineering conformance**, not intelligence certification;
- Unified levels U0-U6/U-Omega as **conjunctive integration gates**, not arithmetic averages.

## Key files
- `canonical_method_catalog.jsonl`: one harmonized method record for every ladder/band/rung.
- `method_style_contract.json`: common testing-method grammar.
- `public/*.jsonl`: public development forms.
- `C_Bench/CORE`, `O_Bench`, `SA_Bench`, `DI_Bench`, `HG_Bench`, `U_Bench`: structured method packages.
- `schemas/harmonized_method.schema.json`: machine-readable schema.
- `verifiers/harmonized_scoring.py`: reference development helpers.

## Binding status
`development-bound` means the public form is concrete enough for runner validation but is not secure certification material. `specification-only` means the canonical law is defined but a secure executable environment/verifier still needs implementation.

## Invariance
Dataset forms instantiate the canonical law; they do not redefine level semantics. Saturation motivates harder construct-equivalent witnesses or higher levels, not moving an old level boundary.
