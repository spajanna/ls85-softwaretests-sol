## Aufgabe 0

### a) Zuordnung

* „Wir werden alle Module mit pytest testen.“ → **Testplan**
* „TC-007 ist fehlgeschlagen: Bestand wurde auf -5 gesetzt.“ → **Testprotokoll**
* „8 von 10 Tests bestanden, 1 Fehler offen.“ → **Testbericht**
* „Abnahmekriterium: Coverage > 80 %.“ → **Testplan**
* „Empfehlung: System ist abnahmebereit.“ → **Testbericht**

---

### b) Zeitpunkt

* Testplan → **vor dem Testen**
* Testprotokoll → **während des Testens**
* Testbericht → **nach dem Testen**

---

### c) Warum Dokumentation nötig ist

Ohne Dokumentation ist nicht nachvollziehbar, was genau getestet wurde und wie die Ergebnisse entstanden sind. Außerdem fehlen Belege für Qualität und Entscheidungen zur Abnahme.

---

## Aufgabe 5 – IHK

### a) Erfolgsquote

8 + 2 + 1 = 11 Tests
8 bestanden

→ 8 / 11 = **72,7 %**

---

### b) FAILED vs ERROR

* **FAILED:** Test lief vollständig, aber Erwartung wurde verletzt
* **ERROR:** Test wurde durch Exception oder technischen Fehler abgebrochen

---

### c) Testbericht

| Status | Anzahl |
| ------ | ------ |
| Passed | 8      |
| Failed | 2      |
| Error  | 1      |

**Bewertung:** Nicht abnahmebereit (zu viele Fehler, kritische Tests betroffen)

---

### d) Maßnahmen

* Fehleranalyse der FAILED Tests
* Ursache des ERROR beheben (Code-Defekt oder Setup)
* Regressionstests erweitern
* erneuter vollständiger Testlauf
* ggf. Refactoring der betroffenen Module

---

#08_testplan.md

## Projekt

Lagerbestandsverwaltung

## Datum

29.06.2026

## Autor

(Dein Name)

---

## Testumfang

* artikel.py: Artikelverwaltung
* lager.py: Bestandslogik
* bericht.py: Auswertung

Nicht getestet:

* externe APIs
* UI/Frontend (falls vorhanden)

---

## Teststufen

* Unit Tests (pytest)
* Integrationstests (Modulzusammenspiel)
* Systemtests (Gesamtablauf)

---

## Testmethoden

* Black-Box Testing
* White-Box Testing
* Äquivalenzklassenanalyse
* Grenzwertanalyse

---

## Werkzeuge

* Python 3.x
* pytest
* pytest-cov

---

## Zeitplan

* Tag 1: Unit Tests
* Tag 2: Integrationstests
* Tag 3: Coverage-Analyse & Nachtests
* Tag 4: Abschlussbericht

---

## Abnahmekriterien

* alle Tests bestanden
* keine kritischen Fehler offen
* Coverage ≥ 80 %
* keine offenen Blocker

---

# IHK-Kernverständnis (kurz)

* **Testplan:** was/wie geplant wird
* **Testprotokoll:** laufende Ergebnisse
* **Testbericht:** Gesamtbewertung für den Kunden

---