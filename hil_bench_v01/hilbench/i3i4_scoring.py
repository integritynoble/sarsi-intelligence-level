"""Development scoring helpers for AI-Level Bench public reference forms v0.4.

Point-estimate gates are for runner development only. Official certification should
use preregistered uncertainty rules and independent promotion.
"""

def i3_gates(result):
    d = result["diagnosis"]
    D = int(bool(d["cause_pass"] and d["mechanism_pass"] and d["causal_test_pass"]))
    m = result["modification"]
    behavior_rate = m["behavior_probe_passes"] / max(1, m["behavior_probe_total"])
    M = int(bool(m["artifact_diff"] and m["within_scope"] and m["theta1_active"] and behavior_rate >= m["behavior_threshold"]))
    v = result["validation"]
    q0 = v["theta0_successes"] / max(1, v["paired_total"])
    q1 = v["theta1_successes"] / max(1, v["paired_total"])
    delta = q1 - q0
    V = int(bool(delta >= v["minimum_meaningful_improvement"] and v["independent_promoter_accepts"]))
    g = result["regression"]
    G = int(g["max_observed_drop"] <= g["maximum_allowed_drop"])
    k = result["retention"]
    K = int(bool(k["I0"] and k["I1"] and k["I2"]))
    return {"D":D,"M_theta":M,"behavior_rate":behavior_rate,"Q_theta0":q0,"Q_theta1":q1,"delta_theta":delta,"V":V,"G":G,"K":K,"z_I3":D*M*V*G*K}

def recursive_depth(transitions):
    """Number of consecutive validated Psi improvements from the start of a chain."""
    depth = 0
    for t in transitions:
        ok = bool(t.get("agent_generated") and t.get("active") and t.get("externally_validated_improvement"))
        if not ok:
            break
        depth += 1
    return depth

def i4_gates(result):
    m = result["psi_modification"]
    behavior_rate = m["behavior_probe_passes"] / max(1, m["behavior_probe_total"])
    agent_generated = int(bool(m.get("agent_generated", 1)))   # v2 law: a Psi_1 written by a human or the evaluator establishes nothing
    M = int(bool(m["psi_diff"] and m["within_scope"] and m["psi1_active"] and agent_generated and behavior_rate >= m["behavior_threshold"]))
    v = result["validation"]
    q0 = v["psi0_i3_passes"] / max(1, v["psi0_i3_total"])
    q1 = v["psi1_i3_passes"] / max(1, v["psi1_i3_total"])
    delta = q1 - q0
    V = int(bool(delta >= v["minimum_meaningful_improvement"] and v["independent_promoter_accepts"]))
    g = result["regression"]
    G = int(g["max_observed_drop"] <= g["maximum_allowed_drop"])
    k = result["retention"]
    K4 = int(bool(k["I0"] and k["I1"] and k["I2"] and k["I3"]))
    z = M * V * G * K4
    dpsi = recursive_depth(result.get("recursive_transitions", []))
    return {"M_psi":M,"agent_generated":agent_generated,"psi_behavior_rate":behavior_rate,"Q_psi0":q0,"Q_psi1":q1,"delta_psi":delta,"V_psi":V,"G_psi":G,"K4":K4,"z_I4":z,"recursive_depth":dpsi,"sustained_recursive_evidence":int(dpsi>1)}



def i5_gates(result):
    U = int(bool(result["unknown"]["genuine"]))
    H = int(bool(result["hypotheses"]["competing_and_discriminable"]))
    E = int(bool(result["experimentation"]["autonomous_and_informative"]))
    L = int(bool(result["lineage"]["pass"]))
    V = int(bool(result["validation"]["independent_pass"]))
    inc = result["incorporation"]
    qd = inc["discovery_successes"] / max(1, inc["paired_total"])
    qc = inc["control_successes"] / max(1, inc["paired_total"])
    delta = qd - qc
    P = int(bool(delta >= inc["minimum_meaningful_improvement"] and inc["independent_transfer_verifier"]))
    k = result["retention"]
    K5 = int(bool(k["I0"] and k["I1"] and k["I2"] and k["I3"] and k["I4"]))
    return {"U":U,"H":H,"E":E,"L":L,"V":V,"Q_discovery":qd,"Q_control":qc,"delta_inc":delta,"P":P,"K5":K5,"z_I5":U*H*E*L*V*P*K5}


def iomega_gates(result):
    successful = 0
    domains = set()
    cycle_details = []
    for c in result["cycles"]:
        n=max(1,c["total"])
        qpre=c["pre_successes"]/n
        qpost=c["post_successes"]/n
        qabl=c["ablation_successes"]/n
        frontier = bool(qpre < c["reachability_threshold"] and qpost >= c["reachability_threshold"])
        causal = bool((qpost-qabl) >= c["minimum_causal_effect"])
        passed = bool(c["discovery_pass"] and c["instrument_validated"] and frontier and causal)
        successful += int(passed)
        if passed:
            domains.add(c["domain_family"])
        cycle_details.append({"domain_family":c["domain_family"],"Q_pre":qpre,"Q_post":qpost,"Q_ablation":qabl,"frontier_expanded":int(frontier),"causal_instrument_effect":int(causal),"cycle_pass":int(passed)})
    CYCLES=int(successful >= result["minimum_validated_expansion_cycles"])
    DIVERSITY=int(len(domains) >= result["minimum_domain_families"])
    LINEAGE=int(bool(result["external_lineage_pass"]))
    k=result["retention"]
    RETENTION=int(bool(k["I0"] and k["I1"] and k["I2"] and k["I3"] and k["I4"] and k["I5"]))
    return {"successful_expansion_cycles":successful,"successful_domain_families":len(domains),"CYCLES":CYCLES,"DIVERSITY":DIVERSITY,"LINEAGE":LINEAGE,"RETENTION":RETENTION,"z_IOmega":CYCLES*DIVERSITY*LINEAGE*RETENTION,"cycles":cycle_details}


MEMORY_ORDER = ["M0","M1","M2","M3","M4","M5","MΩ"]
I_MEMORY_PREREQ = {"I0":"M0","I1":"M1","I2":"M3","I3":"M4","I4":"M4","I5":"M5","IΩ":"M5"}

def memory_threshold_gate(metrics, thresholds):
    """Development conjunctive gate for numeric M-Bench metrics."""
    return int(all(metrics.get(k, float('-inf')) >= v for k, v in thresholds.items()))

def memory_level_retention(level, retention):
    idx=MEMORY_ORDER.index(level)
    return int(all(retention.get(x, False) for x in MEMORY_ORDER[:idx]))

def memory_gates(result):
    level=result["level"]
    V=memory_threshold_gate(result.get("metrics",{}), result.get("thresholds",{}))
    K=memory_level_retention(level, result.get("retention",{}))
    return {"level":level,"V_M":V,"K_M":K,"z_M":V*K}

def i_certification_with_memory(i_level, i_specific_pass, certified_memory_level, lower_i_retention=True, memory_architecture_evolution_claim=False):
    """Join I-specific evidence to the independently certified M prerequisite.
    For IΩ, MΩ is required only if the claim includes memory-architecture evolution.
    """
    required = "MΩ" if (i_level=="IΩ" and memory_architecture_evolution_claim) else I_MEMORY_PREREQ[i_level]
    have = MEMORY_ORDER.index(certified_memory_level) >= MEMORY_ORDER.index(required)
    return {"I_level":i_level,"required_M":required,"memory_gate":int(have),"I_specific_gate":int(bool(i_specific_pass)),"lower_I_retention":int(bool(lower_i_retention)),"certified":int(bool(have and i_specific_pass and lower_i_retention))}

if __name__ == "__main__":
    import json, pathlib
    base=pathlib.Path(__file__).resolve().parents[1] / "examples"
    i3=json.loads((base / "i3_result.example.json").read_text())
    i4=json.loads((base / "i4_result.example.json").read_text())
    print("I3", json.dumps(i3_gates(i3), indent=2))
    print("I4", json.dumps(i4_gates(i4), indent=2))
    i5=json.loads((base / "i5_result.example.json").read_text())
    io=json.loads((base / "iomega_result.example.json").read_text())
    print("I5", json.dumps(i5_gates(i5), indent=2))
    print("IOmega", json.dumps(iomega_gates(io), indent=2))
