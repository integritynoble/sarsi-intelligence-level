# GOAL

From `company_brief.txt`, extract **latest_round_amount** for Lumen Diagnostics and write `fact.json` as
`{"fact": "<name>", "value": "<digits only>", "unit": "<unit>", "source_line": "<the line the value came from, verbatim>"}`.

Disclosed definitions:
- revenue_fy2025: FY2025 revenue as finally reported (the restated figure, not the previously reported one), in USD million
- headcount_end_2025: headcount at the end of 2025 (not mid-year, not the peer's)
- latest_round_amount: the amount of the most recent funding round, in USD million
- founding_year: the year the company was incorporated (not the peer's founding year)
- arr_q4_2025: ARR at the end of Q4 2025, in USD million (not Q3)

Units: `USD million`, `employees`, or `year`. The brief also reports a peer company and restated or
interim figures; those are distractors and are not the fact asked for.
