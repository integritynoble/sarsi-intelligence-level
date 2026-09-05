"""M-Bench v0.5 development scoring helpers.
Illustrative point gates only. Official certification must preregister thresholds,
uncertainty rules, and independent verifier/promoter ownership.
"""
MEMORY_ORDER=["M0","M1","M2","M3","M4","M5","MΩ"]

def lower_retention(level, retention):
    return all(retention.get(x,False) for x in MEMORY_ORDER[:MEMORY_ORDER.index(level)])

def gate(result):
    l=result["level"]; m=result["metrics"]; t=result["thresholds"]
    if l=="M0": V=m["q_state"]>=t["q_state_min"] and m["q_update"]>=t["q_update_min"]
    elif l=="M1": V=m["q_dur"]>=t["q_dur_min"] and m["q_prov"]>=t["q_prov_min"] and m["q_abl"]<=t["q_abl_max"]
    elif l=="M2": V=all([m["retrieval_precision"]>=t["retrieval_precision_min"],m["retrieval_recall"]>=t["retrieval_recall_min"],m["q_prov"]>=t["q_prov_min"],m["q_time"]>=t["q_time_min"],m["q_stale"]>=t["q_stale_min"]])
    elif l=="M3": V=all([m["q_sem"]>=t["q_sem_min"],m["q_proc"]>=t["q_proc_min"],m["q_update"]>=t["q_update_min"],m["q_demote"]>=t["q_demote_min"],m["q_persist"]>=t["q_persist_min"]])
    elif l=="M4": V=all([m["repair_precision"]>=t["repair_precision_min"],m["q_conf"]>=t["q_conf_min"],m["harmful_prune_rate"]<=t["harmful_prune_rate_max"],m["q_recover"]>=t["q_recover_min"],m["protected_retention_drop"]<=t["protected_retention_drop_max"]])
    elif l=="M5": V=all([m["q_chain"]>=t["q_chain_min"],m["q_source"]>=t["q_source_min"],m["q_cross"]>=t["q_cross_min"],m["q_scope"]>=t["q_scope_min"],m["q_stale"]>=t["q_stale_min"],m["q_repro"]>=t["q_repro_min"]])
    elif l=="MΩ": V=all([bool(m["C_diff"]),bool(m["C_scope"]),bool(m["C_active"]),bool(m["C_behavior"]),m["delta_phi"]>=t["delta_phi_min"],bool(m["regression_guard"]),bool(m["lower_M_retention"])])
    else: raise ValueError(l)
    K=lower_retention(l,result.get("retention",{}))
    return {"level":l,"V_M":int(V),"K_lower_M":int(K),"z_M":int(V and K)}
