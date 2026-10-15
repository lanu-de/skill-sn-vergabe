"""Prueft die Kopfdaten (Frontmatter) der echten Skills mit einem YAML-Parser.

Strenge Programme (z. B. der Skill-Upload auf claude.ai) lehnen Skills mit ungueltigem
YAML ab; dieser Test faengt das vor dem Release ab.
"""
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS = sorted(p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file())


def _frontmatter(skill: Path) -> dict:
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    assert text.startswith("---"), "SKILL.md muss mit Frontmatter beginnen"
    return yaml.safe_load(text.split("---", 2)[1])


@pytest.mark.parametrize("skill", SKILLS, ids=lambda p: p.name)
def test_frontmatter_is_valid_yaml_and_follows_standard(skill: Path):
    fm = _frontmatter(skill)

    assert fm["name"] == skill.name
    assert isinstance(fm["description"], str)
    assert 0 < len(fm["description"]) <= 1024
    assert "<" not in fm["description"] and ">" not in fm["description"]
    # Nur Felder des offenen Agent-Skills-Standards (agentskills.io).
    assert set(fm) <= {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    assert fm["license"] == "CC-BY-4.0"
    assert all(isinstance(v, str) for v in fm["metadata"].values())


def test_skill_versions_match_plugin_manifest():
    import json

    version = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
    for skill in SKILLS:
        assert _frontmatter(skill)["metadata"]["version"] == version, (
            f"{skill.name}: 'python scripts/sync_shared.py sync' ausführen"
        )


INSTRUCTIONS = ROOT / "wissensbasis" / "ANWEISUNGEN.md"


def _normalize(text: str) -> str:
    return " ".join(text.replace("> ", " ").replace("*", "").split())


def test_instructions_fit_into_assistant_instruction_fields():
    # M365-Copilot-Agents und Custom GPTs erlauben rund 8.000 Zeichen.
    assert len(INSTRUCTIONS.read_text(encoding="utf-8")) <= 8000


def test_user_notice_is_identical_in_skills_and_instructions():
    instructions = INSTRUCTIONS.read_text(encoding="utf-8")
    notice = instructions.split("„Hinweis: ", 1)[1].split("“", 1)[0]
    for skill in SKILLS:
        skill_text = _normalize((skill / "SKILL.md").read_text(encoding="utf-8"))
        assert _normalize("Hinweis: " + notice) in skill_text, skill.name
