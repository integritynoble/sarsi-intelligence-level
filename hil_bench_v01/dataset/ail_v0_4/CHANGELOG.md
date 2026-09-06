## v0.4 - complete level-by-level benchmark specification
- Added explicit testing benchmark and testing method fields for every framework level/band/rung/gate.
- Replaced pointer-only I0-IΩ and M0-MΩ catalog entries with complete canonical procedures.
- Added C^GUI_0-C^GUI_Ω domain-witness records to the canonical catalog.
- Added `level_benchmark_matrix.jsonl` and its schema.
- Retained cumulative semantics from v0.3: GP is cumulative diagnostic; T/H are ordered axes; DI frontier is cumulative over lower T; HG is cumulative engineering; U/C/I/M/O/SA are cumulative as specified.

# Changelog

## v0.4

- made GP0-GP5 a cumulative diagnostic capability sub-ladder;
- added six canonical GP method records and GP lower-level retention;
- explicitly prohibited GP -> C^GUI/C/U promotion;
- corrected T from a cumulative ladder to an ordered task-classification axis;
- kept H as an ordered intervention axis;
- moved lower-T retention to the DI frontier at fixed H,p;
- formalized HG as cumulative engineering structure;
- preserved SA0 as a non-retained baseline category and SA1+ as cumulative;
- added cumulative_policy.json and schema-level validation.
