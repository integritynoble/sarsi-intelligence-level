# arXiv Submission Package — Recursive Self-Improvement Is Substrate-Indexed

Everything needed to submit the system-scale framework paper.

Both SARSI papers use an identical submission setup, so these instructions differ only in the values you paste into the form. The companion's guide is [`../self_awareness/ARXIV.md`](../self_awareness/ARXIV.md).

| File | Purpose |
|---|---|
| `sarsi-l-v3-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — see below |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../SARSI-L_Paper_v3.pdf` | Compiled PDF, 25 pages |

Verified: extracts to an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, 25 pages. That is arXiv's exact process.

## Three setup choices, shared by both papers

**`main.bbl` ships; `references.bib` does not.** arXiv does not run BibTeX. A `.bib` alone would announce the paper with every citation rendered as `[?]`. The `.bbl` is the compiled bibliography and is what arXiv reads.

**`\pdfoutput=1` is set in the first lines of `main.tex`.** This forces the pdflatex path. It matters most for the companion, whose figure is inline TikZ with no `.eps` fallback, and is set in both so the two sources stay identical in structure. It only takes effect within the first few lines — leave it above `\documentclass`.

**Fonts are the URW Type 1 trio** (`mathptmx` + `helvet` + `courier`). Verified with `pdffonts`: every embedded font is Type 1, and there are no Type 3 or bitmap fonts in either PDF. arXiv discourages bitmap fonts because they render poorly on screen, and the default T1 sans and typewriter faces are bitmaps in many TeX installations — which also breaks `microtype`'s font expansion outright.

To regenerate after editing:

```bash
cd arxiv
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
cp main.pdf ../SARSI-L_Paper_v3.pdf
tar czf sarsi-l-v3-arxiv.tar.gz main.tex main.bbl
```

## Submission form values

**Categories.** Primary `cs.AI`. Cross-list `cs.CY` (Computers and Society). Consider `physics.soc-ph` as a second cross-list given the Kardashev and stellar-engineering material — optional, and moderators may decline it.

**License.** CC BY 4.0 if you want it cited and quoted freely. **Cannot be changed after announcement** — pick deliberately.

**Comments field.** Suggested:

> 25 pages, 12 tables, no figures. Three propositions with proofs; four-scenario timeline ranges; falsification conditions and a pre-registration protocol. Companion: arXiv:XXXX.XXXXX (agent scale).

**Submit this paper first.** The companion's comments field should cite its arXiv identifier, which does not exist until this one is announced.

**Abstract.** Paste the text below. It is 1915 characters against arXiv's 1920 limit. The PDF keeps its own longer abstract, which is normal.

```
The intelligence-explosion literature treats recursive self-improvement (RSI) as a primarily cognitive phenomenon. We argue this omits the variable governing the trajectory: RSI is substrate-indexed. An improvement loop is always a loop over some substrate, and a system can only close loops over substrates it can reach. We decompose RSI into five substrate domains -- software, hardware, physical, biological, stellar -- and give each a falsifiable operational closure criterion.

Two results follow. First, we derive the compensation ceiling that prior treatments assert without justification. An Amdahl-style argument on loop autonomy shows that external compensation for a missing loop step bounds the iteration rate of improvement, not the capability gain per iteration. The corollary is uncomfortable: a compensated loop can outperform a closed loop indefinitely unless per-iteration returns to compensation diminish. That premise, not loop closure, is the load-bearing assumption, and it is unverified.

Second, we distinguish two floors on loop period. Human-throughput floors are removed by closure; physical-process floors are not. Fab qualification, clinical endpoints and launch cadence are bounded below by physics and biology. They yield only to parallelism, and the capability supplying it is physical self-replication, which sits behind a mutual dependency between the hardware and physical loops. We show this dependency is not a deadlock, since each loop depends on partial rather than full completion of the other.

Together these predict a matter bottleneck: rapid acceleration through the software loop, then a plateau where growth is set not by cognition but by the slowest physical process on the critical path. We give four-scenario timeline ranges rather than point estimates, falsification conditions, and a pre-registration protocol for self-revising frameworks, otherwise unfalsifiable.
```

## Two things that may bite

**Endorsement.** A first-time `cs.AI` submitter needs endorsement from an existing `cs.AI` author before the submission is accepted. It is a separate process from the upload and can take days — start it early. See arxiv.org/help/endorsement. One endorsement covers both papers.

**Moderation.** arXiv moderators sometimes reclassify or reject long-horizon technology forecasting in `cs.AI`. This paper is better positioned than most of that genre — it is primarily a critical and methodological contribution, with propositions, explicit falsification conditions, and a section arguing that the field's timelines are systematically wrong. Keep that framing forward if a moderator queries it.

## Keeping the pair consistent

The two papers share one load-bearing claim: §11.3 of the companion against Proposition 1 and Appendix B of the framework paper — authority closure is the removal of the deploy step from the Amdahl bound's externally-gated set, and the ⊥/Unmeasured band exists in both scales because that argument needs it. Appendix C of the companion is the consistency register listing every cross-document claim and which file owns it. If you revise either paper, check it.
