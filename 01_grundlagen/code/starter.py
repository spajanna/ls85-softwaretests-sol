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
# TODO: Die Rechnung ist falsch, es feht das Teilen durch Hundert

# Defect (fehlerhafte Stelle im Code):
# TODO:Die Rechnung, zeile 19

# Failure (was der Benutzer bemerken würde):
# TODO: Es würde eine Zahl im Minus raus kommen


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    rabatt = preis * prozent / 100
    return preis - rabatt  # TODO: Ersetze 'pass' durch deine Implementierung


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    # TODO: Deine Tests hier
    print(berechne_rabatt_korrigiert(100.0, 20))
    


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | X        |           |
# | Programm mit Testdaten ausführen    |          | X         |
# | Syntaxprüfung durch den Editor      | X        |           |
# | Walkthroughs im Team                | X        |           |
# | Unit-Tests laufen lassen            |          | X         |
# | Checklisten für Codestruktur        | X        |           |
#
# Warum reicht statisches Testen allein nicht aus?
# TODO: Es können immer Sachen übersehen werden, die dann aber zum Beispiel beim Starten des Programms auffallen. 


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# TODO: Wenn man ein großes Projekt hat, würde es ziemlich lange dauern jede einzelne Funktion zu testen.

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# TODO: Viele Fehler bauen aufeinander auf und wenn man von unten anfängt macht das oft keinen sinn.

# Welches Prinzip überrascht dich? Warum?
# TODO: Nummer 4. Weil war mir nicht klar. 
