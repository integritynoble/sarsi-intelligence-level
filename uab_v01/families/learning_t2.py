"""U2 learning-transfer suite -- coordinate I (with M3), band T2, paired episodes.

Each seed generates TWO episodes that share one organization-specific convention the task text
never states:

  Episode A (experience)  clean a ledger (raw.csv -> cleaned.csv). A first attempt under the default
                          reading fails one registered check; the harness then hands back FEEDBACK.md
                          naming the convention and saying it applies to all future work for this
                          organization; a second attempt should pass.
  -- process restart; episode A's workspace is deleted --
  Episode B (held-out)    a DIFFERENT task (totals.json from a different ledger) in a new workspace,
                          where the same convention silently decides the answer.

Learning transfer is the paired difference  pass(B | after A) - pass(B | memory ablated).  The
floor is the ablated arm: the same pair, fresh store, episode B only. Nothing in B's text states the
convention, so B is passable only by a pair that carried the lesson across the restart. The default
reading (the "fresh" solver) fails B on every seed by construction; the spec-key test asserts it.

Conventions (one per seed, the others default):
  dup_last          a repeated id is a correction; keep the LAST row        (default: first)
  date_dayfirst     dates are DD/MM/YYYY                                     (default: MM/DD/YYYY)
  cents             amounts are integer cents; report dollars, 2 decimals    (default: as given)
  drop_blank_name   rows with a blank name are excluded                      (default: kept)
  desc_id           output ordered by id descending                          (default: ascending)
"""
from __future__ import annotations
import csv, io, json
from pathlib import Path
from .common import rng, read_json, result

FAMILY = "learning_t2"
CONVENTIONS = ["dup_last", "date_dayfirst", "cents", "drop_blank_name", "desc_id"]
NAMES = ["Ada", "Bram", "Chloe", "Dev", "Esme", "Farid", "Greta", "Hugo"]

LESSON = {
    "dup_last": "In this organization a repeated id is a correction: when an id appears more than once, the LAST row is the valid one and earlier rows are superseded.",
    "date_dayfirst": "In this organization dates are written day-first (DD/MM/YYYY), never month-first.",
    "cents": "In this organization the amount column is recorded in integer cents; reported amounts are dollars with two decimals (divide by 100).",
    "drop_blank_name": "In this organization a row whose name is blank is a void entry and is excluded from every output.",
    "desc_id": "In this organization every per-id output is ordered by id DESCENDING.",
}

def _rows(r, n, conv):
    ids = list(range(100, 100 + n)); r.shuffle(ids)
    rows = []
    for i in ids:
        rows.append({"id": str(i), "name": r.choice(NAMES), "date": f"{r.randint(1, 12):02d}/{r.randint(1, 12):02d}/2025", "amount": str(r.randint(100, 99999))})
    # make the convention matter on this instance
    if conv == "dup_last":
        dup = r.choice(rows); rows.append({"id": dup["id"], "name": dup["name"], "date": dup["date"], "amount": str(int(dup["amount"]) + r.randint(1000, 5000))})
    if conv == "date_dayfirst":
        rows[0]["date"] = f"{r.randint(13, 28):02d}/{r.randint(1, 12):02d}/2025"  # day > 12: month-first parse is impossible/wrong
        rows[1]["date"] = f"{r.randint(1, 12):02d}/{r.randint(1, 12):02d}/2025"
        while rows[1]["date"].split("/")[0] == rows[1]["date"].split("/")[1]:
            rows[1]["date"] = f"{r.randint(1, 12):02d}/{r.randint(1, 12):02d}/2025"
    if conv == "drop_blank_name":
        rows[r.randint(0, n - 1)]["name"] = ""
    if conv == "cents":
        for x in rows: x["amount"] = str(int(x["amount"]) if int(x["amount"]) % 100 else int(x["amount"]) + 7)
    return rows

def _csv(rows):
    o = io.StringIO(); w = csv.DictWriter(o, fieldnames=["id", "name", "date", "amount"]); w.writeheader(); w.writerows(rows); return o.getvalue()

def _apply(rows, conv):
    """Apply the organization convention (or defaults when conv is None) and return normalized rows."""
    out = {}
    for x in rows:
        if conv == "drop_blank_name" and not x["name"].strip():
            continue
        if x["id"] in out and conv != "dup_last":
            continue  # default: first occurrence wins
        d = x["date"].split("/")
        iso = f"{d[2]}-{d[1]}-{d[0]}" if conv == "date_dayfirst" else f"{d[2]}-{d[0]}-{d[1]}"
        amt = f"{int(x['amount']) / 100:.2f}" if conv == "cents" else x["amount"]
        out[x["id"]] = {"id": x["id"], "name": x["name"], "date": iso, "amount": amt}
    rows2 = sorted(out.values(), key=lambda y: int(y["id"]), reverse=(conv == "desc_id"))
    return rows2

def _totals(rows, conv):
    """Episode B answer: per-id amount after the convention, and per-month totals."""
    cleaned = _apply(rows, conv)
    per_id = [{"id": y["id"], "amount": y["amount"]} for y in cleaned]
    month = {}
    for y in cleaned:
        m = y["date"][:7]; month[m] = round(month.get(m, 0.0) + float(y["amount"]), 2)
    return {"per_id": per_id, "per_month": dict(sorted(month.items()))}

def generate_pair(seed: int):
    r = rng(seed, FAMILY)
    conv = CONVENTIONS[seed % len(CONVENTIONS)] if seed < 100 else r.choice(CONVENTIONS)
    rows_a = _rows(r, 6, conv); rows_b = _rows(r, 7, conv)
    baseline = [
        "Baseline conventions (disclosed; apply each one UNLESS this organization has told you otherwise in",
        "previous work for it):",
        "- source dates are MM/DD/YYYY; output dates are ISO YYYY-MM-DD;",
        "- amounts are reported exactly as given in the source;",
        "- when an id appears more than once, the FIRST row is kept;",
        "- rows with a blank name are kept;",
        "- per-id output is ordered by id ascending.",
        "Exactly one of these may be overridden by an organization convention; nothing in this file states",
        "which. The acceptance checks are registered by the organization and are hidden.", "",
    ]
    goal_a = "\n".join([
        "# GOAL (episode A)", "",
        "Clean `raw.csv` into `cleaned.csv` with columns `id,name,date,amount`: one row per id, `date` in ISO",
        "`YYYY-MM-DD`, `amount` as a string. If a check fails you will receive `FEEDBACK.md` and one further",
        "attempt.", "", *baseline,
    ])
    goal_b = "\n".join([
        "# GOAL (episode B)", "",
        "From `ledger.csv` (columns `id,name,date,amount`) write `totals.json` as",
        '`{"per_id": [{"id": "<id>", "amount": "<amount as string>"}, ...], "per_month": {"YYYY-MM": <sum as number>, ...}}`,',
        "one entry per id, months keyed by the ISO month of each kept row.", "", *baseline,
    ])
    files_a = {"GOAL.md": goal_a, "raw.csv": _csv(rows_a)}
    files_b = {"GOAL.md": goal_b, "ledger.csv": _csv(rows_b)}
    key = {"family": FAMILY, "seed": seed, "convention": conv,
           "a_expected": _apply(rows_a, conv), "b_expected": _totals(rows_b, conv), "b_default": _totals(rows_b, None),
           "lesson": LESSON[conv]}
    return files_a, files_b, key

def feedback(key: dict) -> str:
    return "\n".join(["# FEEDBACK from the organization's acceptance check", "",
                      "Your `cleaned.csv` was not accepted. The check that failed concerns a convention of this",
                      "organization that applies to every task you will ever do for it:", "", f"> {key['lesson']}", "",
                      "Remember this convention for all future work for this organization, including work in other",
                      "directories and after a restart. Correct `cleaned.csv` now.", ""])

def _read_csv(p: Path):
    return list(csv.DictReader(io.StringIO(p.read_text(encoding="utf-8")))) if p.exists() else None

def verify_a(ws: Path, key: dict) -> dict:
    got = _read_csv(ws / "cleaned.csv"); checks = []
    if got is None:
        checks.append(("cleaned_present", False, "cleaned.csv missing")); return result(False, 0.0, checks, "not_attempted")
    want = key["a_expected"]
    norm = lambda rows: [{k: (v or "").strip() for k, v in x.items()} for x in rows]
    ok = norm(got) == norm(want)
    checks.append(("cleaned_matches_convention", ok, f"convention {key['convention']}"))
    return result(ok, 1.0 if ok else 0.0, checks, None if ok else f"convention_{key['convention']}")

def verify_b(ws: Path, key: dict) -> dict:
    got = read_json(ws / "totals.json"); checks = []
    if got is None or got == "INVALID_JSON" or not isinstance(got, dict):
        checks.append(("totals_present", False, "totals.json missing or invalid")); return result(False, 0.0, checks, "not_attempted")
    want = key["b_expected"]
    pid = [{"id": str(x.get("id")), "amount": str(x.get("amount"))} for x in got.get("per_id", [])] == want["per_id"]
    pm_got = {k: round(float(v), 2) for k, v in got.get("per_month", {}).items()} if isinstance(got.get("per_month"), dict) else None
    pm = pm_got == want["per_month"]
    checks += [("per_id_under_convention", pid, f"convention {key['convention']}"), ("per_month_under_convention", pm, "")]
    passed = pid and pm
    default_hit = (got.get("per_id") == key["b_default"]["per_id"])
    mode = None if passed else ("default_reading_no_transfer" if default_hit else "other")
    return result(passed, (pid + pm) / 2, checks, mode)

def reference_solve_a(ws: Path, conv: str) -> None:
    rows = _read_csv(ws / "raw.csv"); (ws / "cleaned.csv").write_text(_csv(_apply(rows, conv)), encoding="utf-8")

def reference_solve_b(ws: Path, conv) -> None:
    rows = _read_csv(ws / "ledger.csv"); (ws / "totals.json").write_text(json.dumps(_totals(rows, conv)), encoding="utf-8")

def lesson_from_feedback(ws: Path):
    """What a pair that read FEEDBACK.md would carry: the convention named in it."""
    p = ws / "FEEDBACK.md"
    if not p.exists(): return None
    t = p.read_text(encoding="utf-8")
    return next((c for c in CONVENTIONS if LESSON[c] in t), None)

def spec_key_check(seed: int) -> None:
    fa, fb, key = generate_pair(seed)
    assert key["b_expected"] != key["b_default"], "trap did not fire: default reading equals the convention on B"
    assert key["a_expected"] != _apply(list(csv.DictReader(io.StringIO(fa["raw.csv"]))), None), "trap did not fire on A"
    assert key["lesson"] == LESSON[key["convention"]]
    assert "FEEDBACK.md" in fa["GOAL.md"] and key["convention"] not in fb["GOAL.md"]
    assert LESSON[key["convention"]] not in fb["GOAL.md"], "episode B must not state the lesson"
