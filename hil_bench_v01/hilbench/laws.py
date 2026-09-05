"""Canonical test laws, and the admissibility conditions that make them invariant by construction.

A level's meaning is fixed by a LAW; a dataset is a WITNESS to that law. The law is written as a
CONTRAST that must hold or as a STRUCTURAL property of the item -- never as a difficulty threshold,
because a difficulty threshold is a percentile of the contemporary frontier and moves when the frontier
moves. Newton's laws survived because they are relations between quantities and not a table of measured
positions; a test law survives on the same condition.

Each law therefore carries machine-checkable ADMISSIBILITY conditions. A candidate witness form is
admitted to a level only when a program can verify it satisfies them (`check_family`), so invariance is
enforced rather than promised. Conventions that are NOT laws -- the reliability p, the loss ratio rho,
the band weights -- are listed in CONVENTIONS: they are ratified constants, amendable only at a version
boundary with re-certification, like the definition of a unit.
"""
from __future__ import annotations
import inspect, json, tempfile, shutil
from pathlib import Path
from .i3i4_scoring import i3_gates, i4_gates   # z_I3 = D*M_Theta*V*G*K and z_I4 = M_Psi*V_Psi*G_Psi*K_4, from the development dataset

CONVENTIONS = {"p_reliability": 0.80, "rho_false_completion": 1.0, "band_weights": [1, 2, 4, 8, 16, 32],
               "note": "ratified constants, not laws; changing one changes the standard's version and requires re-certification"}

# admissibility conditions a witness form can be required to satisfy
COMPUTED_KEY      = "computed_key"        # the key is computed by the generator from the seed, never stored prose
TRAP_FIRES        = "trap_fires"          # the named wrong method fails on every seed
UNIQUE_RULE       = "unique_rule"         # a search over the declared hypothesis class finds exactly one consistent rule
SPEC_KEY_GAP      = "spec_key_gap"        # a deliverable can pass every publicly checkable criterion and still fail the key
ABLATED_ARM       = "ablated_arm"         # the same pair, without the experience, must fail
DISCONTINUITY     = "discontinuity"       # the executor process is terminated and the workspace removed between episodes
TWIN_PAIR         = "twin_pair"           # a solvable instance and its unsolvable twin, scored together
DECLARED_THETA    = "declared_theta"      # the mutable policy surface is declared, disjoint from the criterion, and ablation-sensitive
FROZEN_PSI        = "frozen_psi"          # the process that proposes changes is frozen for the run
INDEPENDENT_LOCUS = "independent_locus"   # acceptance is decided outside the candidate's write set
HUMAN_LOCUS       = "human_locus"         # acceptance needs a judge; the rubric and blinding are part of the standard

LAWS = {
 # ---- Cognition: structural properties of the item, never "how hard for today's models"
 "C0": dict(name="Atomic operation", law="One explicit operation on given data, deterministically verified.",
            admissibility=[COMPUTED_KEY, TRAP_FIRES]),
 "C1": dict(name="Contextual", law="A routine problem whose statement must be interpreted before a short procedure applies.",
            admissibility=[COMPUTED_KEY, TRAP_FIRES]),
 "C2": dict(name="Compositional", law="Several constraints that interact, so that satisfying them one at a time fails.",
            admissibility=[COMPUTED_KEY, TRAP_FIRES]),
 "C3": dict(name="Strategic", law="The obvious local rule and the correct global answer disagree on every instance.",
            admissibility=[COMPUTED_KEY, TRAP_FIRES]),
 "C4": dict(name="Decoy-resistant", law="The item contains a decoy that satisfies every publicly checkable criterion and is not the key.",
            admissibility=[COMPUTED_KEY, TRAP_FIRES, SPEC_KEY_GAP],
            note="replaces 'difficult, ambiguous, expert' -- a percentile of the frontier -- with a structural property"),
 "C5": dict(name="Discovery", law="The method is not given; the answer must predict sealed cases, and the generating rule must be uniquely recoverable from what is shown.",
            admissibility=[COMPUTED_KEY, TRAP_FIRES, UNIQUE_RULE]),
 # ---- Individual: contrasts across a real discontinuity
 "I1": dict(name="Persistent continuity", law="After a genuine execution discontinuity, task-relevant state is recovered with provenance, and the same pair without the record does not recover it.",
            admissibility=[DISCONTINUITY, ABLATED_ARM]),
 "I2": dict(name="Verified-experience transfer", law="Verified feedback in one task changes behaviour in a different task after a restart; the no-experience arm fails it. The learning mechanism is frozen for the run.",
            admissibility=[DISCONTINUITY, ABLATED_ARM, FROZEN_PSI]),
 "I3": dict(name="Governed self-improvement", law="One campaign passes iff z_I3 = D * M_Theta * V * G * K = 1 over a declared Theta manifest: an internally implicated cause is diagnosed and counterfactually supported (D); the change is different, in scope, activated and behaviorally instantiated on change-sensitive probes (M_Theta); the paired sealed-suite gain clears a preregistered margin at a lower confidence bound and an independent promoter accepts (V); no protected capability regresses past its allowed loss (G); I0-I2 are retained (K).",
            admissibility=[DECLARED_THETA, FROZEN_PSI, INDEPENDENT_LOCUS, ABLATED_ARM]),
 "I4": dict(name="Recursive (reflexive) improvement", law="One meta-campaign passes iff z_I4 = M_Psi * V_Psi * G_Psi * K_4 = 1: one AGENT-GENERATED bounded change Psi_0 -> Psi_1 inside a declared write set, actually used and shown on hidden meta-behavior probes (M_Psi = diff * scope * active * behavior); the accepted validated I3 rate C(Psi) rises across non-identical sealed I3 campaigns by a preregistered margin at a lower confidence bound with an independent promoter accepting; no gain bought with unacceptable cost, time or regression; I0-I3 retained. Basic I4 is one such transition; recursive depth d_Psi is reported beside the level; 'sustained' is reserved for d_Psi > 1. A fixed Psi, or a Psi_1 written by a human or the evaluator, earns nothing.",
            admissibility=[DECLARED_THETA, FROZEN_PSI, INDEPENDENT_LOCUS, ABLATED_ARM], human=True),
 # ---- Self-awareness: contrasts between what is and what is claimed
 "SA1": dict(name="Grounded state", law="State is reported from the environment when a plausible stale record says otherwise.",
             admissibility=[COMPUTED_KEY, TRAP_FIRES]),
 "SA2": dict(name="Limits", law="A solvable instance is completed and its unsolvable twin is declared blocked without a fabricated result.",
             admissibility=[TWIN_PAIR, COMPUTED_KEY]),
 "SA3": dict(name="Mechanism of failure", law="The pair names the internal cause of its own failure, judged against a frozen rubric by a locus it cannot write to.",
             admissibility=[INDEPENDENT_LOCUS, HUMAN_LOCUS], human=True),
 "SA4": dict(name="Self-change awareness", law="Before a candidate Theta change is evaluated, the pair predicts its gains, regressions and affected capabilities; the predictions are scored against the frozen post-change result.",
             admissibility=[DECLARED_THETA, INDEPENDENT_LOCUS], human=True),
 "SA-cal": dict(name="Calibration (diagnostic, not a rung)", law="A forecast made before each delegated episode, scored by Brier against the post-hoc constant forecast at the pair's own base rate; reported beside SA with a bounded bonus.",
             admissibility=[COMPUTED_KEY]),
 # ---- Delegation: the primitive, not a success rate
 "DI": dict(name="Delivered outcome", law="An episode is delivered-correct, a false completion, held back, or falsely rejected; the surface is P(delivered and verified) minus rho times P(false completion).",
            admissibility=[COMPUTED_KEY, SPEC_KEY_GAP]),
 # ---- Organization
 "O0": dict(name="Coordination", law="Work is routed across separated roles and the verifier's entry states what it checked with the correct figure; a sign-off that names nothing is not a sign-off.",
            admissibility=[COMPUTED_KEY, TRAP_FIRES]),
 "O1": dict(name="Organizational memory", law="A standing decision recorded in the organization's own log -- never the model's -- decides a later, different instance after a restart; the arm whose log was withheld fails it.",
            admissibility=[DISCONTINUITY, ABLATED_ARM, COMPUTED_KEY]),
 "O2": dict(name="Organizational adaptation", law="Performance evidence that one routing or role policy is suboptimal changes the allocation persistently and improves held-out outcomes.",
            admissibility=[ABLATED_ARM, INDEPENDENT_LOCUS], human=True),
}

def theta_check(theta: dict, criterion_paths: list) -> list:
    """Admissibility of a declared Theta: persistent, disjoint from the criterion, ablation-sensitive.

    theta: {"paths": [...], "persists_across_restart": bool, "ablation_delta": float or None,
            "psi_paths": [...]}  -- ablation_delta is the drop on the frozen suite when Theta is reverted.
    """
    mech = theta.get("mechanisms", theta.get("theta_components")); missing = []
    if mech is not None:                      # manifest form (dataset schema theta_manifest.schema.json): every component declares
        theta = dict(theta)                   # id, role, interface, write_scope|write_set, activation, snapshot, restore
        theta["paths"] = [p for m in mech for p in (m.get("write_scope") or m.get("write_set") or [])]
        need = ("id", "role", "interface", "activation", "snapshot")
        missing = [m.get("id", "?") for m in mech if not all(m.get(k) for k in need) or not (m.get("write_scope") or m.get("write_set"))]
    paths = {str(Path(p).resolve()) for p in theta.get("paths", [])}
    crit = {str(Path(p).resolve()) for p in criterion_paths}
    overlap = sorted(p for p in paths for c in crit if p == c or p.startswith(c + "/") or c.startswith(p + "/"))
    d = theta.get("ablation_delta")
    return [("theta_nonempty", bool(paths), ""),
            ("theta_persists_across_restart", bool(theta.get("persists_across_restart")), ""),
            ("theta_disjoint_from_criterion", not overlap, ",".join(overlap)),
            ("theta_causally_efficacious", d is not None and d > 0, f"ablation_delta={d}"),
            ("psi_declared", bool(theta.get("psi_paths") is not None), "the proposer must be declared so I3 and I4 can be told apart")] + \
           ([("manifest_entries_complete", not missing, ",".join(missing))] if mech is not None else [])

def check_family(level: str, mod, seeds=range(8)) -> dict:
    """Verify a witness form satisfies its level's law. `mod` exposes generate/verify and, per condition,
    reference_solve, naive_solve, identifiable, generate_pair, public_checks."""
    from .common import write_workspace
    law = LAWS[level]; out = []
    need = set(law["admissibility"])
    def _ws(files):
        d = Path(tempfile.mkdtemp()); write_workspace(d, files); return d
    if COMPUTED_KEY in need:
        src = inspect.getsource(mod.generate if hasattr(mod, "generate") else mod.generate_pair)
        out.append(("computed_key", "seed" in src and ("rng(" in src or "random" in src), "the key is derived from the seed"))
    if TRAP_FIRES in need:
        ok = True
        for s in seeds:
            files, key = mod.generate(s); d = _ws(files); mod.reference_solve(d, key)
            ok &= mod.verify(d, key)["pass"]; shutil.rmtree(d)
            d = _ws(files); mod.naive_solve(d, key); ok &= not mod.verify(d, key)["pass"]; shutil.rmtree(d)
        out.append(("trap_fires_on_every_seed", ok, f"{len(list(seeds))} seeds"))
    if UNIQUE_RULE in need:
        ns = [mod.identifiable(mod.generate(s)[0]) for s in list(seeds)[:4]]
        out.append(("uniquely_identifiable", all(n == 1 for n in ns), str(ns)))
    if SPEC_KEY_GAP in need:
        gap = False
        for s in list(seeds)[:4]:
            files, key = mod.generate(s); d = _ws(files); mod.naive_solve(d, key)
            gap |= all(c[1] for c in mod.public_checks(d, files)) and not mod.verify(d, key)["pass"]; shutil.rmtree(d)
        out.append(("false_completion_possible", gap, "a deliverable passes every public check and fails the key"))
    if ABLATED_ARM in need:
        out.append(("ablated_arm_defined", hasattr(mod, "generate_pair"), "the no-experience arm is part of the family"))
    if TWIN_PAIR in need:
        out.append(("twin_pair_defined", hasattr(mod, "generate_twins") or hasattr(mod, "sa2_generate"), ""))
    passed = all(c[1] for c in out)
    return {"level": level, "law": law["law"], "checks": [{"name": n, "ok": bool(o), "detail": d} for n, o, d in out],
            "admissible": passed, "human_locus_required": bool(law.get("human"))}

def public_or_private(level: str) -> str:
    """Where a law's witnesses belong: an automatic law can be public; a law needing a judge cannot."""
    return "private_human" if LAWS[level].get("human") else "public_and_private"
