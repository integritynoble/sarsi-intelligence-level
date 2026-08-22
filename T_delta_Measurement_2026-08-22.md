# Measuring T_δ

## First reading of authorization latency in the deployed console

*2026-08-22 · Instrument: [`tools/tdelta.py`](tools/tdelta.py)*

---

## Why this quantity

Once a loop's automated steps are cheap, its iteration rate is bounded by the steps that are not
automated. For a mature software loop that set contains exactly one member — deploy — so
ρ<sub>max</sub> = 1/*T*<sub>δ</sub>, where *T*<sub>δ</sub> is the interval between a candidate being
available and its promotion being authorized.

*T*<sub>δ</sub> is the only quantity in this corpus that is both **decisive** and **cheap to measure**.
Decisive because SARSI-L §4.5's crux — whether compensated loops can track closed ones indefinitely —
lists a falling *T*<sub>δ</sub> under AI-augmented review as evidence for H₂. Cheap because the
authorization events are already timestamped.

Six documents in this repository say it should be measured. This is the attempt.

## Method

The instrument reads a hash-chained audit log, pairs each `candidate_registered` with the next
`promote_version` carrying the same (kind, name, version), and reports the interval.

Three decisions in it are worth stating, because each is a way the measurement could have been made
to look better than it is.

**Censored observations are kept.** A candidate registered and never promoted is an observation —
*at least this long* — not an absence. Dropping such rows measures the subset that happened to
finish, which is a different quantity and is biased fast.

**Chain linkage is verified.** Each record's `prev_hash` must equal the previous record's `hash`. This
does not verify the hashes themselves, which needs the preimage convention, but it catches a record
removed from the middle.

**Intervals below a floor are excluded from the estimate and reported separately.** A promotion
authorized seconds after its candidate was registered was not reviewed; the signature was produced by
the same process that proposed. That is a separation failure, and the interval measures a script.
Default floor 60 s — an order-of-magnitude bound on a human reading an audited score and signing, not
a calibrated threshold.

## What exists to measure

A bounded search of this machine found **one** production audit chain:
`~/.local/share/singularity-web/audit.jsonl`, 8 records. The parallel test registry is empty; the
other registries found are throwaway state under `.claude/jobs/`. No control-plane `runs/` or
`eval/held_out/` trees exist on this host.

## Result

```
records            8
chain linkage      OK
paired             2
censored           1   (registered, never promoted)
orphan promotions  1   (promoted with no registration)

pairs:
  agent/proto-tutor-quizzes-cell-79983/v2    T_d =        5.5 s  <-- below floor
  agent/proto-tutor-quizzes-cell-79983/v3    T_d =        0.0 s  <-- below floor

censored:
  agent/proto-r/v2                           T_d >  2 106 001 s  (24.4 days)

T_delta: NO reviewed authorizations in this log.
```

> **T<sub>δ</sub> has never been observed.**

Not "*T*<sub>δ</sub> is low." The system has never completed a reviewed authorization recorded with
timestamps at both ends. Unmeasured is off the scale, not the bottom of it.

Both paired intervals are 5.5 s and 0.0 s. A human cannot read an audited score and produce an Ed25519
signature in zero seconds, and the `promote_version`, `owner_signature`, and `candidate_registered`
records for v3 share a timestamp to the second. These are scripted promotions from a prototype
exercise — the `proto-` names say as much — and they measure the script, not an authorization.

**The one datum that is not a script points the other way.** `proto-r/v2` was registered on
2026-07-29 and has not been promoted in 24.4 days. If that is representative, *T*<sub>δ</sub> is on
the order of weeks and ρ<sub>max</sub> ≈ 4.7 × 10⁻⁷ s⁻¹ — **about fifteen iterations per year**, and
the two sub-minute readings are the outliers rather than the signal.

That single censored row is worth more than both pairs, which is the argument for keeping censored
observations in the first place.

## Two structural blockers

**1 — The promotions table has no timestamp.** The registry's system of record is

```sql
CREATE TABLE promotions (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         kind TEXT, name TEXT, version TEXT, metadata TEXT)
```

There is no `ts` column, so **the registry cannot answer this question at all.** Every timestamp used
above came from the audit chain, which is a side record. A quantity that bounds the system's iteration
rate is not recorded by the table that records the event.

**2 — The D2 loop emits no candidate-available event.** `~/.local/share/singularity-web/paramloops/`
is empty: the playbook loop has never promoted. Even when it does, its propose → `yes` cycle writes no
`candidate_registered` analogue, so it produces no interval to measure. **Measuring per depth is what
tests whether the gate ladder is real** — if *T*<sub>δ</sub> is flat across D1–D4, the ladder is
nominal — and one of the two shipped depths currently cannot be measured.

## The fix

Not implemented here: both changes touch a live system's schema and its promotion path, which is a
production write and the owner's call.

1. **Add `ts` and `eval_ref` to `promotions`.** Backfill from the audit chain where seq allows; leave
   null where it does not, rather than inventing a value.
2. **Emit `candidate_available` when a candidate is first offered for signature**, in both the D2
   playbook loop and the D3 scaffold loop, carrying the same (kind, name, version) key so the existing
   pairing works unchanged.
3. **Tag each record with its depth** (D1–D4), so per-depth *T*<sub>δ</sub> is separable and B-Rule 3
   becomes checkable rather than asserted.
4. **Run `tools/tdelta.py` on a schedule** and keep the series. One reading is not a measurement;
   the crux in §4.5 turns on whether *T*<sub>δ</sub> **falls**, which needs a trend.

Step 2 is the one that matters. Without a candidate-available event there is no interval, and no
amount of downstream instrumentation recovers it.

## What this changes in the corpus

`SARSI_Applied_Profiles.md` reported the platform's *T*<sub>δ</sub> as "unmeasured." That was right
and understated. It is not merely unmeasured but **unmeasurable from the system of record**, and the
first attempt to measure it found that two of the three available data points are artifacts of a
script rather than observations of an authorization.

The claim in `Capability_Is_Not_A_Level.md` §4.2 — that *T*<sub>δ</sub> is the only cheaply measurable
axis in the paper — survives, with a caveat this reading supplies: **cheap to measure once the events
exist, and they mostly do not.**
