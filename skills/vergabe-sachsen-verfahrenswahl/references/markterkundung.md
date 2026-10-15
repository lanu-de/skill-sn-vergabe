# Markterkundung — Rechtsrahmen, Ablauf und Fehlerquellen

> Teil der geteilten Referenzdaten (`shared/`). **Nicht direkt in Skills bearbeiten** –
> Änderungen ausschließlich hier in `shared/references/markterkundung.md` vornehmen und
> anschließend mit `python scripts/sync_shared.py sync` in alle Skills übernehmen.

Eine **Markterkundung** ist die unverbindliche Erkundung des Anbietermarkts **vor** einem
Vergabeverfahren. Sie klärt, was der Markt anbietet, was es ungefähr kostet und wie sich
der eigene Bedarf marktgerecht beschreiben lässt. Sie ist **selbst kein Vergabeverfahren**:
Es werden keine Angebote eingeholt, nicht gewertet und kein Auftrag erteilt.

Typische Ziele (eines oder mehrere):

- Bedarf schärfen und **Leistungsbeschreibung** marktgerecht vorbereiten,
- **Auftragswert** belastbar schätzen (Grundlage für Ober-/Unterschwelle und Verfahrenswahl),
- **Lose** und Varianten erkennen (z. B. Kauf oder Miete, eigener Betrieb oder Dienstleistung),
- prüfen, ob es **überhaupt mehrere Anbieter** gibt (Voraussetzung für die Begründung von
  Ausnahmeverfahren wegen Alleinstellung),
- Unternehmen **frühzeitig über das Vorhaben informieren**.

Begriffe, die in der Praxis gleichbedeutend verwendet werden: Marktsondierung,
Marktkonsultation, Markterkundung, Marktabfrage, im IT-Bereich auch „RFI“ (Request for
Information). Abzugrenzen ist die **Preisumfrage/Angebotseinholung bei der Freihändigen
Vergabe**: Sie ist bereits Teil des Vergabeverfahrens, die Markterkundung liegt davor.

## Rechtsgrundlagen

In Sachsen gilt unterschwellig für Liefer-/Dienstleistungen die **VOL/A (Ausgabe 2009)**,
für Bauleistungen die **VOB/A Abschnitt 1**, nicht die UVgO (siehe `sachsen-spezifika.md`).
Das SächsVergabeG selbst enthält keine Regelung zur Markterkundung.

| Thema | Regelung | Fundstelle | Stand |
|---|---|---|---|
| Zulässigkeit (Oberschwelle) | Vor Einleitung eines Vergabeverfahrens darf der Auftraggeber Markterkundungen zur Vorbereitung der Vergabe und zur Unterrichtung der Unternehmen über seine Pläne durchführen; sie kann auch soziale, umweltbezogene, Qualitäts- und Innovationsaspekte umfassen und elektronisch erfolgen | § 28 Abs. 1 VgV: https://www.gesetze-im-internet.de/vgv_2016/__28.html | 15.10.2026 geprüft |
| Zulässigkeit (Unterschwelle) | VOL/A und VOB/A Abschnitt 1 enthalten **keine ausdrückliche Erlaubnisnorm**; die Zulässigkeit einer Markterkundung als Vorbereitungshandlung ergibt sich mittelbar aus dem Verbot reiner Erkundungsverfahren (nächste Zeile) **(Auslegung)** | § 2 Abs. 3 VOL/A: https://www.vergabevorschriften.de/vol-a/2 ; § 2 Abs. 5 VOB/A: https://www.vergabevorschriften.de/vob-a/2 | 15.10.2026 geprüft |
| Verbot der Scheinausschreibung | Ein Vergabeverfahren **nur** zur Markterkundung bzw. Kosten-/Preisermittlung durchzuführen, ist unzulässig. Oberschwellig: „lediglich zur Markterkundung und zum Zwecke der Kosten- oder Preisermittlung“; VOL/A: „lediglich zur Markterkundung und zum Zwecke von Ertragsberechnungen“; VOB/A Abschnitt 1: „zum Zwecke der Markterkundung“ | § 28 Abs. 2 VgV: https://www.gesetze-im-internet.de/vgv_2016/__28.html ; § 2 Abs. 3 VOL/A: https://www.vergabevorschriften.de/vol-a/2 ; § 2 Abs. 5 VOB/A: https://www.vergabevorschriften.de/vob-a/2 | 15.10.2026 geprüft |
| Gleichbehandlung, Transparenz, Wettbewerb | Kein Unternehmen darf diskriminiert werden; gilt auch für die Auswahl der angefragten Unternehmen und für die Weitergabe von Informationen | § 97 Abs. 1–2 GWB: https://www.gesetze-im-internet.de/gwb/__97.html ; § 2 Abs. 1 VOL/A: https://www.vergabevorschriften.de/vol-a/2 ; § 2 VOB/A: https://www.vergabevorschriften.de/vob-a/2 | 15.10.2026 geprüft |
| Vorbefasste Unternehmen (Projektanten), Oberschwelle | Hat ein Unternehmen den Auftraggeber beraten oder war es sonst an der Vorbereitung beteiligt, muss der Auftraggeber angemessene Maßnahmen gegen Wettbewerbsverzerrung ergreifen, insbesondere die anderen Teilnehmer über die ausgetauschten Informationen unterrichten und angemessene Fristen setzen. Ausschluss nur, wenn die Verzerrung nicht durch mildere Maßnahmen zu beseitigen ist, und erst nach Gelegenheit zur Stellungnahme | § 7 VgV: https://www.gesetze-im-internet.de/vgv_2016/__7.html ; § 124 Abs. 1 Nr. 6 GWB: https://www.gesetze-im-internet.de/gwb/__124.html | 15.10.2026 geprüft |
| Vorbefasste Unternehmen, Unterschwelle Liefer-/Dienstleistungen | Hat ein Bewerber oder Bieter den Auftraggeber vor Einleitung des Verfahrens beraten oder sonst unterstützt, muss der Auftraggeber sicherstellen, dass der Wettbewerb durch dessen Teilnahme nicht verfälscht wird | § 6 Abs. 6 VOL/A: https://www.vergabevorschriften.de/vol-a/6 | 15.10.2026 geprüft |
| Vorbefasste Unternehmen, Unterschwelle Bau | VOB/A Abschnitt 1 enthält **keine ausdrückliche Projektantenregel**; die Pflicht, Wettbewerbsverzerrungen zu vermeiden, folgt aus den Grundsätzen des § 2 VOB/A **(zu prüfen)** | § 2 VOB/A: https://www.vergabevorschriften.de/vob-a/2 | 15.10.2026 geprüft |
| Vertraulichkeit | Als vertraulich gekennzeichnete Informationen der Unternehmen (insbesondere Betriebs- und Geschäftsgeheimnisse) dürfen nicht weitergegeben werden; der Auftraggeber kann eine Verschwiegenheitserklärung verlangen. VOB/A Abschnitt 1: Vertraulichkeit aller Informationen und Unterlagen. VOL/A: keine ausdrückliche allgemeine Norm, Schutz folgt aus Wettbewerbs- und Gleichbehandlungsgrundsatz **(Auslegung)** | § 5 Abs. 1 und 3 VgV: https://www.gesetze-im-internet.de/vgv_2016/__5.html ; § 2 Abs. 4 VOB/A: https://www.vergabevorschriften.de/vob-a/2 ; § 2 Abs. 1 VOL/A: https://www.vergabevorschriften.de/vol-a/2 | 15.10.2026 geprüft |
| Schätzung des Auftragswerts | Maßgeblich ist der voraussichtliche Gesamtwert ohne Umsatzsteuer einschließlich Optionen und Vertragsverlängerungen; die Markterkundung liefert hierfür die Datengrundlage | § 3 Abs. 1 VgV: https://www.gesetze-im-internet.de/vgv_2016/__3.html | 15.10.2026 geprüft |
| Dokumentation | Das Verfahren ist von Beginn an fortlaufend in Textform zu dokumentieren, ausdrücklich einschließlich der **Kommunikation mit Unternehmen** und der Vorbereitung der Vergabeunterlagen. Unterschwellig: Dokumentation „von Anbeginn fortlaufend“, sodass Stufen, Maßnahmen und Begründungen festgehalten werden | § 8 Abs. 1 VgV: https://www.gesetze-im-internet.de/vgv_2016/__8.html ; § 20 VOL/A: https://www.vergabevorschriften.de/vol-a/20 ; § 20 VOB/A: https://www.vergabevorschriften.de/vob-a/20 | 15.10.2026 geprüft |
| Alleinstellung (nur ein Anbieter) | Ein Verhandlungsverfahren ohne Teilnahmewettbewerb aus technischen Gründen oder wegen Schutzrechten setzt voraus, dass es **keine vernünftige Alternative oder Ersatzlösung** gibt und der fehlende Wettbewerb nicht auf einer künstlichen Einschränkung beruht. Das lässt sich praktisch nur mit einer dokumentierten Markterkundung belegen | § 14 Abs. 4 Nr. 2 Buchst. b und c, Abs. 6 VgV: https://www.gesetze-im-internet.de/vgv_2016/__14.html | 15.10.2026 geprüft |
| Produktneutralität (Folgen für die Leistungsbeschreibung) | Produkt-, Marken- oder Herstellernamen aus den Antworten der Unternehmen dürfen nicht ungeprüft in die Leistungsbeschreibung übernommen werden; Verweise auf bestimmte Erzeugnisse nur, wenn durch den Auftragsgegenstand gerechtfertigt bzw. eine genaue Beschreibung sonst nicht möglich ist, und dann grundsätzlich mit dem Zusatz „oder gleichwertig“ | § 31 Abs. 6 VgV: https://www.gesetze-im-internet.de/vgv_2016/__31.html ; § 7 Abs. 3–4 VOL/A: https://www.vergabevorschriften.de/vol-a/7 ; § 7 Abs. 2 VOB/A: https://www.vergabevorschriften.de/vob-a/7 | 15.10.2026 geprüft |
| Haushaltsrecht | Wirtschaftlichkeit und Sparsamkeit; die Markterkundung sollte erst beginnen, wenn geklärt ist, ob und in welchem Umfang Haushaltsmittel zur Verfügung stehen | § 7 SäHO: https://www.revosax.sachsen.de/vorschrift/4270-Saechsische-Haushaltsordnung | 15.10.2026 geprüft |

## Ablauf in fünf Schritten

1. **Vorbereiten.** Ziel festlegen (was soll die Markterkundung klären?), Bedarf und
   Rahmenbedingungen intern abstimmen (Fachbereich, Haushalt, ggf. IT-Sicherheit,
   Datenschutz, Personalvertretung), Budgetrahmen klären, Zeitplan und Antwortfrist
   festlegen, Dokumentation anlegen.
2. **Unternehmen auswählen.** Mehrere Unternehmen ansprechen, nicht nur bekannte oder
   bisherige Auftragnehmer; kleine und mittlere Unternehmen einbeziehen. Bei EU-weitem Markt
   auch über Sachsen bzw. Deutschland hinaus recherchieren. Quellen und Auswahlkriterien
   festhalten. Alternativ oder ergänzend: öffentliche Bekanntmachung der Markterkundung, damit
   sich jedes interessierte Unternehmen melden kann.
3. **Anfragen.** Allen Unternehmen **dieselben Unterlagen, dieselben Fragen und dieselbe
   Frist** geben. Im Anschreiben klarstellen: keine Ausschreibung, keine verbindlichen
   Angebote, keine Ansprüche. Rückfragen einzelner Unternehmen beantworten, und zwar
   gegenüber allen in gleicher Weise, sofern die Antwort für alle von Bedeutung ist.
   Vorlage: `assets/markterkundung-anschreiben-vorlage.md` (Skill
   `vergabe-sachsen-markterkundung`).
4. **Auswerten.** Antworten in einer Gegenüberstellung vergleichbar machen (Leistung,
   Varianten, Preisspannen mit den jeweiligen Annahmen, Risiken). Unklare Antworten
   schriftlich nachfragen. Gespräche oder Produktvorführungen nur einheitlich (gleiche
   Agenda, gleiche Dauer, Protokoll).
5. **Ergebnis festhalten und überführen.** Erkenntnisse und Schlussfolgerungen dokumentieren:
   Auftragswert, Ober-/Unterschwelle, Verfahrensart, Lose, Inhalte der Leistungsbeschreibung,
   ggf. Verzicht auf die Beschaffung. Vorlage: `assets/markterkundung-vermerk-vorlage.md`
   (Skill `vergabe-sachsen-markterkundung`); der Vermerk wird Teil der Vergabeakte.

## Kontakt mit Unternehmen: Was ist unbedenklich, was nicht?

Je enger ein einzelnes Unternehmen an der Vorbereitung mitwirkt, desto eher wird es zum
**vorbefassten Unternehmen** (siehe Tabelle oben) und desto mehr Ausgleichsmaßnahmen sind im
späteren Verfahren nötig.

| Unbedenklich | Nur mit Vorkehrungen | Unterlassen |
|---|---|---|
| Fragen nach Standardleistungen, Produktkategorien, Liefer- und Bereitstellungszeiten, Preismodellen und groben Preisspannen | Gespräche, Präsentationen, Produktvorführungen — nur mit einheitlicher Agenda und Dauer für alle, Protokoll, wesentliche Klarstellungen an alle | Ein Unternehmen Leistungsbeschreibung, Bewertungsmatrix oder Vertragsentwurf (mit-)formulieren oder kommentieren lassen |
| Bitte um öffentlich verfügbare Unterlagen (Produktblätter, Referenzlisten) | Vertiefende technische Fragen an einzelne Unternehmen — nur, wenn die Antwort keinen Wissensvorsprung verschafft oder allen zugänglich gemacht wird | Interne Entwürfe oder Vergabeunterlagen an einzelne Unternehmen geben |
| Einheitlicher Fragebogen mit gleicher Frist für alle | Nachfragen zu einzelnen Antworten — schriftlich und dokumentiert | Verbindliche Angebote, Preiszusagen oder Verhandlungen über Preise |
| Hinweis auf das geplante Verfahren und den Zeitplan | Antworten in Präsentationsform statt schriftlich — nur ergänzend | Aussicht auf den Auftrag stellen oder den Eindruck einer Vorauswahl erwecken |

## Häufige Fehler

1. **Die Anfrage sieht aus wie eine Ausschreibung.** Formulierungen wie „Angebot“,
   „Zuschlag“ oder „Bindefrist“ im Anschreiben, Bitte um verbindliche Preise. → Ausdrücklich
   als unverbindliche Markterkundung bezeichnen, nur Preisspannen mit Annahmen erfragen.
2. **Die Antworten werden als Angebote verwendet.** Auf eine Antwort aus der Markterkundung
   kann kein Auftrag erteilt werden. → Bei der anschließenden Freihändigen Vergabe oder
   Ausschreibung die Angebote im Verfahren gesondert anfordern.
3. **Nur die „üblichen“ Anbieter werden gefragt.** Bisheriger Auftragnehmer plus zwei
   Bekannte ergibt kein Marktbild. → Breiter recherchieren, Auswahl begründen und festhalten.
4. **Ungleiche Behandlung.** Ein Unternehmen bekommt ein ausführliches Gespräch, die anderen
   nur eine E-Mail; unterschiedliche Fristen oder Unterlagen. → Einheitliches Vorgehen;
   Abweichungen nur aus sachlichem Grund und mit Begründung in der Akte.
5. **Ein Unternehmen schreibt mit.** Formulierungsvorschläge oder „Musterpflichtenhefte“
   eines Anbieters fließen in die Leistungsbeschreibung ein. → Das Unternehmen wird
   vorbefasst; Wissensausgleich und längere Fristen werden nötig, im Extremfall der
   Ausschluss.
6. **Produktnamen wandern in die Leistungsbeschreibung.** → Anforderungen funktional und
   produktneutral formulieren (siehe Tabelle „Produktneutralität“).
7. **Vertrauliches wird weitergegeben.** Preise oder Lösungsdetails eines Unternehmens
   tauchen in Fragen an andere auf. → Ergebnisse nur zusammengefasst und ohne Zuordnung
   verwenden, Zugriff intern beschränken.
8. **Keine Dokumentation.** Die Markterkundung findet „nebenbei“ per Telefon statt. → Von
   Anfang an festhalten: Ziel, Auswahl, Unterlagen, Kommunikation, Antworten, Auswertung,
   Schlussfolgerungen.
9. **Veraltete Ergebnisse.** Eine Markterkundung von vor zwei Jahren dient als Grundlage. →
   Prüfen, ob sich Preise, Technik oder Anbieterlandschaft geändert haben; ggf. kurz
   aktualisieren und das festhalten.
10. **Alleinstellung wird behauptet, nicht belegt.** „Das kann nur Firma X“ ohne Prüfung
    des Marktes. → Für ein Ausnahmeverfahren ohne Wettbewerb ist eine nachvollziehbare
    Markterkundung erforderlich, die das Fehlen von Alternativen zeigt.
11. **Preisangaben werden nicht vergleichbar gemacht.** Ein Anbieter nennt Jahrespreise,
    einer Preise je Nutzer, einer einen Festpreis. → Einheitliche Annahmen vorgeben (Mengen,
    Laufzeit) und die Spannen auf eine gemeinsame Basis umrechnen.

## Abgrenzung zu anderen Referenzdateien

- Schätzung des Auftragswerts und Schwellenwerte: `schwellenwerte-eu.md`
- Wertgrenzen der Verfahrensarten unterschwellig: `wertgrenzen-sachsen.md`
- Verfahrensarten und Ausnahmetatbestände: `verfahrensarten.md`
- Normenübersicht: `rechtsquellen.md`
