## Aufgabe 0
### a) Zuordnung

| Aussage | Dokument |
|---|---|
| „Wir werden alle Module mit pytest testen." | Testplan |
| „TC-007 ist fehlgeschlagen: Bestand wurde auf -5 gesetzt." | Testprotokoll |
| „8 von 10 Tests bestanden, 1 Fehler offen." | Testbericht |
| „Abnahmekriterium: Coverage > 80 %." | Testplan |
| „Empfehlung: System ist abnahmebereit." | Testbericht |

### b) Zeitpunkt

- Testplan: vor dem Testen
- Testprotokoll: während des Testens
- Testbericht: nach dem Testen

### c)

Ohne Dokumentation ist später nicht nachvollziehbar, was genau getestet wurde und welche Fehler aufgetreten sind. Außerdem kann man ohne Testbericht schwer entscheiden, ob das System abnahmebereit ist.

## Aufgabe 1
### a,b)
## a/b) Testfalldokumentation `authentifiziere_benutzer()`

| TC-ID | Titel | Vorbedingung | Testeingabe | Testschritte | Erwartetes Ergebnis | Tatsächliches Ergebnis | Status |
|---|---|---|---|---|---|---|---|
| TC-AUTH-001 | Gültiger Login | Funktion ist vorhanden | `admin`, `geheim123` | Funktion mit gültigen Daten aufrufen | `True` | `True` | Bestanden |
| TC-AUTH-002 | Falsches Passwort | Funktion ist vorhanden | `admin`, `falsch123` | Funktion mit falschem Passwort aufrufen | `False` | `False` | Bestanden |
| TC-AUTH-003 | Unbekannter Benutzer | Funktion ist vorhanden | `unbekannt`, `geheim123` | Funktion mit unbekanntem Benutzer aufrufen | `False` | `False` | Bestanden |
| TC-AUTH-004 | Benutzername zu kurz | Funktion ist vorhanden | `ad`, `geheim123` | Funktion mit zu kurzem Benutzernamen aufrufen | `False` | `False` | Bestanden |
| TC-AUTH-005 | Benutzername zu lang | Funktion ist vorhanden | `sehrlangerbenutzername123`, `geheim123` | Funktion mit zu langem Benutzernamen aufrufen | `False` | `False` | Bestanden |
| TC-AUTH-006 | Sonderzeichen im Benutzernamen | Funktion ist vorhanden | `admin!`, `geheim123` | Funktion mit ungültigem Zeichen aufrufen | `False` | `False` | Bestanden |
| TC-AUTH-007 | Passwort zu kurz | Funktion ist vorhanden | `admin`, `kurz` | Funktion mit zu kurzem Passwort aufrufen | `False` | `False` | Bestanden |
| TC-AUTH-008 | Leerer Benutzername | Funktion ist vorhanden | `""`, `geheim123` | Funktion mit leerem Benutzernamen aufrufen | `False` | `False` | Bestanden |


## Aufgabe 3
### b)
b) Bericht interpretieren

Im Coverage-Bericht steht bei `Missing`, welche Zeilen noch nicht getestet wurden.

Beispiel:

```text
Name        Stmts   Miss  Cover   Missing
starter.py    120     18    85%   45-48, 72, 90-96
```

Das bedeutet:

- `Stmts`: Anzahl der Code-Zeilen
- `Miss`: nicht getestete Zeilen
- `Cover`: aktuelle Testabdeckung
- `Missing`: konkrete Zeilen, die noch fehlen

Zweige fehlen meistens bei `if`, `else`, `raise`, Grenzfällen und Fehlerfällen.

### d)
d) Ist 100 % Coverage ein Qualitätsgarant?

Nein. 100 % Coverage bedeutet nur, dass jede Zeile mindestens einmal ausgeführt wurde.

Es garantiert nicht, dass die Tests sinnvoll sind oder die richtigen Erwartungen prüfen. Ein schlechter Test kann Code ausführen, aber trotzdem keine Fehler finden.

## Aufgabe 5
### a)

Es wurden insgesamt 11 Tests ausgeführt.

8 Tests waren erfolgreich.

Erfolgsquote:

8 / 11 * 100 = 72,7 %

### b)

**FAILED** bedeutet: Der Test wurde ausgeführt, aber das Ergebnis entsprach nicht der Erwartung.

Beispiel: Erwartet wurde eine Fehlermeldung, aber keine wurde ausgelöst.

**ERROR** bedeutet: Der Test konnte nicht korrekt ausgeführt werden, weil ein unerwarteter Fehler aufgetreten ist.

Beispiel: Importfehler, fehlende Datei oder unerwartete Exception.

### c) 

| Testfall | Status | Bewertung |
|---|---|---|
| test_artikel_anlegen | Bestanden | OK |
| test_bestand_erhoehen | Bestanden | OK |
| test_bestand_reduzieren_unter_null | Fehlgeschlagen | Fehler muss behoben werden |
| test_artikel_suchen_vorhanden | Bestanden | OK |
| test_artikel_suchen_nicht_vorhanden | Fehlgeschlagen | Fehler muss behoben werden |
| test_lager_kapazitaet_pruefen | Bestanden | OK |
| test_bericht_erstellen | Error | Ursache muss analysiert werden |
| test_bestand_exportieren | Bestanden | OK |
| test_import_aus_csv | Bestanden | OK |
| test_loeschen_vorhandener_artikel | Bestanden | OK |

**Zusammenfassung**

8 Tests bestanden, 2 Tests fehlgeschlagen, 1 Test mit Error.

Erfolgsquote: 72,7 %

**Bewertung**

Das System ist nicht abnahmebereit, weil noch fehlgeschlagene Tests und ein Error vorhanden sind.

### d)

- Fehler bei `test_bestand_reduzieren_unter_null` analysieren und beheben
- Fehler bei `test_artikel_suchen_nicht_vorhanden` analysieren und beheben
- Ursache für `test_bericht_erstellen` prüfen
- Tests nach der Fehlerbehebung erneut ausführen
- Regressionstests durchführen, damit keine bestehenden Funktionen beschädigt wurden
