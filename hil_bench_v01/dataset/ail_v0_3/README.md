# AI-Level Bench Development Dataset v0.9 — the cell grid

`cells.jsonl` holds one record per level of every ladder (C, C^GUI, GP, I, M, O, SA, T, H, DI, HG, U) in the style of I: construct as a contrast, prerequisite, witness with a control arm, named factors each with the locus that computes it, the gate, the law's constants, the kind of key, the generator that exists for it, and a `status` — `runs` (generator + verifier in the package), `forms` (public forms + reference scorer, no runner yet), `specification` (law fixed, no secure environment yet). `coverage.csv` is regenerated from it. `HG_Bench/hg_conform_public_seeds.json` is a real run of the offline HG0–HG2 conformance probe. Every v0.8 record (HIL-Method-1.0 grammar) is carried unchanged; `method` in a cell names the v0.8 `canonical_method` of the same cell.

---

# AI-Level Benchmark Dataset v0.3

Public development dataset for **AI-Level Bench v0.3**, grounded in **Unified Intelligence Theory and the Artificial Intelligence Level v2.6**.

## Cumulative structure

The dataset distinguishes five measurement structures:

1. **Hard cumulative capability ladders:** `C`, `I`, `M`, `O`, positive `SA1-SAΩ`, and `U`.
2. **Cumulative diagnostic sub-ladder:** `GP0-GP5` (GUI Perception). GP is inside the GUI/screen domain of C but never promotes `C^GUI`, `C`, or `U`.
3. **Cumulative delegation frontier:** `DI` requires every lower `T` band at the same `H` ceiling and reliability `p`.
4. **Ordered non-cumulative axes:** `T` classifies task structure; `H` classifies human cognitive intervention.
5. **Cumulative engineering ladder:** `HG` is a strict mechanism-superset reference harness ladder, not an intelligence family.

`SA0` is a baseline category (absence of a reliable grounded self-model), so SA retention begins at `SA1`.

## GP law

`GP5 => GP4 => GP3 => GP2 => GP1 => GP0`

`A |= GP_g iff V_GP,g(A)=1 and K_GP,<g(A)=1`.

The cumulative GP result is diagnostic only. A native-image `C^GUI` form may declare a minimum GP prerequisite that can block that form, but GP evidence cannot earn C credit.

## Main files

- `cumulative_policy.json` - normative typed cumulative semantics
- `canonical_method_catalog.jsonl` - canonical method records including six GP cumulative methods
- `ai_level_bench_public_dev_combined.jsonl` - combined public forms
- `method_style_contract.json` - AI-Level-Method-1.0 plus cumulative semantics
- `gui_perception_lattice.json` - cumulative GP sub-ladder
- `coverage.csv` - method/public-form coverage
- `validation_report.json` - parse, schema, and cumulative-policy checks

## Certification boundary

This is public development material. Official certification requires protected anchors and fresh hidden witnesses under the same canonical laws.
