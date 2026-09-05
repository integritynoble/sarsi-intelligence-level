"""Self-validation for manifests, generated items, keys, and split isolation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .constants import BENCHMARK_VERSION
from .io import read_json, read_jsonl
from .runner import PACKAGE_ROOT, load_suite, suite_paths


EXPECTED_COUNTS = {
    ("quick", "individual"): 7,
    ("quick", "organization"): 8,
    ("full", "individual"): 22,
    ("full", "organization"): 25,
}


def _metadata(path: Path) -> tuple[set[str], set[str]]:
    rows = read_jsonl(path)
    return {row["family"] for row in rows}, {row["mechanism"] for row in rows}


def validate_installation(include_private: bool = False) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    errors: list[str] = []
    for split in ("dev", "validation"):
        for (mode, track), expected in EXPECTED_COUNTS.items():
            try:
                tasks, _, count = load_suite(split, mode, track)
                if count != expected:
                    raise ValueError(f"expected {expected} tasks, found {count}")
                if any(task["benchmark_version"] != BENCHMARK_VERSION for task in tasks):
                    raise ValueError("materialized version mismatch")
                checks.append({"check": f"{split}:{mode}:{track}", "status": "pass", "tasks": count})
            except Exception as exc:  # report every structural error together
                errors.append(f"{split}:{mode}:{track}: {exc}")
    profile_dir = PACKAGE_ROOT / "profiles"
    if profile_dir.exists():
        for path in sorted(profile_dir.rglob("*.json")):
            try:
                profile = read_json(path)
                if "profile_schema_version" not in profile:
                    raise ValueError("missing profile_schema_version")
                checks.append({"check": f"profile:{path.relative_to(PACKAGE_ROOT)}", "status": "pass"})
            except Exception as exc:
                errors.append(f"profile:{path}: {exc}")
    schema_dir = PACKAGE_ROOT / "schemas"
    if schema_dir.exists():
        for path in sorted(schema_dir.glob("*.json")):
            try:
                value = read_json(path)
                if value.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
                    raise ValueError("schema must declare JSON Schema draft 2020-12")
                checks.append({"check": f"schema:{path.name}", "status": "pass"})
            except Exception as exc:
                errors.append(f"schema:{path}: {exc}")
    if include_private:
        try:
            for (mode, track), expected in EXPECTED_COUNTS.items():
                _, _, count = load_suite("certification", mode, track, allow_private=True)
                if count != expected:
                    raise ValueError(f"certification:{mode}:{track}: expected {expected}, found {count}")
            public_families: set[str] = set()
            public_mechanisms: set[str] = set()
            for split in ("dev", "validation"):
                families, mechanisms = _metadata(suite_paths(split)[0])
                public_families |= families
                public_mechanisms |= mechanisms
            private_families, private_mechanisms = _metadata(suite_paths("certification")[0])
            if public_families & private_families:
                raise ValueError("certification families overlap public families")
            if public_mechanisms & private_mechanisms:
                raise ValueError("certification mechanisms overlap public mechanisms")
            checks.append(
                {
                    "check": "private-family-and-mechanism-isolation",
                    "status": "pass",
                    "private_families": len(private_families),
                    "private_mechanisms": len(private_mechanisms),
                }
            )
        except Exception as exc:
            errors.append(f"private-validation: {exc}")
    return {
        "benchmark_version": BENCHMARK_VERSION,
        "status": "pass" if not errors else "fail",
        "include_private": include_private,
        "checks": checks,
        "errors": errors,
    }
