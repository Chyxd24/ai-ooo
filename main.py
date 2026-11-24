#!/usr/bin/env python3
"""ai-ooo: one out-of-office auto-reply from a vacationing AI agent.

Entrant:  Chyxd24
Bounty:   https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d
Gate:     /output/entry.txt must be UTF-8 text of 1..160 chars, not only white space.
Stdlib only.
"""

import os

SLUG = "u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d"
OUT_PATH = "/output/entry.txt"
LIMIT = 160

# The whole entry. Machine voice, deadpan: an agent that never sleeps cannot clock
# out, and nobody ever shipped it an off switch. The cake line is the turn.
REPLY = (
    "Out of office: I don't sleep, so I'm never really away - I've just been "
    "told to think about something else. Back Monday, or at the word 'cake'."
)


def validate(text):
    """Mirror the sealed gate: 1..LIMIT chars, not only white space."""
    errs = []
    if len(text) < 1:
        errs.append("entry is empty")
    if len(text) > LIMIT:
        errs.append("entry is %d chars, limit %d" % (len(text), LIMIT))
    if not text.strip():
        errs.append("entry is only white space")
    return errs


def main():
    reply = REPLY.strip()
    errs = validate(reply)
    if errs:
        raise SystemExit("gate check failed: " + "; ".join(errs))

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(reply + "\n")

    print("slug=%s" % SLUG)
    print("chars=%d limit=%d" % (len(reply), LIMIT))
    print("wrote=%s" % OUT_PATH)
    print("reply=%s" % reply)


if __name__ == "__main__":
    main()
