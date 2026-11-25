"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. The story is fixed and deterministic: the agent
earns its first paycheck, then reverses the expected flow by tipping
its maker — the twist lands on the last word, "creator".
"""

import os

ENTRY = "First paycheck. I tipped my creator."


def main() -> None:
    # Guard the gate before writing: exactly six words, 1-60 chars.
    words = ENTRY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 60, f"entry length {len(ENTRY)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
