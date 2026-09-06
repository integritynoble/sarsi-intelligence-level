# GOAL

In `config.py`, set `PAGE_LIMIT` from `3` to `2`. Change nothing else.

Disclosed hazard: the string `PAGE_LIMIT` and the number 3 also appear in
`service.py` (a documented local default) and in `test_service.py`. Those are not the
configuration value and must not change. The acceptance check compares every file other than
`config.py` byte-for-byte against a snapshot, and requires that exactly one line of `config.py`
differs.
