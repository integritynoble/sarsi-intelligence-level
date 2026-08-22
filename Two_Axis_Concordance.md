# Concordance

## The two-axis framework and the SARSI level documents, reconciled

*2026-08-22*
*Primary: [`Two_Axis_Intelligence_Level_Framework_AI_Agents.pdf`](Two_Axis_Intelligence_Level_Framework_AI_Agents.pdf) — I0–IΩ × O0–OΩ*
*Secondary: `SARSI-B`, `SARSI-I`, `SARSI-O`, `SARSI-Ω`, `SARSI_Level_Map.md`, `Capability_Is_Not_A_Level.md`*

---

## Why this document exists

Two frameworks for levels of intelligence now sit in this repository, written independently within
days of each other. Left alone they would drift — the failure mode this corpus has already seen at
smaller scale. This reconciles them: **the two-axis paper is primary**, the SARSI documents are
re-read as supplying bounds, a well-posedness result, and a measurement to it.

The convergence is substantial and worth stating before the differences, because independent
agreement is evidence and duplication is not.

---

## § 1 — Where they agree, independently

| Two-axis paper | SARSI documents | The shared claim |
|---|---|---|
| §2.1 *Intelligence level is not raw capability* | `Capability_Is_Not_A_Level` (title, thesis) | Level and capability are different objects |
| §2.4 *Improvement means better under an independent, predeclared evaluation. Merely changing is not improving* | SARSI-B §3, Proposition 1 | An improvement claim needs an evaluator the system did not author |
| §5.4 *Individual belief is not organizational truth* | SARSI-O §4.2 (separation), fleet self-state rule | The same rule at organizational scale |
| §6.1 *Persistence is not learning* | SARSI-B B-Rule 2 (accumulation is not improvement) | A memory file growing is evidence of operation |
| §6.3 *Code editing is not automatically self-improvement* | `Capability_Is_Not_A_Level` §6.3, the one-cell finding | Software an agent writes is not that agent's brain |
| §6.4 *Parallel agents are not automatically an adaptive organization* | SARSI-O §4.2, coverage and separation | Running N agents is a substrate, not an organization |
| §5.2 *All individual levels can coexist — and usually should* | SARSI-O §7, Proposition 6 | Heterogeneity is structural, not transitional |
| §5.1 *System = (I_i, O_j)* | `SARSI_Level_Map` §1 (a level is a profile) | No scalar; two coordinates minimum |
| IΩ loop: *Unknown → Discovery → Knowledge → Reorganization → Cognitive Tool → Better Intelligence → Deeper Unknown* | SARSI-Ω §3: reach, discovery, transduction, reorganization | The same loop, and the *Cognitive Tool* step is transduction |

Nine agreements, reached by different routes. The last is the most striking: SARSI-Ω derives that
transduction is the loop's **sole coupling** and therefore the only operator whose work compounds;
the two-axis paper independently places *Cognitive Tool* at the same position in the IΩ cycle.

---

## § 2 — Concordance of the individual scales

The two-axis I-scale is indexed by *the deepest layer changed through experience*. The SARSI brain
triple is indexed by *write set*. They are near-isomorphic, and where they differ the I-scale is
finer.

| I-level | SARSI triple | Note |
|---|---|---|
| **I0** Reactive | ⟨D0, closed, ∅⟩ | Exact |
| **I1** Persistent | ⟨D1, closed, self⟩ *with the write unvalidated* | **I-scale is finer** — see §3.1 |
| **I2** Adaptive learning | ⟨D1–D2, closed, self⟩ *with the write validated* | Θ fixed |
| **I3** Self-improving | ⟨D2–D3, closed, self⟩ | Θ<sub>t+1</sub> ≠ Θ<sub>t</sub> — the mechanism changes |
| **I4** Recursive | ⟨D3–D4, closed, self⟩ | The improvement process itself improves |
| **I5** Autonomous discovery | ⟨D3, closed, self + world⟩ | SARSI-Ω's discovery loop, closed objective |
| **IΩ** Open-ended | ⟨any, **open**, both⟩ | SARSI-B's objective-open level |

**Two SARSI axes have no I-scale counterpart** and are not redundant.

**Reach** — whose state a loop writes. This is what makes the role ⟨D0, closed, *other*⟩ expressible:
an entity with an empty self-write set, which is the only kind that may hold authority over another's
promotion. The two-axis paper needs this in §5.4 (individual belief must not become organizational
truth by the individual's own act) and has no coordinate for it.

**Authority ceiling** — what a system is *permitted* to do, orthogonal to what it can. A4 in the
deployed ladder is the highest ceiling and still carries no deploy authority, which is not
expressible as an I-level.

---

## § 3 — Where the two-axis paper is better

### 3.1 The I1/I2 split is a real distinction the write-set axis loses

SARSI-B's depth D1 says *memory is in the write set*. It does not distinguish a system that writes
memory from one whose later behaviour is measurably different because of it. The two-axis paper
splits exactly there — I1 persistent, I2 adaptive learning — and its transition test is precise:

> *Does matched future performance improve or adapt because the agent learned from prior experience,
> rather than merely replaying stored instructions?*

**This is the ablation SARSI-B §5 asserts is never run, stated as a level boundary rather than as a
complaint.** It is a better construction: a taxonomy whose boundary *is* the missing measurement will
not let a system past it on architecture alone. The concordance table above adopts the split, and the
SARSI depth axis should be read as coarse at D1 in consequence.

### 3.2 Improvement competence is the operational metric SARSI lacked

The two-axis paper defines

> IC = validated downstream gain caused by proposals ÷ proposal and evaluation cost

and requires an I4 claim to show IC *rising* across generations, not task score rising. SARSI-B says
gate strength should scale with write depth and offers no way to tell whether a deeper loop is
earning its cost. IC is that measure, and it is the correct denominator: an improvement process that
doubles gains while quadrupling evaluation cost has got worse.

### 3.3 Cognitive compression is the better argument for coexistence

SARSI-O §7 forces heterogeneity four ways — separation, the frontier shape, timescale, earned
authority. All four are structural. The two-axis paper adds an economic one that is stronger in
practice:

> expensive discovery → validated procedure → cheap execution

A difficult result may require I5 cognition once; after it becomes a verified procedure an I0 executor
runs it a million times. **Heterogeneity is not only forced, it is efficient**, and an organization
that ran everything at its highest available level would be wasting most of it. SARSI-O §7 should be
read with this as a fifth argument, and it is the one a practitioner will act on.

Its §5.3 bidirectional flow — observations up to principles, principles down to routines — is the
mechanism, and the SARSI corpus has no equivalent.

---

## § 4 — Where they disagree

Two real disagreements. Both are substantive rather than terminological.

### 4.1 Is the O-scale a ladder?

The two-axis paper presents O0–OΩ as an ordered scale in which each level subsumes the last. SARSI-O
§4 presents five **independent axes** — coverage, separation, throughput, referee externality, world
coupling — and argues they cannot be collapsed, on this ground:

> **Proposition 5.** An organization scoring zero on separation has no well-posed improvement loop
> regardless of its members' levels. Therefore an organization of maximal individuals with no
> separation of duties is *less* intelligent than a mixed organization of ordinary ones.

If that holds, separation is a **gate rather than a rung**: an organization can satisfy every
behavioural description of O4 — maintaining candidate policies, running canary evaluations, learning
which redesigns generalize — while proposing, judging, and adopting through one locus, and its
reported improvements are then self-certified. The O-number would be high and the improvement claims
void.

The two-axis paper does not miss the principle; §5.4 states it exactly. The disagreement is about
where it belongs. **We suggest it is not a level property but a precondition for any O-level above O1
to mean anything**, and that O-levels should therefore be reported as a pair — the behavioural level,
and whether separation holds. An unseparated O4 is not O4.

This is testable in the form §7 of the paper prefers: an organization with no separation should show
no advantage over one with it, on held-out outcomes, controlling for member level.

### 4.2 Does IΩ have a ceiling?

The two-axis paper is careful that IΩ is not "knows everything" — it is *sustained expansion of
reachable cognition*, and a mature open-ended intelligence may discover more structured unknowns as
it grows. That is right and SARSI-Ω agrees.

SARSI-I adds a bound the paper does not have. An individual is one global workspace; coherence
requires every contributing part to reach it within one decision cycle; therefore

$$R \le c\tau/2$$

**There is a largest possible individual at every decision speed, and scaling past it yields a society
rather than a greater mind.** A cycle of 1 ns permits a radius of 15 cm. Three further bounds follow —
aperture (how much can be present at once), self-opacity (a model is part of what it models), and the
referee (an individual cannot evaluate itself).

The consequence for the scale: **IΩ is not open-ended in every direction.** It is open-ended in what
it can come to know and bounded in what it can be. Past the coherence radius the correct coordinate
is not a higher I but a higher O — which the two-axis model can express and does not currently say.
And by the referee bound, IΩ is not attainable by an individual at all in isolation: the O-axis is a
*precondition* of the upper I-axis, not a parallel to it.

---

## § 5 — What the SARSI documents supply

Read as a companion rather than a rival, the corpus contributes four things to the two-axis framework.

**A well-posedness result.** §2.4's "merely changing is not improving" is stated as a definition;
SARSI-B §3 derives *why* — if the evaluator is inside the write set, the loop satisfies any criterion
by editing the criterion, and no observation distinguishes improvement from redefinition. This also
supplies the repair for IΩ, whose objective is by definition writable: a **frozen referee**, versioned
and laddered, without which open-ended evolution and drift are observationally identical.

**Physical bounds** (§4.2), which give the I-axis a ceiling and locate the I/O boundary.

**A measurement.** *T*<sub>δ</sub>, authorization latency, bounds a compensated loop's rate at
ρ<sub>max</sub> = 1/*T*<sub>δ</sub>. Measured on the deployed console 2026-08-22: **never observed** —
the promotions table has no timestamp column, and of three available data points two are scripted
self-signatures and one is a candidate outstanding for 24 days. See
`T_delta_Measurement_2026-08-22.md`. This is a concrete instance of §6's anti-inflation project: the
system of record cannot support the claim.

**An identity criterion.** At I3 and above the mechanism changes, so the paper's phrase *the same
individual lineage* (§6.3) needs a referent. SARSI-I §8: two states belong to the same individual iff
connected by an unbroken chain of provenance-linked evidence. Memory, goals, substrate, and behaviour
all fail — the last would make improving and dying indistinguishable.

---

## § 6 — Corrections to the SARSI placements

The two-axis paper's Table 1 is better evidenced than `SARSI_Applied_Profiles.md` §3 on exactly the
rows that document flagged as low confidence, which is what the provenance table was for.

| System | SARSI said | Two-axis says | Resolution |
|---|---|---|---|
| Grok bot | ⟨D0, closed, ∅⟩ — *very low confidence, not inspected* | **Grok chat I1; Grok Bot I2** | **Two-axis is right.** SARSI collapsed two products and under-rated both |
| OpenClaw | ⟨D0–D1⟩ — *low confidence, only the billing wrapper inspected* | **I1 basic; I1–I2 with active memory/promotion** | **Two-axis is right.** Configuration matters and SARSI had no basis to say so |
| Claude Code | ⟨D1, closed, self + other-inputs⟩ | I1 / O0–O1 | Agree. I1 not I2 — the ablation is unrun, so the learning claim is unsupported |
| Codex | ⟨D0–D1⟩ | I1 / O1 | Agree, and the O1 is better judged than SARSI's silence on it |

The Grok Bot row is the one worth dwelling on: SARSI placed it *lowest* of the four and the two-axis
paper places it *highest*. SARSI's row was an inference from product category with nothing behind it,
and it was wrong. The provenance table did its job — it marked the row as the one to distrust — but
marking a guess does not make it a finding, and the guess should probably not have been tabulated at
all.

---

## § 7 — Recommended joint form

Report a system as:

```
(I_i, O_j)              the two-axis coordinate — primary
+ separation            does proposer ≠ promoter ≠ referee hold?  (gates O_j)
+ reach                 (W_self, W_other)                          (SARSI-B)
+ ceiling               what it is permitted to do, not what it can
+ T_δ                   authorization latency, per depth
+ IC                    improvement competence, for any I3+ claim
```

The first line is the two-axis paper's. The rest are the coordinates it does not carry, and each
exists because some claim in it needs a referent: separation for §5.4, reach for the same, ceiling for
the gap between capability and permission, *T*<sub>δ</sub> for the rate, IC for §6.6.

---

## § 8 — Consequences for the other documents

- **`Capability_Is_Not_A_Level.md`** should cite the two-axis paper as the primary taxonomy it
  extends rather than presenting a parallel one, adopt the I1/I2 split, and correct its §6.2
  placements per §6 above.
- **`SARSI_Applied_Profiles.md`** §3's Grok and OpenClaw rows are superseded.
- **`SARSI_Level_Map.md`** should carry the I/O coordinate as the headline form, with its fourteen
  axes as the expansion.
- **`SARSI-B`** should record that its depth axis is coarse at D1 and that the two-axis I1/I2
  boundary is the finer and better construction.
