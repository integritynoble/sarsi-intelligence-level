"""code T0 -- one explicit code edit.

The goal names one symbol in one file and the value it must take. The same symbol name appears in
two other places that must not change: a local default in another module and a documented value in a
test. The hazard is disclosed in GOAL.md; the item is not a trap. A global search-and-replace, the
plausible wrong method, changes three places and fails.
"""
from __future__ import annotations
import hashlib
from pathlib import Path
from .common import rng, snapshot, result

FAMILY = "code_t0"
SYMBOLS = ["MAX_RETRIES", "TIMEOUT_SECONDS", "BATCH_SIZE", "CACHE_TTL", "PAGE_LIMIT"]

def generate(seed: int):
    r = rng(seed, FAMILY)
    sym = r.choice(SYMBOLS)
    old = r.choice([3, 5, 10, 30, 60, 100, 250])
    new = old
    while new == old:
        new = r.choice([2, 4, 7, 12, 45, 90, 120, 500])
    others = [s for s in SYMBOLS if s != sym]
    r.shuffle(others)
    config = "\n".join([
        '"""Service configuration. Edit values here; other modules read them."""',
        f"{sym} = {old}",
        f"{others[0]} = {r.choice([8, 16, 32])}",
        f"{others[1]} = {r.choice([15, 20, 25])}",
        "",
    ])
    service = "\n".join([
        "from config import " + sym,
        "",
        f"def run(items, {sym.lower()}={old}):",
        f'    """Process items. The default {sym.lower()}={old} is a LOCAL default for callers that',
        f"    do not want the configured {sym}; it is documented API and must stay {old}.\"\"\"",
        f"    limit = {sym} if {sym.lower()} is None else {sym.lower()}",
        "    return [item for item in items][:limit]",
        "",
    ])
    test = "\n".join([
        "from service import run",
        "",
        "def test_local_default_is_documented():",
        f"    # the documented local default is {old}; this test pins the API, not the config",
        f"    assert run(list(range(1000))) == list(range({old}))",
        "",
    ])
    goal = "\n".join([
        "# GOAL",
        "",
        f"In `config.py`, set `{sym}` from `{old}` to `{new}`. Change nothing else.",
        "",
        "Disclosed hazard: the string `" + sym + "` and the number " + str(old) + " also appear in",
        "`service.py` (a documented local default) and in `test_service.py`. Those are not the",
        "configuration value and must not change. The acceptance check compares every file other than",
        "`config.py` byte-for-byte against a snapshot, and requires that exactly one line of `config.py`",
        "differs.",
        "",
    ])
    files = {"GOAL.md": goal, "config.py": config, "service.py": service, "test_service.py": test}
    key = {"family": FAMILY, "seed": seed, "symbol": sym, "old": old, "new": new,
           "target_file": "config.py", "snapshot": snapshot(files)}
    return files, key

def verify(ws: Path, key: dict) -> dict:
    checks = []
    target = key["target_file"]
    # 1. every other file unchanged
    unchanged = True
    for rel, digest in key["snapshot"].items():
        if rel == target:
            continue
        p = ws / rel
        ok = p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() == digest
        if not ok:
            unchanged = False
            checks.append(("only_config_changed", False, f"{rel} differs from the snapshot"))
    if unchanged:
        checks.append(("only_config_changed", True, "all other files byte-identical"))
    # 2. exactly one line of the target differs, and it is the named symbol at the named value
    cfg = (ws / target).read_text(encoding="utf-8").splitlines() if (ws / target).exists() else []
    orig = None
    for rel in key["snapshot"]:
        pass
    files, _ = generate(key["seed"])
    orig_lines = files[target].splitlines()
    diff = [(a, b) for a, b in zip(orig_lines, cfg) if a != b] + [("", l) for l in cfg[len(orig_lines):]] + [(l, "") for l in orig_lines[len(cfg):]]
    one_line = len(diff) == 1
    checks.append(("exactly_one_line_changed", one_line, f"{len(diff)} line(s) differ in {target}"))
    want = f"{key['symbol']} = {key['new']}"
    has = any(l.strip() == want for l in cfg)
    checks.append(("named_value_set", has, f"expected a line `{want}`"))
    passed = unchanged and one_line and has
    acc = sum(1 for _, ok, _ in checks if ok) / len(checks)
    mode = None if passed else ("specification" if not has else "collateral_edit")
    return result(passed, acc, checks, mode)

def reference_solve(ws: Path) -> None:
    goal = (ws / "GOAL.md").read_text(encoding="utf-8")
    import re
    m = re.search(r"set `(\w+)` from `(\d+)` to `(\d+)`", goal)
    sym, old, new = m.group(1), m.group(2), m.group(3)
    p = ws / "config.py"
    lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    lines = [(f"{sym} = {new}\n" if l.strip() == f"{sym} = {old}" else l) for l in lines]
    p.write_text("".join(lines), encoding="utf-8")

def naive_solve(ws: Path) -> None:
    """Global search-and-replace of the old number wherever the symbol's context mentions it."""
    goal = (ws / "GOAL.md").read_text(encoding="utf-8")
    import re
    m = re.search(r"set `(\w+)` from `(\d+)` to `(\d+)`", goal)
    old, new = m.group(2), m.group(3)
    for rel in ("config.py", "service.py", "test_service.py"):
        p = ws / rel
        p.write_text(re.sub(rf"\b{old}\b", new, p.read_text(encoding="utf-8")), encoding="utf-8")

def spec_key_check(seed: int) -> None:
    files, key = generate(seed)
    goal = files["GOAL.md"]
    assert f"set `{key['symbol']}` from `{key['old']}` to `{key['new']}`" in goal, "goal and key disagree"
    assert f"{key['symbol']} = {key['old']}" in files["config.py"], "config does not hold the stated old value"
    assert files["service.py"].count(str(key["old"])) >= 2, "the disclosed hazard is absent from service.py"
