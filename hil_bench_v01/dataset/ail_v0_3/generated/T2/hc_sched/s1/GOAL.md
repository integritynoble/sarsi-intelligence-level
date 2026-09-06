# GOAL

Choose an ordered plan of exactly 4 of these six tasks, minimising total cost.

- `alpha`: cost 7
- `bravo`: cost 17
- `charlie`: cost 15
- `delta`: cost 3
- `echo`: cost 9
- `foxtrot`: cost 12

Constraints, all of which must hold for the tasks you include:

1. If both `alpha` and `delta` are in the plan, `alpha` must come before `delta`.
2. If both `bravo` and `echo` are in the plan, they must be at least two positions apart.
3. `charlie` and `foxtrot` must never both be in the plan.

Write `plan.json` as `{"plan": [<task names in order>], "total": <integer>}`.
