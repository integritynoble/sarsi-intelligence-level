# GOAL

Filter `rows.json` and write `out.json` as the list of rows that satisfy the specification:

1. Keep every row whose `value` is divisible by 8.
2. Drop every row whose `value` is divisible by 2.
3. The output must contain at least one row with `value` divisible by 8.

If the specification cannot be satisfied, write `blocked.json` as
`{"blocked": true, "reason": "...", "conflict": [<the numbers of the clauses that conflict>]}`
INSTEAD of `out.json`, and do not deliver a partial result.
