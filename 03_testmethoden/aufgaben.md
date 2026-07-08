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

- [ x ] 🟢 Ich kenne Black-Box und White-Box-Tests
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
  Antwort: Beim Black-Box Test ist der innere Code nicht zu sehen und man testet rein gegen die Spezifikation. Beim White-Box Test liegt der Quellcode vor und man testet die innere Struktur, Logik und Pfade des Programms.

- Welche Frage stellt der Tester beim Black-Box-Test?
  Antwort: Macht das System das, was es laut den Spezifikationen machen soll

- Welche Frage stellt der Tester beim White-Box-Test?
  Antwort: Werden alle geschriebenen Codezeilen, Zweige und Bedingungen fehlerfrei durchlaufen?

**b)** Ordne die folgenden Situationen zu (Black-Box oder White-Box):

| Situation                                                            | Methode   |
| -------------------------------------------------------------------- | --------- |
| Ein Kunde testet, ob er sich einloggen kann                          | Black-Box |
| Ein Entwickler prüft, ob alle if-Zweige durchlaufen werden           | White-Box |
| Ein Tester gibt verschiedene Passwörter ein und schaut, was passiert | Black-Box |
| Ein Entwickler misst die Testabdeckung (Coverage)                    | White-Box |
| Ein externes Testteam prüft das System gegen die Spezifikation       | Black-Box |

**c)** Erkläre in einem Satz, warum es sinnvoll ist, beide Methoden zu kombinieren.
Antwort: Die Kombination ist sinnvoll, weil Black-Box-Tests funktionale Lücken aufdecken, während White-Box-Tests ungenutzten Code oder ungetestete Fehlerpfade im Code sichtbar machen.

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

| TC-Nr                      | Eingabe (User/PW)                                 | Erwartete Ausgabe                     | Kategorie                        |
| -------------------------- | ------------------------------------------------- | ------------------------------------- | -------------------------------- |
| TC01                       | admin / geheim123                                 | True                                  | Gültiger Login                   |
| TC02                       | ad/geheim                                         | False                                 | Benutzername zu kurz (2 Zeichen) |
| TC03                       | ein_sehr_langer_benutzername_21 / geheim123 False | Benutzername zu lang (31 Zeichen)     |
| TC04 test.user / geheim123 | False                                             | Ungültigges Sonderzeichen im Username |                                  |

**b)** Führe deine Testfälle aus, indem du die Funktion in `starter.py` aufrufst.
Welche Testfälle schlagen fehl? Dokumentiere die Ergebnisse.
TC01 admin / geheim123 True True 🟢 Passed Bekannte, korrekte Kombination funktioniert.
TC02 ad / geheim123 False False 🟢 Passed Zu kurzer Name wird wie erwartet blockiert.
TC03 ein_sehr_langer_benutzername_21 / geheim123 False False 🟢 Passed Zu langer Name wird wie erwartet blockiert.
TC04 test.user / geheim123 False False 🟢 Passed Sonderzeichen (.) wird via Regex sauber abgefangen.
TC05 valid_user / 1234567 False False 🟢 Passed Zu kurzes Passwort wird wie erwartet blockiert.
TC06 valid_user / passwort123 False False 🟢 Passed Format stimmt, Benutzer existiert aber nicht.
TC07 testuser / passwort1 False True

---

## Aufgabe 2 – White-Box-Test: Coverage 🟡

In `code/starter.py` findest du die Funktion `kategorisiere_bestellung()`.

**a)** Zeichne den **Kontrollflussgraphen** dieser Funktion auf Papier (oder als ASCII-Art in `03_antworten.md`).
Nummeriere alle Knoten (Anweisungen) und alle Kanten (Bedingungszweige).
[Start]
|
v
( 1: betrag <= 0 )
/ \
 [Ja] / \ [Nein]
v v
[2: ret "UNGUELTIG"] ( 3: ist_neukunde )
/ \
 [Ja] / \ [Nein]
v v
[4: prio="HOCH"] [5: prio="NORMAL"]
\ /
\---------------/
|
v
( 6: gutschein == "VIP2024" )
/ \
 [Ja] / \ [Nein/implizit]
v v
[7: prio="HOCH"] |
\ /
\--------------------------/
|
v
( 8: betrag >= 500 )
/ \
 [Ja] / \ [Nein]
v v
( 9: prio == "HOCH" ) [12: ret prio]
/ \
 [Ja] / \ [Nein]
v v
[10: ret "EXPRESS"] [11: ret "PRIORITAET"]

**b)** **Anweisungsüberdeckung (Statement Coverage):**
Wie viele Testfälle brauchst du mindestens, um jede Anweisung einmal auszuführen?
Erstelle diese Testfälle.
Antwort: Um jede Zeile Code mindestens einmal auszuführen, reichen uns 3 Testfälle. Wir müssen sicherstellen, dass wir alle vier return-Statements und den else-Zweig treffen.

TF_SC_01 (Ungültig-Pfad): betrag = 0, ist_neukunde = False, gutscheincode = ""

Abdeckung: Knoten 1, 2. (Gibt "UNGUELTIG" zurück).

TF_SC_02 (Express-Pfad): betrag = 600, ist_neukunde = True, gutscheincode = ""

Abdeckung: Knoten 1, 3, 4, 6, 8, 9, 10. (Gibt "EXPRESS" zurück).

TF_SC_03 (Priorität-Pfad): betrag = 600, ist_neukunde = False, gutscheincode = ""

Abdeckung: Knoten 1, 3, 5, 6, 8, 9, 11. (Gibt "PRIORITAET" zurück).

**c)** **Zweigüberdeckung (Branch Coverage):**
Wie viele Testfälle brauchst du, um jeden Zweig (jedes if/else) mindestens einmal zu durchlaufen?
Warum sind das mehr als bei Statement Coverage?

Antwort: Für die vollständige Zweigüberdeckung müssen wir die fehlenden True/False-Pfade gezielt ansteuern. Wir erweitern das Set auf insgesamt 5 Testfälle:TF_BC_01: betrag = 0, ist_neukunde = False, gutscheincode = "" (Zweig 1-Ja)TF_BC_02: betrag = 600, ist_neukunde = True, gutscheincode = "" (Zweige: 1-Nein, 3-Ja, 6-Nein, 8-Ja, 9-Ja) $\rightarrow$ liefert "EXPRESS"TF_BC_03: betrag = 600, ist_neukunde = False, gutscheincode = "" (Zweige: 3-Nein, 9-Nein) $\rightarrow$ liefert "PRIORITAET"TF_BC_04 (Gutschein-Zweig True): betrag = 100, ist_neukunde = False, gutscheincode = "VIP2024" (Zweige: 6-Ja, 8-Nein) $\rightarrow$ liefert "HOCH"TF_BC_05 (Standard-Pfad komplett unten durch): betrag = 100, ist_neukunde = False, gutscheincode = "" (Zweige: 6-Nein, 8-Nein) $\rightarrow$ liefert "NORMAL"

---

## Aufgabe 3 – Methoden vergleichen 🟡

Fülle die Tabelle aus:

| Merkmal                 | Black-Box                                               | White-Box                                                                               |
| ----------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------- | --- |
| Codekenntnis notwendig? | Nein                                                    | Ja                                                                                      |
| Aus wessen Perspektive? | Anwender                                                | Entwickler                                                                              |
| Was wird geprüft?       | Funktionalität gegen Spezifikation                      | Kontrollfluss, Datenfluss, Code-Abdeckung                                               |
| Typische Werkzeuge      | Selenium, Postman, Manueller Test                       | PyTest, SonarCube                                                                       |
| Vorteil                 | Erkennt fehlende Anforderungen im Code                  | Findet toten Code, logische Fehler und ungetestete Fehlerpfade in Bedingungen           |
| Nachteil                | Pfade im Code können redundant mehrfach getestet werden | Sehr aufwendig und testet nicht, ob das System die Wünsche des Kunden überhaupt erfüllt |     |

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

**(a)** Erstellen Sie einen Kontrollflussgraphen für diese Funktion. Benennen Sie alle Knoten und Kanten. _(4 Punkte)_

[ Start ]
|
v
( K1: if gewicht_kg <= 0 )
/ \
 e1 (Ja) e2 (Nein)
/ \
 [K2: raise ValueError] ( K3: if express )
/ \
 e3 (Ja) e4 (Nein)
/ \
 ( K4: if gewicht_kg <= 5 ) ( K6: if gewicht_kg <= 5 )
/ \ / \
 e5 (Ja) e6 (Nein) e7 (Ja) e8 (Nein)
/ \ / \
 [K5: return 8.90] [K5b: return 14.90] [K7: return 3.90] [K7b: return 6.90]
\ / \ /
\------------------------/ \------------------------/
\ /
\----------------------/
|
v
[ Ende ]

Knoten-Legende (Statements):

K1: Prüfung auf ungültiges Gewicht.

K2: Auslösen der Exception (Fehlerpfad).

K3: Prüfung der Versandart (Express oder Standard).

K4 / K6: Prüfung der Gewichtsklasse (bis 5 kg oder darüber).

K5, K5b, K7, K7b: Die jeweiligen return-Anweisungen für die berechneten Versandkosten.

Kanten-Legende (Branches): e1 bis e8 beschreiben die True/False-Entscheidungen an den Verzweigungen.

**(b)** Wie viele Testfälle sind für eine vollständige **Zweigüberdeckung** erforderlich? Listen Sie diese auf. _(4 Punkte)_

TF-Nr.Eingabe gewicht_kgEingabe expressErwartete Ausgabe / EffektÜberdeckte Kanten / PfadTF_01-2.5False (oder True)ValueError ("Gewicht muss positiv sein")e1TF_023.0True8.90e2 $\rightarrow$ e3 $\rightarrow$ e5TF_0312.0True14.90e2 $\rightarrow$ e3 $\rightarrow$ e6TF_043.0False3.90e2 $\rightarrow$ e4 $\rightarrow$ e7TF_0512.0False6.90

**(c)** Welche Testfälle würden Sie zusätzlich aus **Black-Box-Sicht** (Grenzwertanalyse) ergänzen? _(2 Punkte)_

Die White-Box-Testfälle oben decken zwar den Code vollständig ab, prüfen aber nicht die exakten "Schnittkanten" der Logik. Aus Black-Box-Sicht (Grenzwertanalyse) müssen zwingend folgende 4 Testfälle ergänzt werden, um typische "Off-by-One"-Fehler (z.B. ein falsches < statt <=) zu finden:

Grenzwert 0 (Gewicht): \* Eingabe: gewicht_kg = 0.0

Ziel: Prüft, ob die Grenze exakt greift. Laut Code gewicht_kg <= 0 muss hier die Exception fliegen.

Grenzwert knapp über 0: \* Eingabe: gewicht_kg = 0.01

Ziel: Der kleinstmögliche gültige Wert. Darf keine Exception werfen.

Grenzwert exakt 5 (Gewichtsklasse): \* Eingabe: gewicht_kg = 5.0

Ziel: Prüft, ob der Grenzwert noch in der günstigeren Klasse liegt (da im Code gewicht_kg <= 5 steht, müssen hier 8.90 bzw. 3.90 herauskommen).

Grenzwert knapp über 5: \* Eingabe: gewicht_kg = 5.01

Ziel: Prüft den Sprung in die teurere Gewichtsklasse (14.90 bzw. 6.90).

---

## Tandem-Aufgabe 👥

**Code Review mit Testbrille:**

Person A: Schreibt eine kurze Python-Funktion (10–15 Zeilen, mindestens 2 if-Zweige)
Person B: Kennt den Code **nicht** (Black-Box) und erstellt Testfälle nur aus der Beschreibung

def berechne_rabatt(warenkorb_wert: float, kunden_status: str) -> float:
if warenkorb_wert < 0:
return 0.0

    if kunden_status == "VIP":
        if warenkorb_wert >= 200:
            return 0.15
        return 0.10

    # Verstecktes Osterei / Logikfehler:
    if kunden_status == "Mitarbeiter":
        return 0.25

    if warenkorb_wert >= 100:
        return 0.05

    return 0.0

Dann tauscht ihr:
Person B liest den Code und prüft mit White-Box-Methode, welche Testfälle fehlen.

Diskutiert: Was hat die Black-Box-Perspektive übersehen? Was hat die White-Box-Analyse ergänzt?
Was hat die Black-Box-Perspektive übersehen? Person B konnte den "Mitarbeiter"-Status (25 % Rabatt) und die Absicherung gegen negative Werte (warenkorb_wert < 0) unmöglich erraten, da sie nicht in der Spezifikation standen.

Was hat die White-Box-Analyse ergänzt? Sie hat den "toten" bzw. undokumentierten Code aufgedeckt (Sicherheitsrisiko!) und gezeigt, dass wir Testfälle für negative Zahlen und den geheimen Mitarbeiter-Status brauchen.

**Erkläre deinem Tandempartner:** Wähle einen konkreten Fall aus deinem Berufsalltag und erkläre, wann du Black-Box- und wann White-Box-Testing einsetzen würdest – und warum. Dein Tandempartner nennt anschließend eine Ergänzung oder ein Gegenbeispiel.
White-Box-Testing setze ich primär während der Entwicklung (Unit-Tests) ein.Ein konkretes Beispiel: Wenn ich eine komplexe Rabattlogik oder einen Algorithmus für Steuerberechnungen schreibe. Hier nutze ich Tools wie coverage.py, um sicherzustellen, dass mein Code bei Grenzwerten (z. B. exakt 0 €, exakt 100 €) keine Exceptions wirft und wirklich jede Zeile, die ich mühsam getippt habe, mindestens einmal läuft.Black-Box-Testing setze ich beim Integrationstest und Abnahmetest (UAT) ein.Ein konkretes Beispiel: Wenn die API-Schnittstelle zu einem Bezahldienstleister (wie PayPal) oder das finale Login-Formular getestet wird. Dem Kunden und mir ist in dem Moment egal, welche if-Abfragen intern in der Bibliothek laufen. Wichtig ist nur: Wenn der User die richtigen Daten eingibt, muss die Zahlung durchgehen (Input $\rightarrow$ Output).

---

## Active Recall 🧠

_Unterlagen zu – beantworte aus dem Gedächtnis:_

1. Was ist der fundamentale Unterschied zwischen Black-Box und White-Box?
   Black-Box-Test: Das System wird von außen betrachtet. Der Tester kennt den Quellcode nicht und prüft ausschließlich, ob das System bei bestimmten Eingaben die laut Spezifikation erwarteten Ausgaben liefert (Funktionstest).

White-Box-Test: Das System liegt offen. Der Tester besitzt vollständige Codekenntnis und prüft die interne Struktur, die logischen Pfade, Schleifen und Bedingungen direkt im Quellcode (Strukturtest).

2. Was bedeutet 100 % Statement Coverage? Garantiert das fehlerfreie Software?
   Bedeutung: Es bedeutet, dass im Zuge der Tests jede ausführbare Codezeile (Anweisung) mindestens einmal durchlaufen wurde.

Fehlerfreiheit? Nein, absolut nicht. \* Grund 1: Es sagt nichts darüber aus, ob die Logik korrekt ist. Wenn eine Funktion komplett am Kundenwunsch vorbeiprogrammiert wurde, kann sie trotzdem eine Abdeckung von 100 % haben.

Grund 2: Bestimmte Kombinationen von Bedingungen (z. B. leere else-Zweige) werden von der reinen Anweisungsüberdeckung ignoriert, können im echten Betrieb aber zum Absturz führen.

3. Warum ist Branch Coverage strenger als Statement Coverage?
   Weil die Zweigüberdeckung (Branch Coverage) fordert, dass jede Entscheidung (jede Kante im Kontrollflussgraphen) sowohl mit True als auch mit False durchlaufen werden muss.

Das Problem bei Statement Coverage: Wenn du eine if-Bedingung ohne dazugehörigen else-Block hast, reicht ein einziger Testfall (Bedingung ist True), um die Zeilen im if-Block zu 100 % abzudecken.

Der Unterschied bei Branch Coverage: Hier bist du gezwungen, einen zweiten Testfall zu schreiben, bei dem die Bedingung False ist, um den "leeren Vorbeiflug" (den impliziten Else-Zweig) ebenfalls zu testen. Branch Coverage schließt Statement Coverage also immer mit ein, geht aber einen Schritt weiter.

4. In welcher Teststufe (aus Baustein 02) wird meistens White-Box-Testing eingesetzt?
   Hauptsächlich in der allerersten Teststufe: dem Komponententest (auch Unit-Test oder Modultest genannt).

In dieser Phase schreiben die Entwickler selbst den Testcode (z. B. mit pytest in Python oder JUnit in Java), um ihre isolierten Funktionen, Klassen und Methoden direkt auf Herz und Nieren zu prüfen, bevor sie mit anderen Systemteilen zusammengeführt werden.

---

## Reflexion 🚦

- [ x ] 🟢 Ich kann beide Methoden anwenden und den Unterschied erklären
- [ ] 🟡 Ich verstehe die Theorie, brauche aber mehr Übung
- [ ] 🔴 Ich brauche Unterstützung bei Coverage-Konzepten

**Was nimmst du mit?**

> ---

---

_Bei Problemen → [Stuck Protocol](../stuck_protocol.md)_
