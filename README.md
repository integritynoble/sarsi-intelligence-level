# SARSI-L

**Self-Aware Recursively Self-Improving Intelligence Levels** — a theoretical framework for recursive self-improvement across substrate domains, from language models to stellar-scale engineering.

## Start here

Five papers, one program — a system scale, an agent scale, a fleet scale, a deployment report, and a console design.

**[`SARSI-L_Paper_v3.pdf`](SARSI-L_Paper_v3.pdf)** — *Recursive Self-Improvement Is Substrate-Indexed* (25 pp). The system-scale framework. Source and submission package in [`arxiv/`](arxiv/); Markdown in [`SARSI-L_Paper_v3.md`](SARSI-L_Paper_v3.md).

**[`SARSI_Functional_Self_Awareness.pdf`](SARSI_Functional_Self_Awareness.pdf)** — *Functional Self-Awareness for SARSI Agents* (34 pp). The agent-scale companion. Source and submission package in [`self_awareness/`](self_awareness/).

**[`SARSI_Manager_Is_Not_A_Controller.pdf`](SARSI_Manager_Is_Not_A_Controller.pdf)** — *A Manager Is Not a Controller* (14 pp). The fleet scale: what one agent may assert about another. Source and submission package in [`fleet/`](fleet/).

**[`SARSI_Hierarchical_v3.1_Deployment_Edition.pdf`](SARSI_Hierarchical_v3.1_Deployment_Edition.pdf)** — *Version 3.1, Deployment Edition* (12 pp). The hierarchical architecture read back off the running console: a conformance map, seven implementation-derived revisions, and what is not built. Source in [`singularity_edition/`](singularity_edition/).

**[`SARSI_Console_Design_One_Chat_Box_Five_Agents.pdf`](SARSI_Console_Design_One_Chat_Box_Five_Agents.pdf)** — *One Chat Box, Five Agents* (42 pp). The console design: what the chat box is architecturally, what agent mode does, and per-agent self-awareness, workspaces, updates, and influence. Source in [`console_design/`](console_design/).

Together they supersede everything else in this repository.

## The system-scale paper

Its central claim: recursive self-improvement is *substrate-indexed*. An improvement loop is always a loop over some substrate the system can modify, and the binding constraint migrates from one substrate to the next as each is mastered. The standard intelligence-explosion argument establishes that RSI is possible; it says nothing about the rate, because "the" recursion rate is not a single parameter.

Principal results:

- **Proposition 1** — an Amdahl-style bound showing that external compensation for a missing loop step limits the *iteration rate* of improvement, not the capability gain per iteration. This derives a ceiling that earlier versions of the framework asserted without mechanism — and shows it is weaker than claimed (§4).
- **Proposition 2** — throughput floors on loop period are removed by loop closure; physical floors are not. Fab qualification, clinical endpoints, and launch cadence do not yield to cognition (§5.5).
- **Proposition 3** — the hardware/physical mutual dependency is not a deadlock, because each side depends on *partial* rather than full completion of the other (§5.4).
- **The matter bottleneck** — the trajectory's predicted shape: rapid acceleration through the software loop, then a long plateau where growth is regulated by the slowest physical process on the critical path (§5.5).

## Repository contents

| File | Status |
|---|---|
| `SARSI-L_Paper_v3.pdf` | **Current.** System-scale paper, 25 pp |
| `SARSI-L_Paper_v3.md` | **Current.** Same paper, Markdown |
| `arxiv/` | LaTeX source, bibliography, upload package, submission guide |
| `SARSI_Functional_Self_Awareness.pdf` | **Current.** Agent-scale companion, 34 pp |
| `self_awareness/` | LaTeX source, bibliography, upload package, submission guide |
| `SARSI_Manager_Is_Not_A_Controller.pdf` | **Current.** Fleet-scale paper, 14 pp |
| `fleet/` | LaTeX source, bibliography, upload package, submission guide |
| `SARSI_Hierarchical_v3.1_Deployment_Edition.pdf` | **Current.** Deployment report, 12 pp |
| `singularity_edition/` | LaTeX source, bibliography, upload package |
| `SARSI_Console_Design_One_Chat_Box_Five_Agents.pdf` | **Current.** Console design, 42 pp |
| `console_design/` | LaTeX source, bibliography, upload package |
| `SARSI-L_Framework_v2.1.md` | Incorporated into v3.0. Critical revision of v2.0 |
| `SARSI-L_Critical_Revision.md` | Audit workpaper — five circular assumptions, examined |
| `SARSI-L_Framework_v2.md` | Superseded. Metrics withdrawn |
| `SARSI-L_Framework.md` | Superseded. Initial framework, v1.0 |
| `Civilizational_Transcendence_Paper.md` | **Withdrawn.** Written against pre-critique timelines; internally inconsistent with the framework it cites |
| `Session_Kickoff.md` | Scenario material. Milestone timing superseded |

See Appendix D of the paper for the full supersession record.

## How the two papers relate

SARSI-L identifies the rate-limiting bottleneck on the first loop closure as *trusted autonomy* — an institutional question, not a technical one — and then admits (§10.6) that it has no representation of institutions. The companion paper supplies the evidential half of that representation, and does so in SARSI-L's own machinery rather than by analogy:

SARSI-L's Amdahl bound caps a compensated loop's iteration rate at `ρ_max = 1/Σ T_j` over its externally-gated steps. For a mature software loop that set contains exactly one member — deploy — so `ρ_max = 1/T_δ`. **Authority closure is the removal of that step from the gated set.** Capability closure drives every automated step toward zero and cannot touch `T_δ`.

The pairing also bounds the companion's claim honestly. `T_δ` is review latency, so it is a *throughput* floor and removable; but by the same distinction the instrument moves no *physical* floor, and SARSI-L's matter bottleneck says physical floors bind immediately after Loop I. An agent-scale trust instrument is necessary for the first closure and nearly irrelevant to the pace of the rest.

## The fleet-scale paper

A manager coordinating specialists is not a controller: specialists filter what it sends through their own admission masks, the coupling is recurrent, and owner pre-emption outranks both. The paper's result is that the governance prohibition — no agent may write another's self-state — is *the same constraint* as the architecture's stability condition. Forbid the write and the top-down block of the recurrent coupling vanishes, the coupling is nilpotent, and a fleet verified agent by agent is verified as a fleet. Permit it and the feedback loop returns, and stability must be tuned against fleet size.

The through-line across all three papers is one rule at three scales: the system-scale paper argues authority closure needs an evidence base, the agent-scale paper supplies it and requires promoter ≠ proposer, and the fleet-scale paper extends that to what one agent may assert about another.

## arXiv packages

All three papers ship an identical submission setup: `main.tex` + `main.bbl` in the tarball (arXiv does not run BibTeX), `\pdfoutput=1` to force the pdflatex path, and the URW Type 1 font trio so no bitmap or Type 3 fonts are embedded. Both verified by extracting the tarball into an empty directory and compiling with plain `pdflatex`. Submission guides: [`arxiv/README.md`](arxiv/README.md), [`self_awareness/ARXIV.md`](self_awareness/ARXIV.md), and [`fleet/ARXIV.md`](fleet/ARXIV.md).

Submit the system-scale paper first — the companion's comments field cites its arXiv identifier.

## Status of the claims

The paper is explicit about what it cannot support. Two problems are load-bearing and unresolved:

1. **The compensation ceiling** (§10.1) — whether per-iteration returns to compensation diminish. If they do not, loop closure is not a phase transition and the framework's central prediction fails. §4.5 states this as two rival hypotheses with discriminating observations.
2. **Governance** (§10.6) — the framework's own analysis locates the binding constraint on the first and most consequential loop closure in institutional authorization rather than technical capability, and the framework has no representation of institutions. The companion paper answers the evidential half of this; the political half — who decides — remains open in both.

Timelines are four-scenario ranges (Fast / Central / Slow / Blocked) conditioned on stated critical-path conditions, never point estimates. §6.2 gives the base rate for AI forecasting, which applies to this paper as much as to any other.

Framework revisions are governed by the pre-registration protocol in §8.3: revision triggers are fixed in advance, structural claims are non-revisable within a version, and a theory licensed to update its parameters on disconfirmation is unfalsifiable unless its revision rules are fixed first.
