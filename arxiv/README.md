# arXiv Submission Package

Everything needed to submit **Recursive Self-Improvement Is Substrate-Indexed** to arXiv.

| File | Purpose |
|---|---|
| `main.tex` | Complete LaTeX source. Single file, no external dependencies, no figures |
| `sarsi-l-v3-arxiv.tar.gz` | **Upload this.** Contains `main.tex` only |
| `../SARSI-L_Paper_v3.pdf` | Compiled PDF, 25 pages |

Verified: extracts to an empty directory and compiles with plain `pdflatex` in two passes — no undefined references, no overfull boxes, 25 pages. That is arXiv's exact process.

---

## Before you submit: two placeholders

`main.tex` has an author block that must be filled in (search for `TODO`):

```latex
\author{[AUTHOR NAME]\\[0.3em]
\normalsize [Affiliation]\\
\normalsize \texttt{[email]}}
```

Replace all three, recompile, and rebuild the tarball:

```bash
cd arxiv
latexmk -pdf main.tex
cp main.pdf ../SARSI-L_Paper_v3.pdf
tar czf sarsi-l-v3-arxiv.tar.gz main.tex
```

arXiv requires real author names — no pseudonyms or institutional-only attribution.

---

## Submission form values

**Categories.** Primary `cs.AI` (Artificial Intelligence). Cross-list `cs.CY` (Computers and Society). Consider `physics.soc-ph` as a second cross-list given the Kardashev and stellar-engineering material — optional, and moderators may decline it.

**License.** CC BY 4.0 is the usual choice for a preprint you want cited and quoted. arXiv's default non-exclusive license is more restrictive; pick deliberately, because **the license cannot be changed after announcement.**

**Journal-ref / comments.** Leave journal-ref empty. Suggested comment field:

> 25 pages, 12 tables, no figures. Three propositions with proofs; four-scenario timeline ranges; falsification conditions and a pre-registration protocol.

**Abstract.** Paste the text below into the web form. It is 1915 characters — arXiv's limit is 1920, so it fits without truncation. Note this is a condensed version; the longer abstract inside the PDF is unchanged and that difference is normal and acceptable.

```
The intelligence-explosion literature treats recursive self-improvement (RSI) as a primarily cognitive phenomenon. We argue this omits the variable governing the trajectory: RSI is substrate-indexed. An improvement loop is always a loop over some substrate, and a system can only close loops over substrates it can reach. We decompose RSI into five substrate domains -- software, hardware, physical, biological, stellar -- and give each a falsifiable operational closure criterion.

Two results follow. First, we derive the compensation ceiling that prior treatments assert without justification. An Amdahl-style argument on loop autonomy shows that external compensation for a missing loop step bounds the iteration rate of improvement, not the capability gain per iteration. The corollary is uncomfortable: a compensated loop can outperform a closed loop indefinitely unless per-iteration returns to compensation diminish. That premise, not loop closure, is the load-bearing assumption, and it is unverified.

Second, we distinguish two floors on loop period. Human-throughput floors are removed by closure; physical-process floors are not. Fab qualification, clinical endpoints and launch cadence are bounded below by physics and biology. They yield only to parallelism, and the capability supplying it is physical self-replication, which sits behind a mutual dependency between the hardware and physical loops. We show this dependency is not a deadlock, since each loop depends on partial rather than full completion of the other.

Together these predict a matter bottleneck: rapid acceleration through the software loop, then a plateau where growth is set not by cognition but by the slowest physical process on the critical path. We give four-scenario timeline ranges rather than point estimates, falsification conditions, and a pre-registration protocol for self-revising frameworks, otherwise unfalsifiable.
```

---

## Two things that may bite

**Endorsement.** If this account has not posted to `cs.AI` before, arXiv requires endorsement from an existing `cs.AI` author before the submission will be accepted. Request it early — it is a separate process from the upload and can take days. See arxiv.org/help/endorsement.

**Moderation.** arXiv moderators sometimes reclassify or reject long-horizon technology-forecasting work in `cs.AI`. This paper is better positioned than most of that genre — it is primarily a critical and methodological contribution, with propositions, explicit falsification conditions, and a section arguing that the field's timelines are systematically wrong — and the framing should be kept front and centre if a moderator queries it. It is still worth knowing the risk before you submit rather than after.

---

## Rebuilding from scratch

```bash
cd arxiv
latexmk -C                      # clean all aux files
latexmk -pdf main.tex           # rebuild PDF
tar czf sarsi-l-v3-arxiv.tar.gz main.tex
```

The bibliography is inlined via `thebibliography`, deliberately: **arXiv does not run BibTeX**, so a `.bib` file would require shipping a `.bbl` and is a common cause of failed builds. There is nothing to configure.
