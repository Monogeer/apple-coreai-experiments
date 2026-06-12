#!/usr/bin/env python3
"""Inspect an exported Apple Core AI model folder.

The script prints a compact tree of a model bundle and highlights common files
such as .aimodel, tokenizer folders, and metadata.json.

Example:
    python scripts/inspect_model_folder.py ~/Documents/learning/coreai-exports/qwen3_model
"""

from __future__ import annotations

import argparse
from pathlib import Path


def format_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"
        value /= 1024
    return f"{value:.2f} GB"


def folder_size(path: Path) -> int:
    if path.is_file():
        return path.stat().st_size
    return sum(p.stat().st_size for p in path.rglob("*") if p.is_file())


def inspect(path: Path, max_depth: int) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Path not found: {path}")

    print(f"Path: {path}")
    print(f"Total size: {format_size(folder_size(path))}")
    print()

    base_depth = len(path.resolve().parts)
    for item in sorted(path.rglob("*")):
        depth = len(item.resolve().parts) - base_depth
        if depth > max_depth:
            continue
        indent = "  " * (depth - 1)
        suffix = "/" if item.is_dir() else f" ({format_size(item.stat().st_size)})"
        print(f"{indent}- {item.name}{suffix}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect an exported model folder.")
    parser.add_argument("path", type=Path, help="Model folder path")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum tree depth")
    args = parser.parse_args()

    inspect(args.path.expanduser(), args.max_depth)


if __name__ == "__main__":
    main()
