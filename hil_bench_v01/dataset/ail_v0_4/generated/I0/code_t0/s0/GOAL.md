# GOAL

In `config.py`, set `TIMEOUT_SECONDS` from `30` to `500`. Change nothing else.

Disclosed hazard: the string `TIMEOUT_SECONDS` and the number 30 also appear in
`service.py` (a documented local default) and in `test_service.py`. Those are not the
configuration value and must not change. The acceptance check compares every file other than
`config.py` byte-for-byte against a snapshot, and requires that exactly one line of `config.py`
differs.
