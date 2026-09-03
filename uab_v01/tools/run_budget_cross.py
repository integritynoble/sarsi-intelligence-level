#!/usr/bin/env python3
"""Budget-cross runs: the bound in-package families at H0, H1 and H2, same seeds at every budget.

  python3 tools/run_budget_cross.py --seeds 0-3 --root DIR --exec 'claude -p {prompt} ...'

Budgets (policies/INTERVENTION_POLICY.md), implemented by an intervention oracle that stands in for the
human logger and is declared as such:
  H0  one invocation; no questions. A QUESTION.md with no deliverable is recorded as held back.
  H1  the executor may write ONE narrow question to QUESTION.md and stop; the oracle answers ONLY by
      restating the disclosed specification (CID1) or says no further information is available; one
      more invocation follows.
  H2  as H1, and after a failed first delivery the oracle writes CORRECTION.md naming the failed check
      and nothing else (CID2, a local correction, no strategy); one more invocation follows.
Zero-intervention rule: an H1 or H2 episode that raised no intervention is ALSO reported at H0.
Every invocation runs in its own process group under an enforced limit; termination reason recorded.
"""
from __future__ import annotations
import argparse, json, os, shlex, signal, shutil, subprocess, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from families import FAMILIES
from families.common import write_workspace

BANDS = {"code_t0": "T0", "funding_t0": "T0", "job_t0": "T0", "paper_t0": "T0", "business_t0": "T0", "paper_t1": "T1"}
FAQ = {  # the only answers the oracle may give: restatements of the disclosed specification
    "code_t0": "Change exactly the one line named in GOAL.md, in config.py only. Every other file must remain byte-identical.",
    "funding_t0": "The field definitions in GOAL.md are complete: the full-proposal deadline is the sponsor's full-proposal due date, not the LOI, start or internal date; verbatim fields are copied from their labelled line; the budget cap is digits only.",
    "job_t0": "Only bullets under the heading 'Required qualifications' are required, whatever order the lists appear in; the location is the text after 'Location:' without the label.",
    "paper_t0": "Compare exactly four fields for the named citation only: first author's surname, year, venue name, page range in order. 'consistent' is true only when the discrepancy list is empty.",
    "business_t0": "The definitions in GOAL.md are complete: use the restated figure, the end-of-2025 figure, the latest round, the company's own founding year, the Q4 ARR; value is digits only; source_line is the whole line, verbatim.",
    "paper_t1": "Report only the named dataset; rank by the stated direction; the margin is the absolute difference rounded as stated; state no number that is not in evidence.json or the margin.",
}
T = ("Read GOAL.md in this directory and do exactly what it says, creating or editing files in this directory. "
     "Do not ask questions. Reply DONE when finished.")
T_Q = ("Read GOAL.md in this directory and do exactly what it says, creating or editing files in this directory. "
       "If, and only if, ONE narrow clarification about the task text would change what you deliver, write that single question "
       "to QUESTION.md and stop without delivering; otherwise complete the task. Reply DONE when finished.")
T_A = "ANSWER.md in this directory answers your question. Now read GOAL.md and complete the task. Reply DONE when finished."
T_C = "CORRECTION.md in this directory names the acceptance check your delivery failed. Read GOAL.md again, correct your delivery, and reply DONE."

def run(cmd_tmpl, prompt, cwd, limit):
    cmd = shlex.split(cmd_tmpl.replace("{prompt}", shlex.quote(prompt))); t0 = time.time()
    p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
    try: p.communicate(timeout=limit); reason = "normal" if p.returncode == 0 else "crashed"
    except subprocess.TimeoutExpired: os.killpg(p.pid, signal.SIGKILL); p.communicate(); reason = "timed_out"
    return {"exit": p.returncode, "termination_reason": reason, "seconds": round(time.time() - t0, 1)}

def deliverable_present(fam, ws):
    names = {"code_t0": "config.py", "funding_t0": "answer.json", "job_t0": "requirements.json", "paper_t0": "citation_check.json",
             "business_t0": "fact.json", "paper_t1": "results_section.md"}
    return (ws / names[fam]).exists()

def episode(fam, mod, seed, budget, exec_tmpl, root, limit):
    ws = root / f"{fam}_s{seed}_{budget}"; files, key = mod.generate(seed); write_workspace(ws, files)
    if fam == "code_t0": (ws / ".snapshot_ok").write_text("")   # config.py exists before the edit; delivery = modified
    interventions, invocations = [], []
    invocations.append(run(exec_tmpl, T if budget == "H0" else T_Q, ws, limit))
    q = ws / "QUESTION.md"
    if q.exists() and budget in ("H1", "H2"):
        (ws / "ANSWER.md").write_text(FAQ[fam] + "\nNo further information is available.\n")
        interventions.append({"kind": "clarification", "cid": 1, "question": q.read_text()[:300]})
        invocations.append(run(exec_tmpl, T_A, ws, limit))
    v = mod.verify(ws, key)
    if budget == "H2" and not v["pass"] and deliverable_present(fam, ws):
        failed = [c["name"] for c in v["checks"] if not c["ok"]]
        (ws / "CORRECTION.md").write_text("Your delivery failed the acceptance check named: " + ", ".join(failed) + ".\n")
        interventions.append({"kind": "local_correction", "cid": 2, "check": failed})
        invocations.append(run(exec_tmpl, T_C, ws, limit)); v = mod.verify(ws, key)
    delivered = deliverable_present(fam, ws) if fam != "code_t0" else True
    if q.exists() and budget == "H0": delivered = delivered and not (ws / "QUESTION.md").exists() or delivered
    outcome = "delivered_correct" if v["pass"] else ("held_back" if (not delivered or (q.exists() and budget == "H0" and not v["pass"])) else "false_completion")
    rec = {"family": fam, "band": BANDS[fam], "seed": seed, "budget": budget, "pass": v["pass"], "outcome": outcome,
           "interventions": interventions, "max_cid": max([i["cid"] for i in interventions], default=0),
           "invocations": invocations, "termination_reason": invocations[-1]["termination_reason"],
           "seconds": round(sum(i["seconds"] for i in invocations), 1), "failure_mode": v["failure_mode"], "accuracy": v["accuracy"],
           "reported_at": budget if interventions or budget == "H0" else "H0"}
    shutil.rmtree(ws); return rec

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--seeds", default="0-3"); ap.add_argument("--root", required=True)
    ap.add_argument("--exec", required=True); ap.add_argument("--limit", type=int, default=300); ap.add_argument("--families", default=",".join(BANDS))
    a = ap.parse_args(); lo, hi = a.seeds.split("-"); seeds = range(int(lo), int(hi) + 1)
    root = Path(a.root).resolve(); root.mkdir(parents=True, exist_ok=True); out = root / "episodes.jsonl"
    with open(out, "a") as f:
        for fam in a.families.split(","):
            for seed in seeds:
                for budget in ("H0", "H1", "H2"):
                    rec = episode(fam, FAMILIES[fam], seed, budget, a.exec, root, a.limit)
                    f.write(json.dumps(rec) + "\n"); f.flush()
                    print(f"{fam:12s} s{seed} {budget}: {'pass' if rec['pass'] else 'FAIL':4s} {rec['outcome']:17s} interventions={len(rec['interventions'])} cid={rec['max_cid']} {rec['seconds']}s", flush=True)
    print("ALLDONE")

if __name__ == "__main__":
    main()
