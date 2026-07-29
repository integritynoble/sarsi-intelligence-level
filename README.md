# SARSI-L

**Self-Aware Recursively Self-Improving Intelligence Levels** — a theoretical framework for recursive self-improvement across substrate domains, from language models to stellar-scale engineering.

## Start here

**[`SARSI-L_Paper_v3.pdf`](SARSI-L_Paper_v3.pdf)** — the paper, typeset (25 pp).
**[`SARSI-L_Paper_v3.md`](SARSI-L_Paper_v3.md)** — the same paper in Markdown.
**[`arxiv/`](arxiv/)** — arXiv submission package: LaTeX source, upload tarball, and submission guide.

It supersedes everything else in this repository.

Its central claim: recursive self-improvement is *substrate-indexed*. An improvement loop is always a loop over some substrate the system can modify, and the binding constraint migrates from one substrate to the next as each is mastered. The standard intelligence-explosion argument establishes that RSI is possible; it says nothing about the rate, because "the" recursion rate is not a single parameter.

Principal results:

- **Proposition 1** — an Amdahl-style bound showing that external compensation for a missing loop step limits the *iteration rate* of improvement, not the capability gain per iteration. This derives a ceiling that earlier versions of the framework asserted without mechanism — and shows it is weaker than claimed (§4).
- **Proposition 2** — throughput floors on loop period are removed by loop closure; physical floors are not. Fab qualification, clinical endpoints, and launch cadence do not yield to cognition (§5.5).
- **Proposition 3** — the hardware/physical mutual dependency is not a deadlock, because each side depends on *partial* rather than full completion of the other (§5.4).
- **The matter bottleneck** — the trajectory's predicted shape: rapid acceleration through the software loop, then a long plateau where growth is regulated by the slowest physical process on the critical path (§5.5).

## Repository contents

| File | Status |
|---|---|
| `SARSI-L_Paper_v3.pdf` | **Current.** Typeset paper, 25 pp |
| `SARSI-L_Paper_v3.md` | **Current.** Consolidated paper, v3.0, Markdown |
| `arxiv/main.tex` | LaTeX source (author block has placeholders — see `arxiv/README.md`) |
| `arxiv/sarsi-l-v3-arxiv.tar.gz` | arXiv upload package |
| `SARSI-L_Framework_v2.1.md` | Incorporated into v3.0. Critical revision of v2.0 |
| `SARSI-L_Critical_Revision.md` | Audit workpaper — five circular assumptions, examined |
| `SARSI-L_Framework_v2.md` | Superseded. Metrics withdrawn |
| `SARSI-L_Framework.md` | Superseded. Initial framework, v1.0 |
| `Civilizational_Transcendence_Paper.md` | **Withdrawn.** Written against pre-critique timelines; internally inconsistent with the framework it cites |
| `Session_Kickoff.md` | Scenario material. Milestone timing superseded |

See Appendix D of the paper for the full supersession record.

## Status of the claims

The paper is explicit about what it cannot support. Two problems are load-bearing and unresolved:

1. **The compensation ceiling** (§10.1) — whether per-iteration returns to compensation diminish. If they do not, loop closure is not a phase transition and the framework's central prediction fails. §4.5 states this as two rival hypotheses with discriminating observations.
2. **Governance** (§10.6) — the framework's own analysis locates the binding constraint on the first and most consequential loop closure in institutional authorization rather than technical capability, and the framework has no representation of institutions.

Timelines are four-scenario ranges (Fast / Central / Slow / Blocked) conditioned on stated critical-path conditions, never point estimates. §6.2 gives the base rate for AI forecasting, which applies to this paper as much as to any other.

Framework revisions are governed by the pre-registration protocol in §8.3: revision triggers are fixed in advance, structural claims are non-revisable within a version, and a theory licensed to update its parameters on disconfirmation is unfalsifiable unless its revision rules are fixed first.
