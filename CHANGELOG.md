# Changelog

Alle nennenswerten Änderungen an diesem Projekt werden hier dokumentiert.
Format nach [Keep a Changelog](https://keepachangelog.com/de/1.1.0/),
Versionierung nach [SemVer](https://semver.org/lang/de/).

## [0.1.0] – 2026-07-01

### Hinzugefügt
- Repo-Grundgerüst (README mit Disclaimer, LICENSE CC BY 4.0, CONTRIBUTING).
- Sync-/Prüf-Werkzeug `scripts/sync_shared.py` (sync + Fundstellenprüfung + CLI), getestet (5/5).
- Referenzdatenbasis unter `shared/references/` (Datenstand 01.07.2026): Glossar,
  Rechtsquellen (inkl. haushaltsrechtlicher Grundlage), EU-Schwellenwerte, sächsische
  Wertgrenzen, Verfahrensarten, Fristen und Sachsen-Spezifika — je mit Fundstelle und Stand.
- Vier Skills (`sn-vergabe-basis`, `-verfahrenswahl`, `-dokumente`, `-begleitung`) mit Anbindung an die geteilte Datenbasis via `sync_shared.py`.
- Distribution als Claude-Code-Plugin und Single-Plugin-Marketplace (.claude-plugin/), INSTALLATION.md mit drei Installationswegen.
