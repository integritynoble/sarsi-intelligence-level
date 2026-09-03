# arXiv submission guide - Unified Intelligence v2.2

Upload unified-v22-arxiv.tar.gz. It contains the TeX source, both bibliography
forms, and the two validated artifact releases under arXiv's reserved anc
directory. Do not upload only the PDF.

## Recommended metadata

**Title**

Measuring the Unified Intelligence Level: A Cumulative, Harness-Measurable Hierarchy

**Authors**

Chengshuai Yang¹,∗  Ting Xue¹

¹ NextGen PlatformAI C Corp, USA
∗ Correspondence: spiritai@platformai.org

The author must verify the account identity, email address, and any affiliation
entered in arXiv. Do not add an affiliation that is not current.

**Abstract**

Intelligence labels often conflate reasoning, persistent learning, collective
organization, autonomous task completion, and evidence-grounded self-modeling.
We present a measurement framework with five conceptual families--Cognitive,
Individual, Organizational, Delegation, and Self-Awareness--and six directly
measured coordinates [C,I,O,T,H,SA], where Delegation is derived from task
difficulty T, human cognitive intervention H, and externally verified
reliability. Long-term memory M is reported separately as a prerequisite for
higher Individual levels; a long context window does not certify persistence
across restarts. The Unified Intelligence scale U0--U-Omega is cumulative and
gated, and the experimental unit is a frozen model-harness pair. Two
preliminary programs test the instrument. Across three 48-episode harness
curves, a success-only delegation score was invariant to an acceptance-only
step for both stronger executors even as each one's false completions fell from
2/12 to 0/12; a delivered-outcome correction restores sensitivity. In a sealed, post-freeze
mechanism probe, one executor passed 5/12 instances versus 1/12 for another and
had lower RMSE on 11/12 pairs (two-sided sign test p=0.00635); the binary
comparison was not significant (McNemar p=0.125). This discriminates the
archived configurations on these instances, not model tiers in general.
Auditing also found four answer-key defects and two apparatus defects. We
therefore require specification-key tests, cross-tier concordance audits,
graded failure modes, per-coordinate headroom, longitudinal evidence, and
explicit resource envelopes. The level thresholds remain working definitions
requiring broader calibration.

This text is ASCII and below arXiv's 1,920-character abstract limit.

**Comments**

50 pages, 0 figures, 39 tables; includes data, code, schemas, and audit tools as ancillary files.

**Category recommendation**

- Primary: cs.AI (Artificial Intelligence)
- One cross-list: cs.MA (Multiagent Systems)

The primary contribution is an AI measurement and evaluation framework.
cs.MA is a defensible cross-list because the framework separately measures
organizational and multi-agent capability. Moderators may reclassify the paper;
do not add unrelated physics or machine-learning cross-lists merely because
individual examples mention those areas.

**License**

The author must choose this in the submission form. The choice is legal and
cannot be made by an editing agent. Confirm that the author has the right to
license the manuscript and ancillary files.

## Submission checklist

1. Log in as the author and confirm whether cs.AI endorsement is required.
2. Upload unified-v22-arxiv.tar.gz.
3. Select PDFLaTeX and main.tex if auto-detection does not.
4. Confirm that arXiv recognizes the anc directory as ancillary material.
5. Paste the ASCII metadata above; do not copy Unicode punctuation from a PDF.
6. Preview the arXiv-generated PDF page by page, especially all tables.
7. Confirm author identity, title, abstract, category, license, and disclosures.
8. Submit only after the author has inspected the data/code and scientific claims.

arXiv moderation is not peer review and acceptance cannot be guaranteed.
The remaining substantive risk is breadth: this is a preliminary measurement
framework with only one fully instrumented coordinate. The manuscript addresses
that risk by foregrounding measured corrections, releasing the evidence, and
limiting all generalization claims.

## Local rebuild

Run:

    ./build_arxiv.sh

The archive intentionally excludes local build logs, the compiled PDF, this
guide, and the build script.
