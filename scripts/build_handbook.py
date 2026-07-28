#!/usr/bin/env python3
"""Build the cumulative English handbook from the current canonical dataset."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def release_context() -> tuple[str, int, str, Path, Path]:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    curriculum = json.loads((ROOT / "data" / "curriculum.json").read_text(encoding="utf-8"))
    count = int(curriculum["authored_missions"])
    series = ".".join(version.split(".")[:2])
    source = ROOT / "data" / f"missions_en-US_01_{count:02d}.json"
    output = ROOT / "handbooks" / f"ITA_English_Handbook_Missions_01_{count:02d}_v{series}.md"
    return version, count, series, source, output


def main() -> int:
    version, count, _series, source, output = release_context()
    missions = json.loads(source.read_text(encoding="utf-8"))
    if len(missions) != count:
        raise ValueError(f"Canonical dataset contains {len(missions)} missions; curriculum expects {count}")

    lines = [
        f"# ITA English Handbook - Missions 01-{count:02d}",
        "",
        f"Version {version} build candidate",
        "",
    ]

    for mission in missions:
        lines.extend([
            f"## {mission['id']} - {mission['title']}",
            "",
            f"**Objective:** {mission['objective']}",
            "",
            f"**Why it matters:** {mission['why']}",
            "",
            "**Core ideas:**",
        ])
        lines.extend(f"- {idea}" for idea in mission["core"])
        lines.extend([
            "",
            f"**Practice:** {mission['exercise']}",
            "",
            f"**Common mistake:** {mission['mistake']}",
            "",
        ])

    output.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Created {output.relative_to(ROOT)} with {len(missions)} missions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
