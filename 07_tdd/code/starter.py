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

def runden_auf_naechste_fuenf(zahl):
    rest = zahl % 5

    if rest == 0:
        return zahl

    return zahl + (5 - rest)

class TestRundenAufNaechsteFuenf:
    """Aufgabe 1 – Entwickle die Funktion Schritt für Schritt nach TDD."""

    def test_runden_3_ergibt_5(self):
        assert runden_auf_naechste_fuenf(3) == 5

    def test_runden_7_ergibt_10(self):
        assert runden_auf_naechste_fuenf(7) == 10

    def test_runden_10_ergibt_10(self):
        assert runden_auf_naechste_fuenf(10) == 10

    def test_runden_0_ergibt_0(self):
        assert runden_auf_naechste_fuenf(0) == 0

    def test_runden_negativ(self):
        # definiertes Verhalten: auf das nächste höhere Vielfache von 5
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

    def generate(
        self,
        laenge=12,
        grossbuchstaben=True,
        ziffern=True,
        sonderzeichen=False
    ) -> str:
        if laenge < 8:
            raise ValueError("Mindestlänge ist 8 Zeichen")

        zeichen_pool = ""
        pflichtzeichen = []

        if grossbuchstaben:
            zeichen_pool += string.ascii_uppercase
            pflichtzeichen.append(random.choice(string.ascii_uppercase))

        if ziffern:
            zeichen_pool += string.digits
            pflichtzeichen.append(random.choice(string.digits))

        if sonderzeichen:
            sonder = "!@#$%&*?"
            zeichen_pool += sonder
            pflichtzeichen.append(random.choice(sonder))

        if not zeichen_pool:
            raise ValueError("Mindestens ein Zeichentyp muss aktiviert sein")

        restlaenge = laenge - len(pflichtzeichen)
        passwort_zeichen = pflichtzeichen

        for _ in range(restlaenge):
            passwort_zeichen.append(random.choice(zeichen_pool))

        random.shuffle(passwort_zeichen)

        return "".join(passwort_zeichen)

class TestPasswortGenerator:
    """Aufgabe 2 – TDD: Tests zuerst, dann Implementierung."""

    def test_passwort_hat_korrekte_laenge(self):
        generator = PasswortGenerator()
        passwort = generator.generate(laenge=16)
        assert len(passwort) == 16

    def test_passwort_standardlaenge_ist_12(self):
        generator = PasswortGenerator()
        passwort = generator.generate()
        assert len(passwort) == 12

    def test_passwort_mit_grossbuchstaben(self):
        generator = PasswortGenerator()
        passwort = generator.generate(grossbuchstaben=True)
        assert any(zeichen.isupper() for zeichen in passwort)

    def test_passwort_ohne_grossbuchstaben(self):
        generator = PasswortGenerator()
        passwort = generator.generate(grossbuchstaben=False, ziffern=True)
        assert not any(zeichen.isupper() for zeichen in passwort)

    def test_passwort_mit_ziffern(self):
        generator = PasswortGenerator()
        passwort = generator.generate(ziffern=True)
        assert any(zeichen.isdigit() for zeichen in passwort)

    def test_passwort_ohne_ziffern(self):
        generator = PasswortGenerator()
        passwort = generator.generate(grossbuchstaben=True, ziffern=False)
        assert not any(zeichen.isdigit() for zeichen in passwort)

    def test_passwort_mit_sonderzeichen(self):
        generator = PasswortGenerator()
        passwort = generator.generate(sonderzeichen=True)
        sonderzeichen = "!@#$%&*?"
        assert any(zeichen in sonderzeichen for zeichen in passwort)

    def test_mindestlaenge_wird_erzwungen(self):
        generator = PasswortGenerator()
        with pytest.raises(ValueError, match="Mindestlänge"):
            generator.generate(laenge=7)

    def test_laenge_8_ist_erlaubt(self):
        generator = PasswortGenerator()
        passwort = generator.generate(laenge=8)
        assert len(passwort) == 8

    def test_laenge_null_wirft_fehler(self):
        generator = PasswortGenerator()
        with pytest.raises(ValueError, match="Mindestlänge"):
            generator.generate(laenge=0)

    def test_alle_zeichentypen_deaktiviert_wirft_fehler(self):
        generator = PasswortGenerator()
        with pytest.raises(ValueError, match="Zeichentyp"):
            generator.generate(
                grossbuchstaben=False,
                ziffern=False,
                sonderzeichen=False
            )


# ============================================================
# Aufgabe 3 – Refactoring unter Tests
# ============================================================

# Diese Funktion ist funktionierend, aber schlecht strukturiert.
# Refactore sie – die Tests sollen danach noch grün sein!

def validiere_bestellung(bestellung: dict) -> list:
    if not bestellung:
        raise ValueError("Bestellung darf nicht leer sein")

    if "artikel" not in bestellung:
        raise ValueError("Bestellung muss 'artikel' enthalten")

    artikel_liste = bestellung["artikel"]

    if not artikel_liste:
        raise ValueError("Artikelliste darf nicht leer sein")

    return artikel_liste


def validiere_artikel(artikel: dict) -> None:
    if "preis" not in artikel:
        raise ValueError(f"Artikel '{artikel.get('name', '?')}' hat keinen Preis")

    if "menge" not in artikel:
        raise ValueError(f"Artikel '{artikel.get('name', '?')}' hat keine Menge")

    if artikel["preis"] < 0:
        raise ValueError("Preis darf nicht negativ sein")

    if artikel["menge"] <= 0:
        raise ValueError("Menge muss positiv sein")


def berechne_gesamtpreis(artikel_liste: list) -> float:
    gesamtpreis = 0

    for artikel in artikel_liste:
        validiere_artikel(artikel)
        gesamtpreis += artikel["preis"] * artikel["menge"]

    return gesamtpreis


def validiere_rabatt(rabatt: float) -> None:
    if not 0 <= rabatt <= 100:
        raise ValueError(f"Rabatt muss zwischen 0 und 100 liegen, war: {rabatt}")


def verarbeite_bestellung(bestellung: dict) -> dict:
    artikel_liste = validiere_bestellung(bestellung)

    gesamtpreis = berechne_gesamtpreis(artikel_liste)

    rabatt = bestellung.get("rabatt_prozent", 0)
    validiere_rabatt(rabatt)

    endpreis = gesamtpreis * (1 - rabatt / 100)

    return {
        "gesamtpreis_brutto": round(gesamtpreis, 2),
        "rabatt_prozent": rabatt,
        "endpreis": round(endpreis, 2),
        "anzahl_artikel": len(artikel_liste),
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

# def berechne_zinsen(kapital: float, zinssatz: float, jahre: int) -> float:
#     """Einfache Zinsberechnung: Kapital * (1 + Zinssatz/100) ^ Jahre"""
#     pass

def berechne_zinsen(kapital, zinssatz, jahre):
    if kapital < 0:
        raise ValueError("Kapital darf nicht negativ sein")

    if zinssatz < 0:
        raise ValueError("Zinssatz darf nicht negativ sein")

    if jahre < 0:
        raise ValueError("Jahre dürfen nicht negativ sein")

    zinsen = kapital * zinssatz / 100 * jahre
    return round(zinsen, 2)

def test_zinsen_normalfall():
    assert berechne_zinsen(1000, 5, 1) == 50.0


def test_zinsen_mehrere_jahre():
    assert berechne_zinsen(1000, 5, 3) == 150.0


def test_zinsen_kein_zinssatz():
    assert berechne_zinsen(1000, 0, 2) == 0.0


def test_zinsen_null_jahre():
    assert berechne_zinsen(1000, 5, 0) == 0.0


def test_negatives_kapital_wirft_fehler():
    with pytest.raises(ValueError):
        berechne_zinsen(-1000, 5, 1)


def test_negativer_zinssatz_wirft_fehler():
    with pytest.raises(ValueError):
        berechne_zinsen(1000, -5, 1)


def test_negative_jahre_werfen_fehler():
    with pytest.raises(ValueError):
        berechne_zinsen(1000, 5, -1)

class TestBerechneZinsen:
    """TODO: Schreibe mindestens 4 Tests BEVOR du berechne_zinsen implementierst."""

    def test_placeholder(self):
        """Entferne diesen Platzhalter und schreibe echte Tests."""
        pass
