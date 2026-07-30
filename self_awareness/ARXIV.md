# arXiv Submission Package — Functional Self-Awareness for SARSI Agents

Everything needed to submit the agent-scale companion paper. The system-scale paper has its own package in [`../arxiv/`](../arxiv/); the two are submitted separately and cross-reference each other.

| File | Purpose |
|---|---|
| `sarsi-selfaware-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — see note below |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../SARSI_Functional_Self_Awareness.pdf` | Compiled PDF, 31 pages |

Verified: extracts to an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, 31 pages. That is arXiv's exact process.

---

## Two things this package does that the other one doesn't

**`main.bbl` is shipped, `references.bib` is not.** arXiv does not run BibTeX. A `.bib` file alone would produce a paper with every citation rendered as `[?]`. The `.bbl` is the compiled output and is what arXiv needs. If you edit the bibliography, regenerate it:

```bash
cd self_awareness
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
cp main.pdf ../SARSI_Functional_Self_Awareness.pdf
tar czf sarsi-selfaware-arxiv.tar.gz main.tex main.bbl
```

(The system-scale paper needs no `.bbl` because its bibliography is inlined via `thebibliography`. Different solution, same reason.)

**`\pdfoutput=1` is set in the first lines of `main.tex`.** The figure is inline TikZ and there are no `.eps` files, so the source must take the pdflatex path. Without this directive arXiv may attempt the DVI route and fail on the TikZ picture. Leave it where it is — it only takes effect within the first few lines of the file.

---

## Submission form values

**Categories.** Primary `cs.AI` (Artificial Intelligence). Cross-list `cs.MA` (Multiagent Systems) for the multi-agent console and role decomposition, and `cs.CY` (Computers and Society) for the governance and authority material.

Consider `q-bio.NC` only if you want the brain-inspired framing foregrounded — but the paper explicitly disclaims biological equivalence and makes no neuroscience claim, so moderators may well decline it. Not recommended.

**License.** CC BY 4.0 if you want it cited and quoted freely. **Cannot be changed after announcement** — pick deliberately.

**Comments field.** Suggested:

> 31 pages, 13 tables, 1 figure. Companion to arXiv:XXXX.XXXXX (SARSI-L, system scale).

Fill in the identifier once the system-scale paper is announced. If you submit both, put the system-scale paper in first so this one can cite a real identifier; otherwise leave the cross-reference to the version note.

**Abstract.** Paste the text below. It is 1914 characters against arXiv's 1920 limit. The PDF keeps its own longer abstract, which is normal.

```
The SARSI program spans two things developed apart: a brain-inspired dynamic state space describing what an agent knows about itself, and SARSI-L, which holds that recursive self-improvement is substrate-indexed and describes how it closes loops from software to stellar engineering. Between them sit four applied systems, each with its own self-model notation. The corpus contradicts itself in five places: the number of self-model dimensions, the depth of the evidence-authority ladder, whether self-awareness is a prerequisite for loop closure, whether autonomous deployment of a self-modification is permitted, and whether autonomous goal revision is a milestone or a violation.

This is the unified edition. It keeps the brain-inspired architecture canonical -- a ten-coordinate evidence-grounded self-state, specialized asynchronous processors, a bounded global workspace, a predictive self-model corrected by residuals, dual-timescale improvement -- and resolves each contradiction rather than restating it. The central construction is a two-scale account: the agent-scale self-state and the system-scale loop-completion profile are the same kind of object, both formerly ladders, both replaced by profiles for the same reason, measured on one shared five-band scale.

We define governed loop closure, separating capability closure from authority closure, and show that SARSI-L's Loop I criterion and the no-self-promotion invariant are compatible once the promoter is a role rather than a species. Stated in SARSI-L's own machinery, authority closure is exactly the removal of the deploy step from the externally-gated set of its Amdahl bound: until granted, that bound caps the software loop's iteration rate at the reciprocal of deploy-authorization latency, however capable the agent becomes. The framework is strictly functional: it measures a control capability and makes no claim about consciousness.
```

---

## Two things that may bite

**Endorsement.** A first-time `cs.AI` submitter needs endorsement from an existing `cs.AI` author before the submission is accepted. It is a separate process from the upload and can take days. See arxiv.org/help/endorsement. If you are submitting both SARSI papers, one endorsement covers both.

**Moderation.** This paper is on safer ground than the system-scale one — it is an architecture-and-measurement paper with an explicit deployment report and a stated non-claim about consciousness, not a forecasting paper. The one thing likely to draw a moderator's attention is the self-awareness framing. The defence is in the paper already: §2 states the non-claim, §3.4 explains why a sentience milestone was withdrawn as a category error, and every coordinate has a deterministic probe. Point at those if queried.

---

## Consistency with the companion

The two papers are maintained as a pair. If you revise either, check `Appendix C` of this paper (the consistency register) — it lists every cross-document claim and which file owns it. The load-bearing shared claim is §11.3 here against Proposition 1 and Appendix B in the companion: authority closure is the removal of the deploy step from the Amdahl bound's externally-gated set, and the ⊥/Unmeasured band exists in both papers' scales because this argument needs it.
