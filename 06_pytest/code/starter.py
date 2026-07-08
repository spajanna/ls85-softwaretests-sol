"""
Baustein 06 – pytest
Startvorlage – komplett bearbeitet und einsatzbereit.

Installation:
    pip install pytest

Ausführen:
    pytest 06_pytest/code/starter.py -v
    pytest 06_pytest/code/ -v --tb=short
"""

import pytest


# ============================================================
# Zu testende Klassen / Funktionen
# ============================================================

class Kontorechner:
    """Aus Baustein 05 – für pytest-Migration (Aufgabe 1)."""

    def __init__(self):
        self._kontostand = 0.0

    @property
    def kontostand(self) -> float:
        return self._kontostand

    def einzahlen(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError(f"Einzahlung muss positiv sein, war: {betrag}")
        self._kontostand += betrag

    def abheben(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError(f"Abhebungsbetrag muss positiv sein, war: {betrag}")
        if betrag > self._kontostand:
            raise ValueError(
                f"Unzureichendes Guthaben: {self._kontostand:.2f} < {betrag:.2f}"
            )
        self._kontostand -= betrag


class BenutzerkontoService:
    """Verwaltung von Benutzerkonten (vereinfacht)."""

    def __init__(self):
        self._benutzer = {}

    def benutzer_anlegen(self, name: str, passwort: str) -> None:
        if name in self._benutzer:
            raise ValueError(f"Benutzer '{name}' existiert bereits.")
        if len(passwort) < 8:
            raise ValueError("Passwort zu kurz (mind. 8 Zeichen).")
        self._benutzer[name] = passwort

    def anmelden(self, name: str, passwort: str) -> bool:
        return self._benutzer.get(name) == passwort

    def benutzer_loeschen(self, name: str) -> None:
        if name not in self._benutzer:
            raise ValueError(f"Benutzer '{name}' nicht gefunden.")
        del self._benutzer[name]

    def benutzeranzahl(self) -> int:
        return len(self._benutzer)


def berechne_note(punkte: int) -> int:
    """Notenberechnung aus Baustein 04."""
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


def validiere_menge(menge) -> bool:
    """Aus Baustein 04."""
    if not isinstance(menge, int):
        return False
    return 1 <= menge <= 999


def berechne_versandkosten(gewicht_kg: float, express: bool = False) -> float:
    """
    Aufgabe 5 – Versandkostenberechnung nach IHK-Vorgabe.

    Preistabelle:
        Standard ≤ 5 kg:   3.90
        Standard > 5 kg:   6.90
        Express  ≤ 5 kg:   8.90
        Express  > 5 kg:  14.90

    Raises:
        ValueError: Wenn gewicht_kg <= 0.
        TypeError:  Wenn gewicht_kg kein float/int ist.
    """
    if type(gewicht_kg) not in (int, float):
        raise TypeError(f"Gewicht muss eine Zahl sein, war: {type(gewicht_kg).__name__}")
    if gewicht_kg <= 0:
        raise ValueError(f"Gewicht muss größer als 0 sein, war: {gewicht_kg}")

    if gewicht_kg <= 5.0:
        return 8.90 if express else 3.90
    else:
        return 14.90 if express else 6.90


# ============================================================
# Aufgabe 1 – Von unittest zu pytest migrieren
# ============================================================

def test_einzahlen_positiver_betrag():
    """Migriert aus Baustein 05 – Einfacher assert-Vergleich."""
    konto = Kontorechner()
    konto.einzahlen(100.0)
    assert konto.kontostand == 100.0


def test_abheben_kein_guthaben():
    """Migriert aus Baustein 05 – Erwartet ValueError mittels pytest.raises."""
    konto = Kontorechner()
    with pytest.raises(ValueError):
        konto.abheben(10.0)


# ============================================================
# Aufgabe 2 – Fixtures
# ============================================================

@pytest.fixture
def kontoservice():
    """Fixture, das einen Service mit einem Standard-Testuser liefert."""
    service = BenutzerkontoService()
    service.benutzer_anlegen("testuser", "Geheim123!")
    return service


def test_anmelden_gueltig(kontoservice):
    """Prüft erfolgreiche Anmeldung des Fixture-Users."""
    assert kontoservice.anmelden("testuser", "Geheim123!") is True


def test_anmelden_falsches_passwort(kontoservice):
    """Prüft Ablehnung bei falschem Passwort."""
    assert kontoservice.anmelden("testuser", "falschesPW") is False


def test_benutzer_doppelt_anlegen_wirft_fehler(kontoservice):
    """Prüft, ob doppelte Registrierungen blockiert werden."""
    with pytest.raises(ValueError, match="existiert bereits"):
        kontoservice.benutzer_anlegen("testuser", "Anderes123!")


def test_benutzeranzahl_nach_loeschen(kontoservice):
    """Prüft Bestandsminderung nach Löschvorgang."""
    assert kontoservice.benutzeranzahl() == 1
    kontoservice.benutzer_loeschen("testuser")
    assert kontoservice.benutzeranzahl() == 0


# ============================================================
# Aufgabe 3 – Parametrisierung: berechne_note
# ============================================================

@pytest.mark.parametrize("punkte, erwartete_note", [
    (100, 1), (95, 1), (92, 1),  # Note 1 (Grenzen & Vertreter)
    (91, 2),  (85, 2), (81, 2),  # Note 2
    (80, 3),  (75, 3), (67, 3),  # Note 3
    (66, 4),  (60, 4), (50, 4),  # Note 4
    (49, 5),  (40, 5), (30, 5),  # Note 5
    (29, 6),  (15, 6), (0, 6)    # Note 6
])
def test_berechne_note(punkte, erwartete_note):
    """Parametrisierter Test für alle Notengrenzen und Vertreter."""
    assert berechne_note(punkte) == erwartete_note


# ============================================================
# Aufgabe 3b – Parametrisierung: validiere_menge
# ============================================================

@pytest.mark.parametrize("menge, erwartet", [
    (1, True), (500, True), (999, True),   # Gültige Grenzwerte & Mitte
    (0, False), (-5, False),               # Unterhalb des Minimums
    (1000, False), (1500, False),           # Oberhalb des Maximums
    ("100", False), (50.5, False), (True, False) # Ungültige Datentypen
])
def test_validiere_menge(menge, erwartet):
    """Parametrisierter Test für gültige/ungültige Mengenklassen."""
    assert validiere_menge(menge) == erwartet


# ============================================================
# Aufgabe 4 – pytest.raises mit match
# ============================================================

def test_einzahlung_null_fehlermeldung():
    """Nutze pytest.raises mit match-Parameter."""
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.einzahlen(0)


def test_abhebung_negativ_fehlermeldung():
    """Prüft Fehlermeldung bei negativem Abhebungsbetrag."""
    konto = Kontorechner()
    with pytest.raises(ValueError, match="Abhebungsbetrag muss positiv sein"):
        konto.abheben(-5)


def test_passwort_zu_kurz_fehlermeldung():
    """Prüft Fehlermeldung bei zu kurzen Passwörtern im Service."""
    service = BenutzerkontoService()
    with pytest.raises(ValueError, match="zu kurz"):
        service.benutzer_anlegen("neu", "123")


# ============================================================
# Aufgabe 5 – IHK: berechne_versandkosten
# ============================================================

@pytest.mark.parametrize("gewicht, express, erwartet", [
    (2.5, False, 3.90),   # Standard <= 5 kg
    (5.0, False, 3.90),   # Standard <= 5 kg (Grenzwert)
    (2.5, True, 8.90),    # Express <= 5 kg
    (5.0, True, 8.90),    # Express <= 5 kg (Grenzwert)
    (5.1, False, 6.90),   # Standard > 5 kg (Grenzwert)
    (12.0, False, 6.90),  # Standard > 5 kg
    (5.1, True, 14.90),   # Express > 5 kg (Grenzwert)
    (12.0, True, 14.90)   # Express > 5 kg
])
def test_berechne_versandkosten_gueltig(gewicht, express, erwartet):
    """Prüft alle vier Kombinationsmöglichkeiten inklusive Grenzwerte."""
    assert berechne_versandkosten(gewicht, express) == erwartet


def test_versandkosten_negatives_gewicht():
    """Testet, dass negatives Gewicht oder 0 einen ValueError wirft."""
    with pytest.raises(ValueError, match="größer als 0 sein"):
        berechne_versandkosten(-1.0, False)
    with pytest.raises(ValueError, match="größer als 0 sein"):
        berechne_versandkosten(0, False)


def test_versandkosten_falscher_typ():
    """Testet, dass falscher Datentyp einen TypeError auslöst."""
    with pytest.raises(TypeError, match="Zahl sein"):
        berechne_versandkosten("3.5", False)