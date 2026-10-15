#!/usr/bin/env python3
"""Baut die Installationspakete der Skills: je Skill eine .zip und eine .skill, dazu ein Sammel-Zip.

Eine .skill-Datei ist ein Zip mit anderer Endung (Format des Anthropic-skill-creator):
im Archiv liegt der Skill-Ordner auf oberster Ebene, also <name>/SKILL.md.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

ALL_SKILLS_ZIP = "vergabe-sachsen-alle-skills.zip"

_JUNK_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
_JUNK_DIRS = {"__pycache__"}
# Fester Zeitstempel, damit gleiche Inhalte byte-gleiche Pakete ergeben.
_FIXED_DATE = (1980, 1, 1, 0, 0, 0)
_NAME_RE = re.compile(r"^name:\s*(\S+)\s*$", re.MULTILINE)


def skill_dirs(root: Path) -> list[Path]:
    skills = root / "skills"
    if not skills.is_dir():
        return []
    return [p for p in sorted(skills.iterdir()) if (p / "SKILL.md").is_file()]


def _check_name(skill: Path) -> None:
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = text.split("---", 2)[1] if text.startswith("---") else ""
    match = _NAME_RE.search(frontmatter)
    if not match or match.group(1) != skill.name:
        found = match.group(1) if match else "fehlt"
        raise ValueError(f"{skill.name}: Frontmatter-name ({found}) muss dem Ordnernamen entsprechen")


def _files(skill: Path) -> list[Path]:
    return sorted(
        p for p in skill.rglob("*")
        if p.is_file()
        and p.name not in _JUNK_NAMES
        and not _JUNK_DIRS.intersection(p.relative_to(skill).parts)
    )


def _write_archive(target: Path, skills: list[Path]) -> None:
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for skill in skills:
            for f in _files(skill):
                info = zipfile.ZipInfo(f.relative_to(skill.parent).as_posix(), _FIXED_DATE)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                zf.writestr(info, f.read_bytes())


def build(root: Path, out_dir: Path) -> list[Path]:
    """Erzeugt alle Pakete in out_dir und gibt die geschriebenen Pfade zurueck."""
    skills = skill_dirs(root)
    for skill in skills:
        _check_name(skill)
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for skill in skills:
        for suffix in (".zip", ".skill"):
            target = out_dir / f"{skill.name}{suffix}"
            _write_archive(target, [skill])
            written.append(target)
    bundle = out_dir / ALL_SKILLS_ZIP
    _write_archive(bundle, skills)
    written.append(bundle)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Skill-Pakete (.zip/.skill) bauen")
    parser.add_argument("--root", default=None, help="Repo-Wurzel (Default: Elternordner von scripts/)")
    parser.add_argument("--out", default="dist", help="Zielordner (Default: dist/)")
    args = parser.parse_args(argv)

    root = Path(args.root) if args.root else Path(__file__).resolve().parent.parent
    try:
        written = build(root, Path(args.out))
    except ValueError as exc:
        print(f"Fehler: {exc}")
        return 1
    for path in written:
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
