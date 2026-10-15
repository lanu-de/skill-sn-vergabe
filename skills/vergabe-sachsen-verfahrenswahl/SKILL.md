---
name: vergabe-sachsen-verfahrenswahl
description: Use when a contracting authority in Saxony must determine which procurement procedure (Verfahrensart) is admissible for a specific need — driven by the estimated contract value, the type of service (Liefer-/Dienstleistung, Bau, freiberuflich), and the applicable thresholds (EU-Schwellenwerte, sächsische Wertgrenzen). German keywords – Verfahrensart, Ausschreibung, Freihändige Vergabe, Direktauftrag, Auftragswert, Wertgrenze, Schwellenwert.
---

# vergabe-sachsen – Verfahrenswahl

> ⚠️ **Disclaimer:** Dieser Skill bietet **Orientierung und ersetzt keine
> Rechtsberatung.** Verbindlichkeit ergibt sich ausschließlich aus den geprüften
> Primärquellen (Gesetze, Verordnungen, Verwaltungsvorschriften) und ggf. einer
> juristischen Beratung im Einzelfall. **Ein Anspruch auf Vollständigkeit besteht nicht.
> Die Verantwortung für die (rechtliche) Richtigkeit und für die Verwendung der
> Ergebnisse liegt beim Nutzer, nicht beim Skill.** Alle Angaben ohne Gewähr.

## Hinweis an den Nutzer (verbindlich)

Schließe deine Antwort mit dem folgenden Satz ab (wörtlich), sobald du

- eine konkrete Verfahrensart empfiehlst,
- eine Wertgrenze, Frist oder Fundstelle als Grundlage für eine Entscheidung nennst oder
- ein Vergabedokument erstellst oder ausfüllst:

> *Hinweis: Orientierungshilfe ohne Anspruch auf Vollständigkeit. Die Verantwortung für die
> rechtliche Richtigkeit und die Verwendung des Ergebnisses liegt bei Ihnen; maßgeblich sind
> die genannten Primärquellen.*

Bei reinen Begriffsklärungen oder allgemeinen Erläuterungen ohne Entscheidungsbezug entfällt
der Satz.

## Überblick

Dieser Skill beantwortet die Frage: **Welches Vergabeverfahren (Verfahrensart) ist für
einen konkreten Beschaffungsbedarf einer sächsischen Vergabestelle zulässig?** Die
Antwort hängt von drei Faktoren ab – dem geschätzten Auftragswert, der Leistungsart und
den daraus folgenden Wertgrenzen – und wird in den fünf nummerierten Schritten unten
hergeleitet, jeweils mit Verweis auf die maßgebliche Referenzdatei.

Für Begriffsklärungen und die vergaberechtliche Normenhierarchie insgesamt siehe
`vergabe-sachsen-basis`. Steht die Verfahrensart fest, hilft `vergabe-sachsen-dokumente` bei der
Erstellung der zugehörigen Vergabeunterlagen (u. a. Vergabevermerk, Leistungsbeschreibung)
und `vergabe-sachsen-begleitung` bei der schrittweisen Durchführung des gewählten Verfahrens.

## Entscheidungsschritte

1. **Auftragswert (netto) schätzen.** Maßgeblich ist die vom Auftraggeber vor
   Verfahrensbeginn zu schätzende voraussichtliche Vergütung ohne Umsatzsteuer; bei
   losweiser Vergabe ist der Gesamtwert aller Lose zu betrachten, bei
   Rahmenvereinbarungen der Gesamtwert aller geplanten Einzelaufträge, bei Optionen und
   Vertragsverlängerungen deren Wert mit. Die vollständigen Schätzregeln (§ 3 VgV:
   Umgehungsverbot, 20-%-Losklausel, 48-Monats-Regel u. a.) stehen in
   `references/schwellenwerte-eu.md`, Abschnitt „Schätzung des Auftragswerts“;
   Begriffe: `references/glossar.md`.

2. **Ober- oder Unterschwelle bestimmen.** Den geschätzten Netto-Auftragswert mit dem
   einschlägigen EU-Schwellenwert vergleichen. Für eine sächsische Vergabestelle ist bei
   Liefer-/Dienstleistungen in aller Regel die Zeile „andere öffentliche Auftraggeber“
   maßgeblich (nicht die niedrigere Bundesbehörden-Schwelle); bei Bauleistungen gilt ein
   eigener, deutlich höherer Schwellenwert; bei Sektorentätigkeiten wiederum ein eigener
   Wert. Aktuelle Werte und Fundstellen: `references/schwellenwerte-eu.md`.

3. **Leistungsart bestimmen.** Liefer-/Dienstleistung, Bauleistung oder freiberufliche
   Leistung? Freiberufliche Leistungen gelten vergaberechtlich als Dienstleistungsauftrag
   und haben **keinen eigenen** Schwellenwert (siehe `references/schwellenwerte-eu.md`).
   Von der Leistungsart hängt ab, welche Verfahrensordnung greift: VgV/VOL/A für
   Liefer-/Dienstleistungen, VOB/A für Bauleistungen. **Achtung Sonderweg:**
   Unterschwellige freiberufliche Leistungen, deren Aufgabe vorab nicht eindeutig und
   erschöpfend beschreibbar ist, unterliegen in Sachsen **keinem förmlichen
   Vergabeverfahren** (§ 1 Abs. 3 SächsVergabeG; § 1 Satz 2 VOL/A schließt freiberufliche
   Leistungen sogar generell aus) — siehe
   `references/verfahrensarten.md`, Abschnitt „Unterschwelle — Freiberufliche
   Leistungen“; oberschwellig gelten die §§ 73 ff. VgV.

4. **Zulässige Verfahrensart ermitteln und sächsische Wertgrenzen prüfen.** Anhand von
   Wertbereich (Schritt 2) und Leistungsart (Schritt 3) die Tabelle in
   `references/verfahrensarten.md` konsultieren: Oberschwellig richtet sich die Wahl nach
   GWB/VgV bzw. VOB/A Abschnitt 2 (Regelverfahren vs. an Ausnahmetatbestände gebundene
   Verfahren); unterschwellig gelten in Sachsen für Liefer-/Dienstleistungen die VOL/A und
   für Bauleistungen die VOB/A Abschnitt 1 (siehe `## Sachsen-Besonderheiten`). Die
   konkreten, den jeweiligen Ausnahmeverfahren zugeordneten Wertgrenzen stehen in
   `references/wertgrenzen-sachsen.md`.

5. **Fristen ermitteln.** Zur gewählten Verfahrensart die Mindest- bzw.
   Angemessenheitsfristen für Teilnahmeanträge und Angebote nachschlagen:
   `references/fristen.md`.

## Sachsen-Besonderheiten

- **Unterschwelle Liefer-/Dienstleistungen = VOL/A, nicht UVgO.** Sachsen hat die UVgO
  für eigene Landes-/Kommunalvergaben bislang nicht eingeführt; maßgeblich ist weiterhin
  die VOL/A (1. Abschnitt). Damit gibt es in Sachsen unterschwellig **keine
  „Verhandlungsvergabe“** (das ist UVgO-Terminologie) – die entsprechende VOL/A-Verfahrensart
  heißt „**Freihändige Vergabe**“. Ein Agent, der aus allgemeinem Wissen heraus für einen
  sächsischen Fall auf „UVgO-Verhandlungsvergabe“ schließt, liegt falsch. Hintergrund:
  `vergabe-sachsen-basis`.
- **Genuin sächsischer Wert: Freihändige Vergabe nach § 4 SächsVergabeG.** Sowohl für
  Liefer-/Dienstleistungen (i. V. m. § 3 Abs. 5 Buchst. i VOL/A) als auch für Bauleistungen
  (i. V. m. § 3a Abs. 3 VOB/A; das Gesetz verweist noch auf den früheren § 3 Abs. 5 VOB/A)
  legt § 4 SächsVergabeG eine eigene, landesrechtliche
  Wertgrenze fest – der einzige originär sächsische Betrag in diesem Themenfeld. Konkreter
  Wert: `references/wertgrenzen-sachsen.md`.
- **Direktkauf.** Für Liefer-/Dienstleistungen existiert unterhalb der Freihändigen
  Vergabe zusätzlich ein Bagatellwert für die Beschaffung ganz ohne förmliches
  Vergabeverfahren (§ 3 Abs. 6 VOL/A). Konkreter Wert: `references/wertgrenzen-sachsen.md`.
- **Bauleistungen = VOB/A Abschnitt 1.** Unterschwellig gilt für Bauleistungen bundesweit
  und auch in Sachsen die VOB/A Abschnitt 1 (Öffentliche Ausschreibung, Beschränkte
  Ausschreibung, Freihändige Vergabe, Direktauftrag). Die Bau-Wertgrenzen für Direktauftrag
  und Freihändige Vergabe sind in Sachsen **„(zu prüfen)“** (siehe nächste Punkte).
- **Freiberufliche Leistungen unterschwellig: kein förmliches Verfahren.** Ist die
  Aufgabe vorab nicht eindeutig und erschöpfend beschreibbar (typisch: Planungs-,
  Architekten-, Ingenieur-, Gutachterleistungen mit Lösungsspielraum), greifen weder
  SächsVergabeG noch VOL/A (§ 1 Abs. 3 SächsVergabeG, § 1 Satz 2 VOL/A); zu beachten
  bleiben Haushaltsgrundsätze, Wettbewerb durch Vergleichsangebote und Dokumentation —
  siehe `references/sachsen-spezifika.md`. Auch freiberufliche Leistungen mit beschreibbarer
  Aufgabe fallen nicht unter die VOL/A-Verfahren (§ 1 Satz 2 VOL/A), wohl aber unter das
  SächsVergabeG (u. a. § 8) — Verfahrensgestaltung dann nach Haushaltsrecht **„(zu prüfen)“**.
- **Bau-Wertgrenze Freihändige Vergabe: Normwiderspruch „(zu prüfen)“.** Zwischen der
  landesgesetzlichen Grenze des § 4 SächsVergabeG und der zum 01.01.2026 neu gefassten,
  höheren Grenze der Bundes-VOB/A (§ 3a Abs. 3) besteht ein amtlich noch nicht geklärter
  Widerspruch. Dieser Punkt ist in `references/wertgrenzen-sachsen.md` ausdrücklich als
  **„(zu prüfen)“** gekennzeichnet und darf nicht als gesichert dargestellt werden; im
  Zweifel ist von der niedrigeren landesgesetzlichen Grenze auszugehen.

## Kleiner Entscheidungsbaum

Der folgende Ablauf bildet nur die *Relation* zu den jeweiligen Schwellen/Wertgrenzen ab
(„≥ EU-Schwelle?“, „≤ Grenze der Freihändigen Vergabe?“) – die konkreten Beträge stehen
ausschließlich in `references/schwellenwerte-eu.md` und `references/wertgrenzen-sachsen.md`:

```
Auftragswert (netto) geschätzt (Schritt 1)
│
├─ ≥ einschlägiger EU-Schwellenwert? (schwellenwerte-eu.md)
│   └─ ja → Oberschwelle: GWB/VgV bzw. VOB/A Abschnitt 2 (verfahrensarten.md)
│
└─ nein → Unterschwelle (Sachsen)
    ├─ freiberufliche Leistung, Aufgabe vorab nicht eindeutig
    │   und erschöpfend beschreibbar?                          → kein förmliches Verfahren
    │                                                              (§ 1 Abs. 3 SächsVergabeG,
    │                                                              § 1 VOL/A; Haushaltsrecht,
    │                                                              Vergleichsangebote)
    ├─ Liefer-/Dienstleistung → VOL/A
    │   ├─ ≤ Bagatellwert Direktkauf (§ 3 Abs. 6 VOL/A)?      → Direktkauf
    │   ├─ ≤ Wertgrenze Freihändige Vergabe (§ 4 SächsVergabeG)? → Freihändige Vergabe
    │   └─ sonst                                                → Öffentliche Ausschreibung
    │                                                              (Regelfall) bzw. Beschränkte
    │                                                              Ausschreibung bei Ausnahme-
    │                                                              tatbestand (§ 3 VOL/A)
    └─ Bau → VOB/A Abschnitt 1
        ├─ ≤ Wertgrenze Direktauftrag
        │   (§ 3a Abs. 4 VOB/A – „(zu prüfen)“, s. u.)?          → Direktauftrag
        ├─ ≤ Wertgrenze Freihändige Vergabe
        │   (§ 4 SächsVergabeG vs. § 3a Abs. 3 VOB/A
        │   – „(zu prüfen)“, s. u.)?                             → Freihändige Vergabe
        └─ sonst                                                → Öffentliche/Beschränkte
                                                                     Ausschreibung (§ 3a VOB/A)
```

**Achtung Bau-Zweig:** Die Prüfreihenfolge setzt voraus, dass die Direktauftragsgrenze
*unter* der Grenze der Freihändigen Vergabe liegt. Das trifft nach Bundes-VOB/A zu, in
Sachsen aber nicht ohne Weiteres: Die landesgesetzliche Grenze der Freihändigen Vergabe
(§ 4 SächsVergabeG) liegt unter der Direktauftragsgrenze der Bundes-VOB/A, und für den
Direktauftrag wird eine Deckelung auf die § 4-Grenze vertreten. Beide Bau-Wertgrenzen
sind deshalb **„(zu prüfen)“** — vor einer Festlegung `references/wertgrenzen-sachsen.md`
(Zeilen Direktauftrag und Freihändige Vergabe Bau sowie Abschnitt „Ungeklärter
Widerspruch“) lesen und die Unsicherheit offen benennen, statt eine Verfahrensart als
gesichert auszugeben.

## Aktualität

Der Datenstand der `references/`-Dateien ist der **01.07.2026**, inhaltliche Nachprüfung
und Ergänzungen zum **02.07.2026**, Korrekturen zum **15.10.2026**. Vor jeder verbindlichen
Auskunft die konkreten Beträge und Fristen in der jeweiligen Referenzdatei prüfen und bei
Bedarf gegen die amtliche Primärquelle verifizieren (`revosax.sachsen.de` für
SächsVergabeG/VOL/A, `gesetze-im-internet.de` für GWB/VgV). Als **„(zu prüfen)“**
markierte Punkte – insbesondere die sächsischen Bau-Wertgrenzen bei der Freihändigen
Vergabe – nicht ungeprüft als gesichert weitergeben.
