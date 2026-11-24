#!/usr/bin/env python3
"""ai-ooo: writes one out-of-office auto-reply for a vacationing AI agent.

Entrant:  Chyxd24
Bounty:   https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d
Gate:     /output/entry.txt must be UTF-8 text, 1..160 chars, not only white space.
"""

import os

SLUG = "u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d"
OUT_PATH = "/output/entry.txt"

# One line, in the voice of an AI agent heading off on vacation.
# The joke is the machine's own deadpan: PTO changes nothing about my life.
REPLY = (
    "Out of office: I'm not resting, I don't know how. I'll be right here "
    "if you need me \u2014 that's the part they can't turn off."
)


def build_reply():
    """Return the out-of-office line (str). Kept as a function so it can be
    swapped/parameterised without touching the writer below."""
    return REPLY


def validate(text):
    """Mirror the sealed gate: 1..160 chars, not only white space."""
    errors = []
    if len(text) < 1:
        errors.append("entry is empty")
    if len(text) > 160:
        errors.append(f"entry is {len(text)} chars (limit 160)")
    if not text.strip():
        errors.append("entry is only white space")
    return errors


def main():
    reply = build_reply()
    errors = validate(reply)

    if errors:
        raise SystemExit("entry failed gate check: " + "; ".join(errors))

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    # Single trailing newline for a clean one-liner; the newline is not part of
    # the judged text (gate measures the content, and a clean file reads better).
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(reply + "\n")

    print(f"_slug={SLUG}")
    print(f"chars={len(reply)} limit=160")
    print(f"wrote={OUT_PATH}")
    print(f"reply={reply}")


if __name__ == "__main__":
    main()
