ANCILLARY MATERIAL FOR "MEASURING THE UNIFIED INTELLIGENCE LEVEL"

Unified_Intelligence_Paper_Dataset.zip
  Machine-readable records for the 48-episode harness-ladder measurement
  and the 24-episode matched regime-switch comparison, together with schemas,
  analysis code, validation code, documentation, and checksums.

HIL_Benchmark_Library_v1_1.zip
  The audited benchmark library, starter instances, schemas, scoring tools,
  specification-key checks, concordance-audit tool, and audit report discussed
  in the paper.

The paper states the limitations of these artifacts. Bound starter instances
are development examples, not hidden certification items. Specification-only
rows are not runnable evidence. The archived frontier executor identifier is
missing and is not inferred.

Internal release-directory and documentation names retain their original
version identifiers. Version 2.3 revises the manuscript (delivered-outcome primitive, named
confidence interval, accurate data statement, figures, captions) and adds the
delivered term and the confidence interval to tools/analyze.py in the paper
dataset; the frozen measurement records themselves are unchanged.

Validation commands after extracting the respective archives:

  python3 tools/validate.py
  python3 tools/validate_library.py data/task_catalog.csv
  python3 tools/audit_items.py
