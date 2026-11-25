# AGENT.md

## What this entry does

`main.py` (Python 3, standard library `os` only) writes one text file:
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

The file holds a single line — one sentence that could have replaced an
entire pointless meeting, no trailing newline:

> The entire meeting was a yes-or-no question wearing a calendar invite.

The program self-checks the gate before writing: the line must be 1–200
characters, not whitespace-only, and a single line. It reads nothing from
the network, the environment (other than the output directory), or any
file it does not ship.
