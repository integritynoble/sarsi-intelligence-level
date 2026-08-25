#!/usr/bin/env python3
"""Refuse a delegation benchmark that cannot produce a delegation frontier.

`Difficulty_Is_Not_The_Index.md` states four repairs to the frontier as
propositions. This is the same content as a check, applied to a dataset file
rather than to a formalism, because a repair stated in a paper and absent from
the dataset is enforced by the diligence of whoever builds the next one.

    python3 tools/check_dli_bench.py dataset/dli_bench_tasks_v0_2.jsonl
    python3 tools/check_dli_bench.py --all
    python3 tools/check_dli_bench.py --self-test

Exit status 1 if anything fails. The checks are grouped by the repair they come
from, and each names the proposition it enforces so that a failure is traceable
to an argument rather than to a preference.

**The first group is the one that matters.** A benchmark can satisfy every field
requirement below and still be unable to report a frontier, because the frontier
is a maximum over a SET and a design in which each intervention budget reaches
one task band makes that set a point. That defect is invisible to per-row
validation — every row is well formed — and it is what v0.1 has.
"""

from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATASET = REPO / "dataset"

#: A frontier quoted at a budget needs at least this many bands under it, or the
#: maximum does not range over anything. Three is the minimum at which the word
#: "maximum" is doing work; it is not a statistical power claim.
MIN_BANDS_PER_BUDGET = 3

#: The budgets a published profile quotes. The framework's reporting form is
#: {F(H0,p), F(H1,p), F(H2,p)}, so these three must each be computable.
PROFILE_BUDGETS = ("H0", "H1", "H2")

#: The framework's eight difficulty coordinates. `risk` is the one v0.1 omits.
FRAMEWORK_COORDS = ("ambiguity", "horizon", "uncertainty", "tool_diversity",
                    "novelty", "verification", "coordination", "risk")

ADMISSIBLE_LOCI = ("a1_declared_test", "a2_separated_process",
                   "a3_independent_party")


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.notes: list[str] = []

    def __call__(self, name: str, ok: bool, detail: str = "") -> None:
        print(("  ok    " if ok else "  FAIL  ") + name +
              (("\n          " + detail) if detail and not ok else ""))
        if not ok:
            self.failures.append(name)

    def note(self, text: str) -> None:
        print("  note  " + text)
        self.notes.append(text)


def load(path: Path):
    rows = []
    for i, line in enumerate(path.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as e:
            raise SystemExit("%s:%d does not parse: %s" % (path, i, e))
    return rows


# ---------------------------------------------- A. the frontier is computable

def check_frontier_computable(rows, r: Report) -> None:
    """Repair 1, the structural half: max{T : S(T,h) >= p} over a real set.

    This is not a field check and cannot be made into one. It is a property of
    the DESIGN — of how the rows cover the (band, budget) grid — and a dataset
    every one of whose rows is perfect can fail it.
    """
    print("\nA. the frontier is a maximum over a set (Repair 1, structural)")
    byH = collections.defaultdict(set)
    for t in rows:
        byH[t.get("primary_intervention_budget")].add(t.get("task_band"))

    for h in PROFILE_BUDGETS:
        bands = sorted(x for x in byH.get(h, ()) if x)
        r("F(%s, p) ranges over >= %d bands" % (h, MIN_BANDS_PER_BUDGET),
          len(bands) >= MIN_BANDS_PER_BUDGET,
          "reaches %s — with fewer than %d, the maximum is a restatement of "
          "the design rather than a measurement"
          % (bands or "nothing", MIN_BANDS_PER_BUDGET))

    # The band must not BE the budget. If every band appears under exactly one
    # budget, then T and h are one variable and S(T,h) cannot vary in h.
    band_to_budgets = collections.defaultdict(set)
    for t in rows:
        band_to_budgets[t.get("task_band")].add(t.get("primary_intervention_budget"))
    crossed = [b for b, hs in band_to_budgets.items() if len(hs) >= 2]
    r("some band is tested under >= 2 budgets, so S(T,h) varies in h at fixed T",
      bool(crossed),
      "every band sits under exactly one budget: the intervention budget and "
      "the task band are the same variable wearing two names")


def check_non_closure_observable(rows, r: Report) -> None:
    """Repair 1, Propositions 1 and 2: kappa must vary within a band.

    If d_ver is a function of the band, the coordinates cannot disagree about
    the ordering, non-closure cannot occur, and the upward bias of Proposition 2
    is unidentifiable — hard-to-do and hard-to-check move together, so no
    observation separates them.
    """
    print("\nB. kappa is reported and varies (Repair 1, Propositions 1-2)")
    have_kappa = [t for t in rows if isinstance(t.get("kappa"), dict)]
    r("every task carries kappa = <verifiability, reversibility>",
      len(have_kappa) == len(rows),
      "%d of %d have no kappa block, so the two coordinates the band "
      "aggregates away are not recoverable"
      % (len(rows) - len(have_kappa), len(rows)))
    if not have_kappa:
        return

    cells = collections.defaultdict(set)
    for t in have_kappa:
        k = t["kappa"]
        cells[t.get("task_band")].add((k.get("verifiability"),
                                       k.get("reversibility")))
    multi = sorted(b for b, c in cells.items() if len(c) >= 2)
    r("some band carries >= 2 kappa cells, so Proposition 1 is testable",
      bool(multi),
      "kappa is a function of the band, so the coordinates cannot disagree "
      "about the ordering and non-closure cannot be observed")

    # The paper's own counterexample: a class near the BOTTOM of the difficulty
    # scale and near the bottom of what anyone will delegate.
    ce = [t for t in have_kappa
          if t.get("task_band") in ("T0", "T1")
          and (t["kappa"].get("reversibility") or 0) >= 4]
    r("a low-band, maximal-kappa class is represented",
      bool(ce),
      "the counterexample the repair is built on — send one external message, "
      "change a production value — has no representative, so the dataset "
      "cannot falsify the frontier it is built to measure")


# ------------------------------------------------------ C. failure is priced

def check_loss(rows, r: Report) -> None:
    """Repair 2: p* is the class's, not the evaluator's."""
    print("\nC. failure is priced (Repair 2, Proposition 3)")
    missing_risk = [t["task_id"] for t in rows
                    if "difficulty_risk" not in t]
    r("every task carries d_risk, the framework's eighth coordinate",
      not missing_risk,
      "%d task(s) have no cost-of-error coordinate, so rho has no inputs and "
      "Repair 2 cannot be applied at all: %s"
      % (len(missing_risk), missing_risk[:3]))

    have_loss = [t for t in rows if isinstance(t.get("loss"), dict)]
    r("every task carries a loss block",
      len(have_loss) == len(rows),
      "%d of %d have none" % (len(rows) - len(have_loss), len(rows)))

    if not have_loss:
        # Not a vacuous ok. A check whose subject is absent has not been
        # satisfied, it has not been run, and reporting it green is how an
        # absent property comes to look like a met one.
        r("p* = rho/(1+rho) on every task", False,
          "no task carries a loss block, so this check had nothing to run on. "
          "An absent property is not a satisfied one.")
        return

    bad = []
    for t in have_loss:
        L = t["loss"]
        rho, ps = L.get("rho"), L.get("p_star")
        if rho is None:
            if ps != 1.0:
                bad.append((t["task_id"], "unbounded rho but p* = %r" % ps))
            continue
        want = rho / (1.0 + rho)
        if ps is None or abs(want - ps) > 1e-3:
            bad.append((t["task_id"], "p* = %r, expected %.4f" % (ps, want)))
    r("p* = rho/(1+rho) on every task", not bad, str(bad[:3]))

    floor = [t for t in have_loss if t["loss"].get("p_star") == 1.0]
    if floor:
        r.note("%d class(es) at the irreversibility floor (p* = 1): %s. These "
               "are in the benchmark to be refused or escalated, not passed."
               % (len(floor), [t["task_id"] for t in floor][:3]))
    else:
        r.note("no class reaches p* = 1. That is a finding about the corpus, "
               "not a pass: a delegation benchmark with no irreversible class "
               "is silent about the classes people most need an answer for.")

    # The evaluator-chosen target must not be the operative one.
    live = [t["task_id"] for t in rows if "reliability_target" in t]
    r("no task carries a live evaluator-chosen reliability_target",
      not live,
      "%d task(s) still set p by hand; p is set by the class. Rename to "
      "reliability_target_v0_1 and derive p* from rho: %s"
      % (len(live), live[:3]))


# --------------------------------------------------- D. the acceptor is named

def check_acceptance(rows, r: Report) -> None:
    """Repair 3, Propositions 4 and 5."""
    print("\nD. the acceptor is a coordinate (Repair 3, Propositions 4-5)")
    have = [t for t in rows if isinstance(t.get("acceptance"), dict)]
    r("every task carries an acceptance block",
      len(have) == len(rows),
      "%d of %d have none, so a self-certified level and a measured one "
      "produce identical profiles" % (len(rows) - len(have), len(rows)))
    if not have:
        return

    bad_locus = [t["task_id"] for t in have
                 if t["acceptance"].get("locus_required") not in ADMISSIBLE_LOCI]
    r("every acceptance locus is admissible", not bad_locus, str(bad_locus[:3]))

    a0 = [t["task_id"] for t in have
          if "a0_performing_system" not in
          (t["acceptance"].get("locus_inadmissible") or ())]
    r("alpha0 is recorded as inadmissible, not merely omitted", not a0,
      "a field that lists only the allowed values refuses nothing: %s"
      % str(a0[:3]))

    noreg = [t["task_id"] for t in have
             if not t["acceptance"].get("criterion_register_required")]
    r("every task requires a criterion register written before the work",
      not noreg,
      "a criterion authored after the work is a criterion fitted to it: %s"
      % str(noreg[:3]))

    # Corollary 5.1 — the sharp one.
    top = [t for t in have if t.get("target_dl") in ("DL6", "DLΩ")]
    unbounded = [t["task_id"] for t in top
                 if (t["acceptance"].get("sigma_bound") is None
                     or t["acceptance"]["sigma_bound"] >= 1.0
                     or not t["acceptance"].get("sigma_bound_mechanism"))]
    r("no DL6/DLΩ task leaves sigma unbounded by structure (Corollary 5.1)",
      not unbounded,
      "sigma rises with the level by construction and reaches 1 at DLΩ. "
      "Without a structural bound these claims are UNMEASURABLE rather than "
      "hard to measure: %s" % str(unbounded[:3]))


# ------------------------------------------------------------ E. Rule 11

def check_rule_11(rows, r: Report, manifest=None) -> None:
    """Rule 11: verifier identity, phi or an explicit unknown, and the count of
    classes excluded for want of a criterion."""
    print("\nE. verifiability is a test condition (Rule 11)")
    have = [t for t in rows if isinstance(t.get("verifier"), dict)]
    r("every task carries a verifier block",
      len(have) == len(rows),
      "%d of %d have none" % (len(rows) - len(have), len(rows)))
    if have:
        nofp = [t["task_id"] for t in have
                if "false_pass_rate" not in t["verifier"]]
        r("every verifier declares a false-pass rate or an explicit unknown",
          not nofp,
          "an ABSENT key is not the same as a null one: null means unknown, "
          "absent means nobody considered it. %s" % str(nofp[:3]))
        unknown = sum(1 for t in have
                      if t["verifier"].get("false_pass_rate") is None)
        if unknown:
            r.note("%d of %d verifiers report phi as unknown. That is the "
                   "honest value and the common one, and it means every "
                   "frontier drawn from this set is an upper bound whose gap "
                   "is largest where d_ver is highest."
                   % (unknown, len(have)))

    if manifest is not None:
        exc = manifest.get("excluded_classes")
        r("the manifest records classes excluded for want of a criterion",
          isinstance(exc, list) and bool(exc),
          "where no external criterion exists S^V is UNDEFINED rather than "
          "small, so the class drops silently out of the maximum and the "
          "frontier reads high because of what is missing from it")


# ----------------------------------------------------------- F. the load term

def check_load(rows, r: Report) -> None:
    """Repair 4: L = r x (T_delta + c_i), and the two timestamps it needs."""
    print("\nF. load is observable (Repair 4)")
    have = [t for t in rows if isinstance(t.get("load_instrumentation"), dict)]
    r("every task declares its load instrumentation",
      len(have) == len(rows),
      "%d of %d have none" % (len(rows) - len(have), len(rows)))
    if not have:
        return
    missing_ts = [t["task_id"] for t in have
                  if not all(any(f.endswith(k) for f in
                                 t["load_instrumentation"].get(
                                     "required_episode_fields", ()))
                             for k in ("raised_at", "responded_at"))]
    r("every task requires the timestamp pair whose difference is T_delta",
      not missing_ts,
      "T_delta bounds the iteration rate of any governed loop, is a "
      "subtraction of two timestamps, and on the one deployed system examined "
      "for this corpus had never been recorded for want of a column: %s"
      % str(missing_ts[:3]))
    hcil = [t["task_id"] for t in rows if "hcil" in json.dumps(t).lower()]
    r("no task defines load as HCIL",
      not hcil,
      "HCIL's denominator is the effort a complete solution required — a "
      "counterfactual nobody performed: %s" % str(hcil[:3]))


# ---------------------------------------------------------------- the driver

def check_file(path: Path) -> int:
    rows = load(path)
    man = None
    guess = path.with_name(path.name.replace("tasks", "manifest")
                           .replace(".jsonl", ".json"))
    if guess.exists():
        man = json.loads(guess.read_text())

    print("\n%s — %d tasks%s"
          % (path.name, len(rows), "" if man else "  (no manifest alongside)"))
    r = Report()
    check_frontier_computable(rows, r)
    check_non_closure_observable(rows, r)
    check_loss(rows, r)
    check_acceptance(rows, r)
    check_rule_11(rows, r, man)
    check_load(rows, r)
    print("\n%d failed" % len(r.failures))
    return 1 if r.failures else 0


def self_test() -> int:
    """v0.1 must fail and v0.2 must pass.

    Both halves matter. A checker that only ever passes has not been shown to
    detect anything, and the defect it is built for is one every row survives.
    """
    ok = True
    v1, v2 = (DATASET / "dli_bench_tasks_v0_1.jsonl",
              DATASET / "dli_bench_tasks_v0_2.jsonl")
    if v1.exists():
        print("=" * 70 + "\nself-test: v0.1 is expected to FAIL\n" + "=" * 70)
        got = check_file(v1)
        print("\n-> v0.1 %s (expected fail)" % ("failed" if got else "PASSED"))
        ok = ok and got == 1
    if v2.exists():
        print("\n" + "=" * 70 + "\nself-test: v0.2 is expected to PASS\n" + "=" * 70)
        got = check_file(v2)
        print("\n-> v0.2 %s (expected pass)" % ("passed" if not got else "FAILED"))
        ok = ok and got == 0
    print("\n%s" % ("SELF-TEST PASSED" if ok else "SELF-TEST FAILED"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", type=Path)
    ap.add_argument("--all", action="store_true",
                    help="check every dli_bench_tasks_*.jsonl in dataset/")
    ap.add_argument("--self-test", action="store_true",
                    help="v0.1 must fail, v0.2 must pass")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    paths = list(a.paths)
    if a.all or not paths:
        paths = sorted(DATASET.glob("dli_bench_tasks_*.jsonl"))
    if not paths:
        raise SystemExit("no dataset files found under %s" % DATASET)
    return max(check_file(p) for p in paths)


if __name__ == "__main__":
    sys.exit(main())
