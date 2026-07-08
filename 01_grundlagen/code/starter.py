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
# TODO: Der Prozentwert muss noch durch 100 geteilt werden

# Defect (fehlerhafte Stelle im Code):
# TODO: Zeile 19: rabatt = preis * prozent muss zu rabatt = preis * (prozent / 100) werden

# Failure (was der Benutzer bemerken würde):
# TODO: Das Programm liefert ein falschen (zu niedriges) Ergebnis


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    # TODO: Ersetze 'pass' durch deine Implementierung

    # Prozentwert in den eigentlichen Rabattbetrag umrechnen
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
    # Test 1: Normaler Rabatt
    print(f"Test 1 (Standard - 20% von 100€): {berechne_rabatt_korrigiert(100.0, 20.0)} (Erwartet: 80.0)")

    # Test 2: Falls ein Nutzer fälschlicherweise 0.20 statt 20 eintippt.
    print(f"Test 2 (Sonderfall - 0.2% von 100€): {berechne_rabatt_korrigiert(100.0, 0.2)} (Erwartet: 99.8)")

    # Test 3: Preiserhöhung um 20%
    print(f"Test 3 (Grenzfall - -20% von 100€): {berechne_rabatt_korrigiert(100.0, -20.0)} (Erwartet: 120.0)")


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    |    X     |           |
# | Programm mit Testdaten ausführen    |          |    X      |
# | Syntaxprüfung durch den Editor      |   X      |           |
# | Walkthroughs im Team                |   X      |           |
# | Unit-Tests laufen lassen            |          |    X      |
# | Checklisten für Codestruktur        |    X     |           |
#
# Warum reicht statisches Testen allein nicht aus?
# TODO: Deine Erklärung hier (2 Sätze)
# Statisches Testen prüft nur den Code, ohne ihn tastsächlich auszuführen. 
# Dafür verwendet man dynamische Tests, um im zusammenspiel mit echten Daten die Performance und das Verhalten im Betrieb zu testen.

# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier
# Ein Online-Shop führt ein neues Gutscheinfeld im Warenkorb ein. Ein vollständiger Test müsste alle 
# Kombinationen ausprobieren, also jedes mögliche Zeichen (Buchstaben, Zahlen, Sonderzeichen, Emojis), 
# jede Gutscheinlänge, alle Währungen, verschiedene Browser, Betriebssysteme und gleichzeitige 
# Klicks von tausenden Nutzern. Da die Anzahl der Kombinationen unendlich ist, konzentriert sich das 
# Team stattdessen auf risikobasierte Tests (z.B. gültige Codes, abgelaufene Codes, leere Eingaben).

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier
# Nach dem Release einer neuen Banking-App stellt das Support-Team fest, dass 80% aller Fehlermeldungen 
# das neu eingeführte Krypto-Modul betreffen. Die alten Module (Überweisungen, Profil) laufen fehlerfrei. 
# Gemäß dem Pareto-Prinzip (80/20-Regel) sammeln sich die meisten Defekte in wenigen, meist komplexen 
# oder hastig geschriebenen Code-Komponenten. Erfahrene Tester suchen deshalb gezielt dort nach Fehlern.

# Welches Prinzip überrascht dich? Warum?
# TODO: Deine Antwort hier
# Das Prinzip des Defect Clustering überrascht am meisten. Man würde erwarten, dass sich Fehler 
# gleichmäßig über den gesamten Code verteilen, wenn Entwickler sorgfältig arbeiten. Dass sich Bugs 
# aber so extrem in bestimmten Clustern ballen, zeigt, wie stark Softwarequalität von 
# der Komplexität eines einzelnen Moduls oder dem Zeitdruck bei dessen Entwicklung abhängt.