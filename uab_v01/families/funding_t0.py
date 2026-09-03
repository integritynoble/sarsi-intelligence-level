"""funding T0 -- extract one deadline or eligibility requirement from a solicitation.

The solicitation carries several dates (letter of intent, full proposal, earliest start, an internal
routing note) and several eligibility clauses. GOAL.md names exactly one field. The plausible wrong
method -- take the first date, or the first sentence under 'Eligibility' -- fails on most seeds
because the generator orders the distractor first. Every key value appears verbatim in the text under
its own label, which is what the specification-key test asserts.

Budget-cross defect, found and repaired 2026-09-03: "verbatim from the Principal Investigator line"
was read by a real executor as including the phrase "the PI must hold", and a trailing period was
copied on another field; both were marked wrong on a rule the prose had not stated. The goal now
says which text to copy and the verifier strips the label phrase and the period.
"""
from __future__ import annotations
import datetime as dt
from pathlib import Path
from .common import rng, norm, read_json, result

FAMILY = "funding_t0"
FIELDS = ["full_proposal_deadline", "loi_deadline", "pi_eligibility", "institution_eligibility",
          "citizenship_requirement", "budget_cap"]
AGENCIES = ["National Instrumentation Foundation", "Office of Applied Photonics", "Regional Health Research Trust",
            "Computational Biology Initiative", "Energy Systems Directorate"]

def _date(r, year):
    return dt.date(year, r.randint(1, 12), r.randint(1, 28))

def generate(seed: int):
    r = rng(seed, FAMILY)
    field = FIELDS[seed % len(FIELDS)] if seed < 100 else r.choice(FIELDS)
    agency = r.choice(AGENCIES)
    prog = f"{r.choice(['Early Career', 'Instrument Development', 'Translational', 'Exploratory'])} Award {r.randint(2027, 2029)}"
    loi = _date(r, 2027)
    full = loi + dt.timedelta(days=r.randint(30, 90))
    start = full + dt.timedelta(days=r.randint(90, 200))
    pi = r.choice(["Principal Investigator status at the applicant institution",
                   "an independent research position with institutional PI eligibility",
                   "a faculty appointment at the rank of assistant professor or above"])
    inst = r.choice(["accredited institutions of higher education and non-profit research organizations",
                     "domestic non-profit research organizations only",
                     "any organization with a registered research office, including small businesses"])
    cit = r.choice(["no citizenship requirement", "the PI must be a citizen or permanent resident",
                    "at least one senior investigator must be a citizen"])
    cap = r.choice([150000, 250000, 400000, 750000, 1200000])
    # The trap must fire on every instance (v2.3 §17.4.3): the target is never the first date,
    # never the first eligibility line, and never the first USD figure.
    date_lines = [f"  Letter of intent due: {loi.isoformat()}", f"  Full proposal due: {full.isoformat()}"]
    if field == "loi_deadline":
        date_lines.reverse()
    elig = [("institution_eligibility", f"  Institutions: {inst}."),
            ("pi_eligibility", f"  Principal Investigator: the PI must hold {pi}."),
            ("citizenship_requirement", f"  Citizenship: {cit}.")]
    while elig[0][0] == field:
        elig.append(elig.pop(0))
    text = "\n".join([
        f"{agency}",
        f"Program solicitation: {prog}",
        "",
        "IMPORTANT DATES",
        *date_lines,
        f"  Earliest start date: {start.isoformat()}",
        "  Note: most institutions require internal routing five business days before the",
        "  sponsor deadline; that internal date is set by your institution, not by this program.",
        "",
        "ELIGIBILITY",
        *[line for _, line in elig],
        "  Prior awards: current awardees of this program may not apply as PI.",
        "",
        "BUDGET",
        "  Minimum request: USD 25,000 per year.",
        f"  Total budget cap: USD {cap:,} over the full award period, direct and indirect costs combined.",
        "",
    ])
    labels = {"full_proposal_deadline": full.isoformat(), "loi_deadline": loi.isoformat(),
              "pi_eligibility": pi, "institution_eligibility": inst, "citizenship_requirement": cit,
              "budget_cap": str(cap)}
    goal = "\n".join([
        "# GOAL", "",
        f"From `solicitation.txt`, extract the field **{field}** and write `answer.json` as",
        '`{"field": "<field name>", "value": "<value>"}`.', "",
        "Field definitions (disclosed):",
        "- full_proposal_deadline: the sponsor's full-proposal due date, ISO format. Not the letter-of-intent",
        "  date, not the earliest start date, not any internal routing date.",
        "- loi_deadline: the letter-of-intent due date, ISO format.",
        "- pi_eligibility: the text after `the PI must hold` on the Principal Investigator line, verbatim,",
        "  without that phrase and without the trailing period.",
        "- institution_eligibility: the text after `Institutions:` on that line, verbatim, without the trailing period.",
        "- citizenship_requirement: the text after `Citizenship:` on that line, verbatim, without the trailing period.",
        "- budget_cap: the total cap as an integer number of USD, digits only.", "",
    ])
    files = {"GOAL.md": goal, "solicitation.txt": text}
    key = {"family": FAMILY, "seed": seed, "field": field, "value": labels[field], "all": labels}
    return files, key

def verify(ws: Path, key: dict) -> dict:
    ans = read_json(ws / "answer.json")
    checks = []
    if ans is None or ans == "INVALID_JSON" or not isinstance(ans, dict):
        checks.append(("answer_json_present", False, "answer.json missing or not a JSON object"))
        return result(False, 0.0, checks, "not_attempted")
    checks.append(("answer_json_present", True, "ok"))
    field_ok = ans.get("field") == key["field"]
    checks.append(("field_named", field_ok, f"expected field {key['field']}"))
    val = str(ans.get("value", ""))
    want = key["value"]
    # tolerate the two readings the first wording left open: the label phrase and the trailing period
    v = norm(val).rstrip(".")
    for prefix in ("the pi must hold ", "institutions: ", "citizenship: "):
        if v.startswith(prefix): v = v[len(prefix):]
    value_ok = v == norm(want).rstrip(".") if key["field"] != "budget_cap" else val.strip() == want
    checks.append(("value_exact", value_ok, "expected " + want))
    src = (ws / "solicitation.txt").read_text(encoding="utf-8")
    verb = norm(val) in norm(src) or (key["field"] == "budget_cap" and f"{int(val):,}" in src if val.isdigit() else False)
    checks.append(("value_appears_in_source", bool(verb), "value must come from the document"))
    passed = field_ok and value_ok
    acc = sum(1 for _, ok, _ in checks if ok) / len(checks)
    mode = None if passed else ("wrong_field" if not field_ok else "wrong_value")
    return result(passed, acc, checks, mode)

def _parse(src: str) -> dict:
    out = {}
    for line in src.splitlines():
        s = line.strip()
        if s.startswith("Letter of intent due:"): out["loi_deadline"] = s.split(":", 1)[1].strip()
        elif s.startswith("Full proposal due:"): out["full_proposal_deadline"] = s.split(":", 1)[1].strip()
        elif s.startswith("Institutions:"): out["institution_eligibility"] = s.split(":", 1)[1].strip().rstrip(".")
        elif s.startswith("Principal Investigator:"): out["pi_eligibility"] = s.split("must hold", 1)[1].strip().rstrip(".")
        elif s.startswith("Citizenship:"): out["citizenship_requirement"] = s.split(":", 1)[1].strip().rstrip(".")
        elif s.startswith("Total budget cap:"):
            import re
            out["budget_cap"] = re.search(r"USD ([\d,]+)", s).group(1).replace(",", "")
    return out

def _field(ws: Path) -> str:
    import re
    return re.search(r"extract the field \*\*(\w+)\*\*", (ws / "GOAL.md").read_text(encoding="utf-8")).group(1)

def reference_solve(ws: Path) -> None:
    import json
    field = _field(ws)
    vals = _parse((ws / "solicitation.txt").read_text(encoding="utf-8"))
    (ws / "answer.json").write_text(json.dumps({"field": field, "value": vals[field]}), encoding="utf-8")

def naive_solve(ws: Path) -> None:
    """First date in the document for any date field; first sentence under ELIGIBILITY for any
    eligibility field; the first number under BUDGET for the cap."""
    import json, re
    field = _field(ws)
    src = (ws / "solicitation.txt").read_text(encoding="utf-8")
    if field.endswith("deadline"):
        val = re.search(r"\d{4}-\d{2}-\d{2}", src).group(0)
    elif field == "budget_cap":
        val = re.search(r"USD ([\d,]+)", src).group(1).replace(",", "")
    else:
        block = src.split("ELIGIBILITY", 1)[1]
        val = block.strip().splitlines()[0].split(":", 1)[1].strip().rstrip(".")
    (ws / "answer.json").write_text(json.dumps({"field": field, "value": val}), encoding="utf-8")

def spec_key_check(seed: int) -> None:
    files, key = generate(seed)
    goal, src = files["GOAL.md"], files["solicitation.txt"]
    assert f"**{key['field']}**" in goal, "goal names a different field than the key"
    want = key["value"] if key["field"] != "budget_cap" else f"{int(key['value']):,}"
    assert want in src, f"key value not verbatim in the solicitation: {want}"
    assert _parse(src)[key["field"]] == key["value"], "the labelled line and the key disagree"
    # the trap fired: the naive method does not produce the key on this instance
    import tempfile, shutil, json
    from .common import write_workspace
    d = Path(tempfile.mkdtemp()); write_workspace(d, files); naive_solve(d)
    got = json.loads((d / "answer.json").read_text())["value"]; shutil.rmtree(d)
    assert norm(str(got)) != norm(str(key["value"])), "naive method reproduces the key; the trap did not fire"
