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
# ============================================================
if __name__ == "__main__":
    print("=== Aufgabe 1 – Black-Box-Tests: authentifiziere_benutzer ===")

    black_box_tests = [
        ("TC01", "admin", "geheim123", True, "Gültiger Standard-Login"),
        ("TC02", "ad", "geheim123", False, "Username zu kurz (Grenzbereich)"),
        ("TC03", "ein_sehr_langer_benutzername_21", "geheim123", False, "Username zu lang (Grenzbereich)"),
        ("TC04", "test.user", "geheim123", False, "Ungültiges Sonderzeichen (.)"),
        ("TC05", "valid_user", "1234567", False, "Passwort zu kurz (7 Zeichen)"),
        ("TC06", "valid_user", "passwort123", False, "Gültiges Format, aber User existiert nicht"),
        ("TC07", "testuser", "passwort1", False, "Laut Spezifikation unbekannt (Sicherheitslücke?)")
    ]

    for tc, user, pw, erwartet, beschreibung in black_box_tests:
        ergebnis = authentifiziere_benutzer(user, pw)
        status = "🟢 PASSED" if ergebnis == erwartet else "🔴 FAILED"
        print(f"{tc} ({beschreibung}):")
        print(f"  Eingabe: {user} / {pw}")
        print(f"  Ergebnis: {ergebnis} (Erwartet: {erwartet}) -> {status}\n")

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

# ============================================================
# Aufgabe 2b+c) – Testfälle für Statement und Branch Coverage
# ============================================================
if __name__ == "__main__":
    print("=== Aufgabe 2 – White-Box Coverage: kategorisiere_bestellung ===")

    white_box_tests = [
        ("TF_BC_01", 0.0, False, "", "UNGUELTIG", "Zweig: Betrag <= 0 (True) -> Direktes Return"),
        ("TF_BC_02", 600.0, True, "", "EXPRESS", "Zweige: Betrag > 0, Neukunde (True), Gutschein (False), Betrag >= 500 (True), Prio HOCH (True)"),
        ("TF_BC_03", 600.0, False, "", "PRIORITAET", "Zweige: Neukunde (False), Gutschein (False), Prio HOCH (False) -> Return PRIORITAET"),
        ("TF_BC_04", 100.0, False, "VIP2024", "HOCH", "Zweige: Gutschein VIP2024 (True) überschreibt Prio, Betrag >= 500 (False) -> Fallback-Return unten"),
        ("TF_BC_05", 100.0, False, "", "NORMAL", "Zweige: Alle IF-Bedingungen sind False -> Komplett glatter Durchlauf bis zum Ende")
    ]

    for tf, betrag, neukunde, code, erwartet, ziel in white_box_tests:
        ergebnis = kategorisiere_bestellung(betrag, neukunde, code)
        status = "🟢 PASSED" if ergebnis == erwartet else "🔴 FAILED"
        print(f"{tf}: {betrag}€ | Neukunde: {neukunde} | Code: '{code}'")
        print(f"  Ergebnis: '{ergebnis}' (Erwartet: '{erwartet}') -> {status}")
        print(f"  Ziel: {ziel}\n")