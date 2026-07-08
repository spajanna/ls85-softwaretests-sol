"""
Baustein 05 – Python unittest
Startvorlage – komplett ausgearbeitet für deine Aufgaben.

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
        """Wird vor jeder Testmethode ausgeführt."""
        self.konto = Kontorechner()

    # --- Einzahlen ---

    def test_einzahlen_positiver_betrag(self):
        """Prüfe, dass eine Einzahlung von 100 den Kontostand auf 100 setzt."""
        self.konto.einzahlen(100.0)
        self.assertEqual(self.konto.kontostand, 100.0)

    def test_einzahlen_mehrere_betraege(self):
        """Prüfe, dass mehrere Einzahlungen korrekt addiert werden."""
        self.konto.einzahlen(50.0)
        self.konto.einzahlen(25.50)
        self.assertEqual(self.konto.kontostand, 75.50)

    def test_einzahlen_null_wirft_fehler(self):
        """Prüfe, dass Einzahlung von 0 einen ValueError wirft."""
        # Variante 1: Als Callable mit Argumenten
        self.assertRaises(ValueError, self.konto.einzahlen, 0)
        
        # Variante 2: Als Context Manager
        with self.assertRaises(ValueError):
            self.konto.einzahlen(0)

    def test_einzahlen_negativ_wirft_fehler(self):
        """Prüfe, dass negativer Betrag einen ValueError wirft."""
        with self.assertRaises(ValueError):
            self.konto.einzahlen(-10.0)

    # --- Abheben ---

    def test_abheben_guthaben_vorhanden(self):
        """Einzahlen und dann korrekt abheben."""
        self.konto.einzahlen(100.0)
        self.konto.abheben(40.0)
        self.assertEqual(self.konto.kontostand, 60.0)

    def test_abheben_kein_guthaben(self):
        """Abhebung ohne Guthaben wirft ValueError."""
        with self.assertRaises(ValueError):
            self.konto.abheben(10.0)

    def test_abheben_exakt_kontostand(self):
        """Abhebung des gesamten Kontostands (Grenzfall)."""
        self.konto.einzahlen(50.0)
        self.konto.abheben(50.0)
        self.assertEqual(self.konto.kontostand, 0.0)

    def test_kontostand_anfangswert(self):
        """Neues Konto hat Kontostand 0."""
        self.assertEqual(self.konto.kontostand, 0.0)


# ============================================================
# Aufgabe 2 – Einkaufsliste implementieren und testen
# ============================================================

class Einkaufsliste:
    """Implementierung des Einkaufslisten-Managers."""

    def __init__(self):
        self._artikel = []

    def hinzufuegen(self, artikel: str) -> None:
        """Fügt einen Artikel hinzu."""
        if not artikel or not isinstance(artikel, str):
            raise ValueError("Artikelname muss ein gültiger Text sein.")
        self._artikel.append(artikel)

    def entfernen(self, artikel: str) -> None:
        """
        Entfernt einen Artikel.
        Raises:
            ValueError: Wenn der Artikel nicht vorhanden ist.
        """
        if artikel not in self._artikel:
            raise ValueError(f"Artikel '{artikel}' ist nicht auf der Liste.")
        self._artikel.remove(artikel)

    def anzeigen(self) -> list:
        """Gibt alle Artikel als Liste zurück."""
        return self._artikel.copy()

    def ist_leer(self) -> bool:
        """Gibt True zurück, wenn die Liste leer ist."""
        return len(self._artikel) == 0

    def anzahl(self) -> int:
        """Gibt die Anzahl der Artikel zurück."""
        return len(self._artikel)


class TestEinkaufsliste(unittest.TestCase):

    def setUp(self):
        """Erstelle eine neue Einkaufsliste vor jedem Test."""
        self.liste = Einkaufsliste()

    def tearDown(self):
        """Wird nach jeder Testmethode ausgeführt."""
        print(f"  [tearDown] Test abgeschlossen.")

    def test_neue_liste_ist_leer(self):
        """Eine frisch erstellte Liste muss leer sein."""
        self.assertTrue(self.liste.ist_leer())
        self.assertEqual(self.liste.anzahl(), 0)

    def test_artikel_hinzufuegen(self):
        """Hinzugefügte Artikel müssen in der Liste erscheinen."""
        self.liste.hinzufuegen("Milch")
        self.assertIn("Milch", self.liste.anzeigen())
        self.assertFalse(self.liste.ist_leer())

    def test_artikel_entfernen(self):
        """Artikel müssen nach dem Entfernen aus der Liste verschwinden."""
        self.liste.hinzufuegen("Brot")
        self.liste.entfernen("Brot")
        self.assertNotIn("Brot", self.liste.anzeigen())
        self.assertTrue(self.liste.ist_leer())

    def test_nicht_vorhandenen_artikel_entfernen_wirft_fehler(self):
        """Das Entfernen unvorhandener Artikel muss fehlschlagen."""
        with self.assertRaises(ValueError):
            self.liste.entfernen("Käse")

    def test_anzahl_nach_mehreren_operationen(self):
        """Die Artikelanzahl muss nach diversen Operationen stimmen."""
        self.liste.hinzufuegen("Äpfel")
        self.liste.hinzufuegen("Bananen")
        self.liste.hinzufuegen("Birnen")
        self.liste.entfernen("Bananen")
        self.assertEqual(self.liste.anzahl(), 2)


# ============================================================
# Aufgabe 3 – assertRaises Varianten
# ============================================================

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

    def test_note_1_bei_100_punkten(self):
        self.assertEqual(berechne_note(100), 1)

    def test_note_6_bei_0_punkten(self):
        self.assertEqual(berechne_note(0), 6)

    def test_ungueltige_punkte_negativ(self):
        """Teste mit -1 – nutze assertRaises als Context Manager."""
        # Variante 2 (with self.assertRaises(...))
        with self.assertRaises(ValueError):
            berechne_note(-1)

    def test_ungueltige_punkte_zu_hoch(self):
        """Teste mit 101 – nutze assertRaises als Callable."""
        # Variante 1 (self.assertRaises(ValueError, berechne_note, 101))
        self.assertRaises(ValueError, berechne_note, 101)

    def test_grenzwert_note_2(self):
        """Teste Grenzwert 91 (letzte Note 2) und 92 (erste Note 1)."""
        self.assertEqual(berechne_note(91), 2)
        self.assertEqual(berechne_note(92), 1)


# ============================================================
# Einstiegspunkt
# ============================================================

if __name__ == "__main__":
    unittest.main(verbosity=2)