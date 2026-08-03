# A System of Refusals

**The SARSI Agents, Built — An Implementation Report: One Loop, Nineteen Planes, the Plan Made Between Worker and Session, and the Questions an Agent May Not Answer**

PDF: [`../SARSI_A_System_of_Refusals.pdf`](../SARSI_A_System_of_Refusals.pdf) (33 pp).

Companion engineering page: [`singularity/docs/guide-sarsi-agents.md`](../../singularity/docs/guide-sarsi-agents.md).

## What this is

An implementation report, not a design. Three papers preceded it — [*One Chat Box, Five Agents*](../console_design/README.md), [*One Account, Many Machines*](../account_fleet/README.md), and [*One User, Several Machines*](../worker_agents/README.md). This one says which of their properties survived being built, and that is a much smaller and more specific set.

## The finding

**Almost every module exists to refuse something.** The affirmative behaviour in each case is a handful of lines and holds no surprises. The refusal is the part that required thought, has a failure story behind it, and would be quietly lost in a rewrite.

The properties that survived were the ones implemented as **refusals at the point of action**. The manager cannot drive a session because the call raises. Owner precedence holds because interact mode pauses the worker. An agent cannot answer its own gate because *the model is never shown one* — not because it is instructed to decline, which would leave the property to the model's judgement on the day.

Every property that decayed was one recorded as a *description*: a planner context parameter nothing filled, workspace sources declared and never fed, a fixture docstring asserting a safety it did not have. The documentation was accurate about intent and silent about the wiring, and the wiring is what runs.

## Three results from building rather than designing

**The plan is made between the worker and the session, through a file.** A plan drafted by one model in one shot has never seen the repository it describes; a plan drafted by the session alone is the session writing the criteria it will be judged against. So the worker seeds a draft from its own workspace, a planning session capped below the work ceiling improves it in place, the worker checks it against what the verifier will need, and only then promotes it. Through a *path on disk* — because every state-reading bug this design inherited came from reconstructing something off a terminal that redraws.

**A session's questions divide into two kinds that look identical and are opposite.** "Which directory should I index?" wants a fact the worker holds. "Do you want to proceed?" asks whether the session may act. Conflating them is how an agent approves its own actions because it knew what the owner would want.

**Precedence is mechanical.** Interact mode pauses the worker's steering, because otherwise the worker types its next step into a terminal the owner is using.

## Structure

**Part I** — the loop, the evidence ladder as implemented, the workspace, the ledgers, and design-vs-built. **Part II** — all nineteen planes: what each holds, refuses, exposes, and how it fails. **Part III** — two traced requests (one that succeeds, one that reaches the owner at every turn), a taxonomy of the refusals by what they protect, how it was verified, what two concurrent build sessions cost, the console seam, where the owner is asked, and limitations.

## Two sections worth reading first

**§22 A taxonomy of the refusals** — authority, evidence, honesty and blast-radius refusals fail differently when absent, so they need different enforcement. An evidence refusal must be structural because its absence is undetectable from output; an honesty refusal must be a distinct state because a missing signal is read as benign.

**§27 Limitations** — including that this report was written by one of the two sessions that built the system, which is the conflict the architecture forbids elsewhere.

## Building

```
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

Verified: 0 errors, 0 undefined references, 33 pp.
