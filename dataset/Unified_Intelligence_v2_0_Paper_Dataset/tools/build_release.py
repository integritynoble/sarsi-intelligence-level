#!/usr/bin/env python3
"""Build a deterministic standalone ZIP and source checksum list."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR = ROOT.parent
OUTPUT = DATASET_DIR / "Unified_Intelligence_v2_0_Paper_Dataset.zip"
ARCHIVE_ROOT = ROOT.name
FIXED_TIME = (2026, 8, 29, 0, 0, 0)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dependency_path() -> Path:
    embedded = ROOT / "dependencies" / "HIL_Coordinate_Benchmark_Datasets_v1_2.zip"
    sibling = DATASET_DIR / "HIL_Coordinate_Benchmark_Datasets_v1_2.zip"
    return embedded if embedded.exists() else sibling


def package_files(dependency: Path) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path != dependency
        and path.name != "checksums.sha256"
        and "__pycache__" not in path.parts
        and not path.name.endswith(".pyc")
    )


def write_checksums(files: list[Path], dependency: Path) -> None:
    lines = [f"{sha256_bytes(path.read_bytes())}  {path.relative_to(ROOT).as_posix()}" for path in files]
    lines.append(f"{sha256_bytes(dependency.read_bytes())}  dependencies/{dependency.name}")
    (ROOT / "checksums.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")


def add_bytes(archive: zipfile.ZipFile, name: str, data: bytes) -> None:
    info = zipfile.ZipInfo(name, FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.flag_bits |= 0x800
    archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "tools" / "analyze.py"), "--write"], check=True, stdout=subprocess.DEVNULL)
    dependency = dependency_path()
    if not dependency.exists():
        raise FileNotFoundError(dependency)
    files = package_files(dependency)
    write_checksums(files, dependency)
    subprocess.run([sys.executable, str(ROOT / "tools" / "validate.py")], check=True)
    files = package_files(dependency) + [ROOT / "checksums.sha256"]
    with zipfile.ZipFile(OUTPUT, "w") as archive:
        for path in sorted(files):
            relative = path.relative_to(ROOT).as_posix()
            add_bytes(archive, f"{ARCHIVE_ROOT}/{relative}", path.read_bytes())
        add_bytes(
            archive,
            f"{ARCHIVE_ROOT}/dependencies/{dependency.name}",
            dependency.read_bytes(),
        )
    print(f"{OUTPUT.name}: {OUTPUT.stat().st_size} bytes")
    print(f"sha256: {sha256_bytes(OUTPUT.read_bytes())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
