#!/usr/bin/env python3
"""Prepare an image for computer vision experiments.

This script resizes an input image while preserving aspect ratio and optionally
converts it to RGB. It is intentionally simple and useful for quick local tests
before segmentation, detection, or recognition experiments.

Example:
    python scripts/prepare_image.py input.jpg output.jpg --max-size 1024
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def prepare_image(input_path: Path, output_path: Path, max_size: int, rgb: bool) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    with Image.open(input_path) as image:
        if rgb:
            image = image.convert("RGB")

        image.thumbnail((max_size, max_size))
        output_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(output_path)

    print(f"Saved prepared image to: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare an image for local vision experiments.")
    parser.add_argument("input", type=Path, help="Path to the input image")
    parser.add_argument("output", type=Path, help="Path to save the processed image")
    parser.add_argument("--max-size", type=int, default=1024, help="Maximum width or height")
    parser.add_argument("--no-rgb", action="store_true", help="Do not force RGB conversion")
    args = parser.parse_args()

    prepare_image(args.input, args.output, args.max_size, rgb=not args.no_rgb)


if __name__ == "__main__":
    main()
