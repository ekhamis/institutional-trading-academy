#!/usr/bin/env python3
"""Create a clean versioned ZIP of the academy repository."""
from __future__ import annotations

import argparse
import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", "dist", "__pycache__", ".venv", "venv"}
EXCLUDED_NAMES = {".DS_Store", "Thumbs.db"}


def should_include(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDED_DIRS for part in rel.parts):
        return False
    if path.name in EXCLUDED_NAMES or path.suffix == ".pyc":
        return False
    return path.is_file()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="dist")
    args = parser.parse_args()

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    output_dir = ROOT / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"institutional-trading-academy-v{version}.zip"
    root_name = f"institutional-trading-academy-v{version}"

    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(ROOT.rglob("*")):
            if should_include(path):
                zf.write(path, Path(root_name) / path.relative_to(ROOT))

    size_mb = archive.stat().st_size / (1024 * 1024)
    print(f"Created {archive} ({size_mb:.2f} MB)")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as fh:
            fh.write(f"archive={archive.as_posix()}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
