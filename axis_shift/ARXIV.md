# arXiv Submission Package — Substrate Indexing Is an Axis Shift

| File | Purpose |
|---|---|
| `axis-shift-arxiv.tar.gz` | **Upload this.** Contains `main.tex` and `main.bbl` |
| `main.tex` | LaTeX source |
| `main.bbl` | Pre-built bibliography — arXiv does not run BibTeX |
| `references.bib` | Kept for regeneration; **not** in the tarball |
| `../Substrate_Indexing_Is_An_Axis_Shift.pdf` | Compiled PDF, 10 pages |

Verified: extracts to an empty directory and compiles with plain `pdflatex` in two passes with **no BibTeX run** — no errors, no undefined citations, no undefined references, no missing files, no overfull boxes, 10 pages, zero Type 3 fonts, all fonts embedded Type 1.

## What this paper is, and what it is not

It is the **companion** to *Intelligence Inside the Circles*, which crosses the same two frameworks and is the descriptive account: per-domain role tables for both level scales, both complete matrices, a seven-role heterogeneous loop, and a unified state profile. **Post that one first.** This paper depends on it — §6's per-domain discussion compresses material treated there at length — and it does not duplicate it.

What this paper adds is analytic rather than descriptive: four propositions and a measurement. A crosswalk answers *what happens where*; this asks *why here rather than there*.

If both are posted, cite the crosswalk's identifier in this paper's comments field and add it to `references.bib` under `yang2026circles`, whose `note` currently gives only a date.

## Dependency warning

Three of the five results depend on premises from unpublished working papers, and a referee will ask.

- **Propositions 1 and 4** rest on the substrate framework's closure criteria as written. Its own author concedes the domain list is "neither obviously complete nor obviously minimal," and §11.3 says so.
- **Proposition 3** rests on the coherence bound from the two-axis framework.
- **Proposition 2** is an ordering by inspection, not a measurement, and inherits the substrate framework's unresolved step-weighting problem.

§11 states all of this. The package should not be submitted as though the parent frameworks were settled literature.

## Submission form values

**Categories.** Primary `cs.AI`. Cross-list `cs.MA` (Multiagent Systems) for the organizational-axis results and `cs.CY` (Computers and Society) for the authority and governance material.

**License.** CC BY 4.0 if you want it cited and quoted freely. **Cannot be changed after announcement.**

**Comments field.** Suggested:

> 10 pages, 3 tables. Companion to arXiv:XXXX.XXXXX (per-domain crosswalk).

**Abstract.** Paste the text below. It is 1823 characters against arXiv's 1920 limit.

```
Two frameworks describe recursive self-improvement from different starting points. One indexes it by substrate -- software, hardware, matter, biology, stellar energy -- and argues the binding constraint migrates outward from one domain to the next. The other indexes it by who changes what: an individual's write depth and an organization's coordination depth. Crossing them supplies something the first asserts without mechanism: why substrate is the right index.

The bridge is the improvement loop both share: identify, implement, validate, deploy. We assign each step to an axis and obtain a result holding in every domain. Validate is organizational by necessity and deploy is organizational always, because a system that authorizes its own deployment has self-certified rather than validated. Two of four steps of every loop, in every domain, are organizational by construction, and no individual level closes any loop alone.

From this follows the central claim. Reading the five substrate closure criteria against the level definitions, the individual requirement saturates while the organizational requirement keeps climbing. Chip specification, machine design and collector design are ordinary engineering cognition; what is hard about the outer domains is everything after the identify step. Substrate indexing is therefore an axis shift, and the intelligence-explosion argument -- a claim about a machine improving its own cognition -- is an argument about one domain only.

Two asymmetries appear at the top: no stated closure criterion requires open-ended individual intelligence, and the outermost domain admits no individual coordinate at all, since a structure spanning an astronomical unit exceeds the coherence bound. We also report that authorization latency, the quantity binding the organizational axis in every domain, has never been observed on a deployed governed system.
```

## Notes for the moderator queue

**The propositions are elementary.** Proposition 1 is a one-line argument and Proposition 3 is arithmetic given its premise. Neither is presented as deep; both are presented as load-bearing, which is a different claim.

**One empirical section, one system.** The measurement is a single audit log on a single host, stated as such in §9 and §11.5. It is offered as evidence that the quantity is unrecorded, not as a finding about the field.

**Self-referential citation.** This paper, its companion crosswalk, and both parent frameworks are by the same author. That is stated in §1.4 and §11.6 rather than left to be noticed.
