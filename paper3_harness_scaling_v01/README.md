# Paper 3 — Engineering Higher-Intelligence AI Agents: Harness Scaling Across Models and Domains (draft v0.1, 2026-09-03)

Pre-registered design + first measurements. Build: `./build.sh` → `main.pdf` (copied to
`Harness_Scaling_Across_Models_and_Domains_v0_1.pdf`). Edit `body.tex`, not `main.tex`.

Data sources: AI4Science `ai4science/harness/agents/delegation/{HSC_CLAUDE,HSC_CODEX,HSC_HAIKU,PAIRED_CLAUDE,PAIRED_HAIKU,RESULT,RESULT_CLAUDE}.txt`
and the v2.0 paper dataset (regime switch). `fig_hsc.pdf` is the v2.3 figure (same data).

Measured so far: one domain, three executors (two families), HG0–HG3 (delegation instantiation), H1 only.
Untested: H2 (intervention), H4 (transfer), H5 (self-improvement). §8 lists the next runs in cost order.
