# arXiv Submission Package — Unified Intelligence, Version 1.4

| File | Purpose |
|---|---|
| `unified-v14-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — arXiv does not run BibTeX |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../Unified_Intelligence_Harness_Scoring_Framework_v1_4.pdf` | Compiled PDF, 33 pages |

Verified: extracts into an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, no overfull boxes, 33 pages, zero Type 3 fonts, all fonts embedded.

## What this version is

Version 1.4 keeps the whole of v1.3 — five families, six coordinates, the gated U0–UΩ scale, HG0–HGΩ, the formal HLIS construction, HIL, and the contemporary-benchmark mapping. It differs in one respect: **the ladder was built and a curve was measured**, and the measurement found a defect in the framework's own scoring variable.

`A_DI` was defined on `P(success)`, which is exactly invariant to the harness generation that adds an acceptance step — because acceptance does not change the probability of success, only what is reported as success. Measured, HG0 and HG1 both scored 93.3 while false completions went 2/12 → 0/12.

The changes that follow from it are in §13.9 (the delivered-outcome primitive), §13.15 (the run log must record acceptance), §14.3 (ρ_V), §14.4 (two cautions on the composite), §11.2b (the reference ladder), §15.1 (per-task specification status), §16.4 (the measurement), and Appendix D (version history).

## Dependency warning

**This is a framework proposal with one small measurement in it, not an empirical paper.** A referee should be told plainly:

- **Three executors from two vendor families, one machine, 48 episodes each, two seeds per class.** The curves in §16.4 are readings, not rates.
- **The task suite is saturated for the two frontier executors**, whose curves are identical to three significant figures. The suite discriminates only the weaker executor, and §16.4.3 says so.
- **Tool authority was equalised by disabling one vendor's own sandbox**, with isolation supplied by the harness adapter instead. Recorded in §16.4 rather than hidden.
- **Between-rung variance was not controlled.** Each rung was an independent run, so one model's HG0→HG1 movement is sampling noise rather than signal. §16.4.3 says so and the protocol now requires a paired design that was not used to produce these numbers.
- **Four rungs of eight.** HG4–HGΩ are specified and not built, so HIL-Level above 3 is not assessable and the measured HIL-AUC is a mean over a truncated ladder.
- **One intervention budget.** Everything at H1, so the frontier cannot be observed moving leftward.
- **One coordinate.** Only DI was instrumented; C, I, O and SA have no runnable suite, so every measured figure is `HLIS_DI`.
- **Every level threshold remains a hypothesis.** §21 says so, and nothing here calibrates them.

The claim worth defending is Proposition 1 (acceptance invariance), which is a statement about the formula rather than about any model: `A_DI` is defined on `P(success)`, and an acceptance step changes neither what the system produces nor whether it is correct. It is refuted by exhibiting two harnesses differing *only* in acceptance whose measured `A_DI` differs under a paired design.

The second empirical claim — that Harness Gain separates models by harness response while HIL-AUC ranks them by baseline — rests on a two-model comparison and is offered as a first data point, not a result.

## Suggested categories

Primary `cs.AI`; cross-list `cs.HC` (the human-factors lineage in §6 and §17 is load-bearing) and `cs.SE` (the run-log schema and reporting standards are engineering artifacts).

## Regenerating

```
cd unified_v14
pdflatex main && bibtex main && pdflatex main && pdflatex main
cp main.pdf ../Unified_Intelligence_Harness_Scoring_Framework_v1_4.pdf
tar czf unified-v14-arxiv.tar.gz main.tex main.bbl
```

`main.bbl` is committed on purpose: it ships inside the tarball because arXiv does not run BibTeX. It is a build input, not an artifact.
