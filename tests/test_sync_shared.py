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
