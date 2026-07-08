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
    """
    Aufgabe 5 – TODO: Implementiere diese Funktion.

    Preistabelle:
        Standard ≤ 5 kg:   3.90
        Standard > 5 kg:   6.90
        Express  ≤ 5 kg:   8.90
        Express  > 5 kg:  14.90

    Raises:
        ValueError: Wenn gewicht_kg <= 0.
        TypeError:  Wenn gewicht_kg kein float/int ist.
    """
    # TODO: Deine Implementierung
    if not isinstance(gewicht_kg, (int, float)):
        raise TypeError(f"Gewicht muss eine Zahl sein, war: {type(gewicht_kg).__name__}")
    if gewicht_kg <= 0:
        raise ValueError(f"Gewicht muss positiv sein, war: {gewicht_kg}")
    if express:
        return 8.90 if gewicht_kg <= 5 else 14.90
    return 3.90 if gewicht_kg <= 5 else 6.90


# ============================================================
# Aufgabe 1 – Von unittest zu pytest migrieren
# ============================================================

def test_einzahlen_positiver_betrag():
    """TODO: Migriere aus Baustein 05."""
    konto = Kontorechner()
    konto.einzahlen(100)
    assert konto.kontostand == 100.0


def test_abheben_kein_guthaben():
    """TODO: Migriere aus Baustein 05, nutze pytest.raises."""
    konto = Kontorechner()
    with pytest.raises(ValueError):
        konto.abheben(10)


# ============================================================
# Aufgabe 2 – Fixtures
# ============================================================

@pytest.fixture
def kontoservice():
    """TODO: Fixture für BenutzerkontoService."""
    # TODO: Service anlegen, Testbenutzer hinzufügen, Service zurückgeben
    service = BenutzerkontoService()
    service.benutzer_anlegen("testuser", "geheim123")
    return service


# TODO: Mindestens 4 Testfunktionen, die das Fixture nutzen

def test_anmelden_gueltig(kontoservice):
    """TODO"""
    assert kontoservice.anmelden("testuser", "geheim123") is True


def test_anmelden_falsches_passwort(kontoservice):
    """TODO"""
    assert kontoservice.anmelden("testuser", "falsch") is False


def test_benutzer_doppelt_anlegen_wirft_fehler(kontoservice):
    """TODO"""
    with pytest.raises(ValueError, match="existiert bereits"):
        kontoservice.benutzer_anlegen("testuser", "passwort1")


def test_benutzeranzahl_nach_loeschen(kontoservice):
    """TODO"""
    kontoservice.benutzer_loeschen("testuser")
    assert kontoservice.benutzeranzahl() == 0


# ============================================================
# Aufgabe 3 – Parametrisierung: berechne_note
# ============================================================

@pytest.mark.parametrize("punkte, erwartete_note", [
    # TODO: Füge alle Grenzwerte und je 2 Vertreter pro Klasse ein
    # Format: (Punktzahl, erwartete Note)
    (100, 1),   # Beispiel – ergänze mindestens 13 weitere
    (92, 1), (96, 1),
    (81, 2), (91, 2), (85, 2),
    (67, 3), (80, 3), (70, 3),
    (50, 4), (66, 4), (55, 4),
    (30, 5), (49, 5), (40, 5),
    (0, 6), (29, 6), (15, 6),
])
def test_berechne_note(punkte, erwartete_note):
    """TODO: Parametrisierter Test für berechne_note."""
    assert berechne_note(punkte) == erwartete_note


# ============================================================
# Aufgabe 3b – Parametrisierung: validiere_menge
# ============================================================

@pytest.mark.parametrize("menge, erwartet", [
    # TODO: Gültige Klassen, ungültige Klassen, alle Grenzwerte
    (1, True),    # Beispiel – ergänze weitere
    (0, False),   # Grenzwert
    (500, True), (999, True),
    (-1, False), (-100, False), (1000, False), (2000, False),
    ("abc", False), (1.5, False), (None, False),
])
def test_validiere_menge(menge, erwartet):
    """TODO: Parametrisierter Test für validiere_menge."""
    assert validiere_menge(menge) == erwartet


# ============================================================
# Aufgabe 4 – pytest.raises mit match
# ============================================================

def test_einzahlung_null_fehlermeldung():
    """TODO: Nutze pytest.raises mit match-Parameter."""
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.einzahlen(0)


# TODO: Zwei weitere Tests mit pytest.raises und match

def test_abheben_negativ_fehlermeldung():
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.abheben(-5)


def test_benutzer_kurzes_passwort():
    service = BenutzerkontoService()
    with pytest.raises(ValueError, match="kurz"):
        service.benutzer_anlegen("neu", "kurz")


# ============================================================
# Aufgabe 5 – IHK: berechne_versandkosten
# ============================================================

@pytest.mark.parametrize("gewicht, express, erwartet", [
    # TODO: Alle vier gültigen Kombinationen
    (1, False, 3.90), (10, False, 6.90),
    (1, True, 8.90), (10, True, 14.90),
    (5, False, 3.90), (5.001, False, 6.90), (5, True, 8.90),
])
def test_berechne_versandkosten_gueltig(gewicht, express, erwartet):
    """TODO: Implementiere nach Fertigstellung von berechne_versandkosten."""
    assert berechne_versandkosten(gewicht, express) == erwartet


def test_versandkosten_negatives_gewicht():
    """TODO: Teste, dass negatives Gewicht ValueError wirft."""
    with pytest.raises(ValueError, match="positiv"):
        berechne_versandkosten(-1)


def test_versandkosten_falscher_typ():
    """TODO: Teste, dass falscher Typ TypeError wirft."""
    with pytest.raises(TypeError, match="Zahl"):
        berechne_versandkosten("schwer")
