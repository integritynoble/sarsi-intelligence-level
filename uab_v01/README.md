# UAB v0.1 — Unified Agent Benchmark, specification package

Frozen 2026-09-03. Read `UAB_SPEC.md` first. Coverage is in `matrix/uab_matrix_v0_1.md` and is
generated: 36 domain-band cells, of which 4 BOUND, 1 GENERATOR_BOUND, 4 BAND_ONLY, 27
SPECIFICATION_ONLY; plus 10 cross-domain coordinate manifests (I1 ×4, SA1/SA2 ×3, DI T0/T1 ×3).

```
python3 tools/build_manifests.py   # writes manifests/*.json with content hashes
python3 tools/build_matrix.py      # regenerates matrix/
python3 tools/validate.py          # schema, hashes, matrix consistency, local asset existence
```

Nothing here is a level. A manifest makes a claim testable; a certification run tests it.
