# Baustein 08 – Testdokumentation 🔴

> **Schwierigkeit:** 🔴 Transfer  
> **Zeitrahmen:** ca. 150 Minuten  
> **Voraussetzung:** Alle vorherigen Bausteine  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/BQurE7rxAq" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 08: Testdokumentation</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich kenne Testpläne und Testberichte
- [ x ] 🟡 Ich habe davon gehört, aber noch nie selbst erstellt
- [ ] 🔴 Das ist mir komplett neu

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … erklären, wozu Testdokumentation dient
- 🟡 … einen Testplan nach Vorlage erstellen
- 🟡 … Testfälle vollständig und formal dokumentieren
- 🔴 … einen Testbericht mit Ergebnissen für einen Auftraggeber erstellen
- 🔴 … Qualitätskennzahlen (Testabdeckung, Fehlerquote) ermitteln und interpretieren

---

## Hintergrund

Im Berufsalltag reicht es nicht, Tests zu schreiben – du musst auch nachweisen,
dass du getestet hast und was dabei herausgekommen ist.

**Testdokumentation dient dazu:**

- Nachvollziehbarkeit: Wer hat was wann getestet?
- Qualitätsnachweis gegenüber Auftraggeber / Kunden
- Grundlage für Abnahmeentscheidungen
- Rückverfolgbarkeit: Welche Anforderung wird durch welchen Test abgedeckt?
- Wissensweitergabe im Team

**Wichtige Dokumente:**

- **Testplan**: Was wird wie getestet? (vor dem Testen)
- **Testfallspezifikation**: Genaue Definition einzelner Tests
- **Testbericht**: Was wurde gefunden? (nach dem Testen)

---

## Aufgabe 0 – Grundbegriffe: Testdokumentation einordnen 🟢

**Einstieg ohne Code:**

**a)** Ordne die folgenden Aussagen dem richtigen Dokument zu
(Testplan / Testprotokoll / Testbericht):

| Aussage                                                    | Dokument |
| ---------------------------------------------------------- | -------- |
| „Wir werden alle Module mit pytest testen."                |          |
| „TC-007 ist fehlgeschlagen: Bestand wurde auf -5 gesetzt." |          |
| „8 von 10 Tests bestanden, 1 Fehler offen."                |          |
| „Abnahmekriterium: Coverage > 80 %."                       |          |
| „Empfehlung: System ist abnahmebereit."                    |          |

**b)** Wann wird jedes Dokument erstellt? Ordne zu:

- Vor dem Testen
- Während des Testens
- Nach dem Testen

**c)** Erkläre in 2 Sätzen: Warum reicht es nicht aus, Tests einfach auszuführen –
ohne sie zu dokumentieren?

Trage deine Antworten in `08_antworten.md` ein.

---

## Aufgabe 1 – Testfall-Dokumentation 🟡

Ein Testfall braucht immer diese Bestandteile:

| Feld                   | Beschreibung                                    |
| ---------------------- | ----------------------------------------------- |
| TC-ID                  | Eindeutige Kennung (z. B. TC-AUTH-001)          |
| Titel                  | Kurze Beschreibung des Tests                    |
| Vorbedingung           | Was muss vor dem Test gelten?                   |
| Testeingabe            | Welche Daten werden verwendet?                  |
| Testschritte           | Was wird Schritt für Schritt getan?             |
| Erwartetes Ergebnis    | Was soll passieren?                             |
| Tatsächliches Ergebnis | Was ist tatsächlich passiert? (nach Ausführung) |
| Status                 | Bestanden / Fehlgeschlagen / Blockiert          |

**a)** Erstelle vollständige Testfalldokumentationen für die Funktion `authentifiziere_benutzer()`
aus Baustein 03. Mindestens 6 Testfälle.

Nutze die Vorlage in `code/starter.py` (als Python-Docstring oder Markdown-Tabelle).

**b)** Führe die Testfälle aus und trage "Tatsächliches Ergebnis" und "Status" ein.

---

## Aufgabe 2 – Testplan erstellen 🟡

Ein Testplan ist das übergeordnete Dokument, das beschreibt:

- Was soll getestet werden (Testumfang)?
- Wie soll getestet werden (Methoden, Werkzeuge)?
- Wer testet was (Verantwortlichkeiten)?
- Wann wird getestet (Zeitplan)?
- Was sind die Abnahmekriterien?

**Szenario:** Du bist Fachinformatiker/in in einem Betrieb.
Ihr habt eine **Lagerbestandsverwaltung** in Python entwickelt (ca. 200 Zeilen Code,
3 Module: `artikel.py`, `lager.py`, `bericht.py`).

Erstelle einen Testplan (in `08_testplan.md`) mit:

- Projektname, Datum, Autor
- Testumfang (was wird getestet, was nicht)
- Teststufen (welche Tests auf welcher Stufe)
- Testmethoden (Black-Box, White-Box, Äquivalenzklassen...)
- Werkzeuge (pytest, Coverage...)
- Zeitplan (wann wird welche Teststufe durchgeführt)
- Abnahmekriterien (z. B. "alle Tests grün", "Coverage > 80 %")

---

## Aufgabe 3 – Coverage-Bericht interpretieren 🔴

In `code/starter.py` findest du ein Modul `lager.py` mit einer `Lager`-Klasse
und eine Test-Suite dafür.

**a)** Installiere pytest-cov und führe den Coverage-Bericht aus:

```bash
pip install pytest-cov
pytest 08_dokumentation/code/starter.py --cov=08_dokumentation/code/starter --cov-report=term-missing -v
```

**b)** Interpretiere den Bericht:

- Welche Zeilen werden nicht getestet ("missing")?
- Welche Zweige fehlen?
- Wie hoch ist die aktuelle Coverage?

**c)** Schreibe zusätzliche Tests, um die Coverage auf mindestens 90 % zu bringen.

**d)** Ist 100 % Coverage ein Qualitätsgarant? Begründe.

---

## Aufgabe 4 – Testbericht erstellen 🔴

Nach dem Abschluss der Tests für die Lagerbestandsverwaltung (Aufgabe 2)
erwartet der Auftraggeber einen formalen Testbericht.

Erstelle `08_testbericht.md` mit:

- Zusammenfassung: Was wurde getestet? Mit welchem Ergebnis?
- Testumgebung: Python-Version, Betriebssystem, pytest-Version
- Testergebnisse: Tabelle mit allen Testfällen und Status
- Gefundene Fehler: Fehlerbeschreibung, Schweregrad, Status (offen/behoben)
- Coverage-Statistik: Tabelle pro Modul
- Bewertung: Ist das System abnahmebereit?
- Offene Punkte: Was bleibt zu tun?

Verwende als Grundlage die Ergebnisse aus Aufgaben 1–3.

---

## Aufgabe 5 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Entwicklungsteam hat folgende pytest-Ausgabe erhalten:

```
PASSED  test_artikel_anlegen                       [ 10%]
PASSED  test_bestand_erhoehen                      [ 20%]
FAILED  test_bestand_reduzieren_unter_null         [ 30%]
PASSED  test_artikel_suchen_vorhanden              [ 40%]
FAILED  test_artikel_suchen_nicht_vorhanden        [ 50%]
PASSED  test_lager_kapazitaet_pruefen              [ 60%]
ERROR   test_bericht_erstellen                     [ 70%]
PASSED  test_bestand_exportieren                   [ 80%]
PASSED  test_import_aus_csv                        [ 90%]
PASSED  test_loeschen_vorhandener_artikel          [100%]

8 passed, 2 failed, 1 error in 0.43s
```

**(a)** Berechnen Sie die Erfolgsquote der Tests in Prozent. _(1 Punkt)_

**(b)** Unterscheiden Sie "FAILED" und "ERROR" in pytest. Was bedeutet jeweils dieser Status? _(4 Punkte)_

**(c)** Erstellen Sie einen kurzen Testbericht (Tabellenformat), der diese Ergebnisse für den Auftraggeber aufbereitet. Bewerten Sie, ob das System abnahmebereit ist. _(6 Punkte)_

**(d)** Welche Maßnahmen würden Sie vor einer erneuten Abnahme empfehlen? _(4 Punkte)_

---

## Tandem-Aufgabe 👥

**Gegenseitiger Testbericht-Review:**

Person A erstellt einen Testplan und Testbericht für ihre Lösung aus Baustein 07 (TDD).
Person B erstellt dasselbe für ihre Lösung aus Baustein 06 (pytest).

Dann tauscht ihr und reviewed gegenseitig:

- Sind alle Pflichtbestandteile vorhanden?
- Ist der Bericht für jemanden verständlich, der den Code nicht kennt?
- Würde der Auftraggeber die Abnahme erteilen?

Haltet Feedback schriftlich fest.

**Erkläre deinem Tandempartner:** Erkläre den Unterschied zwischen Testplan, Testprotokoll und Testbericht – und warum alle drei Dokumente für einen Auftraggeber wichtig sind. Dein Tandempartner prüft, ob alle wesentlichen Punkte korrekt erklärt wurden.

---

## Active Recall 🧠

_Unterlagen zu:_

1. Was ist der Unterschied zwischen Testplan und Testbericht?
2. Was sind typische Abnahmekriterien für Software?
3. Was bedeutet "Testabdeckung" (Coverage) und was misst sie nicht?
4. Wann ist ein Testbericht "gut genug" für einen Kunden?
5. Was ist der Unterschied zwischen FAILED und ERROR in pytest?

---

## Reflexion 🚦

- [ x ] 🟢 Ich kann professionelle Testdokumentation erstellen
- [ ] 🟡 Ich verstehe das Konzept, die Umsetzung braucht noch Übung
- [ ] 🔴 Ich brauche weitere Erklärungen oder Beispiele

**Was war in dieser gesamten Lernsequenz das Wichtigste für dich?**

> ---

**Was nimmst du konkret in deinen Betriebsalltag mit?**

> ---

---

_Bei Problemen → [Stuck Protocol](../stuck_protocol.md)_
