# arXiv Submission Checklist

Status of all five papers. Everything marked **ready** is built, verified, and needs no further work from this side. Everything marked **you** requires an arXiv login and cannot be done by tooling — arXiv has no submission API.

Last verified: 2026-08-01.

---

## Blocking items (do these first)

| | Item | Why it blocks | Est. time |
|---|---|---|---|
| ☐ | **`cs.AI` endorsement** | If `integritynoble` has not posted to `cs.AI`, arXiv rejects the submission until an existing `cs.AI` author endorses you. Separate process from upload. | days — **start now** |
| ☐ | **`cs.MA` endorsement** | Papers 3 and 5 lead with `cs.MA`, which endorses separately from `cs.AI`. Alternative: lead both with `cs.AI` and cross-list `cs.MA`. | days |
| ☐ | **License decision** | **Cannot be changed after announcement.** CC BY 4.0 if you want the work freely cited, quoted, and built on; arXiv's default non-exclusive licence is more restrictive. | minutes |

The repo is public (`https://github.com/integritynoble/sarsi-intelligence-level`), so an endorser can read the papers without an account. That was the practical blocker on endorsement and it is now cleared.

---

## Submission order — this matters

Papers 2–5 cite paper 1's arXiv identifier in their comments fields, currently written as the placeholder `arXiv:XXXX.XXXXX`.

1. **Submit paper 1 first.** Wait for announcement (typically next business day).
2. **Send me the identifier.** I will fill it into all four remaining papers' comments fields, rebuild their tarballs, and push.
3. **Then submit papers 2–5**, in any order.

Submitting out of order is not fatal — you would just be announcing a paper whose cross-reference reads `XXXX.XXXXX`. Avoidable.

---

## Per-paper status

### 1. Recursive Self-Improvement Is Substrate-Indexed — system scale

| | |
|---|---|
| Package | `arxiv/sarsi-l-v3-arxiv.tar.gz` (29 KB) — **ready** |
| PDF | 25 pp |
| Primary / cross-list | `cs.AI` / `cs.CY` |
| Full form values | [`arxiv/README.md`](arxiv/README.md) |
| Comments field | `25 pages, 12 tables, no figures. Three propositions with proofs; four-scenario timeline ranges; falsification conditions and a pre-registration protocol.` |

☐ Upload ☐ Paste metadata ☐ Preview compiled PDF ☐ Submit

### 2. Functional Self-Awareness for SARSI Agents — agent scale

| | |
|---|---|
| Package | `self_awareness/sarsi-selfaware-arxiv.tar.gz` (40 KB) — **ready** |
| PDF | 34 pp |
| Primary / cross-list | `cs.AI` / `cs.MA`, `cs.CY` |
| Full form values | [`self_awareness/ARXIV.md`](self_awareness/ARXIV.md) |
| Comments field | needs paper 1's identifier |

☐ Identifier filled ☐ Upload ☐ Metadata ☐ Preview ☐ Submit

### 3. A Manager Is Not a Controller — fleet scale

| | |
|---|---|
| Package | `fleet/sarsi-manager-arxiv.tar.gz` (17 KB) — **ready** |
| PDF | 14 pp |
| Primary / cross-list | `cs.MA` / `cs.AI`, `cs.CY` |
| Full form values | [`fleet/ARXIV.md`](fleet/ARXIV.md) |
| Comments field | needs paper 1's identifier |

☐ Identifier filled ☐ Upload ☐ Metadata ☐ Preview ☐ Submit

### 4. Hierarchical SARSI v3.1 — Deployment Edition

| | |
|---|---|
| Package | `singularity_edition/sarsi-hierarchical-v31-arxiv.tar.gz` (13 KB) — **ready** |
| PDF | 12 pp |
| Primary / cross-list | `cs.AI` / `cs.SE`, `cs.MA` |
| Overview | [`singularity_edition/README.md`](singularity_edition/README.md) |
| Comments field | needs paper 1's identifier |

☐ Identifier filled ☐ Upload ☐ Metadata ☐ Preview ☐ Submit

### 5. One Chat Box, Five Agents — console design

| | |
|---|---|
| Package | `console_design/sarsi-console-design-arxiv.tar.gz` (35 KB) — **ready** |
| PDF | 42 pp |
| Primary / cross-list | `cs.MA` / `cs.AI`, `cs.HC` |
| Overview | [`console_design/README.md`](console_design/README.md) |
| Comments field | needs paper 1's identifier |

☐ Identifier filled ☐ Upload ☐ Metadata ☐ Preview ☐ Submit

---

## Verification evidence

Each tarball was extracted into an **empty** directory and compiled with plain `pdflatex`, twice, **with no BibTeX run** — replicating arXiv's own process:

| Paper | errors | undefined refs | missing files | Type 3 fonts | pages |
|---|---|---|---|---|---|
| 1 · system | 0 | 0 | 0 | 0 | 25 |
| 2 · agent | 0 | 0 | 0 | 0 | 34 |
| 3 · fleet | 0 | 0 | 0 | 0 | 14 |
| 4 · deployment | 0 | 0 | 0 | 0 | 12 |
| 5 · console | 0 | 0 | 0 | 0 | 42 |

Three setup choices, applied identically to all five:

- **`main.tex` + `main.bbl` ship; `references.bib` does not.** arXiv does not run BibTeX — a `.bib` alone renders every citation as `[?]`.
- **`\pdfoutput=1`** in the first lines, forcing the pdflatex path. Matters most where figures are inline TikZ with no `.eps` fallback.
- **URW Type 1 font trio** (`mathptmx` + `helvet` + `courier`). Verified with `pdffonts`: no Type 3 or bitmap fonts, which arXiv discourages because they render poorly on screen.

---

## Not applicable to this submission

Recorded so their absence reads as a decision rather than an omission.

- **Co-author sign-off** — single author.
- **Figure optimisation** — there are no external figure files. Every diagram is inline TikZ compiled from source, so there is nothing to downsample or convert.
- **Data/code availability statement** — present in papers 2 and 5, which describe a private deployment. No datasets were produced.
- **Anonymisation** — arXiv preprints are not blind.

---

## If a build fails on arXiv

The tarballs compile here, but arXiv's TeX Live may differ. If it rejects one:

1. Copy the exact error from arXiv's log.
2. Give it to me — I will reproduce, fix the source, rebuild, re-verify clean-room, and push.

Do **not** work around it by uploading a PDF-only submission. arXiv accepts that, but it forfeits full-text indexing and the ability to generate other formats, and it cannot be converted to source later.

---

## After announcement

☐ Send me paper 1's identifier → I fill the four cross-references, rebuild, push
☐ Add identifiers to the repo README
☐ Optional: update `references.bib` across all five so the papers cite each other by identifier rather than by title
