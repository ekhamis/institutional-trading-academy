import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit the English master before v1.0.0 lock.")
    parser.add_argument("--write", action="store_true", help="Write the review report under release/v1.0.0-review.")
    args = parser.parse_args()

    curriculum = load_json(ROOT / "data" / "curriculum.json")
    count = int(curriculum["authored_missions"])
    canonical_path = ROOT / "data" / f"missions_en-US_01_{count:02d}.json"
    missions = load_json(canonical_path)
    sources = load_json(ROOT / "data" / "sources.json")
    translation = load_json(ROOT / "data" / "translation_status.json")

    errors: list[str] = []
    warnings: list[str] = []
    ids = [str(mission.get("id", "")) for mission in missions]
    positions = {mission_id: index for index, mission_id in enumerate(ids)}

    if len(missions) != count:
        errors.append(f"Canonical count is {len(missions)}; curriculum declares {count}.")
    duplicates = sorted(item for item, occurrences in Counter(ids).items() if occurrences > 1)
    if duplicates:
        errors.append(f"Duplicate mission IDs: {', '.join(duplicates)}")

    unknown_sources: set[str] = set()
    forward_prerequisites: list[str] = []
    source_usage: Counter[str] = Counter()
    for mission in missions:
        mission_id = str(mission.get("id", ""))
        for prerequisite in mission.get("prerequisites", []):
            if prerequisite not in positions:
                errors.append(f"{mission_id} has unknown prerequisite {prerequisite}.")
            elif positions[prerequisite] >= positions[mission_id]:
                forward_prerequisites.append(f"{mission_id}->{prerequisite}")
        for source_id in mission.get("sources", []):
            source_id = str(source_id)
            source_usage[source_id] += 1
            if source_id not in sources:
                unknown_sources.add(source_id)

    if forward_prerequisites:
        errors.append(f"Forward prerequisite edges: {', '.join(forward_prerequisites)}")
    if unknown_sources:
        errors.append(f"Unknown source IDs: {', '.join(sorted(unknown_sources))}")

    invalid_source_urls = sorted(
        source_id
        for source_id, source in sources.items()
        if not re.fullmatch(r"https://[^\s]+", str(source.get("url", "")))
    )
    if invalid_source_urls:
        errors.append(f"Non-HTTPS or malformed source URLs: {', '.join(invalid_source_urls)}")
    unused_sources = sorted(set(sources) - set(source_usage))
    if unused_sources:
        warnings.append(f"Unused registry sources: {', '.join(unused_sources)}")

    english_markdown = sorted((ROOT / "content" / "en-US").rglob("*.md"))
    if len(english_markdown) != count:
        errors.append(f"English mission Markdown count is {len(english_markdown)}; expected {count}.")
    content_ids = [path.stem[:7] for path in english_markdown]
    if sorted(content_ids) != sorted(ids):
        errors.append("English mission Markdown IDs do not match the canonical dataset.")

    arabic = translation.get("ar", {})
    translated_arabic = int(arabic.get("translated_missions", 0) or 0)
    if translated_arabic:
        errors.append(f"Arabic has {translated_arabic} translated missions before English lock.")

    source_freshness_evidence = (
        ROOT / "release" / "v1.0.0-review" / "source_freshness_spot_check.md"
    )
    package_privacy_evidence = (
        ROOT / "release" / "v1.0.0-review" / "package_privacy_review.md"
    )
    manual_gates_remaining = [
        "Editorial review of all 120 English missions",
        "Independent instructional and risk-language review",
    ]
    manual_gates_completed = []
    if source_freshness_evidence.exists():
        manual_gates_completed.append(
            "Source freshness spot-check before v1.0.0 lock"
        )
    else:
        manual_gates_remaining.insert(
            2, "Source freshness spot-check before v1.0.0 lock"
        )
    if package_privacy_evidence.exists():
        manual_gates_completed.append("Final package privacy review")
    else:
        manual_gates_remaining.append("Final package privacy review")

    report = {
        "audit": "English master pre-lock",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository_version": (ROOT / "VERSION").read_text(encoding="utf-8").strip(),
        "canonical_dataset": canonical_path.relative_to(ROOT).as_posix(),
        "canonical_english_missions": len(missions),
        "english_mission_markdown_files": len(english_markdown),
        "registered_sources": len(sources),
        "sources_used": len(source_usage),
        "official_sources": sum(1 for source in sources.values() if source.get("kind") == "official"),
        "arabic_translated_missions": translated_arabic,
        "errors": errors,
        "warnings": warnings,
        "automated_gate": "PASS" if not errors else "FAIL",
        "manual_gates_completed": manual_gates_completed,
        "manual_gates_remaining": manual_gates_remaining,
    }

    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        output = ROOT / "release" / "v1.0.0-review" / "english_master_audit.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
