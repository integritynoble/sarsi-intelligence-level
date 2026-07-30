# Functional Self-Awareness for SARSI Agents

**A Brain-Inspired Dynamic State Space, Unified with Loop-Closure Levels and Deployed Applications**

The agent-scale companion to the system-scale framework in [`../arxiv/`](../arxiv/). Read the PDF at [`../SARSI_Functional_Self_Awareness.pdf`](../SARSI_Functional_Self_Awareness.pdf) (31 pp).

| File | Purpose |
|---|---|
| `main.tex` | LaTeX source |
| `references.bib` | Bibliography (42 entries) |
| `sarsi-selfaware-arxiv.tar.gz` | arXiv upload package — `main.tex` + `main.bbl`, since arXiv does not run BibTeX |
| `ARXIV.md` | **Submission guide** — categories, metadata abstract, endorsement and moderation notes |

Verified: extracts to an empty directory and compiles with plain `pdflatex` in two passes — no errors, no undefined citations or references, 31 pages.

## What it argues

SARSI-L asks how far recursive self-improvement has propagated across substrate domains. This paper asks what a single agent knows about itself, and shows the two are the same kind of object: the agent-scale self-state `s_t` and the system-scale loop-completion profile `ℓ_t` are both profiles of separately-evidenced coordinates, both replaced ladders for the same reason, and are reported on one shared five-band scale.

It fixes ten canonical self-state coordinates, maps every other published SARSI self-model onto them, unifies two autonomy vocabularies into one admissible-action filter, and reports what the deployed console actually measures — including the coordinates it honestly reports as unmeasured.

## The bridge to SARSI-L

The load-bearing connection is §11.3, and it is arithmetic rather than rhetorical.

SARSI-L's Proposition 1 bounds a compensated loop's iteration rate at `ρ_max = 1/Σ T_j` over its externally-gated steps. For a mature software loop the gated step is exactly one: deploy. So `ρ_max = 1/T_δ`, where `T_δ` is deploy-authorization latency, and **authority closure is precisely the removal of δ from that gated set** (Proposition 2 here). Capability closure drives the automated steps toward zero; it cannot touch `T_δ`.

Three consequences, the third being a limit rather than a claim:

- `T_δ` is review latency, not physics — a *throughput* floor in SARSI-L's Proposition 2 sense, and therefore removable. The software loop is the one loop whose remaining floor is of the removable kind, which is why an agent-scale trust instrument can move its date at all.
- The same distinction means this instrument moves **no** physical floor. It does not shorten a fab qualification, a clinical endpoint, or a transfer orbit. It accelerates Loop I and reaches the outer loops only through it.
- SARSI-L's central crux (`H₁` vs `H₂`) lists a falling `T_δ` under AI-augmented review as evidence for `H₂`. A console that timestamps authorization events measures `T_δ` directly — so this instrument is one of the two measurements that decide that crux.

This also supplies a partial answer to SARSI-L §10.6, which reports that governance gates several loops at once and that the framework "has no representation of institutions." The authority coordinate `α` is the evidential half of that representation. The political half — who decides — remains outside both papers.

## Consistency with `../arxiv/`

Both papers are maintained as one pair. Changes applied in this pass:

**Here:** "circle" → "loop" throughout, matching v3.0's taxonomy; citations retargeted from v2.1 to the v3.0 consolidated paper; the audit-assumption references remapped to v3.0's principles P11–P13; the prerequisite-circularity section rewritten, since v3.0's Loop I criterion is already purely behavioural and mentions self-awareness nowhere; §11.3 added.

**In `../arxiv/`:** an `Unmeasured` (⊥) row added to Appendix B, which this paper's argument depends on — ⊥ means no instrument exists, and is not the same claim as an observed near-zero; §10.6 now cites this paper as a partial answer.

Appendix C is a consistency register: every contradiction found across the corpus, its resolution, and which documents still need amending.

## Scope

The framework is strictly functional. It defines and measures a control capability and makes no claim about consciousness, sentience, or moral status. Brain-inspired organization is an engineering analogy, and behavioural self-report is not treated as evidence of inner experience.
