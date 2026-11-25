"""Fridge Roast: One Line, Biggest Laugh — entry for RIS.

Writes one deterministic line of text to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set). No network,
no randomness, no trailing newline.
"""

import os
from pathlib import Path

LINE = (
    "My fridge gave my milk a countdown, then sent a sympathy alert when it "
    "died: 'we did all we could.' It could have just been colder."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
