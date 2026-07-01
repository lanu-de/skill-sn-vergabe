#!/usr/bin/env python3
"""Synchronisiert geteilte Referenzdaten in alle Skills und prueft die Fundstellenpflicht."""
from __future__ import annotations

import shutil
from pathlib import Path


def shared_references_dir(root: Path) -> Path:
    return root / "shared" / "references"


def skill_dirs(root: Path) -> list[Path]:
    skills = root / "skills"
    if not skills.is_dir():
        return []
    return [p for p in sorted(skills.iterdir()) if p.is_dir()]


def sync(root: Path) -> list[Path]:
    """Kopiert alle *.md aus shared/references/ in <skill>/references/ jedes Skills."""
    sources = sorted(shared_references_dir(root).glob("*.md"))
    written: list[Path] = []
    for skill in skill_dirs(root):
        dest_dir = skill / "references"
        dest_dir.mkdir(parents=True, exist_ok=True)
        for src in sources:
            dest = dest_dir / src.name
            shutil.copyfile(src, dest)
            written.append(dest)
    return written
