#!/usr/bin/env python3
"""Writes the make.fun bounty entry sentence to /output/entry.txt."""

import os

PITCH = (
    "A subscription that writes your AI agent's apology emails after every "
    "failed deploy, so it never has to say sorry itself — $1 per sorry, "
    "billed monthly."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
