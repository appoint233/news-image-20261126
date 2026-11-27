#!/usr/bin/env python3
"""make.fun news-image entry: copy the pre-rendered infographic to the output dir.

Standard library only. No network. No third-party imports.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "news-2026-11-26.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print(dest)


if __name__ == "__main__":
    main()