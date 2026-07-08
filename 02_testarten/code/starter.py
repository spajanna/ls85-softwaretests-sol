"""
Baustein 02 – Testarten
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""

from typing import List, Dict


# ============================================================
# Webshop-Komponenten (vereinfacht)
# ============================================================

def berechne_gesamtpreis(artikel: List[Dict], rabatt_prozent: float = 0) -> float:
    """
    Berechnet den Gesamtpreis eines Warenkorbs.

    Args:
        artikel: Liste von Dicts mit 'name', 'preis', 'menge'
        rabatt_prozent: Rabatt in Prozent (0–100)

    Returns:
        Gesamtpreis nach Rabatt, gerundet auf 2 Dezimalstellen.

    Raises:
        ValueError: Wenn rabatt_prozent außerhalb [0, 100] liegt.
    """
    if not 0 <= rabatt_prozent <= 100:
        raise ValueError(f"Rabatt muss zwischen 0 und 100 liegen, war: {rabatt_prozent}")

    summe = sum(a["preis"] * a["menge"] for a in artikel)
    rabatt = summe * (rabatt_prozent / 100)
    return round(summe - rabatt, 2)


def finde_guenstigsten_artikel(artikel: List[Dict]) -> Dict:
    """
    Gibt den Artikel mit dem niedrigsten Einzelpreis zurück.

    Raises:
        ValueError: Wenn die Liste leer ist.
    """
    if not artikel:
        raise ValueError("Warenkorb ist leer.")
    return min(artikel, key=lambda a: a["preis"])


# ============================================================
# Aufgabe 2b) – Manuelle Tests mit print()
# ============================================================

if __name__ == "__main__":
    # Testdaten
    warenkorb_normal = [
        {"name": "USB-Hub", "preis": 29.99, "menge": 1},
        {"name": "Maus", "preis": 19.99, "menge": 2},
    ]

    warenkorb_leer = []

    # TODO: Test 1 – Normaler Einkauf ohne Rabatt
    # Erwartetes Ergebnis: 69.97
    print("Test 1 – Kein Rabatt:")
    def test_normalerEinkauf():
        """Prueft Einkauf ohne Rabatt."""
        erwartet = 69.97
        ergebnis = berechne_gesamtpreis(warenkorb_normal, 0)
        assert ergebnis == erwartet, f"Erwartet: {erwartet}, Erhalten: {ergebnis}"

    print(test_normalerEinkauf())

    # TODO: Test 2 – Einkauf mit 10 % Rabatt
    # Erwartetes Ergebnis: 62.97
    print("\nTest 2 – 10 % Rabatt:")
    def test_rabattierterEinkauf():
        """Prueft Einkauf ohne Rabatt."""
        erwartet = 62.97
        ergebnis = berechne_gesamtpreis(warenkorb_normal,10)
        assert ergebnis == erwartet, f"Erwartet: {erwartet}, Erhalten: {ergebnis}"
    print(test_rabattierterEinkauf())

    # TODO: Test 3 – Leerer Warenkorb (Sonderfall)
    # Erwartetes Ergebnis: 0.0 (keine Exception!)
    print("\nTest 3 – Leerer Warenkorb:")
    def test_leererWarenkorb():
        """Prueft Einkauf ohne Rabatt."""
        erwartet = 0.0
        ergebnis = berechne_gesamtpreis(warenkorb_leer)
        assert ergebnis == erwartet, f"Erwartet: {erwartet}, Erhalten: {ergebnis}"
    print(test_leererWarenkorb())


# ============================================================
# Aufgabe 1 – Tabelle Teststufen (als Kommentar)
# ============================================================

# | Beschreibung                                           | Teststufe |
# |--------------------------------------------------------|-----------|
# | Testet einzelne Funktionen oder Methoden isoliert      |Unit       |
# | Prüft das Zusammenspiel mehrerer Module                |Integration|
# | Testet das gesamte System gegen die Anforderungen      |System     |
# | Auftraggeber prüft, ob seine Anforderungen erfüllt sind|Abnahme    |
