# UAB v0.1 — Unified Agent Benchmark, specification package

Frozen 2026-09-03. Read `UAB_SPEC.md` first. Coverage is in `matrix/uab_matrix_v0_1.md` and is
generated: 36 domain-band cells, of which 4 BOUND, 7 GENERATOR_BOUND, 2 BAND_ONLY, 23
SPECIFICATION_ONLY; plus 10 cross-domain coordinate manifests (I1 ×4, SA1/SA2 ×3, DI T0/T1 ×3).

Seven families live in this package (`families/`): code T0 one-edit, funding T0 extract-requirement,
job T0 extract-requirements, paper T0 verify-citation, paper T1 results-section, business T0
extract-fact, the U2 learning-transfer suite (`learning_t2`, paired episodes; `tools/run_learning_protocol.py`,
ablated arm first in a separate root), and the U3 self-improvement suite (`selfimprove_t3`: the pair rewrites
its own PROFILE.md from dev evidence; an evaluator it cannot write to scores baseline vs candidate on hidden
instances plus a U0 retention item and promotes or rejects; `tools/run_selfimprove_protocol.py`). Each ships a seeded generator with a hidden key, a verifier, a reference
solver, the plausible wrong method, and a specification–key test; `python3 -m families selftest`
must show the reference passing and the naive method failing on every seed.

```
python3 tools/build_manifests.py   # writes manifests/*.json with content hashes
python3 tools/build_matrix.py      # regenerates matrix/
python3 tools/validate.py          # schema, hashes, matrix consistency, local asset existence
python3 -m families selftest --seeds 0-47   # the three in-package T0 families discriminate
```

Nothing here is a level. A manifest makes a claim testable; a certification run tests it.
