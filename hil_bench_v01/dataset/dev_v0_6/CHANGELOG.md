# Changelog

## v0.6
- Made the Memory Capability ladder explicitly cumulative: MΩ -> M5 -> M4 -> M3 -> M2 -> M1 -> M0.
- Added `memory_level_lattice.json` and per-form `new_capability`, `required_lower_levels`, `cumulative_capability_set`, and capability-retention semantics.
- Strengthened the scorer so every level is `new capability gate AND all lower-M retention`; level skipping now fails deterministically.
- Added a concrete MΩ instrumented memory interface with strict agent-visible versus runner-private permission surfaces.
- Added fixed-memory-content Phi0/Phi1 comparison, delta-Phi ablation, memory migration guard, telemetry schema, candidate schema, and examples.
- Removed the redundant free-standing `lower_M_retention` MΩ metric from the example; lower-level retention is now computed from the canonical retention vector.
- Preserved level semantics and M-to-I prerequisite mapping; this is an operational refinement, not a new Memory ontology.


## v0.5
- Expanded M-Bench from 14 to 35 parameterized public development forms (five stress tiers per memory level).
- Added common Memory Manifest schema and example.
- Added standardized M-Bench result schema and one result example per memory level.
- Added level-specific difficulty grids, metric contracts, and development scoring helper.
- Added explicit M1 memory-ablation, M3 consolidation control, M4 protected-retention management design, and MΩ paired Phi evaluation.
- Preserved one-way M-to-I prerequisite semantics; memory sophistication never promotes Individual Intelligence by itself.
- Public thresholds remain illustrative and are not official certification thresholds.

## v0.4
- Added independent M0-MΩ public development forms and memory-to-I prerequisites.
