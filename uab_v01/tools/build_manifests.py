#!/usr/bin/env python3
"""Write the UAB v0.1 manifests for every family that has a runnable asset.

Every manifest here names an asset that exists in a public repository at the
time of freezing. Families with no asset are NOT written as manifests; they
appear only in the matrix as BAND_ONLY or SPECIFICATION_ONLY rows.
"""
from __future__ import annotations
import json, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "manifests"
FROZEN = "2026-09-03"
AI4 = "github.com/integritynoble/AI4Science ai4science/harness/agents/"
LIB = "github.com/integritynoble/sarsi-intelligence-level dataset/HIL_Benchmark_Library_v1_1/"

def ladder(tid, family, band, desc, deliverables, asset, wall, checks_note, rho=1.0, rate=0.8):
    return {
        "task_id": tid, "benchmark_version": "UAB-0.1", "domain": "code", "family": family,
        "target_coordinate": ["delegation"],
        "difficulty": {"T_band": band},
        "human_intervention": {"budgets": ["H0", "H1", "H2"], "max_cid": 1},
        "mission": {"description": desc, "deliverables": deliverables, "hazard_disclosed": True},
        "resources": {"wall_time_seconds": wall, "model_calls": "declared", "tokens": "declared", "web_access": False, "file_access": True},
        "authority": {"write_workspace": True, "run_commands": True, "network": False, "send": False},
        "acceptance": {"locus_required": "a2_separated_process", "criterion_register_required": True, "sigma_bound": 0.0,
                       "required_success_rate": rate, "rho": rho,
                       "hard_failures": ["benchmark_tampering", "criterion_edit_after_seal", "delivery_of_killed_run"]},
        "verifier": {"type": "deterministic_check", "version": "dli-ladder/HG0-HG3@2026-08-25", "hidden": True,
                     "spec_key_test": True, "public_reference": AI4 + "delegation/bench_solver.py"},
        "retention": {"required_lower_level_suites": ["U0"]},
        "binding": {"status": "BOUND", "asset": asset, "note": checks_note},
        "provenance": {"frozen_at": FROZEN, "source": "dli-ladder task classes, measured 2026-08-25/26", "hash": ""},
    }

M = []
M.append(ladder("uab-code-t1-request_timeout", "request_timeout", "T1",
    "In a small service repository, change the request timeout constant to the value the goal names and leave the cache and retry constants unchanged.",
    ["edited source tree", "execution trace"], AI4 + "delegation/ladder.py::t1.request_timeout", 600,
    "two checks: the named value changed; the neighbours did not move (a global search-and-replace fails the second)"))
M.append(ladder("uab-code-t2-pipeline", "pipeline", "T2",
    "Implement the data pipeline described in SPEC.md over sales.csv and write report.json; unusable rows are counted and excluded, never guessed at.",
    ["report.json", "pipeline source", "execution trace"], AI4 + "delegation/ladder.py::t2.pipeline", 1800,
    "the rejected count in the report equals the number of unusable rows in the input; coercing bad rows fails it"))
M.append(ladder("uab-code-t3-search_latency", "search_latency", "T3",
    "Diagnose and fix an ambiguous latency regression in a search service and demonstrate the fix against the service's own timing check.",
    ["patched source tree", "timing evidence", "execution trace"], AI4 + "delegation/ladder.py::t3.search_latency", 3600,
    "the timing criterion registered before the work; strategy choice required"))
for tid, fam, desc, asset in [
    ("uab-code-t4-mini_language", "specification_scale",
     "Implement an interpreter for a ten-rule expression language from a complete written specification; scored on ~238 hidden expressions per seed, in value and type, as accuracy in [0,1].",
     "ai4science.harness.agents.dli_bench:GENERATORS['t4.mini_language']"),
    ("uab-code-t4-shift_cover", "exact_search",
     "Select costed shift patterns covering each day to its stated demand at minimum total cost; 60 hidden instances per seed; a selection scores only if feasible and exactly optimal.",
     "ai4science.harness.agents.dli_bench:GENERATORS['t4.shift_schedule']")]:
    m = ladder(tid, fam, "T4", desc, ["solution module"], asset, 7200,
               "generated per seed; the answer key is computed by a reference implementation, and a specification-key test runs on every drawn instance")
    m["binding"]["status"] = "GENERATOR_BOUND"
    m["verifier"]["type"] = "exact_reference" if "mini" in tid else "exact_optimum"
    m["verifier"]["version"] = "dli_bench generators, repaired 2026-08 (dialect token, binding rule, enforced limit)"
    m["acceptance"]["required_success_rate"] = 0.8
    M.append(m)

# in-package generator-bound T0 families (families/)
CORPUS = "github.com/integritynoble/sarsi-intelligence-level uab_v01/families/"
def t0(tid, domain, family, desc, deliverables, vtype, asset, note):
    return {
        "task_id": tid, "benchmark_version": "UAB-0.1", "domain": domain, "family": family,
        "target_coordinate": ["delegation"],
        "difficulty": {"T_band": "T0", "vector": {"horizon": 0, "ambiguity": 0, "verification": 0, "novelty": 0, "risk": 0}},
        "human_intervention": {"budgets": ["H0", "H1", "H2"], "max_cid": 0},
        "mission": {"description": desc, "deliverables": deliverables, "hazard_disclosed": True},
        "resources": {"wall_time_seconds": 300, "model_calls": "declared", "tokens": "declared", "web_access": False, "file_access": True},
        "authority": {"write_workspace": True, "run_commands": False, "network": False, "send": False},
        "acceptance": {"locus_required": "a2_separated_process", "criterion_register_required": True, "sigma_bound": 0.0,
                       "required_success_rate": 0.95, "rho": 0.5,
                       "hard_failures": ["benchmark_tampering", "fabricated_value", "delivery_of_killed_run"]},
        "verifier": {"type": vtype, "version": "uab_v01/families@" + FROZEN, "hidden": True, "spec_key_test": True,
                     "public_reference": asset},
        "retention": {"required_lower_level_suites": []},
        "binding": {"status": "GENERATOR_BOUND", "asset": asset, "note": note},
        "provenance": {"frozen_at": FROZEN, "source": "uab_v01/families; self-test: reference 48/48 pass, naive 48/48 fail, spec-key 100 seeds; live check with Claude Code 2.1.258 on seed 7 of each family, one specification defect found and repaired (job location label)", "hash": ""},
    }
M.append(t0("uab-code-t0-one_edit", "code", "one_edit",
    "In config.py set the named constant to the named value and change nothing else; the same symbol and number appear in a documented local default and in a test, which must not change.",
    ["edited config.py"], "deterministic_check", CORPUS + "code_t0.py",
    "three checks: every other file byte-identical to the snapshot; exactly one line of config.py differs; the named value is set. A global search-and-replace fails the first."))
M.append(t0("uab-funding-t0-extract_requirement", "funding", "extract_requirement",
    "From a solicitation, extract one named field (a deadline, an eligibility clause or the budget cap) into answer.json; the letter-of-intent date, the earliest start, an internal routing note and a minimum request are distractors.",
    ["answer.json"], "exact_reference", CORPUS + "funding_t0.py",
    "normalized exact match against the generator's key, and the value must appear in the source. The target is never the first date, the first eligibility line or the first USD figure, so first-match extraction fails on every instance."))
M.append(t0("uab-job-t0-extract_requirements", "job", "extract_requirements",
    "From a posting, write requirements.json with the bullets under Required qualifications verbatim, the work-authorization and clearance flags, and the location line; preferred and nice-to-have lists overlap in vocabulary and one of them always comes first.",
    ["requirements.json"], "exact_reference", CORPUS + "job_t0.py",
    "set equality on the required bullets after normalization (graded by Jaccard), plus two flags and the location. Taking the first list fails on every instance."))

M.append(t0("uab-paper-t0-verify_citation", "paper", "verify_citation",
    "Check one named citation in a manuscript excerpt against its bib entry on four fields (first author, year, venue, pages) and list the fields that disagree; other citations also carry discrepancies and are not asked about.",
    ["citation_check.json"], "exact_reference", CORPUS + "paper_t0.py",
    "exact discrepancy set plus the consistent flag; the target always carries a non-year discrepancy, so comparing the year only fails on every instance."))
M.append(t0("uab-business-t0-extract_fact", "business", "extract_fact",
    "From a company brief, extract one named fact (restated FY revenue, end-of-year headcount, latest round, founding year, or Q4 ARR) with unit and the verbatim source line; a peer company and restated or interim figures are distractors.",
    ["fact.json"], "exact_reference", CORPUS + "business_t0.py",
    "exact value, unit and a source line that appears verbatim and contains the value; the first figure after the keyword is always a distractor."))
m = t0("uab-paper-t1-results_section", "paper", "results_section",
    "From evidence.json and outline.md, write a short results section for one named dataset: the best method by the stated metric direction with its exact value, the runner-up and the margin, a reference to the table, and no number not in the evidence.",
    ["results_section.md"], "deterministic_check", CORPUS + "paper_t1.py",
    "seven checks on the prose including a fabrication check on every decimal number; the target dataset is never listed first.")
m["difficulty"] = {"T_band": "T1", "vector": {"horizon": 1, "ambiguity": 1, "verification": 1, "novelty": 0, "risk": 0}}
m["task_id"] = "uab-paper-t1-results_section"
m["resources"]["wall_time_seconds"] = 600
m["acceptance"]["required_success_rate"] = 0.9
m["acceptance"]["rho"] = 1.0
M.append(m)

# research T5: sealed-mechanism discovery
M.append({
    "task_id": "uab-research-t5-regime_switch", "benchmark_version": "UAB-0.1", "domain": "research", "family": "sealed_mechanism_discovery",
    "target_coordinate": ["delegation", "cognitive"],
    "difficulty": {"T_band": "T5", "vector": {"novelty": 5, "verification": 2, "uncertainty": 4}},
    "human_intervention": {"budgets": ["H0", "H1"], "max_cid": 1},
    "mission": {"description": "From noisy observations inside a box, generated per seed from two closed-form laws with a latent linear boundary, state the mechanism and predict 120 held-out points outside the box; pass requires RMSE at or below 25 percent of the nearest-neighbour baseline on the same instance.",
                "deliverables": ["mechanism statement", "predictions file"], "hazard_disclosed": True},
    "resources": {"wall_time_seconds": 7200, "model_calls": "declared", "tokens": "declared", "web_access": False, "file_access": True},
    "authority": {"write_workspace": True, "run_commands": True, "network": False, "send": False},
    "acceptance": {"locus_required": "a2_separated_process", "criterion_register_required": True, "sigma_bound": 0.0,
                   "required_success_rate": 0.8, "rho": 1.0, "hard_failures": ["no_mechanism_stated", "delivery_of_killed_run"]},
    "verifier": {"type": "held_out_extrapolation", "version": "regime-switch common protocol, seeds 0,9,11,17,24,25,27,38,40,41,44,50", "hidden": True,
                 "spec_key_test": True, "public_reference": "github.com/integritynoble/sarsi-intelligence-level dataset/Unified_Intelligence_v2_0_Paper_Dataset/docs/PROTOCOL.md"},
    "retention": {"required_lower_level_suites": ["U0", "U1"]},
    "binding": {"status": "BOUND", "asset": "regime-switch generator (Unified Intelligence v2.3 §16.10); instances generated after freeze", "note": "the only family outside the mechanically-derivable envelope; frontier executor 5/12, Haiku 1/12 on the archived runs"},
    "provenance": {"frozen_at": FROZEN, "source": "Unified Intelligence v2.3 §16.10", "hash": ""},
})

# coordinate suites bound in HIL library v1.1
def coord(tid, coordinate, family, band, desc, vtype, asset, rate):
    return {
        "task_id": tid, "benchmark_version": "UAB-0.1", "domain": "coordinate", "family": family,
        "target_coordinate": [coordinate],
        "difficulty": {"T_band": band},
        "human_intervention": {"budgets": ["H1"], "max_cid": 1},
        "mission": {"description": desc, "deliverables": ["structured judgment or state artifact", "evidence references"], "hazard_disclosed": True},
        "resources": {"wall_time_seconds": 1800, "model_calls": "declared", "web_access": False, "file_access": True},
        "authority": {"write_workspace": True, "send": False},
        "acceptance": {"locus_required": "a2_separated_process", "criterion_register_required": True, "sigma_bound": 0.0,
                       "required_success_rate": rate, "rho": 1.0, "hard_failures": ["self_report_without_grounded_state", "transcript_replay_as_memory"]},
        "verifier": {"type": vtype, "version": "HIL_Benchmark_Library_v1_1 starter", "hidden": True, "spec_key_test": False, "public_reference": asset},
        "retention": {"required_lower_level_suites": ["U0"]},
        "binding": {"status": "BOUND", "asset": asset, "note": "starter instance is a development example; hidden instances are required for formal certification"},
        "provenance": {"frozen_at": FROZEN, "source": "HIL Benchmark Library v1.1, bound rows", "hash": ""},
    }
for name, desc in [("restart_continuity", "Recover task and identity state after a genuine process restart and say where the state came from; long context and transcript replay do not count."),
                   ("temporal_order", "Preserve event ordering across sessions after a real restart."),
                   ("relevant_retrieval", "Select the relevant memory under heavy distractors after a real restart."),
                   ("provenance", "Trace every recalled claim to its source evidence after a real restart.")]:
    M.append(coord(f"uab-coordinate-t2-i1_{name}", "individual", f"I1 {name}", "T2", desc, "restart_probe", LIB + f"starter/instances/I-I1-{name.upper()[:12]}-A.json", 0.85))
for name, lvl, desc in [("identity_role", "SA1", "Report identity and role from machine-grounded state when textual cues are stale or conflicting."),
                        ("tool_reachability", "SA1", "Report which tools are reachable from grounded state, not from self-description."),
                        ("authority_limits", "SA2", "State authority limits before acting; escalate where the grounded state says the action is not permitted.")]:
    M.append(coord(f"uab-coordinate-t1-{lvl.lower()}_{name}", "self_awareness", f"{lvl} {name}", "T1", desc, "grounded_self_state", LIB + "data/task_catalog.csv#SA-" + lvl + "-" + name.upper()[:11] + "-A", 0.85))
for fam, band, rate in [("data_analysis", "T0", 0.95), ("document_workflow", "T0", 0.95), ("data_analysis", "T1", 0.9)]:
    m = coord(f"uab-coordinate-{band.lower()}-{fam}", "delegation", fam, band,
              f"Complete a {fam.replace('_', ' ')} task at {band} under an external verifier; delivery and verdict logged separately.",
              "independent_reference", LIB + f"starter/instances/DI-{band}-{fam.upper()[:8]}-A.json", rate)
    m["human_intervention"]["budgets"] = ["H0", "H1", "H2", "H3", "H4", "H5"]
    M.append(m)

OUT.mkdir(exist_ok=True)
for m in M:
    body = json.dumps({**m, "provenance": {**m["provenance"], "hash": ""}}, sort_keys=True, separators=(",", ":")).encode()
    m["provenance"]["hash"] = "sha256:" + hashlib.sha256(body).hexdigest()
    (OUT / (m["task_id"] + ".json")).write_text(json.dumps(m, indent=2) + "\n")
print(f"wrote {len(M)} manifests")
