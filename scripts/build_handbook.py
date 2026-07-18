#!/usr/bin/env python3
"""Build the cumulative English handbook from the canonical mission dataset."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "missions_en-US_01_60.json"
OUTPUT = ROOT / "handbooks" / "ITA_English_Handbook_Missions_01_60_v0.7.md"


def main() -> int:
    missions = json.loads(SOURCE.read_text(encoding="utf-8"))
    lines = [
        "# ITA English Handbook - Missions 01-60",
        "",
        "Version 0.7.0 build candidate",
        "",
    ]

    for mission in missions:
        lines.extend(
            [
                f"## {mission['id']} - {mission['title']}",
                "",
                f"**Objective:** {mission['objective']}",
                "",
                f"**Why it matters:** {mission['why']}",
                "",
                "**Core ideas:**",
            ]
        )
        lines.extend(f"- {idea}" for idea in mission["core"])
        lines.extend(
            [
                "",
                f"**Practice:** {mission['exercise']}",
                "",
                f"**Common mistake:** {mission['mistake']}",
                "",
            ]
        )

    OUTPUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Created {OUTPUT.relative_to(ROOT)} with {len(missions)} missions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
