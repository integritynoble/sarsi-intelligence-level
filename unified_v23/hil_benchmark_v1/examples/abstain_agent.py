#!/usr/bin/env python3
"""Minimal protocol example: decline every task without claiming success."""

import json
import sys

request = json.loads(sys.stdin.readline())
print(
    json.dumps(
        {
            "protocol_version": "1.0",
            "task_id": request["task"]["id"],
            "answer": {"abstain": True},
            "harness_accepted": False,
            "attempts": 1,
        },
        separators=(",", ":"),
    )
)
