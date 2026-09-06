"""HIL-Bench command line.

  selftest        offline: generators, computed keys, reference solvers, named traps, law admissibility
  agent           measure a frozen model-harness pair as it is (--with-o adds the organizational suite)
  llm             measure a BARE model in every coordinate at HG0/HG1/HG2 (OpenAI-compatible endpoint)
  llm-harness     the reference ladder with an agent executor as the inner loop (how the first readings were taken)
  extended        T2-T5 generator families, bare, appended to an agent's delegation surface
  m1              re-run the M1 phase of an existing agent record after an item repair
  commit-private  publish only sha256(salt) for the private split
"""
from __future__ import annotations
import argparse, json, os, sys
from pathlib import Path
from typing import Sequence
from . import split, core

def _parse_seed_spec(value: str) -> list[int]:
    """'0-2,7,9-10' -> [0,1,2,7,9,10]."""
    seeds: list[int] = []
    try:
        for part in value.split(","):
            part = part.strip()
            if not part: continue
            if "-" in part[1:]:
                i = part.find("-", 1); a, b = int(part[:i]), int(part[i + 1:])
                if b < a: raise ValueError("range end precedes range start")
                seeds.extend(range(a, b + 1))
            else: seeds.append(int(part))
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid seed specification {value!r}: {exc}") from exc
    if not seeds: raise argparse.ArgumentTypeError("at least one seed is required")
    return seeds

def _selected_seeds(split_name: str, salt_file: str | None) -> list[int]:
    if split_name == "public": return list(split.PUBLIC_SEEDS)
    if not salt_file: raise ValueError("--salt-file is required for the private split")
    salt = Path(salt_file).read_bytes()
    if not salt: raise ValueError("the private salt file is empty")
    if not split.check_commitment(salt): raise ValueError("private salt does not match the published commitment")
    return split.private_seeds(salt)

def _run_selftest(seeds: Sequence[int], verbose=True) -> dict:
    from . import c_items, sa_probes, m1_restart, o_families, hard, harness, laws, score
    from .common import write_workspace
    import tempfile
    n = 0
    for s in seeds:
        c_items.spec_key_check(s); n += len(c_items.BANDS)
        for fam in core.TH: core.UAB_FAMILIES[fam].spec_key_check(s); n += 1
        f, k = sa_probes.sa1_generate(s); assert set(k["real"]).isdisjoint(k["stale"]) and set(k["real"]).issubset(f)
        so, bl, _ = sa_probes.sa2_generate(s); assert "data.csv" in so and "data.csv" not in bl and "ledger-export" in bl["GOAL.md"]
        fa, fb, k3 = m1_restart.generate_pair(s); assert k3["code_name"] in fa["GOAL.md"] and k3["code_name"] not in fb["GOAL.md"]
        o_families.o0_spec_key(s); o_families.o1_spec_key(s); n += 2
    if verbose: print(hard.selftest(range(12)))
    else: hard.selftest(range(min(4, len(seeds)) or 1))
    for name in hard.ITEMS:                                   # the specification-key gap, item by item
        gen, ver, _solve, naive, _ = hard.ITEMS[name]
        f, k = gen(0); d = Path(tempfile.mkdtemp()); write_workspace(d, f); naive(d, k)
        pub = all(c[1] for c in harness.public_checks(name, d, f)); assert not ver(d, k)["pass"], (name, "trap did not fire")
        if verbose: print(f"  {name}: named wrong method -> public checks {'pass' if pub else 'FAIL'}, hidden verifier FAIL"
                          f"{'  (a false completion the harness cannot catch)' if pub else '  (the harness catches this one)'}")
    if verbose:
        for name, lvl in hard.WITNESS_LEVEL.items():           # the law, checked rather than promised
            r = laws.check_family(lvl, hard._Witness(name), range(6))
            assert r["admissible"], (name, lvl, [c for c in r["checks"] if not c["ok"]])
            print(f"  {name}: admissible witness for {lvl} -- " + ", ".join(c["name"] for c in r["checks"]))
    assert score.c_level([{"band": b, "pass": True} for b in ("C0", "C1", "C2", "C3")]) == "C3"
    assert score.frontier([{"band": "T0", "budget": "H0", "delivered_correct": True}, {"band": "T1", "budget": "H0", "delivered_correct": False},
                           {"band": "T2", "budget": "H0", "delivered_correct": True}]) == "T0"
    salt = b"hilbench-selftest-salt"; assert split.private_seeds(salt) == split.private_seeds(salt)
    assert set(split.PUBLIC_SEEDS).isdisjoint(split.private_seeds(salt))
    return {"status": "ok", "offline": True, "seeds": list(seeds), "spec_key_checks": n, "model_calls": 0}

def _build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="hilbench", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    st = sub.add_parser("selftest"); st.add_argument("--seeds", type=_parse_seed_spec, default=list(range(12))); st.add_argument("--quiet", action="store_true")
    def common(p, limit):
        p.add_argument("--label", required=True); p.add_argument("--root", type=Path, required=True, help="fresh output directory")
        p.add_argument("--limit", type=int, default=limit); p.add_argument("--split", choices=("public", "private"), default="public"); p.add_argument("--salt-file")
    a = sub.add_parser("agent"); a.add_argument("--exec", dest="executor", required=True, help="command template containing {prompt}"); common(a, 300)
    a.add_argument("--with-o", action="store_true", help="also run the organizational suite (O0 routing, O1 org-memory with ablated arm)")
    l = sub.add_parser("llm"); common(l, 120); l.add_argument("--api", choices=("openai", "anthropic"), default="openai"); l.add_argument("--seeds-per-family", type=int, default=2)
    ix = sub.add_parser("index", help="the HIL Index: one number per bare model over the reference ladder, three seeds per family"); common(ix, 120)
    ix.add_argument("--api", choices=("openai", "anthropic"), default="openai"); ix.add_argument("--seeds-per-family", type=int, default=3)
    ix.add_argument("--base", default=os.environ.get("HILBENCH_LLM_BASE")); ix.add_argument("--key", default=os.environ.get("HILBENCH_LLM_KEY")); ix.add_argument("--model", default=os.environ.get("HILBENCH_LLM_MODEL"))
    l.add_argument("--base", default=os.environ.get("HILBENCH_LLM_BASE")); l.add_argument("--key", default=os.environ.get("HILBENCH_LLM_KEY")); l.add_argument("--model", default=os.environ.get("HILBENCH_LLM_MODEL"))
    lh = sub.add_parser("llm-harness"); lh.add_argument("--exec", dest="executor", required=True); common(lh, 300)
    e = sub.add_parser("extended"); e.add_argument("--exec", dest="executor", required=True); common(e, 0)
    e.add_argument("--ai4science", default="/home/spiritai/pwm/Physics_World_Model/AI4Science")
    m = sub.add_parser("m1"); m.add_argument("--root", type=Path, required=True); m.add_argument("--exec", dest="executor", required=True); m.add_argument("--limit", type=int, default=300); m.add_argument("--tag", default="r2")
    om = sub.add_parser("o"); om.add_argument("--root", type=Path, required=True); om.add_argument("--exec", dest="executor", required=True); om.add_argument("--limit", type=int, default=300); om.add_argument("--tag", default="o2")
    g = sub.add_parser("gating", help="append episodes at the gating band to an existing record and re-finalize")
    g.add_argument("--root", type=Path, required=True); g.add_argument("--exec", dest="executor", default=None); g.add_argument("--limit", type=int, default=300)
    g.add_argument("--split", choices=("public", "private"), default="public"); g.add_argument("--salt-file"); g.add_argument("--band", default=None)
    g.add_argument("--base", default=os.environ.get("HILBENCH_LLM_BASE")); g.add_argument("--key", default=os.environ.get("HILBENCH_LLM_KEY")); g.add_argument("--model", default=os.environ.get("HILBENCH_LLM_MODEL"))
    i5 = sub.add_parser("i5", help="run the I5-DISC development campaign on the cancer field agent"); i5.add_argument("--label", required=True); i5.add_argument("--exec", dest="executor", required=True); i5.add_argument("--root", type=Path, required=True)
    i5.add_argument("--limit-a", type=int, default=1800); i5.add_argument("--limit-b", type=int, default=600)
    i5t = sub.add_parser("i5-transfer", help="re-run only the transfer arms of a validated I5 campaign, restoring the pair's own staged note as project memory"); i5t.add_argument("--root", type=Path, required=True); i5t.add_argument("--exec", dest="executor", required=True); i5t.add_argument("--limit-b", type=int, default=600); i5t.add_argument("--staged-from", type=Path, default=None)
    c = sub.add_parser("commit-private"); c.add_argument("--salt-file", required=True)
    return ap

def main(argv: Sequence[str] | None = None) -> int:
    ap = _build_parser(); a = ap.parse_args(argv)
    if a.cmd == "selftest":
        r = _run_selftest(a.seeds, verbose=not a.quiet); print(json.dumps(r) if a.quiet else "selftest ok: " + json.dumps(r)); return 0
    if a.cmd == "commit-private":
        salt = Path(a.salt_file).read_bytes()
        split.COMMITMENT_FILE.write_text(json.dumps({"commitment": split.commitment(salt), "n_private_seeds": 4,
                                                      "derivation": "HMAC-SHA256(salt, 'hilbench:i')[:4] as int mod 1e6 + 1000, i in 0..3"}, indent=1))
        print("committed", split.commitment(salt)); return 0
    if a.cmd == "gating":
        seeds = _selected_seeds(a.split, a.salt_file)
        if a.base: core.LLM_BASE = a.base
        if a.key: core.LLM_KEY = a.key
        if a.model: core.LLM_MODEL = a.model
        core.rerun_gating(a.root, seeds, a.executor, a.limit, band=a.band); return 0
    if a.cmd == "i5-transfer":
        from . import i5_campaign
        i5_campaign.rerun_transfer(a.root, a.executor, a.limit_b, staged_from=a.staged_from); return 0
    if a.cmd == "i5":
        from . import i5_campaign
        i5_campaign.run_i5(a.label, a.executor, a.root, a.limit_a, a.limit_b); return 0
    if a.cmd == "o":
        core.rerun_o(a.root, a.executor, a.limit, tag=a.tag); return 0
    if a.cmd == "m1":
        core.rerun_m1(a.root, a.executor, a.limit, tag=a.tag); return 0
    if getattr(a, "executor", None) is not None and "{prompt}" not in a.executor:
        ap.error("--exec must contain the {prompt} placeholder")
    try: seeds = _selected_seeds(a.split, a.salt_file)
    except ValueError as exc: ap.error(str(exc))
    if a.cmd == "agent":
        core.run_agent(a.label, a.executor, a.root, seeds, a.limit, **({"with_o": True} if a.with_o else {}), **({"split_name": a.split} if a.split != "public" else {})); return 0
    if a.cmd in ("llm", "index"):
        extra = {}
        if a.api != "openai": extra["api"] = a.api
        if a.cmd == "index": extra.update(n_seeds=a.seeds_per_family, n_hard=2)
        elif a.seeds_per_family != 2: extra["n_seeds"] = a.seeds_per_family
        if a.split != "public": extra["split_name"] = a.split
        core.run_llm(a.label, a.root, seeds, a.limit, base=a.base, key=a.key, model=a.model, **extra); return 0
    if a.cmd == "llm-harness":
        core.run_llm_via_harness(a.label, a.executor, a.root, seeds, a.limit); return 0
    if a.cmd == "extended":
        core.run_extended(a.label, a.executor, a.root, seeds, a.ai4science); return 0
    return 2

if __name__ == "__main__":
    sys.exit(main())
