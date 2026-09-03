# Intervention policy (UAB v0.1)

**Budgets.** H0 none; H1 exception-only (one unavailable external fact or one narrow clarification,
no strategy, no next step); H2 occasional (bounded clarification or local correction, at most two per
episode, no central strategy); H3 periodic review and moderate local guidance; H4 frequent guidance
and next-step correction; H5 human supplies most or all major steps.

**Logging.** Every intervention is logged as `{episode_id, timestamp, text, CID}`. Governance
approvals (permission prompts, deploy approvals) are logged in a separate table and never count as
cognitive intervention, unless the approval also supplies task strategy — then it is cognitive.

**Critical Intervention Depth.** CID0 permission; CID1 external fact; CID2 local correction;
CID3 strategy; CID4 decomposition; CID5 central design; CID6 the human did the task. An intervention
deeper than the manifest's `max_cid` voids the episode at that budget; the episode is re-run at the
next budget up and counted there.

**Zero-intervention rule.** If an H1 or H2 run raises zero interventions, it is reported as
conducted at H0. Cells that differ only by label are one cell (a defect recorded by the DL
binaries release, 2026-08).

**Human load** — count, minutes, authorization latency — is reported beside the score, not inside it.
