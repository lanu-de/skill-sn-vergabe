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


_PLACEHOLDER = {"", "todo", "tbd", "-", "–", "—", "?", "n/a", "offen"}


def _split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(c and set(c) <= set("-: ") for c in cells)


def check_fundstellen(root: Path) -> list[str]:
    """Prueft Fundstellenpflicht in allen Referenz-Tabellen. Leere Liste = alles belegt."""
    errors: list[str] = []
    for md in sorted(shared_references_dir(root).glob("*.md")):
        header: list[str] | None = None
        idx_fund = idx_stand = None
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if "|" not in line:
                header = None
                continue
            cells = _split_row(line)
            if header is None:
                header = [c.lower() for c in cells]
                idx_fund = next((i for i, h in enumerate(header) if "fundstelle" in h), None)
                idx_stand = next((i for i, h in enumerate(header) if "stand" in h), None)
                continue
            if _is_separator(cells):
                continue
            for idx, label in ((idx_fund, "Fundstelle"), (idx_stand, "Stand")):
                if idx is not None and idx < len(cells):
                    if cells[idx].strip().lower() in _PLACEHOLDER:
                        errors.append(f"{md.name}:{lineno}: leere/unvollstaendige {label}")
    return errors


import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Referenzdaten synchronisieren/pruefen")
    parser.add_argument("command", choices=["sync", "check"])
    parser.add_argument("--root", default=None, help="Repo-Wurzel (Default: Elternordner von scripts/)")
    args = parser.parse_args(argv)

    root = Path(args.root) if args.root else Path(__file__).resolve().parent.parent

    if args.command == "sync":
        written = sync(root)
        print(f"{len(written)} Datei(en) in Skills kopiert.")
        return 0

    errors = check_fundstellen(root)
    if errors:
        print("Fundstellenpflicht verletzt:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("Fundstellenpflicht: alle Werte belegt.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
