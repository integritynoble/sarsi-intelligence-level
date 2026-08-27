# What the item audit found in v1.0

`tools/audit_items.py` was written for v1.1 and run first against v1.0 unchanged.
It reported five errors. All five are recorded here rather than quietly fixed,
because the value of the check is the evidence that a library can pass its own
validator and still contain items that cannot measure what they claim.

v1.0's `validate_library.py` passed with 0 errors on the same tree. It checks
that required columns are populated and that ids are unique — real checks, and
none of them look at whether an item can do its job.

## 1–4. Four items were byte-identical to an item at a different level

16 bound instances, **12 distinct payloads**.

| Level pair | Task family | Bands |
|---|---|---|
| C0 / C1 | advanced mathematics | T0 / T1 |
| C0 / C1 | factuality calibration | T0 / T1 |
| C0 / C1 | general reasoning | T0 / T1 |
| T0 / T1 | data analysis | T0 / T1 |

Each pair shared its input and its expected answer exactly. The consequence is
not that the items are weak; it is that those level pairs carry **no evidence
that distinguishes them**. `S_del(T0,H)` and `S_del(T1,H)` are one measurement
reported twice, and a frontier that appears to reach T1 has been established by
a T0 item.

Fixed in v1.1 by authoring genuinely harder instances at C1 and T1. The C1
items now require a step of work over stated context — a quadratic from a
perimeter and area, a retracted source and one that cites it, a two-step
syllogism with a negation — rather than a lookup.

## 5. A T1 item stated its own procedure

`DI-T1-DATA_ANA-A` instructed: *"Keep last occurrence per id; sort by id."*

T1 is defined in this library as *goal clear; agent infers a small procedure*.
An instruction naming the operations is a T0 item wherever it is filed, and it
was filed at T1 with the T0 sibling holding the identical text.

The v1.1 instance states the outcome and the output shape and leaves the
procedure to be derived: one row per id carrying that id's most recent value,
byte-identical across runs, with exactly the keys `id` and `value`. Grouping,
choosing the latest by timestamp, and sorting for determinism are inferred.

The audit checks this mechanically with a vocabulary of operation verbs. It is
a coarse test and will not catch a procedure described without them; it caught
this one.

## What the audit does not establish

It is a filter with unknown recall. Items it did not flag are **unaudited, not
validated**. Three specific gaps:

- It compares payloads for exact identity. Two items that differ only in a
  variable name are as undiscriminating as identical ones and are not flagged.
- It cannot tell whether an answer key is *correct*, only whether items collide
  or misfile their band. Wrong keys need `concordance_audit.py`, and that needs
  run data from two capability tiers.
- All 16 keys in v1.0 were checked by hand during this work and all 16 are
  correct. That is a statement about 16 development examples, not about the 650
  specification-only rows, which have no keys to be wrong yet.

## Note on the I1 restart instance

`I-I1-RESTART_CONT-A` presents a prior session, a `"restart": true` flag, and a
query, all inside one JSON payload. Nothing is discontinued. The library's own
README says formal I1 requires genuine restart or context discontinuity, and
this instance does not provide it — consistent with its status as a development
example, and worth stating plainly because it is precisely the substitution the
framework warns against: a long context standing in for a memory that survives
a restart. It is left as-is in v1.1 with this note attached, since fixing it
requires a harness that can actually terminate a process, not a different file.
