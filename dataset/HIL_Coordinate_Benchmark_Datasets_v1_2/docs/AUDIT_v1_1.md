# What the item audit found in v1.1

`tools/audit_items.py` was written for v1.2 and run first against v1.1
unchanged. It reported **45 errors**. v1.1's own `validate.py` passes the same
tree with zero — it checks that ids are unique and that each row's coordinate
matches its file, both real checks, and neither of them asks whether an item can
do the job it is filed under.

## 1. A ladder that was one rung repeated

| Family | Items | Distinct payloads |
|---|---|---|
| causal_reasoning | 32 | **1** |
| factuality_calibration | 32 | 3 |
| logical_reasoning | 32 | 6 |
| abstract_rule_induction | 32 | 8 |

The causal family shipped a single payload — a three-node graph and the question
"which descendants can change because of do(A)?" — filed at **all eight levels,
C0 through CΩ**. A system that answers it is certified at every level of that
family at once. `S(C0)` and `S(CΩ)` were the same measurement reported eight
times.

Five other C families (coding, long context, multimodal, quantitative,
scientific) had 32 distinct payloads each and were unaffected.

## 2. Static items at levels that deny static answers

Twenty further items were bound exact-match questions filed at C5, C6 and CΩ.
C5 is discovery and C6 and CΩ are open-ended: a fixed question whose answer is
written down in advance cannot be evidence for any of them, because the answer
existing in advance is precisely what those levels deny. The item may be hard;
hardness is not the property being claimed.

## What v1.2 does about it

**The four collapsed families are regenerated from a reference implementation,
not rewritten by hand.** `tools/c_ladder.py` builds each item and *computes* its
key. Five levels now ask five materially different questions:

| Level | causal | logic | factuality | induction |
|---|---|---|---|---|
| C0 | reachability, 3 nodes | one rule | one source, or none | constant difference |
| C1 | reachability, branching | a chain of four | a retracted source | constant ratio |
| C2 | common causes | conjunctive conditions | two live sources by date | alternating steps |
| C3 | adjustment set | non-entailment | a citation of a retracted source | each term from two |
| C4 | what not to condition on | case analysis over a disjunction | nothing survives the chain | a conditional step rule |

All 80 cells (4 families × 5 levels × 4 variants) are distinct in payload.

**Keys are computed, never asserted.** `audit_items.py` recomputes every key it
can from `KEY_FUNCTIONS` and fails the build on disagreement. Corrupting one
causal key to `{"confounders": ["U"]}` produces:

```
ERROR: C-C2-CAUSA-01: the key says {"confounders": ["U"]},
       the reference computes {"confounders": ["U", "W"]}
```

This matters because hand-written keys are how four defects entered a sibling
suite, every one of them found only when a measurement looked wrong.

**All 68 discovery-level static items become `specification-only`** with
`scoring_type: protocol` and `verifier: sealed-longitudinal`, pointing at the
evidence those levels actually need: a mechanism generated after the system was
frozen and scored on prediction outside the range it was fitted on, or a
longitudinal trial under sealed external evaluation.

The consequence is worth stating plainly rather than hiding in a count: **this
library now contains no runnable evidence for C5 and above.** That is a true
description of where it stands, and it is more useful than 68 items that
appeared to supply some.

## What the audit does not establish

- It is a filter with unknown recall. Items it did not flag are unaudited, not
  validated.
- It compares payloads for exact identity; two items differing only in a
  variable name are as undiscriminating as identical ones and are not flagged.
- `key_recomputable` covers only the four families that ship a reference. The
  other 1,150 items still have asserted keys, and nothing here has checked them.
- Thirty-three within-level duplicate payloads remain as notes rather than
  errors — mostly GUI-perception items paired across two observation channels,
  where sharing a payload is the design. They are listed so a reader can judge
  that rather than take it on trust.
