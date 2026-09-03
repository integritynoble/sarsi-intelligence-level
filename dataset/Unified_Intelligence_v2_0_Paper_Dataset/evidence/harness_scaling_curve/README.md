# Harness Scaling Curve Evidence

`episodes.csv` reconstructs the 48 episode outcomes from the canonical runner
log. `rung_results.csv` preserves the originally reported aggregate, augmented
with actual model-call and rounded runner-time totals. `resource_summary.csv`
contains transcript-derived resource telemetry.

The canonical HSC curve is:

```text
HG0 93.3 -> HG1 93.3 -> HG2 96.7 -> HG3 96.7
```

Important accounting correction: the run recorded 53 harness iterations and 52
actual Claude calls. HG2 `t1.clean_dataset`, seed 0 has three loop iterations,
but the third selected `CriteriaOnly` and failed before model launch.

Run `../../tools/analyze.py --write` from the package root to regenerate
`analysis_results.json`.
