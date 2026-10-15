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
