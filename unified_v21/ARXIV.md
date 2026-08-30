# arXiv Submission Package — Measuring the Unified Intelligence Level

| File | Purpose |
|---|---|
| `unified-v21-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography; arXiv does not run BibTeX |
| `references.bib` | Kept beside the source for regeneration; not in the tarball |
| `../Unified_Intelligence_Harness_Scoring_Framework_v2_1.pdf` | Compiled Version 2.0 PDF, 53 pages |

Version 2.0 is dated August 28, 2026. It carries forward the framework and the
Version 1.9 item-validity and apparatus findings, and adds a same-seed
regime-switch comparison using `measurements/regime_switch_frontier.csv` and
`measurements/regime_switch_haiku.csv`. The common-protocol seeds are
`0,9,11,17,24,25,27,38,40,41,44,50`; seed 12 is excluded because it used the
earlier protocol. Frontier passes 5/12 and Haiku (`claude-haiku-4-5`) passes
1/12. The exact two-sided McNemar p-value is 0.125; frontier RMSE is lower on
11/12, with exact two-sided sign-test p=0.00635. All 24 episodes exit 0 and
state a mechanism.

This is not a Harness Scaling Curve segment. HSC holds a frozen model fixed and
varies harness generation; this experiment holds the harness/protocol fixed
and changes executor/model. The archived frontier CSV does not include a model
ID or executor version, so none is inferred. The comparison is limited to these
instances: one attempt per executor per seed, one mechanism family, one
host/harness configuration, no repeat-run variance estimate, and an incomplete
resource envelope.

## Regenerating

```text
cd unified_v21
pdflatex main && bibtex main && pdflatex main && pdflatex main
cp main.pdf ../Unified_Intelligence_Harness_Scoring_Framework_v2_1.pdf
tar czf unified-v21-arxiv.tar.gz main.tex main.bbl
```

The archive contains only `main.tex` and `main.bbl` so it compiles after
extraction without BibTeX. In a clean directory, run three plain `pdflatex`
passes:

```text
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

The verified build has no errors, missing files, undefined references or
citations, overfull boxes, hyperref token warnings or Type 3 fonts. All fonts
are embedded. Harmless float-placement notices changing `[h]` to `[ht]`, and a
few non-fatal underfull boxes in prose, may remain.

## Presentation note

This draft carries **no internal version history**. Earlier drafts (v1.0–v2.0)
were never published, so referencing them cited documents no reader could
obtain, and the running changelog — three "carried forward from version N"
paragraphs in the abstract, `(new in 1.4)` tags through the normative text, and
an eleven-row history table — read as a working document rather than a paper.
All of that substance is retained; only the archaeology is gone. arXiv supplies
its own v1/v2 versioning for revisions after posting.
