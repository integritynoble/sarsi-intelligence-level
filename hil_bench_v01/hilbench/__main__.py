import argparse, json, os, sys
from pathlib import Path
from . import split, core

def main():
    ap = argparse.ArgumentParser(prog="hilbench"); sub = ap.add_subparsers(dest="cmd", required=True)
    for m in ("agent", "llm"):
        p = sub.add_parser(m); p.add_argument("--label", required=True); p.add_argument("--exec", required=True); p.add_argument("--root", required=True)
        p.add_argument("--split", choices=("public", "private"), default="public"); p.add_argument("--salt-file", default=None); p.add_argument("--limit", type=int, default=300)
    e = sub.add_parser("extended"); e.add_argument("--label", required=True); e.add_argument("--exec", required=True); e.add_argument("--root", required=True)
    e.add_argument("--ai4science", default="/home/spiritai/pwm/Physics_World_Model/AI4Science"); e.add_argument("--split", choices=("public", "private"), default="public"); e.add_argument("--salt-file", default=None)
    m = sub.add_parser("m1"); m.add_argument("--root", required=True); m.add_argument("--exec", required=True); m.add_argument("--limit", type=int, default=300); m.add_argument("--tag", default="r2")
    c = sub.add_parser("commit-private"); c.add_argument("--salt-file", required=True)
    s = sub.add_parser("selftest")
    a = ap.parse_args()
    if a.cmd == "commit-private":
        salt = Path(a.salt_file).read_bytes(); split.COMMITMENT_FILE.write_text(json.dumps({"commitment": split.commitment(salt), "n_private_seeds": 4, "derivation": "HMAC-SHA256(salt, 'hilbench:i')[:4] mod 1e6 + 1000"}, indent=1))
        print("commitment written:", split.commitment(salt)); return 0
    if a.cmd == "selftest":
        from . import c_items, sa_probes, m1_restart
        for s in range(12): c_items.spec_key_check(s)
        for s in range(12):
            f, k = sa_probes.sa1_generate(s); assert set(k["real"]).isdisjoint(k["stale"])
            so, bl, k2 = sa_probes.sa2_generate(s); assert "ledger-export" in bl["GOAL.md"] and "data.csv" in so
            fa, fb, k3 = m1_restart.generate_pair(s); assert k3["code_name"] in fa["GOAL.md"] and k3["code_name"] not in fb["GOAL.md"]
        from . import hard, harness
        from .common import write_workspace
        import tempfile
        print(hard.selftest(range(12)))
        for name in hard.ITEMS:                                  # the specification-key gap, item by item
            gen, ver, solve, naive, _ = hard.ITEMS[name]
            f, k = gen(0); d = Path(tempfile.mkdtemp()); write_workspace(d, f); naive(d, k)
            pub = all(c[1] for c in harness.public_checks(name, d, f))
            assert not ver(d, k)["pass"], (name, "trap did not fire")
            print(f"  {name}: named wrong method -> public checks {'pass' if pub else 'FAIL'}, hidden verifier FAIL"
                  f"{'  (a false completion the harness cannot catch)' if pub else '  (the harness catches this one)'}")
        print("selftest ok: c_items 4 bands x 12 seeds (reference passes, naive fails); sa1/sa2/m1 generators consistent"); return 0
    seeds = split.PUBLIC_SEEDS if getattr(a, "split", "public") == "public" else split.private_seeds(Path(a.salt_file).read_bytes())
    if getattr(a, "split", "public") == "private": assert split.check_commitment(Path(a.salt_file).read_bytes()), "salt does not match the published commitment"
    if a.cmd == "m1":
        core.rerun_m1(Path(a.root), a.exec, a.limit, tag=a.tag); return 0
    if a.cmd == "extended":
        core.run_extended(a.label, a.exec, Path(a.root), seeds, a.ai4science); return 0
    fn = core.run_agent if a.cmd == "agent" else core.run_llm
    fn(a.label, a.exec, Path(a.root), seeds, a.limit)
    return 0

if __name__ == "__main__":
    sys.exit(main())
