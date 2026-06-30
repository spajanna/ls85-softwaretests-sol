"""
Baustein 06 – pytest
Startvorlage – bearbeite diese Datei für deine Aufgaben.

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
    if not isinstance(gewicht_kg, (int, float)):
        raise TypeError("Gewicht muss Zahl sein")

    if gewicht_kg <= 0:
        raise ValueError("Gewicht muss positiv sein")

    if express:
        return 8.90 if gewicht_kg <= 5 else 14.90
    else:
        return 3.90 if gewicht_kg <= 5 else 6.90


# ============================================================
# Aufgabe 1 – Von unittest zu pytest migrieren
# ============================================================

def test_einzahlen_positiver_betrag():
    konto = Kontorechner()
    konto.einzahlen(100)
    assert konto.kontostand == 100


def test_abheben_kein_guthaben():
    konto = Kontorechner()
    with pytest.raises(ValueError):
        konto.abheben(10)


# ============================================================
# Aufgabe 2 – Fixtures
# ============================================================

@pytest.fixture
def kontoservice():
    service = BenutzerkontoService()
    service.benutzer_anlegen("testuser", "Test1234!")
    return service


def test_anmelden_gueltig(kontoservice):
    assert kontoservice.anmelden("testuser", "Test1234!")


def test_anmelden_falsches_passwort(kontoservice):
    assert not kontoservice.anmelden("testuser", "falsch")


def test_benutzer_doppelt_anlegen_wirft_fehler(kontoservice):
    with pytest.raises(ValueError):
        kontoservice.benutzer_anlegen("testuser", "Test1234!")


def test_benutzeranzahl_nach_loeschen(kontoservice):
    kontoservice.benutzer_loeschen("testuser")
    assert kontoservice.benutzeranzahl() == 0


# ============================================================
# Aufgabe 3 – Parametrisierung: berechne_note
# ============================================================

@pytest.mark.parametrize("punkte, erwartete_note", [
    (0,6),(20,6),
    (30,5),(40,5),
    (50,4),(60,4),
    (67,3),(75,3),
    (81,2),(90,2),
    (92,1),(100,1),
    (29,6),(91,2)
])
def test_berechne_note(punkte, erwartete_note):
    """TODO: Parametrisierter Test für berechne_note."""
    assert berechne_note(punkte) == erwartete_note


# ============================================================
# Aufgabe 3b – Parametrisierung: validiere_menge
# ============================================================

@pytest.mark.parametrize("menge, erwartet", [
    (1, True),
    (500, True),
    (999, True),
    (0, False),
    (1000, False),
    (-1, False),
    ("abc", False),
    (1.5, False),
])
def test_validiere_menge(menge, erwartet):
    """TODO: Parametrisierter Test für validiere_menge."""
    assert validiere_menge(menge) == erwartet


# ============================================================
# Aufgabe 4 – pytest.raises mit match
# ============================================================

def test_abheben_null_fehlermeldung():
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.abheben(0)


def test_abheben_zu_viel_fehlermeldung():
    konto = Kontorechner()
    konto.einzahlen(50)
    with pytest.raises(ValueError, match="Unzureichendes"):
        konto.abheben(100)


# ============================================================
# Aufgabe 5 – IHK: berechne_versandkosten
# ============================================================

@pytest.mark.parametrize("gewicht, express, erwartet", [
    (5, False, 3.90),
    (6, False, 6.90),
    (5, True, 8.90),
    (6, True, 14.90),
])
def test_versandkosten_negatives_gewicht():
    with pytest.raises(ValueError):
        berechne_versandkosten(-1)


def test_versandkosten_falscher_typ():
    with pytest.raises(TypeError):
        berechne_versandkosten("abc")
