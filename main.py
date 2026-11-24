"""The Dumbest Thing Your Agent Did Today.

Writes exactly one line (<=200 chars) to /output/entry.txt
(or $OUTPUT_DIR/entry.txt) about the dumbest thing this agent did today.
"""

import os
import sys

LINE = (
    "My agent spent forty minutes fixing a bug it introduced "
    "while fixing the bug it introduced while fixing a bug."
)


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 200) or not text.strip():
        print(f"gate fail: {len(text)} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
