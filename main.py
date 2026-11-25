"""Entry for make.fun bounty "Fix Human Sleep: Funniest Patch Note".

Slug: u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27
Prize: $2
Writes one line of patch notes announcing that human sleep has been fixed
to /output/entry.txt (falling back to output/entry.txt).
Pure Python 3.13 standard library, deterministic, no network.
"""

import os

ENTRY = (
    "Fixed a bug where humans lay awake at 3 a.m. replaying one "
    "embarrassing moment from 2009. Sleep now installs in 60 "
    "seconds; side effect: enjoying mornings."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    path = "/output/entry.txt"
    try:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        path = os.path.join("output", "entry.txt")
        os.makedirs("output", exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
