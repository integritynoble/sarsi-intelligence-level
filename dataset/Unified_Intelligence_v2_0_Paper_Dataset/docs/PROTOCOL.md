# Dataset Protocol

## Coordinate Benchmark Dependency

The v1.2 coordinate archive is inherited without changing item content or answer
keys. Its own `README.md`, `manifest.json`, protocol and audit remain binding.
The dependency contains the core profile `[C,I,O,T,H,SA]`, supporting Memory
Capability `M`, the GUI Perception diagnostic subset, and the derived `T x H`
delegation matrix.

Version 2.0 does not reinterpret specification-only or protocol-bound rows as
runnable certification evidence.

## Harness Scaling Curve

The HSC holds the model, task classes, seeds, external verifiers, tool grant and
H1 intervention budget fixed while changing the harness rung.

| Rung | Added mechanism |
|---|---|
| HG0 | Model, bounded tools and evidence log; one attempt; no acceptance step |
| HG1 | Persistent state, pre-registered criterion and separate-process acceptance |
| HG2 | Snapshot, restore and retry with the failed check named |
| HG3 | Failure classification, competence evidence and routing |

Task classes are `t0.csv_to_json`, `t0.extract_fields`, `t1.clean_dataset`,
`t1.request_timeout`, `t2.pipeline` and `t3.search_latency`, each at seeds 0 and
1 on every rung.

Gross delegation achievement is computed from the success surface:

```text
A_DI = sum(w_T * v_H * success_rate[T,H]) / sum(w_T * v_H)
```

The fixed task weights are `T0=1`, `T1=2`, `T2=4`, `T3=8`; all episodes are at
H1, so the common H weight cancels. The net score with false-completion penalty
`rho=1` subtracts the false-completion rate from each surface cell before the
same weighted average.

`harness_iterations` counts entries through the harness attempt loop.
`model_calls` counts actual executor/model launches. They differ for one HG2
episode because the loop selected a criteria-only provider and failed before
launching a model.

## Regime-Switch Comparison

The regime-switch study freezes task generator, mechanism family, harness,
protocol, timeout and common seed set while changing executor/model.

Each seed generates two closed-form laws and a latent linear boundary between
them. Observations contain 2% noise inside a box. Scoring uses RMSE on 120
held-out points outside that box. The pass bar is 25% of the nearest-neighbour
baseline on the same instance, and a mechanism statement must be delivered.

The common seeds are `0,9,11,17,24,25,27,38,40,41,44,50`. Seed 12 is excluded
because it used an earlier protocol. Each executor has one attempt per seed and
a configured timeout of 7200 seconds.

Primary paired summaries are:

- Pass contingency and exact two-sided McNemar test.
- Per-seed RMSE ordering and exact two-sided sign test.
- Median RMSE.
- Median RMSE normalized by the same-seed nearest-neighbour baseline.

This comparison is not an HSC segment because it changes executor/model rather
than harness generation.

## Missing Data

An empty CSV value means the field was not archived. The analysis does not
impute missing wall times, target spread, model identity or termination reason.
