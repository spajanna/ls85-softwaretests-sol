# Testplan – Lagerbestandsverwaltung

## 1. Allgemeine Informationen

**Projektname:** Lagerbestandsverwaltung  
**Datum:** 30.06.2026  
**Autor:** [Name]

## 2. Testumfang

Getestet werden die Module `artikel.py`, `lager.py` und `bericht.py`.

Getestet werden:

- Artikel anlegen, suchen und verwalten
- Bestand erhöhen und reduzieren
- Fehlerfälle wie negative Mengen, negative Preise oder doppelte Artikel
- Berechnung des Lagergesamtwerts
- Berichte zu Lagerbestand und Mindestbestand

Nicht getestet werden:

- Benutzeroberfläche
- Datenbankanbindung
- Netzwerkfunktionen
- Performance bei sehr großen Datenmengen

## 3. Teststufen

### Unit-Tests

Einzelne Funktionen und Klassen werden isoliert getestet.

Beispiele:

- Artikel wird korrekt erstellt
- Bestand wird korrekt erhöht oder reduziert
- Ungültige Eingaben werfen Fehler

### Integrationstests

Das Zusammenspiel der Module wird getestet.

Beispiele:

- `lager.py` verwendet Artikel aus `artikel.py`
- `bericht.py` erstellt Berichte aus Lagerdaten

### Systemtest

Die gesamte Lagerbestandsverwaltung wird getestet.

Beispiel:

- Artikel anlegen, Bestand ändern, Gesamtwert berechnen und Bericht erzeugen

### Abnahmetest

Der Fachbereich prüft, ob die Software die Anforderungen erfüllt.

Beispiel:

- Ein realistischer Lagerprozess wird vollständig durchgeführt

## 4. Testmethoden

Verwendete Testmethoden:

- Black-Box-Tests
- White-Box-Tests
- Äquivalenzklassen
- Grenzwertanalyse
- Regressionstests nach Änderungen

## 5. Werkzeuge

Verwendete Werkzeuge:

- `pytest`
- `pytest -v`
- `coverage`
- Git

## 6. Zeitplan

- Tag 1: Unit-Tests für `artikel.py`
- Tag 2: Unit-Tests für `lager.py`
- Tag 3: Integrationstests mit `artikel.py`, `lager.py` und `bericht.py`
- Tag 4: Systemtest und Fehlerkorrektur
- Tag 5: Regressionstest und Abnahmetest

## 7. Abnahmekriterien

Die Software ist abnahmebereit, wenn:

- alle automatisierten Tests grün sind
- keine kritischen Fehler offen sind
- die Testabdeckung mindestens 80 % beträgt
- ungültige Eingaben korrekt abgefangen werden
- Lagerwerte und Berichte korrekt berechnet werden
- der Fachbereich den Abnahmetest akzeptiert

## 8. Risiken

Mögliche Risiken:

- Fehler bei Grenzwerten, z. B. Bestand 0 oder Kapazitätsgrenze
- falsche Berechnung des Gesamtwerts
- fehlende Validierung ungültiger Eingaben
- unvollständige Testabdeckung

## 9. Ergebnisdokumentation

Während des Testens werden Ergebnisse und Fehler im Testprotokoll dokumentiert.  
Nach Abschluss wird ein Testbericht erstellt, der zusammenfasst, wie viele Tests bestanden wurden, welche Fehler offen sind und ob das System abnahmebereit ist.