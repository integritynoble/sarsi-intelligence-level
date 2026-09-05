#!/usr/bin/env python3
"""Convenience entry point for the deterministic public release build."""

from pathlib import Path

from hilbench.package import PACKAGE_ROOT, build_public_archive


if __name__ == "__main__":
    result = build_public_archive(PACKAGE_ROOT / "dist" / "hil-core-v1-public.zip")
    print(f"{result['output']}  sha256={result['sha256']}  files={result['files']}")
