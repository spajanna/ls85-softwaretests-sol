"""
Baustein 08 – Testdokumentation
Startvorlage – bearbeite diese Datei für deine Aufgaben.

Ausführen mit Coverage:
    pip install pytest-cov
    pytest 08_dokumentation/code/starter.py -v
    pytest 08_dokumentation/code/starter.py --cov=08_dokumentation/code/starter --cov-report=term-missing
"""

import pytest
from dataclasses import dataclass, field
from typing import Optional


# ============================================================
# Zu testendes Modul: Lagerbestandsverwaltung
# ============================================================

@dataclass
class Artikel:
    artikel_id: str
    name: str
    preis: float
    bestand: int = 0

    def __post_init__(self):
        if not self.artikel_id:
            raise ValueError("Artikel-ID darf nicht leer sein.")
        if self.preis < 0:
            raise ValueError("Preis darf nicht negativ sein.")
        if self.bestand < 0:
            raise ValueError("Bestand darf nicht negativ sein.")


class Lager:
    """Vereinfachte Lagerverwaltung."""

    def __init__(self, kapazitaet: int = 1000):
        if kapazitaet <= 0:
            raise ValueError("Kapazität muss positiv sein.")
        self._kapazitaet = kapazitaet
        self._artikel: dict[str, Artikel] = {}

    def artikel_anlegen(self, artikel: Artikel) -> None:
        """Legt einen neuen Artikel an."""
        if artikel.artikel_id in self._artikel:
            raise ValueError(f"Artikel '{artikel.artikel_id}' existiert bereits.")
        self._artikel[artikel.artikel_id] = artikel

    def bestand_erhoehen(self, artikel_id: str, menge: int) -> None:
        """Erhöht den Bestand eines Artikels."""
        if menge <= 0:
            raise ValueError("Menge muss positiv sein.")
        artikel = self._artikel.get(artikel_id)
        if artikel is None:
            raise KeyError(f"Artikel '{artikel_id}' nicht gefunden.")
        gesamtbestand = sum(a.bestand for a in self._artikel.values())
        if gesamtbestand + menge > self._kapazitaet:
            raise ValueError("Lagerkapazität würde überschritten.")
        artikel.bestand += menge

    def bestand_reduzieren(self, artikel_id: str, menge: int) -> None:
        """Reduziert den Bestand eines Artikels."""
        if menge <= 0:
            raise ValueError("Menge muss positiv sein.")
        artikel = self._artikel.get(artikel_id)
        if artikel is None:
            raise KeyError(f"Artikel '{artikel_id}' nicht gefunden.")
        if artikel.bestand < menge:
            raise ValueError(
                f"Unzureichender Bestand: {artikel.bestand} < {menge}"
            )
        artikel.bestand -= menge

    def artikel_suchen(self, artikel_id: str) -> Optional[Artikel]:
        """Gibt den Artikel zurück oder None, wenn nicht vorhanden."""
        return self._artikel.get(artikel_id)

    def gesamtwert(self) -> float:
        """Berechnet den Gesamtwert aller Artikel im Lager."""
        return round(
            sum(a.preis * a.bestand for a in self._artikel.values()), 2
        )

    def artikel_unter_mindestbestand(self, mindestbestand: int) -> list[Artikel]:
        """Gibt alle Artikel zurück, deren Bestand unter dem Minimum liegt."""
        return [a for a in self._artikel.values() if a.bestand < mindestbestand]

    def artikel_loeschen(self, artikel_id: str) -> None:
        """Löscht einen Artikel aus dem Lager."""
        if artikel_id not in self._artikel:
            raise KeyError(f"Artikel '{artikel_id}' nicht gefunden.")
        del self._artikel[artikel_id]

    @property
    def artikel_anzahl(self) -> int:
        return len(self._artikel)


# ============================================================
# Aufgabe 1 – Dokumentierte Testfälle
# ============================================================

# Testfalldokumentation als strukturierte Kommentare:
#
# TC-ID: TC-LAGER-001
# Titel: Artikel anlegen – Normalfall
# Vorbedingung: Leeres Lager vorhanden
# Testeingabe: Artikel(id="A001", name="USB-Stick", preis=9.99)
# Erwartetes Ergebnis: Artikel ist im Lager vorhanden, artikel_anzahl == 1
# Status: TODO (nach Ausführung eintragen)


class TestLagerDokumentiert:
    """
    Aufgabe 1 – Vollständig dokumentierte Testfälle.
    Für jeden Test: Lies die TC-Dokumentation und implementiere den Test.
    """

    @pytest.fixture
    def leeres_lager(self):
        return Lager(kapazitaet=500)

    @pytest.fixture
    def lager_mit_artikel(self):
        lager = Lager(kapazitaet=500)
        lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99, 50))
        lager.artikel_anlegen(Artikel("A002", "Maus", 24.99, 20))
        return lager

    # TC-LAGER-001: Artikel anlegen – Normalfall
    def test_artikel_anlegen_normalfall(self, leeres_lager):
        """
        Vorbedingung: Leeres Lager
        Eingabe: Artikel A001
        Erwartet: artikel_anzahl == 1
        """
        # TODO: Implementiere den Test
        leeres_lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99))
        assert leeres_lager.artikel_anzahl == 1

    # TC-LAGER-002: Artikel anlegen – Duplikat
    def test_artikel_anlegen_duplikat_wirft_fehler(self, lager_mit_artikel):
        """
        Vorbedingung: Lager mit Artikel A001
        Eingabe: Nochmals Artikel A001 anlegen
        Erwartet: ValueError
        """
        # TODO: Implementiere den Test
        with pytest.raises(ValueError, match="existiert bereits"):
            lager_mit_artikel.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99))

    # TC-LAGER-003: Bestand erhöhen – Normalfall
    def test_bestand_erhoehen_normalfall(self, lager_mit_artikel):
        """
        TODO: Dokumentiere und implementiere
        """
        lager_mit_artikel.bestand_erhoehen("A001", 10)
        artikel = lager_mit_artikel.artikel_suchen("A001")
        assert artikel.bestand == 60

    # TC-LAGER-004: Bestand reduzieren – Normalfall
    def test_bestand_reduzieren_normalfall(self, lager_mit_artikel):
        """TODO"""
        lager_mit_artikel.bestand_reduzieren("A001", 10)
        artikel = lager_mit_artikel.artikel_suchen("A001")
        assert artikel.bestand == 40

    # TC-LAGER-005: Bestand reduzieren – Unter Null (Grenzwert)
    def test_bestand_reduzieren_unter_null(self, lager_mit_artikel):
        """TODO"""
        with pytest.raises(ValueError, match="Bestand"):
            lager_mit_artikel.bestand_reduzieren("A001", 100)

    # TC-LAGER-006: Artikel suchen – vorhanden
    def test_artikel_suchen_vorhanden(self, lager_mit_artikel):
        """TODO"""
        artikel = lager_mit_artikel.artikel_suchen("A001")
        assert artikel is not None
        assert artikel.name == "USB-Stick"

    # TC-LAGER-007: Artikel suchen – nicht vorhanden
    def test_artikel_suchen_nicht_vorhanden(self, lager_mit_artikel):
        """
        Erwartet: None (kein Fehler, aber kein Ergebnis)
        """
        # TODO
        assert lager_mit_artikel.artikel_suchen("X999") is None

    # TC-LAGER-008: Gesamtwert berechnen
    def test_gesamtwert(self, lager_mit_artikel):
        """
        Erwartet: 50 * 9.99 + 20 * 24.99 = 499.50 + 499.80 = 999.30
        """
        # TODO
        assert lager_mit_artikel.gesamtwert() == 999.30

    # TC-LAGER-009: Kapazitätsüberschreitung
    def test_kapazitaet_ueberschreitung(self):
        """TODO: Kleines Lager anlegen und Kapazität überschreiten."""
        lager = Lager(kapazitaet=10)
        lager.artikel_anlegen(Artikel("A001", "Test", 1.0, 10))
        with pytest.raises(ValueError):
            lager.bestand_erhoehen("A001", 1)

    # TC-LAGER-010: Artikel unter Mindestbestand
    def test_artikel_unter_mindestbestand(self, lager_mit_artikel):
        """TODO: mindestbestand=30 → nur A002 (Bestand 20) sollte zurückgegeben werden."""
        niedrig = lager_mit_artikel.artikel_unter_mindestbestand(30)
        assert len(niedrig) == 1
        assert niedrig[0].artikel_id == "A002"


# ============================================================
# Aufgabe 3 – Coverage verbessern
# ============================================================

class TestLagerCoverage:
    """
    Aufgabe 3 – Schreibe Tests, die die Coverage auf >= 90% bringen.
    Führe erst den Coverage-Report aus, dann entscheide, was fehlt.
    """

    @pytest.fixture
    def lager_mit_artikel(self):
        lager = Lager(kapazitaet=500)
        lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99, 50))
        return lager

    # TODO: Ergänze Tests für noch nicht abgedeckte Zeilen/Zweige

    def test_lager_init_ungueltige_kapazitaet(self):
        with pytest.raises(ValueError, match="Kapazität"):
            Lager(kapazitaet=0)

    def test_artikel_leere_id(self):
        with pytest.raises(ValueError, match="Artikel-ID"):
            Artikel("", "Test", 1.0)

    def test_artikel_negativer_preis(self):
        with pytest.raises(ValueError, match="Preis"):
            Artikel("A001", "Test", -1.0)

    def test_artikel_negativer_bestand(self):
        with pytest.raises(ValueError, match="Bestand"):
            Artikel("A001", "Test", 1.0, -5)

    def test_bestand_erhoehen_artikel_nicht_gefunden(self):
        lager = Lager()
        with pytest.raises(KeyError, match="nicht gefunden"):
            lager.bestand_erhoehen("X999", 1)

    def test_bestand_erhoehen_ungueltige_menge(self):
        lager = Lager()
        with pytest.raises(ValueError, match="positiv"):
            lager.bestand_erhoehen("A001", 0)

    def test_bestand_reduzieren_artikel_nicht_gefunden(self):
        lager = Lager()
        with pytest.raises(KeyError, match="nicht gefunden"):
            lager.bestand_reduzieren("X999", 1)

    def test_bestand_reduzieren_ungueltige_menge(self):
        lager = Lager()
        with pytest.raises(ValueError, match="positiv"):
            lager.bestand_reduzieren("A001", 0)

    def test_artikel_loeschen_normalfall(self):
        lager = Lager()
        lager.artikel_anlegen(Artikel("A001", "Test", 1.0))
        lager.artikel_loeschen("A001")
        assert lager.artikel_anzahl == 0

    def test_artikel_loeschen_nicht_gefunden(self):
        lager = Lager()
        with pytest.raises(KeyError, match="nicht gefunden"):
            lager.artikel_loeschen("X999")

    def test_gesamtwert_leeres_lager(self):
        lager = Lager()
        assert lager.gesamtwert() == 0.0

    def test_artikel_unter_mindestbestand_keine(self, lager_mit_artikel):
        niedrig = lager_mit_artikel.artikel_unter_mindestbestand(10)
        assert len(niedrig) == 0


# ============================================================
# Aufgabe 5 – IHK Testbericht (Antworten als Kommentare)
# ============================================================

# (a) Erfolgsquote: 9 von 11 Tests erfolgreich = 81.8 %

# (b) Unterschied FAILED vs ERROR:
# FAILED: Der Test läuft durch, aber eine Assertion schlägt fehl
#         (z. B. assert ergebnis == 5, aber es kam 4).
# ERROR:  Der Test selbst stürzt mit einer Exception ab
#         (z. B. NameError, TypeError im Testcode).

# (c) Testbericht-Tabelle:
# | TC-ID | Titel                            | Status    |
# |-------|----------------------------------|-----------|
# | TC-01 | Artikel anlegen                  | PASSED    |
# | TC-02 | Bestand erhöhen                  | PASSED    |
# | TC-03 | Bestand reduzieren unter Null    | FAILED    |
# | ...   |                                  |           |
# Abnahmebereit: Nein – ein Test ist fehlgeschlagen (Bestand reduzieren
# unter Null). Der Fehler muss korrigiert werden, bevor die Abnahme
# erfolgen kann.

# (d) Empfohlene Maßnahmen:
# 1. Fehler in bestand_reduzieren beheben (Bestandsprüfung vor Reduktion)
# 2. Regressionstests für alle Bestandsänderungen ausführen
# 3. Code-Review der Korrektur durch zweiten Entwickler
