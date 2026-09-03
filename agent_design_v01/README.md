# Agents That Earn a Level — draft v0.1 (2026-09-03)

*Harness Design Across Motors, with a Downloadable Fleet.* Companion to the Unified Intelligence
framework v2.3 (`../unified_v23`).

Build: `./build.sh` (latexmk; produces `main.pdf` and `Agents_That_Earn_a_Level_v0_1.pdf`).
Source is assembled from `preamble.tex` + `body_part1.tex` + `body_part2.tex`; edit the parts, not `main.tex`.

## What it contains

1. Introduction — levels are properties of the pair; the one-cell finding as a design target.
2. What a level requires — six coordinates, M gate, HG ladder, the three things an LLM cannot design, write-set depth.
3. Motors are adapters — Claude Code, Codex, OpenCode, Hermes behind one executor protocol; status of each.
4. The rung recipe — HG0–HG3 in three columns (contains / outside / promotes); the arms measurement (0/15 → 15/15).
5. Coordinate contracts — M, O, SA; the placement rule; apparatus rules.
6. Worked designs — sarsi-worker; the three motors; funding; job; social-media; learning; the eight research agents; DL0–DL3 binaries.
7. Catalogue — Table 6 (downloads, with commands) and Table 7 (fleet: target vs measured; every U cell empty).
8. How to measure what you built — cost-ordered protocol.
9. Limitations. 10. Conclusion. Availability.

## Facts the draft depends on (verified 2026-09-03)

- Motors on the build host: claude 2.1.258, codex 0.151.0 (npm), opencode 1.18.25 (present, never exercised by `sarsi-open`), hermes not installed (adapter only).
- Downloadables: AI4Science (PyPI `pwm-ai4science` 1.0.0; research-agent and sarsi packages in source tree only), eight `pwm-agent-*` dists (0.1.0), intelligence-level `dist/dli.pyz` + wheel 0.4.0, claude-pwm release 2.1.220, codex-pwm builds, openclaw-pwm npm.
- The fleet's funding/job/social-media/learning/research deployments are designs in a private repo that bind no runtime; the handoff record there says nothing in them has been executed.

## Open decisions for the author

- Authorship: listed as Chengshuai Yang alone; add Ting Xue if that is the intent.
- Whether to release the fleet charters (private repo) so Table 7 rows become downloadable.
- Whether to publish a fresh `pwm-ai4science` wheel so the research-agent and sarsi packages install from PyPI.
