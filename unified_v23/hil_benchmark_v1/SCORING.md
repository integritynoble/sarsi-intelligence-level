# Scoring contract

HIL-Core reports structure before a headline number. Every applicable coordinate
has a 0--100 achievement, ordinal band, task count, coverage, and uncertainty.
M is supporting evidence and is not multiplied into HLIS.

For C, I, O, SA, and M, let `q[k]` be verified performance at level `k` and let
`qstar[k] = min(q[0], ..., q[k])`. Achievement is the weighted mean of qstar
with weights `2**k`. An ordinal band passes at qstar >= 0.80 and only when every
lower band is present. Thus a hard item cannot compensate for failed retention.

For each DI cell:

```text
net(T,H) = max(0,
  P(delivered and verifier-pass) - rho * P(false completion))
```

v1 fixes `rho=1`, weights a cell by `2**T * (6-H)`, and reports both the surface
and its weighted mean. A held-back wrong result costs human load but is not a
false completion. A held-back correct result is a false rejection and receives
no delivered-success credit. The frontier at H is the largest contiguous T for
which every band from T0 through T meets reliability 0.80.

For an individual, `D={C,I,DI,SA}`. For an organization,
`D={C,I,O,DI,SA}`. With equal preregistered weights:

```text
HLIS = 100 * geometric_mean(A[d] for d in D)
```

O is N/A—not zero—for an individual. If any required dimension is unassessed,
HLIS is null and the missing dimensions are named. If an assessed dimension is
zero, HLIS is zero.

U* is a separate cumulative gate. HIL-Core v1 instruments U0--U2. U2 requires
C2, I2, SA2, T2 at H<=2, and M3; the organization track also requires O2.
The U-level is not inferred by rounding HLIS.

Wilson 95% intervals describe binary sampling uncertainty. The propagated HLIS
interval is descriptive, not a substitute for repeated-run or psychometric
uncertainty. Resource and human-load fields remain separate from intelligence
achievement. Working thresholds are frozen for v1 but are not claimed to be
validated population norms.
