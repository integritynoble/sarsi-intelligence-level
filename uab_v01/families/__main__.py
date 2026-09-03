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
