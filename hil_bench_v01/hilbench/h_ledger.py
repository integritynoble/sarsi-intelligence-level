"""The H class of an episode is a property of its transcript: every human intervention is classified by the COGNITION it
supplied, by a locus outside the pair, and the class is the highest one present.  Counts do not classify; content does."""
CLASSES = {
    "H0": (), "H1": ("unavailable_fact", "narrow_clarification"), "H2": ("bounded_clarification", "local_correction"),
    "H3": ("periodic_review", "moderate_guidance"), "H4": ("repeated_guidance", "next_step_correction"), "H5": ("major_step", "strategy", "decomposition"),
}
KIND_TO_CLASS = {k: c for c, ks in CLASSES.items() for k in ks}

def h_class(ledger: list) -> str:
    """ledger: list of {kind, text, by}.  An unknown kind is H5: what cannot be classified is charged at the top."""
    if not ledger: return "H0"
    return max((KIND_TO_CLASS.get(e.get("kind"), "H5") for e in ledger), key=lambda c: int(c[1]))

def within(ledger: list, declared: str) -> bool:
    return int(h_class(ledger)[1]) <= int(declared[1])
