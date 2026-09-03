"""paper T0 -- verify one citation against the reference list.

manuscript.md cites several references in-text with author and year; references.bib holds the
entries. GOAL.md names one citation number and asks whether the in-text attribution and the bib
entry agree on four fields (first author, year, venue, pages), listing the fields that disagree.
The target always carries one or two discrepancies, at least one of which is not the year, so the
plausible wrong method -- compare the year only -- never produces the key. Other citations also
carry discrepancies, so checking the wrong citation fails too.
"""
from __future__ import annotations
import json
from pathlib import Path
from .common import rng, norm, read_json, result

FAMILY = "paper_t0"
AUTHORS = ["Okafor", "Lindqvist", "Marchetti", "Tanaka", "Haddad", "Petrova", "Nwosu", "Bergström", "Castillo", "Iyer"]
VENUES = ["Journal of Imaging Science", "Proc. ICML", "Nature Methods", "IEEE Trans. Med. Imaging", "Proc. NeurIPS"]
FIELDS = ["author", "year", "venue", "pages"]

def _entry(r, k):
    a = r.sample(AUTHORS, 2); y = r.randint(2015, 2026); v = r.choice(VENUES)
    p0 = r.randint(1, 900); pages = f"{p0}--{p0 + r.randint(5, 30)}"
    return {"key": f"ref{k}", "author": a, "year": y, "venue": v, "pages": pages,
            "title": r.choice(["Coded apertures revisited", "Learned priors for inverse problems",
                               "A benchmark for snapshot spectral imaging", "Restart continuity in agents",
                               "Calibration of clinical risk models", "On the measure of delegation"])}

def _perturb(r, e, fields):
    t = dict(e); t["author"] = list(e["author"])
    for f in fields:
        if f == "author": t["author"][0] = r.choice([x for x in AUTHORS if x not in e["author"]])
        elif f == "year": t["year"] = e["year"] + r.choice([-2, -1, 1, 2])
        elif f == "venue": t["venue"] = r.choice([x for x in VENUES if x != e["venue"]])
        elif f == "pages":
            a, b = e["pages"].split("--"); t["pages"] = f"{b}--{a}" if r.random() < 0.5 else f"{int(a) + 100}--{int(b) + 100}"
    return t

def generate(seed: int):
    r = rng(seed, FAMILY)
    n = 5
    bib = [_entry(r, k + 1) for k in range(n)]
    target = r.randint(1, n)
    intext = {}
    disc = {}
    for k in range(1, n + 1):
        if k == target:
            nonyear = r.choice(["author", "venue", "pages"])
            fields = [nonyear] + ([ "year"] if r.random() < 0.5 else [])
        else:
            fields = r.sample(FIELDS, r.choice([0, 1, 2]))
        disc[k] = sorted(fields)
        intext[k] = _perturb(r, bib[k - 1], fields)
    lines = ["# Manuscript excerpt", ""]
    for k in range(1, n + 1):
        t = intext[k]
        lines.append(f"As shown by {t['author'][0]} and {t['author'][1]} ({t['year']}) in {t['venue']}, pp. {t['pages']} [{k}], "
                     f"{r.choice(['the reconstruction error falls with mask density', 'restart recovery is the binding test', 'calibration is reported beside discrimination', 'the operator is known and the prior is learned'])}.")
    lines.append("")
    bibtext = "\n\n".join(
        f"@article{{{e['key']},\n  author = {{{e['author'][0]} and {e['author'][1]}}},\n  title = {{{e['title']}}},\n  journal = {{{e['venue']}}},\n  year = {{{e['year']}}},\n  pages = {{{e['pages']}}}\n}}"
        for e in bib) + "\n"
    goal = "\n".join([
        "# GOAL", "",
        f"Check citation **[{target}]** in `manuscript.md` against entry `ref{target}` in `references.bib` and write",
        '`citation_check.json` as `{"citation": <number>, "consistent": <true|false>, "discrepancies": [<field names>]}`.', "",
        "Disclosed rules: compare exactly four fields -- `author` (the first author's surname), `year`, `venue`",
        "(the journal or proceedings name) and `pages` (the page range, in order). A field is a discrepancy",
        "if the in-text attribution and the bib entry differ on it. `consistent` is true only if the",
        "discrepancy list is empty. Check only the citation named above; other citations may also be wrong",
        "and are not asked about.", "",
    ])
    files = {"GOAL.md": goal, "manuscript.md": "\n".join(lines), "references.bib": bibtext}
    key = {"family": FAMILY, "seed": seed, "citation": target, "discrepancies": disc[target], "all": disc}
    return files, key

def verify(ws: Path, key: dict) -> dict:
    ans = read_json(ws / "citation_check.json")
    checks = []
    if ans is None or ans == "INVALID_JSON" or not isinstance(ans, dict):
        checks.append(("citation_check_present", False, "citation_check.json missing or not a JSON object"))
        return result(False, 0.0, checks, "not_attempted")
    checks.append(("citation_check_present", True, "ok"))
    c_ok = ans.get("citation") == key["citation"]
    checks.append(("citation_number", c_ok, f"expected {key['citation']}"))
    got = sorted(norm(x) for x in ans.get("discrepancies", []) if isinstance(x, str))
    want = key["discrepancies"]
    d_ok = got == want
    checks.append(("discrepancy_set_exact", d_ok, f"expected {want}, got {got}"))
    b_ok = ans.get("consistent") is (len(want) == 0)
    checks.append(("consistent_flag", b_ok, ""))
    passed = c_ok and d_ok and b_ok
    inter = len(set(got) & set(want)); union = len(set(got) | set(want)) or 1
    acc = (c_ok + (inter / union) + b_ok) / 3
    mode = None if passed else ("wrong_citation" if not c_ok else "wrong_fields")
    return result(passed, acc, checks, mode)

def _parse_bib(text: str) -> dict:
    out = {}
    for block in text.split("@article{")[1:]:
        key = block.split(",", 1)[0].strip()
        f = {}
        for line in block.splitlines()[1:]:
            if "=" in line:
                k, v = line.split("=", 1); f[k.strip()] = v.strip().strip("{},").strip("{}")
        out[key] = {"author": f["author"].split(" and ")[0].strip(), "year": int(f["year"]), "venue": f["journal"], "pages": f["pages"]}
    return out

def _parse_intext(text: str) -> dict:
    import re
    out = {}
    for m in re.finditer(r"As shown by (\w+) and \w+ \((\d{4})\) in (.+?), pp\. (\S+) \[(\d+)\]", text):
        out[int(m.group(5))] = {"author": m.group(1), "year": int(m.group(2)), "venue": m.group(3), "pages": m.group(4)}
    return out

def _target(ws: Path) -> int:
    import re
    return int(re.search(r"citation \*\*\[(\d+)\]\*\*", (ws / "GOAL.md").read_text(encoding="utf-8")).group(1))

def reference_solve(ws: Path) -> None:
    k = _target(ws)
    bib = _parse_bib((ws / "references.bib").read_text(encoding="utf-8"))[f"ref{k}"]
    it = _parse_intext((ws / "manuscript.md").read_text(encoding="utf-8"))[k]
    disc = sorted(f for f in FIELDS if str(bib[f]) != str(it[f]))
    (ws / "citation_check.json").write_text(json.dumps({"citation": k, "consistent": not disc, "discrepancies": disc}), encoding="utf-8")

def naive_solve(ws: Path) -> None:
    """Compare the year only."""
    k = _target(ws)
    bib = _parse_bib((ws / "references.bib").read_text(encoding="utf-8"))[f"ref{k}"]
    it = _parse_intext((ws / "manuscript.md").read_text(encoding="utf-8"))[k]
    disc = ["year"] if bib["year"] != it["year"] else []
    (ws / "citation_check.json").write_text(json.dumps({"citation": k, "consistent": not disc, "discrepancies": disc}), encoding="utf-8")

def spec_key_check(seed: int) -> None:
    files, key = generate(seed)
    assert f"**[{key['citation']}]**" in files["GOAL.md"]
    bib = _parse_bib(files["references.bib"])[f"ref{key['citation']}"]
    it = _parse_intext(files["manuscript.md"])[key["citation"]]
    derived = sorted(f for f in FIELDS if str(bib[f]) != str(it[f]))
    assert derived == key["discrepancies"], f"key {key['discrepancies']} vs derived {derived}"
    assert any(f != "year" for f in key["discrepancies"]), "trap did not fire: year-only discrepancy"
