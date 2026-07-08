# 03_antworten.md – Baustein 03: Testmethoden

## Aufgabe 0 – Grundbegriffe: Black-Box vs. White-Box

**(a)** Unterschied:
- **Black-Box**: Test ohne Codekenntnis, nur über Ein-/Ausgabe.
  Frage: „Macht die Funktion das, was sie soll?"
- **White-Box**: Test mit Codekenntnis, prüft innere Struktur.
  Frage: „Werden alle Code-Pfade durchlaufen?"

**(b)** Zuordnung:

| Situation | Methode |
|-----------|---------|
| Kunde testet Login | Black-Box |
| Entwickler prüft if-Zweige | White-Box |
| Tester gibt Passwörter ein | Black-Box |
| Entwickler misst Coverage | White-Box |
| Externes Testteam prüft gegen Spezifikation | Black-Box |

**(c)** Kombination: Black-Box findet fachliche Fehler (falsche Logik),
White-Box findet technische Lücken (ungetestete Code-Pfade).

---

## Aufgabe 2a – Kontrollflussgraph (ASCII)

```
                  [Start]
                     |
                     v
              [betrag <= 0?] --(T)--> ["UNGUELTIG"] --> [Ende]
                     |
                    (F)
                     |
                     v
              [ist_neukunde?] --(T)--> [prioritaet = "HOCH"]
                     |                      |
                    (F)                     |
                     |                      |
                     v                      |
             [prioritaet = "NORMAL"]        |
                     |                      |
                     +----------+-----------+
                                |
                                v
                   [gutschein == "VIP2024"?] --(T)--> [prioritaet = "HOCH"]
                                |
                               (F)
                                |
                                v
                         [betrag >= 500?] --(T)--> [prioritaet == "HOCH"?]
                                |                      |            |
                               (F)                    (T)          (F)
                                |                      |            |
                                v                      v            v
                        [return prioritaet]    [return "EXPRESS"] [return "PRIORITAET"]
                                |                      |            |
                                +----------+-----------+------------+
                                           |
                                           v
                                        [Ende]
```

---

## Aufgabe 3 – Methoden vergleichen

| Merkmal | Black-Box | White-Box |
|---------|-----------|-----------|
| Codekenntnis notwendig? | Nein | Ja |
| Aus wessen Perspektive? | Kunde/Anwender | Entwickler |
| Was wird geprüft? | Funktion korrekt? | Code-Struktur vollständig? |
| Typische Werkzeuge | Manuelle Tests, Äquivalenzklassen | Coverage-Tools, Debugger |
| Vorteil | Entdeckt fachliche Fehler | Findet toten Code |
| Nachteil | Lässt Code-Pfade ungetestet | Kann fachliche Fehler übersehen |

---

## Aufgabe 4 – IHK-Stil

**(a)** Kontrollflussgraph für `versandkosten()`:

```
              [Start]
                 |
                 v
       [gewicht <= 0?] --(T)--> [raise ValueError] --> [Ende]
                 |
                (F)
                 |
                 v
           [express?] --(T)--> [gewicht <= 5?] --(T)--> [return 8.90]
                 |                    |                       |
                (F)                  (F)                       |
                 |                    |                        |
                 v                    v                        |
         [gewicht <= 5?] --(T)--> [return 3.90]               |
                 |                    |                        |
                (F)                   |                        |
                 |                    |                        |
                 v                    v                        |
           [return 6.90]        [return 14.90] <----(F)--------+
```

**(b)** Für vollständige Zweigüberdeckung braucht man 4 Testfälle:

| TC | Eingabe | Erwartet | Abgedeckte Zweige |
|----|---------|----------|-------------------|
| 1 | gewicht=1, express=True | 8.90 | express:T, gewicht≤5:T |
| 2 | gewicht=10, express=True | 14.90 | express:T, gewicht≤5:F |
| 3 | gewicht=1, express=False | 3.90 | express:F, gewicht≤5:T |
| 4 | gewicht=10, express=False | 6.90 | express:F, gewicht≤5:F |

Jedes if hat genau 2 Zweige, mit 4 Tests sind alle 4×2=8 Zweig-Kombinationen abgedeckt.

**(c)** Zusätzliche Black-Box-Tests (Grenzwertanalyse):
- gewicht=0 → ValueError (untere Grenze ungültig)
- gewicht=5.0 → 8.90 (express) / 3.90 (standard) – genaue Grenze
- gewicht=5.001 → 14.90 (express) / 6.90 (standard) – knapp über Grenze
- gewicht=-0.1 → ValueError (negative Werte)
