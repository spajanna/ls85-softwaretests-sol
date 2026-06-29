"""
Baustein 05 – Python unittest
Startvorlage – bearbeite diese Datei für deine Aufgaben.

Ausführen:
    python -m unittest 05_unittest/code/starter.py -v
"""

import unittest


# ============================================================
# Zu testende Klasse: Kontorechner
# ============================================================

class Kontorechner:
    """Vereinfachter Kontostand-Manager."""

    def __init__(self):
        self._kontostand = 0.0

    @property
    def kontostand(self) -> float:
        return self._kontostand

    def einzahlen(self, betrag: float) -> None:
        """
        Zahlt einen Betrag ein.

        Raises:
            ValueError: Wenn betrag <= 0.
        """
        if betrag <= 0:
            raise ValueError(f"Einzahlung muss positiv sein, war: {betrag}")
        self._kontostand += betrag

    def abheben(self, betrag: float) -> None:
        """
        Hebt einen Betrag ab.

        Raises:
            ValueError: Wenn betrag <= 0 oder Kontostand unzureichend.
        """
        if betrag <= 0:
            raise ValueError(f"Abhebungsbetrag muss positiv sein, war: {betrag}")
        if betrag > self._kontostand:
            raise ValueError(
                f"Unzureichendes Guthaben: {self._kontostand:.2f} < {betrag:.2f}"
            )
        self._kontostand -= betrag


# ============================================================
# Aufgabe 1 – Testklasse für Kontorechner
# ============================================================

class TestKontorechner(unittest.TestCase):

    def setUp(self):
        self.konto = Kontorechner()

    def test_einzahlen_positiver_betrag(self):
        self.konto.einzahlen(100)
        self.assertEqual(self.konto.kontostand, 100)

    def test_einzahlen_mehrere_betraege(self):
        self.konto.einzahlen(50)
        self.konto.einzahlen(25)
        self.assertEqual(self.konto.kontostand, 75)

    def test_einzahlen_null_wirft_fehler(self):
        with self.assertRaises(ValueError):
            self.konto.einzahlen(0)

    def test_einzahlen_negativ_wirft_fehler(self):
        with self.assertRaises(ValueError):
            self.konto.einzahlen(-10)

    def test_abheben_guthaben_vorhanden(self):
        self.konto.einzahlen(100)
        self.konto.abheben(40)
        self.assertEqual(self.konto.kontostand, 60)

    def test_abheben_kein_guthaben(self):
        with self.assertRaises(ValueError):
            self.konto.abheben(10)

    def test_abheben_exakt_kontostand(self):
        self.konto.einzahlen(50)
        self.konto.abheben(50)
        self.assertEqual(self.konto.kontostand, 0)

    def test_kontostand_anfangswert(self):
        self.assertEqual(self.konto.kontostand, 0)



# ============================================================
# Aufgabe 2 – Einkaufsliste implementieren und testen
# ============================================================

class Einkaufsliste:

    def __init__(self):
        self._artikel = []

    def hinzufuegen(self, artikel: str) -> None:
        self._artikel.append(artikel)

    def entfernen(self, artikel: str) -> None:
        if artikel not in self._artikel:
            raise ValueError("Artikel nicht vorhanden")
        self._artikel.remove(artikel)

    def anzeigen(self) -> list:
        return self._artikel.copy()

    def ist_leer(self) -> bool:
        return len(self._artikel) == 0

    def anzahl(self) -> int:
        return len(self._artikel)

class TestEinkaufsliste(unittest.TestCase):

    def setUp(self):
        self.liste = Einkaufsliste()

    def test_neue_liste_ist_leer(self):
        self.assertTrue(self.liste.ist_leer())

    def test_artikel_hinzufuegen(self):
        self.liste.hinzufuegen("Apfel")
        self.assertIn("Apfel", self.liste.anzeigen())

    def test_artikel_entfernen(self):
        self.liste.hinzufuegen("Milch")
        self.liste.entfernen("Milch")
        self.assertNotIn("Milch", self.liste.anzeigen())

    def test_nicht_vorhandenen_artikel_entfernen_wirft_fehler(self):
        with self.assertRaises(ValueError):
            self.liste.entfernen("Brot")

    def test_anzahl_nach_mehreren_operationen(self):
        self.liste.hinzufuegen("A")
        self.liste.hinzufuegen("B")
        self.liste.entfernen("A")
        self.assertEqual(self.liste.anzahl(), 1)

    def tearDown(self):
        print("Test fertig")




# ============================================================
# Aufgabe 3 – assertRaises Varianten
# ============================================================

# Importiere berechne_note aus Baustein 04 oder kopiere die Funktion hier:

def berechne_note(punkte: int) -> int:
    """Notenberechnung aus Baustein 04 – hier für Testzwecke."""
    if not isinstance(punkte, int) or punkte < 0 or punkte > 100:
        raise ValueError(f"Punkte müssen zwischen 0 und 100 liegen, war: {punkte}")
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


class TestBerechneNote(unittest.TestCase):

    def test_ungueltige_punkte_negativ(self):
        with self.assertRaises(ValueError):
            berechne_note(-1)

    def test_ungueltige_punkte_zu_hoch(self):
        self.assertRaises(ValueError, berechne_note, 101)

    def test_grenzwert_note_2(self):
        self.assertEqual(berechne_note(91), 2)
        self.assertEqual(berechne_note(92), 1)



# ============================================================
# Einstiegspunkt
# ============================================================

if __name__ == "__main__":
    unittest.main(verbosity=2)
