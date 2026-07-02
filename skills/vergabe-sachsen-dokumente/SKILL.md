---
name: vergabe-sachsen-dokumente
description: Use when a contracting authority in Saxony needs to create or draft a procurement document — Vergabevermerk, Leistungsbeschreibung, Eignungs-/Zuschlagskriterien, Bekanntmachungstext, or a Zuschlags-/Absageschreiben — as a fill-in template.
---

# vergabe-sachsen – Dokumente

> ⚠️ **Disclaimer:** Dieser Skill bietet **Orientierung und ersetzt keine
> Rechtsberatung.** Verbindlichkeit ergibt sich ausschließlich aus den geprüften
> Primärquellen (Gesetze, Verordnungen, Verwaltungsvorschriften) und ggf. einer
> juristischen Beratung im Einzelfall. Alle Angaben ohne Gewähr.

## Überblick

Dieser Skill liefert **ausfüllbare Vorlagen** für die wiederkehrenden Dokumente eines
Vergabeverfahrens einer sächsischen Vergabestelle. Er setzt voraus, dass die Verfahrensart
bereits feststeht (siehe `vergabe-sachsen-verfahrenswahl`) bzw. eine allgemeine Rechtsfrage
bereits mit `vergabe-sachsen-basis` geklärt wurde, dessen Wegweiser für das Anliegen „Ein
Vergabedokument erstellen“ hierher verweist. Für die schrittweise Durchführung eines
konkreten Verfahrens (inkl. Einsatz dieser Vorlagen zum passenden Verfahrensschritt) siehe
`vergabe-sachsen-begleitung`.

## Verfügbare Vorlagen

| Dokument | Vorlage | Verfahrensschritt |
|---|---|---|
| Vergabevermerk | `assets/vergabevermerk-vorlage.md` | fortlaufende Dokumentation des gesamten Verfahrens, von Beschaffungsentscheidung bis Zuschlag |
| Leistungsbeschreibung | `assets/leistungsbeschreibung-vorlage.md` | Bestandteil der Vergabeunterlagen, vor Bekanntmachung/Aufforderung zur Angebotsabgabe |
| Absageschreiben (Vorabinformation) | `assets/absageschreiben-vorlage.md` | Information nicht berücksichtigter Bieter vor Zuschlagserteilung |
| Zuschlagsschreiben | `assets/zuschlagsschreiben-vorlage.md` | Mitteilung der Zuschlagserteilung an den erfolgreichen Bieter, nach Ablauf der Warte-/Informationsfrist |

## Nutzung

1. **Vorlage auswählen** anhand des Verfahrensschritts (Tabelle oben). Steht die
   Verfahrensart selbst noch nicht fest, zunächst `vergabe-sachsen-verfahrenswahl` konsultieren.
2. **Alle mit `[…]` markierten Platzhalter** durch die Angaben des konkreten Vergabefalls
   ersetzen (Auftraggeber, Aktenzeichen, Datum, Bieter, Auftragswert, Angebotssumme,
   Zuschlags-/Ablehnungsgründe u. Ä.). Kein Platzhalter darf unausgefüllt bleiben.
3. **Sächsische Pflichtangaben beachten** — insbesondere die beiden folgenden, die in mehreren
   Vorlagen wiederkehren:
   - **Dokumentationspflicht (Vergabevermerk):** oberschwellig § 8 VgV (Liefer-/Dienst-/
     freiberuflich) bzw. § 20 EU VOB/A (Bau); unterschwellig § 20 VOB/A Abschnitt 1 (Bau)
     bzw. § 20 VOL/A (Liefer-/Dienstleistungen); ergänzend verlangt § 5 Abs. 1 SächsVergabeG
     i. V. m. Anlage 1 die Dokumentation der stufenweisen Wertung.
     **Achtung:** § 9 SächsVergabeG regelt den **Vergabebericht** (aggregierter Bericht der
     Staatsregierung an den Landtag) — das ist **nicht** der Vergabevermerk des
     Einzelverfahrens.
   - **Vorabinformation/Wartefrist vor Zuschlag:** oberschwellig § 134 GWB, unterschwellig
     in Sachsen § 8 SächsVergabeG.
   - Die konkreten Fristen, Aufgreifschwellen (Auftragswert, ab dem die sächsische
     Informationspflicht überhaupt greift) und Fundstellen stehen ausschließlich in
     `references/sachsen-spezifika.md` — dort auch als **„(zu prüfen)“** gekennzeichnete
     Punkte unbedingt beachten und nicht als gesichert weitergeben.
4. **Vor jedem verbindlichen Einsatz** die in der jeweiligen Vorlage genannten Fundstellen
   gegen `references/rechtsquellen.md` und `references/sachsen-spezifika.md` prüfen,
   insbesondere Fristen und Wertgrenzen, da sich diese mit der angekündigten
   SächsVergabeG-Novelle ändern können.

## Aktualität

Der Datenstand aller `references/`-Dateien ist **01.07.2026**. Vor jeder verbindlichen
Verwendung einer Vorlage die konkreten Beträge, Fristen und Paragrafen in der jeweiligen
Referenzdatei prüfen und bei Bedarf gegen die amtliche Primärquelle verifizieren
(`revosax.sachsen.de` für SächsVergabeG/VOL/A, `gesetze-im-internet.de` für GWB/VgV). Als
**„(zu prüfen)“** markierte Punkte nicht ungeprüft als gesichert weitergeben.
