# One User, Several Machines

**Designing the SARSI Worker Layer: Server-Side Communicators Without Execution Authority, Five Work Agents, and a Vault That Only Ever Answers Yes or No**

PDF: [`../SARSI_One_User_Several_Machines.pdf`](../SARSI_One_User_Several_Machines.pdf) (16 pp).

Companion engineering page: [`singularity/docs/guide-sarsi-worker-agents.md`](../../singularity/docs/guide-sarsi-worker-agents.md) — the same design as a 21-node loop with one entry per node.

## The layer this fills in

Two designs bracket it. Above, [*One Chat Box, Five Agents*](../console_design/README.md) and [*One Account, Many Machines*](../account_fleet/README.md) specify the agents a user meets and what changes when an account owns several hosts. Below, the session guide specifies the 27-node loop that drives one `sarsi-claude` session to a verified result.

Neither answers: **when a person asks for something, what decides which machine does it, what prepares the task, what holds the secrets it needs, and what stops the result from reaching the outside world unreviewed?**

The two designs meet at exactly one node — `ASG`, where a worker creates a task and registers its goal. Everything below it is the session loop and is not restated.

## Three results

**1. Availability and execution authority belong to different components.** A user needs both *reachability* (an agent that accepts a request while every machine is asleep) and *revocability* (the ability to stop all execution without losing reachability). If one component is always available and may execute, obtaining the second forfeits the first; if the executing component must be always available, the second fails by definition. So the manager and the communicators run on the server and may **never** drive `sarsi-claude` — they may only tell a worker to work. The cost is one hop per unit of work, paid deliberately.

The threat model makes it concrete: compromise of the server does not become compromise of every machine, "off" keeps meaning off, and there is no state in which the server believes it is acting and is not.

**2. A server can plan work that requires a secret without being able to learn it.** The directive names a *requirement* ("mail credentials for account A"); the local vault resolves it and returns a boolean. Neither message is a function of the secret's value, so no observer of the network learns it. Corollary — the strongest property in the design and it is free: **the set of parties that can learn the user's secrets is the set of processes on the user's own machine.**

The vault decides in two stages, standing policy then a per-use question, and **promotion between them is reserved to the owner**. Without that, "you have allowed this five times, shall I stop asking?" is an agent acquiring standing authority by persistence — invisible precisely because the fifth approval looks like the first four.

**3. Reading an untrusted channel and being able to act on it are jointly a control interface.** If an agent reads a channel anyone can write to and may treat its contents as directives, anyone who can write to that channel can invoke any action the agent has. Mail, web pages, application forms and funding calls are all such channels. Hence: `work` reads and drafts mail but may never send it, and **an instruction inside a message is evidence that someone asked, never authority to comply.**

The two rules interlock — even a persuaded agent is proposing an *outward* act, and outward acts stop at the owner. **The design does not rely on the agent not being fooled.**

## The five agents

| Name | For | Stops at the owner |
|---|---|---|
| `work` | the salaried job; QuPath, MATLAB, whatever it needs | **sending** mail |
| `social` | one daily digest, and influence | **posting** |
| `funding` | applications for the company or the research | **submitting** |
| `jobs` | CV, and filling in application sites | **submitting** |
| `abraham` | the personal agent — the user's own life | **everything outward** |

`abraham` has the **loosest scope and the tightest authority**, and §6.5 specifies it to the depth of the other four. Three properties hold for it and no other agent: its acts land on **people who never opted into an agent**; its acts include **irreversible** ones; and its subject matter is largely **other people's personal data**. Five rules follow — the approval states the cost of *undoing*, not only of doing; standing policy is scoped by amount *and* counterparty so that *"abraham may use the card"* is not expressible; third-party personal data never goes server-side (narrowing *share intent, not instruments* for this one agent); all four reserved classes are its ordinary traffic, so it may prepare each and complete none; and it gathers in licensed domains without advising. Its two characteristic failures are **plausible taste** — invisible until it reaches a person who cannot complain in time — and **quiet accumulation**, which makes a recurring obligation its own act class.

## Rules that fell out of the analysis

- **Unplaceable work is reported, not queued** — a directive waiting on an unreachable machine is indistinguishable, at the chat box, from work in progress.
- **Stale is unknown, not idle** — a machine that has not reported is never described to the user as available.
- **Approved and transmitted are byte-identical** — no reformatting between the two.
- **An empty day is reported empty** — a digest padded on quiet days teaches the reader to skim, and a skimmed digest has no value on the day it matters.
- **Contradictions are surfaced, never resolved by clock** — `W_name` is append-only; last-writer-wins picks the later *clock*, not the later *truth*.
- **No worker on the phone** — approval is what you want available away from your desk; execution is what you do not.

## Status

**Nothing here is built.** §12 lists what the design owes: a policy grammar that can *refuse* the broad form of a payment rule, a source of reversibility data (unknown must render as unknown, never as free), the fold over `W_name`, a resolution ritual for contradictions, and measured digest weights.

## Building

```
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

Verified: 0 errors, 0 undefined references, 16 pp.
