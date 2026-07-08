"""
Baustein 07 – Test-Driven Development (TDD)
Startvorlage – bearbeite diese Datei für deine Aufgaben.

TDD-Regel: Kein Code ohne vorherigen Test!

Ausführen:
    pytest 07_tdd/code/starter.py -v
"""

import pytest
import string
import random


# ============================================================
# Aufgabe 1 – runden_auf_naechste_fuenf (TDD-Übung)
# ============================================================

# TODO: Schreibe zuerst die Tests, dann die Implementierung!

def runden_auf_naechste_fuenf(zahl: int) -> int:
    return ((zahl + 4) // 5) * 5


class TestRundenAufNaechsteFuenf:
    """Aufgabe 1 – Entwickle die Funktion Schritt für Schritt nach TDD."""

    def test_runden_3_ergibt_5(self):
        """Zyklus 1: Dieser Test muss zuerst ROT sein."""
        # TODO: Schreibe den Test – führe ihn aus – er wird rot sein
        # Dann: Implementiere runden_auf_naechste_fuenf minimal
        assert runden_auf_naechste_fuenf(3) == 5

    def test_runden_7_ergibt_10(self):
        """Zyklus 2: TODO"""
        assert runden_auf_naechste_fuenf(7) == 10

    def test_runden_10_ergibt_10(self):
        """Zyklus 3: Bereits ein Vielfaches von 5."""
        assert runden_auf_naechste_fuenf(10) == 10

    def test_runden_0_ergibt_0(self):
        """Zyklus 4: Sonderfall 0."""
        assert runden_auf_naechste_fuenf(0) == 0

    def test_runden_negativ(self):
        """Zyklus 5: Was passiert mit negativen Zahlen? Definiere zuerst das Verhalten!"""
        assert runden_auf_naechste_fuenf(-3) == 0
        assert runden_auf_naechste_fuenf(-7) == -5


# ============================================================
# Aufgabe 2 – PasswortGenerator (TDD Praxisprojekt)
# ============================================================

# SCHRITT 1: Schreibe alle Tests BEVOR du die Klasse implementierst!
# Die Klasse ist absichtlich noch nicht implementiert.

class PasswortGenerator:
    """
    TODO: Implementiere diese Klasse NACH den Tests.

    Anforderungen:
    - generate(laenge, grossbuchstaben, ziffern, sonderzeichen) -> str
    - Standard: laenge=12, grossbuchstaben=True, ziffern=True, sonderzeichen=False
    - Mindestlänge: 8 Zeichen (sonst ValueError)
    - Gibt einen String der gewünschten Länge zurück
    """

    def generate(self, laenge: int = 12, grossbuchstaben: bool = True,
                 ziffern: bool = True, sonderzeichen: bool = False) -> str:
        if laenge < 8:
            raise ValueError(f"Mindestlänge ist 8, war: {laenge}")
        if not any([grossbuchstaben, ziffern, sonderzeichen]):
            raise ValueError("Mindestens ein Zeichentyp muss aktiviert sein")

        pool = string.ascii_lowercase
        mindestens = []

        if grossbuchstaben:
            pool += string.ascii_uppercase
            mindestens.append(random.choice(string.ascii_uppercase))
        if ziffern:
            pool += string.digits
            mindestens.append(random.choice(string.digits))
        if sonderzeichen:
            pool += "!@#$%^&*"
            mindestens.append(random.choice("!@#$%^&*"))

        rest = [random.choice(pool) for _ in range(laenge - len(mindestens))]
        chars = mindestens + rest
        random.shuffle(chars)
        return ''.join(chars)


class TestPasswortGenerator:
    """Aufgabe 2 – TDD: Tests zuerst, dann Implementierung."""

    # User Story 1: Konfigurierbare Länge
    def test_passwort_hat_korrekte_laenge(self):
        """TODO: Schreibe vor der Implementierung!"""
        gen = PasswortGenerator()
        pw = gen.generate(10)
        assert len(pw) == 10

    def test_passwort_standardlaenge_ist_12(self):
        """TODO"""
        gen = PasswortGenerator()
        pw = gen.generate()
        assert len(pw) == 12

    # User Story 2: Großbuchstaben
    def test_passwort_mit_grossbuchstaben(self):
        """TODO: Mindestens ein Großbuchstabe vorhanden."""
        gen = PasswortGenerator()
        pw = gen.generate(grossbuchstaben=True)
        assert any(c.isupper() for c in pw)

    def test_passwort_ohne_grossbuchstaben(self):
        """TODO: Kein Großbuchstabe vorhanden wenn deaktiviert."""
        gen = PasswortGenerator()
        pw = gen.generate(grossbuchstaben=False, ziffern=True)
        assert not any(c.isupper() for c in pw)

    # User Story 3: Ziffern
    def test_passwort_mit_ziffern(self):
        """TODO"""
        gen = PasswortGenerator()
        pw = gen.generate(ziffern=True)
        assert any(c.isdigit() for c in pw)

    def test_passwort_ohne_ziffern(self):
        """TODO"""
        gen = PasswortGenerator()
        pw = gen.generate(ziffern=False, sonderzeichen=True)
        assert not any(c.isdigit() for c in pw)

    # User Story 4: Sonderzeichen
    def test_passwort_mit_sonderzeichen(self):
        """TODO"""
        gen = PasswortGenerator()
        pw = gen.generate(sonderzeichen=True)
        assert any(c in "!@#$%^&*" for c in pw)

    # User Story 5: Mindestlänge
    def test_mindestlaenge_wird_erzwungen(self):
        """TODO: laenge=7 soll ValueError werfen."""
        gen = PasswortGenerator()
        with pytest.raises(ValueError):
            gen.generate(7)

    def test_laenge_8_ist_erlaubt(self):
        """TODO: Grenzwert – muss funktionieren."""
        gen = PasswortGenerator()
        pw = gen.generate(8)
        assert len(pw) == 8

    # User Story 6: Fehlermeldungen
    def test_laenge_null_wirft_fehler(self):
        """TODO"""
        gen = PasswortGenerator()
        with pytest.raises(ValueError):
            gen.generate(0)

    def test_alle_zeichentypen_deaktiviert_wirft_fehler(self):
        """TODO: Was soll passieren, wenn keine Zeichen erlaubt sind?"""
        gen = PasswortGenerator()
        with pytest.raises(ValueError):
            gen.generate(grossbuchstaben=False, ziffern=False, sonderzeichen=False)


# ============================================================
# Aufgabe 3 – Refactoring unter Tests
# ============================================================

# Diese Funktion ist funktionierend, aber schlecht strukturiert.
# Refactore sie – die Tests sollen danach noch grün sein!

def _validiere_bestellung(bestellung: dict) -> None:
    if not bestellung:
        raise ValueError("Bestellung darf nicht leer sein")
    if "artikel" not in bestellung:
        raise ValueError("Bestellung muss 'artikel' enthalten")
    if not bestellung["artikel"]:
        raise ValueError("Artikelliste darf nicht leer sein")


def _validiere_artikel(artikel: dict) -> None:
    if "preis" not in artikel:
        raise ValueError(f"Artikel '{artikel.get('name', '?')}' hat keinen Preis")
    if "menge" not in artikel:
        raise ValueError(f"Artikel '{artikel.get('name', '?')}' hat keine Menge")
    if artikel["preis"] < 0:
        raise ValueError("Preis darf nicht negativ sein")
    if artikel["menge"] <= 0:
        raise ValueError("Menge muss positiv sein")


def _berechne_gesamtpreis(artikel: list) -> float:
    return sum(a["preis"] * a["menge"] for a in artikel)


def _validiere_rabatt(rabatt: float) -> None:
    if not 0 <= rabatt <= 100:
        raise ValueError(f"Rabatt muss zwischen 0 und 100 liegen, war: {rabatt}")


def verarbeite_bestellung(bestellung: dict) -> dict:
    """
    Verarbeitet eine Bestellung und gibt ein Ergebnis-Dict zurück.
    (Schlecht strukturiert – refactoring notwendig!)
    """
    _validiere_bestellung(bestellung)

    for artikel in bestellung["artikel"]:
        _validiere_artikel(artikel)

    gesamtpreis = _berechne_gesamtpreis(bestellung["artikel"])
    rabatt = bestellung.get("rabatt_prozent", 0)
    _validiere_rabatt(rabatt)

    endpreis = gesamtpreis * (1 - rabatt / 100)

    return {
        "gesamtpreis_brutto": round(gesamtpreis, 2),
        "rabatt_prozent": rabatt,
        "endpreis": round(endpreis, 2),
        "anzahl_artikel": len(bestellung["artikel"]),
    }


class TestVerarbeiteBestellung:
    """Diese Tests sollen nach dem Refactoring noch alle grün sein."""

    def test_normale_bestellung(self):
        bestellung = {
            "artikel": [
                {"name": "USB-Stick", "preis": 9.99, "menge": 2},
                {"name": "Maus", "preis": 19.99, "menge": 1},
            ]
        }
        ergebnis = verarbeite_bestellung(bestellung)
        assert ergebnis["gesamtpreis_brutto"] == 39.97
        assert ergebnis["endpreis"] == 39.97
        assert ergebnis["anzahl_artikel"] == 2

    def test_bestellung_mit_rabatt(self):
        bestellung = {
            "artikel": [{"name": "Monitor", "preis": 300.00, "menge": 1}],
            "rabatt_prozent": 10,
        }
        ergebnis = verarbeite_bestellung(bestellung)
        assert ergebnis["endpreis"] == 270.00

    def test_leere_bestellung_wirft_fehler(self):
        with pytest.raises(ValueError):
            verarbeite_bestellung({})

    def test_negativer_preis_wirft_fehler(self):
        with pytest.raises(ValueError, match="negativ"):
            verarbeite_bestellung({
                "artikel": [{"name": "Fehler", "preis": -5.00, "menge": 1}]
            })

    def test_ungültiger_rabatt_wirft_fehler(self):
        with pytest.raises(ValueError, match="Rabatt"):
            verarbeite_bestellung({
                "artikel": [{"name": "Artikel", "preis": 10.00, "menge": 1}],
                "rabatt_prozent": 150,
            })


# ============================================================
# Aufgabe 4 – IHK: berechne_zinsen (TDD)
# ============================================================

# TODO: Schreibe ZUERST die Testklasse TestBerechneZinsen,
#       DANN die Funktion berechne_zinsen!

def berechne_zinsen(kapital: float, zinssatz: float, jahre: int) -> float:
    """Einfache Zinsberechnung: Kapital * (1 + Zinssatz/100) ^ Jahre"""
    if kapital < 0:
        raise ValueError("Kapital darf nicht negativ sein")
    if zinssatz < 0:
        raise ValueError("Zinssatz darf nicht negativ sein")
    if jahre <= 0:
        raise ValueError("Jahre muss positiv sein")
    return round(kapital * (1 + zinssatz / 100) ** jahre, 2)


class TestBerechneZinsen:
    """TODO: Schreibe mindestens 4 Tests BEVOR du berechne_zinsen implementierst."""

    def test_einfache_verzinsung_1_jahr(self):
        assert berechne_zinsen(1000, 5, 1) == 1050.00

    def test_mehrere_jahre(self):
        assert berechne_zinsen(1000, 5, 3) == 1157.63

    def test_null_kapital(self):
        assert berechne_zinsen(0, 5, 5) == 0.00

    def test_null_zinssatz(self):
        assert berechne_zinsen(1000, 0, 5) == 1000.00

    def test_negatives_kapital_wirft_fehler(self):
        with pytest.raises(ValueError, match="Kapital"):
            berechne_zinsen(-100, 5, 1)
