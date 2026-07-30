# arXiv Submission Package — Functional Self-Awareness for SARSI Agents

Everything needed to submit the agent-scale companion paper.

Both SARSI papers use an identical submission setup, so these instructions differ only in the values you paste into the form. The companion's guide is [`../arxiv/README.md`](../arxiv/README.md).

| File | Purpose |
|---|---|
| `sarsi-selfaware-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — see below |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../SARSI_Functional_Self_Awareness.pdf` | Compiled PDF, 34 pages |

Verified: extracts to an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, 34 pages. That is arXiv's exact process.

## Three setup choices, shared by both papers

**`main.bbl` ships; `references.bib` does not.** arXiv does not run BibTeX. A `.bib` alone would announce the paper with every citation rendered as `[?]`. The `.bbl` is the compiled bibliography and is what arXiv reads.

**`\pdfoutput=1` is set in the first lines of `main.tex`.** This forces the pdflatex path. It matters most for the companion, whose figure is inline TikZ with no `.eps` fallback, and is set in both so the two sources stay identical in structure. It only takes effect within the first few lines — leave it above `\documentclass`.

**Fonts are the URW Type 1 trio** (`mathptmx` + `helvet` + `courier`). Verified with `pdffonts`: every embedded font is Type 1, and there are no Type 3 or bitmap fonts in either PDF. arXiv discourages bitmap fonts because they render poorly on screen, and the default T1 sans and typewriter faces are bitmaps in many TeX installations — which also breaks `microtype`'s font expansion outright.

To regenerate after editing:

```bash
cd self_awareness
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
cp main.pdf ../SARSI_Functional_Self_Awareness.pdf
tar czf sarsi-selfaware-arxiv.tar.gz main.tex main.bbl
```

## Submission form values

**Categories.** Primary `cs.AI`. Cross-list `cs.MA` (Multiagent Systems) for the multi-agent console and role decomposition, and `cs.CY` (Computers and Society) for the governance and authority material. Consider `q-bio.NC` only if you want the brain-inspired framing foregrounded — but the paper explicitly disclaims biological equivalence and makes no neuroscience claim, so moderators may well decline it. Not recommended.

**License.** CC BY 4.0 if you want it cited and quoted freely. **Cannot be changed after announcement** — pick deliberately.

**Comments field.** Suggested:

> 34 pages, 13 tables, 1 figure. Companion: arXiv:XXXX.XXXXX (SARSI-L, system scale).

**Submit this paper second**, so the identifier above is real. If you must submit both at once, drop the cross-reference rather than guessing an identifier.

**Abstract.** Paste the text below. It is 1914 characters against arXiv's 1920 limit. The PDF keeps its own longer abstract, which is normal.

```
The SARSI program spans two things developed apart: a brain-inspired dynamic state space describing what an agent knows about itself, and SARSI-L, which holds that recursive self-improvement is substrate-indexed and describes how it closes loops from software to stellar engineering. Between them sit four applied systems, each with its own self-model notation. The corpus contradicts itself in five places: the number of self-model dimensions, the depth of the evidence-authority ladder, whether self-awareness is a prerequisite for loop closure, whether autonomous deployment of a self-modification is permitted, and whether autonomous goal revision is a milestone or a violation.

This is the unified edition. It keeps the brain-inspired architecture canonical -- a ten-coordinate evidence-grounded self-state, specialized asynchronous processors, a bounded global workspace, a predictive self-model corrected by residuals, dual-timescale improvement -- and resolves each contradiction rather than restating it. The central construction is a two-scale account: the agent-scale self-state and the system-scale loop-completion profile are the same kind of object, both formerly ladders, both replaced by profiles for the same reason, measured on one shared five-band scale.

We define governed loop closure, separating capability closure from authority closure, and show that SARSI-L's Loop I criterion and the no-self-promotion invariant are compatible once the promoter is a role rather than a species. Stated in SARSI-L's own machinery, authority closure is exactly the removal of the deploy step from the externally-gated set of its Amdahl bound: until granted, that bound caps the software loop's iteration rate at the reciprocal of deploy-authorization latency, however capable the agent becomes. The framework is strictly functional: it measures a control capability and makes no claim about consciousness.
```

## Two things that may bite

**Endorsement.** A first-time `cs.AI` submitter needs endorsement from an existing `cs.AI` author before the submission is accepted. It is a separate process from the upload and can take days — start it early. See arxiv.org/help/endorsement. One endorsement covers both papers.

**Moderation.** This paper is on safer ground than the framework paper — it is an architecture-and-measurement contribution with an explicit deployment report, not a forecast. The one thing likely to draw attention is the self-awareness framing. The defence is already in the text: §2 states the non-claim, §3.4 explains why a sentience milestone was withdrawn as a category error, and every coordinate has a deterministic probe. Point at those if queried.

## Keeping the pair consistent

The two papers share one load-bearing claim: §11.3 of the companion against Proposition 1 and Appendix B of the framework paper — authority closure is the removal of the deploy step from the Amdahl bound's externally-gated set, and the ⊥/Unmeasured band exists in both scales because that argument needs it. Appendix C of the companion is the consistency register listing every cross-document claim and which file owns it. If you revise either paper, check it.
