"""
Baustein 04 – Äquivalenzklassen & Grenzwertanalyse
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Mengenvalidierung
# ============================================================

def validiere_menge(menge) -> bool:
    if not isinstance(menge, int):
            return False

    if menge < 1:
        return False

    if menge > 999:
        return False

    return True


# ============================================================
# Aufgabe 2 – Passwortprüfung
# ============================================================

def pruefe_passwort(passwort: str) -> bool:
    if not isinstance(passwort, str):
        return False

    if len(passwort) < 8 or len(passwort) > 64:
        return False

    if not any(zeichen.isupper() for zeichen in passwort):
        return False

    if not any(zeichen.isdigit() for zeichen in passwort):
        return False

    if " " in passwort:
        return False

    return True


# ============================================================
# Aufgabe 4 – Notenberechnung (IHK-Stil)
# ============================================================

def berechne_note(punkte: int) -> int:
    if not isinstance(punkte, int) or isinstance(punkte, bool):
        raise ValueError("Punktzahl muss ganzzahlig sein")

    if punkte < 0 or punkte > 100:
        raise ValueError("Punktzahl muss zwischen 0 und 100 liegen")

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

    # Äquivalenzklassen testen:
    print("AK1:", validiere_menge(10), "erwartet: True")
    print("AK2:", validiere_menge(0), "erwartet: False")
    print("AK3:", validiere_menge(1000), "erwartet: False")
    print("AK4:", validiere_menge(2.5), "erwartet: False")

    # Grenzwerte testen:
    # TODO: Grenzwert 0, 1, 999, 1000
    print("\n=== Grenzwerte ===")
    print("GW1:", validiere_menge(0), "erwartet: False")
    print("GW2:", validiere_menge(1), "erwartet: True")
    print("GW3:", validiere_menge(998), "erwartet: True")
    print("GW4:", validiere_menge(999), "erwartet: True")
    print("GW5:", validiere_menge(1000), "erwartet: False")
    
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
        "A" * 64 + "1",  # zu lang
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
