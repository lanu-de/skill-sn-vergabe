---
name: vergabe-sachsen-begleitung
description: Use when a contracting authority in Saxony is carrying out a complete procurement procedure from needs assessment through award and documentation, and wants step-by-step guidance with checklists and the applicable documentation duties.
---

# vergabe-sachsen – Begleitung

> ⚠️ **Disclaimer:** Dieser Skill bietet **Orientierung und ersetzt keine
> Rechtsberatung.** Verbindlichkeit ergibt sich ausschließlich aus den geprüften
> Primärquellen (Gesetze, Verordnungen, Verwaltungsvorschriften) und ggf. einer
> juristischen Beratung im Einzelfall. Alle Angaben ohne Gewähr.

## Überblick

Dieser Skill begleitet ein **konkretes Vergabeverfahren einer sächsischen
Vergabestelle Schritt für Schritt** — von der Bedarfsermittlung bis zum Zuschlag
und dessen Dokumentation. Er führt die übrigen `vergabe-sachsen`-Skills entlang des
Verfahrensablaufs zusammen: Für die Wahl der Verfahrensart verweist er auf
`vergabe-sachsen-verfahrenswahl`, für die Erstellung der Vergabeunterlagen auf
`vergabe-sachsen-dokumente`; für allgemeine Begriffs- und Rechtsfragen siehe
`vergabe-sachsen-basis`.

Die sieben Phasen unten bilden den **typischen Ablauf eines Vergabeverfahrens** ab
(Ober- wie Unterschwelle); je Phase wird auf die maßgebliche Referenzdatei und –
soweit einschlägig – den zuständigen Fachskill verwiesen. Eine schrittweise
Checkliste zum Abhaken steht in `checklisten/checkliste-verfahren.md`.

## Phasen

1. **Bedarfsermittlung und Schätzung des Auftragswerts** — Beschaffungsbedarf
   feststellen, Leistungsart bestimmen (Liefer-/Dienstleistung, Bauleistung,
   freiberufliche Leistung) und den voraussichtlichen Auftragswert (netto, ohne
   Umsatzsteuer) schätzen, ggf. unter Berücksichtigung einer losweisen Vergabe.
   Begriffe: `references/glossar.md`; Einordnung Ober-/Unterschwelle:
   `references/schwellenwerte-eu.md` und `references/wertgrenzen-sachsen.md`.

2. **Verfahrenswahl** — anhand von Wertbereich und Leistungsart die zulässige
   Verfahrensart ermitteln. Die vollständige Herleitung mit Entscheidungsbaum
   liefert der Skill `vergabe-sachsen-verfahrenswahl`; die Verfahrensarten-Übersicht
   selbst steht in `references/verfahrensarten.md`.

3. **Vergabeunterlagen/Dokumente** — Leistungsbeschreibung, Eignungs- und
   Zuschlagskriterien sowie den (fortlaufend zu führenden) Vergabevermerk anlegen
   und den Bekanntmachungstext vorbereiten. Ausfüllbare Vorlagen liefert der Skill
   `vergabe-sachsen-dokumente`; die zugrunde liegende Dokumentationspflicht (§ 8 VgV/§ 20
   EU VOB/A oberschwellig bzw. § 20 VOB/A/§ 20 VOL/A unterschwellig; ergänzend § 5
   Abs. 1 SächsVergabeG i. V. m. Anlage 1) steht in
   `references/sachsen-spezifika.md` und `references/rechtsquellen.md`.

4. **Bekanntmachung und Fristen** — das Verfahren veröffentlichen (Vergabeplattform
   des Freistaates Sachsen, bei Bauvergaben zusätzlich die SIB-Plattform;
   oberschwellig zusätzlich EU-Amtsblatt) und die für die gewählte Verfahrensart
   geltende Teilnahme-/Angebotsfrist setzen. Fristentabelle je Verfahrensart:
   `references/fristen.md`; Plattformen: `references/sachsen-spezifika.md`.

5. **Angebotswertung** — nach Fristablauf die eingegangenen Angebote werten. In
   Sachsen gilt unterschwellig das **vierstufige Prüfschema des § 5 SächsVergabeG
   i. V. m. Anlage 1**: (1) formale Prüfung, (2) Eignungsprüfung, (3) Prüfung der
   Preisangemessenheit/Auskömmlichkeit, (4) Wirtschaftlichkeitsbewertung und
   Zuschlagsentscheidung. Die konkrete Aufgreifschwelle für Zweifel an der
   Preisangemessenheit steht in `references/sachsen-spezifika.md`; Vordruck zur
   Dokumentation der Wertung: Vergabevermerk-Vorlage in `vergabe-sachsen-dokumente`.

6. **Vorabinformation vor Zuschlag** — nicht berücksichtigte Bieter informieren,
   bevor der Vertrag geschlossen wird: unterschwellig **§ 8 SächsVergabeG**
   (Textform, sächsisches Nachprüfungsverfahren bei Beanstandung, Aufgreifschwelle
   nach Auftragswert), oberschwellig **§ 134 GWB** (Warte-/Stillhaltefrist). Die
   konkreten Fristen und Aufgreifschwellen stehen in
   `references/sachsen-spezifika.md`; Vorlage für das Absageschreiben:
   `vergabe-sachsen-dokumente`.

7. **Zuschlag und Dokumentation** — nach Ablauf der Warte-/Informationsfrist den
   Zuschlag erteilen, das Zuschlagsschreiben versenden und den Vergabevermerk
   abschließen. Vorlagen: `vergabe-sachsen-dokumente`. Zum Rechtsschutz (Nachprüfung
   ober- und unterschwellig) siehe `references/sachsen-spezifika.md`.

## Checkliste

Eine abhakbare Schritt-für-Schritt-Checkliste über alle sieben Phasen (mit
Platzhaltern und Verweisen auf die jeweils passende Referenzdatei bzw. den
passenden Fachskill) steht in `checklisten/checkliste-verfahren.md`. Sie ist eine
**skill-eigene Prozesshilfe** und wird — anders als `references/` — nicht durch den
Sync-Mechanismus überschrieben.

## Aktualität

Der Datenstand aller `references/`-Dateien ist **01.07.2026**. Vor jeder
verbindlichen Durchführung eines Verfahrens die konkreten Beträge, Fristen und
Paragrafen in der jeweiligen Referenzdatei prüfen und bei Bedarf gegen die
amtliche Primärquelle verifizieren (`revosax.sachsen.de` für SächsVergabeG/VOL/A,
`gesetze-im-internet.de` für GWB/VgV). Als **„(zu prüfen)“** markierte Punkte —
insbesondere die angekündigte SächsVergabeG-Novelle und die sächsischen
Bau-Wertgrenzen — nicht ungeprüft als gesichert weitergeben.
