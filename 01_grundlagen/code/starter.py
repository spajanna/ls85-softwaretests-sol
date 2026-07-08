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
# Ein Logikfehler ist dem Entwickler unterlaufen

# Defect (fehlerhafte Stelle im Code):
# Rabatt wird falsch berechnet

# Failure (was der Benutzer bemerken würde):
# Der Wert, der zurückgegeben wird, ist viel zu groß.


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    if prozent<0.0:
        return "Prozent darf nicht negativ sein."
    elif preis<0.0:
        return "preis darf nicht negativ sein."
    elif prozent >100:
        return "Prozent muss unter 100 sein."
    rabatt = preis * prozent/100  # <-- Zeile mit Defekt
    return preis - rabatt

# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?
    print(berechne_rabatt_korrigiert(100.0, -10.0)) #Case negatives Prozent behandelt
    print(berechne_rabatt_korrigiert(100.0, 'a')) #ungültiges Zeichen in Prozent behandelt
    print(berechne_rabatt(100.0, 120))  # Zu hohe Prozentangabe behandelt



# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    |    x     |           |
# | Programm mit Testdaten ausführen    |          |     x     |
# | Syntaxprüfung durch den Editor      |    x     |           |
# | Walkthroughs im Team                |          |     x     |
# | Unit-Tests laufen lassen            |          |     x     |
# | Checklisten für Codestruktur        |    x     |           |
#
# Warum reicht statisches Testen allein nicht aus?
# TODO: Deine Erklärung hier (2 Sätze)
# Statisches Testen allein reicht nicht aus, da der Code nicht ausgeführt wird. Eher oberflächliche, strukturelle und semantische Fehler werden hier behandelt.
# Dynamisches Testen hingegen beschäftigt sich mit der Ausführung des Codes, welches die konkrete Funktionalität auf einer oder mehreren Ebenen testet.


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# Die Qualitätssicherung kann intern zu 100% abgeschlossen sein und dennoch fallen bei der Auslieferung Fehler auf.
# Gründe: Unterschiedliche oder komplexe Infrastruktur, kundenspezifische Anpassungen sind auf älteren Stand und machen Probleme, etc.

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# 80% der Fehler verstecken sich in 20% des Codes. Beim Defect Clustering werden Fehler identifiziert und klassifiziert um diese anschließend entsprechend zu behandeln.

# Welches Prinzip überrascht dich? Warum?
# Keine Fehler != gute Software, da erfahrene Entwickler von Grund auf auch richtig coden können.