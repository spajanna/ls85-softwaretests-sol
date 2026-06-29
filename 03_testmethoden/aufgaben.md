# Baustein 03 – Testmethoden 🟡

> **Schwierigkeit:** 🟡 Anwendung  
> **Zeitrahmen:** ca. 120 Minuten  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/zeNGxav483" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 03: Testmethoden</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [*] 🟢 Ich kenne Black-Box und White-Box-Tests
- [ ] 🟡 Ich habe von diesen Begriffen gehört, bin aber unsicher
- [ ] 🔴 Diese Methoden sind mir unbekannt

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … Black-Box-Tests von White-Box-Tests unterscheiden
- 🟡 … Testfälle nach der Black-Box-Methode ohne Codekenntnis ableiten
- 🟡 … Anweisungsüberdeckung (Statement Coverage) und Zweigüberdeckung (Branch Coverage) erklären
- 🟡 … einen einfachen Kontrollflussgraphen aus Code erstellen
- 🔴 … begründen, welche Testmethode für welches Testziel am besten geeignet ist

---

## Hintergrund

Bei **Black-Box-Tests** (funktionaler Test) kennst du den Quellcode nicht – du testest nur über
Ein- und Ausgaben. Das entspricht der Perspektive des Kunden oder des Testers ohne Codekenntnis.

Bei **White-Box-Tests** (struktureller Test) kennst du den Quellcode und prüfst gezielt,
ob bestimmte Codeabschnitte durchlaufen werden. Ziel ist eine möglichst hohe **Testabdeckung** (Coverage).

**Grey-Box**: Kombination beider Ansätze – du kennst die Architektur, aber nicht alle Details.

---

## Aufgabe 0 – Grundbegriffe: Black-Box vs. White-Box 🟢

**Wiederholen und verorten:**

**a)** Erkläre in eigenen Worten (ohne Nachschauen):
- Was ist der grundlegende Unterschied zwischen Black-Box- und White-Box-Test?
- Welche Frage stellt der Tester beim Black-Box-Test?
- Welche Frage stellt der Tester beim White-Box-Test?

**b)** Ordne die folgenden Situationen zu (Black-Box oder White-Box):

| Situation | Methode |
|-----------|---------|
| Ein Kunde testet, ob er sich einloggen kann | |
| Ein Entwickler prüft, ob alle if-Zweige durchlaufen werden | |
| Ein Tester gibt verschiedene Passwörter ein und schaut, was passiert | |
| Ein Entwickler misst die Testabdeckung (Coverage) | |
| Ein externes Testteam prüft das System gegen die Spezifikation | |

**c)** Erkläre in einem Satz, warum es sinnvoll ist, beide Methoden zu kombinieren.

Trage deine Antworten in `03_antworten.md` ein.

---

## Aufgabe 1 – Black-Box-Test: Benutzerauthentifizierung 🟡

In `code/starter.py` ist eine Funktion `authentifiziere_benutzer()` implementiert.
Du darfst den Implementierungstext **nicht** lesen (falte ihn mental weg) –
arbeite nur mit der Schnittstellenbeschreibung:

**Spezifikation:**
- Eingabe: `benutzername` (str), `passwort` (str)
- Ausgabe: `True` wenn gültig, `False` wenn ungültig
- Regeln:
  - Benutzername: 3–20 Zeichen, keine Sonderzeichen außer `_`
  - Passwort: mindestens 8 Zeichen
  - Bekannte gültige Zugangsdaten: `admin` / `geheim123`

**a)** Erstelle eine Testtabelle mit mindestens 6 Black-Box-Testfällen:

| TC-Nr | Eingabe (User/PW) | Erwartete Ausgabe | Kategorie |
|-------|-------------------|------------------|-----------|
| TC01 | admin / geheim123 | True | Gültiger Login |
| TC02 | admin / falsch123 | False | Falsches Passwort |
| TC03 | unbekannt / geheim123 | False | Unbekannter Benutzer |
| TC04 | ad / geheim123 | False | Benutzername zu kurz |
| TC05 | sehrlangerbenutzername123 / geheim123 | False | Benutzername zu lang |
| TC06 | admin! / geheim123 | False | Sonderzeichen im Benutzernamen |

**b)** Führe deine Testfälle aus, indem du die Funktion in `starter.py` aufrufst.
Welche Testfälle schlagen fehl? Dokumentiere die Ergebnisse.
Alle Testfälle waren erfolgreich.

---

## Aufgabe 2 – White-Box-Test: Coverage 🟡

In `code/starter.py` findest du die Funktion `kategorisiere_bestellung()`.

**a)** Zeichne den **Kontrollflussgraphen** dieser Funktion auf Papier (oder als ASCII-Art in `03_antworten.md`).
Nummeriere alle Knoten (Anweisungen) und alle Kanten (Bedingungszweige).

**b)** **Anweisungsüberdeckung (Statement Coverage):**
Wie viele Testfälle brauchst du mindestens, um jede Anweisung einmal auszuführen?
Erstelle diese Testfälle.

**c)** **Zweigüberdeckung (Branch Coverage):**
Wie viele Testfälle brauchst du, um jeden Zweig (jedes if/else) mindestens einmal zu durchlaufen?
Warum sind das mehr als bei Statement Coverage?

---

## Aufgabe 3 – Methoden vergleichen 🟡

Fülle die Tabelle aus:

| Merkmal | Black-Box | White-Box |
|---|---|---|
| Codekenntnis notwendig? | Nein | Ja |
| Aus wessen Perspektive? | Nutzer/Kunde/Tester | Entwickler |
| Was wird geprüft? | Verhalten und Anforderungen | Code, Logik, Zweige |
| Typische Werkzeuge | Testfälle nach Spezifikation, manuelle Tests | Unit-Tests, Coverage-Tools |
| Vorteil | Testet realistisch aus Nutzersicht | Findet Fehler in der internen Logik |
| Nachteil | Interne Codefehler können übersehen werden | Nutzeranforderungen können übersehen werden |

---

## Aufgabe 4 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Entwickler hat folgende Python-Funktion geschrieben:

```python
def versandkosten(gewicht_kg: float, express: bool) -> float:
    if gewicht_kg <= 0:
        raise ValueError("Gewicht muss positiv sein")
    if express:
        if gewicht_kg <= 5:
            return 8.90
        else:
            return 14.90
    else:
        if gewicht_kg <= 5:
            return 3.90
        else:
            return 6.90
```

**(a)** Erstellen Sie einen Kontrollflussgraphen für diese Funktion. Benennen Sie alle Knoten und Kanten. *(4 Punkte)*

## (a) Kontrollflussgraph

Knoten:

1 Start  
2 if gewicht_kg <= 0  
3 raise ValueError  
4 if express  
5 if gewicht_kg <= 5  (Express-Zweig)  
6 return 8.90  
7 return 14.90  
8 if gewicht_kg <= 5  (Normal-Zweig)  
9 return 3.90  
10 return 6.90  
11 Ende  

ASCII-Graph:

1 Start
  |
  v
2 gewicht_kg <= 0?
  |-- ja  --> 3 raise ValueError --> 11 Ende
  |
  |-- nein
        v
4 express?
  |-- ja
  |     v
  |   5 gewicht_kg <= 5?
  |     |-- ja  --> 6 return 8.90 --> 11 Ende
  |     |-- nein --> 7 return 14.90 --> 11 Ende
  |
  |-- nein
        v
      8 gewicht_kg <= 5?
        |-- ja  --> 9 return 3.90 --> 11 Ende
        |-- nein --> 10 return 6.90 --> 11 Ende

Kanten:

E1: 1 -> 2  
E2: 2 -> 3  ja  
E3: 2 -> 4  nein  
E4: 3 -> 11  
E5: 4 -> 5  ja  
E6: 4 -> 8  nein  
E7: 5 -> 6  ja  
E8: 5 -> 7  nein  
E9: 6 -> 11  
E10: 7 -> 11  
E11: 8 -> 9  ja  
E12: 8 -> 10 nein  
E13: 9 -> 11  
E14: 10 -> 11  

**(b)** Wie viele Testfälle sind für eine vollständige **Zweigüberdeckung** erforderlich? Listen Sie diese auf. *(4 Punkte)*
Für vollständige Zweigüberdeckung braucht man mindestens 5 Testfälle.

TC01:
gewicht_kg = 0, express = False
Erwartet: ValueError
Deckt ab: gewicht_kg <= 0 ist True

TC02:
gewicht_kg = 3, express = True
Erwartet: 8.90
Deckt ab: express True, gewicht_kg <= 5 True

TC03:
gewicht_kg = 6, express = True
Erwartet: 14.90
Deckt ab: express True, gewicht_kg <= 5 False

TC04:
gewicht_kg = 3, express = False
Erwartet: 3.90
Deckt ab: express False, gewicht_kg <= 5 True

TC05:
gewicht_kg = 6, express = False
Erwartet: 6.90
Deckt ab: express False, gewicht_kg <= 5 False

**(c)** Welche Testfälle würden Sie zusätzlich aus **Black-Box-Sicht** (Grenzwertanalyse) ergänzen? *(2 Punkte)*
Aus Black-Box-Sicht würde ich besonders die Grenzen 0 kg und 5 kg testen:

- gewicht_kg = -1 → ValueError
- gewicht_kg = 0 → ValueError
- gewicht_kg = 0.01 → gültig
- gewicht_kg = 5.0 → noch günstiger Tarif
- gewicht_kg = 5.01 → teurer Tarif

---

## Tandem-Aufgabe 👥

**Code Review mit Testbrille:**

Person A: Schreibt eine kurze Python-Funktion (10–15 Zeilen, mindestens 2 if-Zweige)
Person B: Kennt den Code **nicht** (Black-Box) und erstellt Testfälle nur aus der Beschreibung

Dann tauscht ihr:
Person B liest den Code und prüft mit White-Box-Methode, welche Testfälle fehlen.

Diskutiert: Was hat die Black-Box-Perspektive übersehen? Was hat die White-Box-Analyse ergänzt?

**Erkläre deinem Tandempartner:** Wähle einen konkreten Fall aus deinem Berufsalltag und erkläre, wann du Black-Box- und wann White-Box-Testing einsetzen würdest – und warum. Dein Tandempartner nennt anschließend eine Ergänzung oder ein Gegenbeispiel.

---

## Active Recall 🧠

*Unterlagen zu – beantworte aus dem Gedächtnis:*

1. Was ist der fundamentale Unterschied zwischen Black-Box und White-Box?
Black-Box: Test ohne Codekenntnis, nur Verhalten von außen.
White-Box: Test mit Codekenntnis, interne Logik wird geprüft.
2. Was bedeutet 100 % Statement Coverage? Garantiert das fehlerfreie Software?
100 % Statement Coverage bedeutet: Jede Anweisung im Code wurde mindestens einmal ausgeführt.
Nein, das garantiert keine fehlerfreie Software.
3. Warum ist Branch Coverage strenger als Statement Coverage?
Branch Coverage ist strenger, weil bei jedem if sowohl der True- als auch der False-Zweig getestet werden muss.
4. In welcher Teststufe (aus Baustein 02) wird meistens White-Box-Testing eingesetzt?
Meistens bei Unit-Tests / Komponententests, oft durch Entwickler.

---

## Reflexion 🚦

- [*] 🟢 Ich kann beide Methoden anwenden und den Unterschied erklären
- [ ] 🟡 Ich verstehe die Theorie, brauche aber mehr Übung
- [ ] 🔴 Ich brauche Unterstützung bei Coverage-Konzepten

**Was nimmst du mit?**

> Ich nehme mit, dass Black-Box-Tests das Verhalten von außen prüfen und White-Box-Tests die interne Code-Logik. Beide Methoden ergänzen sich: Black-Box findet Fehler aus Nutzersicht, White-Box findet fehlende Zweige oder ungetestete Code-Stellen.

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
