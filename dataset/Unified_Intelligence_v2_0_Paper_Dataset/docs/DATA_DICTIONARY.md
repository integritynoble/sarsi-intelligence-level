# Data Dictionary

## HSC Episodes

| Field | Meaning |
|---|---|
| `episode_id` | Stable row identifier |
| `rung` | Harness generation HG0-HG3 |
| `task_class` | Generator/verifier task family |
| `T_band` | Task-difficulty band used for surface weighting |
| `H_budget` | Human cognitive intervention budget; H1 for this study |
| `seed` | Deterministic task seed |
| `verifier_pass` | External benchmark verdict, 0 or 1 |
| `harness_accepted` | Harness acceptance, blank where HG0 has no acceptance step |
| `false_completion` | Returned as done while externally wrong |
| `held_back` | Harness declined an externally wrong result |
| `false_rejection` | Harness declined an externally correct result |
| `harness_iterations` | Attempts counted by the harness loop |
| `model_calls` | Actual executor/model launches |
| `wall_time_seconds` | Rounded episode time from the canonical log |
| `termination_reason` | Separate termination reason; unavailable in the original log |
| `evidence_status` | Provenance status of the row |
| `notes` | Defect or reconstruction note |

## HSC Resource Summary

Token fields are deduplicated by executor message ID. `cache_creation_tokens` and
`cache_read_tokens` remain separate from uncached `input_tokens`. These values
are reconstructed from local transcript caches and were not part of the
original paper artifact.

## Regime-Switch Observations

| Field | Meaning |
|---|---|
| `seed` | Deterministic mechanism seed |
| `result` | `pass` or `capability_failure` |
| `extrapolation_rmse` | RMSE over 120 held-out extrapolation points |
| `bar` | Pass threshold, 25% of nearest-neighbour RMSE |
| `nn_baseline_rmse` | Same-instance nearest-neighbour baseline |
| `target_spread` | Target-distribution spread when archived |
| `mechanism_stated` | Whether `mechanism.txt` was delivered |
| `exit_code` | Executor process exit code |
| `seconds` | Wall time when archived |

## Paired Regime-Switch Results

| Field | Meaning |
|---|---|
| `frontier_normalized_rmse` | Frontier RMSE divided by nearest-neighbour RMSE |
| `haiku_normalized_rmse` | Haiku RMSE divided by nearest-neighbour RMSE |
| `pass_pair` | `both_pass`, `frontier_only`, `haiku_only` or `both_fail` |
| `rmse_winner` | Executor with lower RMSE, or `tie` |
