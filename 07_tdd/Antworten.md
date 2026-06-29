Hier ist alles **extern als „antworten.md“ gedacht** (ohne Bezug zu starter.py):

---

# antworten.md

## Aufgabe 0 – TDD-Zyklus

### a) Reihenfolge

C → B → D → E → A

---

### b) Goldene TDD-Regel

Erst einen Test schreiben, der fehlschlägt, dann nur so viel Code schreiben, dass er besteht, danach verbessern ohne das Verhalten zu ändern.

---

### c) Warum „hässlicher“ Code im Green-Schritt?

Weil nur das Minimum implementiert wird, um den Test zu erfüllen.
Im nächsten Schritt wird dieser Code bewusst verbessert (Refactoring), ohne das Verhalten zu verändern.

---

### d) Baby Step

Ein sehr kleiner Entwicklungsschritt im TDD.

Warum sinnvoll:

 Fehler sind leichter zu finden
 weniger Risiko bei Änderungen
schneller Feedback-Zyklus

---

## Aufgabe 4 – IHK-Stil

### a) TDD-Phasen
Red: Test schreiben → muss fehlschlagen
Green: Minimalen Code schreiben → Test besteht
Refactor<> Code verbessern ohne Verhalten zu ändern

---

### b) Tests (vor Implementierung)

```python
import unittest

class TestZinsen(unittest.TestCase):

    def test_standard_fall(self):
        self.assertEqual(berechne_zinsen(1000, 5, 1), 1050)

    def test_null_jahre(self):
        self.assertEqual(berechne_zinsen(1000, 5, 0), 1000)

    def test_null_kapital(self):
        self.assertEqual(berechne_zinsen(0, 5, 5), 0)

    def test_negative_zinssatz(self):
        with self.assertRaises(ValueError):
            berechne_zinsen(1000, -1, 5)
```

---

### c) Implementierung

```python
def berechne_zinsen(kapital, zinssatz, jahre):
    if kapital < 0 or zinssatz < 0 or jahre < 0:
        raise ValueError("ungültige Eingabe")

    return kapital * (1 + zinssatz / 100) ** jahre
```

---

### d) Vorteile / Nachteil von TDD

Vorteile:

 frühzeitige Fehlererkennung
 besser strukturierter Code

Nachteil:

 höherer Anfangsaufwand / langsamer Start

---
