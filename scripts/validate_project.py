#!/usr/bin/env python3
"""Validate the Institutional Trading Academy repository."""
from __future__ import annotations

import json
import re
import struct
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


def release_context() -> tuple[str, int, str, Path]:
    version_path = ROOT / "VERSION"
    if not version_path.exists():
        error("VERSION file is missing")
        return "0.0.0", 0, "0.0", ROOT / "data" / "missing.json"
    version = version_path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        error(f"VERSION must use semantic versioning, found: {version!r}")
    curriculum = load_json(ROOT / "data" / "curriculum.json")
    count = int(curriculum.get("authored_missions", 0)) if isinstance(curriculum, dict) else 0
    series = ".".join(version.split(".")[:2])
    canonical = ROOT / "data" / f"missions_en-US_01_{count:02d}.json"
    return version, count, series, canonical


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


def collect_missions(canonical: Path, expected_count: int) -> list[dict]:
    if not canonical.exists():
        error(f"Canonical mission dataset is missing: {canonical.relative_to(ROOT)}")
        return []
    data = load_json(canonical)
    if not isinstance(data, list):
        error(f"{canonical.relative_to(ROOT)} must be a JSON array")
        return []
    if len(data) != expected_count:
        error(f"Canonical mission count ({len(data)}) must match curriculum authored_missions ({expected_count})")
    return data


def validate_missions(missions: list[dict]) -> None:
    required = ("id", "title", "time", "visual", "competencies", "prerequisites", "objective", "why", "core", "scenario", "exercise", "quiz", "mistake", "evidence", "sources")
    ids: list[str] = []
    for index, mission in enumerate(missions, start=1):
        if not isinstance(mission, dict):
            error(f"Mission #{index} is not an object")
            continue
        mission_id = mission.get("id")
        if not mission_id or not re.fullmatch(r"L\d{2}-M\d{2}", str(mission_id)):
            error(f"Mission #{index} has invalid id: {mission_id!r}")
            continue
        ids.append(str(mission_id))
        for field in required:
            value = mission.get(field)
            empty_required_list = value == [] and field != "prerequisites"
            if value is None or value == "" or empty_required_list:
                error(f"{mission_id} missing required field: {field}")
        if not isinstance(mission.get("core"), list) or len(mission.get("core", [])) < 3:
            error(f"{mission_id} must contain at least three core ideas")
        quiz = mission.get("quiz")
        if not isinstance(quiz, list) or not quiz:
            error(f"{mission_id} must contain at least one quiz item")
        else:
            for qindex, item in enumerate(quiz, start=1):
                if not isinstance(item, list) or len(item) != 2 or not all(isinstance(v, str) and v.strip() for v in item):
                    error(f"{mission_id} quiz item #{qindex} must be a non-empty [question, answer] pair")
        visual = mission.get("visual")
        if visual:
            visual_path = ROOT / "assets" / "illustrations" / str(visual)
            if not visual_path.exists():
                error(f"{mission_id} references missing illustration: {visual}")
        if not isinstance(mission.get("competencies"), list):
            error(f"{mission_id} competencies must be an array")
        if not isinstance(mission.get("prerequisites"), list):
            error(f"{mission_id} prerequisites must be an array")
        if not isinstance(mission.get("sources"), list) or not mission.get("sources"):
            error(f"{mission_id} must reference at least one approved source")

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
        warning(f"English mission markdown count ({len(markdown_files)}) differs from canonical mission count ({len(missions)})")


def validate_sources(missions: list[dict]) -> None:
    source_data = load_json(ROOT / "data" / "sources.json")
    if not isinstance(source_data, dict):
        error("data/sources.json must be an object")
        return
    source_ids = set(map(str, source_data.keys()))
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
    mission_status = status.get("missions", [])
    if len(mission_status) != len(missions):
        error("translation_status mission records must match canonical mission count")
    elif [item.get("id") for item in mission_status] != [item.get("id") for item in missions]:
        error("translation_status mission order and IDs must match canonical missions")
    arabic = status.get("arabic", {})
    if isinstance(arabic, dict) and arabic.get("translated_missions", 0) not in (0, None):
        warning("Arabic missions exist before English master is locked")
    arabic_md = [p for p in (ROOT / "content" / "ar").rglob("*.md") if p.name.lower() != "readme.md"]
    if arabic_md:
        warning(f"Found {len(arabic_md)} Arabic mission files before English content lock")



def png_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        with path.open("rb") as handle:
            header = handle.read(24)
        if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
            return None
        return struct.unpack(">II", header[16:24])
    except OSError:
        return None


def validate_release_manifest(version: str) -> None:
    manifest = ROOT / "release" / f"v{version}" / "update_manifest.txt"
    if not manifest.exists():
        error(f"Missing release update manifest: {manifest.relative_to(ROOT)}")
        return
    entries = [line.strip() for line in manifest.read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]
    if not entries:
        error("Release update manifest is empty")
        return
    if len(entries) != len(set(entries)):
        error("Release update manifest contains duplicate paths")
    for item in entries:
        relative = Path(item)
        if relative.is_absolute() or ".." in relative.parts:
            error(f"Unsafe release-manifest path: {item}")
            continue
        if relative.parts and relative.parts[0] == "dist":
            error(f"Release manifest must not stage generated dist output: {item}")
        target = ROOT / relative
        if not target.is_file():
            error(f"Release-manifest file is missing: {item}")
            continue
        if relative.parts[:2] == ("assets", "illustrations") and target.suffix.lower() == ".png":
            dimensions = png_dimensions(target)
            if dimensions != (1600, 900):
                error(f"Release illustration must be 1600 x 900: {item} is {dimensions}")
    required = {
        f"release/v{version}/update_manifest.txt",
        f"scripts/push_v{'.'.join(version.split('.')[:2])}_candidate.ps1",
    }
    missing_required = sorted(required.difference(entries))
    for item in missing_required:
        error(f"Release update manifest is missing required handoff file: {item}")

def validate_schema_alignment() -> None:
    schema = load_json(ROOT / "schemas" / "mission.schema.json")
    if not isinstance(schema, dict):
        return
    required = set(schema.get("required", []))
    expected = {"id", "title", "time", "visual", "competencies", "prerequisites", "objective", "why", "core", "scenario", "exercise", "quiz", "mistake", "evidence", "sources"}
    if required != expected:
        error("mission.schema.json required fields do not match the canonical mission record")


def validate_release_consistency(missions: list[dict], version: str, count: int, series: str) -> None:
    curriculum = load_json(ROOT / "data" / "curriculum.json")
    if not isinstance(curriculum, dict):
        return
    if curriculum.get("version") != version:
        error("curriculum version must match VERSION")
    if curriculum.get("authored_missions") != len(missions):
        error("curriculum authored mission count must match canonical missions")

    validate_localization(missions, version)
    release_label = f"v{version}"
    status_matches = sorted((ROOT / "docs").glob(f"*_BUILD_STATUS_v{series}.md"))
    if len(status_matches) != 1:
        error(f"Expected exactly one build-status document for v{series}, found {len(status_matches)}")
        status_path = None
    else:
        status_path = status_matches[0]

    required_text: dict[Path, tuple[str, ...]] = {
        ROOT / "README.md": (f"**{version}**", f"**{count}**"),
        ROOT / "docs" / "04_KNOWLEDGE_GRAPH.md": (release_label, f"{count} canonical English missions"),
        ROOT / "docs" / "10_ROADMAP.md": (release_label,),
    }
    if status_path:
        required_text[status_path] = (release_label, f"{count} canonical English missions")
    for path, markers in required_text.items():
        if not path.exists():
            error(f"Missing release consistency document: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                error(f"{path.relative_to(ROOT)} missing release marker: {marker}")

    handbook = ROOT / "handbooks" / f"ITA_English_Handbook_Missions_01_{count:02d}_v{series}.md"
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
    version, count, series, canonical = release_context()
    missions = collect_missions(canonical, count)
    validate_missions(missions)
    validate_sources(missions)
    validate_schema_alignment()
    validate_release_manifest(version)
    validate_release_consistency(missions, version, count, series)

    print(f"Validated repository: {ROOT}")
    print(f"Canonical dataset: {canonical.relative_to(ROOT)}")
    print(f"Canonical English missions: {len(missions)}")
    print(f"Errors: {len(ERRORS)} | Warnings: {len(WARNINGS)}")
    for item in WARNINGS:
        print(f"WARNING: {item}")
    for item in ERRORS:
        print(f"ERROR: {item}")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    raise SystemExit(main())
