---
name: vergabe-sachsen-verfahrenswahl
description: Use when a contracting authority in Saxony must determine which procurement procedure (Verfahrensart) is admissible for a specific need — driven by the estimated contract value, the type of service (Liefer-/Dienstleistung, Bau, freiberuflich), and the applicable thresholds (EU-Schwellenwerte, sächsische Wertgrenzen). German keywords – Verfahrensart, Ausschreibung, Freihändige Vergabe, Direktauftrag, Auftragswert, Wertgrenze, Schwellenwert.
license: CC-BY-4.0
metadata:
  author: André Tegge
  publisher: Sächsische Landesstiftung Natur und Umwelt (LaNU)
  version: "0.3.2"
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
   [references/schwellenwerte-eu.md](references/schwellenwerte-eu.md), Abschnitt „Schätzung des Auftragswerts“;
   Begriffe: [references/glossar.md](references/glossar.md).

2. **Ober- oder Unterschwelle bestimmen.** Den geschätzten Netto-Auftragswert mit dem
   einschlägigen EU-Schwellenwert vergleichen. Für eine sächsische Vergabestelle ist bei
   Liefer-/Dienstleistungen in aller Regel die Zeile „andere öffentliche Auftraggeber“
   maßgeblich (nicht die niedrigere Bundesbehörden-Schwelle); bei Bauleistungen gilt ein
   eigener, deutlich höherer Schwellenwert; bei Sektorentätigkeiten wiederum ein eigener
   Wert. Aktuelle Werte und Fundstellen: [references/schwellenwerte-eu.md](references/schwellenwerte-eu.md).

3. **Leistungsart bestimmen.** Liefer-/Dienstleistung, Bauleistung oder freiberufliche
   Leistung? Freiberufliche Leistungen gelten vergaberechtlich als Dienstleistungsauftrag
   und haben **keinen eigenen** Schwellenwert (siehe [references/schwellenwerte-eu.md](references/schwellenwerte-eu.md)).
   Von der Leistungsart hängt ab, welche Verfahrensordnung greift: VgV/VOL/A für
   Liefer-/Dienstleistungen, VOB/A für Bauleistungen. **Achtung Sonderweg:**
   Unterschwellige freiberufliche Leistungen, deren Aufgabe vorab nicht eindeutig und
   erschöpfend beschreibbar ist, unterliegen in Sachsen **keinem förmlichen
   Vergabeverfahren** (§ 1 Abs. 3 SächsVergabeG; § 1 Satz 2 VOL/A schließt freiberufliche
   Leistungen sogar generell aus). Ist die Aufgabe dagegen beschreibbar, gilt das
   SächsVergabeG ohne VOL/A — siehe
   [references/verfahrensarten.md](references/verfahrensarten.md), Abschnitt „Unterschwelle — Freiberufliche
   Leistungen“; oberschwellig gelten die §§ 73 ff. VgV.

4. **Zulässige Verfahrensart ermitteln und sächsische Wertgrenzen prüfen.** Anhand von
   Wertbereich (Schritt 2) und Leistungsart (Schritt 3) die Tabelle in
   [references/verfahrensarten.md](references/verfahrensarten.md) konsultieren: Oberschwellig richtet sich die Wahl nach
   GWB/VgV bzw. VOB/A Abschnitt 2 (Regelverfahren vs. an Ausnahmetatbestände gebundene
   Verfahren); unterschwellig gelten in Sachsen für Liefer-/Dienstleistungen die VOL/A und
   für Bauleistungen die VOB/A Abschnitt 1 (siehe `## Sachsen-Besonderheiten`). Die
   konkreten, den jeweiligen Ausnahmeverfahren zugeordneten Wertgrenzen stehen in
   [references/wertgrenzen-sachsen.md](references/wertgrenzen-sachsen.md).
   Soll ein Verfahren ohne Wettbewerb damit begründet werden, dass nur ein Unternehmen
   die Leistung erbringen kann, muss eine dokumentierte Markterkundung das Fehlen
   vernünftiger Alternativen belegen (oberschwellig § 14 Abs. 6 VgV; siehe
   [references/markterkundung.md](references/markterkundung.md), Zeile „Alleinstellung“, und
   Skill `vergabe-sachsen-markterkundung`).

5. **Fristen ermitteln.** Zur gewählten Verfahrensart die Mindest- bzw.
   Angemessenheitsfristen für Teilnahmeanträge und Angebote nachschlagen:
   [references/fristen.md](references/fristen.md).

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
  Wert: [references/wertgrenzen-sachsen.md](references/wertgrenzen-sachsen.md).
- **Direktkauf.** Für Liefer-/Dienstleistungen existiert unterhalb der Freihändigen
  Vergabe zusätzlich ein Bagatellwert für die Beschaffung ganz ohne förmliches
  Vergabeverfahren (§ 3 Abs. 6 VOL/A). Eine höhere sächsische Grenze gibt es nicht; in
  Praxisquellen genannte höhere Werte gelten in Sachsen nicht. Konkreter Wert:
  [references/wertgrenzen-sachsen.md](references/wertgrenzen-sachsen.md).
- **Bauleistungen = VOB/A Abschnitt 1.** Unterschwellig gilt für Bauleistungen bundesweit
  und auch in Sachsen die VOB/A Abschnitt 1 (Öffentliche Ausschreibung, Beschränkte
  Ausschreibung, Freihändige Vergabe, Direktauftrag) — aber nur, soweit das SächsVergabeG
  nichts anderes bestimmt (§ 1 Abs. 2). Für Freihändige Vergabe und Direktauftrag bestimmt
  § 4 SächsVergabeG etwas anderes (nächster Punkt).
- **Bau: § 4 SächsVergabeG deckelt Freihändige Vergabe und Direktauftrag.** Nach
  Auffassung des Justiziariats der LaNU (29.10.2026) gilt für die Freihändige Vergabe von
  Bauleistungen die landesgesetzliche Grenze des § 4 SächsVergabeG, nicht die höhere Grenze
  des § 3a Abs. 3 VOB/A; der veraltete Verweis auf „§ 3 Abs. 5 VOB/A“ ändert daran nichts.
  Der Direktauftrag (§ 3a Abs. 4 VOB/A) ist auf dieselbe Grenze gedeckelt; auch für ihn
  sind wegen Wirtschaftlichkeit und Sparsamkeit in der Regel **drei oder mehr Angebote**
  einzuholen. Die Grenze der Beschränkten Ausschreibung ohne Teilnahmewettbewerb (§ 3a
  Abs. 2 VOB/A) gilt uneingeschränkt. Werte und Begründung:
  [references/wertgrenzen-sachsen.md](references/wertgrenzen-sachsen.md). Die Auffassung ist
  eine interne Rechtsauffassung, keine amtliche Klärung; das so offen sagen.
- **Freiberufliche Leistungen unterschwellig: zwei Fälle.** Ist die Aufgabe vorab nicht
  eindeutig und erschöpfend beschreibbar (typisch: Planungs-, Architekten-, Ingenieur-,
  Gutachterleistungen mit Lösungsspielraum), greifen weder SächsVergabeG noch VOL/A (§ 1
  Abs. 3 SächsVergabeG, § 1 Satz 2 VOL/A); zu beachten bleiben Haushaltsgrundsätze,
  Vergleichsangebote in einer dem Auftragswert angemessenen Zahl und Dokumentation
  mindestens nach § 20 VOL/A. Ist die Aufgabe **beschreibbar**, gilt das SächsVergabeG
  (insbesondere §§ 4, 5, 8), die VOL/A wegen § 1 Satz 2 VOL/A aber nicht; das Verfahren
  richtet sich nach der SäHO — siehe [references/sachsen-spezifika.md](references/sachsen-spezifika.md).

## Kleiner Entscheidungsbaum

Der folgende Ablauf bildet nur die *Relation* zu den jeweiligen Schwellen/Wertgrenzen ab
(„≥ EU-Schwelle?“, „≤ Grenze der Freihändigen Vergabe?“) – die konkreten Beträge stehen
ausschließlich in [references/schwellenwerte-eu.md](references/schwellenwerte-eu.md) und [references/wertgrenzen-sachsen.md](references/wertgrenzen-sachsen.md):

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
    ├─ freiberufliche Leistung, Aufgabe beschreibbar?          → SächsVergabeG ohne VOL/A
    │                                                              (§§ 4, 5, 8 SächsVergabeG;
    │                                                              Verfahren nach SäHO)
    ├─ Liefer-/Dienstleistung → VOL/A
    │   ├─ ≤ Bagatellwert Direktkauf (§ 3 Abs. 6 VOL/A)?      → Direktkauf
    │   ├─ ≤ Wertgrenze Freihändige Vergabe (§ 4 SächsVergabeG)? → Freihändige Vergabe
    │   └─ sonst                                                → Öffentliche Ausschreibung
    │                                                              (Regelfall) bzw. Beschränkte
    │                                                              Ausschreibung bei Ausnahme-
    │                                                              tatbestand (§ 3 VOL/A)
    └─ Bau → VOB/A Abschnitt 1
        ├─ ≤ Wertgrenze Freihändige Vergabe
        │   (§ 4 SächsVergabeG; deckelt auch den
        │   Direktauftrag nach § 3a Abs. 4 VOB/A)?               → Direktauftrag (mit in der
        │                                                              Regel 3+ Angeboten) oder
        │                                                              Freihändige Vergabe
        ├─ ≤ Wertgrenze Beschränkte Ausschreibung
        │   ohne Teilnahmewettbewerb (§ 3a Abs. 2 VOB/A)?        → Beschränkte Ausschreibung
        │                                                              ohne Teilnahmewettbewerb
        └─ sonst                                                → Öffentliche Ausschreibung/
                                                                     Beschränkte Ausschreibung mit
                                                                     Teilnahmewettbewerb (§ 3a VOB/A)
```

**Hinweis Bau-Zweig:** In Sachsen fallen die Grenzen für Direktauftrag und Freihändige
Vergabe bei Bauleistungen zusammen, weil § 4 SächsVergabeG beide deckelt (Justiziariat der
LaNU, 29.10.2026; Werte in [references/wertgrenzen-sachsen.md](references/wertgrenzen-sachsen.md)).
Unterhalb dieser Grenze ist auch beim Direktauftrag Wettbewerb über mehrere Angebote
herzustellen. In der LaNU wird auch unterhalb der Grenzen oft öffentlich ausgeschrieben, wenn
kein ausreichender Bieterkreis bekannt ist oder mehr Wettbewerb wirtschaftlicher ist.

## Aktualität

Der Datenstand der `references/`-Dateien ist der **01.07.2026**, inhaltliche Nachprüfung
und Ergänzungen zum **02.07.2026**, Korrekturen zum **15.10.2026**, Antworten des
Justiziariats der LaNU zu den offenen Rechtsfragen zum **29.10.2026**. Vor jeder verbindlichen
Auskunft die konkreten Beträge und Fristen in der jeweiligen Referenzdatei prüfen und bei
Bedarf gegen die amtliche Primärquelle verifizieren (`revosax.sachsen.de` für
SächsVergabeG/VOL/A, `gesetze-im-internet.de` für GWB/VgV). Als **„(zu prüfen)“**
markierte Punkte nicht ungeprüft als gesichert weitergeben. Bei Angaben, die auf der
Auffassung des Justiziariats der LaNU beruhen, die Quelle nennen.
