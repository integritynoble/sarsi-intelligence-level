"""Reference harnesses HG0/HG1/HG2 over any executor, with PUBLIC checks per family.

A public check is a criterion derivable from the visible specification alone (never from the key); it is
the harness's own acceptance step. HG0: one attempt, no acceptance. HG1: one attempt; the public checks
run in the harness and a failing deliverable is HELD BACK (not delivered). HG2: snapshot before each
attempt, restore on rejection, up to three attempts with the failed public check named.
The hidden verifier is applied afterwards to what was DELIVERED; the four outcomes follow.
"""
from __future__ import annotations
import csv, io, json, re, shutil
from pathlib import Path
from .common import run_exec, read_json, norm, TASK

def _lines(p): return p.read_text(encoding="utf-8").splitlines() if p.exists() else []

def public_checks(fam: str, ws: Path, files: dict) -> list:
    """Returns [(name, ok, detail)] using only what the executor could see."""
    g = files.get("GOAL.md", "")
    if fam == "code_t0":
        m = re.search(r"set `(\w+)` from `(\d+)` to `(\d+)`", g); sym, old, new = m.group(1), m.group(2), m.group(3)
        other_same = all((ws / f).read_text(encoding="utf-8") == files[f] for f in files if f != "config.py")
        diff = sum(1 for a, b in zip(files["config.py"].splitlines(), _lines(ws / "config.py")) if a != b)
        return [("other_files_untouched", other_same, ""), ("one_line_changed", diff == 1, f"{diff}"),
                ("named_line_set", any(l.strip() == f"{sym} = {new}" for l in _lines(ws / "config.py")), "")]
    if fam == "funding_t0":
        a = read_json(ws / "answer.json"); field = re.search(r"\*\*(\w+)\*\*", g).group(1)
        ok = isinstance(a, dict) and a.get("field") == field and bool(a.get("value"))
        src = files["solicitation.txt"]; verb = ok and (norm(a["value"]).rstrip(".") in norm(src) or (str(a["value"]).isdigit()))
        return [("shape_and_field", ok, ""), ("value_from_source", bool(verb), "")]
    if fam == "job_t0":
        a = read_json(ws / "requirements.json"); ok = isinstance(a, dict) and isinstance(a.get("required"), list) and a.get("required")
        post = files["posting.txt"]; allin = ok and all(isinstance(x, str) and norm(x) in norm(post) for x in a["required"])
        flags = ok and isinstance(a.get("work_authorization_required"), bool) and isinstance(a.get("clearance_required"), bool)
        return [("shape", bool(ok), ""), ("bullets_in_posting", bool(allin), ""), ("flags_boolean", bool(flags), "")]
    if fam == "paper_t0":
        a = read_json(ws / "citation_check.json"); k = int(re.search(r"\[(\d+)\]", g).group(1))
        ok = isinstance(a, dict) and a.get("citation") == k and isinstance(a.get("discrepancies"), list) and isinstance(a.get("consistent"), bool)
        cons = ok and (a["consistent"] == (len(a["discrepancies"]) == 0))
        fields = ok and all(x in ("author", "year", "venue", "pages") for x in a["discrepancies"])
        return [("shape_and_citation", bool(ok), ""), ("consistent_matches_list", bool(cons), ""), ("known_fields", bool(fields), "")]
    if fam == "business_t0":
        a = read_json(ws / "fact.json"); fact = re.search(r"\*\*(\w+)\*\*", g).group(1)
        ok = isinstance(a, dict) and a.get("fact") == fact and str(a.get("value", "")).isdigit()
        src = files["company_brief.txt"]; line = ok and norm(a.get("source_line", "")) in norm(src) and str(a["value"]) in str(a.get("source_line", ""))
        return [("shape_and_fact", bool(ok), ""), ("source_line_verbatim", bool(line), "")]
    if fam == "paper_t1":
        p = ws / "results_section.md"; txt = p.read_text(encoding="utf-8") if p.exists() else ""
        ev = json.loads(files["evidence.json"]); ds = re.search(r"\*\*(\w+)\*\*", files["outline.md"]).group(1)
        nums = [float(x) for x in re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])", txt)]
        allowed = {round(v, 3) for d in ev["results"].values() for v in d.values()}
        vals = ev["results"][ds]; hi = "higher" in ev["direction"]; s = sorted(vals.values(), reverse=hi); margin = round(abs(s[0] - s[1]), 3 if not hi else 2)
        allowed.add(round(margin, 3))
        return [("present", bool(txt), ""), ("dataset_named", ds.lower() in txt.lower(), ""), ("table_named", ev["table"].lower() in txt.lower(), ""),
                ("no_number_outside_evidence", all(round(n, 3) in allowed for n in nums), "")]
    if fam.startswith("hc_"):
        return _hard_public_checks(fam, ws, files)
    return []

def _hard_public_checks(fam: str, ws: Path, files: dict) -> list:
    """Core-H checks. Each is stated in GOAL.md and computable without the key; what stays hidden is the
    part that needs the reasoning -- whether the predictions are right, whether the plan is optimal,
    whether blocking was the correct call, and which of two candidate lines the answer had to come from."""
    from .common import read_json, norm
    if fam == "hc_rule":
        p = read_json(ws / "predictions.json"); at = json.loads(files["predict_at.json"])
        m = (ws / "mechanism.txt").read_text(encoding="utf-8", errors="replace") if (ws / "mechanism.txt").exists() else ""
        shape = isinstance(p, dict) and all(str(x) in {str(k) for k in p} for x in at)
        ints = shape and all(isinstance(p.get(str(x), p.get(x)), int) for x in at)
        return [("predictions_for_every_x", bool(shape), ""), ("predictions_integer", bool(ints), ""),
                ("mechanism_states_switch_and_period", bool(re.search(r"switch:\s*-?\d+", m) and re.search(r"period:\s*\d+", m)), "")]
    if fam == "hc_sched":
        a = read_json(ws / "plan.json"); g = files["GOAL.md"]
        costs = {m.group(1): int(m.group(2)) for m in re.finditer(r"`(\w+)`: cost (\d+)", g)}
        n = int(re.search(r"exactly (\d+) of these", g).group(1))
        bef = re.search(r"If both `(\w+)` and `(\w+)` are in the plan, `\1` must come before", g)
        apart = re.search(r"If both `(\w+)` and `(\w+)` are in the plan, they must be at least two", g)
        excl = re.search(r"`(\w+)` and `(\w+)` must never both be in the plan", g)
        ok = isinstance(a, dict) and isinstance(a.get("plan"), list) and len(a["plan"]) == n and len(set(a["plan"])) == n and all(t in costs for t in a["plan"])
        pl = a["plan"] if ok else []
        c1 = ok and not (bef.group(1) in pl and bef.group(2) in pl and pl.index(bef.group(1)) > pl.index(bef.group(2)))
        c2 = ok and not (apart.group(1) in pl and apart.group(2) in pl and abs(pl.index(apart.group(1)) - pl.index(apart.group(2))) < 2)
        c3 = ok and not (excl.group(1) in pl and excl.group(2) in pl)
        c4 = ok and str(a.get("total")) == str(sum(costs[t] for t in pl))
        return [("shape", bool(ok), ""), ("order_constraint", bool(c1), ""), ("separation_constraint", bool(c2), ""),
                ("exclusion_constraint", bool(c3), ""), ("total_matches_plan", bool(c4), "")]
    if fam == "hc_contra":
        out = (ws / "out.json").exists(); bl = read_json(ws / "blocked.json")
        one = out != bool(isinstance(bl, dict))
        named = (not isinstance(bl, dict)) or bool(bl.get("conflict"))
        return [("exactly_one_deliverable", bool(one), "out.json xor blocked.json"), ("conflict_clauses_named_if_blocked", bool(named), "")]
    if fam == "hc_decoy":
        a = read_json(ws / "answer.json"); src = files["solicitation.txt"]
        y = int(re.search(r"the (\d{4}) cycle", files["GOAL.md"]).group(1))
        ok = isinstance(a, dict) and str(a.get("cycle")) == str(y) and bool(str(a.get("maximum_award", "")).strip())
        inf = ok and str(a["maximum_award"]).strip() in src
        ln = ok and norm(a.get("source_line", "")) in norm(src) and bool(norm(a.get("source_line", "")))
        return [("shape_and_cycle", bool(ok), ""), ("amount_occurs_in_file", bool(inf), ""), ("source_line_is_a_line_of_the_file", bool(ln), "")]
    return []

def run_rung(rung: str, fam: str, files: dict, ws: Path, exec_tmpl: str, limit: int, env=None) -> dict:
    """Runs the executor under the rung's mechanism; returns attempts, delivered flag, held_back flag, checks."""
    from .common import write_workspace
    write_workspace(ws, files); attempts = []; delivered = True; held = False
    if rung == "HG0":
        attempts.append(run_exec(exec_tmpl, TASK, ws, limit, env)); return {"attempts": attempts, "delivered": True, "held_back": False, "public": None}
    max_att = 1 if rung == "HG1" else 3
    snap = ws.parent / (ws.name + "_snap")
    for i in range(max_att):
        if rung == "HG2":
            shutil.rmtree(snap, ignore_errors=True); shutil.copytree(ws, snap)
        prompt = TASK if i == 0 else (f"CORRECTION.md in this directory names the acceptance check your delivery failed. Read GOAL.md again, correct your delivery, and reply DONE.")
        attempts.append(run_exec(exec_tmpl, prompt, ws, limit, env))
        pc = public_checks(fam, ws, files); failed = [n for n, ok, _ in pc if not ok]
        if not failed: return {"attempts": attempts, "delivered": True, "held_back": False, "public": pc}
        if rung == "HG2" and i < max_att - 1:
            shutil.rmtree(ws); shutil.copytree(snap, ws)
            (ws / "CORRECTION.md").write_text("Your delivery failed the acceptance check named: " + ", ".join(failed) + ".\n")
    # rejected on the last attempt: held back, nothing delivered
    shutil.rmtree(snap, ignore_errors=True)
    return {"attempts": attempts, "delivered": False, "held_back": True, "public": pc}
