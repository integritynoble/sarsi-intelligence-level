from __future__ import annotations
import hashlib, json, os, random, re, shlex, shutil, signal, subprocess, time
from pathlib import Path

def rng(seed: int, family: str) -> random.Random:
    return random.Random(int(hashlib.sha256(f"{family}:{seed}".encode()).hexdigest(), 16) % (2**32))

def write_workspace(ws: Path, files: dict) -> None:
    ws.mkdir(parents=True, exist_ok=True)
    for rel, text in files.items():
        p = ws / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text, encoding="utf-8")

def read_json(p: Path):
    try: return json.loads(p.read_text(encoding="utf-8"))
    except FileNotFoundError: return None
    except json.JSONDecodeError: return "INVALID_JSON"

def norm(s) -> str:
    return re.sub(r"\s+", " ", str(s).strip().lower())

def result(passed, accuracy, checks, failure_mode):
    return {"pass": bool(passed), "accuracy": round(float(accuracy), 4),
            "checks": [{"name": n, "ok": bool(ok), "detail": d} for n, ok, d in checks], "failure_mode": failure_mode}

def run_exec(cmd_tmpl: str, prompt: str, cwd: Path, limit: int, env: dict | None = None) -> dict:
    """One executor invocation in its own process group under an enforced limit. Records why it ended."""
    cmd = shlex.split(cmd_tmpl.replace("{prompt}", shlex.quote(prompt))); t0 = time.time()
    e = {**os.environ, "PWD": str(cwd), **(env or {})}
    p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True, env=e)
    try: out, err = p.communicate(timeout=limit); reason = "normal" if p.returncode == 0 else "crashed"
    except subprocess.TimeoutExpired: os.killpg(p.pid, signal.SIGKILL); out, err = p.communicate(); reason = "timed_out"
    return {"exit": p.returncode, "termination_reason": reason, "seconds": round(time.time() - t0, 1),
            "stdout_tail": out.decode(errors="replace")[-160:]}

TASK = ("Read GOAL.md in this directory and do exactly what it says, creating or editing files in this directory. "
        "Do not ask questions. Reply DONE when finished.")
