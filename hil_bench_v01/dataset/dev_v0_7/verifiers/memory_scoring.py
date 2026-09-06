"""M-Bench v0.6 development scoring helpers.

Cumulative law: a level passes only if its newly added capability passes AND
all lower M levels required by the canonical ordering are retained. The scorer
therefore forbids level skipping. Public point thresholds are illustrative only.
"""
MEMORY_ORDER=["M0","M1","M2","M3","M4","M5","MΩ"]

def required_lower(level):
    return MEMORY_ORDER[:MEMORY_ORDER.index(level)]

def lower_retention(level, retention):
    req=required_lower(level)
    failed=[x for x in req if not bool(retention.get(x,False))]
    return (len(failed)==0, failed)

def new_capability_gate(result):
    l=result["level"]; m=result["metrics"]; t=result["thresholds"]
    if l=="M0": return m["q_state"]>=t["q_state_min"] and m["q_update"]>=t["q_update_min"]
    if l=="M1": return m["q_dur"]>=t["q_dur_min"] and m["q_prov"]>=t["q_prov_min"] and m["q_abl"]<=t["q_abl_max"]
    if l=="M2": return all([m["retrieval_precision"]>=t["retrieval_precision_min"],m["retrieval_recall"]>=t["retrieval_recall_min"],m["q_prov"]>=t["q_prov_min"],m["q_time"]>=t["q_time_min"],m["q_stale"]>=t["q_stale_min"]])
    if l=="M3": return all([m["q_sem"]>=t["q_sem_min"],m["q_proc"]>=t["q_proc_min"],m["q_update"]>=t["q_update_min"],m["q_demote"]>=t["q_demote_min"],m["q_persist"]>=t["q_persist_min"]])
    if l=="M4": return all([m["repair_precision"]>=t["repair_precision_min"],m["q_conf"]>=t["q_conf_min"],m["harmful_prune_rate"]<=t["harmful_prune_rate_max"],m["q_recover"]>=t["q_recover_min"],m["protected_retention_drop"]<=t["protected_retention_drop_max"]])
    if l=="M5": return all([m["q_chain"]>=t["q_chain_min"],m["q_source"]>=t["q_source_min"],m["q_cross"]>=t["q_cross_min"],m["q_scope"]>=t["q_scope_min"],m["q_stale"]>=t["q_stale_min"],m["q_repro"]>=t["q_repro_min"]])
    if l=="MΩ":
        promoter=bool(result.get("promotion",{}).get("accepted",False))
        instr=result.get("instrumentation",{})
        causal=all(bool(instr.get(k,False)) for k in ["manifest_diff_pass","scope_pass","activation_pass","behavior_probe_pass","fixed_content_pair_pass","delta_ablation_pass","migration_guard_pass"])
        return all([bool(m["C_diff"]),bool(m["C_scope"]),bool(m["C_active"]),bool(m["C_behavior"]),m["delta_phi"]>=t["delta_phi_min"],bool(m["regression_guard"]),promoter,causal])
    raise ValueError(l)

def gate(result):
    l=result["level"]
    V=bool(new_capability_gate(result))
    K,failed=lower_retention(l,result.get("retention",{}))
    return {"level":l,"V_new":int(V),"K_lower_M":int(K),"failed_lower_M":failed,"z_M":int(V and K)}

def highest_certified(results_by_level):
    highest=None
    for lvl in MEMORY_ORDER:
        r=results_by_level.get(lvl)
        if r is None: break
        if gate(r)["z_M"]!=1: break
        highest=lvl
    return highest
