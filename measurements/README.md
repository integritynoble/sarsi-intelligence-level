# Regime-switch discovery probe, same-seed executor comparison

`t5.hidden_law`, `regime_switch` family. Every regime-switch instance in seeds
0–59 (13 exist; 12 are here, seed 12 was scored under an earlier protocol and
passed at 0.206 against a bar of 0.889).

Each episode: a mechanism generated from the seed — two closed-form laws and a
latent linear boundary between them — sampled with 2% noise inside a box, scored
by RMSE on 120 held-out points **outside** that box. Passing requires 25% of the
nearest-neighbour baseline computed on the same instance, and requires the rule
to be stated in `mechanism.txt`, not merely used.

| | |
|---|---|
| Episodes scored | 12 |
| Passed | 5 |
| Capability failures | **7 (58%)** |
| Worse than the nearest-neighbour baseline | 3 (seeds 0, 24, 41) |
| Deliverable failures | 0 |
| Killed by the harness | 0 |

All twelve exited 0 with a mechanism stated, so none is a timeout or a
non-delivery. Three exceeded the error that memorising the training set
achieves, which is the specific failure the extrapolation grid exists to detect.

## Protocol note, and a retracted number

An earlier run of this family used a 2400-second executor limit and produced
results that are **not** in this table because they were harness artifacts.
Seed 27 reached an RMSE of 0.086 against a bar of 0.934 and was killed before
writing `mechanism.txt`; rerun at 7200 seconds it passes at 0.060. Seed 11 was
recorded as a capability failure at 0.258 against a bar of 0.043 and **passes at
0.021** when given the time to finish.

That retracted seed-11 number was the headline of the first draft of v1.9. A
limit that fires correctly still corrupts a measurement if it is shorter than
the task, and the failure is invisible in the verdict: a truncated run and a
wrong answer look identical unless the runner records why the episode ended.
The probe now prints the executor's exit note beside every verdict.

The frontier CSV lacks wall times for six seeds and neither CSV has a separate
termination-reason field. Exit code 0 and the presence of each mechanism make
the included episodes distinguishable from the known timeout artifacts, but
the archived rows do not fully satisfy the reporting standard adopted after
those artifacts were found.

## Same-seed executor comparison

`regime_switch_haiku.csv` contains the same twelve common-protocol seeds run with
the Haiku executor (`claude-haiku-4-5`), using the same 7200-second timeout and
scoring protocol as `regime_switch_frontier.csv`. The common seeds are
0,9,11,17,24,25,27,38,40,41,44,50. Seed 12 is excluded because it was scored
under an earlier protocol. The archived frontier CSV does not identify the
frontier model or executor version.

Frontier passed 5/12 (41.7%) and Haiku passed 1/12 (8.3%). There were four
frontier-only passes, no Haiku-only passes, one both-pass (seed 27), and seven
both-fail outcomes. All 24 episodes exited 0 and stated a mechanism; there were
no timeout or delivery failures. The exact two-sided McNemar test is p=0.125,
and the observed paired pass-rate difference is 33.3 percentage points. A
conservative 95% paired-difference interval is approximately -0.9 to +60.2
percentage points, so the binary result should not be described as significant.

Frontier RMSE was lower on 11/12 matched instances (exact two-sided sign test
p=0.00635). Median RMSE was 0.639 for frontier versus 5.112 for Haiku; median
RMSE normalized to the same-seed nearest-neighbour baseline was 0.359 versus
2.142. These robust medians matter because Haiku seed 40 has RMSE 1187.885.
All 11 Haiku failures were worse than the nearest-neighbour baseline.

This is a same-seed discrimination measurement on these instances, not a
universal model-tier ordering. It holds the harness and protocol fixed while
changing the executor/model, so it is not a Harness Scaling Curve segment.
There is one attempt per executor per seed, one mechanism family, one
host/harness configuration, no repeat-run variance estimate, and an incomplete
resource envelope.
