"""
Baustein 01 – Grundlagen der Softwaretests
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Fehlerhafte Funktion
# ============================================================

def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Beispiel:
        berechne_rabatt(100.0, 20) soll 80.0 zurückgeben.
    """
    # Hier ist ein Defekt eingebaut – findest du ihn?
    rabatt = preis * prozent  # <-- Zeile mit Defekt
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

# Error (falsche Handlung des Entwicklers):
# Der Entwickler hat vergessen, durch 100 zu teilen. Die Formel
# "preis * prozent" müsste korrekt "preis * (prozent / 100)" lauten.

# Defect (fehlerhafte Stelle im Code):
# Zeile 19: rabatt = preis * prozent
# Die Division durch 100 fehlt; der Rabatt wird daher als direkter
# Faktor statt als prozentualer Anteil berechnet.

# Failure (was der Benutzer bemerken würde):
# Bei berechne_rabatt(100, 20) erwartet der Benutzer 80.00,
# erhält aber -1900.00. Die Funktion liefert offensichtlich falsche Werte.


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    rabatt = preis * (prozent / 100)
    return preis - rabatt


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    # TODO: Deine Tests hier
    print(f"Test 1: 100 Euro, 20% Rabatt -> {berechne_rabatt_korrigiert(100.0, 20)} (erwartet: 80.0)")
    print(f"Test 2: 50 Euro, 0% Rabatt -> {berechne_rabatt_korrigiert(50.0, 0)} (erwartet: 50.0)")
    print(f"Test 3: 29.99 Euro, 10% Rabatt -> {berechne_rabatt_korrigiert(29.99, 10)} (erwartet: 26.991)")


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | x        |           |
# | Programm mit Testdaten ausführen    |          | x         |
# | Syntaxprüfung durch den Editor      | x        |           |
# | Walkthroughs im Team                | x        |           |
# | Unit-Tests laufen lassen            |          | x         |
# | Checklisten für Codestruktur        | x        |           |
#
# Warum reicht statisches Testen allein nicht aus?
# Statisches Testen findet nur formale/logische Fehler im Code, aber nicht
# Laufzeitfehler oder falsches Verhalten bei realen Eingaben. Erst dynamisches
# Testen zeigt, ob die Software tatsächlich korrekt arbeitet.


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# Eine Login-Funktion mit 3 Feldern (User, PW, Captcha) hat
# unendlich viele Eingabekombinationen. Man kann nie alle testen –
# man muss eine repräsentative Auswahl treffen (z. B. Äquivalenzklassen).

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# In einer Webapp treten 80 % der Fehler im Zahlungsmodul auf,
# während die Profilseite fast fehlerfrei ist. Man testet daher das
# Zahlungsmodul besonders intensiv.

# Welches Prinzip überrascht dich? Warum?
# Prinzip 7 („Keine Fehler" = „Gutes System"), weil man intuitiv annimmt,
# dass eine fehlerfrei laufende Software auch gut ist – dabei kann sie
# trotzdem die Benutzeranforderungen vollständig verfehlen.
