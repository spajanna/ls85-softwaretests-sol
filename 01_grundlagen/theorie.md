# Baustein 01 – Theorie: Grundlagen der Softwaretests

> **Lesezeit:** ca. 20–25 Minuten  
> Lies diesen Text vollständig durch, bevor du mit den Aufgaben beginnst.

---

## Was ist Softwaretesting und warum ist es wichtig?

Softwaretesting ist der systematische Prozess, bei dem Software auf Fehler und Abweichungen vom
erwarteten Verhalten geprüft wird. Ziel ist **nicht**, zu beweisen, dass Software fehlerfrei ist,
sondern Fehler **aufzudecken** – bevor sie im Produktivbetrieb zu Schäden führen.

Reale Beispiele zeigen die Konsequenzen fehlender Tests:

- **Ariane-5-Absturz (1996):** Ein Ganzzahlüberlauf in der Flugsoftware zerstörte die Rakete
  37 Sekunden nach dem Start – Schaden: ca. 370 Mio. USD.
- **Therac-25-Strahlengerät (1985–1987):** Software-Fehler in der Steuerung führten zu massiven
  Überdosierungen bei Krebspatienten mit tödlichen Folgen.
- **Y2K-Bug:** Das Jahrtausend-Problem zwang Unternehmen weltweit, Milliarden in nachträgliche
  Korrekturen und Tests zu investieren.

Im Berufsalltag als Fachinformatiker bedeutet das: Wer systematisch testet, handelt professionell
und schützt Kunden, das Unternehmen und sich selbst vor vermeidbaren Fehlern.

---

## Grundbegriffe: Fehler, Defekt, Versagen

Diese drei Begriffe werden häufig verwechselt – der ISTQB-Standard trennt sie klar:

| Begriff      | Englisch             | Bedeutung                                                                |
| ------------ | -------------------- | ------------------------------------------------------------------------ |
| **Fehler**   | Error / Mistake      | Die falsche Handlung eines Menschen (z. B. falscher Algorithmus gedacht) |
| **Defekt**   | Defect / Bug / Fault | Die fehlerhafte Stelle im Code (Ergebnis des Fehlers)                    |
| **Versagen** | Failure              | Das beobachtbare Fehlverhalten zur Laufzeit                              |

**Beispiel:** Ein Entwickler denkt an die falsche Formel (_Error_), schreibt deshalb `> 0` statt
`>= 0` (_Defect_), und das Programm liefert bei Eingabe `0` ein falsches Ergebnis (_Failure_).

Die Kette lautet immer: **Error → Defect → Failure**

---

## Ziele des Testens (nach ISTQB)

Das ISTQB definiert folgende Hauptziele für das Testen:

1. **Fehler finden** – Defekte aufdecken, bevor Software ausgeliefert wird
2. **Vertrauen aufbauen** – Qualität gegenüber Kunden und Stakeholdern nachweisen
3. **Informationen liefern** – Entscheidungsgrundlage für die Release-Freigabe schaffen
4. **Fehler verhindern** – durch frühe Einbindung von Testern in Anforderungsanalyse und Design

Ein wichtiges Grundprinzip: **Testen zeigt die Anwesenheit von Fehlern, nicht deren Abwesenheit.**
Software, die alle Tests besteht, ist nicht beweisbar fehlerfrei – vollständiges Testen ist
aufgrund der unendlichen Zahl möglicher Eingaben praktisch unmöglich.

---

### Die 7 Grundprinzipien des Testens (ISTQB)

| #   | Prinzip                                       | Bedeutung                                                                                          |
| --- | --------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 1   | **Testen zeigt die Anwesenheit von Fehlern**  | Tests können beweisen dass Fehler vorhanden sind – aber nie dass keine vorhanden sind              |
| 2   | **Vollständiges Testen ist nicht möglich**    | Alle Eingaben und Pfade zu testen wäre unendlich aufwändig – deshalb priorisieren wir              |
| 3   | **Frühzeitiges Testen spart Kosten**          | Ein Fehler der früh gefunden wird ist 10× billiger zu beheben als einer der spät gefunden wird     |
| 4   | **Fehler häufen sich**                        | 80% der Fehler stecken in 20% des Codes – dort zuerst testen!                                      |
| 5   | **Pestizid-Paradoxon**                        | Immer dieselben Tests finden irgendwann keine neuen Fehler mehr – Tests müssen aktualisiert werden |
| 6   | **Testen ist kontextabhängig**                | Eine Steuerungssoftware für Flugzeuge braucht andere Tests als eine App                            |
| 7   | **Trugschluss: keine Fehler = gute Software** | Fehlerfreier Code der die Anforderungen nicht erfüllt ist trotzdem wertlos                         |

---

## Das V-Modell

Das V-Modell ordnet jeder Entwicklungsphase eine korrespondierende Testphase gegenüber:

![V-Modell](../assets/01_v-modell.png)

Linke Seite = Entwicklung, rechte Seite = Test. Testplanung beginnt **parallel zur Entwicklung**,
nicht erst danach. Die **Rule of Ten** besagt: Ein Fehler kostet in jeder nächsten Phase
ca. 10-mal mehr zur Behebung als in der vorherigen.

---

## Testprozess: Die 5 Phasen

| Phase               | Was passiert?                                           |
| ------------------- | ------------------------------------------------------- |
| **1. Planung**      | Ziele, Umfang, Ressourcen und Zeitplan festlegen        |
| **2. Analyse**      | Anforderungen und Risiken prüfen – _Was_ wird getestet? |
| **3. Entwurf**      | Testfälle, Testdaten und Testumgebung spezifizieren     |
| **4. Durchführung** | Tests ausführen, Ergebnisse protokollieren              |
| **5. Auswertung**   | Testergebnisse bewerten, Abschlussberichte erstellen    |

---

## Codebeispiele

### Beispiel 1: Fehlerhafte Funktion (Defekt)

```python
def berechne_mehrwertsteuer(netto_preis: float) -> float:
    """Berechnet den Bruttopreis mit 19 % MwSt."""
    # DEFEKT: gibt nur den MwSt-Betrag zurueck, nicht den Bruttopreis
    return netto_preis * 19 / 100
```

Der Fehler: `netto_preis * 19 / 100` ergibt nur den **MwSt-Betrag** (z. B. 19,00 €),
aber nicht den **Bruttopreis** (119,00 €). Der Entwickler hat die Formel falsch umgesetzt (_Error_).

### Beispiel 2: Test deckt den Defekt auf

```python
def test_berechne_mehrwertsteuer():
    """Prueft, ob der Bruttopreis korrekt berechnet wird."""
    netto = 100.0
    erwartet = 119.0          # 100 EUR + 19 % MwSt = 119 EUR

    ergebnis = berechne_mehrwertsteuer(netto)

    assert ergebnis == erwartet, f"Erwartet: {erwartet}, Erhalten: {ergebnis}"
```

**Ausgabe beim Ausführen mit pytest:**

```
FAILED - AssertionError: Erwartet: 119.0, Erhalten: 19.0
```

Der Test **schlägt fehl** und zeigt genau, wo und warum – das ist der Zweck eines guten Tests.

**Korrigierte Funktion:**

```python
def berechne_mehrwertsteuer(netto_preis: float) -> float:
    """Berechnet den Bruttopreis mit 19 % MwSt."""
    return netto_preis * 1.19   # Brutto = Netto * 1,19
```

---

## Weiterführende Links

| Ressource                                                                                       | Beschreibung                                                                             |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [ISTQB – istqb.org](https://www.istqb.org)                                                      | Offizielle Seite der ISTQB-Zertifizierung: Glossare, Lehrpläne, Prüfungsinfos (englisch) |
| [pytest Dokumentation](https://docs.pytest.org)                                                 | Vollständige Doku des meistgenutzten Python-Test-Frameworks                              |
| [unittest – Python Docs](https://docs.python.org/3/library/unittest.html)                       | Eingebautes Testframework in Python, kein separates Install nötig                        |
| [Guru99 – Software Testing Grundlagen (englisch)](https://www.guru99.com/software-testing.html) | Praxisnaher Einstiegsartikel mit vielen Beispielen (englisch)                            |

---

### 🎮 Lernkarten & Wiederholung

- [📦 Alle Lernkarten LS 8.5 – Quizlet Ordner](https://quizlet.com/user/A__J_35/folders/ls-85-softwaretests?i=20ii9u&x=1xqt)
- [🃏 Quizlet – Baustein 01: Grundlagen](https://quizlet.com/de/karteikarten/01-grundlagen-softwaretests-1179872668?i=20ii9u&x=1jqt)

> Nutze die Lernkarten zur Wiederholung nach dem Baustein –
> ideal für Spaced Repetition und IHK-Vorbereitung!

---

## Was kommt als nächstes?

In **Baustein 02 – Teststufen und Testarten** vertiefst du das V-Modell und lernst, wie
Unit-Tests, Integrationstests und Systemtests in der Praxis eingesetzt werden.
Du wirst erste echte Unit-Tests mit `pytest` schreiben und verstehen, wann welche Teststufe
die richtige Wahl ist.

---

_[➡️ Weiter zu aufgaben.md](aufgaben.md) · Bei Problemen → [Stuck Protocol](../stuck_protocol.md)_
