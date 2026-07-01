# Installation

Die Skill-Sammlung **sn-vergabe** lässt sich auf drei Wegen nutzen. Das `SKILL.md`-Format
ist überall gleich — es gibt keine Format-Konflikte.

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
/plugin install sn-vergabe@sn-vergabe
```

Aktualisieren: `/plugin marketplace update sn-vergabe`.

## 3. Manuell (ZIP)

ZIP herunterladen, `skills/`-Ordner entpacken und wie unter 1. nach `~/.claude/skills/` legen.

## Hinweis zur Aktualität

Die Rechtsdaten haben einen Datenstand (siehe README und die `Stand`-Spalten in
`shared/references/`). Vor verbindlicher Nutzung die Primärquelle prüfen.
