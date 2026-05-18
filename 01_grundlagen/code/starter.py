"""
Baustein 01 – Grundlagen der Softwaretests
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Fehlerhafte Funktion
# ============================================================
# berechne_rabatt ist hier nicht ganz richtig. berechne_rabatt_preis wäre sinnvoller
def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Beispiel:
        berechne_rabatt(100.0, 20) soll 80.0 zurückgeben.
    """
    # Hier ist ein Defekt eingebaut – findest du ihn?
    # rabatt = preis * (prozent/100)
    rabatt = preis * prozent  # <-- Zeile mit Defekt
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

# Error (falsche Handlung des Entwicklers):
# TODO: Deine Antwort hier

# Defect (fehlerhafte Stelle im Code):
# TODO: Deine Antwort hier

# Failure (was der Benutzer bemerken würde):
# TODO: Deine Antwort hier


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """

    rabatt= float(preis) *(float(prozent)/100)
    if rabatt < 0:
        return 0
    return preis-rabatt


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet
    print(berechne_rabatt(100.0, 20))
    print("\n=== Test: berechne_rabatt_korrigiert ===")
    print(berechne_rabatt_korrigiert(100.0, -20.0)) # 0 als Ausgabe erwartet, weil ungültig
    print(berechne_rabatt_korrigiert("a", "b"))   # Keine Ausgabe erwartet
    print(berechne_rabatt(100, 200))   # 0 als Ausgabe erwartet, weil ungültig


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | TODO     | TODO      |
# | Programm mit Testdaten ausführen    | TODO     | TODO      |
# | Syntaxprüfung durch den Editor      | TODO     | TODO      |
# | Walkthroughs im Team                | TODO     | TODO      |
# | Unit-Tests laufen lassen            | TODO     | TODO      |
# | Checklisten für Codestruktur        | TODO     | TODO      |
#
# Warum reicht statisches Testen allein nicht aus?
# TODO: Deine Erklärung hier (2 Sätze)


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier

# Welches Prinzip überrascht dich? Warum?
# TODO: Deine Antwort hier
