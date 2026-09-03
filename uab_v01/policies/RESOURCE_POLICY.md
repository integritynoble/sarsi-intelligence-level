# Resource policy (UAB v0.1)

Every pair report carries a resource envelope `R`: wall clock, model calls, tokens in/out, tool
calls, subagent count, compute class, persistent-memory budget, external-knowledge access. Two pairs
with different envelopes are compared only with both envelopes shown.

**Enforced, not stated.** The wall-clock limit in the manifest is the limit the runner enforces on the
executor's **process group**. A limit that is stated and not enforced, or that kills only the direct
child, is an apparatus defect; the release that found both is v2.3 §16.11.

**Per-band ceilings (defaults):** T0 300 s, T1 600 s, T2 1800 s, T3 3600 s, T4 7200 s, T5 7200 s.
A ceiling shorter than the task corrupts the measurement invisibly; every record therefore carries
`limit_reached` and `termination_reason`, and a truncated run is never scored as a delivery.

**Cost per verified completion** is a primary endpoint. Equal scores at unequal cost are unequal
results.

**Tool authority** is equalised across executors or recorded as unequal; two executors with different
tool authority are not comparable however carefully everything else is held fixed.
