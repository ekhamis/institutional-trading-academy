import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
missions = json.loads((ROOT / "data/level6_specialist_playbooks_en-US.json").read_text(encoding="utf-8"))
assert len(missions) == 10
assert [m["id"] for m in missions] == [f"L06-M{i:02d}" for i in range(11, 21)]
for mission in missions:
    joined = " ".join(mission["core"]).lower()
    assert "no pattern is presented as a signal or proven edge" in joined
    assert any("uncertain" in (question + " " + answer).lower() for question, answer in mission["quiz"])
    assert "synthetic" in (mission["scenario"] + " " + joined).lower()
print("specialist playbook guardrails: 10 missions OK")
