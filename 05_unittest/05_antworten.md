# 05_antworten.md – Baustein 05: Python unittest

## Aufgabe 1c – Testausgabe interpretieren

Ein `.` bedeutet ein erfolgreicher Test, `F` ein fehlgeschlagener,
`E` ein Fehler (Exception im Test). Bei `python -m unittest -v`
sieht man zusätzlich die Namen aller Tests.

---

## Aufgabe 2c – Warum setUp()?

`setUp()` vermeidet Code-Duplikation: statt in jeder Testmethode
ein neues `Einkaufsliste()`-Objekt zu erstellen, passiert das
automatisch vor jedem Test. Zudem stellt `setUp()` sicher, dass
jeder Test mit einem frischen, definierten Zustand startet.

---

## Aufgabe 3b – assertRaises Variante

- **Context Manager** (`with self.assertRaises(...)`): Lesbarer,
  erlaubt Code nach der Exception im selben Block
- **Callable** (`self.assertRaises(Error, func, arg)`): Kompakter,
  nützlich für Einzeiler ohne zusätzliche Asserts

Beide testen, ob eine bestimmte Exception geworfen wird.

---

## Aufgabe 4 – IHK-Stil

```python
def berechne_mehrwertsteuer(netto: float, satz: float) -> float:
    return round(netto * satz, 2)
```

Tests:
- `test_mwst_19_prozent`: netto=100, satz=0.19 → erwartet 19.00
- `test_mwst_7_prozent`: netto=100, satz=0.07 → erwartet 7.00
- `test_mwst_null`: netto=0, satz=0.19 → erwartet 0.00
- `test_mwst_rundung`: netto=9.99, satz=0.19 → erwartet 1.90

Float-Problem: `9.99 * 0.19 = 1.8981`, gerundet auf 2 Stellen = 1.90.
`assertEqual(1.8981, 1.90)` würde wegen Float-Ungenauigkeiten fehlschlagen.
Alternative: `assertAlmostEqual(1.8981, 1.90, places=2)` oder
die Funktion rundet bereits auf 2 Stellen → direkter Vergleich möglich.
