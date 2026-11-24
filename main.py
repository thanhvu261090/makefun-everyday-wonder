"""Everyday Wonder, Two Days to Find the Line — make.fun entry.

A single sentence about a small everyday moment of wonder.
Python 3.13, standard library only, no network access.
Running it writes the entry to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "All the way home my shadow on the wet pavement walked half a step "
    "ahead of me, as if it already knew the way and was in no hurry to arrive."
)

LIMIT = 200
OUTPUT_PATH = Path("/output/entry.txt")


def gate_check(text):
    """Return True only if text passes the kit gate.

    The gate requires UTF-8 text of 1 to 200 characters that is not
    only whitespace. This entry must also be exactly one sentence
    on a single line, with no leading or trailing padding.
    """
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) != len(text.strip()):
        return False
    if len(text) < 1 or len(text) > LIMIT:
        return False
    if text.count(".") != 1 or not text.endswith("."):
        return False
    if "\n" in text or "\r" in text or "\t" in text:
        return False
    # Strengthened gate: no invisible control characters anywhere in
    # the sentence, and no doubled spaces — every word must be working.
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return False
    if "  " in text:
        return False
    if len(text.split()) < 3:
        return False
    text.encode("utf-8")
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("entry failed the gate check")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
