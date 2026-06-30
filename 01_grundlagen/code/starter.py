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
    rabatt = preis * prozent  # mit einer eingabe von prozent = 20 wäre das rabatt = preis * 20 genommen 
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

# Error (falsche Handlung des Entwicklers):
# Der Entwickler hat seine Funktion nicht getested

# Defect (fehlerhafte Stelle im Code):
# rabatt = preis * prozent (prozent beispielsweise * 20 nicht 1.2)

# Failure (was der Benutzer bemerken würde):
# einen aufpreis stadt prozent


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    """
    rabatt = preis * (prozent / 100 + 1)
    print(preis)
    print(rabatt)
    print(preis - rabatt)
    return preis - rabatt


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    print(berechne_rabatt_korrigiert(100.0, 20))


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | 0000     | xxxx      |
# | Programm mit Testdaten ausführen    | xxxx     | 0000      |
# | Syntaxprüfung durch den Editor      | xxxx     | 0000      |
# | Walkthroughs im Team                | 0000     | xxxx      |
# | Unit-Tests laufen lassen            | xxxx     | 0000      |
# | Checklisten für Codestruktur        | xxxx     | 0000      |
#
# Warum reicht statisches Testen allein nicht aus?
# weil durch statische tests fehler die auserhalt der statischen parameter liegen nicht auffallen


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# Modul funktionirt nicht mehr aber durch mangelhafte überpfüfung schaft es der code in prod.

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# eine änderung in den shared klassen von modul 1 funktionirt in 1 bricht aber in 2

# Welches Prinzip überrascht dich? Warum?
# prinzip 2 man kann alle szenarien durchgehen es dauert halt nur unendlich viel zeit
