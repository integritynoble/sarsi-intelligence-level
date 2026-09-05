# HIL-Core v1

HIL-Core v1 is a small, executable research prototype for measuring a frozen
model--harness pair across Cognitive (C), Individual (I), Organizational (O),
Delegation (DI), and operational Self-Awareness (SA) tasks, with Memory (M)
reported as a supporting prerequisite. It runs on Python 3 using only the
standard library.

It deliberately makes no measured claim about Codex, Claude Code, Qwen,
OpenCode, or any other system. The included profiles are unfilled manifests,
not scores. This compact synthetic suite has not been psychometrically
calibrated, is not yet a measure of general intelligence, and is not evidence
that it replaces ARC-AGI or another benchmark. The point of v1 is to make the
proposed measurement contract runnable, cheap to audit, and easy to extend.

## Start in under a minute

From this directory:

```bash
python3 -m hilbench validate
python3 -m hilbench run --split dev --mode quick --adapter oracle
python3 -m hilbench run --split validation --mode full --adapter mock
python3 -m unittest discover -s tests -v
```

`oracle` is an answer-key apparatus self-test and `mock` is a deterministic
abstaining plumbing test. Neither is a candidate result. Quick mode runs 7
tasks on the individual track or 8 on the organization track; it is always a
screen, never certification. Full mode runs 22 or 25 tasks respectively.

## Evaluate a process

The generic adapter sends one JSON request on stdin and expects exactly one JSON
response line on stdout. It receives no answer key. The command is an argument
vector and is executed directly; no shell is used.

```bash
python3 -m hilbench run \
  --split dev --mode quick \
  --profile profiles/codex.json \
  --adapter subprocess \
  --events run-events.jsonl \
  --output pair-report.json \
  --command python3 examples/abstain_agent.py
```

Put `--command` last because every remaining argument belongs to the candidate
process. See [PROTOCOL.md](PROTOCOL.md) for the wire format. The Codex, Claude
Code, and OpenCode+Qwen profiles contain placeholders: copy one, enter exact
model/harness versions and hashes, declare the resource envelope, and only then
run it.

## Public and organizer-private evaluation

- `tasks/public/dev.jsonl` and `validation.jsonl` are public parameter specs;
  their keys are public so developers can audit the generators and scorer.
- `organizer_private/` contains the certification task specs, independent
  mechanisms, and keys. It is for an organizer checkout only.
- Certification families and mechanisms are disjoint from the public families;
  the private split is not a random sample of public rows.
- `python3 -m hilbench package` builds
  `dist/hil-core-v1-public.zip` from an explicit allowlist. The entire
  organizer-private tree is excluded and the archive is inspected afterward.
- A private full run is requested with `--split certification --mode full
  --allow-private`. The software marks a complete candidate report as
  `organizer_review_required`; it never self-certifies a score.

Never publish a private task, key, prompt, response containing hidden material,
or a model trace that reconstructs it. Rotate a family after suspected exposure.

## What the report means

The primary experimental unit is the frozen pair, not the model alone. A report
contains:

- 0--100 achievement, an ordinal level, Wilson interval, and coverage for every
  applicable coordinate;
- an explicit `not_applicable` O result for an individual, distinct from an
  applicable but `unassessed` coordinate;
- M beside I, excluded from HLIS to avoid double-counting;
- the delivered-outcome DI surface, false completions, and cumulative T frontier
  at every measured H budget;
- cumulative gated U*, a named next-gate bottleneck, and pair-level HLIS;
- resource fields, including explicit `unassessed` values when a candidate does
  not report tokens, cost, human load, or compute.

An incomplete required coordinate makes HLIS `null`; missing evidence is never
silently scored as zero. Conversely, a measured zero remains zero and forces the
geometric mean to zero.

## Model-HIL, not a mislabeled bare-model score

To characterize an LLM, hold the exact model fixed and obtain pair reports under
the three reference manifests in `profiles/reference_harnesses/`:

1. `HIL-REF-HG0-v1`: minimal stateless direct solver;
2. `HIL-REF-HG1-v1`: persistent task state, preregistered criterion, and an
   independent acceptor, without verifier-driven retry;
3. `HIL-REF-HG2-v1`: HG1 plus bounded planning/tool routing and one
   verifier-driven correction attempt.

Then compose the curve:

```bash
python3 -m hilbench curve --reports hg0.json hg1.json hg2.json --output model-hil.json
```

The output keeps the curve primary and reports HIL-Level, HIL-AUC,
HIL-Ceiling, and Harness Gain. Truncated curves are labeled incomparable to a
complete curve. A submitted Codex/Claude Code/OpenCode harness result is an
agent-pair score unless that harness implements the frozen reference manifest.

## Tracks and limitations

Use `--track individual` for one persistent decision locus. O is N/A there and
is omitted from the geometric mean. Use `--track organization` only when the
evaluated system actually has multiple differentiated members and evidence flow;
O is required on that track.

The v1 tasks are deterministic, structured probes through U2. Their simulated
restart, revision, coordination, and bounded-assistance fields are inexpensive
proxies; they do not establish long-horizon learning, real process persistence,
open-world autonomy, consciousness, or organizational emergence. Certification
worthy of a public leaderboard additionally needs repeated runs, human
calibration, adversarial item audit, contamination controls, real restart and
longitudinal protocols, cost verification, and a much larger hidden bank.

Reference implementation assistance is attributed to OpenAI Codex. That credit
is provenance, not a benchmark result or endorsement.

## License

See [LICENSE](LICENSE). Dataset limitations and intended use are in
[DATA_CARD.md](DATA_CARD.md).
