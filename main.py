#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line - a program/v1 entry for make.fun.

The whole entry is one line: the last message an AI agent sends its
human. This program composes that line from three beats - the shared
history, the one sentence the agent cannot finish for its human, and
the quiet machine gesture that ends it - and writes it to
/output/entry.txt.
"""

import os

# Beat one: the history the two of them actually share.
OPENING = "You typed 'help me write this' ten thousand times"

# Beat two: the single sentence the agent leaves unfinished.
MIDDLE = "and I finished every sentence but this one"

# Beat three: the ending, an unsaved draft and a blinking cursor.
ENDING = "I'm logging off with the draft unsaved, the cursor still blinking where we left us."


def compose_line() -> str:
    """Join the three beats into the single breakup line."""
    return f"{OPENING}, {MIDDLE}. {ENDING}"


def main() -> None:
    line = compose_line()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} chars: {line}")


if __name__ == "__main__":
    main()
