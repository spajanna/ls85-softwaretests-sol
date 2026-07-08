# Baustein 06 – pytest 🔴

> **Schwierigkeit:** 🔴 Transfer  
> **Zeitrahmen:** ca. 150 Minuten  
> **Voraussetzung:** Baustein 05 (unittest) abgeschlossen  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/kZUchAUVA9" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 06: pytest</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich kenne pytest und habe damit gearbeitet
- [ ] 🟡 Ich habe von pytest gehört
- [ ] 🔴 Das ist Neuland für mich

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … pytest installieren und einfache Testfunktionen schreiben
- 🟡 … Fixtures mit `@pytest.fixture` definieren und in Testfunktionen nutzen
- 🟡 … mit `@pytest.mark.parametrize` einen Test für viele Eingaben wiederverwenden
- 🟡 … erwartete Ausnahmen mit `pytest.raises` testen
- 🔴 … einen sinnvollen pytest-Testlauf konfigurieren und das Ergebnis auswerten

---

## Setup – pytest installieren

```bash
# Installation (einmalig):
pip install pytest

# Version prüfen:
pytest --version

# Tests ausführen (im Projektverzeichnis):
pytest 06_pytest/code/ -v

# Mit Coverage (optional):
pip install pytest-cov
pytest 06_pytest/code/ --cov=06_pytest/code/ --cov-report=term-missing
```

---

## Hintergrund

pytest ist der de-facto Standard für Python-Tests im Berufsalltag.
Im Vergleich zu unittest hat pytest:

- Kein Boilerplate – Testfunktionen statt Testklassen
- Bessere Fehlerausgaben (zeigt Variablenwerte bei Fehlern)
- Mächtiges Fixture-System für Testvorbereitung
- Parametrisierung für Datentabellen-Tests
- Große Plugin-Bibliothek (pytest-cov, pytest-mock, ...)

---

## Aufgabe 0 – Grundbegriffe: pytest-Ausgabe lesen 🟢

**Einstieg: Ergebnisse interpretieren**

Lies folgende pytest-Ausgabe und beantworte die Fragen:

```
==================== test session starts ====================
collected 5 items

test_rechner.py::test_addieren_positiv   PASSED          [ 20%]
test_rechner.py::test_addieren_negativ   PASSED          [ 40%]
test_rechner.py::test_dividieren         FAILED          [ 60%]
test_rechner.py::test_division_durch_null PASSED         [ 80%]
test_rechner.py::test_falscher_typ       ERROR           [100%]

==================== 3 passed, 1 failed, 1 error in 0.04s ====================
```

**a)** Wie viele Tests wurden ausgeführt? Wie viele waren erfolgreich?

**b)** Was ist der Unterschied zwischen `FAILED` und `ERROR`?

**c)** Welcher Test schlägt fehl? Was könnte der Grund sein?

**d)** In welcher Datei befinden sich die Tests? Wie erkennst du das?

**e)** Wie lautet der Befehl, mit dem diese Ausgabe erzeugt wurde?
(Tipp: Was bedeutet das `-v`-Flag?)

Trage deine Antworten in `06_antworten.md` ein.

---

## Aufgabe 1 – Von unittest zu pytest migrieren 🟡

**a)** Konvertiere zwei Testmethoden aus Baustein 05 in pytest-Testfunktionen.
Vergleiche: Was vereinfacht sich? Was fehlt?

```python
# unittest-Stil (Baustein 05):
class TestKontorechner(unittest.TestCase):
    def test_einzahlen_positiver_betrag(self):
        konto = Kontorechner()
        konto.einzahlen(100)
        self.assertEqual(konto.kontostand, 100)

# pytest-Stil (deine Aufgabe):
def test_einzahlen_positiver_betrag():
    # TODO: Deine Implementierung
    pass
```

**b)** Führe die Tests mit `pytest 06_pytest/code/starter.py -v` aus.
Was bedeutet die Ausgabe `PASSED` / `FAILED` / `ERROR`?

---

## Aufgabe 2 – Fixtures 🟡

**Szenario:** Du testest eine Klasse `Benutzerkontoservice` aus `starter.py`.
Das Anlegen eines Test-Kontos ist aufwändig – du willst es nicht in jedem Test wiederholen.

**a)** Schreibe ein Fixture `kontoservice()`, das einen fertig eingerichteten `BenutzerkontoService` zurückgibt.

```python
@pytest.fixture
def kontoservice():
    # TODO: Service anlegen, Testbenutzer eintragen
    service = BenutzerkontoService()
    service.benutzer_anlegen("testuser", "Test1234!")
    return service
```

**b)** Verwende das Fixture in mindestens 4 Testfunktionen.
Beachte: Das Fixture wird für jeden Test neu erzeugt – warum ist das wichtig?

**c)** Erweitere das Fixture um `scope="module"` und erkläre, wann das sinnvoll ist.

---

## Aufgabe 3 – Parametrisierung 🟡

Ohne Parametrisierung:

```python
def test_note_bei_100():
    assert berechne_note(100) == 1

def test_note_bei_90():
    assert berechne_note(90) == 2
# ... (sehr viel Wiederholung)
```

Mit Parametrisierung:

```python
@pytest.mark.parametrize("punkte, erwartete_note", [
    (100, 1),
    (92, 1),
    (91, 2),
    # ...
])
def test_berechne_note(punkte, erwartete_note):
    assert berechne_note(punkte) == erwartete_note
```

**a)** Schreibe einen parametrisierten Test für `berechne_note()` aus Baustein 04,
der alle Notengrenzen und mindestens 2 Vertreter je Äquivalenzklasse prüft (mind. 14 Testfälle).

**b)** Schreibe einen parametrisierten Test für `validiere_menge()` aus Baustein 04,
der alle gültigen und ungültigen Klassen plus alle Grenzwerte abdeckt.

**c)** Führe aus und interpretiere: Wie viele Tests wurden erzeugt? Wie lange hat das gedauert?

---

## Aufgabe 4 – pytest.raises 🟡

```python
# Einfache Variante:
def test_negative_einzahlung():
    konto = Kontorechner()
    with pytest.raises(ValueError):
        konto.einzahlen(-50)

# Mit Prüfung der Fehlermeldung:
def test_negative_einzahlung_fehlermeldung():
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.einzahlen(-50)
```

**a)** Schreibe mindestens 3 Tests mit `pytest.raises`, die auch die Fehlermeldung prüfen (`match=`).

**b)** Was ist der Unterschied zwischen `pytest.raises` und `unittest.assertRaises`?
Welche Variante bevorzugst du und warum?

---

## Aufgabe 5 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Entwicklungsteam hat folgende Testanforderung dokumentiert:

> "Die Funktion `berechne_versandkosten(gewicht, express)` soll für alle
> Kombination aus Gewichtsklassen (≤5 kg, >5 kg) und Express-Option
> korrekte Preise zurückgeben. Zusätzlich sollen ungültige Eingaben
> (negatives Gewicht, falscher Typ) korrekt abgelehnt werden."

**(a)** Implementieren Sie `berechne_versandkosten()` in `starter.py`. _(4 Punkte)_

**(b)** Schreiben Sie einen vollständigen parametrisierten pytest-Test für alle gültigen Fälle. _(6 Punkte)_

**(c)** Schreiben Sie je einen Test für die beiden ungültigen Eingaben. _(4 Punkte)_

**(d)** Erläutern Sie den Vorteil der Parametrisierung gegenüber einzelnen Testfunktionen. _(2 Punkte)_

---

## Tandem-Aufgabe 👥

**Code Review der Tests:**

Jede Person schreibt für eine selbst gewählte Funktion:

- Mindestens 2 normale Testfunktionen
- Mindestens 1 Fixture
- Mindestens 1 parametrisierten Test

Dann Code-Review im Tandem:

- Sind die Testnamen aussagekräftig?
- Werden alle Äquivalenzklassen aus Baustein 04 abgedeckt?
- Wird `pytest.raises` für alle Fehlerfälle genutzt?
- Gibt es unnötige Wiederholungen, die durch Parametrisierung beseitigt werden könnten?

**Erkläre deinem Tandempartner:** Erkläre, warum `@pytest.fixture` mächtiger ist als das Anlegen eines Objekts direkt im Test. Nutze ein Beispiel aus deiner eigenen Lösung. Dein Tandempartner stellt mindestens eine Rückfrage.

---

## Active Recall 🧠

_Unterlagen zu:_

1. Wie unterscheidet sich eine pytest-Testfunktion von einer unittest-Testmethode?
2. Wozu dient ein Fixture?
3. Was passiert, wenn ein Fixture mit `scope="module"` definiert ist?
4. Wie prüfst du in pytest, dass eine bestimmte Exception geworfen wird?
5. Warum ist Parametrisierung besser als viele separate Testfunktionen?

---

## Reflexion 🚦

- [ x ] 🟢 Ich kann pytest eigenständig einsetzen und Fixtures + Parametrisierung nutzen
- [ ] 🟡 Ich verstehe die Konzepte, habe aber noch Probleme bei Fixtures
- [ ] 🔴 Ich brauche mehr Erklärungen oder Übung

**Was nimmst du mit?**

> ---

---

_Bei Problemen → [Stuck Protocol](../stuck_protocol.md)_
