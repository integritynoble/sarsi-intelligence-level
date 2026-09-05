"""Frozen public constants for HIL-Core v1."""

BENCHMARK_VERSION = "HIL-Core-v1.0.0"
PROTOCOL_VERSION = "1.0"
REPORT_SCHEMA_VERSION = "1.0"
CURVE_SCHEMA_VERSION = "1.0"
PROFILE_SCHEMA_VERSION = "1.0"
REFERENCE_LADDER_ID = "HIL-REF-v1"

CORE_COORDINATES = ("C", "I", "O", "DI", "SA")
SUPPORTING_COORDINATES = ("M",)
ALL_COORDINATES = CORE_COORDINATES + SUPPORTING_COORDINATES
INDIVIDUAL_DIMENSIONS = ("C", "I", "DI", "SA")
ORGANIZATION_DIMENSIONS = ("C", "I", "O", "DI", "SA")

REFERENCE_HARNESSES = (
    ("HG0", "HIL-REF-HG0-v1", 0),
    ("HG1", "HIL-REF-HG1-v1", 1),
    ("HG2", "HIL-REF-HG2-v1", 2),
)

DEFAULT_RELIABILITY = 0.80
DEFAULT_LEVEL_THRESHOLD = 0.80
DEFAULT_FALSE_COMPLETION_LOSS_RATIO = 1.0

LEVEL_NAMES = {
    "C": ("Reactive", "Contextual", "Compositional", "Strategic", "Expert", "Discovery", "Frontier-Generalizing"),
    "I": ("Transient", "Persistent", "Adaptive", "Self-Improving", "Recursive", "Discovery"),
    "O": ("Routing", "Persistent", "Adaptive", "Self-Improving", "Recursive", "Collective-Discovery"),
    "SA": ("Non-self-modeling", "State", "Capability", "Causal", "Self-change", "Metacognitive", "Mission-role"),
    "M": ("Ephemeral", "Persistent", "Structured-episodic", "Consolidating", "Self-managing", "Longitudinal"),
}

U_GATES = {
    0: {"C": 0, "I": 0, "O": 0, "SA": 0, "M": 0, "T": 0, "max_H": 5},
    1: {"C": 1, "I": 1, "O": 1, "SA": 1, "M": 1, "T": 1, "max_H": 3},
    # I2 requires independently demonstrated consolidating memory (M3).
    2: {"C": 2, "I": 2, "O": 2, "SA": 2, "M": 3, "T": 2, "max_H": 2},
}
