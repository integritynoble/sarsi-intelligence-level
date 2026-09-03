"""UAB v0.1 bound task families that live in this package (standard library only).

Each family module exposes the same five functions:

    generate(seed)            -> (files: dict[str, str], key: dict)   the workspace and the hidden key
    verify(ws, key)           -> dict(pass, accuracy, checks, failure_mode)
    reference_solve(ws)       -> None   edits the workspace the way a careful executor would; never sees the key
    naive_solve(ws)           -> None   the plausible wrong method the family is built to catch
    spec_key_check(seed)      -> None   raises AssertionError if the visible specification and the key disagree

The key is written outside the workspace. A verifier that reads the workspace and the key is the
acceptance locus; it is never the solver.
"""
from . import code_t0, funding_t0, job_t0

FAMILIES = {
    "code_t0": code_t0,
    "funding_t0": funding_t0,
    "job_t0": job_t0,
}
