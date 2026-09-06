# GOAL

Choose an ordered plan of exactly 4 of these six tasks, minimising total cost.

- `alpha`: cost 15
- `bravo`: cost 16
- `charlie`: cost 13
- `delta`: cost 16
- `echo`: cost 8
- `foxtrot`: cost 5

Constraints, all of which must hold for the tasks you include:

1. If both `alpha` and `delta` are in the plan, `alpha` must come before `delta`.
2. If both `bravo` and `echo` are in the plan, they must be at least two positions apart.
3. `charlie` and `foxtrot` must never both be in the plan.

Write `plan.json` as `{"plan": [<task names in order>], "total": <integer>}`.
