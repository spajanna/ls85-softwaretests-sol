## Aufgabe 0
### a)

`test_rabatt_wird_korrekt_abgezogen` prüft, ob bei 5 Stiften à 2,00 € ein Rabatt von 10 % korrekt abgezogen wird und der Gesamtpreis 9,00 € ist.

`test_leere_bestellung_hat_preis_null` prüft, ob eine Bestellung ohne Artikel den Gesamtpreis 0,0 hat.

`test_negativer_rabatt_wirft_fehler` prüft, ob ein negativer Rabatt eine `ValueError`-Exception auslöst.

### b)

Verwendete Klasse:

- `Bestellsystem`

Verwendete Methoden:

- `artikel_hinzufuegen()`
- `rabatt_setzen()`
- `gesamtpreis()`

### c)

`assertAlmostEqual` prüft, ob zwei Zahlen ungefähr gleich sind.

Das wird bei Fließkommazahlen benutzt, weil es bei Dezimalzahlen kleine Rundungsfehler geben kann. Deshalb ist es hier sicherer als `assertEqual`.

### d)

Wenn `test_negativer_rabatt_wirft_fehler` fehlschlägt, wurde bei `rabatt_setzen(-5)` keine `ValueError` ausgelöst.

Das Problem wäre dann, dass die Implementierung negative Rabatte erlaubt oder nicht richtig validiert.

## Aufgabe 1
### a) Analyse der Klasse

Die Klasse `Kontorechner` verwaltet einen einfachen Kontostand.

Methoden:

- `__init__()`: setzt den Anfangskontostand auf `0.0`
- `kontostand`: gibt den aktuellen Kontostand zurück
- `einzahlen(betrag)`: erhöht den Kontostand um den Betrag
- `abheben(betrag)`: reduziert den Kontostand um den Betrag

Fehlerfälle:

- Einzahlung mit `0` oder negativem Betrag wirft `ValueError`
- Abhebung mit `0`, negativem Betrag oder zu wenig Guthaben wirft `ValueError`

### c)
## c) Ausgabe interpretieren

`.` bedeutet: Test erfolgreich bestanden.

`F` bedeutet: Test fehlgeschlagen, weil das Ergebnis nicht der Erwartung entspricht.

`E` bedeutet: Fehler im Test, z. B. unerwartete Exception oder Programmfehler.

Beispiel:  
Wenn alle Tests bestanden sind, sieht man mehrere Punkte:

......

Das bedeutet: Alle Tests waren erfolgreich.

## Aufgabe 2
### c)
setUp() ist sinnvoll, weil vor jedem Test automatisch eine frische Einkaufsliste erstellt wird.
Dadurch muss man den gleichen Code nicht in jeder Testmethode wiederholen. Außerdem beeinflussen sich die Tests nicht gegenseitig, weil jeder Test mit einer neuen, leeren Liste startet.

## Aufgabe 3
### a)
```python
def test_einzahlen_null_wirft_fehler(self):
    # Variante 2: Context Manager
    with self.assertRaises(ValueError):
        self.konto.einzahlen(0)

def test_einzahlen_negativ_wirft_fehler(self):
    # Variante 1: Callable + Argumente
    self.assertRaises(ValueError, self.konto.einzahlen, -50)
```

### Aufgabe 4
### (a) 

Annahme: `steuersatz` wird in Prozent angegeben und die Funktion gibt nur den Steuerbetrag zurück.

| Testfall | netto | steuersatz | Erwartung |
|---|---:|---:|---:|
| TC01 Standardfall 19 % | 100.00 | 19 | 19.00 |
| TC02 Ermäßigter Steuersatz 7 % | 200.00 | 7 | 14.00 |
| TC03 Netto 0 € | 0.00 | 19 | 0.00 |
| TC04 Kommazahl | 49.99 | 19 | 9.4981 |

### (b) 

```python

class TestMehrwertsteuer(unittest.TestCase):

    def test_standard_19_prozent(self):
        ergebnis = berechne_mehrwertsteuer(100.00, 19)
        self.assertAlmostEqual(ergebnis, 19.00)

    def test_ermaessigter_steuersatz_7_prozent(self):
        ergebnis = berechne_mehrwertsteuer(200.00, 7)
        self.assertAlmostEqual(ergebnis, 14.00)

    def test_netto_null(self):
        ergebnis = berechne_mehrwertsteuer(0.00, 19)
        self.assertAlmostEqual(ergebnis, 0.00)

    def test_kommazahl(self):
        ergebnis = berechne_mehrwertsteuer(49.99, 19)
        self.assertAlmostEqual(ergebnis, 9.4981)

```

### (c)

Bei Kommazahlen ist `assertEqual` problematisch, weil Float-Werte kleine Rundungsfehler enthalten können.

Besser ist `assertAlmostEqual`, weil damit geprüft wird, ob zwei Kommazahlen ungefähr gleich sind.

## Aufgabe Tandem
setUp() bereitet vor jedem Test eine frische Testumgebung vor, z. B. einen neuen Logger.
Der eigentliche Testcode führt die Aktion aus und prüft mit assert, ob das Ergebnis stimmt.
tearDown() räumt nach jedem Test auf, z. B. Dateien löschen oder Verbindungen schließen.
Die Trennung ist wichtig, damit Tests übersichtlich bleiben und sich nicht gegenseitig beeinflussen.