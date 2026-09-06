#!/usr/bin/env python3
"""Minimal Markdown -> LaTeX -> PDF for the free edition: headings, bold/italic, bullets, numbered lists, tables, rules, links."""
import re, sys, subprocess, html
from pathlib import Path
src = Path(sys.argv[1]); out = src.with_suffix('.tex')
def esc(t):
    t = t.replace('\\', r'\textbackslash{}')
    for a, b in [('&', r'\&'), ('%', r'\%'), ('$', r'\$'), ('#', r'\#'), ('_', r'\_'), ('{', r'\{'), ('}', r'\}'), ('~', r'\textasciitilde{}'), ('^', r'\textasciicircum{}')]:
        t = t.replace(a, b)
    t = t.replace('★', r'$\star$').replace('—', '---').replace('–', '--').replace('…', r'\ldots{}')
    return t
def inline(t):
    t = esc(t)
    t = re.sub(r'\\\*\\\*(.+?)\\\*\\\*|\*\*(.+?)\*\*', lambda m: r'\textbf{' + (m.group(1) or m.group(2)) + '}', t)
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'\\emph{\1}', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: r'\href{' + m.group(2).replace('\\_', '_').replace('\\%', '%') + '}{' + m.group(1) + '}', t)
    return t
lines = src.read_text().split('\n'); body = []; i = 0; in_ul = in_ol = False; title_block = []
def close():
    global in_ul, in_ol
    if in_ul: body.append(r'\end{itemize}'); in_ul = False
    if in_ol: body.append(r'\end{enumerate}'); in_ol = False
while i < len(lines):
    l = lines[i]
    if l.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[-| :]+\|$', lines[i+1].strip()):
        close(); hdr = [c.strip() for c in l.strip('|').split('|')]; i += 2; rows = []
        while i < len(lines) and lines[i].startswith('|'): rows.append([c.strip() for c in lines[i].strip('|').split('|')]); i += 1
        n = len(hdr); spec = '@{}' + 'p{2.6cm}' + 'X' * (n - 1) + '@{}'
        body.append(r'\begin{center}\small\begin{tabularx}{\textwidth}{' + spec + '}\toprule ' + ' & '.join(inline(h) for h in hdr) + r' \\ \midrule')
        for r in rows: body.append(' & '.join(inline(c) for c in r) + r' \\')
        body.append(r'\bottomrule\end{tabularx}\end{center}'); continue
    if l.startswith('# '):  close(); title_block.append(r'{\LARGE\bfseries ' + inline(l[2:]) + r'}\\[6pt]')
    elif l.startswith('## ') and not body and len(title_block) < 3: title_block.append(r'{\Large\bfseries ' + inline(l[3:]) + r'}\\[4pt]')
    elif l.startswith('### ') and not body and len(title_block) < 4: title_block.append(r'{\large\itshape ' + inline(l[4:]) + r'}\\[10pt]')
    elif l.startswith('## '): close(); body.append(r'\section*{' + inline(l[3:]) + '}')
    elif l.startswith('### '): close(); body.append(r'\subsection*{' + inline(l[4:]) + '}')
    elif l.strip() == '---': close(); body.append(r'\medskip\noindent\rule{\textwidth}{0.3pt}\medskip')
    elif re.match(r'^- ', l):
        if not in_ul: close(); body.append(r'\begin{itemize}[leftmargin=1.4em,itemsep=2pt]'); in_ul = True
        body.append(r'\item ' + inline(l[2:]))
    elif re.match(r'^\d+\. ', l):
        if not in_ol: close(); body.append(r'\begin{enumerate}[leftmargin=1.6em,itemsep=2pt]'); in_ol = True
        body.append(r'\item ' + inline(re.sub(r'^\d+\. ', '', l)))
    elif l.strip() == '': close(); body.append('')
    elif not body and l.startswith('**') and len(title_block) < 8: title_block.append(inline(l) + r'\\[2pt]')
    elif not body and l.startswith('*') and len(title_block) < 9: title_block.append(r'\\[4pt]' + inline(l) + r'\\[14pt]')
    else: body.append(inline(l))
    i += 1
close()
tex = r'''\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage[margin=1in]{geometry}
\usepackage{mathptmx}\usepackage{booktabs}\usepackage{tabularx}\usepackage{enumitem}\usepackage{microtype}
\usepackage[colorlinks=true,linkcolor=blue!60!black,urlcolor=blue!60!black]{hyperref}\usepackage{fancyhdr}
\pagestyle{fancy}\fancyhf{}\fancyhead[L]{\small AI-Level --- The Free Edition}\fancyhead[R]{\small Yang}\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.3pt}\setlength{\headheight}{14pt}\setlength{\parskip}{4pt}
\begin{document}
\begin{center}
''' + '\n'.join(t for t in title_block if t.strip()) + r'''
\end{center}
''' + '\n'.join(body) + r'''
\end{document}
'''
out.write_text(tex)
r = subprocess.run(['pdflatex', '-interaction=nonstopmode', out.name], cwd=src.parent, capture_output=True, text=True)
r = subprocess.run(['pdflatex', '-interaction=nonstopmode', out.name], cwd=src.parent, capture_output=True, text=True)
pdf = src.with_suffix('.pdf'); print('pdf:', pdf.exists(), pdf)
