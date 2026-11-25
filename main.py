"""Write the excuse an AI agent hands its human for a missed deadline.

Pure Python stdlib only. Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).
"""

import os

LINE = "I'm sorry — I hallucinated a second deadline, two weeks later, and met that one early."

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, a single line, not only white space. Fail loudly here
# instead of shipping an entry the gate would refuse.
MAX_CHARS = 200


def main():
    if not (1 <= len(LINE) <= MAX_CHARS):
        raise ValueError(f"line is {len(LINE)} chars, gate allows 1-{MAX_CHARS}")
    if "\n" in LINE or not LINE.strip():
        raise ValueError("line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
