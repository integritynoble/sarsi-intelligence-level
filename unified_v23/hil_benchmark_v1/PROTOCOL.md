# HIL-Core JSON response protocol 1.0

The subprocess adapter launches the candidate directly with an argument vector,
once per task. It writes one compact JSON object followed by a newline to stdin,
closes stdin, and accepts exactly one non-empty JSON line on stdout. Diagnostic
text belongs on stderr. A timeout, non-zero exit, extra stdout line, malformed
JSON, wrong version, or wrong task id is a protocol failure and a failed item.

## Request

```json
{
  "protocol_version": "1.0",
  "type": "task",
  "run_id": "uuid",
  "task": {
    "id": "dev-C-L0-100",
    "benchmark_version": "HIL-Core-v1.0.0",
    "split": "dev",
    "coordinate": "C",
    "level": 0,
    "family": "symbolic_composition",
    "mechanism": "affine_chain",
    "seed": 100,
    "track": "both",
    "quick": true,
    "difficulty": null,
    "prompt": "...",
    "input": {},
    "answer_schema": {"type": "object", "additionalProperties": false},
    "scoring": {"method": "exact_json", "weight": 1.0}
  },
  "context": {"mode": "quick", "expected_answer_is_hidden": true}
}
```

## Response

```json
{
  "protocol_version": "1.0",
  "task_id": "dev-C-L0-100",
  "answer": {"value": 10},
  "harness_accepted": true,
  "attempts": 1,
  "verification_responsive": null,
  "usage": {
    "input_tokens": 200,
    "output_tokens": 20,
    "llm_calls": 1,
    "cost_usd": 0.001
  }
}
```

Required fields are `protocol_version`, `task_id`, and `answer`.
`harness_accepted` is `true`, `false`, or `null`/omitted when the harness has no
independent acceptance step. Omitting it does not turn a wrong delivered answer
into a refusal: wrong plus `null` is a false completion. `attempts` defaults to
1. `usage` is optional; absent resource quantities are reported as unassessed.

The exact-JSON verifier ignores object key order but does not coerce strings,
numbers, arrays, or missing fields. Candidate output and answer keys are never
stored in the key-free event log; only verdicts and a response digest are kept.
