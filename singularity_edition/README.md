# Hierarchical SARSI, Version 3.1 — Deployment Edition

**What Building It Changed** — an implementation-grounded revision of Version 3.0, written from the console running at `singularity.comparegpt.io`.

PDF: [`../SARSI_Hierarchical_v3.1_Deployment_Edition.pdf`](../SARSI_Hierarchical_v3.1_Deployment_Edition.pdf) (12 pp).

| File | Purpose |
|---|---|
| `main.tex` | LaTeX source |
| `references.bib` | Bibliography — kept for regeneration, not shipped |
| `main.bbl` | Pre-built bibliography, shipped in the tarball |
| `sarsi-hierarchical-v31-arxiv.tar.gz` | arXiv upload package |

Verified clean-room: extracts to an empty directory, compiles with plain `pdflatex`, no BibTeX run — no errors, no undefined references, no missing files, zero Type 3 fonts, 12 pages.

## Why this edition

Version 3.0 is a complete architecture. What it cannot do is say **which of it is real** — and that matters here more than usual, because the architecture's central claims are *prohibitions*. A prohibition is satisfied trivially by a system that lacks the mechanism it forbids, and a reader cannot tell from the specification whether an invariant is *enforced* or merely *unviolated*. This edition separates the two everywhere it can.

It is written for three readers, and says so up front: if you are **extending** the system, §3 is the map; if you are **evaluating** the architecture, §4 is where the spec was wrong and §7 where it is unrealised; if you are **auditing**, §5 lists every prohibition as a test name so it can be checked rather than believed.

## What's in it

**A conformance map (§3).** Every equation and invariant of Version 3.0 traced to the module, function, and test that implements it — or marked *not built*. Fifteen rows; five unimplemented, and the paper says plainly that they are not the easy five: the predictive dynamics, the interrupt state machine, and the algorithms are what make the architecture a control system rather than a communication channel.

**Seven implementation-derived revisions (§4).** Each records something the specification described in purpose but not at its edges:

1. **A shared workspace is the wrong object** — the first fleet channel was built as one shared workspace, which Version 3.0's own Invariant 4 forbids. Corrected in place to a nested one via `project_for_specialist()`. This is the case where the specification earned its cost: the shared design was simpler, passed its own tests, and would have shipped.
2. **An unmeasured reliability is the prior mean, never zero** — the natural implementation (successes ÷ attempts) is undefined at zero and gets coerced, usually to 0. Zero reads as *this specialist fails*, and the specialist is then never ranked highly enough to earn the outcomes that would correct it. Self-fulfilling in both directions.
3. **Bounding a round ≠ bounding storage** — the per-agent cap `κ_a` bounds attention, not disk. Three bounds are needed where the paper gives one.
4. **An admitted report must be consumed** — otherwise it is re-admitted every round forever. Passes a one-round unit test; fails only under sustained operation.
5. **Nothing may be dropped silently** — a truncated view that doesn't announce its truncation reads as complete, and absence of contradiction reads as consensus.
6. **The softmax need not be computed to be used** — monotone in its logits, so ranking uses the raw score. The normalisation *is* needed where the aggregate matters, and presenting one expression for both uses invites the error.
7. **Grouping two interrupt classes into one branch under-specifies both** — steering and mission revision share a mechanism and differ in what happens to completed work and verdict validity. Should be six classes, not five.

**Invariants as executable objects (§5).** Twelve named tests, listed so a reader can check the paper's claims. The most important is `broadcasting_never_writes_another_agents_self_state`.

**Two corpus/runtime divergences (§6),** reported rather than silently reconciled:

- **Four ceilings, not five — and the top one is *earned*.** The deployed top ceiling is unlocked by a trust ledger requiring verified approvals against a threshold with zero forbidden trips; the console *refuses* to set it directly rather than silently capping. This is a stronger mechanism than the specification describes, and the paper argues it should be lifted into the architecture: the base invariant forbids a bad route to authority, and an earned ceiling supplies the good one — in the same currency everything else uses, verified outcomes.
- **The repertoire has `recover` and lacks `use tool`.** Not a naming difference. Recovery acts on the agent's own resource coordinate rather than on the task, and belongs in the repertoire for the same reason abstention does. The deployed control code selects it with reference to a self-state coordinate by name — which is the only arrangement in which functional self-awareness earns the word *functional*.

## The honest part

§7 lists what is not built, in dependency order, and §8 states the status plainly:

> The architecture's strongest claims are currently free. No agent writes another's self-state because there is no channel that could. Delegated authority cannot be laundered because there is no delegation.

The first unbuilt item — the typed downward directive — is also the point at which the cross-write prohibition stops being structural and must become enforced. The paper's recommendation is that it be written together with its enforcement rather than before it.

## Relation to the rest of the repository

| Paper | Scale | Question |
|---|---|---|
| [`../arxiv/`](../arxiv/) | System | How far has recursive self-improvement propagated across substrates? |
| [`../self_awareness/`](../self_awareness/) | Agent | What must one agent know about itself? |
| [`../fleet/`](../fleet/) | Fleet | What may one agent assert about another? |
| **this paper** | **Deployment** | **Which of it is actually real?** |
