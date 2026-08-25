# External Benchmarks and HIL

External benchmarks are treated as evidence sources, not as replacements for HIL-native
longitudinal and harness tests.

Examples:
- HLE, MMLU-Pro, GPQA, FrontierMath, ARC-AGI, MMMU, RULER and LongBench contribute mainly to C.
- BFCL, SWE-bench, tau-bench, BrowseComp, GAIA, OSWorld, WebArena and Terminal-Bench contribute mainly to DI.
- SimpleQA may be paired with calibration/abstention protocols to contribute limited SA evidence.
- Chatbot Arena/LMArena is useful as an ecological real-user signal but should remain outside core HLIS unless a frozen protocol is declared.

The spreadsheet `External_Registry` contains the version-lock rule and official URL for
each registry entry. No third-party benchmark content is redistributed.
