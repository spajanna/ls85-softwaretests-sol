# 06_antworten.md – Baustein 06: pytest

## Aufgabe 0 – pytest-Output interpretieren

Ein `pytest -v` zeigt pro Test: Datei::TestName und Status.
- PASSED: Test bestanden
- FAILED: Assertion fehlgeschlagen
- ERROR: Exception im Test außerhalb von Asserts

`-v` = verbose, zeigt alle Testnamen. Ohne `-v` sieht man nur
Punkte (.) und F/E.

---

## Aufgabe 1b – Migration unittest → pytest

Unterschiede:
- Keine Klasse nötig (einfache Funktionen reichen)
- `assert` statt `self.assertEqual()`
- `pytest.raises` statt `self.assertRaises`
- Kein `setUp()` nötig (Fixture-Funktion falls benötigt)
- Kürzer, lesbarer, weniger Boilerplate

---

## Aufgabe 2b – Warum wird Fixture pro Test neu erstellt?

pytest erstellt standardmäßig eine neue Fixture-Instanz pro Testfunktion
(`scope="function"`). So hat jeder Test einen sauberen, isolierten Zustand.
Das verhindert Seiteneffekte: Test A kann Test B nicht beeinflussen.

---

## Aufgabe 2c – scope="module"

`@pytest.fixture(scope="module")` erstellt das Fixture einmal pro Modul.
Sinnvoll, wenn die Initialisierung teuer ist (Datenbankverbindung,
API-Client), und der Zustand zwischen Tests nicht zurückgesetzt werden muss.

---

## Aufgabe 4b – pytest.raises vs unittest.assertRaises

| Aspekt | pytest.raises | unittest.assertRaises |
|--------|---------------|----------------------|
| Syntax | `with pytest.raises(...)` | `with self.assertRaises(...)` |
| match- Parameter | `match="Text"` | Kein direkter Match |
| Lesbarkeit | Kürzer | Länger (self.-Präfix) |
| Exception-Info | `as exc_info` möglich | `as cm` möglich |
| Import | `import pytest` | `import unittest` |

---

## Aufgabe 5 – IHK

`berechne_versandkosten()`-Tests decken alle 4 Kombinationen aus
Gewicht (≤5 / >5) und Versandart (Standard / Express) ab, plus
Grenzfälle (genau 5 kg) und Fehlerfälle (negativ, falscher Typ).
