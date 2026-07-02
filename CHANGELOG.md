# Changelog

Alle nennenswerten Änderungen an diesem Projekt werden hier dokumentiert.
Format nach [Keep a Changelog](https://keepachangelog.com/de/1.1.0/),
Versionierung nach [SemVer](https://semver.org/lang/de/).

## [Unreleased]

### Behoben
- Leistungsbeschreibungs-Vorlage: Fundstelle für die unterschwellige
  Leistungsbeschreibung von „§ 8 VOL/A“ auf **§ 7 VOL/A** korrigiert (§ 8 VOL/A regelt
  die Vergabeunterlagen).
- `wertgrenzen-sachsen.md`: Zitierfehler „§ 2 SächsVergabeG“ → **§ 1 Abs. 2
  SächsVergabeG** (dynamischer Verweis auf die VOB/A).
- `sachsen-spezifika.md`: Warte-/Stillhaltefrist — beide Fristen (15/10 Kalendertage)
  korrekt **§ 134 Abs. 2 GWB** zugeordnet (zuvor teilweise Abs. 1).
- Glossar: SächsVergabeDVO als **außer Kraft** (§ 11 SächsVergabeG) dargestellt;
  `rechtsquellen.md`: irreführender Begriff „Verhandlungsvergabe“ aus der
  SächsVergabeG-Beschreibung entfernt.
- `sachsen-spezifika.md`: veraltete Recherche-Meta-Kommentare entfernt
  (bereits umgesetzte „Korrekturbedarf glossar.md“-Hinweise, Konsistenzhinweis zur
  Plattformbezeichnung).

### Hinzugefügt
- **Freiberufliche Leistungen unterschwellig** (sächsischer Sonderweg nach § 1 Abs. 3
  SächsVergabeG / § 1 VOL/A: kein förmliches Vergabeverfahren): neuer Abschnitt in
  `verfahrensarten.md` und `sachsen-spezifika.md`, neuer Zweig im Entscheidungsbaum der
  Verfahrenswahl, Glossar-Eintrag.
- **Schätzung des Auftragswerts (§ 3 VgV)**: neuer Abschnitt in `schwellenwerte-eu.md`
  (Optionen, Lose/20-%-Klausel, Rahmenvereinbarungen, 48-Monats-Regel,
  Umgehungsverbot); Verfahrenswahl Schritt 1 entsprechend erweitert.
- **Wettbewerbsregister-Abfrage** (§ 6 WRegG) und **Vergabestatistik-Meldung**
  (VergStatVO) in Checkliste und Begleitung-Skill (Phase 7); Glossar-Einträge.
- **Aufhebung des Verfahrens** (§ 63 VgV, § 17 VOB/A, § 17 VOL/A): Hinweis in
  `verfahrensarten.md`, Glossar-Eintrag, Sonderfall-Block in der Checkliste.
- **Rahmenvereinbarungen** (§ 21 VgV, § 4 VOL/A, Auftragswert nach § 3 Abs. 4 VgV):
  Hinweis in `verfahrensarten.md`, Glossar-Eintrag.
- E-Vergabe: Pflicht zur elektronischen Kommunikation oberschwellig (§ 97 Abs. 5 GWB,
  §§ 9 ff., 53 VgV) in `sachsen-spezifika.md` ergänzt.
- Bau-Direktauftrag: Fachliteratur-Hinweis zur „berichtigenden“ Auslegung
  (Deckelung auf 25.000 EUR über § 4 SächsVergabeG) in `wertgrenzen-sachsen.md`.
- SächsVergabeG-Novelle: geplante Wertgrenzen aus dem Koalitionsvertrag
  (155.000 EUR Bau / 102.000 EUR Liefer-/Dienstleistungen, Beschränkte Ausschreibung
  ohne Teilnahmewettbewerb) nachrichtlich ergänzt.
- README: Abschnitt „Methodik“ (Recherche mit Claude Fable 5, Prüfung gegen amtliche
  Primärquellen).

### Geändert
- `rechtsquellen.md`: Einleitung präzisiert (EU-Primärrechts-Grundsätze bei
  grenzüberschreitendem Interesse; „in Sachsen statt der UVgO weiterhin die VOL/A“).
- `vergabe-sachsen-basis`: Normenhierarchie-Formulierung präzisiert (SächsVergabeG
  ordnet VOL/A/VOB/A-Anwendung an und geht diesen Vergabeordnungen vor — nicht „dem
  Bundesrecht“).
- Datenstand-Angaben auf „01.07.2026, Ergänzungen 02.07.2026“ aktualisiert.

## [0.2.0] – 2026-07-02

### Geändert
- Plugin, Marketplace und Skills von `sn-vergabe` in `vergabe-sachsen` umbenannt
  (GitHub-Repository unverändert `lanu-de/skill-sn-vergabe`).
- Referenzdaten bereinigt: veralteter Konsistenz-Hinweis und Recherche-Artefakte in
  `wertgrenzen-sachsen.md` entfernt; Glossar-Begriffsteil präzisiert (in Sachsen VOL/A
  statt UVgO); README-Umfang entsprechend korrigiert.
- Marketplace-Manifest: Beschreibung ergänzt; Owner „LaNU Sachsen“ (Schreibweise
  korrigiert) mit Website https://www.lanu.de.

### Hinzugefügt
- INSTALLATION.md: Abschnitt zur Nutzung mit ChatGPT (Projekt bzw. Custom GPT).
- GitHub Action `release-zips`: erzeugt bei jedem Release automatisch ein Zip je Skill
  und hängt es an die Release-Seite (auch für claude.ai-Upload geeignet).
- Tag-Check im Release-Workflow: bricht ab, wenn der Release-Tag nicht zur Version in
  `.claude-plugin/plugin.json` passt.

## [0.1.0] – 2026-07-01

### Hinzugefügt
- Repo-Grundgerüst (README mit Disclaimer, LICENSE CC BY 4.0, CONTRIBUTING).
- Sync-/Prüf-Werkzeug `scripts/sync_shared.py` (sync + Fundstellenprüfung + CLI), getestet (5/5).
- Referenzdatenbasis unter `shared/references/` (Datenstand 01.07.2026): Glossar,
  Rechtsquellen (inkl. haushaltsrechtlicher Grundlage), EU-Schwellenwerte, sächsische
  Wertgrenzen, Verfahrensarten, Fristen und Sachsen-Spezifika — je mit Fundstelle und Stand.
- Vier Skills (`sn-vergabe-basis`, `-verfahrenswahl`, `-dokumente`, `-begleitung`) mit Anbindung an die geteilte Datenbasis via `sync_shared.py`.
- Distribution als Claude-Code-Plugin und Single-Plugin-Marketplace (.claude-plugin/), INSTALLATION.md mit drei Installationswegen.
