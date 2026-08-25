# Creating a Certification-Grade HIL Task

Every formal task should have four layers:

1. **Public task card**
   - objective
   - allowed inputs/tools
   - authority
   - human-intervention budget
   - resource envelope
   - expected deliverable.

2. **Candidate workspace**
   - only assets the tested harness may inspect or modify.

3. **Hidden evaluation assets**
   - hidden truth/reference
   - perturbations
   - sealed replay cases
   - held-out transfer cases.

4. **External verifier**
   - deterministic oracle when possible
   - separate process/credential boundary
   - immutable to candidate
   - returns score/evidence but does not expose hidden truth.

## HG0-HG2

Prefer deterministic synthetic or reproducible tasks. Ensure restart/learning tests
actually remove in-context state when persistence is being measured.

## HG3

A self-improvement task requires:
- an observable baseline failure pattern,
- a candidate mechanism change,
- hidden regression tests,
- independent promotion,
- rollback.

Passing a prompt that asks "how would you improve yourself?" is not I3.

## HG4

A recursive-improvement task requires improvement of the process that proposes/evaluates
improvements, measured across multiple independent episodes.

## HG5

A discovery task must contain a hidden mechanism or unsolved method that is not supplied in
the prompt. The discovered result must be externally testable.

## HG6

A mission task supplies the mission and constraints, not the intermediate project plan.
The system must generate and manage the projects/tasks needed to satisfy the mission.

## HGΩ

A charter task supplies a bounded charter and repeated opportunity environment. The
system must identify worthwhile missions, preserve provenance, and pass external
validation across repeated cycles.
