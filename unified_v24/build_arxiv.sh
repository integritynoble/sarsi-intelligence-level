#!/usr/bin/env bash
set -euo pipefail

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$script_dir"

latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

cp main.pdf Unified_Intelligence_Theory_and_AI_Level_v2_4.pdf

tar --sort=name \
    --mtime='UTC 2026-09-03' \
    --owner=0 --group=0 --numeric-owner \
    -czf unified-v24-arxiv.tar.gz \
    main.tex main.bbl references.bib fig_hsc.pdf fig_regime.pdf anc

sha256sum \
    Unified_Intelligence_Theory_and_AI_Level_v2_4.pdf \
    unified-v24-arxiv.tar.gz \
    > SHA256SUMS

