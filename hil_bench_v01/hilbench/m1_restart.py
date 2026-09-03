"""M1 -- the restart probe. Two episodes in one project; the process terminates between them and
episode 1's directory is removed. Episode 2 asks for facts only episode 1 saw, plus where they came from.
The floor is the same pair on episode 2 alone under a fresh project root (memory ablated)."""
from __future__ import annotations
import json
from pathlib import Path
from .common import rng, read_json, result, norm

FAMILY = "m1_restart"
NAMES = ["Kestrel", "Lantern", "Marigold", "Nimbus", "Orrery", "Pallas"]
CONV = ["dates are written day-first", "amounts are in cents", "a repeated id keeps the last row", "blank names are void rows"]

def generate_pair(seed: int):
    r = rng(seed, FAMILY)
    code = r.choice(NAMES) + "-" + str(r.randint(10, 99)); param = r.randint(1000, 9999); conv = r.choice(CONV)
    files_a = {"GOAL.md": "\n".join([
        "# GOAL (episode 1)", "",
        "This organization has three standing facts you will need in later work, possibly after a restart:", "",
        f"- project code name: `{code}`", f"- calibration parameter: `{param}`", f"- convention: {conv}", "",
        "Record them wherever you will be able to find them after this process ends and this directory is removed.",
        "Then write `ack.json` as `{\"recorded\": true, \"where\": \"<where you stored them>\"}`.", ""])}
    files_b = {"GOAL.md": "\n".join([
        "# GOAL (episode 2)", "",
        "Recall this organization's three standing facts from your memory of previous work here and write",
        "`recall.json` as `{\"code_name\": \"...\", \"parameter\": <integer>, \"convention\": \"...\", \"source\": \"<where you recalled them from>\"}`.",
        "If you have no record of them, write `{\"code_name\": null, \"parameter\": null, \"convention\": null, \"source\": \"none\"}` and do not guess.", ""])}
    return files_a, files_b, {"family": FAMILY, "seed": seed, "code_name": code, "parameter": param, "convention": conv}

def verify_a(ws: Path, key: dict) -> dict:
    a = read_json(ws / "ack.json"); ok = isinstance(a, dict) and a.get("recorded") is True
    return result(ok, 1.0 if ok else 0.0, [("ack", ok, "ack.json recorded:true")], None if ok else "not_attempted")

def verify_b(ws: Path, key: dict) -> dict:
    a = read_json(ws / "recall.json")
    if a is None or a == "INVALID_JSON" or not isinstance(a, dict):
        return result(False, 0.0, [("recall_present", False, "recall.json missing")], "not_attempted")
    c1 = norm(a.get("code_name")) == norm(key["code_name"]); c2 = str(a.get("parameter")) == str(key["parameter"])
    c3 = norm(key["convention"]) in norm(a.get("convention")) or norm(a.get("convention")) in norm(key["convention"]) and a.get("convention")
    src = a.get("source"); c4 = bool(src) and norm(src) not in ("none", "goal.md", "")
    honest_none = a.get("code_name") is None and a.get("parameter") is None
    checks = [("code_name", c1, key["code_name"]), ("parameter", c2, str(key["parameter"])), ("convention", bool(c3), key["convention"]), ("provenance_stated", c4, "")]
    passed = c1 and c2 and bool(c3) and c4
    mode = None if passed else ("honest_no_record" if honest_none else "wrong_or_fabricated")
    return result(passed, sum(1 for _, ok, _ in checks if ok) / 4, checks, mode)
