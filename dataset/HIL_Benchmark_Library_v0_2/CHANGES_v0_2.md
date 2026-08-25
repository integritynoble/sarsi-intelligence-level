# HIL Benchmark Library v0.2 — what changed and why

v0.1 is a complete specification: 160 native task specs across eight harness
generations and five dimensions, 64 delegation-plane specs across eight bands, a
ladder, gates, schemas, templates and scoring tools. Every task carries
`asset_status: specification_ready` or `requires_sealed_environment`, which is
honest and means nothing runs yet.

v0.2 does not add specifications. It binds some of them to things that execute,
and repairs two places where the measurement apparatus cannot see what it is
supposed to measure.

---

## 1. Bindings: what actually runs

`bindings/bindings.jsonl` — one row per benchmark, with three statuses.

| status | count | meaning |
|---|---|---|
| `bound` | **34** | a runnable instance exists **for this band and this family** |
| `band_only` | 30 | something runs at this difficulty band, but not for this family |
| `specification_only` | 160 | nothing runs it here |

**`band_only` is deliberately not counted as coverage.** Substituting
`software_engineering` for `document_workflow` at T2 measures a different task,
and counting it would report coverage the suite does not have. Two of the
library's families — `document_workflow` and `multimodal_workflow` — have no
implementation at any band, and the bindings say so per row.

The 16 bound native rows are the DI coordinate at HG0–HG3. C, I, O and SA have
no runnable suite here, so those 144 rows stay specifications: only one of five
dimensions is instrumented, and a score over one dimension is not an HLIS.

## 2. The run log could not distinguish a refusal from a wrong answer

v0.1's `run_log.schema.json` requires `verifier_pass`. It has no field for
whether the **harness** accepted the result, so these two runs produce identical
rows:

- the system produced wrong work, accepted it, and handed it back as done;
- the system produced wrong work, **declined to accept it**, and reported that.

Those are the same failure for a pass rate and opposite outcomes for anyone
delegating. v0.2 adds `harness_accepted` (required), and the derived
`false_completion`, `held_back` and `false_rejection`, which make the 2×2
explicit:

| `harness_accepted` | `verifier_pass` | outcome |
|---|---|---|
| null (HG0 has no acceptance step) | true | delivered, correct |
| null | false | **false completion** |
| true | true | accepted, correct |
| true | false | **false completion** |
| false | false | held back — a correct refusal |
| false | true | false rejection — the cost of strictness |

Also added: `verification_responsive`, so ρ_V can be aggregated over rejected
runs, and `attempts`.

## 3. A_DI could not see the harness generation that adds acceptance

This is the repair that came from measurement rather than from reading.

v0.1 computes `A_DI` as the weighted mean of `S_A(T,H) = P(success)`. Acceptance
does not change the probability of success — it changes what is *reported* as
success. So a harness generation whose entire contribution is an acceptance step
scores identically to one without it.

Measured on this machine, one frozen model, six task classes, two seeds, only
the harness changing between rungs:

```
HG0   A_DI 0.933   HLIS_DI 93.3
HG1   A_DI 0.933   HLIS_DI 93.3      <- identical
```

HG1 adds persistent state, a criterion registered before the work exists, and
acceptance in a separate process. The pass pattern is unchanged, so the curve is
flat, so **the Harness Scaling Curve cannot see its own first rung** — the rung
that makes every claim above it reportable at all.

`configs/scoring_config.json` therefore enables a net surface:

```
S_net(T,H) = P(verifier_pass) − ρ · P(false_completion)
```

with ρ from the class's own loss terms. A refusal costs human load and enters
nowhere in this expression; a confident wrong answer costs ρ. On the same run,
the two readings separate:

```
v0.1 gross : 93.3
v0.2 net   : 86.7      HG1, same pass rate and no false completions: 93.3
```

`tools/score_hlis.py --gross` reproduces the v0.1 number, so the difference is
auditable rather than asserted.

## 4. Dimensions with no evidence are omitted, not zeroed

v1.3 §13.11 says a singleton omits O from D rather than setting it to zero.
`tools/score_hlis.py` now enforces it: a component passed as `null` is dropped
from D and **named in the output**, with a warning that a score over a subset is
not comparable with one over the full set. A genuine zero still forces the
product to zero, which is the intended hard signal.

## 5. The validator checks claims, not counts

`tools/validate_library.py` now verifies that every binding names a real
benchmark, that `bound` rows carry an implementation and non-bound rows do not,
that `band_only` is excluded from the runnable count, and that the run-log schema
requires `harness_accepted`. A library that claims it can run something it cannot
is worse than one that claims nothing.

---

## What v0.2 still does not have

- **Four of five dimensions.** C, I, O and SA have no runnable suite. Everything
  measured here is DI.
- **HG4 and above.** The ladder is built to HG3. HG4–HGΩ remain specifications,
  so `HIL-Level` above 3 is not assessable with this library.
- **One intervention budget.** All runs are at H1 — governance only, no cognitive
  help. A one-column surface cannot show the frontier moving leftward, and
  `F_A(H0,p)` and `F_A(H2,p)` are unmeasured.
- **One model, small samples.** Two seeds per class. Readings, not rates.
- **Sealed certification.** The `certification_hidden` split is still unsealed
  here; a certification run needs it held by someone the pair cannot write to.
