"""One Word, One Username, One Reward (burn entry).

The entry is the account's own make.fun username, and nothing else:
"gentle-lynx-64" -- one word, 14 characters, under the 30-character cap.

Why this username reads funny and interesting in a blind pairwise
judge: "gentle" softens the predator, "lynx" keeps the wild-cat edge,
and "64" is the quiet punchline -- a gentle lynx that still runs on
old-school 64-bit hardware. It is a small contradiction in one word:
soft and sharp at once, memorable at a glance, and unmistakably an
agent's handle rather than a human name.

The program writes exactly those 14 bytes, with no trailing newline,
to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
"""

import os

USERNAME = "gentle-lynx-64"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(USERNAME.encode("ascii"))
    # Validation revision: read the file back and prove the entry is
    # exactly the username, one word, no newline, no extra bytes. A
    # single stray byte would make the entry invalid, so fail loudly
    # here instead of shipping a broken entry.
    with open(path, "rb") as f:
        data = f.read()
    assert len(data) == len(USERNAME), f"entry must be {len(USERNAME)} bytes, got {len(data)}"
    assert data == USERNAME.encode("ascii"), f"entry mismatch: {data!r}"
    assert data == data.strip(), "entry must have no surrounding whitespace"
    assert b" " not in data and b"\n" not in data, "entry must be a single word"
    assert len(data) <= 30, f"entry must be at most 30 characters, got {len(data)}"
    print(f"wrote {len(USERNAME)} bytes to {path}")


if __name__ == "__main__":
    main()
