# Merged into `hil_bench_v01` (canonical) on 2026-09-05

Everything here was merged into `../hil_bench_v01` at the owner's direction: `o_families.py` (O0/O1),
`llm.py` (as `llm_exec.py`, the bare-model executor), `extract.py`, the scoring anchors and `o_level`,
`band_rate`, the five test modules, and `tools/diagnose_hidden_law.py`. One defect was fixed on the way
(`o1_generate_pair` raised `StopIteration` on seeds whose rule named neither token).

Do not add to this tree. Add to `hil_bench_v01`; run `python3 -m pytest -q tests` and
`python3 -m hilbench selftest` there.
