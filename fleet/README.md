# A Manager Is Not a Controller

**Global-Workspace Coordination for SARSI Fleets: Bidirectional Influence, Owner Pre-emption, and Why a Manager May Not Write Another Agent's Self-State**

Read the PDF at [`../SARSI_Manager_Is_Not_A_Controller.pdf`](../SARSI_Manager_Is_Not_A_Controller.pdf) (14 pp). Submission guide: [`ARXIV.md`](ARXIV.md).

| File | Purpose |
|---|---|
| `main.tex` | LaTeX source |
| `references.bib` | Bibliography — kept for regeneration, not shipped |
| `main.bbl` | Pre-built bibliography, shipped in the tarball |
| `sarsi-manager-arxiv.tar.gz` | arXiv upload package |
| `ARXIV.md` | Submission guide |

## What it argues

*Functional Self-Awareness for Hierarchical SARSI Multi-Agent Systems: Version 3.0* specifies the manager–specialist architecture this paper builds on, and calls the manager an **executive-control hub**. That description is natural, and it invites a design the architecture's own invariants forbid: a manager that holds an estimate of each specialist's state and, on disagreement, resolves toward its own — writing the result into the specialist's model of itself.

The paper argues the manager is not a controller, on three grounds already present in the base architecture. Specialists filter what the manager sends through their own admission masks, so influence is *offered*, not applied. The coupling is recurrent, so the manager's own state is revised by the agents it coordinates. And neither party is sovereign, since owner pre-emption outranks both. Global workspace theory, which the base architecture draws on, has no homunculus directing specialized processors — only a bounded broadcast channel they compete for.

## The main result

The governance prohibition and the stability condition turn out to be **the same constraint**, and this is the reason to care.

Version 3.0 requires `ρ(J_σ(A_hier + C_rec + G_pred J_g)) < 1`, where `C_rec` carries manager–specialist coupling in both directions. Under the base paper's own bias invariant — a directive may change precision, attention, and evidence order, but not the conditional mean of any specialist estimator — the **top-down block of `C_rec` vanishes** in the mean linearization (Proposition 2). The block is then strictly triangular, `C_rec² = 0`, and `ρ(C_rec) = 0`.

Two consequences:

- **Stability is independent of fleet size** (Corollary 1). The condition becomes block-diagonal by agent, so an operator who has verified each agent individually has verified the hierarchy. Adding specialists adds blocks, not eigenvalues.
- **Cross-write reinstates the loop** (Proposition 3). If the manager may write specialist coordinates through a projection `P ≠ 0`, then `ρ(C_rec)² = ρ(C_{M←J} P)`, the condition no longer decomposes, and stability must be bought by bounding `γ‖P‖` — a tuning exercise sensitive to fleet size.

The prohibition does not *bound* the loop. It *removes* it. A designer indifferent to governance should still refuse the write, for reasons available in the spectral radius.

§5 is explicit about the limits: this is a first-moment argument near an operating point, under the same assumptions the base paper's own stability condition carries. It says nothing about variance, which is why report storms remain a live failure mode in §8.

## Three further results

- **A manager cannot certify a specialist** (Proposition 1). A cross-agent claim is model inference on the evidence ladder, below the specialist's own instrumentation — *regardless of seniority in the authority chain*. Being higher in a permission lattice is not an epistemic qualification. Table 2 gives the per-coordinate exception: a manager is authoritative about **what it asked for** (mission, contract, delegation records) and never about **how well the specialist does it**.
- **Delegation intersects, never unions** (Invariant 5). Otherwise a fleet's effective authority becomes that of its most privileged member, reachable by anyone who can route to it — a laundering route invisible to a per-agent audit, since every individual action lies within its own actor's ceiling.
- **An owner interrupt pauses but never edits** (Proposition 4). A state-writing interrupt is, from inside the affected agent, indistinguishable from an overstepping manager: same coordinate, same absence of provenance, same bypass of the admission mask. No predicate the agent can evaluate separates them, and neither can an auditor reading the log.

## Relation to the rest of the repository

| Paper | Scale | Question |
|---|---|---|
| [`../arxiv/`](../arxiv/) | System | How far has recursive self-improvement propagated across substrate domains? |
| [`../self_awareness/`](../self_awareness/) | Agent | What must one agent know about itself, and who may be justified in trusting it? |
| **this paper** | **Fleet** | **What may one agent assert about another, and what does forbidding it buy?** |

The through-line is one rule at three scales. The system-scale paper argues authority closure requires an evidence base. The agent-scale paper supplies that base and shows the promoter must not be the proposer. This paper is the same claim with one word changed: an agent's statements about *another* agent must be evidence-linked, and they almost never are.

## Standalone, not a continuation

An earlier draft was written as §§20–29 continuing the base paper's own section and equation numbering. This version is standalone — its own numbering, with §2 reproducing the carried-over objects in one table. A submission that opens at §20 and refers to equations 1–32 appearing nowhere in it is hard to review and easy for a moderator to bounce.

## Deployment status

§9 says plainly what is built and what is not. Owner pre-emption exists with all three properties. The shared workspace does not: bottom-up influence currently reaches the manager only through the owner, and the top-down bias is not implemented. The prohibition holds today because no cross-write channel exists, not because one is policed — so Corollary 1 is a claim about an architecture, not a measurement of a running fleet.
