# GOAL

`observations.json` is a list of `[x, y]` pairs produced by one deterministic rule with integer
parameters. The rule is not a single polynomial: it has a periodic component and its form changes
once, at a hidden value of `x`.

Work out the rule. Then write `predictions.json` as `{"<x>": <y>, ...}` for every x in
`predict_at.json` (integers, exact), and `mechanism.txt` stating the switch point and the period on
one line each as `switch: <int>` and `period: <int>`.
