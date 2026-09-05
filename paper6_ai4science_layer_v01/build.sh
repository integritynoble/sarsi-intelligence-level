#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
{ cat preamble.tex body.tex; printf '\n\\bibliographystyle{plainnat}\n\\bibliography{references}\n\\end{document}\n'; } > main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf The_AI4Science_Layer_v0_1.pdf
