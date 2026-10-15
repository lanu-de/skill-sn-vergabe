from __future__ import annotations

import zipfile
from pathlib import Path

import pytest

from scripts.build_packages import ALL_SKILLS_ZIP, KNOWLEDGE_ZIP, build


def _skill(root: Path, name: str, frontmatter_name: str | None = None) -> Path:
    skill = root / "skills" / name
    (skill / "references").mkdir(parents=True)
    (skill / "SKILL.md").write_text(
        f"---\nname: {frontmatter_name or name}\ndescription: Test-Skill.\n---\n\n# {name}\n",
        encoding="utf-8",
    )
    (skill / "references" / "a.md").write_text("A", encoding="utf-8")
    return skill


def test_build_creates_zip_and_skill_per_skill_plus_bundle(tmp_path: Path):
    _skill(tmp_path, "skill-eins")
    _skill(tmp_path, "skill-zwei")
    out = tmp_path / "dist"

    build(tmp_path, out)

    assert sorted(p.name for p in out.iterdir()) == sorted([
        "skill-eins.zip", "skill-eins.skill",
        "skill-zwei.zip", "skill-zwei.skill",
        ALL_SKILLS_ZIP,
    ])


def test_skill_archive_has_skill_folder_as_root(tmp_path: Path):
    _skill(tmp_path, "skill-eins")
    out = tmp_path / "dist"

    build(tmp_path, out)

    for suffix in (".zip", ".skill"):
        with zipfile.ZipFile(out / f"skill-eins{suffix}") as zf:
            assert sorted(zf.namelist()) == [
                "skill-eins/SKILL.md",
                "skill-eins/references/a.md",
            ]


def test_bundle_contains_all_skills(tmp_path: Path):
    _skill(tmp_path, "skill-eins")
    _skill(tmp_path, "skill-zwei")
    out = tmp_path / "dist"

    build(tmp_path, out)

    with zipfile.ZipFile(out / ALL_SKILLS_ZIP) as zf:
        assert "skill-eins/SKILL.md" in zf.namelist()
        assert "skill-zwei/SKILL.md" in zf.namelist()


def test_build_skips_os_junk_files(tmp_path: Path):
    skill = _skill(tmp_path, "skill-eins")
    (skill / ".DS_Store").write_bytes(b"x")
    (skill / "Thumbs.db").write_bytes(b"x")
    out = tmp_path / "dist"

    build(tmp_path, out)

    with zipfile.ZipFile(out / "skill-eins.skill") as zf:
        assert not any(n.endswith((".DS_Store", "Thumbs.db")) for n in zf.namelist())


def test_build_rejects_name_mismatch(tmp_path: Path):
    _skill(tmp_path, "skill-eins", frontmatter_name="anderer-name")

    with pytest.raises(ValueError, match="skill-eins"):
        build(tmp_path, tmp_path / "dist")


def test_build_is_reproducible(tmp_path: Path):
    _skill(tmp_path, "skill-eins")

    build(tmp_path, tmp_path / "d1")
    build(tmp_path, tmp_path / "d2")

    assert (tmp_path / "d1" / "skill-eins.skill").read_bytes() == \
        (tmp_path / "d2" / "skill-eins.skill").read_bytes()


def _knowledge_base_repo(root: Path) -> None:
    skill = _skill(root, "vergabe-sachsen-eins")
    (skill / "assets").mkdir()
    (skill / "assets" / "vorlage.md").write_text("V", encoding="utf-8")
    (root / "shared" / "references").mkdir(parents=True)
    (root / "shared" / "references" / "a.md").write_text("A", encoding="utf-8")
    (root / "wissensbasis").mkdir()
    (root / "wissensbasis" / "ANWEISUNGEN.md").write_text("Anweisungen", encoding="utf-8")


def test_knowledge_base_is_flat_folder_with_instructions_guides_and_files(tmp_path: Path):
    _knowledge_base_repo(tmp_path)
    out = tmp_path / "dist"

    build(tmp_path, out)

    with zipfile.ZipFile(out / KNOWLEDGE_ZIP) as zf:
        assert sorted(zf.namelist()) == [
            "vergabe-sachsen-wissensbasis/ANWEISUNGEN.md",
            "vergabe-sachsen-wissensbasis/a.md",
            "vergabe-sachsen-wissensbasis/leitfaden-eins.md",
            "vergabe-sachsen-wissensbasis/vorlage.md",
        ]


def test_knowledge_base_rejects_duplicate_file_names(tmp_path: Path):
    _knowledge_base_repo(tmp_path)
    (tmp_path / "shared" / "references" / "vorlage.md").write_text("doppelt", encoding="utf-8")

    with pytest.raises(ValueError, match="vorlage.md"):
        build(tmp_path, tmp_path / "dist")


def test_no_knowledge_base_without_instructions(tmp_path: Path):
    _skill(tmp_path, "skill-eins")
    out = tmp_path / "dist"

    build(tmp_path, out)

    assert not (out / KNOWLEDGE_ZIP).exists()
