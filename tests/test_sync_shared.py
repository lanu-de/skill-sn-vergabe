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
