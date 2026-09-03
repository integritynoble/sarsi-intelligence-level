#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
{ cat preamble.tex body_part1.tex body_part2.tex; printf '\n\\bibliographystyle{plainnat}\n\\bibliography{references}\n\\end{document}\n'; } > main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf Agents_That_Earn_a_Level_v0_1.pdf
