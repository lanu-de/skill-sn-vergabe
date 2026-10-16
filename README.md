# vergabe-sachsen – Vergabe-Skills für den Freistaat Sachsen

Eine Sammlung von KI-Skills im offenen [Agent-Skills-Standard](https://agentskills.io), die
**öffentliche Auftraggeber im Freistaat Sachsen** bei der Durchführung von Vergabeverfahren unterstützt: das richtige Verfahren wählen,
Vergabedokumente erstellen, Rechtsfragen beantworten und ein Verfahren Schritt für
Schritt durchführen. Die Skills funktionieren mit Claude, ChatGPT, GitHub Copilot, Codex,
Cursor, Gemini CLI u. a.; für Assistenten ohne Skill-Unterstützung wie Microsoft 365
Copilot gibt es ein Wissensbasis-Paket.

> ⚠️ **Disclaimer:** Diese Skills bieten **Orientierung und ersetzen keine
> Rechtsberatung.** Verbindlichkeit ergibt sich ausschließlich aus den geprüften
> Primärquellen (Gesetze, Verordnungen, Verwaltungsvorschriften) und ggf. einer
> juristischen Beratung im Einzelfall. **Ein Anspruch auf Vollständigkeit besteht nicht.
> Die Verantwortung für die (rechtliche) Richtigkeit und für die Verwendung der
> Ergebnisse liegt beim Nutzer, nicht bei den Skills.** Alle Angaben ohne Gewähr.

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
| `vergabe-sachsen-markterkundung` | Markterkundung vor der Vergabe: Anfrage, Auswertung, Vermerk |
| `vergabe-sachsen-verfahrenswahl` | Passende Verfahrensart nach Wert & Leistungsart |
| `vergabe-sachsen-dokumente` | Vergabevermerk, Leistungsbeschreibung, Schreiben u. a. |
| `vergabe-sachsen-begleitung` | Schritt-für-Schritt durch ein komplettes Verfahren |

## Installation

Kurzfassung — Schritt für Schritt und für weitere Programme in
[INSTALLATION.md](INSTALLATION.md):

- **claude.ai / Claude Desktop:** Customize → Plugins → Add marketplace →
  `lanu-de/skill-sn-vergabe`; alternativ die `.skill`-Dateien von der
  [Release-Seite](https://github.com/lanu-de/skill-sn-vergabe/releases/latest) unter
  Customize → Skills hochladen.
- **Claude Code:** `/plugin marketplace add lanu-de/skill-sn-vergabe` →
  `/plugin install vergabe-sachsen@vergabe-sachsen`.
- **GitHub Copilot, Codex, Cursor, Gemini CLI u. a.:** `npx skills add lanu-de/skill-sn-vergabe`.
- **ChatGPT:** Skills-Upload (Business/Enterprise/Edu).
- **Microsoft 365 Copilot, ChatGPT-Projekte, Gemini Gems u. a.:**
  `vergabe-sachsen-wissensbasis.zip` von der Release-Seite — Anweisungen einfügen,
  Dateien als Wissen hochladen.

## Rechts-Datenstand und Methodik

**Geprüft zum:** 01.07.2026, inhaltliche Nachprüfung und Ergänzungen zum 02.07.2026, Korrekturen zum 15.10.2026 —
siehe Spalte „Stand“ in den Referenzdaten unter `shared/references/`. Einzelne
landesrechtliche Punkte sind als „(zu prüfen)“ markiert (v. a. sächsische
Bau-Wertgrenzen und die angekündigte SächsVergabeG-Novelle mit
Tariftreue/Vergabemindestentgelt).

**Methodik:** Die Referenzdaten wurden mit Unterstützung von Claude (Anthropic,
Modell Claude Fable 5) recherchiert und gegen die in den Dateien genannten amtlichen
Primärquellen (REVOSax, gesetze-im-internet.de, Bundesanzeiger, EUR-Lex) sowie
unabhängige Fachquellen — insbesondere die Auftragsberatungsstelle Sachsen
([abstsachsen.de](https://www.abstsachsen.de/)) — gegengelesen. Jede Angabe trägt Fundstelle und Prüfdatum;
als „(zu prüfen)“ markierte Punkte sind vor verbindlicher Verwendung durch eine
fachkundige Person zu verifizieren.

## Mitwirken

Siehe [CONTRIBUTING.md](CONTRIBUTING.md).

## Lizenz

Herausgeber: [Sächsische Landesstiftung Natur und Umwelt (LaNU)](https://www.lanu.de). Autor: André Tegge.

Lizenziert unter [CC BY 4.0](LICENSE), soweit Schutzrechte bestehen. Erstellt mit Unterstützung eines KI-Assistenten;
Inhalte beruhen auf den jeweils angegebenen Quellen.

Gesetzes- und Verordnungstexte sind amtliche Werke und gemeinfrei (§ 5 UrhG); die
Lizenz betrifft die eigene Zusammenstellung, Erklärungen und Vorlagen.
