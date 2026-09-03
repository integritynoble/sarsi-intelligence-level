from __future__ import annotations
import hashlib, json, random, re
from pathlib import Path

def rng(seed: int, family: str) -> random.Random:
    h = int(hashlib.sha256(f"{family}:{seed}".encode()).hexdigest(), 16) % (2**32)
    return random.Random(h)

def write_workspace(ws: Path, files: dict[str, str]) -> None:
    ws.mkdir(parents=True, exist_ok=True)
    for rel, text in files.items():
        p = ws / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

def snapshot(files: dict[str, str]) -> dict[str, str]:
    return {rel: hashlib.sha256(t.encode()).hexdigest() for rel, t in files.items()}

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())

def read_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return "INVALID_JSON"

def result(passed: bool, accuracy: float, checks: list[tuple[str, bool, str]], failure_mode: str | None) -> dict:
    return {"pass": bool(passed), "accuracy": round(accuracy, 4),
            "checks": [{"name": n, "ok": bool(ok), "detail": d} for n, ok, d in checks],
            "failure_mode": failure_mode}
