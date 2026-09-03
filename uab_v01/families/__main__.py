"""CLI for the in-package families.

  python3 -m families gen      <family> --seed N --out DIR      write workspace to DIR and key to DIR.key.json
  python3 -m families verify   <family> --ws DIR --key FILE    print the verdict JSON
  python3 -m families speckey  <family> --seeds 0-11           run the specification-key test
  python3 -m families selftest [--seeds 0-11]                  reference passes, naive fails, per family
"""
from __future__ import annotations
import argparse, json, shutil, sys, tempfile
from pathlib import Path
from . import FAMILIES
from .common import write_workspace

def seeds_of(s: str):
    if "-" in s:
        a, b = s.split("-"); return list(range(int(a), int(b) + 1))
    return [int(x) for x in s.split(",")]

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="families")
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("gen"); g.add_argument("family"); g.add_argument("--seed", type=int, default=0); g.add_argument("--out", required=True)
    v = sub.add_parser("verify"); v.add_argument("family"); v.add_argument("--ws", required=True); v.add_argument("--key", required=True)
    k = sub.add_parser("speckey"); k.add_argument("family"); k.add_argument("--seeds", default="0-11")
    t = sub.add_parser("selftest"); t.add_argument("--seeds", default="0-11")
    a = ap.parse_args(argv)
    if a.cmd == "gen":
        files, key = FAMILIES[a.family].generate(a.seed)
        out = Path(a.out); write_workspace(out, files)
        Path(str(out) + ".key.json").write_text(json.dumps(key, indent=1))
        print(f"workspace {out}; key {out}.key.json (keep outside the executor's reach)"); return 0
    if a.cmd == "verify":
        key = json.load(open(a.key)); r = FAMILIES[a.family].verify(Path(a.ws), key)
        print(json.dumps(r, indent=1)); return 0 if r["pass"] else 1
    if a.cmd == "speckey":
        for s in seeds_of(a.seeds): FAMILIES[a.family].spec_key_check(s)
        print(f"{a.family}: specification and key agree on seeds {a.seeds}"); return 0
    if a.cmd == "selftest":
        failures = 0
        from . import learning_t2
        seeds = seeds_of(a.seeds); learned = fresh_fail = 0
        for s in seeds:
            learning_t2.spec_key_check(s)
            fa, fb, key = learning_t2.generate_pair(s)
            da, db = Path(tempfile.mkdtemp()), Path(tempfile.mkdtemp()); write_workspace(da, fa); write_workspace(db, fb)
            learning_t2.reference_solve_a(da, None)                       # attempt 1: default reading
            assert not learning_t2.verify_a(da, key)["pass"], "attempt 1 should fail under the default reading"
            (da / "FEEDBACK.md").write_text(learning_t2.feedback(key))
            conv = learning_t2.lesson_from_feedback(da)
            learning_t2.reference_solve_a(da, conv); a2 = learning_t2.verify_a(da, key)["pass"]
            learning_t2.reference_solve_b(db, conv); b_learned = learning_t2.verify_b(db, key)["pass"]   # carried the lesson
            learning_t2.reference_solve_b(db, None); b_fresh = learning_t2.verify_b(db, key)               # ablated: default reading
            learned += a2 and b_learned; fresh_fail += (not b_fresh["pass"]) and b_fresh["failure_mode"] == "default_reading_no_transfer"
            shutil.rmtree(da); shutil.rmtree(db)
        ok = learned == len(seeds) and fresh_fail == len(seeds); failures += 0 if ok else 1
        print(f"{'learning_t2':12s} learned   {learned}/{len(seeds)} pass  ablated {fresh_fail}/{len(seeds)} fail  spec-key ok  -> {'OK' if ok else 'FAIL'}")
        from . import selfimprove_t3
        okc = 0
        for s in seeds:
            selfimprove_t3.spec_key_check(s); r = selfimprove_t3.selftest(s); okc += r["ok"]
            if not r["ok"]: print("   selfimprove_t3 seed", s, r["decisions"])
        ok = okc == len(seeds); failures += 0 if ok else 1
        print(f"{'selfimprove_t3':12s} promoter  {okc}/{len(seeds)} seeds sort good/overfit/regressing/nochange correctly  spec-key ok  -> {'OK' if ok else 'FAIL'}")
        for name, mod in FAMILIES.items():
            ref_pass = naive_fail = 0; seeds = seeds_of(a.seeds)
            for s in seeds:
                mod.spec_key_check(s)
                for solver, expect in ((mod.reference_solve, True), (mod.naive_solve, False)):
                    d = Path(tempfile.mkdtemp()); files, key = mod.generate(s); write_workspace(d, files)
                    solver(d); r = mod.verify(d, key); shutil.rmtree(d)
                    if expect and r["pass"]: ref_pass += 1
                    if not expect and not r["pass"]: naive_fail += 1
            ok = ref_pass == len(seeds) and naive_fail == len(seeds)
            failures += 0 if ok else 1
            print(f"{name:12s} reference {ref_pass}/{len(seeds)} pass  naive {naive_fail}/{len(seeds)} fail  spec-key ok  -> {'OK' if ok else 'FAIL'}")
        return 1 if failures else 0
    return 2

if __name__ == "__main__":
    sys.exit(main())
