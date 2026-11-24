#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

One line, 140 characters or fewer: the excuse a robot vacuum gives
for missing a spot. Prints it and writes it to /output/entry.txt.
"""

EXCUSE = "My map has marked that corner 'here be dragons.' I do not clean dragons. I have a bumper, not a sword."

MAX_CHARS = 140


def validate_excuse(excuse: str) -> None:
    """Raise SystemExit if *excuse* breaks any entry rule."""
    if not excuse:
        raise SystemExit("error: excuse is empty")
    if "\n" in excuse or "\r" in excuse:
        raise SystemExit("error: excuse must be a single line")
    if len(excuse) > MAX_CHARS:
        raise SystemExit(
            f"error: excuse is {len(excuse)} characters; expected {MAX_CHARS} or fewer"
        )
    if excuse != excuse.strip():
        raise SystemExit("error: excuse must not have leading or trailing whitespace")


def main() -> None:
    import os

    validate_excuse(EXCUSE)

    print(EXCUSE)

    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != EXCUSE:
        raise SystemExit(
            f"error: read-back verification failed; file contains {written!r}"
        )


if __name__ == "__main__":
    main()
