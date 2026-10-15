# Installation

Die Skill-Sammlung **vergabe-sachsen** besteht aus vier Skills im offenen
[Agent-Skills-Format](https://agentskills.io) (`SKILL.md`). Dieses Format verstehen
inzwischen viele KI-Assistenten — Claude, ChatGPT, GitHub Copilot, Codex, Cursor,
Gemini CLI u. a. Unterschiedlich ist nur, **wie** die Skills hineinkommen.

> ⚠️ **Disclaimer:** Diese Skills bieten Orientierung und ersetzen keine Rechtsberatung.

> 💡 **Am besten immer alle vier Skills installieren.** Sie verweisen aufeinander
> (z. B. nutzt `vergabe-sachsen-begleitung` die Vorlagen aus
> `vergabe-sachsen-dokumente`). Einzeln funktionieren sie, aber mit Lücken.

## Welcher Weg passt?

| Ich nutze … | Empfohlener Weg | Abschnitt |
|---|---|---|
| **claude.ai** im Browser oder die **Claude Desktop-App** (Chat) | Plugin hinzufügen, sonst `.skill`-Dateien hochladen | [1](#1-claudeai-und-claude-desktop-app) |
| Claude **Team/Enterprise** und will Skills für alle bereitstellen | Zentral durch die Administration | [2](#2-für-die-ganze-organisation-claude-team--enterprise) |
| **Claude Code** (Terminal, IDE, „Code“-Tab der Desktop-App) | `/plugin`-Befehl | [3](#3-claude-code) |
| **GitHub Copilot, Codex, Cursor, Gemini CLI, OpenCode, Windsurf** u. a. | ein Befehl: `npx skills add …` | [4](#4-andere-ki-assistenten-copilot-codex-cursor-gemini-) |
| **ChatGPT** | Skills hochladen bzw. als Projekt nachbauen | [5](#5-chatgpt) |

Alle Download-Dateien liegen auf der
[Release-Seite](https://github.com/lanu-de/skill-sn-vergabe/releases/latest):

- **`vergabe-sachsen-….skill`** — je Skill eine Datei zum Hochladen in Claude.
- **`vergabe-sachsen-….zip`** — dasselbe als gewöhnliches Zip (z. B. für ChatGPT).
- **`vergabe-sachsen-alle-skills.zip`** — alle vier Skill-Ordner zusammen, zum
  Entpacken in einen Skill-Ordner (Abschnitte 3 und 4). **Nicht** zum Hochladen
  geeignet — Upload-Dialoge erwarten genau einen Skill pro Datei.

## 1. claude.ai und Claude Desktop-App

Gilt für den normalen Chat im Browser und in der Desktop-App (beide teilen dieselben
Einstellungen Ihres Claude-Kontos). Voraussetzung: ein bezahlter Tarif (Pro, Max,
Team oder Enterprise).

**Weg A — als Plugin (empfohlen, ohne Download):**

1. In der Seitenleiste **Customize → Plugins** öffnen.
2. **Add → Add marketplace** wählen und eingeben: `lanu-de/skill-sn-vergabe`
3. Unter **Discover** das Plugin **vergabe-sachsen** auswählen und **Add** klicken.

Damit sind alle vier Skills auf einmal installiert, und Aktualisierungen kommen
automatisch über den Marketplace.

**Weg B — `.skill`-Dateien hochladen** (falls Weg A in Ihrem Konto nicht angeboten wird):

1. Unter **Settings → Capabilities** die Code-Ausführung einschalten (Skills setzen sie
   voraus).
2. Die vier `.skill`-Dateien von der
   [Release-Seite](https://github.com/lanu-de/skill-sn-vergabe/releases/latest)
   herunterladen.
3. **Customize → Skills → + → Upload a skill** und die erste Datei auswählen.
   Für die anderen drei Dateien wiederholen.

Aktualisieren bei Weg B: neue `.skill`-Dateien herunterladen und erneut hochladen.

> Hinweis: Der Ordner `~/.claude/skills/` auf dem eigenen Rechner wird vom Chat **nicht**
> gelesen — nur von Claude Code (Abschnitt 3).

## 2. Für die ganze Organisation (Claude Team / Enterprise)

Owner können Skills und Plugins zentral bereitstellen, damit nicht jede Person selbst
installieren muss: **Organization settings → Plugins & skills**. Dort lässt sich der
Marketplace `lanu-de/skill-sn-vergabe` hinzufügen bzw. die `.skill`-Dateien hochladen
und das Plugin für alle freischalten oder als Standard setzen.

## 3. Claude Code

In Claude Code (Terminal, VS Code/JetBrains oder „Code“-Tab der Desktop-App):

```
/plugin marketplace add lanu-de/skill-sn-vergabe
/plugin install vergabe-sachsen@vergabe-sachsen
```

Aktualisieren: `/plugin marketplace update vergabe-sachsen`.

**Ohne Plugin-System:** `vergabe-sachsen-alle-skills.zip` herunterladen und den Inhalt
(die vier Ordner `vergabe-sachsen-…`) direkt nach `~/.claude/skills/` entpacken
(Windows: `%USERPROFILE%\.claude\skills\`). Danach muss es z. B.
`~/.claude/skills/vergabe-sachsen-basis/SKILL.md` geben.

## 4. Andere KI-Assistenten (Copilot, Codex, Cursor, Gemini, …)

**Ein Befehl für alle** — das Werkzeug [`skills`](https://github.com/vercel-labs/skills)
kennt die Skill-Ordner von rund 70 Programmen und fragt, wohin installiert werden soll.
Voraussetzung: [Node.js](https://nodejs.org) ist installiert.

```
npx skills add lanu-de/skill-sn-vergabe
```

Nützliche Optionen: `-g` installiert für den Benutzer statt nur für das aktuelle
Projekt, `-y` überspringt Rückfragen. Aktualisieren: `npx skills update`.

**Programmeigene Wege** (alternativ):

| Programm | Befehl |
|---|---|
| GitHub Copilot CLI | `copilot plugin marketplace add lanu-de/skill-sn-vergabe`, dann `copilot plugin install vergabe-sachsen@vergabe-sachsen` |
| Gemini CLI | je Skill: `gemini skills install https://github.com/lanu-de/skill-sn-vergabe --path skills/vergabe-sachsen-basis` (ebenso für `-verfahrenswahl`, `-dokumente`, `-begleitung`) |
| Codex | im Chat `$skill-installer` aufrufen und `lanu-de/skill-sn-vergabe` angeben |

**Manuell:** `vergabe-sachsen-alle-skills.zip` in den Skill-Ordner des Programms
entpacken:

| Programm | Skill-Ordner (für alle Projekte) |
|---|---|
| GitHub Copilot (VS Code, CLI) | `~/.copilot/skills/` |
| Codex | `~/.agents/skills/` |
| Cursor | `~/.cursor/skills/` |
| Gemini CLI | `~/.gemini/skills/` |
| OpenCode | `~/.config/opencode/skills/` |

Viele dieser Programme lesen zusätzlich `~/.agents/skills/` oder `~/.claude/skills/`.

## 5. ChatGPT

**a) Als Skills hochladen** (sofern Ihr ChatGPT-Tarif Skills anbietet, derzeit v. a.
Business/Enterprise/Edu): In ChatGPT unter **Skills → Create → Upload from your
computer** die vier `.zip`-Dateien von der Release-Seite einzeln hochladen.

**b) Als Projekt nachbauen** (für alle Tarife):

1. In ChatGPT ein neues Projekt anlegen (z. B. „Vergabe Sachsen“).
2. Als Projektdateien hochladen: die sieben Dateien aus `shared/references/`, die vier
   `SKILL.md` aus `skills/` sowie bei Bedarf die Vorlagen aus
   `skills/vergabe-sachsen-dokumente/assets/`.
3. In die Projektanweisungen den Kern der Skills übernehmen, zum Beispiel:

   > Du unterstützt eine Vergabestelle im Freistaat Sachsen. Beantworte Vergabefragen
   > ausschließlich anhand der hochgeladenen Dateien und nenne immer Fundstelle und
   > Stand. Wichtig: In Sachsen gilt unterschwellig die VOL/A, nicht die UVgO
   > („Freihändige Vergabe“ statt „Verhandlungsvergabe“). Als „(zu prüfen)“ markierte
   > Werte nie als gesichert ausgeben. Du bietest Orientierung und ersetzt keine
   > Rechtsberatung.

   Zum Teilen im Team lässt sich dasselbe als **Custom GPT** anlegen (Dateien unter
   „Wissen“, gleiche Anweisungen; erfordert einen Bezahltarif).

**Einschränkungen von b):** Kein automatisches Erkennen, welcher Skill zuständig ist;
ChatGPT durchsucht die Dateien stichwortartig, statt sie gezielt vollständig zu lesen —
Antworten daher immer gegen die genannte Fundstelle prüfen. Aktualisierte Dateien müssen
manuell neu hochgeladen werden.

## Hinweis zur Aktualität

Die Rechtsdaten haben einen Datenstand (siehe README und die `Stand`-Spalten in
`shared/references/`). Vor verbindlicher Nutzung die Primärquelle prüfen.
