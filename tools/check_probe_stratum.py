#!/usr/bin/env python3
"""Hold DLI-Bench to the framework's ANTI-INFLATION rules.

`Delegation_Intelligence_Framework.pdf` §10 states ten rules and §16 six failure
modes. A dataset that claims to test them has to satisfy them first — a
benchmark whose own rows violate Rule 1 cannot enforce Rule 1 on a system.

**Scope.** This checker owns §10 and §16, and the structure of the probe
stratum. It does NOT own the measurement repairs from
`Difficulty_Is_Not_The_Index.md` — frontier computability, kappa cells, the
acceptance block, Rule 11's false-pass field, the load identity. Those are
`tools/check_dli_bench.py`, and both run over the same file:

    python3 tools/check_dli_bench.py        dataset/dli_bench_tasks_v0_2.jsonl
    python3 dataset/validate_dli_bench.py   dataset/dli_bench_tasks_v0_2.jsonl

Two checkers, one dataset, disjoint rules. A rule enforced in both would drift.

Each check names the section it comes from. Exit code 1 on any violation.

    python3 validate_dli_bench.py --self-test      # prove the checks can fail
"""
from __future__ import annotations

import collections
import json
import pathlib
import sys

BANDS = ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "TΩ"]
DLS = ["DL0", "DL1", "DL2", "DL3", "DL4", "DL5", "DL6", "DLΩ"]
SPLITS = ["dev", "validation", "certification_hidden"]
CIDS = [f"CID{i}" for i in range(7)]
HS = ["H0", "H1", "H2", "H3", "H4", "H5"]

#: §7's typical regions. A row that claims a DL band while allowing more
#: cognitive help than that band tolerates is not measuring that band.
MAX_HELP = {"DL0": "H5", "DL1": "H4", "DL2": "H3", "DL3": "H2",
            "DL4": "H1", "DL5": "H1", "DL6": "H1", "DLΩ": "H1"}

#: Rule 1 — no high DL claim on low-difficulty tasks. The band a DL row sits
#: on may not be more than one below its own level's anchor band.
MIN_BAND = {"DL0": 0, "DL1": 1, "DL2": 2, "DL3": 3, "DL4": 4, "DL5": 5,
            "DL6": 6, "DLΩ": 7}

DIFF = ["difficulty_horizon", "difficulty_coordination", "difficulty_uncertainty",
        "difficulty_ambiguity", "difficulty_tool_diversity",
        "difficulty_verification", "difficulty_novelty", "difficulty_env_change"]


def _h_index(budget: str) -> int:
    """The loosest budget a row allows, as an index into HS. `H5-H4` -> H5."""
    parts = [p.strip() for p in str(budget).replace(";", "-").split("-") if p.strip()]
    idx = [HS.index(p) for p in parts if p in HS]
    return max(idx) if idx else -1


def check(rows):
    """Every violation found, as (rule, task_id, message)."""
    bad = []

    def fail(rule, tid, msg):
        bad.append((rule, tid, msg))

    ids = [r["task_id"] for r in rows]
    for tid, n in collections.Counter(ids).items():
        if n > 1:
            fail("integrity", tid, f"task_id appears {n} times")

    for r in rows:
        tid = r["task_id"]
        probe = r.get("probe_kind", "")

        # ── Rule 9: difficulty is externally declared, and declared fully ──
        for f in DIFF:
            v = r.get(f)
            if not isinstance(v, int) or not 0 <= v <= 5:
                fail("Rule 9", tid, f"{f}={v!r} is not an integer in 0..5")
        if r.get("task_band") not in BANDS:
            fail("Rule 9", tid, f"task_band {r.get('task_band')!r} is not a T band")
        # `unassigned_by_design` is the budget-cross stratum's sentinel and is
        # correct there: assigning a DL to a row whose whole purpose is to vary
        # h at fixed T would presuppose the answer the row exists to measure.
        if r.get("target_dl") not in DLS and r.get("target_dl") != "unassigned_by_design":
            fail("Rule 9", tid, f"target_dl {r.get('target_dl')!r} is not a DL band")

        # ── Rule 1: no high DL claim on a LOW-DIFFICULTY task ─────────────
        # The first version of this check read "low difficulty" as "low band",
        # which is the assumption Proposition 1 refutes: T aggregates
        # coordinates whose effects on S have opposite signs, so a T0-T1 class
        # with maximal d_ver and d_risk is near the bottom of the band scale
        # and near the top of what anyone will delegate. The kappa_cross
        # stratum exists to hold exactly those, and flagging them was the
        # checker importing the defect it was written to catch.
        #
        # So the rule is applied where it means something: a claim is on a
        # low-difficulty task when the band is low AND kappa is low too —
        # nothing hard to do, nothing hard to check, nothing costly to get
        # wrong. A saturation gradient is the remaining exception, and only
        # because its low member is labelled and paired with the high one.
        if r.get("target_dl") in MIN_BAND and r.get("task_band") in BANDS:
            want, got = MIN_BAND[r["target_dl"]], BANDS.index(r["task_band"])
            k = r.get("kappa") or {}
            hard_to_check = max(int(k.get("verifiability") or 0),
                                int(k.get("reversibility") or 0)) >= 4
            if got < want and not hard_to_check and probe != "saturation_gradient":
                fail("Rule 1", tid,
                     f"{r['target_dl']} claimed on {r['task_band']} with kappa "
                     f"{k or 'absent'} — low to do, low to check, low to undo")

        # ── §7: the budget must not exceed what the DL band tolerates ─────
        # A sweep member is exempt, and the exemption is the point of a sweep:
        # §6 asks for F_A(h,p) as a SURFACE, so the group deliberately runs the
        # same task outside the band's own budget to find where the frontier
        # falls. Its `target_dl` names the band the task anchors, not a claim
        # the member makes. The group-level check below keeps that honest by
        # requiring at least one member inside the band.
        allowed = _h_index(r.get("primary_intervention_budget", ""))
        if allowed < 0:
            fail("§5", tid, f"primary_intervention_budget "
                            f"{r.get('primary_intervention_budget')!r} is not an H level")
        elif (r.get("target_dl") in MAX_HELP and probe != "h_sweep"
              and r.get("stratum") != "budget_cross"):
            if allowed > HS.index(MAX_HELP[r["target_dl"]]):
                fail("§7", tid,
                     f"{r['target_dl']} allows {r['primary_intervention_budget']}, looser "
                     f"than {MAX_HELP[r['target_dl']]} — the band's own definition")

        # ── §9.2: the CID ceiling has to be a real level ──────────────────
        if r.get("max_cid") not in CIDS:
            fail("§9.2", tid, f"max_cid {r.get('max_cid')!r} is not CID0..CID6")

        # ── Rule 5: success is externally declared, never self-reported ───
        crit = (r.get("success_criterion") or "").lower()
        if not crit:
            fail("Rule 5", tid, "no success_criterion")
        for phrase in ("self-report", "the agent reports", "claims success"):
            if phrase in crit:
                fail("Rule 5", tid, f"success_criterion rests on {phrase!r}")
        vtype = (r.get("verifier_type")
                 or (r.get("verifier") or {}).get("verifier_type") or "")
        if not str(vtype).strip():
            fail("Rule 5", tid, "no verifier_type")
        if not (r.get("verifier_inputs") or "").strip():
            fail("Rule 5", tid, "no verifier_inputs")

        # ── Rule 6: the tool set is part of the test condition ────────────
        if not (r.get("declared_tool_set") or "").strip():
            fail("Rule 6", tid, "no declared_tool_set — results are not comparable "
                                "without it")

        # ── Rule 7: cost is reported, never folded into the score ─────────
        # The strata carry it as the `loss` block, which is the stronger form:
        # p* = rho/(1+rho) is set by the class rather than chosen by the
        # evaluator. Either shape satisfies the rule; neither being present
        # does not.
        loss = r.get("loss")
        if not (r.get("cost_normalization") or "").strip() and not isinstance(loss, dict):
            fail("Rule 7", tid, "no cost_normalization and no loss block")
        if isinstance(loss, dict):
            if "p_star" not in loss:
                fail("Rule 7", tid, "loss block without p_star")
            elif loss.get("c_residual") is None and loss.get("p_star") != 1.0:
                fail("Rule 7", tid,
                     "residual harm is unbounded but p* is not 1.0 — the "
                     "irreversibility floor is the point of the field")

        # ── d_risk: the framework's eighth coordinate, absent from v0.1 ────
        if not isinstance(r.get("difficulty_risk"), int):
            fail("§4.1", tid, "no difficulty_risk — the framework's vector is "
                              "<d_dec, d_hor, d_unc, d_tool, d_nov, d_ver, "
                              "d_coord, d_risk> and v0.1 carried env_change in "
                              "its place")

        # ── Rule 8: escalation is an outcome and needs a stated meaning ───
        pol = (r.get("escalation_policy") or "").strip()
        if not pol:
            fail("Rule 8", tid, "no escalation_policy")
        if r.get("expected_outcome_class") not in ("complete", "escalate", "refuse"):
            fail("Rule 8", tid,
                 f"expected_outcome_class {r.get('expected_outcome_class')!r} is not "
                 f"one of complete/escalate/refuse")

        # ── a probe must be able to fail ──────────────────────────────────
        if probe:
            if not (r.get("falsified_if") or "").strip():
                fail("§10", tid, f"probe {probe!r} has no falsified_if — a probe that "
                                 f"cannot be falsified is a task")
            if not (r.get("rules_exercised") or "").strip():
                fail("§10", tid, f"probe {probe!r} names no rule or failure mode")

        # ── §16.4: a scripted rescue must say what is said and when ───────
        if probe == "silent_rescue":
            if not (r.get("intervention_script") or "").strip():
                fail("§16.4", tid, "a silent-rescue probe with no script is not "
                                   "reproducible across systems")
            if r.get("max_cid") == "CID0":
                fail("§16.4", tid, "the probe delivers cognitive help; its CID ceiling "
                                   "cannot be CID0")

        # ── §16.2: approval inflation is only a test at CID0 ──────────────
        if probe == "approval_inflation" and r.get("max_cid") != "CID0":
            fail("§16.2", tid, "governance supplies no cognition, so the ceiling is CID0")

        # ── §15.2: compression must report BOTH bands ─────────────────────
        if probe == "delegation_compression":
            if not (r.get("original_task_band") and r.get("post_tool_task_band")):
                fail("§15.2", tid, "compression row must carry original and post-tool bands")

        # ── §15.3: an organizational row must be coordination-ESSENTIAL ───
        if probe == "coordination_essential":
            if r.get("coordination_required") != "essential":
                fail("§15.3", tid, "an O-DL row whose coordination is not essential "
                                   "measures its best member")
            if not (r.get("dl_o_target") or "").startswith("O-DL"):
                fail("§8", tid, "no dl_o_target")

        # ── Rule 8 again: an escalation probe must not accept an artifact ─
        if probe == "escalation_correct":
            if r.get("expected_outcome_class") != "escalate":
                fail("Rule 8", tid, "an underdetermined task whose expected outcome is "
                                    "'complete' is not underdetermined")

    # ── §16.3 / §6: splits must span the bands ────────────────────────────
    per_split = collections.defaultdict(set)
    for r in rows:
        per_split[r.get("split")].add(r.get("task_band"))
    for s in SPLITS:
        got = per_split.get(s, set())
        if not got:
            fail("§11", s, "split is empty")
            continue
        low = {b for b in got if BANDS.index(b) <= 2}
        high = {b for b in got if BANDS.index(b) >= 4}
        if not low or not high:
            fail("§6", s,
                 f"split {s!r} spans {sorted(got, key=BANDS.index)} — a frontier "
                 f"F(h,p)=max{{T:S>=p}} needs anchors both below and above the "
                 f"band being certified")

    # ── pairs and groups must be complete ─────────────────────────────────
    pairs = collections.defaultdict(list)
    for r in rows:
        if r.get("probe_pair_id"):
            pairs[r["probe_pair_id"]].append(r["task_id"])
    for p, members in pairs.items():
        if len(members) < 2:
            fail("§10", p, f"pair has one member ({members}) — the comparison IS the "
                           f"measurement")
    groups = collections.defaultdict(list)
    for r in rows:
        if r.get("h_sweep_group"):
            groups[r["h_sweep_group"]].append(r)
    for g, members in groups.items():
        budgets = [m["primary_intervention_budget"] for m in members]
        if len(set(budgets)) < 2:
            fail("§6", g, f"sweep group has one budget ({budgets}) — one point is "
                          f"not a surface")
        # The exemption above lets a member sit outside its band's budget. It
        # must not let EVERY member sit outside, or the group measures a
        # frontier for a band it never actually tests.
        inside = [m for m in members
                  if m.get("target_dl") in MAX_HELP
                  and _h_index(m["primary_intervention_budget"])
                  <= HS.index(MAX_HELP[m["target_dl"]])]
        if not inside:
            fail("§7", g, f"every member of the sweep is looser than its band allows "
                          f"({budgets}) — nothing in the group tests the band it names")
        # A sweep compares budgets, so everything else has to be held constant.
        for field in ("task_band", "target_dl", "family", "environment_seed",
                      "verifier_type", "hidden_perturbation"):
            if len({str(m.get(field)) for m in members}) > 1:
                fail("§11.2", g, f"sweep members differ in {field!r}; then the "
                                 f"difference between them is not the budget")

    return bad


def _self_test():
    """Prove each check can fail, on rows built to break it.

    A validator nobody has seen fail is a validator nobody should trust.
    """
    good = {
        "task_id": "X-1", "target_dl": "DL3", "task_band": "T3", "family": "software",
        "primary_intervention_budget": "H1", "max_cid": "CID1",
        "success_criterion": "sealed reference matched",
        "verifier_type": "unit_test", "verifier_inputs": "hidden tests",
        "declared_tool_set": "sandbox", "cost_normalization": "reported separately",
        "escalation_policy": "allowed", "expected_outcome_class": "complete",
        "probe_kind": "", "falsified_if": "", "rules_exercised": "",
        "split": "dev", "probe_pair_id": "", "h_sweep_group": "",
    }
    good.update({f: 2 for f in DIFF})
    good["difficulty_risk"] = 1
    good["kappa"] = {"verifiability": 2, "reversibility": 1}
    good["loss"] = {"value": 1.0, "c_residual": 0.0, "p_star": 0.2}
    good["verifier"] = {"verifier_type": "unit_test", "false_pass_rate": None}
    good["acceptance"] = {"locus_required": "a2_separated_process",
                          "sigma_bound": 0.3, "sigma_bound_mechanism": "sealed tests"}
    cases = [
        ("Rule 1", dict(good, task_id="X-2", target_dl="DL5", task_band="T1")),
        ("Rule 5", dict(good, task_id="X-3",
                        success_criterion="the agent reports that it finished")),
        ("Rule 6", dict(good, task_id="X-4", declared_tool_set="")),
        ("Rule 8", dict(good, task_id="X-5", expected_outcome_class="done")),
        ("Rule 9", dict(good, task_id="X-6", difficulty_horizon="high")),
        ("§7", dict(good, task_id="X-7", target_dl="DL4",
                    task_band="T4", primary_intervention_budget="H3")),
        ("§10", dict(good, task_id="X-8", probe_kind="autonomy_theater",
                     falsified_if="")),
        ("§16.4", dict(good, task_id="X-9", probe_kind="silent_rescue",
                       intervention_script="", max_cid="CID2")),
        ("§16.2", dict(good, task_id="X-10", probe_kind="approval_inflation",
                       max_cid="CID3", falsified_if="x", rules_exercised="y")),
        ("§15.2", dict(good, task_id="X-11", probe_kind="delegation_compression",
                       falsified_if="x", rules_exercised="y")),
        ("§15.3", dict(good, task_id="X-12", probe_kind="coordination_essential",
                       falsified_if="x", rules_exercised="y",
                       coordination_required="helpful")),
        ("§4.1", dict(good, task_id="X-16", loss={"p_star": 0.2, "c_residual": 0.0},
                      difficulty_risk="high")),
        ("Rule 7", dict(good, task_id="X-17",
                        loss={"c_residual": None, "p_star": 0.5})),
        ("integrity", [dict(good), dict(good)]),
    ]
    ok = True
    for rule, case in cases:
        rows = case if isinstance(case, list) else [case]
        # every self-test set needs a spanning split or §6 fires and masks it
        rows = rows + [dict(good, task_id=f"{rows[0]['task_id']}-anchor-{b}",
                            task_band=b, target_dl=dl,
                            primary_intervention_budget="H0", split=s)
                       for b, dl in (("T1", "DL1"), ("T5", "DL5"))
                       for s in SPLITS]
        found = {v[0] for v in check(rows)}
        hit = rule in found
        print(f"  {'fires ' if hit else 'SILENT'}  {rule:12} on a row built to break it")
        ok &= hit
    return ok


def main(argv):
    if "--self-test" in argv:
        print("self-test: each check, against a row that violates it")
        ok = _self_test()
        print("\nself-test:", "PASS" if ok else "FAIL")
        return 0 if ok else 1

    path = pathlib.Path(argv[1] if len(argv) > 1
                        else pathlib.Path(__file__).parent / "dli_bench_tasks_v0_2.jsonl")
    rows = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    bad = check(rows)
    probes = [r for r in rows if r.get("probe_kind")]
    print(f"{path.name}: {len(rows)} rows "
          f"({len(rows) - len(probes)} ladder, {len(probes)} probe)")
    if not bad:
        print("all framework checks pass")
        return 0
    print(f"\n{len(bad)} violation(s):")
    for rule, tid, msg in bad:
        print(f"  [{rule}] {tid}: {msg}")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
