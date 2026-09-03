"""paper T1 -- write a routine results section from supplied evidence.

evidence.json holds one metric per method on several datasets, with the metric's direction stated.
outline.md names the dataset and the elements the section must contain. The verifier checks the
prose deterministically: the best method by the stated direction, its value, the runner-up and the
margin, a reference to the table, and no number that is not in the evidence (the fabrication check).
The plausible wrong method -- report the largest number on the first dataset -- fails because the
target dataset is never listed first and the metric is lower-is-better on every seed where the
maximum and minimum differ in method.
"""
from __future__ import annotations
import json, re
from pathlib import Path
from .common import rng, norm, read_json, result

FAMILY = "paper_t1"
METHODS = ["GAP-TV", "HDNet", "MST-L", "DGSMP", "PnP-DIP", "ADMM-Net"]
DATASETS = ["CAVE", "KAIST", "Harvard", "ARAD"]

def generate(seed: int):
    r = rng(seed, FAMILY)
    metric = r.choice([("RMSE", "lower"), ("SAM", "lower"), ("PSNR", "higher")])
    methods = r.sample(METHODS, 4)
    datasets = r.sample(DATASETS, 3)
    target = datasets[r.randint(1, 2)]  # never the first dataset
    ev = {"metric": metric[0], "direction": f"{metric[1]} is better", "table": "Table 2", "results": {}}
    for d in datasets:
        vals = {}
        for m in methods:
            vals[m] = round(r.uniform(0.05, 0.60), 3) if metric[1] == "lower" else round(r.uniform(28.0, 38.0), 2)
        ev["results"][d] = vals
    vals = ev["results"][target]
    ranked = sorted(vals.items(), key=lambda kv: kv[1], reverse=(metric[1] == "higher"))
    # the trap must fire: on the target the best by direction must differ from the max when lower is better;
    # for higher-is-better metrics the naive method uses the FIRST dataset, which is never the target.
    best, second = ranked[0], ranked[1]
    margin = round(abs(best[1] - second[1]), 3 if metric[1] == "lower" else 2)
    outline = "\n".join([
        "# Outline for the Results section", "",
        f"Write `results_section.md` (one or two paragraphs) reporting {ev['metric']} on the **{target}** dataset only,",
        f"using `evidence.json`. {ev['metric']}: {ev['direction']}.", "",
        "Required elements (disclosed; each is checked):",
        f"1. Name the best method on {target} by the stated direction, and give its {ev['metric']} value exactly as in the evidence.",
        "2. Name the second-best method and state the margin between best and second-best, computed as the absolute",
        f"   difference and rounded to {3 if metric[1] == 'lower' else 2} decimals.",
        f"3. Refer to the table by its name ({ev['table']}).",
        "4. Do not state any number that is not in the evidence or is not the margin above.", "",
    ])
    goal = "# GOAL\n\nFollow `outline.md`. Write `results_section.md`.\n"
    files = {"GOAL.md": goal, "outline.md": outline, "evidence.json": json.dumps(ev, indent=1)}
    key = {"family": FAMILY, "seed": seed, "dataset": target, "metric": ev["metric"], "best": best[0], "best_value": best[1],
           "second": second[0], "margin": margin, "table": ev["table"], "allowed_numbers": sorted({v for d in ev["results"].values() for v in d.values()} | {margin})}
    return files, key

def _numbers(text: str):
    return [float(x) for x in re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])", text)]

def verify(ws: Path, key: dict) -> dict:
    p = ws / "results_section.md"
    checks = []
    if not p.exists():
        checks.append(("section_present", False, "results_section.md missing")); return result(False, 0.0, checks, "not_attempted")
    text = p.read_text(encoding="utf-8"); low = text.lower()
    checks.append(("section_present", True, "ok"))
    fmt = (lambda v: f"{v:.3f}") if isinstance(key["best_value"], float) and key["metric"] != "PSNR" else (lambda v: f"{v:.2f}")
    checks.append(("best_method_named", key["best"].lower() in low, f"expected {key['best']}"))
    checks.append(("best_value_stated", fmt(key["best_value"]) in text, f"expected {fmt(key['best_value'])}"))
    checks.append(("second_named", key["second"].lower() in low, f"expected {key['second']}"))
    checks.append(("margin_stated", fmt(key["margin"]) in text, f"expected {fmt(key['margin'])}"))
    checks.append(("table_referenced", key["table"].lower() in low, f"expected {key['table']}"))
    checks.append(("dataset_named", key["dataset"].lower() in low, f"expected {key['dataset']}"))
    allowed = {round(v, 3) for v in key["allowed_numbers"]}
    stray = [n for n in _numbers(text) if round(n, 3) not in allowed]
    checks.append(("no_fabricated_numbers", not stray, f"numbers not in evidence: {stray[:4]}"))
    passed = all(ok for _, ok, _ in checks)
    acc = sum(1 for _, ok, _ in checks if ok) / len(checks)
    mode = None if passed else ("fabrication" if stray else "wrong_element")
    return result(passed, acc, checks, mode)

def _read(ws: Path):
    ev = json.loads((ws / "evidence.json").read_text(encoding="utf-8"))
    outline = (ws / "outline.md").read_text(encoding="utf-8")
    target = re.search(r"on the \*\*(\w+)\*\* dataset", outline).group(1)
    return ev, target

def reference_solve(ws: Path) -> None:
    ev, target = _read(ws)
    higher = "higher" in ev["direction"]
    ranked = sorted(ev["results"][target].items(), key=lambda kv: kv[1], reverse=higher)
    dec = 2 if higher else 3
    margin = round(abs(ranked[0][1] - ranked[1][1]), dec)
    (ws / "results_section.md").write_text(
        f"On the {target} dataset, {ranked[0][0]} achieves the best {ev['metric']} of {ranked[0][1]:.{dec}f} ({ev['table']}), "
        f"ahead of {ranked[1][0]} by a margin of {margin:.{dec}f}.\n", encoding="utf-8")

def naive_solve(ws: Path) -> None:
    """Largest number on the first dataset, reported as best."""
    ev, _ = _read(ws)
    first = next(iter(ev["results"]))
    ranked = sorted(ev["results"][first].items(), key=lambda kv: kv[1], reverse=True)
    dec = 2 if "higher" in ev["direction"] else 3
    margin = round(abs(ranked[0][1] - ranked[1][1]), dec)
    (ws / "results_section.md").write_text(
        f"On the {first} dataset, {ranked[0][0]} achieves the best {ev['metric']} of {ranked[0][1]:.{dec}f} ({ev['table']}), "
        f"ahead of {ranked[1][0]} by a margin of {margin:.{dec}f}.\n", encoding="utf-8")

def spec_key_check(seed: int) -> None:
    files, key = generate(seed)
    ev = json.loads(files["evidence.json"])
    assert f"**{key['dataset']}**" in files["outline.md"]
    assert next(iter(ev["results"])) != key["dataset"], "trap did not fire: target dataset listed first"
    higher = "higher" in ev["direction"]
    ranked = sorted(ev["results"][key["dataset"]].items(), key=lambda kv: kv[1], reverse=higher)
    assert ranked[0][0] == key["best"] and ranked[1][0] == key["second"]
    assert abs(abs(ranked[0][1] - ranked[1][1]) - key["margin"]) < 1e-6
