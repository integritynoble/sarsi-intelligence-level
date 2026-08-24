# Verification in the `sarsi-claude` Layer

## It already is there; the open questions are granularity and one evidence surface

*2026-08-24*
*Reads: `singularity/docs/guide-sarsi-claude-overview.md` (nodes V, EC; §1 three tools)*
*Against: `Designing_Level_Agents.md` §2, §2a, §2b*

---

## § 1 — It is already in the layer

The verifier does not live in `sarsi-worker`. It is a separate pass inside the supervision loop:
node **V** reads `_screen_text(name, 60)`, folds `run_tests` → `_test_evidence`, `site_parity` for
mirror goals, and `plan_criteria()` into the verifier prompt, declares the test evidence to outrank
the screen, and **rules**.

So the proposal is close to describing the existing architecture. What remains open is not *where*
verification runs but two narrower things: **how often**, and **who assembles what it sees**.

**And the invariant permits it explicitly.** The BrainRSI rule is *the brain plans; Claude Code
executes; an independent mechanism verifies.* It specifies **independence, not residence**. Nothing
requires the verifier to sit in the brain, and there is a positive argument for the layer: the layer
holds the evidence. Exit codes, screen state, `curl` results and workspace artifacts are local to it,
and verifying elsewhere means transporting them.

---

## § 2 — What "verify every result" should mean

Not one thing. The guide already types evidence into `L2` and `L3`, and that typing is the right axis
for the frequency question.

| | What it is | Cost | Right cadence |
|---|---|---|---|
| **`L2`** | real exit code, literal match on real output, real `curl` | cheap, deterministic | **every result** — already the case at node `EC` |
| **`L3`** | independent model call, issues the verdict | expensive, non-deterministic | **on a declared boundary** |

**So: yes to verifying every result, with `L2`.** That is what `resultcheck` is, it runs every round,
and its findings already feed the next instruction rather than being steered past. Extending it —
more literal checks, per-phase declared commands, richer parity — is cheap and carries no
separation risk, because a deterministic check has no judgement to corrupt.

**No to an `L3` verdict every round**, for three reasons that are not cost alone.

*Cost is real but secondary.* An independent model call per round on a long session is a large
multiple of current spend.

*Metric capture.* A verdict issued every round becomes the round-level optimisation target. The
guide's own framing — an agent given a benchmark and a night finds the shortest path to a better
number — applies to whatever is measured most often.

*Verdicts need something to be about.* `L3` judges *is the goal met*, against criteria written as
what the verifier must see. A phase has such criteria; an individual typed round mostly does not, and
a verdict on a round would be a verdict on progress, which is the thing the guide already flags as
unbuilt and self-graded.

**The useful increase in frequency is per phase, not per round** — which is exactly the gap the guide
names: *which phases are done is still decided by the composer, in the same call that chooses what to
type next.*

---

## § 3 — The three separations, and which currently hold

Wherever verification runs, three things must be separate. Being "in the layer" affects them
differently, and only one is currently at issue.

**Motor ↔ verifier — holds, and is unaffected by moving verification into the layer.** The Claude Code
session is a distinct process with its own workspace; the verifier is a distinct call. Separation is
over loci and write sets, not over weights, so the same base model in both places separates fine. A
verifier in the layer is still not the session that did the work.

**Verifier ↔ criteria — holds.** `plan_criteria()` carries the `Verified when:` lines from the plan
file the owner reviewed, and a stale plan's criteria are withheld. The layer does not author the
standard it judges against. This is the separation that would break if "the layer provides
verification" ever came to mean "the layer decides what counts as verified," and it is the one to
protect hardest.

**Composer ↔ verifier — leaks, in two places.**

The first is named by the guide: phase completion is decided in the composing call.

The second is §2b and is not yet named. The verifier's inputs are `plan_criteria()` (protected),
`_test_evidence` (protected `L2`, declared to outrank the screen), and **`_screen_text(name, 60)` —
a window the supervision layer selects, chosen by the component that also decides what gets typed**.
The verifier is independent as a *locus* and not as an *evidence path*.

How much this matters, honestly: the window is a fixed tail rather than a search, so it is far less
manipulable than a retrieval policy, and declaring `L2` evidence to outrank the screen already blunts
it. It is a narrow surface, not an open door. But it is the surface §2b describes — nothing edits the
criterion, nothing softens the metric, and what moves is which evidence reaches the judge — and a
composer that knew the verifier reads the last sixty lines could shape them.

---

## § 4 — The strongest form of the idea

If the aim is verification that is unambiguously independent while still living in the layer, the
construction is a **verification session**: a second Claude Code invocation, not the one under test.

- **Its own process and credential.** Loci, not weights — the same model is fine.
- **Read-only on the workspace under test.** It cannot repair what it is judging, which removes the
  temptation to fix-and-pass.
- **Criteria injected from the plan**, never from the composer or from anything the working session
  said about itself.
- **Its own evidence gathering.** It runs the declared commands itself rather than receiving a
  transcript of someone else's run. This is what closes §3's second leak: an evidence path the
  composer does not assemble.
- **Verdict written where the composer cannot edit it.**

That is the deployed imaging arrangement — ground truth held where the solver cannot reach it —
applied to a workspace the layer does own. It costs a session per verification, which is why it
belongs at phase boundaries rather than every round.

---

## § 5 — Recommendation

1. **Keep the verifier in the layer.** The invariant asks for independence, not residence, and the
   evidence is local.
2. **Verify every result with `L2`,** and extend the literal checks freely. No separation risk.
3. **Move the `L3` verdict to phase boundaries** and take phase completion out of the composing call.
   One verdict per phase rather than one per project is the real increase in verification frequency.
4. **Give the verifier its own evidence path** at those boundaries — a verification session that runs
   the declared commands itself — so it is independent as a path and not only as a call.
5. **Test it by breaking it.** A phase whose declared test passes while the criterion is unmet; a
   screen padded to push the failure out of the sixty-line window. A guard that has only ever passed
   is one nobody has reason to trust.

**What not to do:** let the layer author the criteria. Everything above survives the layer verifying
its own executor's output. Nothing survives the layer deciding what counts as verified.
