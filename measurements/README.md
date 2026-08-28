# Regime-switch discovery probe, frontier executor

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
