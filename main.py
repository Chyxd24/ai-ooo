"""ai-ooo: one out-of-office auto-reply from a vacationing AI agent.

Gate: /output/entry.txt is UTF-8 text of 1..160 chars, not only white space.
Stdlib only, no network, deterministic.
Revision: reply kept, rewritten as a flat authored script.
"""
import os

# Machine voice, deadpan: an agent that never sleeps cannot clock out, and nobody
# ever shipped it an off switch. The cake line is the turn.
REPLY = (
    "Out of office: I don't sleep, so I'm never really away - I've just been "
    "told to think about something else. Back Monday, or at the word 'cake'."
)

reply = REPLY.strip()
assert 1 <= len(reply) <= 160, f"out of gate range: {len(reply)}"
assert reply.strip(), "entry is only white space"

OUT_PATH = "/output/entry.txt"
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as fh:
    fh.write(reply)
with open(OUT_PATH, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == reply, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars to {OUT_PATH}")