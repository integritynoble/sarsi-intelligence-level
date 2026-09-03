# Retention policy (UAB v0.1)

Promotion to `U_n` requires the `U_n` suite **and** every `U_0 … U_(n−1)` retention suite to pass, in
the same frozen configuration, in the same certification run.

**Regression.** A candidate that raises a higher-level score while lowering any lower-level suite
below its gate is not promoted; the regression is reported as a primary result, not as noise.

**Examples.** HG2 cannot earn U2 if restart persistence regresses. HG3 cannot earn U3 if
self-improvement improves one score while breaking basic task reliability. HG4 cannot earn U4 if
meta-improvement causes repeated regression of lower-level skills.

**Longitudinal levels.** I3+, O3+, SA4+ and U4+ require evidence across several improvement cycles;
a single cycle earns nothing above U3.

**Paired rungs.** Where two harness generations differ only in post-hoc machinery (HG0 vs HG1), they
are scored from the **same** executor outputs; an independent run per rung introduces between-rung
variance that can exceed the effect.
