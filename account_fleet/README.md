# One Account, Many Machines

**Designing the Multi-Host SARSI Console: Per-Host Agents, Host-Indexed Evidence, Channels That Can Drop, and What a Machine Takes With It When It Leaves**

PDF: [`../SARSI_One_Account_Many_Machines.pdf`](../SARSI_One_Account_Many_Machines.pdf) (21 pp).

The successor to [*One Chat Box, Five Agents*](../console_design/README.md). That design specifies a manager-fronted console with five agents, four channels, and per-agent evidence-linked self-models. It contains an assumption it never states: **that the fleet lives on one host.** Every channel is a function call, every report arrives, every measurement is comparable with every other, and the machine agent is a singular noun.

That assumption has failed in deployment. An account now owns several machines; a machine joins an account and can leave it; the host serving the registry is not a member of the fleet it serves; and the account's machine agent has already migrated between hosts while its sessions were copied across by hand.

## Three things that stop being free

| Property | Free on one host | Load-bearing on many |
|---|---|---|
| Comparability of evidence | one machine, so coordinates are commensurable | a reading is indexed by the host that took it, and aggregation has a wrong default |
| Delivery | a channel is a function call; sending is receiving | a channel may drop, and absence is ambiguous between *nothing happened* and *nothing arrived* |
| Membership | the fleet is whatever is running | a revocable relation, so identity, authority and history all need a scope |

## Four results

**1. An account-level self-state is a vector over machines, not a scalar.** No scalar aggregate of a host-indexed integrity coordinate is monotone in fleet health. Two machines — one idle at `1.0`, one carrying every task at `0.05` — average to a reassuring `0.525`; linking a *third idle machine* raises it to `0.68` while nothing about the working machine changes. Any account can improve its reported health by adding hosts that do nothing. This is the corpus's own "vector, not level" argument recurring one level up — and the companion, having forbidden the aggregate *within* an agent, reaches for exactly it when describing a fleet.

**2. Containment is not a leak test across a network.** The companion's check — project twice, assert containment — is a *safety* property, and safety properties are satisfied by doing nothing: `∅ ⊆ X`. A fleet with every link down reports perfect structural integrity, with the strongest possible margin, precisely when the console knows nothing. Hence a liveness companion, and the general principle: **silence must be attributable** to *not sent* or *not delivered*.

**3. Capability does not migrate; history may.** A capability posterior is evidence gathered under a *tool environment*. Crediting it to another host asserts a claim about outcomes under conditions never observed there — unsupported in exactly the direction that matters, since the outcomes were successes. Episodic and procedural memory cross with provenance (procedural marked *unverified on this host*); protected and audit memory cross unchanged; the posterior and **path-scoped grants** do not, because the same path string on another host is a different resource.

**4. Exactly one agent legitimately spans hosts.** Re-partitioning the roster by *scope* rather than *role* gives two account-scoped agents (manager; learning — because its object is a **person**, and a per-machine instantiation would make one owner into two partial, asymmetric learners), *n* host-scoped, many task-scoped, and one that spans: the working-process agent. It is therefore the only place cross-machine coordination is designed rather than forbidden, and §8 constructs it as **queue-mediated with manager-governed admission** so that it does not reinstate a peer edge — what crosses is a job, not an assertion.

## The observation that gets stronger

The companion argues from parsimony that the manager's dominant coordinate is **organizational awareness, not capability**. Multi-host converts that into a consequence: a manager separated from every host by a network *cannot* hold any host's capability or resource state, so it must route on ownership and authority, or ask. Organizational dominance is no longer a design preference.

## Refused, deliberately

- **A load-weighted fleet mean.** Better than the plain mean and still wrong: it leaves an aggregate whose value moves with a quantity the console itself controls. A health indicator that improves when the scheduler moves work is measuring the scheduler.
- **A machine-level governor switch.** Per-task governor state is read from the artefact that enforces it. A machine-level switch would live somewhere else and could eventually claim a governed fleet containing an ungoverned task. A machine-level *view* is required; a *switch* is not offered.
- **Backlog replay on reconnect.** A rejoining machine reports current state and the fact of the gap. A queue of stale states delivered at once is indistinguishable, at a bounded workspace, from rapid change.

## Build order

Heartbeat separate from reporting → acknowledged controls → account state as a vector → freshness on structural checks → migration as a procedure → queue-mediated cross-host work. The last is the most valuable and is deliberately last: built before its admission is governed, cross-host dispatch *is* the peer edge the architecture forbids, and it would be hard to remove afterwards.

## Status

Appendix B is honest per element. Built: account machine list, account-from-credential, registry served from outside the fleet, per-host machine agents, host-scoped coordinates, the single opt-out predicate, per-user structural isolation. **Not built:** account state as a vector, heartbeat, acknowledged controls, freshness, migration procedure. Partly: cross-host dispatch runs real jobs without manager-governed admission — the largest gap in the paper.

## Building

```
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

Verified: 0 errors, 0 undefined references, 21 pp.
