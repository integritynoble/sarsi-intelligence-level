#!/usr/bin/env python3
"""Measure a built PDF page by page: text past either margin, pages left under-filled, and (from the log) overfull boxes.

The text box is taken as the modal left/right/bottom of the pages themselves, so it needs no knowledge of the class.
Headers and page numbers are excluded by y-band.  A page is "short" only if it is not the last page and not the page
that ends a section whose next section starts a new page for a legitimate reason -- that judgement is left to the reader;
the script reports the fill percentage and the reader decides."""
import re, sys, collections
from pathlib import Path
import subprocess

def audit(pdf: Path, log: Path | None = None, fill_floor=0.65):
    xml = subprocess.run(["pdftotext", "-bbox", str(pdf), "-"], capture_output=True, text=True).stdout
    pages = re.split(r"<page ", xml)[1:]
    per = []
    for i, pg in enumerate(pages, 1):
        ws = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', pg)
        body = [w for w in ws if 60 < float(w[1]) < 700]
        if body:
            per.append({"p": i, "l": min(float(w[0]) for w in body), "r": max(float(w[2]) for w in body),
                        "b": max(float(w[3]) for w in body), "words": body})
    if not per: return {"pdf": pdf.name, "pages": 0}
    R = collections.Counter(round(x["r"]) for x in per).most_common(1)[0][0]
    L = collections.Counter(round(x["l"]) for x in per).most_common(1)[0][0]
    B = max(round(x["b"]) for x in per)   # the deepest baseline any page reaches; a modal bottom is fooled when many pages are short
    over = [(x["p"], round(x["r"]), " ".join(w[4] for w in x["words"] if float(w[2]) > R + 3)[:60]) for x in per if x["r"] > R + 3]
    left = [(x["p"], round(x["l"])) for x in per if x["l"] < L - 3]
    short = [(x["p"], round(100 * (x["b"] - 72) / (B - 72))) for x in per if x["b"] < B - (1 - fill_floor) * (B - 72) and x["p"] < len(per)]
    of = []
    if log and log.exists():
        t = log.read_text(errors="replace")
        of = sorted((float(m.group(1)) for m in re.finditer(r"Overfull \\hbox \(([\d.]+)pt too wide\)", t)), reverse=True)
    return {"pdf": pdf.name, "pages": len(per), "box": (L, R, B), "over_right": over, "over_left": left, "short": short,
            "overfull": len(of), "worst_overfull": of[:3], "qq": subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout.count("??")}

if __name__ == "__main__":
    for d in sys.argv[1:]:
        p = Path(d)
        pdf = p / "main.pdf"
        if not pdf.exists(): print(f"{d}: no main.pdf"); continue
        r = audit(pdf, p / "main.log")
        print(f"\n=== {d}: {r['pages']} pp, box L={r['box'][0]} R={r['box'][1]} bottom={r['box'][2]}, overfull={r['overfull']} {r['worst_overfull']}, '??'={r['qq']}")
        print(f"    past right margin: {r['over_right'] if r['over_right'] else 'none'}")
        if r["over_left"]: print(f"    past left margin:  {r['over_left']}")
        print(f"    under 65% filled:  {r['short'] if r['short'] else 'none'}")
