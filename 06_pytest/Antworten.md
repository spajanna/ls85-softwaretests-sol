0.

a)
Es wurden 5 Tests ausgeführt. Davon waren 3 erfolgreich.

b)

 FAILED: Der Test wurde ausgeführt, aber das Ergebnis war falsch.
 ERROR: Während des Tests ist ein Fehler (Exception) aufgetreten.

c)
`test_dividieren` schlägt fehl. Wahrscheinlich liefert die Funktion ein falsches Ergebnis.

d)
Die Tests befinden sich in test_rechner.py. Das erkennt man am Anfang jeder Zeile der Ausgabe.

e)

```bash
pytest test_rechner.py -v
```

`-v` bedeutet verbose und zeigt die einzelnen Tests mit ihrem Ergebnis an.



1.

a)

```python
def test_einzahlen_positiver_betrag():
    konto = Kontorechner()
    konto.einzahlen(100)
    assert konto.kontostand == 100


def test_einzahlen_null_wirft_fehler():
    konto = Kontorechner()
    with pytest.raises(ValueError):
        konto.einzahlen(0)
```

Vereinfacht:

 keine Testklasse nötig
 kein `self`
 `assert` statt `assertEqual`

Fehlt:

 keine `unittest.TestCase`

b)

 PASSED: Test erfolgreich
 FAILED: Test fehlgeschlagen
 ERROR: Fehler während der Testausführung



2.

b)

Das Fixture wird in jeder Testfunktion verwendet.

Es wird für jeden Test neu erstellt, damit sich die Tests nicht gegenseitig beeinflussen.

c)

```python
@pytest.fixture(scope="module")
```

Das ist sinnvoll, wenn das Erstellen des Objekts lange dauert und alle Tests dieselben Daten verwenden können.



3.

c)

Es werden so viele Tests erzeugt, wie Datensätze in `@pytest.mark.parametrize` vorhanden sind.

Die Ausführung dauert meist nur wenige Millisekunden.



4.

a)

```python
with pytest.raises(ValueError, match="positiv"):
    konto.einzahlen(-10)

with pytest.raises(ValueError, match="positiv"):
    konto.abheben(0)

with pytest.raises(ValueError, match="Guthaben"):
    konto.abheben(100)
```

b)

`pytest.raises` wird mit einem `with`-Block verwendet.

`assertRaises` gehört zu `unittest`.

Ich bevorzuge `pytest.raises`, weil der Code kürzer und besser lesbar ist.



5.

d)

Durch Parametrisierung wird derselbe Test mit mehreren Eingaben ausgeführt.

Dadurch gibt es weniger doppelten Code und die Tests sind leichter zu erweitern und zu warten.
