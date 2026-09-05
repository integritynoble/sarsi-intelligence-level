"""Command-line interface for HIL-Core v1."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from .curve import build_model_hil_curve
from .io import read_json, read_jsonl, write_json
from .package import build_public_archive, verify_public_archive
from .runner import PACKAGE_ROOT, load_profile, load_suite, run_suite
from .scoring import score_episodes
from .validation import validate_installation


def _emit(value: Any, output: Path | None) -> None:
    if output is None:
        json.dump(value, sys.stdout, indent=2, sort_keys=True, ensure_ascii=False)
        sys.stdout.write("\n")
    else:
        write_json(output, value)


def _common_suite(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--split", choices=("dev", "validation", "certification"), default="dev")
    parser.add_argument("--mode", choices=("quick", "full"), default="quick")
    parser.add_argument("--track", choices=("individual", "organization"))
    parser.add_argument("--allow-private", action="store_true", help="acknowledge organizer-only certification access")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python3 -m hilbench", description="HIL-Core v1 reference benchmark")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    list_parser = subparsers.add_parser("list", help="list task metadata without answer keys")
    _common_suite(list_parser)
    list_parser.add_argument("--output", type=Path)

    validate_parser = subparsers.add_parser("validate", help="validate tasks, keys, schemas, and profiles")
    validate_parser.add_argument("--include-private", action="store_true")
    validate_parser.add_argument("--output", type=Path)

    run_parser = subparsers.add_parser("run", help="execute and score one frozen model--harness pair")
    _common_suite(run_parser)
    run_parser.add_argument("--profile", type=Path)
    run_parser.add_argument("--adapter", choices=("oracle", "mock", "subprocess"), default="mock")
    run_parser.add_argument("--timeout-seconds", type=float, default=15.0)
    run_parser.add_argument("--events", type=Path, help="optional key-free episode log")
    run_parser.add_argument("--output", type=Path)
    run_parser.add_argument(
        "--command",
        nargs=argparse.REMAINDER,
        help="candidate argv; must be the final option, e.g. --command python3 agent.py",
    )

    score_parser = subparsers.add_parser("score", help="rescore a key-free episode JSONL log")
    _common_suite(score_parser)
    score_parser.add_argument("--profile", type=Path)
    score_parser.add_argument("--events", type=Path, required=True)
    score_parser.add_argument("--adapter-name", default="external-log")
    score_parser.add_argument("--output", type=Path)

    curve_parser = subparsers.add_parser("curve", help="compose reference-harness pair reports into Model-HIL")
    curve_parser.add_argument("--reports", type=Path, nargs="+", required=True)
    curve_parser.add_argument("--output", type=Path)

    package_parser = subparsers.add_parser("package", help="build or verify the allowlisted public archive")
    package_parser.add_argument("--output", type=Path, default=PACKAGE_ROOT / "dist" / "hil-core-v1-public.zip")
    package_parser.add_argument("--verify", action="store_true", help="verify an existing archive instead of building")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.subcommand == "validate":
            result = validate_installation(args.include_private)
            _emit(result, args.output)
            return 0 if result["status"] == "pass" else 1
        if args.subcommand == "package":
            result = verify_public_archive(args.output) if args.verify else build_public_archive(args.output)
            _emit(result, None)
            return 0 if result["status"] == "pass" else 1
        if args.subcommand == "curve":
            reports = [read_json(path) for path in args.reports]
            _emit(build_model_hil_curve(reports), args.output)
            return 0
        if args.subcommand in {"list", "run", "score"}:
            pair, track = load_profile(getattr(args, "profile", None), args.track)
            if args.subcommand == "list":
                tasks, _, _ = load_suite(args.split, args.mode, track, allow_private=args.allow_private)
                metadata = [
                    {
                        key: task[key]
                        for key in ("id", "split", "coordinate", "level", "family", "mechanism", "track", "quick", "difficulty")
                    }
                    for task in tasks
                ]
                _emit({"split": args.split, "mode": args.mode, "track": track, "tasks": metadata}, args.output)
                return 0
            if args.subcommand == "run":
                report = run_suite(
                    split=args.split,
                    mode=args.mode,
                    track=track,
                    pair=pair,
                    adapter_kind=args.adapter,
                    command=args.command,
                    timeout_seconds=args.timeout_seconds,
                    allow_private=args.allow_private,
                    events_path=args.events,
                )
                _emit(report, args.output)
                return 0
            _, _, expected = load_suite(args.split, args.mode, track, allow_private=args.allow_private)
            episodes = read_jsonl(args.events)
            report = score_episodes(
                episodes,
                pair=pair,
                track=track,
                split=args.split,
                mode=args.mode,
                expected_tasks=expected,
                adapter_name=args.adapter_name,
            )
            _emit(report, args.output)
            return 0
    except (FileNotFoundError, PermissionError, ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 2
