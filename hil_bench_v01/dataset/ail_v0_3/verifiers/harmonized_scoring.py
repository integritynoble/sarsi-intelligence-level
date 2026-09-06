
"""Reference helpers for AI-Level Bench v0.2 harmonized method records.
Public development code only; not an official certification verifier.
"""
from math import prod

def conjunctive_gate(flags):
    return bool(flags) and all(bool(x) for x in flags)

def retention_gate(passed_levels, required_levels):
    return all(x in set(passed_levels) for x in required_levels)

def classify_h_band(events):
    """Events are dicts with `band` in H0..H5; return highest intervention band observed."""
    order={f"H{i}":i for i in range(6)}
    if not events: return "H0"
    return f"H{max(order.get(e.get('band','H5'),5) for e in events)}"

def delegation_frontier(cell_scores, h_band, p):
    """cell_scores keys are (T_index,H_index); values are S_net estimates."""
    hi=int(h_band[1:])
    passing=[t for (t,h),q in cell_scores.items() if h<=hi and q>=p]
    return max(passing) if passing else None

def unified_gate(coordinate_flags, delegation_ok, lower_u_retained=True):
    return all(bool(v) for v in coordinate_flags.values()) and bool(delegation_ok) and bool(lower_u_retained)
