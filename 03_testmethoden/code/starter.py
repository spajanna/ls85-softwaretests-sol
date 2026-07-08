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

    # TODO: Füge deine Testfälle aus der Tabelle ein
    # Beispiel (TC01):
    ergebnis = authentifiziere_benutzer("admin", "geheim123")
    print(f"TC01: admin/geheim123 → {ergebnis} (erwartet: True)")

    # TC02: TODO
    ergebnis = authentifiziere_benutzer("admin", "falsch")
    print(f"TC02: admin/falsch → {ergebnis} (erwartet: False) [Falsches Passwort]")
    # TC03: TODO
    ergebnis = authentifiziere_benutzer("ab", "geheim123")
    print(f"TC03: ab/geheim123 → {ergebnis} (erwartet: False) [Username zu kurz]")
    # TC04: Gültiger Login testuser
    ergebnis = authentifiziere_benutzer("testuser", "passwort1")
    print(f"TC04: testuser/passwort1 → {ergebnis} (erwartet: True) [Zweiter gültiger Benutzer]")
    # TC05: Sonderzeichen im Username
    ergebnis = authentifiziere_benutzer("user@name", "passwort1")
    print(f"TC05: user@name/passwort1 → {ergebnis} (erwartet: False) [Sonderzeichen]")
    # TC06: Leerer Username
    ergebnis = authentifiziere_benutzer("", "geheim123")
    print(f"TC06: leer/geheim123 → {ergebnis} (erwartet: False) [Leerer Username]")
    # TC07: Passwort zu kurz
    ergebnis = authentifiziere_benutzer("admin", "kurz")
    print(f"TC07: admin/kurz → {ergebnis} (erwartet: False) [Passwort zu kurz]")
    # TC08: Username zu lang
    ergebnis = authentifiziere_benutzer("a" * 21, "geheim123")
    print(f"TC08: (21 chars)/geheim123 → {ergebnis} (erwartet: False) [Username zu lang]")
    # ...weitere Testfälle ergänzen


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

    sc_faelle = [
        (0, False, "", "UNGUELTIG"),
        (10, True, "", "HOCH"),
        (500, True, "", "EXPRESS"),
        (500, False, "", "PRIORITAET"),
    ]
    for betrag, neukunde, code, erwartet in sc_faelle:
        erg = kategorisiere_bestellung(betrag, neukunde, code)
        print(f"  Statement: ({betrag}, {neukunde}, {code!r}) -> {erg} (erwartet: {erwartet}) {'OK' if erg == erwartet else 'FEHL'}")

    bc_faelle = [
        (0, False, "", "UNGUELTIG"),
        (10, True, "", "HOCH"),
        (10, False, "", "NORMAL"),
        (10, False, "VIP2024", "HOCH"),
        (500, True, "", "EXPRESS"),
        (500, False, "", "PRIORITAET"),
    ]
    for betrag, neukunde, code, erwartet in bc_faelle:
        erg = kategorisiere_bestellung(betrag, neukunde, code)
        print(f"  Branch: ({betrag}, {neukunde}, {code!r}) -> {erg} (erwartet: {erwartet}) {'OK' if erg == erwartet else 'FEHL'}")

    # Halte fest, welche Zeilen von welchem Testfall abgedeckt werden.
