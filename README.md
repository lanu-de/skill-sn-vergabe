# vergabe-sachsen – Vergabe-Skills für den Freistaat Sachsen

Eine Sammlung von Claude-Skills, die **öffentliche Auftraggeber im Freistaat Sachsen**
bei der Durchführung von Vergabeverfahren unterstützt: das richtige Verfahren wählen,
Vergabedokumente erstellen, Rechtsfragen beantworten und ein Verfahren Schritt für
Schritt durchführen.

> ⚠️ **Disclaimer:** Diese Skills bieten **Orientierung und ersetzen keine
> Rechtsberatung.** Verbindlichkeit ergibt sich ausschließlich aus den geprüften
> Primärquellen (Gesetze, Verordnungen, Verwaltungsvorschriften) und ggf. einer
> juristischen Beratung im Einzelfall. Alle Angaben ohne Gewähr.

## Zielgruppe

Alle, die im Freistaat Sachsen öffentliche Aufträge vergeben — ob in der Kommune, der
Landesbehörde, im Zweckverband oder einer anderen öffentlichen Einrichtung, mit oder
ohne eigene Vergabestelle.

## Umfang

- **Leistungsarten:** Liefer-/Dienstleistungen (oberschwellig VgV; unterschwellig gilt
  in Sachsen die VOL/A — nicht die UVgO), Bauleistungen (VOB/A), freiberufliche
  Leistungen.
- **Wertbereiche:** Oberschwelle (EU) und Unterschwelle (national/sächsisch).

## Die Skills

| Skill | Zweck |
|-------|-------|
| `vergabe-sachsen-basis` | Grundlagen, Nachschlagewerk, Rechtsfragen, Einstieg |
| `vergabe-sachsen-verfahrenswahl` | Passende Verfahrensart nach Wert & Leistungsart |
| `vergabe-sachsen-dokumente` | Vergabevermerk, Leistungsbeschreibung, Schreiben u. a. |
| `vergabe-sachsen-begleitung` | Schritt-für-Schritt durch ein komplettes Verfahren |

## Installation

Drei Wege für Claude — ausführlich in [INSTALLATION.md](INSTALLATION.md), dort auch ein
Abschnitt zur Nutzung mit ChatGPT:
- **Claude Desktop:** `skills/`-Ordner nach `~/.claude/skills/` kopieren.
- **Claude Code:** `/plugin marketplace add lanu-de/skill-sn-vergabe` → `/plugin install vergabe-sachsen@vergabe-sachsen`.
- **Manuell:** ZIP herunterladen und `skills/` ablegen.

## Rechts-Datenstand und Methodik

**Geprüft zum:** 01.07.2026, inhaltliche Nachprüfung und Ergänzungen zum 02.07.2026 —
siehe Spalte „Stand“ in den Referenzdaten unter `shared/references/`. Einzelne
landesrechtliche Punkte sind als „(zu prüfen)“ markiert (v. a. sächsische
Bau-Wertgrenzen und die angekündigte SächsVergabeG-Novelle mit
Tariftreue/Vergabemindestentgelt).

**Methodik:** Die Referenzdaten wurden mit Unterstützung von Claude (Anthropic,
Modell Claude Fable 5) recherchiert und gegen die in den Dateien genannten amtlichen
Primärquellen (REVOSax, gesetze-im-internet.de, Bundesanzeiger, EUR-Lex) sowie
unabhängige Fachquellen gegengelesen. Jede Angabe trägt Fundstelle und Prüfdatum;
als „(zu prüfen)“ markierte Punkte sind vor verbindlicher Verwendung durch eine
fachkundige Person zu verifizieren.

## Mitwirken

Siehe [CONTRIBUTING.md](CONTRIBUTING.md).

## Lizenz

[CC BY 4.0](LICENSE). Amtliche Werke/Gesetzestexte sind nach § 5 UrhG gemeinfrei; die
Lizenz betrifft die eigene Zusammenstellung, Erklärungen und Vorlagen.
