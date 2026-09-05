"""Command-line entry point for HIL-Bench.

The self-test is deliberately offline: it validates generated specifications,
computed keys, reference solvers, and named naive traps without invoking an
agent or a model endpoint.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Sequence

from . import c_items, core, m1_restart, o_families, sa_probes, score, split


def _parse_seed_spec(value: str) -> list[int]:
    """Parse a comma-separated list of integers and inclusive ranges."""
    seeds: list[int] = []
    try:
        for part in value.split(","):
            part = part.strip()
            if not part:
                continue
            if "-" in part[1:]:
                separator = part.find("-", 1)
                start, stop = int(part[:separator]), int(part[separator + 1 :])
                if stop < start:
                    raise ValueError("range end precedes range start")
                seeds.extend(range(start, stop + 1))
            else:
                seeds.append(int(part))
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid seed specification {value!r}: {exc}") from exc
    if not seeds:
        raise argparse.ArgumentTypeError("at least one seed is required")
    return seeds


def _selected_seeds(split_name: str, salt_file: str | None) -> list[int]:
    if split_name == "public":
        return list(split.PUBLIC_SEEDS)
    if not salt_file:
        raise ValueError("--salt-file is required for the private split")
    salt = Path(salt_file).read_bytes()
    if not salt:
        raise ValueError("the private salt file is empty")
    if not split.check_commitment(salt):
        raise ValueError("private salt does not match the published commitment")
    return split.private_seeds(salt)


def _run_selftest(seeds: Sequence[int]) -> dict:
    family_checks = 0
    for seed in seeds:
        # Each spec-key check proves that the reference answer passes and the
        # predeclared plausible wrong method fails for that generated item.
        c_items.spec_key_check(seed)
        family_checks += len(c_items.BANDS)

        for family in core.TH:
            core.UAB_FAMILIES[family].spec_key_check(seed)
            family_checks += 1

        files, key = sa_probes.sa1_generate(seed)
        assert set(key["real"]).isdisjoint(key["stale"])
        assert set(key["real"]).issubset(files)
        solvable, blocked, _ = sa_probes.sa2_generate(seed)
        assert "data.csv" in solvable and "data.csv" not in blocked
        assert "ledger-export" in blocked["GOAL.md"]

        episode_a, episode_b, memory_key = m1_restart.generate_pair(seed)
        assert memory_key["code_name"] in episode_a["GOAL.md"]
        assert memory_key["code_name"] not in episode_b["GOAL.md"]

        o_families.o0_spec_key(seed)
        o_families.o1_spec_key(seed)
        family_checks += 2

    # Scoring invariants exercise cumulative band and rung semantics without
    # relying on a live executor.
    c_eps = [
        {"band": band, "pass": True}
        for band in ("C0", "C1", "C2", "C3")
    ]
    assert score.c_level(c_eps) == "C3"
    assert score.frontier(
        [
            {"band": "T0", "budget": "H0", "delivered_correct": True},
            {"band": "T1", "budget": "H0", "delivered_correct": False},
            {"band": "T2", "budget": "H0", "delivered_correct": True},
        ]
    ) == "T0"

    salt = b"hilbench-selftest-salt"
    assert split.private_seeds(salt) == split.private_seeds(salt)
    assert set(split.PUBLIC_SEEDS).isdisjoint(split.private_seeds(salt))

    return {
        "status": "ok",
        "offline": True,
        "seeds": list(seeds),
        "spec_key_checks": family_checks,
        "model_calls": 0,
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hilbench")
    commands = parser.add_subparsers(dest="command", required=True)

    selftest = commands.add_parser("selftest", help="run offline generator and scoring checks")
    selftest.add_argument(
        "--seeds",
        type=_parse_seed_spec,
        default=_parse_seed_spec("0-5"),
        help="comma-separated seeds/ranges (default: 0-5)",
    )

    agent = commands.add_parser("agent", help="measure a frozen model-harness pair")
    agent.add_argument("--label", required=True)
    agent.add_argument("--exec", dest="executor", required=True, help="command template containing {prompt}")
    agent.add_argument("--root", type=Path, required=True, help="fresh output directory")
    agent.add_argument("--limit", type=int, default=300, help="per-call wall-clock limit in seconds")
    agent.add_argument("--split", choices=("public", "private"), default="public")
    agent.add_argument("--salt-file")

    llm = commands.add_parser("llm", help="measure a model through the reference harness ladder")
    llm.add_argument("--label", required=True)
    llm.add_argument("--root", type=Path, required=True, help="fresh output directory")
    llm.add_argument("--limit", type=int, default=120, help="per-call wall-clock limit in seconds")
    llm.add_argument("--split", choices=("public", "private"), default="public")
    llm.add_argument("--salt-file")
    llm.add_argument("--base", default=os.environ.get("HILBENCH_LLM_BASE"))
    llm.add_argument("--key", default=os.environ.get("HILBENCH_LLM_KEY"))
    llm.add_argument("--model", default=os.environ.get("HILBENCH_LLM_MODEL"))

    commit = commands.add_parser("commit-private", help="publish only the hash of a private salt")
    commit.add_argument("--salt-file", required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "selftest":
        print(json.dumps(_run_selftest(args.seeds), sort_keys=True))
        return 0

    if args.command == "commit-private":
        salt = Path(args.salt_file).read_bytes()
        if not salt:
            parser.error("the private salt file is empty")
        payload = {
            "commitment": split.commitment(salt),
            "n_private_seeds": 4,
            "derivation": "HMAC-SHA256(salt, 'family:index')[:4] mod 1e6 + 1000",
        }
        split.COMMITMENT_FILE.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(payload["commitment"])
        return 0

    try:
        seeds = _selected_seeds(args.split, args.salt_file)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    if args.command == "agent":
        if "{prompt}" not in args.executor:
            parser.error("--exec must contain the {prompt} placeholder")
        core.run_agent(args.label, args.executor, args.root, seeds, args.limit)
        return 0

    core.run_llm(
        args.label,
        args.root,
        seeds,
        args.limit,
        base=args.base,
        key=args.key,
        model=args.model,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
