#!/usr/bin/env python3
"""Validate the Institutional Trading Academy repository."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVALID_WINDOWS = set('<>:"\\|?*')
ERRORS: list[str] = []
WARNINGS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def warning(message: str) -> None:
    WARNINGS.append(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        error(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")
        return None


def validate_filenames() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if any(ch in path.name for ch in INVALID_WINDOWS):
            error(f"Windows-incompatible filename: {path.relative_to(ROOT)}")


def validate_json_files() -> None:
    for path in ROOT.rglob("*.json"):
        if ".git" not in path.parts:
            load_json(path)


def collect_missions() -> list[dict]:
    canonical = ROOT / "data" / "missions_en-US_01_60.json"
    data = load_json(canonical)
    if not isinstance(data, list):
        error("data/missions_en-US_01_60.json must be a JSON array")
        return []
    return data


def validate_missions(missions: list[dict]) -> None:
    ids: list[str] = []
    for index, mission in enumerate(missions, start=1):
        if not isinstance(mission, dict):
            error(f"Mission #{index} is not an object")
            continue
        mission_id = mission.get("id")
        if not mission_id or not re.fullmatch(r"L\d{2}-M\d{2}", str(mission_id)):
            error(f"Mission #{index} has invalid id: {mission_id!r}")
            continue
        ids.append(mission_id)
        for field in ("title", "objective", "exercise", "evidence"):
            if not mission.get(field):
                error(f"{mission_id} missing required field: {field}")
        visual = mission.get("visual")
        if visual:
            visual_path = ROOT / "assets" / "illustrations" / str(visual)
            if not visual_path.exists():
                error(f"{mission_id} references missing illustration: {visual}")
        if not isinstance(mission.get("quiz"), list) or not mission.get("quiz"):
            error(f"{mission_id} must contain at least one quiz item")

    duplicate_ids = sorted({item for item in ids if ids.count(item) > 1})
    for mission_id in duplicate_ids:
        error(f"Duplicate mission id: {mission_id}")

    known = set(ids)
    for mission in missions:
        mission_id = mission.get("id")
        for prereq in mission.get("prerequisites", []):
            if prereq not in known:
                error(f"{mission_id} references unknown prerequisite: {prereq}")

    markdown_files = list((ROOT / "content" / "en-US").rglob("*.md"))
    if len(markdown_files) != len(missions):
        warning(
            f"English mission markdown count ({len(markdown_files)}) differs from canonical mission count ({len(missions)})"
        )


def validate_sources(missions: list[dict]) -> None:
    source_data = load_json(ROOT / "data" / "sources.json")
    if source_data is None:
        return
    if isinstance(source_data, dict):
        if "sources" in source_data and isinstance(source_data["sources"], list):
            source_ids = {str(item.get("id")) for item in source_data["sources"] if isinstance(item, dict)}
        else:
            source_ids = set(map(str, source_data.keys()))
    elif isinstance(source_data, list):
        source_ids = {str(item.get("id")) for item in source_data if isinstance(item, dict)}
    else:
        error("data/sources.json must be an object or array")
        return

    for mission in missions:
        for source_id in mission.get("sources", []):
            if str(source_id) not in source_ids:
                error(f"{mission.get('id')} references unknown source: {source_id}")


def validate_localization(missions: list[dict], version: str) -> None:
    status = load_json(ROOT / "data" / "translation_status.json")
    if not isinstance(status, dict):
        return
    if status.get("source_locale") != "en-US":
        error("translation_status source_locale must remain en-US until English master lock")
    if status.get("project_version") != version:
        error("translation_status project_version must match VERSION")
    english_master = status.get("english_master", {})
    if not isinstance(english_master, dict) or english_master.get("authored_missions") != len(missions):
        error("translation_status authored mission count must match canonical missions")
    if len(status.get("missions", [])) != len(missions):
        error("translation_status mission records must match canonical mission count")
    arabic = status.get("arabic", {})
    if isinstance(arabic, dict) and arabic.get("translated_missions", 0) not in (0, None):
        warning("Arabic missions exist before English master is locked")
    arabic_md = [p for p in (ROOT / "content" / "ar").rglob("*.md") if p.name.lower() != "readme.md"]
    if arabic_md:
        warning(f"Found {len(arabic_md)} Arabic mission files before English content lock")


def validate_release_consistency(missions: list[dict]) -> None:
    version_file = ROOT / "VERSION"
    if not version_file.exists():
        error("VERSION file is missing")
        return
    version = version_file.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        error(f"VERSION must use semantic versioning, found: {version!r}")
        return

    curriculum = load_json(ROOT / "data" / "curriculum.json")
    if not isinstance(curriculum, dict):
        return
    if curriculum.get("version") != version:
        error("curriculum version must match VERSION")
    if curriculum.get("authored_missions") != len(missions):
        error("curriculum authored mission count must match canonical missions")

    validate_localization(missions, version)

    release_label = f"v{version}"
    release_series = ".".join(version.split(".")[:2])
    count = len(missions)
    required_text = {
        ROOT / "README.md": (f"**{version}**", f"**{count}**"),
        ROOT / "docs" / "04_KNOWLEDGE_GRAPH.md": (release_label, f"{count} canonical English missions"),
        ROOT / "docs" / f"22_BUILD_STATUS_v{release_series}.md": (release_label, f"{count} canonical English missions"),
    }
    for path, markers in required_text.items():
        if not path.exists():
            error(f"Missing release consistency document: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                error(f"{path.relative_to(ROOT)} missing release marker: {marker}")

    handbook = ROOT / "handbooks" / f"ITA_English_Handbook_Missions_01_{count}_v{release_series}.md"
    if not handbook.exists():
        error(f"Missing cumulative handbook: {handbook.relative_to(ROOT)}")
    else:
        handbook_text = handbook.read_text(encoding="utf-8")
        if f"Version {version} build candidate" not in handbook_text:
            error("Cumulative handbook version must match VERSION")
        heading_count = len(re.findall(r"^## L\d{2}-M\d{2} - ", handbook_text, re.MULTILINE))
        if heading_count != count:
            error(f"Cumulative handbook mission count ({heading_count}) must match canonical missions ({count})")


def main() -> int:
    validate_filenames()
    validate_json_files()
    missions = collect_missions()
    validate_missions(missions)
    validate_sources(missions)
    validate_release_consistency(missions)

    print(f"Validated repository: {ROOT}")
    print(f"Canonical English missions: {len(missions)}")
    print(f"Errors: {len(ERRORS)} | Warnings: {len(WARNINGS)}")
    for item in WARNINGS:
        print(f"WARNING: {item}")
    for item in ERRORS:
        print(f"ERROR: {item}", file=sys.stderr)
    return 1 if ERRORS else 0


if __name__ == "__main__":
    raise SystemExit(main())
