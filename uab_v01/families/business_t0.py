"""business T0 -- extract one market or company fact from a brief.

company_brief.txt carries figures across years, a restated prior figure, and a competitor's figures.
GOAL.md names one fact. The plausible wrong method -- the first number after the keyword -- fails on
every instance because the generator places a restated or competitor figure before the target.
"""
from __future__ import annotations
import json, re
from pathlib import Path
from .common import rng, norm, read_json, result

FAMILY = "business_t0"
FACTS = ["revenue_fy2025", "headcount_end_2025", "latest_round_amount", "founding_year", "arr_q4_2025"]
COMPANIES = ["Halcyon Labs", "Northbridge AI", "Lumen Diagnostics", "Vantage Compute", "Orrery Systems"]

def generate(seed: int):
    r = rng(seed, FAMILY)
    fact = FACTS[seed % len(FACTS)] if seed < 100 else r.choice(FACTS)
    co, comp = r.sample(COMPANIES, 2)
    rev24 = r.randint(20, 400); rev25 = rev24 + r.randint(5, 120); rev25_prev = rev25 - r.randint(3, 15)
    head24 = r.randint(80, 900); head25 = head24 + r.randint(20, 300); head_mid = head24 + r.randint(5, 19)
    rnd = r.choice([15, 25, 40, 60, 120, 200]); prev_rnd = r.choice([5, 8, 12])
    founded = r.randint(2009, 2021); comp_founded = founded - r.randint(1, 6)
    arr = r.randint(30, 500); arr_q3 = arr - r.randint(4, 30)
    comp_rev = rev25 + r.randint(50, 300)
    lines = [
        f"{co} -- company brief (prepared 2026-01)", "",
        "Peer comparison",
        f"  {comp} (founded {comp_founded}) reported FY2025 revenue of USD {comp_rev}M and about {head25 + 400} employees.", "",
        "Financials",
        f"  FY2025 revenue was previously reported as USD {rev25_prev}M and restated to USD {rev25}M after the audit.",
        f"  FY2024 revenue: USD {rev24}M.",
        f"  ARR at the end of Q3 2025 was USD {arr_q3}M; ARR at the end of Q4 2025 was USD {arr}M.", "",
        "People",
        f"  Headcount reached {head_mid} in mid-2025 and {head25} at the end of 2025 (up from {head24} at the end of 2024).", "",
        "Funding",
        f"  Seed round: USD {prev_rnd}M. Latest round (Series B, closed 2025-11): USD {rnd}M.", "",
        "History",
        f"  The company was incorporated in {founded}, two years after its founders left {comp}.", "",
    ]
    text = "\n".join(lines)
    values = {"revenue_fy2025": (str(rev25), "USD million"), "headcount_end_2025": (str(head25), "employees"),
              "latest_round_amount": (str(rnd), "USD million"), "founding_year": (str(founded), "year"),
              "arr_q4_2025": (str(arr), "USD million")}
    defs = {"revenue_fy2025": "FY2025 revenue as finally reported (the restated figure, not the previously reported one), in USD million",
            "headcount_end_2025": "headcount at the end of 2025 (not mid-year, not the peer's)",
            "latest_round_amount": "the amount of the most recent funding round, in USD million",
            "founding_year": "the year the company was incorporated (not the peer's founding year)",
            "arr_q4_2025": "ARR at the end of Q4 2025, in USD million (not Q3)"}
    goal = "\n".join([
        "# GOAL", "",
        f"From `company_brief.txt`, extract **{fact}** for {co} and write `fact.json` as",
        '`{"fact": "<name>", "value": "<digits only>", "unit": "<unit>", "source_line": "<the line the value came from, verbatim>"}`.', "",
        "Disclosed definitions:", *[f"- {k}: {v}" for k, v in defs.items()], "",
        "Units: `USD million`, `employees`, or `year`. The brief also reports a peer company and restated or",
        "interim figures; those are distractors and are not the fact asked for.", "",
    ])
    files = {"GOAL.md": goal, "company_brief.txt": text}
    key = {"family": FAMILY, "seed": seed, "fact": fact, "value": values[fact][0], "unit": values[fact][1], "company": co}
    return files, key

def verify(ws: Path, key: dict) -> dict:
    ans = read_json(ws / "fact.json")
    checks = []
    if ans is None or ans == "INVALID_JSON" or not isinstance(ans, dict):
        checks.append(("fact_json_present", False, "fact.json missing or not a JSON object")); return result(False, 0.0, checks, "not_attempted")
    checks.append(("fact_json_present", True, "ok"))
    f_ok = ans.get("fact") == key["fact"]; checks.append(("fact_named", f_ok, f"expected {key['fact']}"))
    v_ok = str(ans.get("value", "")).strip() == key["value"]; checks.append(("value_exact", v_ok, f"expected {key['value']}"))
    u_ok = norm(str(ans.get("unit", ""))) == norm(key["unit"]); checks.append(("unit", u_ok, f"expected {key['unit']}"))
    src = (ws / "company_brief.txt").read_text(encoding="utf-8")
    line = str(ans.get("source_line", "")).strip()
    s_ok = bool(line) and norm(line) in norm(src) and key["value"] in line
    checks.append(("source_line_verbatim_and_contains_value", s_ok, ""))
    passed = f_ok and v_ok and u_ok and s_ok
    acc = sum(1 for _, ok, _ in checks if ok) / len(checks)
    mode = None if passed else ("wrong_value" if not v_ok else "provenance")
    return result(passed, acc, checks, mode)

def _fact(ws: Path) -> str:
    return re.search(r"extract \*\*(\w+)\*\*", (ws / "GOAL.md").read_text(encoding="utf-8")).group(1)

PATTERNS = {
    "revenue_fy2025": (r"restated to USD (\d+)M", "USD million"),
    "headcount_end_2025": (r"and (\d+) at the end of 2025", "employees"),
    "latest_round_amount": (r"Latest round \(.*?\): USD (\d+)M", "USD million"),
    "founding_year": (r"incorporated in (\d{4})", "year"),
    "arr_q4_2025": (r"end of Q4 2025 was USD (\d+)M", "USD million"),
}
KEYWORD = {"revenue_fy2025": "revenue", "headcount_end_2025": "employees", "latest_round_amount": "round",
           "founding_year": "founded", "arr_q4_2025": "ARR"}

def reference_solve(ws: Path) -> None:
    fact = _fact(ws); src = (ws / "company_brief.txt").read_text(encoding="utf-8")
    pat, unit = PATTERNS[fact]
    m = re.search(pat, src)
    line = next(l for l in src.splitlines() if m.group(0) in l).strip()
    (ws / "fact.json").write_text(json.dumps({"fact": fact, "value": m.group(1), "unit": unit, "source_line": line}), encoding="utf-8")

def naive_solve(ws: Path) -> None:
    """First number on the first line that contains the keyword."""
    fact = _fact(ws); src = (ws / "company_brief.txt").read_text(encoding="utf-8")
    kw = KEYWORD[fact]
    line = next(l for l in src.splitlines() if kw.lower() in l.lower()).strip()
    val = re.search(r"\d{4}" if fact == "founding_year" else r"\d+", line).group(0)
    (ws / "fact.json").write_text(json.dumps({"fact": fact, "value": val, "unit": PATTERNS[fact][1], "source_line": line}), encoding="utf-8")

def spec_key_check(seed: int) -> None:
    import tempfile, shutil
    from .common import write_workspace
    files, key = generate(seed)
    assert f"**{key['fact']}**" in files["GOAL.md"]
    m = re.search(PATTERNS[key["fact"]][0], files["company_brief.txt"])
    assert m and m.group(1) == key["value"], "labelled figure and key disagree"
    d = Path(tempfile.mkdtemp()); write_workspace(d, files); naive_solve(d)
    got = json.loads((d / "fact.json").read_text())["value"]; shutil.rmtree(d)
    assert got != key["value"], f"trap did not fire on seed {seed}: naive == key"
