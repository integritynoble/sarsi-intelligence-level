"""Deterministic allowlisted public-release builder."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path, PurePosixPath
from typing import Iterable

from .runner import PACKAGE_ROOT

PUBLIC_FILES = (
    "README.md",
    "PROTOCOL.md",
    "SCORING.md",
    "DATA_CARD.md",
    "LICENSE",
    "benchmark_manifest.json",
    "build_public_release.py",
)
PUBLIC_DIRECTORIES = (
    "hilbench",
    "tasks/public",
    "profiles",
    "schemas",
    "examples",
    "tests",
)
FORBIDDEN_PARTS = {"organizer_private", "certification_keys.json", "private_generators.py"}


def _included_files(root: Path) -> Iterable[Path]:
    for relative in PUBLIC_FILES:
        path = root / relative
        if path.is_file():
            yield path
    for relative in PUBLIC_DIRECTORIES:
        directory = root / relative
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"symlinks are not permitted in a release: {path}")
            if not path.is_file():
                continue
            if path.suffix in {".pyc", ".pyo"} or "__pycache__" in path.parts:
                continue
            yield path


def build_public_archive(output: Path, root: Path = PACKAGE_ROOT) -> dict[str, object]:
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    files = sorted(set(_included_files(root)), key=lambda path: path.relative_to(root).as_posix())
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = PurePosixPath("hil_benchmark_v1") / PurePosixPath(path.relative_to(root).as_posix())
            if any(part in FORBIDDEN_PARTS for part in relative.parts):
                raise ValueError(f"private path reached public allowlist: {relative}")
            info = zipfile.ZipInfo(relative.as_posix(), date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    verification = verify_public_archive(output)
    if verification["status"] != "pass":
        raise ValueError("public archive verification failed: " + "; ".join(verification["errors"]))
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    return {"status": "pass", "output": str(output), "files": len(files), "sha256": digest}


def verify_public_archive(path: Path) -> dict[str, object]:
    errors: list[str] = []
    names: list[str] = []
    try:
        with zipfile.ZipFile(path, "r") as archive:
            names = archive.namelist()
            for name in names:
                parts = PurePosixPath(name).parts
                if any(part in FORBIDDEN_PARTS for part in parts):
                    errors.append(f"forbidden private member: {name}")
                if name.startswith("/") or ".." in parts:
                    errors.append(f"unsafe member path: {name}")
    except (OSError, zipfile.BadZipFile) as exc:
        errors.append(str(exc))
    return {"status": "pass" if not errors else "fail", "members": len(names), "errors": errors}
