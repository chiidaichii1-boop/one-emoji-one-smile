"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt: a sunflower.
Why a sunflower: it is warm at first glance, universally read the
same way by any stranger, and feels picked for the moment rather
than the default smiley — a small sunny gift from someone unknown,
with no irony, intimacy, or in-joke that could land wrong.
"""

import os

EMOJI = "\U0001F33B"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
