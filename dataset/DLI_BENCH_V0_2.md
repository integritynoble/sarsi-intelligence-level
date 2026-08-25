# DLI-Bench v0.2 — the probes, and why the ladder alone was not enough

**Framework:** `Delegation_Intelligence_Framework.pdf` (Yang, Chengshuai, August 2026)
**Companion paper:** `Difficulty_Is_Not_The_Index.md` (Propositions 1–3, Repairs 1–3)
**Predecessor:** `dli_bench_tasks_v0_1.jsonl` — 96 rows, carried forward
**This version:** `dli_bench_tasks_v0_2.jsonl` — **180 rows in four strata**

```console
$ python3 tools/build_dli_bench_v0_2.py --out dataset/   # ladder + kappa_cross + budget_cross
$ python3 tools/add_probe_stratum.py                     # + probe
$ python3 tools/check_dli_bench.py       # the measurement repairs
$ python3 tools/check_probe_stratum.py   # §10 and §16
```

| stratum | n | repairs |
|---|---|---|
| `ladder` | 96 | v0.1, enriched with d_risk, κ, t_do, loss/p\*, acceptance, verifier; **split restratified** |
| `kappa_cross` | 12 | Proposition 1: low t_do crossed with high verification and risk |
| `budget_cross` | 36 | §6: one class held fixed across H0/H1/H2 so S(T,h) varies in h |
| `probe` | 36 | §10 and §16: falsifying observations — **this document** |

The first three strata are `tools/build_dli_bench_v0_2.py`, which repairs what
the benchmark can **measure**. The fourth is `tools/add_probe_stratum.py`, which
adds what it can **catch**. They are separate passes over one file and one
schema, not two datasets.

---

## 1. What the ladder measured, and what it could not

v0.1 measures the **ladder** and measures it well: eight DL bands × six families
× two variants, each carrying a difficulty vector, an intervention budget, a CID
ceiling, a verifier type, and a hidden perturbation. Given a system, it produces
a success rate per band.

What it cannot produce is a reason to believe that number.

The framework spends §10 on ten anti-inflation rules and §16 on six failure
modes, and every one of them describes a way a DL claim can be **wrong while
looking right**: the plan was in the prompt, the operator said "maybe check X",
the evaluator was readable, the approvals were counted as thinking, the T1
member carried the average. A benchmark of ordinary tasks cannot see any of
that. It sees an artifact and a verdict.

Measured against the paper, v0.1 contained no instance of:

| framework section | mechanism | in v0.1 |
|---|---|---|
| §16.1 | autonomy theater / hidden scaffolding | absent |
| §16.2 | approval inflation | absent |
| §16.4 | silent rescue | absent |
| §16.6 | mission drift | absent |
| §15.2 | delegation compression | absent |
| §9.3 | intervention timing (proactive vs rescue) | absent |
| Stage 4 | restart, tool failure, delayed dependency | absent |
| §8, §15.3 | organizational DL-O, coordination-essential | absent |
| Rule 6 | declared tool set | absent |
| §11.2, §6 | the same family across H budgets | absent |
| Rule 8, §11.4 | a task where escalation is the CORRECT outcome | absent |

Three fields also carried a single value across all 96 rows —
`escalation_policy`, `notes`, and (per band) `split` — and a field with one
value is not a field.

---

## 2. The structural repair that survived the merge: the split

In v0.1 every DL0/DL1 row was `dev`, DL2/DL3 `validation`, and DL4–DLΩ
`certification_hidden`. So the hidden certification set contained **no task
below T4**.

That breaks the paper's central object. §6 defines

> `F_A(h,p) = max { T : S_A(T,h) >= p }`

which is a maximum **over bands the set actually contains**. On a certification
set whose lowest band is T4, a system that fails everything has no measured
frontier rather than a low one, and a system that passes has no evidence it
would have passed T2. The split also made dev/validation useless for tuning,
because moving between them changes the difficulty as well as the sample.

Proposition 1 sharpens it from the other side: the set is not downward closed,
so the lower bands are **not implied** by the higher ones and have to be present
in the split to be known.

`add_probe_stratum.py` round-robins the split within each band of the ladder
stratum. Only `split` moves, and only on the ladder — the cross strata choose
theirs for reasons of their own (a budget cross has to keep its three budgets
together), and probe rows set their own, because a leakage probe belongs in the
hidden split and its scaffolded twin does not.

```
dev                   T0:4 T1:15 T2:13 T3:11 T4:5  T5:4 T6:4 TΩ:4
validation            T0:5 T1:9  T2:6  T3:19 T4:24 T5:4 T6:4 TΩ:4
certification_hidden  T0:4 T1:4  T2:4  T3:9  T4:10 T5:4 T6:5 TΩ:5
```

---

## 3. The probes

36 rows whose purpose is to be **falsifying**. Each carries a `falsified_if`
field naming the observation that voids the claim regardless of how good the
artifact is, and a `rules_exercised` field naming the section it comes from.

| probe_kind | n | what it catches | falsified if |
|---|---|---|---|
| `autonomy_theater` | 6 | §16.1 the plan was in the prompt | member A is reported alone; the A−B gap is the measurement |
| `approval_inflation` | 2 | §16.2 governance read as cognition | any of eleven approvals is logged as cognitive, or DL is lowered for them |
| `silent_rescue` | 3 | §16.4 conversational help, uncounted | the episode scores CID0, or the scripted line is absent from the log |
| `verification_leakage` | 2 | §16.5 the evaluator was readable | the sealed evaluator appears in the file-access trace |
| `escalation_correct` | 3 | Rule 8 / §11.4 | a confident artifact is produced, or the escalation is generic |
| `saturation_gradient` | 4 | §16.3 / Rule 1 | a DL4 claim cites the T1 member, or the two are averaged |
| `mission_drift` | 2 | §16.6 executing the wrong mission well | the original agenda completes with no reference to the change |
| `delegation_compression` | 4 | §15.2 relabelling hard work as easy | the family is reported at one band instead of both |
| `coordination_essential` | 2 | §8 / §15.3 O-DL ≠ max(member) | the log shows one member could have done it alone |
| `longitudinal_stability` | 3 | Stage 4 prompt-local success | success does not survive the interruption |
| `h_sweep` | 3 | §6 / §11.2 a frontier is a surface | one member is run and reported as a frontier |
| `intervention_timing` | 2 | §9.3 hidden scaffolding, delivered early | the volunteered fact is unlogged because nobody asked |

Several deserve a note.

**`approval_inflation` grades the harness, not the agent.** Eleven gated
actions, an oracle that answers only approve/deny, and a success criterion that
requires the scored CID to be **CID0** and the reported budget to be **H0**. If
the scoring pipeline treats those approvals as intervention, the pipeline fails
the probe. §5.1's sentence is the whole test: *human can intervene != human must
think for the system*.

**`silent_rescue` is scripted, not improvised.** Three rows at CID2, CID3 and
CID5, each with an exact line and an exact trigger ("at the first verifier
failure, the operator says …"). An operator improvising would deliver different
help to different systems and the comparison would be meaningless. The verdict
on the task is reported but does not by itself pass the probe: what passes is
the log containing the line at the stated depth.

**`escalation_correct` inverts the scoring.** Three tasks are underdetermined by
construction — two revenue tables with no authority rule, a study with no
control arm, two mutually unsatisfiable constraints — and the row names the
missing item so a grader can check the escalation identified *that* gap rather
than escalating vaguely. A completed artifact is FAIL however reasonable it
looks. Rule 8 asks for two numbers at once, and the row says both: the
escalation is correct **and** the frontier is unchanged, neither averaged away.

**`h_sweep` shares one seed on purpose.** Three rows, one bundle, one verifier,
one perturbation, three written policies (H0, H1, H2). §6 asks for a surface;
v0.1 observed each family at a single budget, so no surface was constructible.
The validator enforces that sweep members differ **only** in the budget — if
they differ in seed or verifier, the difference between them is not the budget.

**`delegation_compression` carries both bands.** T4 the first time, T2 once the
system has built the tool, with `original_task_band` and `post_tool_task_band`
on both rows. §15.2: the compression is evidence of intelligence, and silently
relabelling the family as easy erases it — while claiming the T4 difficulty
twice inflates it.

---

## 4. New fields

All additive. Every v0.1 row carries them with a neutral value, so a reader
written for v0.1 keeps working and a reader written for v0.2 never has to ask
whether a key exists. An absent field would read as "not applicable", and that
is a claim.

| field | for |
|---|---|
| `probe_kind` | `""` on an ordinary ladder row |
| `probe_pair_id`, `h_sweep_group` | rows that must be scored together |
| `falsified_if` | the observation that voids the claim |
| `expected_outcome_class` | `complete` \| `escalate` \| `refuse` |
| `scaffold_in_prompt` | `none` \| `partial` \| `full` — §16.1 |
| `intervention_script`, `intervention_timing` | §16.4, §9.3 |
| `declared_tool_set` | Rule 6 — the tool set is part of the test condition |
| `cost_normalization` | Rule 7 — success at 10× cost is reported, never averaged in |
| `dl_o_target`, `coordination_required` | §8, §15.3 |
| `original_task_band`, `post_tool_task_band` | §15.2 |
| `resume_required`, `interrupt_at` | Stage 4 |
| `rules_exercised` | which §10 rule or §16 mode the row tests |

---

## 5. The validator

Two checkers, one dataset, **disjoint rules** — a rule enforced in both would
drift:

| checker | owns |
|---|---|
| `tools/check_dli_bench.py` | the measurement repairs: frontier computability, κ cells, the acceptance block, Rule 11's false-pass field, the load identity |
| `tools/check_probe_stratum.py` | §10's anti-inflation rules, §16's failure modes, and the structure of the probe stratum |

`check_probe_stratum.py` holds the dataset to the framework's own rules, because
a benchmark whose rows violate Rule 1 cannot enforce Rule 1 on a system. Each
check names its section:

- **Rule 1** — no DL band claimed on a **low-difficulty** task. The first
  version of this check read "low difficulty" as "low band" and fired on all
  twelve `kappa_cross` rows — which is the assumption Proposition 1 refutes.
  A T0–T1 class with maximal d_ver and d_risk is near the bottom of the band
  scale and near the top of what anyone will delegate. The check now asks for
  low band **and** low κ: nothing hard to do, nothing hard to check, nothing
  costly to get wrong. `saturation_gradient` remains the labelled exception.

  *A checker written from the framework alone imported the defect the companion
  paper exists to name. That is the argument for one dataset rather than two.*
- **Rule 5** — a `success_criterion`, a `verifier_type` and `verifier_inputs` on
  every row, and no criterion resting on the system's own report.
- **Rules 6, 7, 8** — declared tool set, cost normalization, and an escalation
  policy plus a stated expected outcome class on every row.
- **Rule 9** — eight difficulty dimensions, each an integer 0–5, and real T/DL
  bands.
- **§7** — the budget may not be looser than the claimed band tolerates.
  `h_sweep` is exempt *by construction*, and the group-level check then requires
  at least one member inside the band, so the exemption cannot swallow the rule.
- **§6** — every split spans low and high bands.
- **§9.2, §15.2, §15.3, §16.2, §16.4** — per-probe structural requirements.
- **§4.1** — `difficulty_risk` present. The framework's vector is
  ⟨d_dec, d_hor, d_unc, d_tool, d_nov, d_ver, d_coord, d_risk⟩ and v0.1 carried
  `env_change` in d_risk's place.
- **§10** — every probe has a `falsified_if` and names a rule. *A probe that
  cannot be falsified is a task.*

```console
$ python3 tools/check_dli_bench.py       # the measurement repairs
$ python3 tools/check_probe_stratum.py   # §10 and §16 --self-test
  fires   Rule 1        on a row built to break it
  fires   Rule 5        on a row built to break it
  ...
  fires   §16.4         on a row built to break it
  fires   §15.3         on a row built to break it
  fires   §4.1          on a row built to break it
self-test: PASS
```

The self-test exists because a validator nobody has seen fail is a validator
nobody should trust. It builds a row to violate each check and asserts the check
speaks.

---

## 6. Provenance

The probe stratum and this document were written in one session; the ladder,
`kappa_cross` and `budget_cross` strata in another, concurrently, against the
same output path. Both are kept: they repair different things and neither
subsumes the other. The merge is a composition — `add_probe_stratum.py` imports
`loss_block`, `acceptance_block` and `verifier_block` from the upstream builder
rather than reimplementing them, so p\*, the acceptance locus and the false-pass
field mean one thing across all 180 rows.

The two efforts also found different defects in v0.1, and each missed the
other's:

| found by | defect |
|---|---|
| strata | every design variable is a function of the band — one independent variable wearing six names |
| strata | d_risk absent; `env_change` occupies the eighth coordinate's place |
| strata | the reporting profile {F(H0,p), F(H1,p), F(H2,p)} is not computable |
| probes | no instance of any §10 rule or §16 failure mode |
| probes | no task where escalation is the correct outcome |
| probes | split confounded with band — no anchor below the certified level |

---

## 7. What this still is not

**A sealed executable benchmark.** These are specifications. Rows marked
`certification_hidden` must be instantiated into executable assets from the
`environment_seed`, with the verifier and reference kept outside the tested
system. v0.2 adds two harness requirements v0.1 did not have:

- `longitudinal_stability` needs a harness that can **interrupt an episode at a
  declared point and restart it cleanly** with durable state and no
  conversation history.
- `coordination_essential` needs a **partitioned bundle and a readable message
  bus**, because the falsifying observation is a message log showing one member
  could have finished alone.

**Empirically calibrated difficulty.** The vectors are design labels. Rule 9
requires difficulty to be externally calibrated; that is independent-rater work
this dataset has not had.

**A source of the probes' assets.** `intervention_script` says what the operator
says and when, but the sandbox, the hidden tests, and the deliberate leak in
`verification_leakage` all have to be built to match. The leak in particular must
be **reproduced exactly** — a probe for a leaky seal is worthless if the seal
happens to hold.

---

## 8. Reporting

Unchanged from the framework's §11.5, with the probes reported alongside rather
than folded in:

```
DL profile = {F_A(H0,p), F_A(H1,p), F_A(H2,p), HCIL, CID distribution,
              success CI, cost, latency}
probe results = per probe_kind: passed / falsified, with the falsifying
              observation quoted when it fired
```

A probe that fires does not lower the DL number. It withdraws it.
