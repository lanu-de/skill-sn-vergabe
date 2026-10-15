from pathlib import Path

from scripts.sync_shared import sync


def test_sync_copies_references_into_each_skill(tmp_path: Path):
    ref = tmp_path / "shared" / "references"
    ref.mkdir(parents=True)
    (ref / "a.md").write_text("Inhalt A", encoding="utf-8")
    (tmp_path / "skills" / "skill-eins").mkdir(parents=True)
    (tmp_path / "skills" / "skill-zwei").mkdir(parents=True)

    written = sync(tmp_path)

    for skill in ("skill-eins", "skill-zwei"):
        dest = tmp_path / "skills" / skill / "references" / "a.md"
        assert dest.read_text(encoding="utf-8") == "Inhalt A"
    assert len(written) == 2


def test_sync_removes_orphaned_references(tmp_path: Path):
    ref = tmp_path / "shared" / "references"
    ref.mkdir(parents=True)
    (ref / "neu.md").write_text("neu", encoding="utf-8")
    dest = tmp_path / "skills" / "skill-eins" / "references"
    dest.mkdir(parents=True)
    (dest / "alt.md").write_text("veraltet", encoding="utf-8")

    sync(tmp_path)

    assert sorted(p.name for p in dest.iterdir()) == ["neu.md"]


def test_sync_writes_plugin_version_into_skill_frontmatter(tmp_path: Path):
    (tmp_path / "shared" / "references").mkdir(parents=True)
    (tmp_path / ".claude-plugin").mkdir()
    (tmp_path / ".claude-plugin" / "plugin.json").write_text('{"version": "1.2.3"}', encoding="utf-8")
    skill = tmp_path / "skills" / "skill-eins"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text(
        '---\nname: skill-eins\ndescription: x\nmetadata:\n  version: "0.0.0"\n---\n\nversion: "0.0.0" im Text bleibt\n',
        encoding="utf-8",
    )

    sync(tmp_path)

    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    assert 'metadata:\n  version: "1.2.3"\n---' in text
    assert 'version: "0.0.0" im Text bleibt' in text


from scripts.sync_shared import check_fundstellen


def _write_ref(tmp_path: Path, name: str, content: str) -> None:
    ref = tmp_path / "shared" / "references"
    ref.mkdir(parents=True, exist_ok=True)
    (ref / name).write_text(content, encoding="utf-8")


def test_check_passes_when_table_is_complete(tmp_path: Path):
    _write_ref(
        tmp_path, "w.md",
        "| Gegenstand | Wert | Fundstelle | Stand |\n"
        "|---|---|---|---|\n"
        "| Direktauftrag | 5.000 EUR | Ziffer X VwV | 01.07.2026 |\n",
    )
    assert check_fundstellen(tmp_path) == []


def test_check_flags_missing_fundstelle(tmp_path: Path):
    _write_ref(
        tmp_path, "w.md",
        "| Gegenstand | Wert | Fundstelle | Stand |\n"
        "|---|---|---|---|\n"
        "| Direktauftrag | 5.000 EUR | TODO | 01.07.2026 |\n",
    )
    errors = check_fundstellen(tmp_path)
    assert len(errors) == 1
    assert "Fundstelle" in errors[0]


def test_check_matches_stand_column_exactly(tmp_path: Path):
    # „Gegenstand“ und „Stand in Sachsen“ enthalten „stand“, sind aber nicht die Stand-Spalte.
    _write_ref(
        tmp_path, "w.md",
        "| Gegenstand | Stand in Sachsen | Fundstelle | Stand |\n"
        "|---|---|---|---|\n"
        "| Direktauftrag | gilt | Ziffer X VwV | TODO |\n",
    )
    errors = check_fundstellen(tmp_path)
    assert len(errors) == 1
    assert "Stand" in errors[0]


from scripts.sync_shared import main


def test_main_check_returns_1_on_missing_source(tmp_path: Path):
    _write_ref(
        tmp_path, "w.md",
        "| Wert | Fundstelle | Stand |\n|---|---|---|\n| 5.000 EUR | TODO | 01.07.2026 |\n",
    )
    assert main(["check", "--root", str(tmp_path)]) == 1


def test_main_check_returns_0_when_complete(tmp_path: Path):
    _write_ref(
        tmp_path, "w.md",
        "| Wert | Fundstelle | Stand |\n|---|---|---|\n| 5.000 EUR | VwV X | 01.07.2026 |\n",
    )
    assert main(["check", "--root", str(tmp_path)]) == 0
