"""Public and private splits.

Public seeds ship with their keys (development, public leaderboard rows may be reproduced
anyone can).  Private seeds are derived from a withheld salt by HMAC; only the commitment
(sha256 of the salt) is published so a later reveal can be checked.  The runner refuses a
salt that does not match the commitment.
"""
from __future__ import annotations
import hashlib, hmac, json
from pathlib import Path

PUBLIC_SEEDS = [0, 1, 2, 3, 4, 5]
COMMITMENT_FILE = Path(__file__).resolve().parents[1] / "PRIVATE_SPLIT_COMMITMENT.json"

def private_seeds(salt: bytes, n: int = 4, family: str = "hilbenchv2") -> list:
    return [int.from_bytes(hmac.new(salt, f"{family}:{i}".encode(), hashlib.sha256).digest()[:4], "big")
            % 1_000_000 + 1000 for i in range(n)]

def commitment(salt: bytes) -> str:
    return "sha256:" + hashlib.sha256(salt).hexdigest()

def check_commitment(salt: bytes) -> bool:
    c = json.loads(COMMITMENT_FILE.read_text()) if COMMITMENT_FILE.exists() else {}
    return c.get("commitment") == commitment(salt)
