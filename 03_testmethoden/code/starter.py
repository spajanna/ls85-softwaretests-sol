"""
Baustein 03 – Testmethoden (Black-Box, White-Box, Grey-Box)
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Black-Box-Test (Implementierung absichtlich unten)
# ============================================================

def authentifiziere_benutzer(benutzername: str, passwort: str) -> bool:
    """
    Prüft, ob Benutzername und Passwort gültig sind.

    Spezifikation (für Black-Box-Tests):
    - Benutzername: 3–20 Zeichen, nur Buchstaben, Zahlen, Unterstrich
    - Passwort: mindestens 8 Zeichen
    - Bekannte gültige Kombination: 'admin' / 'geheim123'
    - Gibt True zurück wenn gültig, False wenn ungültig

    Hinweis: Schau dir die Implementierung erst NACH dem Erstellen
    deiner Black-Box-Testfälle an!
    """
    # --- Implementierung (erst nach Aufgabe 1a lesen!) ---
    import re

    if not benutzername or not passwort:
        return False

    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', benutzername):
        return False

    if len(passwort) < 8:
        return False

    gueltige_benutzer = {"admin": "geheim123", "testuser": "passwort1"}
    return gueltige_benutzer.get(benutzername) == passwort


# Aufgabe 1b) – Führe deine Testfälle hier aus:
if __name__ == "__main__":
    print("=== Aufgabe 1 – Black-Box-Tests: authentifiziere_benutzer ===")
    testcases = [
        ("TC01", "admin", "geheim123", True),
        ("TC02", "admin", "falsch123", False),
        ("TC03", "unbekannt", "geheim123", False),
        ("TC04", "ad", "geheim123", False),
        ("TC05", "sehrlangerbenutzername123", "geheim123", False),
        ("TC06", "admin!", "geheim123", False),
    ]
    # TODO: Füge deine Testfälle aus der Tabelle ein
    for tc_nr, user, pw, erwartet in testcases:
        ergebnis = authentifiziere_benutzer(user, pw)
        status = "OK" if ergebnis == erwartet else "FEHLER"
        print(f"{tc_nr}: {user}/{pw} → {ergebnis} (erwartet: {erwartet}) [{status}]")


# ============================================================
# Aufgabe 2 – White-Box-Test: Kontrollflussgraph & Coverage
# ============================================================

def kategorisiere_bestellung(betrag: float, ist_neukunde: bool, gutscheincode: str) -> str:
    """
    Kategorisiert eine Bestellung und gibt eine Priorität zurück.

    Erstelle den Kontrollflussgraphen dieser Funktion für Aufgabe 2.
    """
    if betrag <= 0:
        return "UNGUELTIG"

    if ist_neukunde:
        prioritaet = "HOCH"
    else:
        prioritaet = "NORMAL"

    if gutscheincode == "VIP2024":
        prioritaet = "HOCH"

    if betrag >= 500:
        if prioritaet == "HOCH":
            return "EXPRESS"
        else:
            return "PRIORITAET"

    return prioritaet


# Aufgabe 2b+c) – Testfälle für Statement und Branch Coverage:
if __name__ == "__main__":
    print("\n=== Aufgabe 2 – White-Box Coverage: kategorisiere_bestellung ===")

    # TODO: Ergänze Testfälle für vollständige Statement Coverage
    # TODO: Ergänze weitere Testfälle für vollständige Branch Coverage

    # Halte fest, welche Zeilen von welchem Testfall abgedeckt werden.
