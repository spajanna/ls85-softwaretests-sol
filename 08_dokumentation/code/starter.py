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

    @pytest.fixture
    def leeres_lager(self):
        return Lager(kapazitaet=500)

    @pytest.fixture
    def lager_mit_artikel(self):
        lager = Lager(kapazitaet=500)
        lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99, 50))
        lager.artikel_anlegen(Artikel("A002", "Maus", 24.99, 20))
        return lager

    def test_artikel_anlegen_normalfall(self, leeres_lager):
        leeres_lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99))
        assert leeres_lager.artikel_anzahl == 1

    def test_artikel_anlegen_duplikat_wirft_fehler(self, lager_mit_artikel):
        with pytest.raises(ValueError):
            lager_mit_artikel.artikel_anlegen(
                Artikel("A001", "USB-Stick", 9.99, 10)
            )

    def test_bestand_erhoehen_normalfall(self, lager_mit_artikel):
        lager_mit_artikel.bestand_erhoehen("A001", 10)
        assert lager_mit_artikel.artikel_suchen("A001").bestand == 60

    def test_bestand_reduzieren_normalfall(self, lager_mit_artikel):
        lager_mit_artikel.bestand_reduzieren("A001", 10)
        assert lager_mit_artikel.artikel_suchen("A001").bestand == 40

    def test_bestand_reduzieren_unter_null(self, lager_mit_artikel):
        with pytest.raises(ValueError):
            lager_mit_artikel.bestand_reduzieren("A001", 999)

    def test_artikel_suchen_vorhanden(self, lager_mit_artikel):
        assert lager_mit_artikel.artikel_suchen("A001") is not None

    def test_artikel_suchen_nicht_vorhanden(self, lager_mit_artikel):
        assert lager_mit_artikel.artikel_suchen("XXX") is None

    def test_gesamtwert(self, lager_mit_artikel):
        assert lager_mit_artikel.gesamtwert() == 999.3

    def test_kapazitaet_ueberschreitung(self):
        lager = Lager(kapazitaet=10)
        lager.artikel_anlegen(Artikel("A1", "Test", 1.0, 10))
        with pytest.raises(ValueError):
            lager.bestand_erhoehen("A1", 1)

    def test_artikel_unter_mindestbestand(self, lager_mit_artikel):
        result = lager_mit_artikel.artikel_unter_mindestbestand(30)
        assert len(result) == 1
        assert result[0].artikel_id == "A002"

# ============================================================
# Aufgabe 3 – Coverage verbessern
# ============================================================

class TestLagerCoverage:

    def test_artikel_loeschen(self):
        lager = Lager()
        lager.artikel_anlegen(Artikel("A1", "Test", 1.0))
        lager.artikel_loeschen("A1")
        assert lager.artikel_anzahl == 0

    def test_artikel_loeschen_fehler(self):
        lager = Lager()
        with pytest.raises(KeyError):
            lager.artikel_loeschen("X")

    def test_bestand_erhoehen_fehler_menge(self):
        lager = Lager()
        lager.artikel_anlegen(Artikel("A1", "Test", 1.0))
        with pytest.raises(ValueError):
            lager.bestand_erhoehen("A1", 0)

    def test_bestand_reduzieren_fehler_key(self):
        lager = Lager()
        with pytest.raises(KeyError):
            lager.bestand_reduzieren("X", 1)


# ============================================================
# Aufgabe 5 – IHK Testbericht (Antworten als Kommentare)
# ============================================================

# (a) Erfolgsquote: TODO (x von 11 Tests erfolgreich = x%)
#11 Tests insgesamt
# (b) Unterschied FAILED vs ERROR:
#FAILED: Assertion falsch
#ERROR: Test bricht durch Exception vorher ab 

# (c) Testbericht-Tabelle:
# | TC-ID | Titel                            | Status    |
# |-------|----------------------------------|-----------|
# | TC-01 | Artikel anlegen                  | PASSED    |
# | TC-02 | Bestand erhöhen                  | PASSED    |
# | TC-03 | Bestand reduzieren unter Null    | FAILED    |
# | ...   |                                  |           |
# Abnahmebereit: TODO (Ja/Nein + Begründung)

#| TC    | Status |
#| ----- | ------ |
#| TC-01 | PASSED |
#| TC-02 | PASSED |
#| TC-03 | FAILED |
#| TC-04 | PASSED |
#| TC-05 | PASSED |


# (d) Empfohlene Maßnahmen:
#FAILED-Test analysieren und Logik korrigieren
#Fehlerquelle im Bestandssystem prüfen
#Regressionstests erweitern
#erneuter vollständiger Testlauf
