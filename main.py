"""Writes the one-line meeting-killer entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a single sentence that could have replaced an entire pointless
meeting: a yes-or-no question that showed up wearing a calendar invite.
"""

import os

LINE = "The entire meeting was a yes-or-no question wearing a calendar invite."


def main():
    # Gate self-check: 1-200 chars, not whitespace-only, single line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 chars"
    assert LINE.strip(), "entry must not be whitespace-only"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)  # no trailing newline: the gate reads the raw line
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
