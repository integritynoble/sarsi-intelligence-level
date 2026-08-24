# arXiv Submission Package — Difficulty Is Not the Index

| File | Purpose |
|---|---|
| `delegation-frontier-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — arXiv does not run BibTeX |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../Difficulty_Is_Not_The_Index.pdf` | Compiled PDF, 14 pages |
| `../Difficulty_Is_Not_The_Index.md` | Same paper, Markdown |

Verified: extracts to an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, no overfull boxes, 14 pages, zero Type 3 fonts, all fonts embedded Type 1.

## What this paper is, and what it is not

It is the **companion** to *Delegation Intelligence*, which is the framework it repairs and the source of everything it uses: T0–T6, H0–H5, DL0–DLΩ, CID0–CID6, the ten anti-inflation rules, and the frontier itself. **Post that one first.** This paper is unreadable without it — every section takes an object from it and changes one thing about that object.

What this paper adds is analytic rather than architectural: five propositions, two corollaries, one definition, and a reporting form. The framework answers *how do we measure delegation*; this asks *what does the measurement get wrong, and in which direction*.

If both are posted, cite the framework's identifier in this paper's comments field and add it to `references.bib` under `yang2026delegation`, whose `note` currently gives only a description.

## Dependency warning

Every result is conditional on premises from unpublished working papers, and a referee will ask.

- **Propositions 1, 2 and 3** are about the frontier as the framework defines it. If the definition is revised — in particular if the frontier is already understood as set-valued rather than a maximum — Proposition 1 lapses and Proposition 2 weakens to a caveat.
- **Propositions 4 and 5** rest on the acceptance ceiling from the task-property account, which is itself unpublished.
- **The §6.3 reading of T_δ** is one system and one absence. It establishes that the quantity was unrecorded there and nothing about the field.
- **Nothing is measured.** The tables in §3.2 and §4.1 are worked illustrations, which by this paper's own standard makes them illustrations and not findings. §10 says so first.

§10 states all of this. The package should not be submitted as though the parent framework were settled literature.

## Suggested categories

Primary `cs.AI`; cross-list `cs.HC` (the human-factors lineage in §2 is load-bearing) and `cs.SE` (the reporting form and episode record in §8 are engineering artifacts).

## Regenerating

```
cd delegation_frontier
pdflatex main && bibtex main && pdflatex main && pdflatex main
cp main.pdf ../Difficulty_Is_Not_The_Index.pdf
tar czf delegation-frontier-arxiv.tar.gz main.tex main.bbl
```

`main.bbl` is committed on purpose: it ships inside the tarball because arXiv does not run BibTeX. It is a build input, not an artifact.
