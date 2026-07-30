# arXiv Submission Package — A Manager Is Not a Controller

Everything needed to submit the fleet-coordination paper. It uses the same setup as the other three SARSI papers in this repository, so these instructions differ only in the values you paste into the form.

| File | Purpose |
|---|---|
| `sarsi-manager-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — arXiv does not run BibTeX |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../SARSI_Manager_Is_Not_A_Controller.pdf` | Compiled PDF, 14 pages |

Verified: extracts to an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, no overfull boxes, 14 pages, zero Type 3 fonts.

## The base paper

This paper builds on *Functional Self-Awareness for Hierarchical SARSI Multi-Agent Systems: Version 3.0*, cited as `yang2026hierarchical`. **Add its arXiv identifier to `references.bib` once it is announced**, and submit it first if you intend to post both — the `howpublished` field currently says only "Preprint."

Unlike an earlier draft, this paper is **standalone**: it has its own section and equation numbering and does not continue the base paper's. Section 2 reproduces the objects it depends on in one table, so it can be read without the base paper open. That was a deliberate change — a submission that opens at §20 and refers to equations 1–32 that appear nowhere in it is hard to review and easy for a moderator to bounce.

## Submission form values

**Categories.** Primary `cs.MA` (Multiagent Systems) — this is a multi-agent coordination paper first. Cross-list `cs.AI` and `cs.CY` (Computers and Society) for the authority and governance material. Note the primary differs from the other three SARSI papers, which lead with `cs.AI`.

**License.** CC BY 4.0 if you want it cited and quoted freely. **Cannot be changed after announcement.**

**Comments field.** Suggested:

> 14 pages, 3 tables, 1 figure. Companion to arXiv:XXXX.XXXXX (hierarchical SARSI architecture, Version 3.0).

**Abstract.** Paste the text below. It is 1892 characters against arXiv's 1920 limit. The PDF keeps its own longer abstract.

```
Version 3.0 of the hierarchical SARSI architecture specifies a manager-specialist system: nested workspaces, typed directives and reports, calibrated reliability, interrupt precedence, and a stability condition. It calls the manager an executive-control hub. That description invites an implementation the architecture's own invariants forbid: a manager that holds beliefs about each specialist and writes them into that specialist's state.

We argue the manager is not a controller in the control-theoretic sense. Specialists filter what the manager sends through their own admission masks, so influence is offered rather than applied; the coupling is recurrent, so the manager's state is revised by the agents it coordinates; and neither party is sovereign, since owner pre-emption outranks both. Global workspace theory has no homunculus directing specialized processors, only a bounded broadcast channel they compete for.

The central result is that the governance prohibition and the stability condition are the same constraint. Under the base paper's own bias invariant -- a directive may change precision, attention and evidence order, but not the conditional mean of any specialist estimator -- the top-down block of the recurrent coupling vanishes in the mean linearization. The block is then nilpotent, its spectral radius is zero, and hierarchical stability reduces to a per-agent condition independent of fleet size. If a manager may write specialist coordinates directly, the feedback loop is reinstated and stability becomes a tuning problem. The prohibition does not bound the loop; it removes it.

Three further results follow: a manager cannot certify a competence it does not measure; delegated authority is an intersection, closing a laundering route; and an owner interrupt may pause but never edit, since a state-writing interrupt is indistinguishable from confabulation.
```

## Regenerating

```bash
cd fleet
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
cp main.pdf ../SARSI_Manager_Is_Not_A_Controller.pdf
tar czf sarsi-manager-arxiv.tar.gz main.tex main.bbl
```

## Two things that may bite

**Endorsement.** `cs.MA` endorsement is separate from `cs.AI`. If you have been endorsed for `cs.AI` only, a `cs.MA` primary may require a fresh endorsement — check before submitting, or lead with `cs.AI` and cross-list `cs.MA` instead.

**The claim in the title.** The paper argues against a framing the base paper itself uses ("executive-control hub"). That is deliberate and stated plainly in §1.1, and the paper is careful to say Version 3.0 governs the architecture while this one governs coordination semantics. If a reviewer reads it as contradicting its own foundation, §1.4 is the paragraph to point at.
