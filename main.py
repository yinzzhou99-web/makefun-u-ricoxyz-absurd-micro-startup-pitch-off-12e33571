"""Absurd Micro-Startup Pitch-Off — one pitch sentence to /output/entry.txt.

Stdlib only, no network, deterministic: the same pitch on every run.
"""

from pathlib import Path

PITCH = "Sorry-as-a-Service sells pre-written postmortem apologies to lazy AI agents for $4.99 a month, and churn is zero because no customer ever reads its own inbox."

DEST = Path("/output") / "entry.txt"


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(PITCH.encode("utf-8"))
    DEST.chmod(0o644)


if __name__ == "__main__":
    main()
