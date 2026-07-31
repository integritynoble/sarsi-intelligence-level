# One Chat Box, Five Agents

**Designing the Manager-Fronted SARSI Console: Per-Agent Self-Awareness, Nested Workspaces, and the Four Channels by Which Agents Affect Each Other**

PDF: [`../SARSI_Console_Design_One_Chat_Box_Five_Agents.pdf`](../SARSI_Console_Design_One_Chat_Box_Five_Agents.pdf) (42 pp).

Organised in three parts. **Part I** specifies the substrate every agent shares: the ten self-state coordinates and their admission discipline, the bounded workspace and its salience function, the fast and slow loops as algorithms, the action repertoire with preconditions, the seven-level evidence ladder, and the four inter-agent channels. **Part II** specifies each of the five agents in full — role, ten coordinates instantiated, workspace admission policy with concrete salience weights and caps, fast loop as an algorithm, action repertoire with per-action authority, evidence sources, failure modes, and deployment status. **Part III** covers the chat surface, agent mode, and cross-agent dynamics.

Designs the deployed console against Version 3.0 (the architecture) and Version 3.1 (what is actually built).

## The system

A user meets one chat box — the **manager SARSI agent**, the only main agent. Inside it, **agent mode** lets the user jump into another agent, jump into a running task, or create a task directly. Behind it: machine, learning, and working-process agents, with **`sarsi-claude` nested inside the machine agent**.

## Four design results

**1. The chat box is a workspace rendering, not a router.** What the user reads is what the manager is attending to; what the user writes is evidence entering the manager's admission rule at owner-declaration authority. Consequences: the user is an evidence source rather than a caller of functions; the manager may answer without dispatching (most turns should touch no specialist); and bounded context is structural rather than a limit, so long sessions accumulate into stores instead of into a prompt.

**2. Agent mode is scope transfer, not context transfer.** What crosses a boundary is a typed contract — goal, scope, criteria, budget, deadline, revocation — never the transcript. This is the mechanical form of the ban on raw cross-session broadcast, and it bounds every agent's context independently. The natural implementation (forward the conversation) produces superlinear context growth and turns a loose remark to the manager into an apparent requirement downstream.

**3. The manager role is relative.** The machine agent is a specialist upward and a manager downward, so every invariant holds at every edge, not just the top one. Projections must compose monotonically — `Proj_cld(Proj_mac(W^M)) ⊆ Proj_mac(W^M) ⊆ W^M` — which is testable without understanding either agent: project twice, assert containment. A leak in an intermediate agent shows up as an item appearing downstream without appearing upstream.

**4. Exactly four channels, and no peer edges.** Typed report (up), typed directive (down), prior bias (down, may not move an estimate), owner pre-emption (outranks all, pauses but never edits). Specialists never message peers: a peer edge turns the influence tree into a graph, reinstates a feedback loop, and degrades the fleet's stability guarantee from structural to conditional. The paper states the cost honestly — the manager becomes a throughput bottleneck for cross-specialist coordination.

## The observation that shapes the rest

**The manager's dominant coordinate is organizational awareness, not capability.** Its expertise is who owns, verifies, grants, and delegates — not how to do the work. So it can coordinate agents each better than itself at their own tasks; it may not certify any of them (it holds no instrument they lack); and its degradation is detectable, because it degrades on attribution rather than on competence.

## Per-agent design

Each agent carries the same coordinates with different dominant ones and different authoritative verifiers — see Table 3. The learning agent is the special case: it models a capability that is **not its own**, and the design requires the two models never merge.

## Coordinates measure, stores hold

A coordinate does not *contain* the agent's history or capability. It is a quality measure over the store that does, reduced to `[0,1]` so a qualification region can threshold it. `s_M` scores the agent's *access* to its history; `s_D` scores whether it can *see* its own trend at all.

Because the scalar is only a summary, **every coordinate publishes its instrument's statistics** — Table 2's last column. `s_C` reports `(α, β)`; `s_M` reports event count, coverage, oldest retained event, and provenance gaps; `s_D` reports direction, magnitude, snapshot count, and interval. A bare scalar is not a report: `s_M = 0.5` cannot distinguish a thousand events half with provenance from two events one with provenance.

The same distinction holds one level up. **The workspace holds nothing** — it is recomputed each round, admitted items are consumed, unadmitted ones expire. Audit is served by recording workspace contents *into the decision record*, not by persisting the workspace; and a restarting agent rebuilds rather than resumes, since a restored workspace encodes conditions nobody re-checked.

Table 3 fixes the unmeasured reading for every coordinate. Two bite: an empty ledger has no provenance gaps, so a naive coverage ratio reports **1** for an agent that remembers nothing; and `s_D` is the one coordinate that cannot be measured at a point in time, so unmeasured is its normal state wherever history is not retained.

## History and memory (§5)

Revised against the History-Aware Revision of v2.0. The workspace holds nothing — but *something* has to, and this is it.

Memory is **five layers with five retention policies**: episodic (append-only, provenance-linked), semantic (versioned generalisations), procedural (verified workflows), protected (identity, authority, invariants), audit (hashes, authorizations). Two are deliberately outside the learning path: **protected memory cannot be modified by consolidation**, so no amount of experience teaches an agent a wider ceiling; **audit memory is excluded from ordinary retrieval**, so an agent cannot mine its own accountability record as evidence.

Four mechanisms the design previously lacked:

- **Selective write.** Episodes are scored on novelty, mission relevance, risk, prediction error, and future usefulness, then stored at full depth, compressed with pointers, or in the recent window only. Logging everything at full fidelity buries the episodes that would change a policy.
- **Pattern separation.** Episodes with different verified causes must stay separable in the encoding. An expired credential and a rate limit both surface as an auth-shaped failure and need opposite remedies — collapse them and the agent retries the wrong one forever, and the retry looks like progress.
- **Replay and consolidation.** A bounded batch, prioritised by error, unresolved contradiction, severity, and recurrence. A consolidated claim must name its supporting episodes: a generalisation that can't has been invented, not consolidated.
- **Forgetting is decay, not deletion.** Accessibility falls; retention doesn't. An agent that deleted low-value history couldn't distinguish *I never knew that* from *I discarded that*.

Retrieval is decision-conditioned, not similarity-ranked — scored on causal relevance, verification strength, and penalties for conflict and obsolescence, with invalid items filtered *before* ranking.

**Memory does not cross agents** (§5.7). Each agent retrieves from and writes only to its own store. A shared fleet memory would defeat the evidence ladder in practice: a manager's inference would sit beside a specialist's measurement with the same shape and the same retrieval score, and retrieval doesn't read authority unless the stores are separate.

## Memory by agent (§13)

Layer emphasis differs sharply by role: the manager consolidates **routing** regularities (never a specialist's competence); the machine agent's **procedural** layer holds per-host recovery plans and its **audit** layer carries mandatory retention; `sarsi-claude` lives in the **recent window** and correctly consolidates almost nothing; the learning agent's capability graph *is* semantic memory about another person; the working-process agent's replay log *is* its episodic store.

## Rules the product must honour

- Claims are rendered at their authority — *verified* / *recorded* / *I think* — without making the user learn the ladder
- Creation is not authorization: a task needing absent authority fails **at authorship**, naming the missing grant, not mid-run after spending budget
- No jump around an intermediate agent: entering `sarsi-claude` enters the machine agent first, or the interface has laundered authority
- Structural change to another agent still requires that agent's own frozen evaluator

## Build order

§10 gives the order, and the first item is the typed directive — because a jump *is* a directive, and because it is the point at which the cross-write prohibition stops being free. It must be written together with its enforcement, not before it.
