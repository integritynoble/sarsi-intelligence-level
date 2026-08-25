# HLIS and HIL Scoring Guide

## 1. Component achievement

For each declared intelligence dimension d, calculate an externally verified normalized
achievement `A_d` in [0,1].

Recommended singleton dimensions:
- C
- I
- DI
- SA

Recommended organization dimensions:
- C
- I
- O
- DI
- SA

Do not insert O=0 for a singleton. O is N/A and omitted.

## 2. Continuous pair score

HLIS is a weighted geometric mean:

`HLIS(m,h;D,alpha,R,B) = 100 * exp( sum_d alpha_d ln(A_d) / sum_d alpha_d )`

The geometric mean discourages a single very strong dimension from masking a major
weakness elsewhere.

## 3. Cumulative dimensions

For cumulative level tests I, O and SA, use:

`q*_(d,k) = min_{j<=k} q_(d,j)`

before aggregation. This makes higher-level credit conditional on retaining lower-level
capability.

## 4. Delegation achievement

Always retain the raw surface:

`S_A(T,H) = P(success|T,H)`

and frontier:

`F_A(H,p) = max{T : S_A(T,H)>=p}`.

A continuous `A_DI` may be calculated from a weighted average of the success surface,
with greater weights for harder tasks and lower human cognitive intervention.

## 5. Harness scaling

For frozen model m:

`HSC_m(k) = HLIS(m,HG_k)`.

Report:
- HIL-Level
- HIL-AUC
- HIL-Ceiling
- Harness-Gain
- resource usage
- confidence interval
- full per-generation HLIS curve.

## 6. Provisional HIL score

The package includes:

`HIL-Score = 0.55*HIL-AUC + 0.35*HIL-Ceiling + 0.10*Harnessability`

This is provisional and should not be treated as a universal scientific constant.
Empirical calibration is required.

## 7. Reporting

Recommended result:

`U3 | HLIS=74.3 | [C5,I3,O3,T4/H1,SA3] | p=.80 | HIL-R1 | benchmark/harness versions`

Never report the scalar alone.
