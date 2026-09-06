"""Development helpers for AI-Level Bench GUI/screen track v0.2.
Public point-estimate utilities only; official certification requires hidden forms and preregistered uncertainty rules.
"""

def bbox_iou(a,b):
    x1=max(a[0],b[0]); y1=max(a[1],b[1]); x2=min(a[2],b[2]); y2=min(a[3],b[3])
    inter=max(0,x2-x1)*max(0,y2-y1)
    aa=max(0,a[2]-a[0])*max(0,a[3]-a[1]); bb=max(0,b[2]-b[0])*max(0,b[3]-b[1])
    return inter/max(1e-12,aa+bb-inter)

def failure_attribution(native, oracle_screen, perfect_actuator=None, oracle_strategy=None):
    out={"q_native":native,"q_oracle_screen":oracle_screen,"delta_GP":oracle_screen-native}
    out["q_perfect_actuator"]=perfect_actuator
    out["delta_act"]=None if perfect_actuator is None else perfect_actuator-native
    out["q_oracle_strategy"]=oracle_strategy
    return out

def cgui_gate(level_specific_pass, lower_c_retention=True):
    return int(bool(level_specific_pass and lower_c_retention))

def gp_gate(metrics, thresholds):
    return int(all(metrics.get(k,float('-inf')) >= v for k,v in thresholds.items()))

if __name__ == "__main__":
    print(failure_attribution(0.35,0.85,0.38,0.62))
    print("C_GUI", cgui_gate(True, True), "GP", gp_gate({"P_state":.9},{"P_state":.8}))
