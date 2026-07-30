# One Chat Box, Five Agents

**Designing the Manager-Fronted SARSI Console: Per-Agent Self-Awareness, Nested Workspaces, and the Four Channels by Which Agents Affect Each Other**

PDF: [`../SARSI_Console_Design_One_Chat_Box_Five_Agents.pdf`](../SARSI_Console_Design_One_Chat_Box_Five_Agents.pdf) (33 pp).

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

## Rules the product must honour

- Claims are rendered at their authority — *verified* / *recorded* / *I think* — without making the user learn the ladder
- Creation is not authorization: a task needing absent authority fails **at authorship**, naming the missing grant, not mid-run after spending budget
- No jump around an intermediate agent: entering `sarsi-claude` enters the machine agent first, or the interface has laundered authority
- Structural change to another agent still requires that agent's own frozen evaluator

## Build order

§10 gives the order, and the first item is the typed directive — because a jump *is* a directive, and because it is the point at which the cross-write prohibition stops being free. It must be written together with its enforcement, not before it.
