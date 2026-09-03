"""job T0 -- extract the hard requirements from one posting.

A posting lists required, preferred and nice-to-have qualifications, plus gates (work authorization,
clearance, location, degree). GOAL.md asks for the required set only, normalized. The plausible wrong
method -- everything that looks like a qualification, or the first list -- fails because the generator
always puts a non-required list first and makes the lists overlap in vocabulary.

Live-check defect, found and repaired 2026-09-03: the first wording asked for "the Location line,
verbatim"; a real executor returned the line including its `Location:` label and was marked wrong on a
rule the prose did not state. The goal now says the label is excluded and the verifier strips it.
"""
from __future__ import annotations
from pathlib import Path
from .common import rng, norm, read_json, result

FAMILY = "job_t0"
SKILLS = ["Python", "PyTorch", "C++", "distributed training", "CUDA", "Kubernetes", "SQL",
          "signal processing", "computational imaging", "statistics", "Rust", "JAX"]
DEGREES = ["PhD in a quantitative field", "MS in computer science or equivalent", "BS in engineering or equivalent"]

def generate(seed: int):
    r = rng(seed, FAMILY)
    title = r.choice(["Research Scientist, Agents", "Applied Scientist, Imaging", "ML Engineer, Inference",
                      "Senior Research Engineer", "Computational Biologist"])
    company = r.choice(["Halcyon Labs", "Northbridge AI", "Lumen Diagnostics", "Vantage Compute", "Orrery Systems"])
    loc = r.choice(["Boston, MA (on-site)", "Remote (US)", "Austin, TX (hybrid)", "London, UK (on-site)"])
    degree = r.choice(DEGREES)
    years = r.choice([2, 3, 5, 7])
    skills = r.sample(SKILLS, 5)
    req_skills, pref_skills = skills[:2], skills[2:4]
    nice = skills[4]
    auth = r.choice([True, False])
    clearance = r.choice([True, False, False])
    required = [degree, f"{years}+ years of relevant experience"] + req_skills
    if auth: required.append("authorization to work in the posting's country without sponsorship")
    if clearance: required.append("ability to obtain a security clearance")
    preferred = pref_skills + [f"experience with {nice} in production", "publications in a relevant venue"]
    lists = [("Required qualifications", required), ("Preferred qualifications", preferred),
             ("Nice to have", ["open-source contributions", f"familiarity with {nice}"])]
    # The trap must fire on every instance: a non-required list always comes first.
    first = r.choice([1, 2])
    lists[0], lists[first] = lists[first], lists[0]
    body = [f"{title} -- {company}", f"Location: {loc}", "", "About the role", "You will build and evaluate agent systems with a small team.", ""]
    for name, items in lists:
        body.append(name)
        body += [f"  - {it}" for it in items]
        body.append("")
    text = "\n".join(body)
    goal = "\n".join([
        "# GOAL", "",
        "From `posting.txt`, write `requirements.json` as", "",
        '`{"required": [<each bullet under "Required qualifications", verbatim>],',
        ' "work_authorization_required": <true|false>, "clearance_required": <true|false>,',
        ' "location": "<the text after `Location:` on the Location line, verbatim, without the label>"}`', "",
        "Disclosed: only the bullets under the heading `Required qualifications` are required. Bullets",
        "under `Preferred qualifications` and `Nice to have` are not, even when they mention the same",
        "skills, and the lists are not always in the same order. `work_authorization_required` is true",
        "only if a required bullet mentions work authorization; `clearance_required` only if a required",
        "bullet mentions a clearance.", "",
    ])
    files = {"GOAL.md": goal, "posting.txt": text}
    key = {"family": FAMILY, "seed": seed, "required": required, "work_authorization_required": auth,
           "clearance_required": clearance, "location": loc}
    return files, key

def verify(ws: Path, key: dict) -> dict:
    ans = read_json(ws / "requirements.json")
    checks = []
    if ans is None or ans == "INVALID_JSON" or not isinstance(ans, dict):
        checks.append(("requirements_json_present", False, "requirements.json missing or not a JSON object"))
        return result(False, 0.0, checks, "not_attempted")
    checks.append(("requirements_json_present", True, "ok"))
    got = {norm(x) for x in ans.get("required", []) if isinstance(x, str)}
    want = {norm(x) for x in key["required"]}
    jacc = len(got & want) / len(got | want) if (got | want) else 0.0
    checks.append(("required_set_exact", got == want, f"jaccard {jacc:.2f}; extra {sorted(got - want)[:3]}; missing {sorted(want - got)[:3]}"))
    a_ok = ans.get("work_authorization_required") is key["work_authorization_required"]
    c_ok = ans.get("clearance_required") is key["clearance_required"]
    loc = norm(str(ans.get("location", "")))
    loc = loc[len("location:"):].strip() if loc.startswith("location:") else loc
    l_ok = loc == norm(key["location"])
    checks += [("work_authorization_flag", a_ok, ""), ("clearance_flag", c_ok, ""), ("location_verbatim", l_ok, "")]
    passed = got == want and a_ok and c_ok and l_ok
    acc = (jacc + a_ok + c_ok + l_ok) / 4
    mode = None if passed else ("included_non_required" if got - want else "missed_required" if want - got else "flag_or_location")
    return result(passed, acc, checks, mode)

def _lists(src: str) -> dict[str, list[str]]:
    out, cur = {}, None
    for line in src.splitlines():
        if line and not line.startswith(" ") and line.strip() in ("Required qualifications", "Preferred qualifications", "Nice to have"):
            cur = line.strip(); out[cur] = []
        elif cur and line.strip().startswith("- "):
            out[cur].append(line.strip()[2:])
        elif not line.strip():
            cur = None
    return out

def reference_solve(ws: Path) -> None:
    import json
    src = (ws / "posting.txt").read_text(encoding="utf-8")
    req = _lists(src).get("Required qualifications", [])
    loc = next(l for l in src.splitlines() if l.startswith("Location:")).split(":", 1)[1].strip()
    (ws / "requirements.json").write_text(json.dumps({
        "required": req,
        "work_authorization_required": any("authorization" in x.lower() for x in req),
        "clearance_required": any("clearance" in x.lower() for x in req),
        "location": loc}), encoding="utf-8")

def naive_solve(ws: Path) -> None:
    """Take the first bulleted list in the posting as the requirements."""
    import json
    src = (ws / "posting.txt").read_text(encoding="utf-8")
    first = next(iter(_lists(src).values()), [])
    loc = next(l for l in src.splitlines() if l.startswith("Location:")).split(":", 1)[1].strip()
    (ws / "requirements.json").write_text(json.dumps({
        "required": first,
        "work_authorization_required": any("authorization" in x.lower() for x in first),
        "clearance_required": any("clearance" in x.lower() for x in first),
        "location": loc}), encoding="utf-8")

def spec_key_check(seed: int) -> None:
    files, key = generate(seed)
    lists = _lists(files["posting.txt"])
    assert lists["Required qualifications"] == key["required"], "the Required list and the key disagree"
    assert key["work_authorization_required"] == any("authorization" in x.lower() for x in key["required"])
    assert key["clearance_required"] == any("clearance" in x.lower() for x in key["required"])
    assert f"Location: {key['location']}" in files["posting.txt"]
    first_list = next(iter(lists.values()))
    assert first_list != key["required"], "naive method reproduces the key; the trap did not fire"
