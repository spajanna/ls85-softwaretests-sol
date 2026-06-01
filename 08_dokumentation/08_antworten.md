# 08_antworten.md – Baustein 08: Testdokumentation

## Aufgabe 0 – Testplan, Testprotokoll, Testbericht

| Aussage | Kategorie |
|---------|-----------|
| Definiert Testziele, -umfang und -zeitplan | Testplan |
| Enthält Datum, Testergebnis und Tester-Name | Testprotokoll |
| Fasst Ergebnisse zusammen und gibt Abnahmeempfehlung | Testbericht |
| Wird vor dem Testen erstellt | Testplan |
| Wird während des Testens ausgefüllt | Testprotokoll |
| Enthält Metriken (Coverage, Fehlerquote) | Testbericht |

Warum Dokumentation notwendig ist:
- Nachvollziehbarkeit: Was wurde getestet? Mit welchem Ergebnis?
- Haftung: Bei Fehlern im Produktivbetrieb kann nachgewiesen werden,
  welche Tests durchgeführt wurden.
- Wiederholbarkeit: Regressionstests können später exakt reproduziert werden.
- Kommunikation: Der Auftraggeber sieht, ob die Software abnahmebereit ist.

---

## Aufgabe 1b – Testausführung

Alle 10 Testfälle wurden implementiert und ausgeführt:
- TC-LAGER-001 bis TC-LAGER-010: alle **PASSED**

---

## Aufgabe 3d – 100 % Coverage = Qualität?

Nein. 100 % Coverage bedeutet nur, dass jede Codezeile mindestens einmal
ausgeführt wurde. Es sagt nichts aus über:
- Vollständigkeit der Testfälle (sind alle Randfälle abgedeckt?)
- Korrektheit der Logik (ein Test kann grün sein, obwohl die Implementierung falsch ist)
- Performance, Sicherheit, Benutzerfreundlichkeit

Coverage ist ein Werkzeug, kein Qualitätsziel.
