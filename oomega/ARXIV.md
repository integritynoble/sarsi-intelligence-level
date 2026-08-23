# arXiv Submission Package — Open-Ended Evolving Organization, Version 2

Everything needed to submit the OΩ paper. It uses the same setup as the other SARSI papers in this repository, so these instructions differ only in the values you paste into the form.

| File | Purpose |
|---|---|
| `oomega-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — arXiv does not run BibTeX |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../Open_Ended_Evolving_Organization_v2.pdf` | Compiled PDF, 10 pages |

Verified: extracts to an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, no overfull boxes, 10 pages, zero Type 3 fonts, all fonts embedded Type 1.

## Relation to Version 1

This supersedes `../Open_Ended_Evolving_Organization_OOmega.pdf`, retained in the repository as the record. **Version 1 has not been posted**, so there is no arXiv identifier to cite and no replacement to file — submit this as a new paper, not as `v2` of an existing announcement.

The paper is deliberately *not* self-contained in the way the two-axis paper is. It retains Version 1's twelve metrics, reference architecture, failure modes, roadmap, and prior-work survey **by reference rather than by restatement**, because reproducing them would double the length without adding to the argument. The consequence for submission: a reviewer who has not seen Version 1 can follow every claim made here, but cannot check that the retained material is as described. If that matters, post Version 1 first and cite it — `references.bib` has the entry under `yang2026oomega` with `note` giving its date.

## Bibliography note

Version 1's reference list included several recent arXiv works on group-evolving agents, multi-agent discovery, and institution design whose full citation details were not available when this package was built. Rather than reconstruct them approximately, `references.bib` cites Version 1 itself as carrying that list, and gives full entries only for works verified independently. **Before submitting, merge Version 1's actual bibliography** — an arXiv submission that gestures at a prior list rather than reproducing it is a weakness a referee will notice.

## Submission form values

**Categories.** Primary `cs.MA` (Multiagent Systems) — this is an organizational-architecture paper first, and the coordination bound and separation results are multi-agent claims. Cross-list `cs.AI` and `cs.CY` (Computers and Society) for the governance and institutional material. Note the primary differs from the two-axis paper, which leads with `cs.AI`.

**License.** CC BY 4.0 if you want it cited and quoted freely. **Cannot be changed after announcement.**

**Comments field.** Suggested:

> 10 pages, 4 tables. Version 2 of a working framework; supersedes an unposted Version 1.

**Abstract.** Paste the text below. It is 1798 characters against arXiv's 1920 limit. The PDF keeps its own longer abstract.

```
An earlier version proposed Open-Ended Evolving Organization as a class of organizational intelligence: a persistent collective that preserves identity across member turnover, integrates distributed observation into evidence-bearing memory, reallocates roles and topology, modifies its own coordination mechanisms, improves the process generating those modifications, identifies its own unknowns, and converts discoveries into tools that expand its future frontier. It gave twelve axioms, twelve metrics, a reference architecture and an experimental program. This version makes six changes, two of them structural.

The twelve axioms are not independent and six are theorems. An axiom set exists to isolate what must be assumed from what follows; we give six independent axioms and derive the rest.

There is a coordination bound. Promotion of local claims to organizational knowledge requires verification by a locus other than the proposer; verification costs communication growing with the number of members consulted; marginal member value is bounded and may be negative. There is therefore a size beyond which adding members lowers organizational intelligence, and growth past it must be federation rather than accumulation. This is why such an organization is hierarchical and why cognitive compression is structurally necessary rather than merely economical.

Frontier expansion becomes measurable negatively. The defining containment condition cannot be evaluated because the reachable frontier cannot be enumerated; a retained registry of problem classes that failed under a stated budget makes expansion observable as recorded failure becoming reproducible success with an attributable cause.

We also report that the cheapest of the twelve metrics, promotion latency, has never been observed on a deployed governed system whose promotions table has no timestamp.
```

## Notes for the moderator queue

**One empirical claim, one system.** The measurement in §9.1 is a single audit log on a single host, and §11 says so. It is offered as a demonstration that the quantity is unrecorded, not as a finding about the field.

**The propositions are elementary.** Proposition 1 is a one-line argument and Proposition 7 is an existence claim with no functional form, which the paper states as a limitation rather than concealing. Neither is presented as deep; both are presented as load-bearing, which is a different claim.

**A note on self-supersession.** This paper corrects an unpublished paper by the same author. That is unusual and is stated openly in the abstract and §1 rather than presented as new work — the retained material is credited to Version 1 throughout, and §3's table names exactly which of its axioms are being demoted to theorems.
