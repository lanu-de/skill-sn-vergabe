# Installation

Die Skill-Sammlung **vergabe-sachsen** lässt sich in Claude auf drei Wegen nutzen. Das
`SKILL.md`-Format ist überall gleich — es gibt keine Format-Konflikte. Für die Nutzung
mit ChatGPT siehe Abschnitt 4.

> ⚠️ **Disclaimer:** Diese Skills bieten Orientierung und ersetzen keine Rechtsberatung.

## 1. Claude Desktop (empfohlen für Endnutzer)

Claude Desktop kennt keine `/plugin`-Befehle. Die Skills werden direkt eingebunden:

1. Repository klonen oder als ZIP herunterladen.
2. Die vier Ordner aus `skills/` nach `~/.claude/skills/` kopieren
   (Windows: `%USERPROFILE%\.claude\skills\`).
3. Claude Desktop neu starten; die Skills stehen zur Verfügung.

## 2. Claude Code (CLI/IDE) — Plugin über den Marketplace

```
/plugin marketplace add lanu-de/skill-sn-vergabe
/plugin install vergabe-sachsen@vergabe-sachsen
```

Aktualisieren: `/plugin marketplace update vergabe-sachsen`.

## 3. Manuell (ZIP)

ZIP herunterladen, `skills/`-Ordner entpacken und wie unter 1. nach `~/.claude/skills/` legen.

## 4. Nutzung mit ChatGPT (Nachbau, mit Einschränkungen)

ChatGPT kennt das Claude-Skill-Format nicht — eine „Installation“ wie oben gibt es dort
nicht. Die Inhalte sind aber gewöhnliche Markdown-Dateien und lassen sich als
Wissensbasis in ChatGPT nachbauen. Zwei Wege:

**a) Als Projekt (für die eigene Nutzung):**

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

**b) Als Custom GPT (zum Teilen mit Kolleginnen und Kollegen):**

Wie a), nur als „GPT“ angelegt: GPT erstellen, die Dateien unter „Wissen“ hochladen,
dieselben Anweisungen eintragen. Der fertige GPT lässt sich per Link im Team teilen.
Das Erstellen erfordert einen Bezahltarif (ChatGPT Plus/Team).

**Einschränkungen gegenüber Claude:** Es gibt kein automatisches Erkennen, welcher
Skill für eine Frage zuständig ist; ChatGPT durchsucht die hochgeladenen Dateien
stichwortartig, statt sie gezielt vollständig zu lesen — Antworten daher immer gegen
die genannte Fundstelle prüfen. Bei aktualisierten Referenzdaten müssen die Dateien
manuell neu hochgeladen werden.

## Hinweis zur Aktualität

Die Rechtsdaten haben einen Datenstand (siehe README und die `Stand`-Spalten in
`shared/references/`). Vor verbindlicher Nutzung die Primärquelle prüfen.
