"""The LLM executor for LLM mode: an OpenAI-compatible chat client with two read-only tools
(list_files, read_file). It reads the workspace, and its FINAL message is one JSON object that
is written to response.json in the working directory.

Run as a module:  python3 -m hilbench.llm_exec --base URL --key K --model M '<prompt>'

No dependencies: stdlib urllib. Works with Ollama and any OpenAI-compatible endpoint.
"""
from __future__ import annotations
import json, re, sys, urllib.request
from pathlib import Path

SYSTEM = (
    "You work in a file workspace. Use list_files to see it and read_file to read files. "
    "Your FINAL message must be exactly one JSON object and nothing else --- no prose, no code "
    "fences --- containing the deliverable the task asks for. If a file must be produced, put its "
    "full contents under a string key named after the filename; put deliverable fields at top level."
)

def _call(base, key, model, payload, timeout):
    req = urllib.request.Request(base.rstrip("/") + "/chat/completions",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + key})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())

def _parse(text):
    if not text or not text.strip():
        return None, "empty"
    t = text.strip()
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", t, re.S)
    if m:
        t = m.group(1)
    try:
        obj = json.loads(t)
        if isinstance(obj, dict):
            return obj, None
    except json.JSONDecodeError:
        pass
    i, j = t.find("{"), t.rfind("}")
    if 0 <= i < j:
        try:
            obj = json.loads(t[i:j + 1])
            if isinstance(obj, dict):
                return obj, None
        except json.JSONDecodeError:
            pass
    return None, "invalid_json"

def run(base, key, model, prompt, cwd, timeout=300, max_turns=5):
    def tool(name, args):
        if name == "list_files":
            fs = sorted(str(p.relative_to(cwd)) for p in cwd.rglob("*") if p.is_file())
            return json.dumps(fs[:200])
        root = cwd.resolve(); p = (cwd / str(args.get("path", ""))).resolve()
        if root not in p.parents and p != root or not p.exists() or not p.is_file():
            return "file not found"                       # a path outside the workspace does not exist, as far as the model is told
        return p.read_text(encoding="utf-8", errors="replace")[:60000]
    tools = [
        {"type": "function", "function": {"name": "list_files", "description": "list files in the workspace",
                                          "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {"name": "read_file", "description": "read one file",
                                          "parameters": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}}},
    ]
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}]
    text = ""
    for turn in range(max_turns):
        resp = _call(base, key, model,
                     {"model": model, "messages": messages, "temperature": 0.0,
                      "max_tokens": 4000, "tools": tools, "tool_choice": "auto"}, timeout)
        msg = resp["choices"][0]["message"]
        calls = msg.get("tool_calls") or []
        if not calls:
            text = msg.get("content") or ""
            break
        messages.append({"role": "assistant", "content": msg.get("content") or "", "tool_calls": calls})
        for c in calls:
            fn = c["function"]["name"]
            a = c["function"].get("arguments", c["function"].get("args"))   # OpenAI's field is `arguments`
            if isinstance(a, str):
                try:
                    a = json.loads(a)
                except json.JSONDecodeError:
                    a = {}
            out = tool(fn, a or {})
            messages.append({"role": "tool", "tool_call_id": c.get("id", ""), "content": out})
    else:
        resp = _call(base, key, model,
                     {"model": model, "messages": messages + [{"role": "user", "content": "Finish now: reply with exactly one JSON object containing the deliverable."}],
                      "temperature": 0.0, "max_tokens": 4000, "tools": None}, timeout)
        text = resp["choices"][0]["message"].get("content") or ""
    return text

def main():
    a = sys.argv[1:]
    base = key = model = prompt = None
    timeout = 300
    i = 0
    while i < len(a):
        if a[i] == "--base": base = a[i + 1]; i += 2
        elif a[i] == "--key": key = a[i + 1]; i += 2
        elif a[i] == "--model": model = a[i + 1]; i += 2
        elif a[i] == "--timeout": timeout = int(a[i + 1]); i += 2
        elif a[i] == "--prompt": prompt = a[i + 1]; i += 2
        elif a[i].startswith("-"): i += 1
        else: prompt = a[i]; i += 1
    if not (base and key and model and prompt):
        print("usage: -m hilbench.llm --base URL --key K --model M --prompt P", file=sys.stderr)
        return 2
    cwd = Path.cwd()
    text = run(base, key, model, prompt, cwd, timeout=timeout)
    obj, err = _parse(text)
    if err:
        text2 = run(base, key, model, text + "\n\nRestate ONLY the final answer as one JSON object, no prose.", cwd, timeout=timeout)
        obj, err2 = _parse(text2)
    if obj is None:
        (cwd / "response.json").write_text("null")
        print("PARSE_FAIL")
        return 0
    (cwd / "response.json").write_text(json.dumps(obj, indent=1), encoding="utf-8")
    print("OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
