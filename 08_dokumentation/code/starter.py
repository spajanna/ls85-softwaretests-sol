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

    def test_artikel_anlegen_normalfall(self, leeres_lager):
        """
        TC-LAGER-001
        Vorbedingung: Leeres Lager
        Eingabe: Artikel A001
        Erwartet: artikel_anzahl == 1
        """
        leeres_lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99, 50))

        assert leeres_lager.artikel_anzahl() == 1

    def test_artikel_anlegen_duplikat_wirft_fehler(self, lager_mit_artikel):
        """
        TC-LAGER-002
        Vorbedingung: Lager mit Artikel A001
        Eingabe: Nochmals Artikel A001 anlegen
        Erwartet: ValueError
        """
        with pytest.raises(ValueError):
            lager_mit_artikel.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99, 50))

    def test_bestand_erhoehen_normalfall(self, lager_mit_artikel):
        """
        TC-LAGER-003
        Vorbedingung: Lager mit Artikel A001
        Eingabe: Bestand von A001 um 10 erhöhen
        Erwartet: Bestand von A001 ist 60
        """
        lager_mit_artikel.bestand_erhoehen("A001", 10)

        artikel = lager_mit_artikel.artikel_suchen("A001")
        assert artikel.bestand == 60

    def test_bestand_reduzieren_normalfall(self, lager_mit_artikel):
        """
        TC-LAGER-004
        Vorbedingung: Lager mit Artikel A001
        Eingabe: Bestand von A001 um 20 reduzieren
        Erwartet: Bestand von A001 ist 30
        """
        lager_mit_artikel.bestand_reduzieren("A001", 20)

        artikel = lager_mit_artikel.artikel_suchen("A001")
        assert artikel.bestand == 30

    def test_bestand_reduzieren_unter_null(self, lager_mit_artikel):
        """
        TC-LAGER-005
        Vorbedingung: Lager mit Artikel A002, Bestand 20
        Eingabe: Bestand von A002 um 25 reduzieren
        Erwartet: ValueError
        """
        with pytest.raises(ValueError):
            lager_mit_artikel.bestand_reduzieren("A002", 25)

    def test_artikel_suchen_vorhanden(self, lager_mit_artikel):
        """
        TC-LAGER-006
        Vorbedingung: Lager mit Artikel A001
        Eingabe: Suche nach A001
        Erwartet: Artikel wird gefunden
        """
        artikel = lager_mit_artikel.artikel_suchen("A001")

        assert artikel is not None
        assert artikel.id == "A001"
        assert artikel.name == "USB-Stick"

    def test_artikel_suchen_nicht_vorhanden(self, lager_mit_artikel):
        """
        TC-LAGER-007
        Vorbedingung: Lager ohne Artikel A999
        Eingabe: Suche nach A999
        Erwartet: None
        """
        artikel = lager_mit_artikel.artikel_suchen("A999")

        assert artikel is None

    def test_gesamtwert(self, lager_mit_artikel):
        """
        TC-LAGER-008
        Vorbedingung: Lager mit A001 und A002
        Erwartet: 50 * 9.99 + 20 * 24.99 = 999.30
        """
        assert lager_mit_artikel.gesamtwert() == pytest.approx(999.30)

    def test_kapazitaet_ueberschreitung(self):
        """
        TC-LAGER-009
        Vorbedingung: Lager mit Kapazität 10
        Eingabe: Artikel mit Bestand 11 anlegen
        Erwartet: ValueError
        """
        kleines_lager = Lager(kapazitaet=10)

        with pytest.raises(ValueError):
            kleines_lager.artikel_anlegen(Artikel("A003", "Tastatur", 49.99, 11))

    def test_artikel_unter_mindestbestand(self, lager_mit_artikel):
        """
        TC-LAGER-010
        Vorbedingung: A001 Bestand 50, A002 Bestand 20
        Eingabe: mindestbestand = 30
        Erwartet: Nur A002 wird zurückgegeben
        """
        artikel_liste = lager_mit_artikel.artikel_unter_mindestbestand(30)

        assert len(artikel_liste) == 1
        assert artikel_liste[0].id == "A002"


# ============================================================
# Aufgabe 3 – Coverage verbessern
# ============================================================

class TestLagerCoverage:

    def test_artikel_mit_negativem_preis_wirft_fehler(self):
        lager = Lager(kapazitaet=100)

        with pytest.raises(ValueError):
            lager.artikel_anlegen(Artikel("A003", "Defekt", -1.0, 5))

    def test_artikel_mit_negativem_bestand_wirft_fehler(self):
        lager = Lager(kapazitaet=100)

        with pytest.raises(ValueError):
            lager.artikel_anlegen(Artikel("A004", "Fehlerartikel", 10.0, -1))

    def test_bestand_erhoehen_unbekannter_artikel_wirft_fehler(self):
        lager = Lager(kapazitaet=100)

        with pytest.raises(ValueError):
            lager.bestand_erhoehen("A999", 10)

    def test_bestand_erhoehen_mit_null_wirft_fehler(self):
        lager = Lager(kapazitaet=100)
        lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99, 10))

        with pytest.raises(ValueError):
            lager.bestand_erhoehen("A001", 0)

    def test_bestand_reduzieren_unbekannter_artikel_wirft_fehler(self):
        lager = Lager(kapazitaet=100)

        with pytest.raises(ValueError):
            lager.bestand_reduzieren("A999", 5)

    def test_bestand_reduzieren_mit_null_wirft_fehler(self):
        lager = Lager(kapazitaet=100)
        lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99, 10))

        with pytest.raises(ValueError):
            lager.bestand_reduzieren("A001", 0)

    def test_artikel_unter_mindestbestand_keine_treffer(self):
        lager = Lager(kapazitaet=100)
        lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99, 50))

        ergebnis = lager.artikel_unter_mindestbestand(10)

        assert ergebnis == []

    def test_gesamtwert_leeres_lager(self):
        lager = Lager(kapazitaet=100)

        assert lager.gesamtwert() == 0.0


# ============================================================
# Aufgabe 5 – IHK Testbericht (Antworten als Kommentare)
# ============================================================

# (a) Erfolgsquote: TODO (x von 11 Tests erfolgreich = x%)

# (b) Unterschied FAILED vs ERROR:
# FAILED: TODO
# ERROR:  TODO

# (c) Testbericht-Tabelle:
# | TC-ID | Titel                            | Status    |
# |-------|----------------------------------|-----------|
# | TC-01 | Artikel anlegen                  | PASSED    |
# | TC-02 | Bestand erhöhen                  | PASSED    |
# | TC-03 | Bestand reduzieren unter Null    | FAILED    |
# | ...   |                                  |           |
# Abnahmebereit: TODO (Ja/Nein + Begründung)

# (d) Empfohlene Maßnahmen:
# 1. TODO
# 2. TODO
# 3. TODO
