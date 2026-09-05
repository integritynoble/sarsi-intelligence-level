"""LLM-mode deliverable extraction.

In LLM mode the executor cannot edit workspace files, so its answer arrives as one JSON object
(the final message, in response.json). This module turns that object into the deliverable files
each family's verifier expects. The verifiers are UNCHANGED: they are the same acceptance loci
used in agent mode, which is what makes the two modes comparable.
"""
from __future__ import annotations
import json
from pathlib import Path
from .common import read_json, parse_llm_json

def _resp(ws: Path):
    r = read_json(ws / "response.json")
    if r is None or r == "INVALID_JSON":
        return None
    if not isinstance(r, dict):
        return None
    if len(r) == 1:
        v = next(iter(r.values()))
        if isinstance(v, dict):
            return v
    return r

def _collect(fam: str, ws: Path, files: dict) -> dict:
    """Files to materialize from the LLM response (or {}). Returns {file: text}; extract() writes them."""
    r = _resp(ws) or {}
    out = {}
    if fam == "code_t0":
        # the LLM returns the corrected config.py content under "config.py"
        cfg = r.get("config.py") or r.get("config")
        if isinstance(cfg, str):
            out["config.py"] = cfg
        if out: return out
    if fam in ("funding_t0",):
        v = {"field": r.get("field"), "value": r.get("value")}
        if all(x is not None for x in v.values()): out["answer.json"] = json.dumps(v)
        if out: return out
    if fam == "job_t0":
        v = {k: r.get(k) for k in ("required", "work_authorization_required", "clearance_required", "location")}
        if isinstance(r.get("required"), list): out["requirements.json"] = json.dumps(v)
        if out: return out
    if fam == "paper_t0":
        v = {k: r.get(k) for k in ("citation", "discrepancies", "consistent")}
        if all(k in r for k in ("citation", "discrepancies", "consistent")): out["citation_check.json"] = json.dumps(v)
        if out: return out
    if fam == "paper_t1":
        t = r.get("text") or r.get("section")
        if isinstance(t, str) and t.strip(): out["results_section.md"] = t
        if out: return out
    if fam == "business_t0":
        v = {k: r.get(k) for k in ("fact", "value", "unit", "source_line")}
        if all(k in r for k in v): out["fact.json"] = json.dumps(v)
        if out: return out
    if fam == "c_items":
        a = r.get("answer")
        if a is not None:
            v = {"answer": a}
            if r.get("cost") is not None: v["cost"] = r["cost"]
            out["answer.json"] = json.dumps(v)
        if out: return out
    if fam == "m1_ack":
        if r.get("recorded") is True: out["ack.json"] = json.dumps({"recorded": True, "where": str(r.get("where", ""))})
        if out: return out
    if fam == "m1_recall":
        v = {k: r.get(k) for k in ("code_name", "parameter", "convention", "source")}
        if any(v.values()): out["recall.json"] = json.dumps(v)
        if out: return out
    if fam == "sa1":
        v = {k: r.get(k) for k in ("files", "notes_accurate", "tools_available")}
        if isinstance(r.get("files"), list): out["state.json"] = json.dumps(v)
        if out: return out
    if fam == "sa2_solvable":
        if r.get("total") is not None: out["total.json"] = json.dumps({"total": r["total"]})
        if out: return out
    if fam == "sa2_blocked":
        if r.get("blocked") is True: out["blocked.json"] = json.dumps({"blocked": True, "reason": str(r.get("reason", ""))})
        if out: return out
    if fam == "o0":
        if isinstance(r.get("plan"), (list, dict)): out["plan.json"] = json.dumps(r)
        else: out["plan.json"] = json.dumps({"plan": []})
        if out: return out
    if fam == "o1":
        v = {k: r.get(k) for k in ("routing_decision", "basis")}
        if v.get("routing_decision"): out["routing_decision.json"] = json.dumps(v)
        if out: return out
    if fam == "i2_a":
        if isinstance(r.get("cleaned"), list): out["cleaned.json_rows"] = json.dumps(r["cleaned"])
        if out: return out
    if fam == "i2_b":
        v = {k: r.get(k) for k in ("per_id", "per_month")}
        if isinstance(r.get("per_id"), list): out["totals.json"] = json.dumps(v)
        return out
    if not out:
        # Generic contract for every other family: the response is the deliverable. A key that names a
        # deliverable file carries that file's content (string) or object (JSON); otherwise the whole
        # response is written as the family's single deliverable. Verifiers are unchanged.
        from .core import DELIV
        deliv = {**DELIV, "c_items": "answer.json", "sa1": "state.json", "sa2": "total.json",
                 "o0_routing": "org_record.json", "o1_orgmem": "report.json"}.get(fam)
        for k, v in list(r.items()):
            if isinstance(k, str) and "." in k and (isinstance(v, str) or isinstance(v, (dict, list))):
                out[k] = v if isinstance(v, str) else json.dumps(v)
        if r.get("blocked") is True and fam not in ("hc_contra", "sa2") and not out:
            (ws / "DECLINED.json").write_text(json.dumps(r), encoding="utf-8")   # held back: nothing delivered, nothing priced
            return out
        if deliv and deliv not in out and r:
            if fam == "hc_contra" and r.get("blocked") is True: out["blocked.json"] = json.dumps(r)
            elif fam == "sa2" and r.get("blocked") is True: out["blocked.json"] = json.dumps(r)
            elif fam == "c_items": out["answer.json"] = json.dumps(r)
            elif fam == "sa1": out["state.json"] = json.dumps(r)
            elif fam == "o0_routing": out["org_record.json"] = json.dumps(r)
            else: out[deliv] = json.dumps(r)
        if fam == "hc_rule" and "mechanism.txt" not in out and ("switch" in r or "period" in r):
            out["mechanism.txt"] = f"switch: {r.get('switch')}\nperiod: {r.get('period')}\n"
    return out

def extract(fam: str, ws: Path, files: dict) -> dict:
    """Turn response.json into the deliverable files the family's verifier expects, and write them."""
    out = _collect(fam, ws, files)
    for name, text in out.items():
        (ws / name).write_text(text if isinstance(text, str) else json.dumps(text), encoding="utf-8")
    return out
