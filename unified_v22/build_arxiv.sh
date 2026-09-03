#!/usr/bin/env bash
set -euo pipefail

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$script_dir"

latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

cp main.pdf Unified_Intelligence_Harness_Scoring_Framework_v2_2.pdf

tar --sort=name \
    --mtime='UTC 2026-08-31' \
    --owner=0 --group=0 --numeric-owner \
    -czf unified-v22-arxiv.tar.gz \
    main.tex main.bbl references.bib anc

sha256sum \
    Unified_Intelligence_Harness_Scoring_Framework_v2_2.pdf \
    unified-v22-arxiv.tar.gz \
    > SHA256SUMS

