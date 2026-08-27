# arXiv Submission Package — Unified Intelligence, Version 1.6

| File | Purpose |
|---|---|
| `unified-v16-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — arXiv does not run BibTeX |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../Unified_Intelligence_Harness_Scoring_Framework_v1_6.pdf` | Compiled PDF, 42 pages |

Verified: extracts into an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, no overfull boxes, 42 pages, zero Type 3 fonts, all fonts embedded.

## What this version is

Version 1.6 keeps the whole of v1.4 and folds in v1.5's memory contract. Two things are new.

**Long-term memory is embedded inside Individual Intelligence** (§5.1) rather than added as a sixth family, with a per-level M0–MΩ contract and an explicit exclusion: a long context window is not long-term memory, so RULER/LongBench-style evidence contributes to C and cannot certify I1.

**The items themselves are audited** (§16). Version 1.4 examined the scoring arithmetic and found it blind to something that mattered. Version 1.6 examines the benchmark items the arithmetic runs on, and finds that two of them graded a rule they never stated. Both were found by the same signature: a frontier executor and a much weaker one returned the *same* answer to the *same* item, and both were marked wrong. That signature is the section's main contribution — it is a validity check on a hidden answer key that needs no ground truth, which matters because the ground truth is what is in doubt.

The changes are in §5.1 (memory), §16.1 (disclosed hazards do not desaturate a suite), §16.2 (two DL4 item families, on specification scale and on search), §16.3 (cross-tier concordance auditing), §16.4 (specification–key consistency for parameterised families), §16.5 (graded item scoring and separated failure modes), §16.6 (what the corrected items measured), §13.15 (headroom and audit status in the reporting standard), and Appendix D.

## Dependency warning

**This is a framework proposal with small measurements in it, not an empirical paper.** A referee should be told plainly:

- **The frontier is still not measured.** The scale-difficulty item family scores 1.000 on every seed for the frontier executor. It separates a weaker executor from a stronger one — the first item in the suite to do so — and does not locate the top of the range. §16.6 says this in the same breath as the positive result, and every frontier figure in the paper is a lower bound set by the suite.
- **Neither difficulty axis reached the frontier.** The search family has now been run: both executors score 1.000 on every attempted seed, so the greedy trap it was built around — feasible 60/60, optimal 3–12/60 — catches a plausible wrong method that neither model used. Scale separated the tiers; search separated nothing. Two axes are not an exhaustive search of the space and the paper offers no third candidate.
- **Two executors is the minimum for a concordance audit and not a good number.** Concordant error is a strong signal with an unquantified false-positive rate; two models from overlapping training distributions could share a misreading. Three independent lineages would separate that from a defective key, and that has not been run.
- **The audit found two defects and does not establish that two is all there were.** It is a filter with unknown recall; unflagged items are unaudited, not validated.
- **Discovery was retrospective.** Both defects were found because a measurement looked wrong, not because the audit was standing policy. §16.3 is a proposal informed by two instances, not a protocol with a measured detection rate.
- **One author wrote both the specifications and the tests that check them.** The consistency tests catch mechanical divergence between prose and key, which is what failed. They cannot catch a rule stated and graded consistently and wrong in both places.
- Everything carried from Version 1.4 keeps its own limitations: three executors, one machine, 48 episodes, two seeds per class, four rungs of eight, one intervention budget, one coordinate instrumented.

The claim worth defending is Proposition 1 (acceptance invariance), which is a statement about the formula rather than about any model. The new claim worth defending is narrower and stated as such: **concordant cross-tier error is evidence about the item rather than the executors**, and it is refuted by exhibiting items that several independent executors fail identically and whose keys are then confirmed correct.

## Suggested categories

Primary `cs.AI`; cross-list `cs.HC` (the human-factors lineage in §11 and §21 is load-bearing) and `cs.SE` (the run-log schema, item-validity tests and reporting standards are engineering artifacts).

## Regenerating

```
cd unified_v16
pdflatex main && bibtex main && pdflatex main && pdflatex main
cp main.pdf ../Unified_Intelligence_Harness_Scoring_Framework_v1_6.pdf
tar czf unified-v16-arxiv.tar.gz main.tex main.bbl
```

`main.bbl` is committed on purpose: it ships inside the tarball because arXiv does not run BibTeX. It is a build input, not an artifact.
