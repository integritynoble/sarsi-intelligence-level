# Unified Intelligence Version 2.0 Paper Dataset

This package is the data release for *Measuring the Unified Intelligence Level,
Version 2.0*. It joins three kinds of evidence that were previously distributed
across the repository:

1. The audited HIL coordinate benchmark datasets from v1.2.
2. The 48-episode Harness Scaling Curve (HSC) measurement carried forward in the
   paper.
3. The 24-episode same-seed regime-switch executor comparison added in Version
   2.0.

The package does not turn preliminary measurements into certification claims.
The coordinate library contains protocols and specification-only rows at levels
where runnable evidence does not yet exist, and the two empirical studies retain
the limitations stated in the paper.

## Release Contents

| Path | Purpose |
|---|---|
| `manifest.json` | Package identity, counts, provenance and limitations |
| `evidence/harness_scaling_curve/` | HSC episode, rung and resource records |
| `evidence/regime_switch/` | Matched frontier/Haiku observations and analysis |
| `schemas/` | Machine-readable schemas for released evidence rows |
| `docs/` | Protocol, data dictionary and limitations |
| `tools/analyze.py` | Recompute all headline statistics without third-party packages |
| `tools/validate.py` | Validate counts, pairings, hashes and derived outputs |
| `tools/build_release.py` | Build the deterministic standalone ZIP and checksums |
| `dependencies/` | In the release ZIP, contains the inherited v1.2 coordinate archive |

The Git tree does not duplicate the coordinate archive inside this directory.
`tools/build_release.py` embeds the sibling file
`../HIL_Coordinate_Benchmark_Datasets_v1_2.zip` as
`dependencies/HIL_Coordinate_Benchmark_Datasets_v1_2.zip` in the standalone
release ZIP. When run from an extracted release, the tools use that embedded
copy instead, so analysis, validation and rebuilding do not require the source
repository layout.

## Reproduce the Results

Run from this directory:

```text
python3 tools/analyze.py --write
python3 tools/validate.py
python3 tools/build_release.py
```

`analyze.py` writes:

- `evidence/harness_scaling_curve/analysis_results.json`
- `evidence/regime_switch/paired_results.csv`
- `evidence/regime_switch/analysis_results.json`

`build_release.py` writes `checksums.sha256` and creates
`../Unified_Intelligence_v2_0_Paper_Dataset.zip`. Archive entries have a fixed
timestamp so identical source bytes produce an identical ZIP.

## Headline Results

### Harness Scaling Curve

- 48 episodes: 12 at each of HG0, HG1, HG2 and HG3.
- Gross `HLIS_DI`: `93.3 -> 93.3 -> 96.7 -> 96.7`.
- False completions: 2, 0, 0, 0 by rung.
- Held-back invalid results: 0, 2, 1, 1 by rung.
- 53 harness-loop iterations, but 52 actual model calls. One HG2 iteration
  selected a criteria-only provider and failed before model launch.

### Regime-Switch Comparison

- Common seeds: `0,9,11,17,24,25,27,38,40,41,44,50`.
- Frontier: 5/12 passes; Haiku (`claude-haiku-4-5`): 1/12.
- Exact two-sided McNemar test: `p=0.125`.
- Frontier RMSE lower on 11/12; exact two-sided sign test:
  `p=0.00634765625`.
- Median RMSE: 0.6385 versus 5.1115.
- Median nearest-neighbour-normalized RMSE: 0.3593 versus 2.1421.

## Evidence Status

Fields use explicit status labels:

- `archived`: present in the original tracked measurement artifact.
- `reconstructed`: recovered from the canonical log and local executor
  transcripts after the run.
- `source_inferred`: established from the frozen implementation, not a
  persisted run event.
- `not_archived`: unavailable and intentionally left unknown.

Missing values are empty in CSV and `null` in JSON. They are never filled by
guessing.

## Citation

Yang, Chengshuai. *Measuring the Unified Intelligence Level: A Cumulative,
Harness-Measurable Hierarchy*, Version 2.0, August 2026.
