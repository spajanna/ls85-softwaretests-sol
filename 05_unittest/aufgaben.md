# Baustein 05 – Python unittest 🟡

> **Schwierigkeit:** 🟡 Anwendung  
> **Zeitrahmen:** ca. 120 Minuten  
> **Voraussetzung:** Baustein 01–04 abgeschlossen  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/YKEuBgsNm9" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 05: unittest</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich habe bereits Unit-Tests in Python geschrieben
- [ ] 🟡 Ich weiß was Unit-Tests sind, habe aber noch keinen geschrieben
- [ ] 🔴 Das ist Neuland für mich

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … das `unittest`-Modul importieren und eine Testklasse erstellen
- 🟡 … Testmethoden mit `self.assertEqual`, `self.assertRaises`, `self.assertTrue` schreiben
- 🟡 … `setUp()` und `tearDown()` für Testvorbereitung und -bereinigung nutzen
- 🟡 … Tests mit `python -m unittest` ausführen und das Ergebnis interpretieren
- 🔴 … Tests sinnvoll benennen, strukturieren und nach Äquivalenzklassen organisieren

---

## Hintergrund

Das Modul `unittest` ist Pythons eingebautes Test-Framework – keine Installation notwendig.
Es folgt dem xUnit-Muster, das aus Java (JUnit) stammt und in fast allen Sprachen existiert.

```bash
# Tests ausführen (im Verzeichnis des Projekts):
python -m unittest 05_unittest/code/starter.py -v

# Alle Tests im Projekt finden und ausführen:
python -m unittest discover -v
```

Das `-v` steht für "verbose" – du siehst dann den Namen jedes Tests.

---

## Aufgabe 0 – Grundbegriffe: Unit-Test lesen und verstehen 🟢

**Einstieg: Tests lesen lernen**

Lies den folgenden Unit-Test und beantworte die Fragen – ohne die Implementierung zu kennen:

```python
import unittest

class TestBestellsystem(unittest.TestCase):

    def test_rabatt_wird_korrekt_abgezogen(self):
        bestellung = Bestellsystem()
        bestellung.artikel_hinzufuegen("Stift", 2.00, 5)
        bestellung.rabatt_setzen(10)
        self.assertAlmostEqual(bestellung.gesamtpreis(), 9.00)

    def test_leere_bestellung_hat_preis_null(self):
        bestellung = Bestellsystem()
        self.assertEqual(bestellung.gesamtpreis(), 0.0)

    def test_negativer_rabatt_wirft_fehler(self):
        bestellung = Bestellsystem()
        with self.assertRaises(ValueError):
            bestellung.rabatt_setzen(-5)
```

**a)** Was testet jeder dieser Tests? Beschreibe in je einem Satz.
Der erste Test stellt sicher, dass ein gesetzter Rabatt in Prozent den Gesamtpreis der hinzugefügten Artikel mathematisch korrekt mindert. Der zweite Test überprüft, ob ein neu erstelltes, leeres Bestellsystem standardmäßig einen Gesamtpreis von exakt Null zurückgibt. Der dritte Test stellt sicher, dass das System die Eingabe eines unzulässigen, negativen Rabattwerts blockiert und dies mit einem ValueError quittiert.

**b)** Welche Klasse und welche Methoden werden in den Tests verwendet?
In den Tests wird die Testklasse TestBestellsystem verwendet, welche von unittest.TestCase erbt. Seitens der Anwendungslogik werden die Klasse Bestellsystem sowie deren Methoden artikel_hinzufuegen, rabatt_setzen und gesamtpreis aufgerufen.

**c)** Was bedeutet `assertAlmostEqual` und warum wird es hier statt `assertEqual` verwendet?
In den Tests wird die Testklasse TestBestellsystem verwendet, welche von unittest.TestCase erbt. Seitens der Anwendungslogik werden die Klasse Bestellsystem sowie deren Methoden artikel_hinzufuegen, rabatt_setzen und gesamtpreis aufgerufen.

**d)** Was passiert, wenn `test_negativer_rabatt_wirft_fehler` fehlschlägt?
Was wäre dann das Problem in der Implementierung?
Wenn dieser Test fehlschlägt, bedeutet das, dass bei der Übergabe eines negativen Werts kein ValueError ausgelöst wurde. Das Problem in der Implementierung wäre demnach eine fehlende oder fehlerhafte Validierungslogik in der Methode rabatt_setzen, wodurch unzulässige Werte unbemerkt verarbeitet würden.

Trage deine Antworten in `05_antworten.md` ein.

---

## Aufgabe 1 – Erste Unit-Tests schreiben 🟡

In `code/starter.py` findest du die Klasse `Kontorechner` – ein vereinfachter Kontostand-Manager.

**a)** Analysiere die Klasse: Welche Methoden hat sie? Was soll jede Methode tun?

**b)** Schreibe in der vorbereiteten Testklasse `TestKontorechner` mindestens folgende Tests:

| Testmethode                           | Was wird geprüft                         |
| ------------------------------------- | ---------------------------------------- |
| `test_einzahlen_positiver_betrag`     | Einzahlung erhöht den Kontostand korrekt |
| `test_einzahlen_null_wirft_fehler`    | Einzahlung von 0 → `ValueError`          |
| `test_einzahlen_negativ_wirft_fehler` | Negativer Betrag → `ValueError`          |
| `test_abheben_guthaben_vorhanden`     | Abhebung reduziert Kontostand korrekt    |
| `test_abheben_kein_guthaben`          | Abhebung ohne Guthaben → `ValueError`    |
| `test_kontostand_anfangswert`         | Neues Konto hat Kontostand 0             |

**c)** Führe die Tests aus und interpretiere die Ausgabe.
Was bedeuten `.`, `F` und `E` in der Ausgabe?

---

## Aufgabe 2 – setUp und tearDown 🟡

**Szenario:** Du testest eine Klasse `Einkaufsliste`, die Artikel hinzufügen, entfernen und anzeigen kann.

**a)** Implementiere `Einkaufsliste` in `starter.py` (mindestens: `hinzufuegen`, `entfernen`, `anzeigen`, `ist_leer`).

**b)** Schreibe eine Testklasse `TestEinkaufsliste`, die:

- In `setUp()` eine neue `Einkaufsliste` anlegt
- In `tearDown()` eine Meldung ausgibt (demonstriert die Reihenfolge)
- Mindestens 5 Testmethoden enthält

**c)** Warum ist `setUp()` sinnvoller als das Erstellen des Objekts in jeder einzelnen Testmethode?

---

## Aufgabe 3 – assertRaises richtig nutzen 🟡

Ein häufiger Fehler: `assertRaises` wird falsch verwendet.

```python
# Falsch – Exception wird sofort geworfen, nicht gefangen:
self.assertRaises(ValueError, meine_funktion(-1))

# Richtig – Variante 1 (Callable + Argumente):
self.assertRaises(ValueError, meine_funktion, -1)

# Richtig – Variante 2 (Context Manager):
with self.assertRaises(ValueError):
    meine_funktion(-1)
```

**a)** Zeige anhand deiner Tests aus Aufgabe 1, dass du beide Varianten korrekt anwenden kannst.

**b)** Schreibe einen Test für die Funktion `berechne_note()` aus Baustein 04, der prüft,
dass bei einer Punktzahl von -1 und 101 jeweils ein `ValueError` geworfen wird.

---

## Aufgabe 4 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Betrieb hat eine Funktion `berechne_mehrwertsteuer(netto: float, steuersatz: float) -> float` entwickelt.

**(a)** Nennen Sie vier sinnvolle Testfälle mit konkreten Eingabe- und Erwartungswerten. _(4 Punkte)_

**(b)** Schreiben Sie die vier Testfälle als Python-`unittest`-Methoden in eine Testklasse. _(8 Punkte)_

**(c)** Welcher Assertion-Typ ist bei Kommazahlen problematisch? Nennen Sie die Alternative und warum diese nötig ist. _(3 Punkte)_

---

## Tandem-Aufgabe 👥

**Gegenseitiges Testen:**

Person A: Implementiert eine Klasse `Dateilogger` mit den Methoden:

- `schreiben(nachricht: str)` → fügt Nachricht zur Log-Liste hinzu
- `auslesen()` → gibt alle Nachrichten als Liste zurück
- `loeschen()` → leert den Log
- `anzahl_eintraege()` → gibt Anzahl der Einträge zurück

Person B: Schreibt die Tests für diese Klasse, ohne die Implementierung zu kennen (nur die Schnittstellenbeschreibung).

Dann: Tests zusammenführen, ausführen – was schlägt fehl? Warum?

**Erkläre deinem Tandempartner:** Erkläre den Unterschied zwischen `setUp()`, dem eigentlichen Testcode und `tearDown()`. Warum ist die Trennung dieser drei Teile wichtig? Dein Tandempartner stellt mindestens eine Rückfrage.

---

## Active Recall 🧠

_Unterlagen zu:_

1. Wie heißt die Basisklasse, von der alle Testklassen erben müssen?
2. Mit welchem Befehl führst du alle Tests in einem Verzeichnis aus?
3. Was ist der Unterschied zwischen `assertEqual` und `assertAlmostEqual`?
4. Wann wird `setUp()` aufgerufen – einmal pro Testklasse oder einmal pro Testmethode?
5. Was bedeutet ein `E` (Error) in der unittest-Ausgabe im Unterschied zu `F` (Failure)?

---

## Reflexion 🚦

- [ ] 🟢 Ich kann eigenständig Unit-Tests mit unittest schreiben
- [ ] 🟡 Ich verstehe das Konzept, habe aber noch Probleme mit assertRaises
- [ ] 🔴 Ich brauche mehr Erklärungen oder Beispiele

**Was nimmst du mit?**

> ---

---

_Bei Problemen → [Stuck Protocol](../stuck_protocol.md)_
