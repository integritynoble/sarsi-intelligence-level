# HIL Coordinate Benchmark Datasets v1.2

Aligned to Unified Intelligence / HIL **v1.9**. Everything in v1.1 is carried
forward. What v1.2 adds is the part that checks whether the items can measure
what they are filed under.

## What the audit found in v1.1

`tools/audit_items.py`, run against v1.1 unchanged, reports **45 errors**. v1.1's
own `validate.py` passes the same tree with zero, because it asks a different
and also-real question: are ids unique, do coordinates match their file.

The headline: **the causal-reasoning family shipped 32 items with one distinct
payload**, the same three-node graph question filed at all eight levels from C0
to CΩ. Three more C families collapsed nearly as far. A system answering that
one question was certified at every level of the family at once.

Full write-up, including what v1.2 does about it and what the audit still cannot
see: [`docs/AUDIT_v1_1.md`](docs/AUDIT_v1_1.md).

## What changed

- **Four C families regenerated from a reference implementation.**
  `tools/c_ladder.py` builds each item and *computes* its key. Five levels now
  ask five materially different questions, and all 80 cells are distinct.
- **Keys are recomputed by the audit**, not trusted. Corrupting one key fails
  the build with both values printed.
- **68 static exact-match items at discovery and open-ended levels are now
  `specification-only` / `protocol`.** A fixed question whose answer is written
  down in advance cannot be evidence for a level defined by not having one. The
  consequence, stated plainly: this library now contains **no runnable evidence
  for C5 and above**, which is a true description of where it stands and more
  useful than 68 items that appeared to supply some.
- **GUI items carry `gp_level`.** GP is a subscale of C and its levels are not C
  levels: a previously unseen layout is legitimate static evidence for GP5,
  while nothing static is evidence for C5. The rows now say which claim they
  support instead of leaving the C number to be read at face value.

## Tools

| Tool | Purpose |
|---|---|
| `validate.py` | ids unique, coordinates match their file |
| `audit_items.py` | ladders distinct across levels, keys recomputable, no static items at discovery levels, GP levels labelled |
| `c_ladder.py` | reference implementation and generator for the four regenerated C families |
| `verify_development_item.py` | exact-match check for one development item |

Both validators exit non-zero on findings and belong in CI.


---

## v1.1 README (retained)

# HIL Coordinate Benchmark Datasets v1.1

Aligned to the HIL/Unified Intelligence framework v1.8.

## Core measured coordinates
C, I, O, T, H, SA. Delegation Intelligence is derived from T × H × p.

## New in v1.1: independent Memory Capability
Memory Capability **M** is now benchmarked independently as a **supporting coordinate**.
It is not a sixth conceptual intelligence family and is excluded from default HLIS.

Formal relationship:
`I(A) >= I_n  =>  M(A) >= mu_n`
The converse does not hold.

This means a system may validly be **I1/M4**, for example: excellent durable/self-managing memory
without adaptive learning or self-improvement.

## Dataset sizes
- C-Bench: 320
- I-Bench: 168
- O-Bench: 126
- T-Bench: 256
- H-Bench: 180
- SA-Bench: 192
- M-Bench (supporting): 168
- DI T×H cells: 1536
- GUI Perception image subset: 32

## I prerequisites
I0>=M0; I1>=M1; I2>=M3; I3>=M4; I4>=M4; I5>=M5; IΩ>=M5.
Require MΩ only when memory-architecture evolution itself is part of the IΩ claim.

## Validity
Specification-key consistency, cross-tier concordance audit, graded scoring/failure modes,
and per-coordinate headroom remain mandatory.
