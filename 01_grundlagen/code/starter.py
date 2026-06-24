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
# Der Entwickler vernwendet den faktor 20 statt 20%.

# Defect (fehlerhafte Stelle im Code):
# rabatt = preis * prozent  ist defekt

# Failure (was der Benutzer bemerken würde):
# Der User würde bemereken das der berchnete Preis falsch ist


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    rabatt = prozent / 100 * preis
    return preis - rabatt


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    print(berechne_rabatt_korrigiert(100.0, 20))
    print(berechne_rabatt_korrigiert(100.0, 0))
    print(berechne_rabatt_korrigiert(100.0, 100))
    print(berechne_rabatt_korrigiert(34.56, 50))


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    |  x       |           |
# | Programm mit Testdaten ausführen    |          |   x       |
# | Syntaxprüfung durch den Editor      |  x       |           |
# | Walkthroughs im Team                |  x       |           |
# | Unit-Tests laufen lassen            |          |   x       |
# | Checklisten für Codestruktur        |  x       |           |
#
# Warum reicht statisches Testen allein nicht aus?
# Statische Testen reicht nicht aus der Tester immer Fehler übersehen kann (besonders bei großen Projekten).
# Dynamische Tests bieten hier eine zweite Schicht der Kontrolle.


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# Eine Website hat viele mögliche Fehlerquellen (z.B. Bildformat und Sonderzeichen).
# Testen um alle möglichen Fehler zu finden kostet zu viel Zeit.

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# Die meisten Defekte findet man im User Interface. Im Backend treten fast gar keine auf.

# Welches Prinzip überrascht dich? Warum?
# Am meisten überrascht mich "5. Beware of the Pesticide Paradox" da wenn eine Software ein Update bekommt.
# Die alten Tests wieder Relevant werden