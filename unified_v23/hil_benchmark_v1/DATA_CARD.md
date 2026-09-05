# HIL-Core v1 data card

## Summary

HIL-Core v1 contains deterministic parameter specifications for six compact
mechanism families in each split: C, I, O, DI, SA, and supporting M. Each full
split has 25 tasks (22 applicable to an individual); quick mode selects 8 or 7.
All content is English and structured JSON. No personal data is used.

## Split policy

Development and validation specs and keys are public. They support debugging,
generator/key consistency checks, and transparent scoring. They must not be used
for a hidden leaderboard claim. Certification material is stored under a
separate organizer-only tree. Its families and solution mechanisms—not merely
its random seeds—are disjoint from public content. The release builder uses an
allowlist and verifies that no organizer-private member enters the archive.

The included private bank is an example organizer bank for the accompanying
paper artifact. Anyone who receives this source tree must consider that bank
exposed; a real public competition must deploy a separately held, rotated bank
that has never been shipped to participants.

## Intended use

- test the HIL reporting and model--harness curve contract;
- compare frozen configurations under identical splits and resource policies;
- develop new, audited task families without changing score semantics silently;
- provide a fast preflight before costly longitudinal evaluation.

## Out-of-scope and prohibited interpretations

Do not describe quick results as certification. Do not compare individual-track
HLIS directly with organization-track HLIS. Do not attribute a pair score to the
base model alone. Do not turn N/A or unassessed into zero. Do not claim that the
small synthetic tasks establish general intelligence, persistent learning,
consciousness, open-ended autonomy, or replacement of ARC-AGI.

## Known limitations

The task count is too small for stable rankings; public mechanisms are easily
contaminated; exact-match grading omits partial credit; human baselines and item
response calibration are absent; most tasks are symbolic proxies; simulated
restart fields are not genuine process-restart evidence; DI has one item per
cell; U3+ is uninstrumented; cost and token reports depend on candidate honesty;
and confidence intervals do not include model stochasticity unless evaluators
repeat runs. O tasks test role allocation proxies, not emergent organizations.

Before operating a consequential leaderboard, add first-contact human studies,
multiple independent items per cell, repeat attempts, real persistence and
longitudinal protocols, sealed execution, contamination monitoring, independent
cost accounting, accessibility review, cross-tier concordance audits, and a
published incident/rotation policy.

## Maintenance

Every task-family change requires specification--key consistency tests. Audit
items that materially different systems fail identically before blaming the
systems. Version score or threshold changes. Retire and replace suspected leaked
private families; never patch a key after inspecting candidate identities
without invalidating affected runs.
