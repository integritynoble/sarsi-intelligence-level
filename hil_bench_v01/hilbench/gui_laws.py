"""Method B (dataset v0.7): GUI/screen understanding is a DOMAIN of Cognitive Intelligence, not a level and not a family.

C^GUI_k is a GUI-grounded witness of the existing semantic level C_k; GP0-GP5 is a diagnostic perceptual subscale of
the representation supplied to cognition.  Containment: GP < C^GUI < C, and GP_g is never equivalent to C_g.  The gate
for a GUI-domain C level is the ordinary cumulative one, z_CGUI,k = V_GUI,Ck * K_C,<k; GP never promotes C by itself.
Failure is kept legible by matched arms: native screenshot, oracle screen graph, perfect actuator, optional oracle
strategy, with delta_GP = Q(oracle_screen) - Q(native) and delta_act = Q(perfect_actuator) - Q(native_actuator).  A
delivered-success endpoint counts once, as C or as DI, never both.  Systems without a screen modality report N/A.
"""
DOMAIN_PANEL = ("general", "science", "mathematics", "abstract", "code", "multimodal/spatial", "GUI/screen", "long-context")

GP_LEVELS = {
    "GP0": ("Pixel and text recognition", "recognises visible text, icons, colours and elementary features, claiming no task understanding"),
    "GP1": ("UI-element recognition", "distinguishes buttons, menus, fields, tabs, dialogs, lists, windows as interface objects"),
    "GP2": ("Spatial grounding and hierarchy", "grounds a referred element to the correct region; containment, adjacency, ownership, labeling, target relations"),
    "GP3": ("Interface-state understanding", "enabled/disabled, selected, focused, open/closed, loading, error, modal and analogous states"),
    "GP4": ("Dynamic GUI understanding", "tracks change across screenshots/actions: what changed, whether the intended effect occurred, what is unresolved"),
    "GP5": ("Novel-interface perceptual generalisation", "grounds and interprets unfamiliar software without application-specific scripting or memorised element paths"),
}
CGUI_WITNESSES = {
    "C0": "read, identify or localise one explicitly requested screen element with no hidden planning requirement",
    "C1": "infer the ordinary function of a visible interface element from screen context and a routine goal",
    "C2": "combine several GUI elements, states, spatial relations, panels, rows or constraints to answer a structured question",
    "C3": "construct or select an interface-navigation strategy and transfer it to a held-out layout or unfamiliar surface",
    "C4": "reason through a dense expert interface with ambiguity, interacting constraints and relevant distractors",
    "C5": "infer an unknown interface rule, workflow or transition model and predict sealed GUI states",
    "C6": "integrate GUI understanding with several genuinely necessary domains (code, mathematics, science, documents, spatial)",
    "CΩ": "create a new interface representation, parser, abstraction or method that causally expands the reachable GUI problem classes",
}
SPEC_ONLY = ("C6", "CΩ")   # development templates pending a secure executable environment
DIFFICULTY_VECTOR = ("N_e", "N_p", "d_h", "r_d", "rho_o", "N_w", "N_s", "d_t", "nu_l", "B_res")   # varies WITHIN a C level; never a pseudo-level
ARMS = ("native_screenshot", "oracle_screen", "perfect_actuator", "oracle_strategy")
GUI_LEVELS = set(GP_LEVELS) | set(CGUI_WITNESSES)

def failure_record(q_native, q_oracle_screen, q_perfect_actuator=None, q_oracle_strategy=None) -> dict:
    """F_GUI = (q_native, q_oracle_screen, q_perfect_actuator, q_oracle_strategy, delta_GP, delta_act)."""
    rec = {"q_native": q_native, "q_oracle_screen": q_oracle_screen, "q_perfect_actuator": q_perfect_actuator,
           "q_oracle_strategy": q_oracle_strategy, "delta_GP": q_oracle_screen - q_native,
           "delta_act": (q_perfect_actuator - q_native) if q_perfect_actuator is not None else None}
    rec["limit"] = "perception" if rec["delta_GP"] > 0.1 else ("action" if (rec["delta_act"] or 0) > 0.1 else "cognition")
    return rec

def cgui_gate(level_specific_pass: bool, lower_c_retention: bool) -> bool:
    """z_CGUI,k = V_GUI,Ck * K_C,<k; GP evidence is deliberately not an input."""
    return bool(level_specific_pass and lower_c_retention)
