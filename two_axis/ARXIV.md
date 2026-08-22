# arXiv Submission Package — A Two-Axis Intelligence Level Framework, Version 2

Everything needed to submit the level-framework paper. It uses the same setup as the other SARSI papers in this repository, so these instructions differ only in the values you paste into the form.

| File | Purpose |
|---|---|
| `two-axis-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — arXiv does not run BibTeX |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../Two_Axis_Intelligence_Level_Framework_v2.pdf` | Compiled PDF, 13 pages |

Verified: extracts to an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, no overfull boxes, 13 pages, zero Type 3 fonts, all fonts embedded Type 1.

## Relation to Version 1

This supersedes `../Two_Axis_Intelligence_Level_Framework_AI_Agents.pdf`, which is retained in the repository as the record. **Version 1 has not been posted**, so there is no arXiv identifier to cite and no replacement to file — submit this as a new paper, not as `v2` of an existing announcement.

The paper is self-contained: it restates Version 1's scales, transition tests, and evidence rules rather than referring to them, so a reviewer needs no other document open. That was deliberate. A submission whose central claims are corrections to an unpublished predecessor is hard to review if the predecessor is not in front of the reader.

If Version 1 is posted first, add its identifier to `references.bib` under `yang2026twoaxis`, whose `note` field currently says only "Version 1, 22 August 2026."

## Submission form values

**Categories.** Primary `cs.AI` — this is a taxonomy-and-measurement paper about AI systems generally. Cross-list `cs.MA` (Multiagent Systems) for the organizational scale and the separation results, and `cs.CY` (Computers and Society) for the authority and governance material.

**License.** CC BY 4.0 if you want it cited and quoted freely. **Cannot be changed after announcement.**

**Comments field.** Suggested:

> 13 pages, 3 tables. Version 2 of a working framework; supersedes an unposted Version 1.

**Abstract.** Paste the text below. It is 1741 characters against arXiv's 1920 limit. The PDF keeps its own longer abstract.

```
We revise a two-axis taxonomy for agentic AI: an Individual Intelligence Evolution Scale (reactive, persistent, adaptive-learning, self-improving, recursively self-improving, autonomous-discovery, open-ended) and an Organizational Intelligence Evolution Scale. The prior version's scales, transition tests and anti-inflation evidence rules are retained; this version repairs three problems internal to them, adds a physical bound, and reports a measurement.

The open-ended individual level was undefined as stated. The framework requires improvement to be judged under an independent, predeclared evaluation, while that level by construction revises the objective the evaluation encodes. We resolve this with a frozen referee: versioned criteria, each revision judged against its immediate predecessor. Without one, open-ended evolution and undirected drift are observationally identical.

Organizational levels are gated rather than ordered. An organization can satisfy every behavioural description of a high level while proposing, evaluating and adopting through one locus, in which case its improvement claims are self-certified. Separation of proposer, evaluator and promoter becomes a precondition on the scale, and organizational intelligence is shown to be non-monotone in member level.

The individual axis has a ceiling. Coherence of a single decision locus requires R <= c*tau/2, so past a bound the available direction of development is a higher organizational level rather than a higher individual one, making organization the more fundamental coordinate.

We measure authorization latency, which bounds any governed loop's iteration rate. On a deployed governed system it has never been observed: two of three data points are promotions authorized within seconds of proposal, and the system of record has no timestamp for the event.
```

## Notes for the moderator queue

Two things a moderator may look at.

**It is a taxonomy paper with one empirical section.** The measurement in §8 is a single audit log on a single host, and §11 says so explicitly. It is offered as a demonstration that the quantity is unrecorded, not as a finding about the field.

**The propositions are elementary.** Proposition 1 (well-posedness) is a one-line argument, and Proposition 2 (coherence) is arithmetic given its premise. Neither is presented as deep; both are presented as load-bearing, which is a different claim. The paper says which of its results are derived and which are definitions, and §9 gives falsification targets for each.
