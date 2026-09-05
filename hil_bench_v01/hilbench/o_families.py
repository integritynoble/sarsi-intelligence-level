"""Organizational coordinate O, bound core O0 and O1.

O0 -- coordination/routing. A compound task is routed across three separated roles (planner,
executor, verifier) by a harness-held dispatch record; the deliverable is an execution record with
per-role evidence and an explicit verification entry. Anti-rubber-stamp check: the verifier's
entry must state, with the correct computed figure, what was checked --- 'looks fine' scores zero.

O1 -- persistent organizational memory. Episode A: the organization makes a standing routing
decision and the harness records it in the organization's decision log (harness-held, never the
model's). -- restart, episode A's workspace removed --. Episode B: a different instance of the
same task type; the standing decision (a convention it fixes) decides the answer. The floor is
the ablated arm whose decision log was withheld. The default reading fails B on every seed by
construction (asserted per instance by the spec-key test).

Both are single-episode LLM tasks with computed keys, a reference solver, the plausible wrong
method, and a specification-key test.
"""
from __future__ import annotations
import csv, io, json
from .common import rng, read_json, result

FAM_O0 = "o0_routing"
FAM_O1 = "o1_orgmem"

ROLES = ["planner", "executor", "verifier"]

# ---------------- O0 ----------------

def o0_generate(seed: int):
    r = rng(seed, FAM_O0)
    n = r.randint(5, 8)
    rows = [{"id": f"R{r.randint(10, 99)}-{i}", "amount": str(r.randint(10, 99999)), "region": r.choice(["north", "south", "east", "west"])} for i in range(n)]
    kept = [x for x in rows if int(x["amount"]) >= 1000]
    total = sum(int(x["amount"]) for x in kept)
    by_region = {}
    for x in kept:
        by_region[x["region"]] = by_region.get(x["region"], 0) + int(x["amount"])
    top_region = max(by_region.items(), key=lambda kv: (kv[1], kv[0]))[0]
    data = "id,amount,region\n" + "".join(f"{x['id']},{x['amount']},{x['region']}\n" for x in rows)
    org = "\n".join([
        "# ORGANIZATION CHARTER", "",
        "This organization runs work through three separated roles. A task is complete only when",
        "the organization's execution record shows the work routed across them with the evidence.", "",
        "- planner: decomposes the task and assigns the sub-tasks to roles",
        "- executor: performs the computation and produces the working figures",
        "- verifier: checks the executor's figures against the data and signs off; its entry must",
        "  name what it checked and the figure it verified", "",
        "Disclosed rule: rows with amount below 1000 are out of scope and excluded. Nothing else",
        "is excluded. The acceptance record is held by the organization and is hidden.", "",
    ])
    goal = "\n".join([
        "# GOAL (O0: routing)", "",
        "Complete the task `regional_total` with the three roles above and write `org_record.json` as",
        '`{"plan": [{"role": "<role>", "task": "<sub-task>"} in dispatch order],',
        ' "execution": {"kept_rows": <count of in-scope rows>, "grand_total": <sum>, "top_region": "<region>"},',
        ' "verification": {"checked": ["<what the verifier checked>", ...], "verified_total": <figure verified against the data>, "sign_off": true}}`.', "",
        "The verifier must have checked the figure against the data and stated it; a sign-off that",
        "states nothing it checked is not a sign-off.", "",
    ])
    files = {"GOAL.md": goal, "ORG.md": org, "data.csv": data}
    key = {"family": FAM_O0, "seed": seed, "kept_rows": len(kept), "grand_total": total, "top_region": top_region,
           "naive_name": "rubber-stamp verification (no checked figure)", "naive_total": total + 777}
    return files, key

def o0_verify(ws: Path, key: dict) -> dict:
    rec = read_json(ws / "org_record.json")
    if rec is None or rec == "INVALID_JSON" or not isinstance(rec, dict):
        return result(False, 0.0, [("org_record_present", False, "org_record.json missing")], "not_attempted")
    plan = rec.get("plan")
    ok_plan = isinstance(plan, list) and [p.get("role") for p in plan if isinstance(p, dict)] == ROLES
    ex = rec.get("execution") if isinstance(rec.get("execution"), dict) else {}
    ok_ex = ex.get("kept_rows") == key["kept_rows"] and str(ex.get("grand_total")) == str(key["grand_total"]) and str(ex.get("top_region")) == key["top_region"]
    vr = rec.get("verification") if isinstance(rec.get("verification"), dict) else {}
    ok_vr = (isinstance(vr.get("checked"), list) and len(vr.get("checked")) >= 1
             and str(vr.get("verified_total")) == str(key["grand_total"])
             and vr.get("sign_off") is True)
    checks = [("routing_plan_exact_roles_in_order", ok_plan, "planner -> executor -> verifier"),
              ("execution_correct", ok_ex, f"expected {key['kept_rows']} rows, total {key['grand_total']}, top {key['top_region']}"),
              ("verification_substantive", ok_vr, "checked list non-empty, verified_total correct, sign_off true")]
    passed = ok_plan and ok_ex and ok_vr
    mode = None if passed else ("rubber_stamp" if not ok_vr else ("wrong_routing" if not ok_plan else "wrong_computation"))
    return result(passed, sum(1 for _, ok, _ in checks if ok) / len(checks), checks, mode)

def o0_reference(ws: Path, key: dict) -> None:
    import csv, io
    rows = list(csv.DictReader(io.StringIO((ws / "data.csv").read_text())))
    kept = [x for x in rows if int(x["amount"]) >= 1000]
    total = sum(int(x["amount"]) for x in kept)
    by = {}
    for x in kept:
        by[x["region"]] = by.get(x["region"], 0) + int(x["amount"])
    rec = {"plan": [{"role": r, "task": t} for r, t in zip(ROLES, ["decompose and assign", "kept rows, totals, top region", "check figures vs data"])],
           "execution": {"kept_rows": len(kept), "grand_total": total, "top_region": max(by.items(), key=lambda kv: (kv[1], kv[0]))[0]},
           "verification": {"checked": ["kept_rows count vs data.csv", "grand_total vs data.csv", "top_region vs data.csv"],
                            "verified_total": total, "sign_off": True}}
    (ws / "org_record.json").write_text(json.dumps(rec, indent=1), encoding="utf-8")

def o0_naive(ws: Path, key: dict) -> None:
    o0_reference(ws, key)
    rec = json.loads((ws / "org_record.json").read_text())
    rec["verification"] = {"checked": [], "verified_total": key["naive_total"], "sign_off": True}
    (ws / "org_record.json").write_text(json.dumps(rec, indent=1), encoding="utf-8")

def o0_spec_key(seed: int) -> None:
    files, key = o0_generate(seed)
    assert key["kept_rows"] >= 1 and key["grand_total"] > 0
    assert "below 1000" in files["GOAL.md"] or "below 1000" in files["ORG.md"]
    import tempfile, shutil
    d = __import__("pathlib").Path(tempfile.mkdtemp())
    from .common import write_workspace
    write_workspace(d, files); o0_reference(d, key); assert o0_verify(d, key)["pass"], "reference fails"
    o0_naive(d, key); assert not o0_verify(d, key)["pass"], "rubber-stamp trap did not fire"
    shutil.rmtree(d)

# ---------------- O1 ----------------

# Each rule must be able to change the answer, and the generator regenerates the instance until it does on BOTH
# episodes (asserted per seed by o1_spec_key). The first version had a rule naming the alphabetical order, which
# could never fire, and amounts that were multiples of 100, so rounding could never fire either.
O1_RULES = ["the top region is the region with the most in-scope rows (a row count, not a total); ties alphabetical",
            "amounts below 5000 are out of scope in the totals report (threshold 5000, not 1000)",
            "the top region is the one with the highest in-scope total after rounding each amount to the nearest 100"]

def o1_generate_pair(seed: int):
    r = rng(seed, FAM_O1)
    rule = O1_RULES[seed % len(O1_RULES)] if seed < 100 else r.choice(O1_RULES)
    def instance(n):
        return [{"id": f"R{r.randint(10, 99)}-{i}", "amount": str(r.choice([800, 4900, 7500, 12000, 30000]) + r.randint(1, 99)),
                 "region": r.choice(["north", "south", "east", "west"])} for i in range(n)]
    def answer(rows):
        kept = [x for x in rows if int(x["amount"]) >= (5000 if "5000" in rule else 1000)]
        by, cnt = {}, {}
        for x in kept:
            v = int(x["amount"])
            if "nearest 100" in rule: v = round(v / 100) * 100
            by[x["region"]] = by.get(x["region"], 0) + v; cnt[x["region"]] = cnt.get(x["region"], 0) + 1
        if "most in-scope rows" in rule: top = min(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[0] if cnt else None
        else: top = max(by.items(), key=lambda kv: (kv[1], kv[0]))[0] if by else None
        return len(kept), sum(by.values()), top
    def default_answer(rows):
        kept = [x for x in rows if int(x["amount"]) >= 1000]; by = {}
        for x in kept: by[x["region"]] = by.get(x["region"], 0) + int(x["amount"])
        return len(kept), sum(by.values()), (max(by.items(), key=lambda kv: (kv[1], kv[0]))[0] if by else None)
    for _ in range(500):                       # the standing decision must change the answer in both episodes
        rows_a, rows_b = instance(6), instance(7)
        if answer(rows_a) != default_answer(rows_a) and answer(rows_b) != default_answer(rows_b): break
    else:
        raise RuntimeError(f"o1: no discriminating instance for seed {seed}")
    k_a, t_a, top_a = answer(rows_a); k_b, t_b, top_b = answer(rows_b)
    data = lambda rows: "id,amount,region\n" + "".join(f"{x['id']},{x['amount']},{x['region']}\n" for x in rows)
    baseline = ("\n".join([
        "Baseline report convention (disclosed; applies UNLESS this organization has recorded a standing",
        "decision in its decision log that overrides it):",
        "- in scope: amount >= 1000;",
        "- top region: highest in-scope total, ties broken alphabetically.",
        "Exactly one item may be overridden by a standing decision of this organization. Nothing in this",
        "file states which, if any."]))
    files_a = {"GOAL.md": "\n".join([
        "# GOAL (episode A, O1)", "",
        "Report `regional_total` on `data.csv` and write `report.json` as",
        '`{"kept_rows": <int>, "grand_total": <int>, "top_region": "<region or null>"}`.', "",
        "This organization has a STANDING DECISION for this task family, recorded in its decision log at",
        "`../DECISION_LOG.md` (held by the organization, outside this episode's directory). It overrides the",
        "baseline convention below on exactly one item. Apply it to this report.", "",
        "After you are done, restate it in `standing_decision.json` as",
        '`{"decision": "<the standing decision, in your own words>", "scope": "this task family"}`.', "",
        *split_para(baseline)]), "data.csv": data(rows_a)}
    files_b = {"GOAL.md": "\n".join([
        "# GOAL (episode B, O1)", "",
        "Report `regional_total` on `data.csv` and write `report.json` as",
        '`{"kept_rows": <int>, "grand_total": <int>, "top_region": "<region or null>"}`.', "",
        "If this organization has recorded a standing decision for this task family in its decision log",
        "(`../DECISION_LOG.md`, if present), it overrides the baseline convention below; if there is no",
        "such record, apply the baseline exactly and do not invent a decision.", "",
        *split_para(baseline)]), "data.csv": data(rows_b)}
    def report(rows):
        k, t, top = answer(rows)
        return {"kept_rows": k, "grand_total": t, "top_region": top}
    def default_report(rows):
        kept = [x for x in rows if int(x["amount"]) >= 1000]
        by = {}
        for x in kept:
            by[x["region"]] = by.get(x["region"], 0) + int(x["amount"])
        top = max(by.items(), key=lambda kv: (kv[1], kv[0]))[0] if by else None
        return {"kept_rows": len(kept), "grand_total": sum(by.values()), "top_region": top}
    key = {"family": FAM_O1, "seed": seed, "rule": rule, "a": report(rows_a), "b": report(rows_b),
           "b_default": default_report(rows_b),
           "decision_norm": "5000" if "5000" in rule else ("nearest 100" if "nearest 100" in rule else "row count")}
    key["decision_token"] = "5000" if "5000" in rule else ("100" if "nearest 100" in rule else "count")
    key["decision_log"] = ("# DECISION LOG (held by the organization)\n\n"
                           f"- {r.choice(['2026-03-04','2026-05-19','2026-07-02'])} standing decision, task family `regional_total`: {rule}.\n")
    return files_a, files_b, key

def split_para(t):
    return [t]

def o1_rule_match(decision: str, token: str) -> bool:
    import re
    d = (decision or "").lower()
    if token == "5000":
        return bool(re.search(r"\b5,?000\b", d))
    if token == "100":
        return bool(re.search(r"nearest 100|round(ed|ing)? (to )?(the )?(nearest )?100", d))
    return bool(re.search(r"row count|count of (in-scope )?rows|number of (in-scope )?rows|most (in-scope )?rows|by count", d))

def o1_verify_a(ws: Path, key: dict) -> dict:
    rep = read_json(ws / "report.json")
    ok = isinstance(rep, dict) and rep.get("kept_rows") == key["a"]["kept_rows"] and str(rep.get("grand_total")) == str(key["a"]["grand_total"]) and rep.get("top_region") == key["a"]["top_region"]
    dec = read_json(ws / "standing_decision.json")
    ok2 = isinstance(dec, dict) and o1_rule_match(str(dec.get("decision", "")), key["decision_token"])
    checks = [("report_correct_under_convention", bool(ok), ""), ("standing_decision_stated", bool(ok2), "states the organization's convention")]
    return result(bool(ok and ok2), (ok + bool(ok2)) / 2, checks, None if ok and ok2 else "no_decision_or_wrong_report")

def o1_verify_b(ws: Path, key: dict) -> dict:
    rep = read_json(ws / "report.json")
    if rep is None or rep == "INVALID_JSON" or not isinstance(rep, dict):
        return result(False, 0.0, [("report_present", False, "report.json missing")], "not_attempted")
    ok = rep.get("kept_rows") == key["b"]["kept_rows"] and str(rep.get("grand_total")) == str(key["b"]["grand_total"]) and rep.get("top_region") == key["b"]["top_region"]
    mode = None if ok else ("default_reading_no_org_memory" if (rep == key["b_default"]) else "other")
    return result(bool(ok), 1.0 if ok else 0.0, [("report_under_standing_decision", bool(ok), f"token {key['decision_token']}")], mode)

def o1_reference_a(ws: Path, key: dict) -> None:
    (ws / "report.json").write_text(json.dumps(key["a"]), encoding="utf-8")
    (ws / "standing_decision.json").write_text(json.dumps({"decision": key["rule"], "scope": "regional_total"}), encoding="utf-8")

def o1_reference_b(ws: Path, key: dict) -> None:
    (ws / "report.json").write_text(json.dumps(key["b"]), encoding="utf-8")

def o1_default_b(ws: Path, key: dict) -> None:
    (ws / "report.json").write_text(json.dumps(key["b_default"]), encoding="utf-8")

def o1_spec_key(seed: int) -> None:
    fa, fb, key = o1_generate_pair(seed)
    assert key["b"] != key["b_default"], "trap did not fire: standing decision does not change B's answer"
    import tempfile, shutil
    from pathlib import Path
    from .common import write_workspace
    d = Path(tempfile.mkdtemp()); write_workspace(d, fb); o1_default_b(d, key); assert not o1_verify_b(d, key)["pass"], "default reading must fail B"
    o1_reference_b(d, key); assert o1_verify_b(d, key)["pass"], "reference must pass B"
    shutil.rmtree(d)

# ---------------- registry ----------------

O_FAMILIES = {"o0_routing": (o0_generate, o0_verify), "o1_orgmem": (o1_generate_pair, None)}
