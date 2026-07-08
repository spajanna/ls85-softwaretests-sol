"""
Baustein 04 – Äquivalenzklassen & Grenzwertanalyse
Startvorlage – bearbeitet und einsatzbereit.
"""


# ============================================================
# Aufgabe 1 – Mengenvalidierung
# ============================================================

def validiere_menge(menge) -> bool:
    """
    Prüft, ob eine Bestellmenge gültig ist.

    Regeln:
    - Typ: ganzzahlig (bool wird explizit ausgeschlossen, da isinstance(True, int) == True ist)
    - Minimum: 1
    - Maximum: 999

    Returns:
        True wenn gültig, False wenn ungültig.
    """
    # Prüfen, ob der Typ exakt ein Integer ist
    if type(menge) is not int:
        return False
        
    # Prüfen, ob die Menge innerhalb der Grenzwerte liegt
    if menge >= 1 and menge <= 999:
        return True
        
    return False


# ============================================================
# Aufgabe 2 – Passwortprüfung
# ============================================================

def pruefe_passwort(passwort: str) -> bool:
    """
    Prüft, ob ein Passwort den Anforderungen entspricht.

    Regeln:
    - Länge: 8–64 Zeichen
    - Mindestens ein Großbuchstabe
    - Mindestens eine Ziffer
    - Keine Leerzeichen

    Returns:
        True wenn gültig, False wenn ungültig.
    """
    # Typ-Check zur Sicherheit
    if not isinstance(passwort, str):
        return False

    # Regel: Länge 8-64 Zeichen
    if len(passwort) < 8 or len(passwort) > 64:
        return False

    # Regel: Keine Leerzeichen
    if ' ' in passwort:
        return False

    # Regeln für Zeichenbestandteile prüfen
    hat_grossbuchstabe = any(char.isupper() for char in passwort)
    hat_ziffer = any(char.isdigit() for char in passwort)

    return hat_grossbuchstabe and hat_ziffer


# ============================================================
# Aufgabe 4 – Notenberechnung (IHK-Stil)
# ============================================================

def berechne_note(punkte: int) -> int:
    """
    Gibt die Note (1–6) für eine Punktzahl zurück.

    Skala:
        92–100 → 1
        81–91  → 2
        67–80  → 3
        50–66  → 4
        30–49  → 5
        0–29   → 6

    Raises:
        ValueError: Wenn punkte außerhalb [0, 100] liegt oder kein Integer ist.
    """
    if type(punkte) is not int or punkte < 0 or punkte > 100:
        raise ValueError("Punktzahl muss eine Ganzzahl zwischen 0 und 100 sein.")

    if punkte >= 92:
        return 1
    elif punkte >= 81:
        return 2
    elif punkte >= 67:
        return 3
    elif punkte >= 50:
        return 4
    elif punkte >= 30:
        return 5
    else:
        return 6


# ============================================================
# Tests (manuelle Überprüfung)
# ============================================================

if __name__ == "__main__":

    # --- Aufgabe 1: validiere_menge ---
    print("=== Aufgabe 1: validiere_menge ===")

    # Die Testschleife deckt bereits alle geforderten Äquivalenzklassen 
    # und kritischen Grenzwerte (0, 1, 999, 1000) sowie den Typfehler ab:
    for testfall in [0, 1, 500, 999, 1000, -1, "abc"]:
        try:
            ergebnis = validiere_menge(testfall)
            print(f"  validiere_menge({testfall!r}) → {ergebnis}")
        except Exception as e:
            print(f"  validiere_menge({testfall!r}) → Exception: {e}")

    # --- Aufgabe 2: pruefe_passwort ---
    print("\n=== Aufgabe 2: pruefe_passwort ===")
    testpasswoerter = [
        "Abc12345",       # gültig
        "abc12345",       # kein Großbuchstabe
        "ABCDEFGH",       # keine Ziffer
        "Abc 1234",       # Leerzeichen
        "Ab1",            # zu kurz
        "A" * 64 + "1",   # zu lang
    ]
    for pw in testpasswoerter:
        print(f"  pruefe_passwort({pw!r}) → {pruefe_passwort(pw)}")

    # --- Aufgabe 4: berechne_note ---
    print("\n=== Aufgabe 4: berechne_note ===")
    # Alle Notengrenzen testen (Grenzwertanalyse):
    grenzwerte = [0, 29, 30, 49, 50, 66, 67, 80, 81, 91, 92, 100]
    for p in grenzwerte:
        try:
            print(f"  berechne_note({p}) → {berechne_note(p)}")
        except ValueError as e:
            print(f"  berechne_note({p}) → ValueError: {e}")

    # Ungültige Werte:
    for p in [-1, 101]:
        try:
            print(f"  berechne_note({p}) → {berechne_note(p)}")
        except ValueError as e:
            print(f"  berechne_note({p}) → ValueError: {e}")