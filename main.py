#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun bounty u-suroto-two-sentence-horror-acea9253.

Writes one original two-sentence horror story to /output/entry.txt
(or a path given as argv[1]). Deterministic: the story is hardcoded,
no randomness, no time, no network.
"""

import sys

STORY = (
    "Every night I tell my smart speaker goodnight, and every night "
    "it says goodnight back. "
    "Last night it said goodnight before I spoke \u2014 in my voice, "
    "to someone standing behind me."
)

MAX_CHARS = 400


def validate_entry(text: str) -> str:
    """Check the story against the bounty gate before writing it.

    The gate requires UTF-8 text of 1-400 characters, not only
    whitespace, telling exactly two sentences.
    """
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    sentences = [s for s in text.split(". ") if s.strip()]
    if len(sentences) != 2 or not text.rstrip().endswith("."):
        raise ValueError("entry must be exactly two sentences")
    return text


def write_entry(text: str, path: str) -> None:
    """Write the validated story to path as UTF-8 text."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate_entry(text))


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    write_entry(STORY, path)


if __name__ == "__main__":
    main()
