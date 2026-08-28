# arXiv Submission Package — Unified Intelligence, Version 1.9

| File | Purpose |
|---|---|
| `unified-v19-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — arXiv does not run BibTeX |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../Unified_Intelligence_Harness_Scoring_Framework_v1_9.pdf` | Compiled PDF, 51 pages |

Verified: extracts into an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, no overfull boxes, 51 pages, zero Type 3 fonts, all fonts embedded.

## What this version is

Version 1.9 keeps everything in 1.8 — the five-family core, the gated U0–UΩ scale, HLIS and HIL, the item-validity requirements of 1.6, the GUI-perception subscale of 1.7, and 1.8's separation of Memory Capability M into an independently measured supporting coordinate joined to I by the one-way gate `I(A) ≥ I_n ⟹ M(A) ≥ μ_n`.

The new material is measurement, and one result of it is positive for the first time.

**Four difficulty axes have now been built and run against a frontier executor.** Disclosed reasoning hazards separate no model. Specification scale separates executor tiers and not the frontier. Exact search separates nothing. Decidability — whether the task is answerable at all — separates the three reference strategies sharply and no live model. §16 states the argument that explains all three: **once a specification is written without ambiguity, every property of the task is mechanically derivable from it, and anything mechanically derivable is within reach of an executor that can implement the specification.** Difficulty inside that envelope does not exist to be found.

**The first axis built outside the envelope produced a frontier capability failure.** On a sealed mechanism generated after the executor was frozen — two laws and a latent boundary between them — the frontier executor extrapolated with an RMSE of 0.258 against a bar of 0.043, worse than the 0.174 that nearest-neighbour achieves. It did worse than memorising, outside the sampled box.

**Two findings about the apparatus rather than the model.** A fourth answer-key defect, in the class built specifically to be different; and a timeout that could not fire, which turned a killed run into a recorded capability result and said nothing in the data.

## Dependency warning

**This is a framework proposal with small measurements in it, not an empirical paper.** A referee should be told plainly:

- **The one frontier failure rests on a single instance.** Seed 11 of the regime-switch family is the only capability failure by a frontier executor anywhere in this work. One instance is an existence proof, not a rate. Four earlier apparent frontier failures in this same line of work all turned out to be the author's own ambiguities, so this should be treated as the leading candidate for a fifth defect rather than a settled result.
- **Four seeds on that family, one lost to the harness.** One killed by the timeout defect, one failed on a missing deliverable while extrapolating *below* the bar, one failed on capability, one passed. No executor comparison was run.
- **Three axes saturate and the argument that explains them is an argument, not a theorem.** It is refuted by exhibiting a task with a complete, unambiguous specification that a frontier executor reliably fails for a reason other than ambiguity.
- **The item audits are filters with unknown recall.** Unflagged items are unaudited, not validated. Roughly 1,150 items in one audited library still carry asserted keys that nothing has checked.
- **A library repaired by this standard looks worse.** Removing static items from discovery levels leaves one audited library with no runnable evidence at C5 and above. That is where it actually stands.
- Everything carried from earlier versions keeps its own limitations: three executors, one machine, 48 episodes, two seeds per class, four rungs of eight, one intervention budget.

The claim worth defending is Proposition 1 (acceptance invariance), which is a statement about the formula rather than about any model. The new claim worth defending is narrower and stated as such: **concordant cross-tier error is evidence about the item rather than the executors**, and it is refuted by exhibiting items that several independent executors fail identically and whose keys are then confirmed correct.

## Suggested categories

Primary `cs.AI`; cross-list `cs.HC` (the human-factors lineage in §11 and §21 is load-bearing) and `cs.SE` (the run-log schema, item-validity tests and reporting standards are engineering artifacts).

## Regenerating

```
cd unified_v19
pdflatex main && bibtex main && pdflatex main && pdflatex main
cp main.pdf ../Unified_Intelligence_Harness_Scoring_Framework_v1_9.pdf
tar czf unified-v19-arxiv.tar.gz main.tex main.bbl
```

`main.bbl` is committed on purpose: it ships inside the tarball because arXiv does not run BibTeX. It is a build input, not an artifact.
