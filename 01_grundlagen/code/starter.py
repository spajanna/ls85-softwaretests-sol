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
# Das Ergebnis wird falsch berechnet.

# Defect (fehlerhafte Stelle im Code):
# Nach der Multiplikation muss es durch 100 geteilt werden, damit der Rabatt korrekt berechnet wird.

# Failure (was der Benutzer bemerken würde):
# Zu hohen Rabatt, z.B. 2000.0 statt 20.0 bei 20% von 100.0.


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    rabatt = preis * prozent / 100
    return preis - rabatt


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    # Test 1: 20% von 100.0
    print(berechne_rabatt_korrigiert(100.0, 20))  # Erwartet: 80.0
    # Test 2: 50% von 200.0
    print(berechne_rabatt_korrigiert(200.0, 50))  # Erwartet: 100.0
    # Test 3: 10% von 50.0
    print(berechne_rabatt_korrigiert(50.0, 10))  # Erwartet: 45.0


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | ++++     | TODO      |
# | Programm mit Testdaten ausführen    | TODO     | ++++      |
# | Syntaxprüfung durch den Editor      | ++++     | TODO      |
# | Walkthroughs im Team                | ++++     | TODO      |
# | Unit-Tests laufen lassen            | TODO     | ++++      |
# | Checklisten für Codestruktur        | ++++     | TODO      |
#
# Warum reicht statisches Testen allein nicht aus?
# Es ist unmöglich, alle möglichen Ausführungen eines Programms zu testen.
# Dynamisches Testen ist notwendig, um das Verhalten des Programms unter realen Bedingungen zu überprüfen.


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# Bei frontend-Entwicklung könnte es unzählige Kombinationen von Browsern, Betriebssystemen und Bildschirmgrößen geben, die getestet werden müssten. Es ist unmöglich, alle Kombinationen abzudecken.

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# Je schwieriger ein Bereich des Codes ist, desto mehr Fehler finden sich darin.

# Welches Prinzip überrascht dich? Warum?
# 4 – Defect Clustering überrascht mich, weil es zeigt, dass Fehler nicht gleichmäßig im Code verteilt sind, sondern sich in bestimmten Bereichen konzentrieren können. Das bedeutet, dass es besonders wichtig ist, diese Bereiche sorgfältig zu testen und zu überprüfen.
