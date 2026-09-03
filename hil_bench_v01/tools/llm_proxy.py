#!/usr/bin/env python3
"""Point Claude Code at another model through an Anthropic-compatible endpoint.

    python3 tools/llm_proxy.py PORT UPSTREAM MODEL [nothink]

Rewrites every request's model name to MODEL (Claude Code 2.1.x refuses an ANTHROPIC_MODEL it does not
recognise and otherwise sends its own default name, which foreign endpoints reject), hoists system-role
messages into the top-level system field (some shims require it), and with `nothink` prefixes the system
prompt with /nothink (Qwen). Credentials are never read here: Claude Code sends them and they are forwarded.
Run Claude Code with ANTHROPIC_BASE_URL=http://127.0.0.1:PORT and ANTHROPIC_AUTH_TOKEN=<the upstream key>.
"""
import http.server, json, sys, urllib.request, urllib.error
PORT = int(sys.argv[1]); UPSTREAM = sys.argv[2].rstrip("/"); MODEL = sys.argv[3]; NOTHINK = "nothink" in sys.argv[4:]

def _text(c): return c if isinstance(c, str) else "\n".join(b.get("text", "") for b in (c or []) if isinstance(b, dict))

class H(http.server.BaseHTTPRequestHandler):
    def _fwd(self, method):
        n = int(self.headers.get("Content-Length", 0)); body = self.rfile.read(n) if n else b""
        if body:
            try:
                d = json.loads(body); d["model"] = MODEL
                msgs = d.get("messages") or []; sys_msgs = [m for m in msgs if m.get("role") == "system"]
                if sys_msgs:
                    d["system"] = "\n\n".join([_text(d.get("system") or "")] + [_text(m.get("content")) for m in sys_msgs]).strip()
                    d["messages"] = [m for m in msgs if m.get("role") != "system"]
                if NOTHINK and "/nothink" not in json.dumps(d.get("system", ""))[:20]:
                    d["system"] = "/nothink\n" + (d["system"] if isinstance(d.get("system"), str) else _text(d.get("system")))
                body = json.dumps(d).encode()
            except Exception: pass
        req = urllib.request.Request(UPSTREAM + self.path, data=body if method == "POST" else None, method=method)
        for k, v in self.headers.items():
            if k.lower() not in ("host", "content-length", "accept-encoding"): req.add_header(k, v)
        try:
            with urllib.request.urlopen(req, timeout=900) as r:
                self.send_response(r.status)
                for k, v in r.headers.items():
                    if k.lower() not in ("transfer-encoding", "content-length", "content-encoding"): self.send_header(k, v)
                self.end_headers()
                while True:
                    chunk = r.read(4096)
                    if not chunk: break
                    self.wfile.write(chunk); self.wfile.flush()
        except urllib.error.HTTPError as e:
            self.send_response(e.code); self.end_headers(); self.wfile.write(e.read())
    def do_POST(self): self._fwd("POST")
    def do_GET(self): self._fwd("GET")
    def log_message(self, *a): pass

http.server.ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
