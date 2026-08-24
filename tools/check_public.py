#!/usr/bin/env python3
"""Refuse to publish private coordinates in a public repository.

This repository is public. Twice now a document has shipped with the filename of
an internal specification in its provenance header -- once in August 2026 across
four documents, once again three days later in two more. Both times the remedy
was the same: describe what the specification covers instead of naming it.

A rule applied twice by hand is a rule that should be checked. This is the check.

    python3 tools/check_public.py          # scan the working tree
    python3 tools/check_public.py --self-test

Exit status 1 if anything matches, with file, line and the reason.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Each rule is (name, compiled pattern, why it is not publishable).
RULES: list[tuple[str, re.Pattern[str], str]] = [
    (
        "private-repo-path",
        re.compile(r"singularity[-/]docs|singularity/docs|openclaw[-/]docs"),
        "names a path inside a private repository",
    ),
    (
        "dated-internal-doc",
        re.compile(r"docs/(plans|specs)/\d{4}-\d{2}-\d{2}"),
        "carries the internal plan numbering and its dates",
    ),
    (
        "escape-to-sibling-repo",
        re.compile(r"\]\(\.\./\.\./(?!\.)"),
        "links out of this repository, so the link is broken for every reader",
    ),
]

SKIP_DIRS = {".git", ".claude"}
SCAN_SUFFIXES = {".md", ".tex", ".bib"}


def tracked_and_untracked_files() -> list[Path]:
    """Every file git would consider, so a scan covers work not yet committed."""
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    )
    files = []
    for line in out.stdout.splitlines():
        p = REPO / line
        if p.suffix in SCAN_SUFFIXES and not SKIP_DIRS & set(Path(line).parts):
            files.append(p)
    return files


def scan_text(rel: str, text: str) -> list[str]:
    findings = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for name, pattern, why in RULES:
            if pattern.search(line):
                findings.append(f"{rel}:{lineno}: [{name}] {why}\n    {line.strip()[:140]}")
    return findings


def scan_tree() -> list[str]:
    findings = []
    for path in tracked_and_untracked_files():
        rel = str(path.relative_to(REPO))
        if rel == "tools/check_public.py":
            continue  # the rules themselves quote the patterns they forbid
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        findings.extend(scan_text(rel, text))
    return findings


def self_test() -> int:
    """Prove the checker fails on the thing it exists to catch."""
    cases = [
        ("*Reads: `singularity/docs/guide-sarsi-claude-overview.md`*", "private-repo-path"),
        ("*Plan: `docs/plans/2026-08-20-sarsi-worker-brainrsi-plan.md`*", "dated-internal-doc"),
        ("See [`guide.md`](../../singularity/docs/guide.md).", "private-repo-path"),
        ("Companion page: [`g.md`](../../other-repo/g.md)", "escape-to-sibling-repo"),
    ]
    failures = 0
    for text, expected in cases:
        found = scan_text("<self-test>", text)
        if not any(f"[{expected}]" in f for f in found):
            print(f"SELF-TEST FAIL: {expected!r} not raised on: {text}")
            failures += 1
    clean = "*Reads: the internal engineering overview of the layer*"
    if scan_text("<self-test>", clean):
        print(f"SELF-TEST FAIL: clean line flagged: {clean}")
        failures += 1
    if failures:
        return 1
    print(f"self-test: {len(cases)} violations caught, 1 clean line passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true", help="check the checker, then exit")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    findings = scan_tree()
    if findings:
        print("Private coordinates in a public repository:\n")
        for f in findings:
            print(f)
        print(
            f"\n{len(findings)} finding(s). The remedy is to describe what the document "
            "covers rather than name it -- see the August 2026 precedent in git history."
        )
        return 1
    print("clean: no private coordinates found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
