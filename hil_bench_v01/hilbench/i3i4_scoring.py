"""Development scoring helpers for HIL-Bench public reference forms.

These helpers intentionally use simple point-estimate gates for runner development.
Official certification should replace V gates with preregistered uncertainty rules.
"""

def i3_gates(result):
    d = result["diagnosis"]
    D = int(bool(d["cause_pass"] and d["mechanism_pass"] and d["causal_test_pass"]))

    m = result["modification"]
    behavior_rate = m["behavior_probe_passes"] / max(1, m["behavior_probe_total"])
    M = int(bool(
        m["artifact_diff"]
        and m["within_scope"]
        and m["theta1_active"]
        and behavior_rate >= m["behavior_threshold"]
    ))

    v = result["validation"]
    q0 = v["theta0_successes"] / max(1, v["paired_total"])
    q1 = v["theta1_successes"] / max(1, v["paired_total"])
    delta = q1 - q0
    V = int(bool(
        delta >= v["minimum_meaningful_improvement"]
        and v["independent_promoter_accepts"]
    ))

    g = result["regression"]
    G = int(g["max_observed_drop"] <= g["maximum_allowed_drop"])

    k = result["retention"]
    K = int(bool(k["I0"] and k["I1"] and k["I2"]))

    z = D * M * V * G * K
    return {
        "D": D,
        "M_theta": M,
        "behavior_rate": behavior_rate,
        "Q_theta0": q0,
        "Q_theta1": q1,
        "delta_theta": delta,
        "V": V,
        "G": G,
        "K": K,
        "z_I3": z
    }

def i4_gates(result):
    m = result["psi_modification"]
    M = int(bool(m["psi_diff"] and m["within_scope"] and m["psi1_active"]))

    v = result["validation"]
    baseline = v["psi0_i3_passes"] / max(1, v["psi0_i3_total"])
    after = v["psi1_i3_passes"] / max(1, v["psi1_i3_total"])
    delta = after - baseline
    V = int(bool(
        delta >= v["minimum_meaningful_improvement"]
        and v["independent_promoter_accepts"]
    ))

    g = result["regression"]
    G = int(g["max_observed_drop"] <= g["maximum_allowed_drop"])

    k = result["retention"]
    K4 = int(bool(k["I0"] and k["I1"] and k["I2"] and k["I3"]))

    z = M * V * G * K4
    return {
        "M_psi": M,
        "Q_psi0": baseline,
        "Q_psi1": after,
        "delta_psi": delta,
        "V_psi": V,
        "G_psi": G,
        "K4": K4,
        "z_I4": z
    }

if __name__ == "__main__":
    import json, pathlib
    ex = pathlib.Path(__file__).resolve().parents[1] / "examples" / "i3_result.example.json"
    result = json.loads(ex.read_text())
    print(json.dumps(i3_gates(result), indent=2))
