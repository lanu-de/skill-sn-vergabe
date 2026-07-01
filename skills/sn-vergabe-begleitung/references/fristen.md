# Fristen — Mindestfristen je Verfahrensart (Angebots-/Teilnahmefristen)

> Teil der geteilten Referenzdaten (`shared/`). **Nicht direkt in Skills bearbeiten** –
> Änderungen ausschließlich hier in `shared/references/fristen.md` vornehmen und
> anschließend mit `python scripts/sync_shared.py sync` in alle Skills übernehmen.

Diese Datei listet die **Mindestfristen für den Eingang von Teilnahmeanträgen und Angeboten**
(Teilnahmefrist/Angebotsfrist) je Verfahrensart, getrennt nach Ober- und Unterschwelle sowie
Leistungsart, zusammen mit den zulässigen **Verkürzungstatbeständen** (Vorinformation,
elektronische Übermittlung der Angebote, Dringlichkeit, einvernehmliche Fristsetzung).
Verfahrensbezeichnungen sind konsistent mit `verfahrensarten.md`; die Wertgrenzen/Schwellen, ab
denen ein Verfahren zulässig ist, stehen in `wertgrenzen-sachsen.md` bzw. `schwellenwerte-eu.md`.
**Nicht Gegenstand dieser Datei:** die Bindefrist (Dauer der Angebotsbindung nach Fristablauf)
und die vergaberechtliche Warte-/Stillhaltefrist vor Zuschlagserteilung (§ 134 GWB) — beide
betreffen andere Verfahrensabschnitte und werden hier nur am Rande erwähnt.

> ⚠️ **Zentrales Rechercheergebnis (kritisch für die Praxis):** Das zum **01.07.2026** in Kraft
> getretene **Vergabebeschleunigungsgesetz** („Gesetz zur Beschleunigung der Vergabe
> öffentlicher Aufträge", BGBl. 2026 I Nr. 137) hat die in dieser Tabelle genannten
> **Mindestfristen der §§ 15–20 VgV inhaltlich NICHT geändert** — trotz seines
> Beschleunigungs-Titels bleiben Angebots- und Teilnahmefristen unverändert bei den seit der
> VgV-Fassung 2016 geltenden Werten (35/30/15/10 Tage je nach Verfahren und Tatbestand). Diese
> Aussage wurde am 01.07.2026 wie folgt verifiziert:
> 1. **Primärquelle:** Der aktuelle Wortlaut der §§ 15–20 VgV auf gesetze-im-internet.de wurde
>    Absatz für Absatz abgerufen und entspricht exakt der bereits vor 2026 geltenden Fassung
>    (keine neuen/kürzeren Tageszahlen, keine neuen Verkürzungstatbestände).
> 2. **Sekundärquellen:** Mehrere unabhängige, detaillierte Fachbeiträge zum
>    Vergabebeschleunigungsgesetz (cosinex-Blog, Gleiss Lutz, KPMG Law, Oppenhoff, vergabepilot.ai
>    — siehe Primärquellen-Hinweis unten) zählen die materiellen Änderungen des Gesetzes im
>    Einzelnen auf; **keine** dieser Aufstellungen nennt eine Änderung der Angebots- oder
>    Teilnahmefristen nach §§ 15–20 VgV. Die tatsächlichen Änderungen betreffen andere Bereiche:
>    neuer Losgrundsatz mit Ausnahme für Infrastrukturvorhaben (§ 97a GWB), höhere
>    Direktauftragsgrenze (§ 55 BHO, 50.000 EUR, nur Bund), erleichterte Eignungsnachweise
>    (Eigenerklärungen im ersten Schritt), Wegfall der aufschiebenden Wirkung der sofortigen
>    Beschwerde im Nachprüfungsverfahren, Wegfall des Vier-Augen-Prinzips bei elektronischen
>    Angeboten, digitale Souveränität als Zuschlagskriterium (§ 58 VgV) u. Ä. — **die
>    Fristenregime der §§ 15–20 VgV sind darunter nicht genannt.**
> 3. **Historischer Abgleich:** Die letzte inhaltliche Änderung der Fristenparagraphen §§ 15–20
>    VgV lag bereits vor 2026 (u. a. redaktionelle Anpassung des § 17 VgV im Zuge des Gesetzes
>    zur Änderung des Gesetzes zur Regelung von Ingenieur- und Architektenleistungen, in Kraft
>    19.11.2020); die dortigen Fristwerte sind identisch mit den unten genannten.
>
> **Ergebnis:** Alle unten genannten VgV-Fristen sind **unverändert (alt = neu)**. Für VOB/A
> (Abschnitt 1 und 2) gilt ohnehin ein eigener, vom Vergabebeschleunigungsgesetz unabhängiger
> Änderungsweg (Verwaltungsvorschrift/Erlass des zuständigen Bundesministeriums, nicht
> Bundesgesetz) — auch dort wurden die Fristenparagraphen (§ 10, §§ 10a–10d EU) durch das
> Vergabebeschleunigungsgesetz nicht berührt.

## Oberschwelle — Liefer-/Dienstleistungen (VgV, §§ 15–20)

| Wertbereich | Verfahren | Mindestfrist | Verkürzung möglich (Tatbestand → Frist) | Fundstelle | Stand |
|---|---|---|---|---|---|
| Oberschwelle | Offenes Verfahren – Angebotsfrist | 35 Tage, gerechnet ab dem Tag nach Absendung der Auftragsbekanntmachung | Dringlichkeit → eigener Fristenzweig, mind. 15 Tage (§ 15 Abs. 3 VgV; kein zusätzlicher Abzug für elektronische Übermittlung auf diesen Zweig); elektronische Übermittlung der Angebote → −5 Tage auf die 35-Tage-Grundfrist, d. h. 30 Tage (§ 15 Abs. 4 VgV) | § 15 Abs. 2–4 VgV: https://www.gesetze-im-internet.de/vgv_2016/__15.html | 12.05.2026 (VgV-Gesamtfassung, Vergabebeschleunigungsgesetz BGBl. 2026 I Nr. 137; § 15 inhaltlich unverändert) / 01.07.2026 geprüft |
| Oberschwelle | Nicht offenes Verfahren – Teilnahmefrist | 30 Tage, gerechnet ab Absendung der Auftragsbekanntmachung | Dringlichkeit → eigener Zweig, mind. 15 Tage (§ 16 Abs. 3 VgV); keine Verkürzung durch elektronische Übermittlung vorgesehen | § 16 Abs. 2–3 VgV: https://www.gesetze-im-internet.de/vgv_2016/__16.html | 12.05.2026 / 01.07.2026 geprüft |
| Oberschwelle | Nicht offenes Verfahren – Angebotsfrist | 30 Tage, gerechnet ab Absendung der Aufforderung zur Angebotsabgabe | Einvernehmliche Fristsetzung mit den Bewerbern (außer oberste Bundesbehörden), mangels Einvernehmen mind. 10 Tage (§ 16 Abs. 6 VgV); Dringlichkeit → eigener Zweig, mind. 10 Tage (Abs. 7); elektronische Übermittlung → −5 Tage auf die 30-Tage-Grundfrist, d. h. 25 Tage (Abs. 8) | § 16 Abs. 5–8 VgV: https://www.gesetze-im-internet.de/vgv_2016/__16.html | 12.05.2026 / 01.07.2026 geprüft |
| Oberschwelle | Verhandlungsverfahren mit Teilnahmewettbewerb – Teilnahmefrist | 30 Tage, gerechnet ab Absendung der Auftragsbekanntmachung | Dringlichkeit → eigener Zweig, mind. 15 Tage (§ 17 Abs. 3 VgV) | § 17 Abs. 2–3 VgV: https://www.gesetze-im-internet.de/vgv_2016/__17.html | 12.05.2026 / 01.07.2026 geprüft |
| Oberschwelle | Verhandlungsverfahren mit Teilnahmewettbewerb – Angebotsfrist | 30 Tage, gerechnet ab Absendung der Aufforderung zur Angebotsabgabe | Einvernehmliche Fristsetzung, mangels Einvernehmen mind. 10 Tage (§ 17 Abs. 7 VgV); Dringlichkeit → eigener Zweig, mind. 10 Tage (Abs. 8); elektronische Übermittlung → −5 Tage auf die 30-Tage-Grundfrist, d. h. 25 Tage (Abs. 9) | § 17 Abs. 6–9 VgV: https://www.gesetze-im-internet.de/vgv_2016/__17.html | 12.05.2026 / 01.07.2026 geprüft |
| Oberschwelle | Verhandlungsverfahren ohne Teilnahmewettbewerb – Angebotsfrist | Keine gesetzliche Regel-Mindestfrist. Im Sonderfall äußerster, vom Auftraggeber nicht verschuldeter Dringlichkeit nach § 14 Abs. 4 Nr. 3 VgV ist ausdrücklich **keine** Mindestfrist zu beachten (§ 17 Abs. 15 VgV); in den übrigen zulässigen Fallgruppen (Alleinstellungsmerkmal, gescheitertes Vorverfahren) gilt nur die allgemeine Angemessenheitspflicht des § 20 VgV | Entfällt (bereits Ausnahme ohne feste Mindestfrist bzw. nur Angemessenheitsmaßstab) | § 17 Abs. 5, Abs. 15 VgV i. V. m. § 14 Abs. 4 Nr. 3 VgV, § 20 VgV: https://www.gesetze-im-internet.de/vgv_2016/__17.html | 12.05.2026 / 01.07.2026 geprüft |
| Oberschwelle | Wettbewerblicher Dialog – Teilnahmefrist | 30 Tage, gerechnet ab Absendung der Auftragsbekanntmachung | Keine Verkürzung vorgesehen (weder Dringlichkeit noch elektronische Übermittlung im Wortlaut genannt) | § 18 Abs. 3 VgV: https://www.gesetze-im-internet.de/vgv_2016/__18.html | 12.05.2026 / 01.07.2026 geprüft |
| Oberschwelle | Innovationspartnerschaft – Teilnahmefrist | 30 Tage, gerechnet ab Absendung der Auftragsbekanntmachung | Keine Verkürzung vorgesehen | § 19 Abs. 3 VgV: https://www.gesetze-im-internet.de/vgv_2016/__19.html | 12.05.2026 / 01.07.2026 geprüft |
| Oberschwelle | Alle Verfahren – Angemessene Fristsetzung/Verlängerungspflicht (Grundsatznorm) | Keine feste Tageszahl; die Frist ist unter Berücksichtigung der Komplexität der Leistung und der für die Angebotsausarbeitung nötigen Zeit angemessen festzulegen; zwingende Fristverlängerung, wenn zusätzliche Auskünfte nicht mind. 6 Tage vor Ablauf der Angebotsfrist (bzw. 4 Tage bei Dringlichkeitsverfahren) erteilt werden oder der Auftraggeber wesentliche Änderungen an den Vergabeunterlagen vornimmt | Nicht einschlägig (Grundsatznorm ohne eigene Verkürzungstatbestände; wirkt als Untergrenze/Korrektiv zu allen Fristen oben) | § 20 VgV: https://www.gesetze-im-internet.de/vgv_2016/__20.html | 12.05.2026 / 01.07.2026 geprüft |

## Oberschwelle — Bauleistungen (VOB/A Abschnitt 2, „VOB/A-EU", §§ 10a–10d EU)

| Wertbereich | Verfahren | Mindestfrist | Verkürzung möglich (Tatbestand → Frist) | Fundstelle | Stand |
|---|---|---|---|---|---|
| Oberschwelle | Offenes Verfahren – Angebotsfrist | 35 Kalendertage, gerechnet ab Absendung der Auftragsbekanntmachung | Vorinformation (Vorabbekanntmachung 35 Tage bis 12 Monate vor Absendung der Auftragsbekanntmachung) → 15 Tage; Dringlichkeit → 15 Tage; elektronische Übermittlung der Angebote → −5 Tage; Verlängerung um 5 Tage, wenn bestimmte Vergabeunterlagen nicht elektronisch bereitgestellt werden können (außer bei Dringlichkeit) | § 10a EU VOB/A: https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_31012019_BWI781063060120180001604634.htm | 14.02.2024 (letzte Änderungsbekanntmachung VOB/A Abschnitt 2; durch Vergabebeschleunigungsgesetz nicht berührt) / 01.07.2026 geprüft |
| Oberschwelle | Nicht offenes Verfahren / Verhandlungsverfahren mit Teilnahmewettbewerb – Teilnahmefrist | 30 Kalendertage, gerechnet ab Absendung der Auftragsbekanntmachung | Dringlichkeit → 15 Tage (§ 10b Abs. 5 EU VOB/A) | § 10b Abs. 1, 5 EU VOB/A i. V. m. § 10c Abs. 1 EU VOB/A: https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_31012019_BWI781063060120180001604634.htm | 14.02.2024 / 01.07.2026 geprüft |
| Oberschwelle | Nicht offenes Verfahren / Verhandlungsverfahren mit Teilnahmewettbewerb – Angebotsfrist | 30 Kalendertage, gerechnet ab Absendung der Aufforderung zur Angebotsabgabe | Vorinformation → 10 Tage (§ 10b Abs. 3 EU VOB/A); elektronische Übermittlung → −5 Tage (Abs. 4); Dringlichkeit → 10 Tage (Abs. 5) | § 10b Abs. 2–5 EU VOB/A i. V. m. § 10c Abs. 1 EU VOB/A: https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_31012019_BWI781063060120180001604634.htm | 14.02.2024 / 01.07.2026 geprüft |
| Oberschwelle | Verhandlungsverfahren ohne Teilnahmewettbewerb – Angebotsfrist | Ausreichende Angebotsfrist; auch bei Dringlichkeit nicht unter 10 Kalendertagen | Entfällt (bereits gesetzlicher Mindestwert; keine Unterschreitung von 10 Tagen zulässig, auch nicht bei Dringlichkeit) | § 10c Abs. 2 EU VOB/A: https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_31012019_BWI781063060120180001604634.htm | 14.02.2024 / 01.07.2026 geprüft |
| Oberschwelle | Wettbewerblicher Dialog / Innovationspartnerschaft – Teilnahmefrist | 30 Kalendertage, gerechnet ab Absendung der Auftragsbekanntmachung | Verweist auf § 10b Abs. 7–9 EU VOB/A (entsprechende Anwendung); ob daraus zusätzlich zur elektronischen Verkürzung auch eine eigenständige Dringlichkeits-Verkürzung der Teilnahmefrist folgt, ließ sich anhand der verfügbaren Quellen nicht abschließend und widerspruchsfrei verifizieren — **Verkürzungsumfang im Dringlichkeitsfall (zu prüfen)**, Grundfrist von 30 Tagen ist gesichert | § 10d EU VOB/A: https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_31012019_BWI781063060120180001604634.htm | 14.02.2024 / 01.07.2026 geprüft |

## Unterschwelle — Liefer-/Dienstleistungen (Sachsen: VOL/A, § 10)

Im Unterschwellenbereich gibt es für Liefer-/Dienstleistungen in Sachsen (VOL/A statt UVgO,
siehe `verfahrensarten.md`) **keine EU-artigen, in Tagen bezifferten Mindestfristen**. Maßgeblich
ist stattdessen ein allgemeiner Angemessenheitsmaßstab.

| Wertbereich | Verfahren | Mindestfrist | Verkürzung möglich (Tatbestand → Frist) | Fundstelle | Stand |
|---|---|---|---|---|---|
| Unterschwelle | Öffentliche Ausschreibung / Beschränkte Ausschreibung (mit oder ohne Teilnahmewettbewerb) / Freihändige Vergabe – Teilnahme-, Angebots- und Bindefrist | Keine gesetzlich fixierte Tageszahl. Wörtlich: „Für die Bearbeitung und Abgabe der Teilnahmeanträge und der Angebote sowie für die Geltung der Angebote sind ausreichende Fristen (Teilnahme-, Angebots- und Bindefristen) vorzusehen" (§ 10 Abs. 1 VOL/A) — die Frist muss lediglich der Komplexität der Leistung und dem Bearbeitungsaufwand angemessen sein | Kein Katalog von Regel-/Ausnahmefristen wie im Oberschwellenbereich, daher kein „Verkürzungstatbestand" im engeren Sinn. In der Vergabepraxis wird zur Konkretisierung der „Ausreichung" häufig orientierend auf die Mindestfristen der VgV zurückgegriffen, ohne dass dies rechtlich verbindlich vorgeschrieben ist — **Praxis-Konvention, keine amtliche sächsische Konkretisierung gefunden (zu prüfen)** | § 10 Abs. 1 VOL/A (Ausgabe 2009) i. V. m. § 2 SächsVergabeG: https://www.vergabevorschriften.de/vol-a/10 ; https://www.revosax.sachsen.de/vorschrift/12749-Saechsisches-Vergabegesetz | 20.11.2009 (VOL/A-Fassung, seither unverändert) / 01.07.2026 geprüft |

## Unterschwelle — Bauleistungen (Sachsen: VOB/A Abschnitt 1, § 10)

Für Bauleistungen enthält die VOB/A Abschnitt 1 (anders als VOL/A) einen **festen Mindestwert
von 10 Kalendertagen** für die Angebotsfrist, im Übrigen ebenfalls den Angemessenheitsmaßstab.

| Wertbereich | Verfahren | Mindestfrist | Verkürzung möglich (Tatbestand → Frist) | Fundstelle | Stand |
|---|---|---|---|---|---|
| Unterschwelle | Öffentliche Ausschreibung / Beschränkte Ausschreibung mit Teilnahmewettbewerb – Angebotsfrist | Ausreichende Angebotsfrist; auch bei Dringlichkeit nicht unter 10 Kalendertagen (§ 10 Abs. 1 VOB/A) | Entfällt (bereits gesetzlicher Mindestwert; auch bei Dringlichkeit keine Unterschreitung von 10 Kalendertagen zulässig) | § 10 Abs. 1 VOB/A (1. Abschnitt) i. V. m. § 2 SächsVergabeG: https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_31012019_BWI781063060120180001604634.htm ; https://www.revosax.sachsen.de/vorschrift/12749-Saechsisches-Vergabegesetz | 25.09.2023 (letzte Änderungsbekanntmachung VOB/A Abschnitt 1) / 01.07.2026 geprüft |
| Unterschwelle | Beschränkte Ausschreibung mit Teilnahmewettbewerb – Bewerbungsfrist | Keine feste Tageszahl; „ausreichende Bewerbungsfrist" (§ 10 Abs. 3 VOB/A) | Nicht einschlägig (Angemessenheitsmaßstab, kein Fristenkatalog) | § 10 Abs. 3 VOB/A (1. Abschnitt): https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_31012019_BWI781063060120180001604634.htm | 25.09.2023 / 01.07.2026 geprüft |
| Unterschwelle | Freihändige Vergabe – Angebotsfrist | § 10 Abs. 1 VOB/A gilt entsprechend (§ 10 Abs. 6): ausreichende Frist, auch bei Dringlichkeit nicht unter 10 Kalendertagen | Entfällt (wie Öffentliche Ausschreibung) | § 10 Abs. 1, 6 VOB/A (1. Abschnitt): https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_31012019_BWI781063060120180001604634.htm | 25.09.2023 / 01.07.2026 geprüft |

## Hinweise zur Tabelle

- **Vergabebeschleunigungsgesetz — explizites Ergebnis für Fristen.** Das zum 01.07.2026 in
  Kraft getretene Vergabebeschleunigungsgesetz (BGBl. 2026 I Nr. 137) ändert die
  Mindestfristen der §§ 15–20 VgV **nicht**. Die oben genannten Tageszahlen (35/30/15/10 Tage
  je nach Verfahren und Tatbestand) entsprechen exakt der bereits vor dem 01.07.2026 geltenden
  Fassung; ein Alt-/Neu-Vergleich ergibt daher **keine Änderung**. Auch VOB/A (Abschnitt 1 und
  2) ist nicht betroffen, da deren Fristenparagraphen (§ 10, §§ 10a–10d EU) über eine
  eigenständige Verwaltungsvorschrift des zuständigen Bundesministeriums geändert werden,
  nicht über das (nur GWB/VgV/BHO/weitere Bundesgesetze ändernde) Vergabebeschleunigungsgesetz.
  Die tatsächlichen Schwerpunkte des Gesetzes liegen bei Losgrundsatz (§ 97a GWB, neu),
  Wertgrenzen (§ 55 BHO), Eignungsnachweisen (Eigenerklärungen), digitaler Souveränität als
  Zuschlagskriterium (§ 58 VgV) und beschleunigtem Rechtsschutz (Wegfall der aufschiebenden
  Wirkung der sofortigen Beschwerde) — siehe `rechtsquellen.md` und `verfahrensarten.md`.
- **VgV vs. VOB/A-EU: unterschiedliche Verkürzungstatbestände.** Anders als § 10a/10b EU VOB/A
  kennt die VgV **keine Vorinformations-basierte Verkürzung** der Angebots- oder Teilnahmefrist
  bei offenem und nicht offenem Verfahren (§§ 15, 16 VgV enthalten hierzu keinen Absatz); dort
  existieren nur die Verkürzungstatbestände Dringlichkeit und elektronische Übermittlung. Bei
  Bauleistungen (VOB/A-EU) ist die Vorinformations-Verkürzung dagegen ausdrücklich geregelt.
  Diese Abweichung wurde durch mehrfachen Abgleich der Absatzzahlen gegen die Primärquelle
  bestätigt und ist kein Recherchefehler.
- **Elektronische Verkürzung wirkt nicht kumulativ mit der Dringlichkeitsfrist.** In §§ 15–17
  VgV verweist die Verkürzungsregel für die elektronische Übermittlung ausdrücklich auf die
  „Frist gemäß Absatz 2" bzw. „Absatz 5" (die reguläre Grundfrist), nicht auf die
  Dringlichkeitsfrist. Die beiden Verkürzungswege (Dringlichkeit einerseits, elektronische
  Übermittlung andererseits) sind daher **zwei getrennte Fristzweige** und nicht addierbar
  (z. B. offenes Verfahren: entweder 35 → 30 Tage bei elektronischer Übermittlung **oder**
  35 → 15 Tage bei Dringlichkeit, nicht 35 → 10 Tage kumuliert).
- **Unterschwelle: Angemessenheit statt Tagesfrist.** Für Liefer-/Dienstleistungen gilt in
  Sachsen (VOL/A, kein UVgO-Land) ausschließlich der Angemessenheitsmaßstab des § 10 Abs. 1
  VOL/A ohne bezifferte Mindesttage. Für Bauleistungen schreibt § 10 Abs. 1 VOB/A (1.
  Abschnitt) demgegenüber einen festen Mindestwert von 10 Kalendertagen für die Angebotsfrist
  vor (auch bei Dringlichkeit nicht unterschreitbar) — dies ist die einzige feste,
  bezifferte Unterschwellen-Mindestfrist in dieser Tabelle. Ein eigener sächsischer
  Fristen-Erlass (analog zu den Wertgrenzen-Diskussionen in `wertgrenzen-sachsen.md`) konnte
  nicht ermittelt werden.
- **Nicht Gegenstand dieser Tabelle:** Bindefrist (Dauer der Angebotsgültigkeit nach
  Fristablauf, § 10 Abs. 4–5 VOB/A bzw. entsprechend VgV/VOB/A-EU) sowie die vergaberechtliche
  Warte-/Stillhaltefrist vor Zuschlagserteilung nach § 134 GWB (Oberschwelle) — beide sind
  eigene Fristinstitute außerhalb der Angebots-/Teilnahmefrist und bei Bedarf gesondert zu
  dokumentieren.
- **Primärquellen / Prüfung:** VgV über gesetze-im-internet.de (§§ 15–20, Absatz für Absatz
  einzeln abgerufen); VOB/A Abschnitt 1 und 2 über verwaltungsvorschriften-im-internet.de;
  VOL/A (Ausgabe 2009) über vergabevorschriften.de; SächsVergabeG über revosax.sachsen.de.
  Zur Verifikation der Aussage „keine Fristenänderung durch das Vergabebeschleunigungsgesetz"
  wurden zusätzlich mehrere unabhängige Fachbeiträge ausgewertet (u. a. cosinex-Blog,
  Gleiss Lutz, KPMG Law, Oppenhoff, vergabepilot.ai) — keiner nennt eine Änderung der
  §§ 15–20 VgV. Alle Angaben wurden am **01.07.2026** gegen die genannten Primärquellen
  geprüft. Die mit „(zu prüfen)" gekennzeichneten Punkte (Dringlichkeits-Verkürzung der
  Teilnahmefrist bei wettbewerblichem Dialog/Innovationspartnerschaft nach VOB/A-EU; Praxis-
  Konvention zur Orientierung an EU-Fristen im VOL/A-Bereich) sind vor verbindlicher Nutzung
  gesondert zu verifizieren.
