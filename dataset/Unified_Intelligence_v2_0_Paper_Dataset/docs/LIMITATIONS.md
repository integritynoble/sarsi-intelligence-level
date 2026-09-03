# Limitations and Provenance Boundaries

## Coordinate Library

- The inherited v1.2 library is aligned to framework v1.9 and carried forward,
  not regenerated from Version 2.0 prose.
- It contains no runnable C5-or-higher certification evidence.
- Most asserted answer keys do not yet have executable reference
  implementations.
- The audit is a filter with unknown recall, not proof that every unflagged item
  is valid.

## Harness Scaling Curve

- The canonical tracked artifact is an aggregate text report. The 48-row episode
  table is reconstructed from the canonical runner log.
- Exact raw task directories, withheld keys, criterion registers, acceptance
  objects, snapshots, routing decisions and final workspaces were not archived
  as a release bundle.
- Separate process termination reasons are unavailable.
- The original report labels the model as Claude Code 2.1.234 with the default
  model. Local transcripts identify `claude-opus-5`; that identity is marked as
  reconstructed rather than silently substituted into the canonical label.
- One HG2 episode has three harness iterations but two model calls. The third
  iteration selected a criteria-only provider because of a routing-pool defect
  and failed before model launch.
- Token data are reconstructed from local transcript caches and deduplicated by
  message ID. They are not third-party reproducible from the original Git
  release alone.
- CPU, memory, host load, cost and complete environment metadata are absent.
- The study measures one model, six classes, two seeds, one H budget and four
  rungs. It is not a general estimate of harness effects.

## Regime-Switch Study

- The frontier model ID and executor version are absent from the archived CSV.
- Six frontier rows lack wall time and target spread.
- Neither executor CSV has a separate termination-reason field.
- Exit code 0 and mechanism delivery distinguish these rows from known timeout
  artifacts, but do not provide a complete termination record.
- There is one attempt per executor/seed, one mechanism family and one
  host/harness setup.
- No repeat-run variance, order randomization or cross-host replication is
  available.
- The binary pass difference is not statistically significant under the exact
  two-sided McNemar test (`p=0.125`).
- The continuous RMSE ordering is strong on these 12 pairs but does not establish
  a universal model-tier ordering.
