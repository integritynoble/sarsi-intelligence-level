# GOAL (O0: routing)

Complete the task `regional_total` with the three roles above and write `org_record.json` as
`{"plan": [{"role": "<role>", "task": "<sub-task>"} in dispatch order],
 "execution": {"kept_rows": <count of in-scope rows>, "grand_total": <sum>, "top_region": "<region>"},
 "verification": {"checked": ["<what the verifier checked>", ...], "verified_total": <figure verified against the data>, "sign_off": true}}`.

The verifier must have checked the figure against the data and stated it; a sign-off that
states nothing it checked is not a sign-off.
