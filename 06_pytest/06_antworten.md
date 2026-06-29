## Aufgabe 0
### a)

Es wurden **5 Tests** ausgeführt.  
Davon waren **3 erfolgreich**.

### b)

**FAILED** bedeutet: Der Test wurde ausgeführt, aber das Ergebnis war falsch.

**ERROR** bedeutet: Während des Tests ist ein unerwarteter Fehler aufgetreten, z. B. eine Exception.

### c)

Der Test `test_dividieren` schlägt fehl.

Möglicher Grund: Die Funktion `dividieren()` liefert ein falsches Ergebnis oder die erwartete Ausgabe im Test stimmt nicht.

### d)

Die Tests befinden sich in der Datei `test_rechner.py`.

Das erkennt man an den Zeilen:

`test_rechner.py::test_addieren_positiv`

### e)

Das -v bedeutet verbose, also ausführlichere Ausgabe.

## Aufgabe 1
### a)

Bei `pytest` braucht man keine Testklasse und kein `self.assertEqual`.

Man schreibt einfach:

```python
assert konto.kontostand == 100
```

Für Fehler nutzt man:

```python
with pytest.raises(ValueError):
    konto.einzahlen(0)
```

Was fehlt: `setUp()` aus `unittest`; bei `pytest` nutzt man dafür meistens `fixtures`.

## b) Tests ausführen

```bash
pytest 06_pytest/code/starter.py -v
```

`PASSED` bedeutet: Test bestanden.

`FAILED` bedeutet: Test wurde ausgeführt, aber das Ergebnis war falsch.

`ERROR` bedeutet: Test konnte wegen eines Fehlers nicht richtig ausgeführt werden. 

## Aufgabe 2
### b)
Das Fixture wird für jeden Test neu erzeugt. Das ist wichtig, damit jeder Test mit einem frischen Zustand startet und Tests sich nicht gegenseitig beeinflussen.

### c)
`scope="module"` bedeutet: Das Fixture wird nur einmal pro Testdatei erstellt und dann für alle Tests wiederverwendet.
Das ist sinnvoll, wenn das Erstellen sehr aufwändig ist, z. B. bei Datenbankverbindungen oder großen Testdaten.
Nachteil: Wenn ein Test den Zustand verändert, kann das andere Tests beeinflussen. Deshalb sollte man `scope="module"` nur verwenden, wenn die Tests den gemeinsamen Zustand nicht kaputtmachen.

## Aufgabe 3
### c)
Insgesamt werden hier erzeugt:

- `14` Tests für gültige Notengrenzen
- `3` Tests für ungültige Punktzahlen
- `10` Tests für `validiere_menge`

Also insgesamt: `27` einzelne Testfälle.

Die Laufzeit ist meistens sehr kurz

## Aufgabe 4
### b)
`pytest.raises` wird im pytest-Stil genutzt:

```python
with pytest.raises(ValueError):
    konto.einzahlen(-50)
```

`unittest.assertRaises` wird im unittest-Stil genutzt:

```python
with self.assertRaises(ValueError):
    konto.einzahlen(-50)
```

Ich bevorzuge `pytest.raises`, weil es kürzer und gut lesbar ist. Außerdem kann man mit `match=` einfach prüfen, ob auch die Fehlermeldung passt.

## Aufgabe 5
### d)
Parametrisierung vermeidet Wiederholung.  
Man schreibt eine Testfunktion und kann viele Eingabekombinationen übersichtlich testen.

## Aufgabe Tandem
`@pytest.fixture` ist mächtiger als ein Objekt oder Testdaten direkt im Test anzulegen, weil die Vorbereitung zentral an einer Stelle steht und von mehreren Tests wiederverwendet werden kann. In meinem Beispiel liefert das Fixture `beispiel_noten` mehrere typische Notenfälle. Wenn sich die Testdaten ändern, muss ich sie nur im Fixture anpassen und nicht in jedem einzelnen Test.

Mögliche Rückfrage des Tandempartners:  
Warum nutzt man dann nicht immer Fixtures?
Fixtures sind sinnvoll bei wiederverwendbarer Vorbereitung. Für sehr kleine Einzeltests reicht manchmal direktes Anlegen im Test.