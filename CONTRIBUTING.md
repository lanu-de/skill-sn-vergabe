# Mitwirken an vergabe-sachsen

## Grundprinzipien

- **Single Source of Truth:** Geteilte Rechtsdaten stehen **nur** in
  `shared/references/`. Nie direkt in einem Skill-Ordner bearbeiten.
- **Fundstellenpflicht:** Jede Zahl (Schwellenwert, Wertgrenze, Frist) braucht in der
  Tabelle eine `Fundstelle` und einen `Stand` (`TT.MM.JJJJ`).
- **Primärquellen:** Landesrecht über revosax.sachsen.de, Bundesrecht über
  gesetze-im-internet.de, EU-Schwellenwerte über die aktuelle Delegierte Verordnung.

## Workflow beim Aktualisieren von Werten

1. Wert in der passenden Datei unter `shared/references/` ändern, Fundstelle und Stand
   aktualisieren.
2. Fundstellenpflicht prüfen: `python scripts/sync_shared.py check`
3. In alle Skills übernehmen: `python scripts/sync_shared.py sync`
4. `CHANGELOG.md` ergänzen und ggf. die Version in `.claude-plugin/plugin.json` erhöhen.
5. Änderungen committen. Die GitHub-Action „Prüfung“ wiederholt Tests, Fundstellen-Check
   und den Abgleich `shared/` ↔ Skills bei jedem Push.

## Installationspakete

`python scripts/build_packages.py` baut nach `dist/` je Skill eine `.skill`- und eine
`.zip`-Datei sowie `vergabe-sachsen-alle-skills.zip`. Beim Veröffentlichen eines
GitHub-Releases (Tag `v<Version>` passend zu `.claude-plugin/plugin.json`) geschieht das
automatisch; die Pakete werden an die Release-Seite angehängt.

## Voraussetzungen

- Python 3.9+ (nur für `sync`/`check`; nicht nötig, um die Skills zu *benutzen*).
- Das Sync- und Check-Tool nutzt ausschließlich die Python-Standardbibliothek. Es gibt daher keine
  Runtime-Dependencies und keine `requirements.txt`; nur pytest für Tests ist nötig, via
  `requirements-dev.txt`.
