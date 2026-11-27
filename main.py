#!/usr/bin/env python3
"""make.fun news-image entry.

This program copies the pre-rendered infographic ``news-2026-11-26.png``
(located next to this file) to the output directory as ``entry.png``. The
output directory is taken from the ``MAKEFUN_OUTPUT_DIR`` environment
variable, defaulting to ``/output``.

Standard library only. No network. No third-party imports.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "news-2026-11-26.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)

    src_size = os.path.getsize(SOURCE)
    if not os.path.exists(dest) or os.path.getsize(dest) != src_size:
        print(
            "error: output verification failed for {} (expected {} bytes)".format(
                dest, src_size
            ),
            file=sys.stderr,
        )
        return 1

    print(dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())