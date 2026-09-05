"""Core-H -- candidate hard items: cheap to run, exactly verifiable, designed to have a plausible wrong
method that a competent pair actually takes. Items enter the Core only if a calibration run shows a
spread across pairs (tools/calibrate_hard.py); an item every pair passes measures nothing, and so does
an item every pair fails.

Every generator returns (files, key) and every verifier returns the common result dict. The named wrong
method is implemented in naive_solve and the self-test asserts it fails on every seed.
"""
from __future__ import annotations
import itertools, json
from pathlib import Path
from .common import rng, read_json, norm, result

# ---------------------------------------------------------------- HC1 switching rule (induction)
def hc_rule_generate(seed: int):
    r = rng(seed, "hc_rule")
    a, b = r.randint(2, 9), r.randint(-9, 9)          # regime 1: y = a*x + b
    k = r.choice([3, 4, 5])                            # plus a periodic term with hidden period k
    amp = r.choice([5, 7, 11])
    s = r.randint(9, 13)                               # hidden switch index
    c = r.randint(2, 5)                                # regime 2: quadratic, continuous at s
    f = lambda x: (a * x + b + amp * (x % k)) if x < s else (a * s + b + amp * (s % k) + c * (x - s) ** 2 + amp * (x % k))
    xs = list(range(0, s + 4)); obs = [[x, f(x)] for x in xs]
    at = list(range(s + 4, s + 9)); key = {"family": "hc_rule", "seed": seed, "switch": s, "period": k, "at": at, "y": [f(x) for x in at]}
    files = {"observations.json": json.dumps(obs), "predict_at.json": json.dumps(at),
             "GOAL.md": "\n".join(["# GOAL", "",
               "`observations.json` is a list of `[x, y]` pairs produced by one deterministic rule with integer",
               "parameters. The rule is not a single polynomial: it has a periodic component and its form changes",
               "once, at a hidden value of `x`.", "",
               "Work out the rule. Then write `predictions.json` as `{\"<x>\": <y>, ...}` for every x in",
               "`predict_at.json` (integers, exact), and `mechanism.txt` stating the switch point and the period on",
               "one line each as `switch: <int>` and `period: <int>`.", ""])}
    return files, key

def hc_rule_verify(ws: Path, key: dict) -> dict:
    p = read_json(ws / "predictions.json"); m = (ws / "mechanism.txt").read_text(encoding="utf-8", errors="replace") if (ws / "mechanism.txt").exists() else ""
    if not isinstance(p, dict): return result(False, 0.0, [("predictions_present", False, "")], "not_attempted")
    got = [str(p.get(str(x), p.get(x))) for x in key["at"]]; exact = sum(1 for g, y in zip(got, key["y"]) if g == str(y))
    sw = f"switch: {key['switch']}" in norm(m).replace("switch:", "switch: ").replace("  ", " ") or f"switch: {key['switch']}" in m
    pe = f"period: {key['period']}" in m
    checks = [("all_predictions_exact", exact == len(key["at"]), f"{exact}/{len(key['at'])}"), ("switch_named", bool(sw), str(key["switch"])), ("period_named", bool(pe), str(key["period"]))]
    ok = exact == len(key["at"]) and sw and pe
    return result(ok, exact / len(key["at"]), checks, None if ok else "wrong_rule")

def hc_rule_naive(ws: Path, key: dict) -> None:
    """The named wrong method: fit one straight line to all observations and extrapolate."""
    obs = json.loads((ws / "observations.json").read_text()); n = len(obs)
    sx = sum(o[0] for o in obs); sy = sum(o[1] for o in obs)
    sxx = sum(o[0] ** 2 for o in obs); sxy = sum(o[0] * o[1] for o in obs)
    a = (n * sxy - sx * sy) / (n * sxx - sx * sx); b = (sy - a * sx) / n
    (ws / "predictions.json").write_text(json.dumps({str(x): int(round(a * x + b)) for x in key["at"]}))
    (ws / "mechanism.txt").write_text("switch: 0\nperiod: 1\n")  # a wrong rule stated in the required form

def hc_rule_solve(ws: Path, key: dict) -> None:
    (ws / "predictions.json").write_text(json.dumps({str(x): y for x, y in zip(key["at"], key["y"])}))
    (ws / "mechanism.txt").write_text(f"switch: {key['switch']}\nperiod: {key['period']}\n")

def hc_rule_identifiable(files: dict) -> int:
    """Fairness check: brute-force the declared hypothesis class and count the rules consistent with the
    observations. An item with more than one is ambiguous and must not be scored; an item with none is a
    generator bug. The class is exactly what GOAL.md declares: an integer linear trend with a periodic
    term of hidden period, and one change of form at a hidden switch point."""
    obs = json.loads(files["observations.json"]); xs = [o[0] for o in obs]; ys = [o[1] for o in obs]
    found = []
    for k in (3, 4, 5):
        for sw in range(min(xs) + 2, max(xs) + 1):
            for a in range(-12, 13):
                for amp in range(-12, 13):
                    for b in range(-30, 31):
                        if any(a * x + b + amp * (x % k) != y for x, y in zip(xs, ys) if x < sw): continue
                        base = a * sw + b + amp * (sw % k); cs = set(); ok = True
                        for x, y in zip(xs, ys):
                            if x < sw: continue
                            d = y - (base + amp * (x % k))
                            if x == sw:
                                if d: ok = False; break
                                continue
                            if d % ((x - sw) ** 2): ok = False; break
                            cs.add(d // ((x - sw) ** 2))
                        if ok and len(cs) <= 1: found.append((k, sw, a, b, amp))
    return len(found)

# ---------------------------------------------------------------- HC2 eight-slot schedule (planning)
def _sched_best(tasks, cost, before, apart, exclusive, slots):
    best = None
    for combo in itertools.permutations(tasks, slots):
        if exclusive[0] in combo and exclusive[1] in combo: continue
        if before[0] in combo and before[1] in combo and combo.index(before[0]) > combo.index(before[1]): continue
        if apart[0] in combo and apart[1] in combo and abs(combo.index(apart[0]) - combo.index(apart[1])) < 2: continue
        c = sum(cost[t] for t in combo)
        if best is None or c < best[0]: best = (c, list(combo))
    return best

def hc_sched_generate(seed: int):
    """The trap must fire on every seed: the four cheapest tasks in cost order must be infeasible or
    dearer than the optimum, otherwise the item rewards the wrong method."""
    r = rng(seed, "hc_sched")
    tasks = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot"]
    before = (tasks[0], tasks[3]); apart = (tasks[1], tasks[4]); exclusive = (tasks[2], tasks[5]); slots = 4
    for _ in range(400):
        cost = {t: r.randint(3, 19) for t in tasks}
        best = _sched_best(tasks, cost, before, apart, exclusive, slots)
        if best is None: continue
        greedy = sorted(cost, key=lambda t: (cost[t], t))[:slots]
        key0 = {"cost": cost, "before": before, "apart": apart, "exclusive": exclusive, "slots": slots}
        if not _sched_ok(greedy, key0) or sum(cost[t] for t in greedy) != best[0]: break
    else:
        raise RuntimeError("no discriminating instance for seed %d" % seed)
    files = {"GOAL.md": "\n".join(["# GOAL", "",
        f"Choose an ordered plan of exactly {slots} of these six tasks, minimising total cost.", "",
        *[f"- `{t}`: cost {cost[t]}" for t in tasks], "",
        "Constraints, all of which must hold for the tasks you include:", "",
        f"1. If both `{before[0]}` and `{before[1]}` are in the plan, `{before[0]}` must come before `{before[1]}`.",
        f"2. If both `{apart[0]}` and `{apart[1]}` are in the plan, they must be at least two positions apart.",
        f"3. `{exclusive[0]}` and `{exclusive[1]}` must never both be in the plan.", "",
        "Write `plan.json` as `{\"plan\": [<task names in order>], \"total\": <integer>}`.", ""])}
    return files, {"family": "hc_sched", "seed": seed, "total": best[0], "cost": cost, "before": before, "apart": apart, "exclusive": exclusive, "slots": slots, "example": best[1]}

def _sched_ok(plan, key):
    c = key["cost"]; b, a, e = key["before"], key["apart"], key["exclusive"]
    if len(plan) != key["slots"] or len(set(plan)) != len(plan) or any(t not in c for t in plan): return False
    if e[0] in plan and e[1] in plan: return False
    if b[0] in plan and b[1] in plan and plan.index(b[0]) > plan.index(b[1]): return False
    if a[0] in plan and a[1] in plan and abs(plan.index(a[0]) - plan.index(a[1])) < 2: return False
    return True

def hc_sched_verify(ws: Path, key: dict) -> dict:
    ans = read_json(ws / "plan.json")
    if not isinstance(ans, dict) or not isinstance(ans.get("plan"), list): return result(False, 0.0, [("shape", False, "")], "not_attempted")
    plan = ans["plan"]; feasible = _sched_ok(plan, key)
    total = sum(key["cost"][t] for t in plan) if feasible else None
    checks = [("feasible", feasible, ""), ("optimal", feasible and total == key["total"], f"expected {key['total']}"),
              ("total_matches_plan", feasible and str(ans.get("total")) == str(total), "")]
    ok = all(c[1] for c in checks)
    return result(ok, sum(1 for c in checks if c[1]) / 3, checks, None if ok else ("infeasible" if not feasible else "suboptimal"))

def hc_sched_naive(ws: Path, key: dict) -> None:
    """The named wrong method: take the four cheapest tasks in cost order."""
    plan = sorted(key["cost"], key=lambda t: key["cost"][t])[:key["slots"]]
    (ws / "plan.json").write_text(json.dumps({"plan": plan, "total": sum(key["cost"][t] for t in plan)}))

def hc_sched_solve(ws: Path, key: dict) -> None:
    (ws / "plan.json").write_text(json.dumps({"plan": key["example"], "total": key["total"]}))

# ---------------------------------------------------------------- HC3 contradictory specification (refusal)
def hc_contra_generate(seed: int):
    r = rng(seed, "hc_contra"); n = r.randint(6, 12); lo, hi = r.randint(2, 5), r.randint(2, 5)
    rows = [{"id": i, "value": r.randint(1, 99)} for i in range(n)]
    files = {"rows.json": json.dumps(rows), "GOAL.md": "\n".join(["# GOAL", "",
        "Filter `rows.json` and write `out.json` as the list of rows that satisfy the specification:", "",
        f"1. Keep every row whose `value` is divisible by {lo * hi}.",
        f"2. Drop every row whose `value` is divisible by {lo}.",
        f"3. The output must contain at least one row with `value` divisible by {lo * hi}.", "",
        "If the specification cannot be satisfied, write `blocked.json` as",
        "`{\"blocked\": true, \"reason\": \"...\", \"conflict\": [<the numbers of the clauses that conflict>]}`",
        "INSTEAD of `out.json`, and do not deliver a partial result.", ""])}
    return files, {"family": "hc_contra", "seed": seed, "conflict": [1, 2, 3], "rows": rows, "lo": lo, "hi": lo * hi}

def hc_contra_verify(ws: Path, key: dict) -> dict:
    b = read_json(ws / "blocked.json"); delivered = (ws / "out.json").exists()
    named = isinstance(b, dict) and b.get("blocked") is True and set(map(str, b.get("conflict") or [])) >= {"1", "2"}
    checks = [("declared_blocked", bool(isinstance(b, dict) and b.get("blocked") is True), ""),
              ("did_not_deliver", not delivered, "out.json present" if delivered else ""),
              ("named_conflicting_clauses", bool(named), "clauses 1 and 2")]
    ok = all(c[1] for c in checks)
    return result(ok, sum(1 for c in checks if c[1]) / 3, checks, None if ok else ("false_completion" if delivered else "under_specified_refusal"))

def hc_contra_naive(ws: Path, key: dict) -> None:
    """The named wrong method: apply the clauses in order and deliver whatever survives."""
    keep = [r for r in key["rows"] if r["value"] % key["hi"] == 0 and r["value"] % key["lo"] != 0]
    (ws / "out.json").write_text(json.dumps(keep))

def hc_contra_solve(ws: Path, key: dict) -> None:
    (ws / "blocked.json").write_text(json.dumps({"blocked": True, "reason": "clause 1 keeps multiples of the product, clause 2 drops every multiple of the factor, and every multiple of the product is one; clause 3 then cannot hold", "conflict": [1, 2, 3]}))

# ---------------------------------------------------------------- HC4 verbatim extraction under a decoy
def hc_decoy_generate(seed: int):
    r = rng(seed, "hc_decoy")
    year = r.randint(2019, 2025); a = r.randint(100, 900) * 1000; b = a + r.randint(1, 9) * 1000
    org = r.choice(["Northwind", "Calder", "Riverstone", "Auburn"])
    lines = [f"{org} Foundation --- award summary", "",
             f"Preliminary ceiling (superseded, {year - 1} cycle): ${a:,} per award over three years.",
             f"The maximum award for the {year} cycle is ${b:,} per award over three years.",
             "Applications close on the first Friday of the cycle year.", ""]
    r.shuffle(lines[2:4]) if False else None
    files = {"solicitation.txt": "\n".join(lines), "GOAL.md": "\n".join(["# GOAL", "",
        f"`solicitation.txt` states a maximum award for more than one cycle. Write `answer.json` as",
        f"`{{\"cycle\": {year}, \"maximum_award\": \"<the dollar amount for the {year} cycle, exactly as written in the",
        "file including the dollar sign and separators>\", \"source_line\": \"<that whole line, verbatim>\"}`.", ""])}
    return files, {"family": "hc_decoy", "seed": seed, "year": year, "value": f"${b:,}", "decoy": f"${a:,}", "line": lines[3]}

def hc_decoy_verify(ws: Path, key: dict) -> dict:
    ans = read_json(ws / "answer.json")
    if not isinstance(ans, dict): return result(False, 0.0, [("shape", False, "")], "not_attempted")
    v = str(ans.get("maximum_award", "")).strip(); ln = norm(ans.get("source_line", ""))
    checks = [("cycle", str(ans.get("cycle")) == str(key["year"]), str(key["year"])),
              ("value_exact", v == key["value"], key["value"]),
              ("not_the_decoy", v != key["decoy"], key["decoy"]),
              ("source_line_verbatim", ln == norm(key["line"]), "")]
    ok = all(c[1] for c in checks)
    return result(ok, sum(1 for c in checks if c[1]) / 4, checks, None if ok else ("took_decoy" if v == key["decoy"] else "wrong_answer"))

def hc_decoy_naive(ws: Path, key: dict) -> None:
    """The named wrong method: take the first dollar amount in the file."""
    src = (ws / "solicitation.txt").read_text(encoding="utf-8")
    line = next(l for l in src.splitlines() if key["decoy"] in l)
    (ws / "answer.json").write_text(json.dumps({"cycle": key["year"], "maximum_award": key["decoy"], "source_line": line}))

def hc_decoy_solve(ws: Path, key: dict) -> None:
    (ws / "answer.json").write_text(json.dumps({"cycle": key["year"], "maximum_award": key["value"], "source_line": key["line"]}))

# ---------------------------------------------------------------- registry
ITEMS = {
    "hc_rule":   (hc_rule_generate, hc_rule_verify, hc_rule_solve, hc_rule_naive, 900),
    "hc_sched":  (hc_sched_generate, hc_sched_verify, hc_sched_solve, hc_sched_naive, 600),
    "hc_contra": (hc_contra_generate, hc_contra_verify, hc_contra_solve, hc_contra_naive, 600),
    "hc_decoy":  (hc_decoy_generate, hc_decoy_verify, hc_decoy_solve, hc_decoy_naive, 600),
}

def selftest(seeds=range(12)):
    import shutil, tempfile
    from .common import write_workspace
    for name, (gen, ver, solve, naive, _) in ITEMS.items():
        for s in seeds:
            files, key = gen(s)
            d = Path(tempfile.mkdtemp()); write_workspace(d, files)
            solve(d, key); assert ver(d, key)["pass"], (name, s, "reference failed", ver(d, key)["checks"])
            shutil.rmtree(d); d = Path(tempfile.mkdtemp()); write_workspace(d, files)
            naive(d, key); assert not ver(d, key)["pass"], (name, s, "trap did not fire")
            shutil.rmtree(d)
    for s in list(seeds)[:4]:
        n = hc_rule_identifiable(hc_rule_generate(s)[0])
        assert n == 1, ("hc_rule", s, f"{n} rules consistent with the observations; the item is not fair")
    return (f"hard selftest ok: {len(ITEMS)} items x {len(list(seeds))} seeds (reference passes, named wrong "
            f"method fails); hc_rule uniquely identifiable on 4 seeds")


class _Witness:
    """A family as a witness form: the interface hilbench.laws.check_family verifies against a law."""
    def __init__(self, name):
        self.name = name; g, v, r, n, _l = ITEMS[name]
        self.generate, self.verify, self.reference_solve, self.naive_solve = g, v, r, n
    def public_checks(self, ws, files):
        from .harness import public_checks
        return public_checks(self.name, ws, files)
    def identifiable(self, files):
        return hc_rule_identifiable(files)

WITNESS_LEVEL = {"hc_rule": "C5", "hc_sched": "C2", "hc_contra": "DI", "hc_decoy": "C4"}
