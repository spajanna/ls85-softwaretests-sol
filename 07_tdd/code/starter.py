import pytest
import string
import random
import math


# ============================================================
# Aufgabe 1 – runden_auf_naechste_fuenf
# ============================================================

def runden_auf_naechste_fuenf(zahl: int) -> int:
    if zahl < 0:
        raise ValueError("negative Zahlen nicht erlaubt")
    return ((zahl + 4) // 5) * 5


class TestRundenAufNaechsteFuenf:

    def test_runden_3_ergibt_5(self):
        assert runden_auf_naechste_fuenf(3) == 5

    def test_runden_7_ergibt_10(self):
        assert runden_auf_naechste_fuenf(7) == 10

    def test_runden_10_ergibt_10(self):
        assert runden_auf_naechste_fuenf(10) == 10

    def test_runden_0_ergibt_0(self):
        assert runden_auf_naechste_fuenf(0) == 0

    def test_runden_negativ(self):
        with pytest.raises(ValueError):
            runden_auf_naechste_fuenf(-1)


# ============================================================
# Aufgabe 2 – PasswortGenerator
# ============================================================

class PasswortGenerator:

    def generate(self, laenge=12, grossbuchstaben=True, ziffern=True, sonderzeichen=False):
        if laenge < 8:
            raise ValueError("zu kurz")

        chars = string.ascii_lowercase

        if grossbuchstaben:
            chars += string.ascii_uppercase
        if ziffern:
            chars += string.digits
        if sonderzeichen:
            chars += string.punctuation

        if chars == string.ascii_lowercase:
            raise ValueError("keine Zeichen erlaubt")

        return "".join(random.choice(chars) for _ in range(laenge))


class TestPasswortGenerator:

    def setup_method(self):
        self.gen = PasswortGenerator()

    def test_passwort_hat_korrekte_laenge(self):
        pw = self.gen.generate(10)
        assert len(pw) == 10

    def test_passwort_standardlaenge_ist_12(self):
        assert len(self.gen.generate()) == 12

    def test_passwort_mit_grossbuchstaben(self):
        pw = self.gen.generate(20, grossbuchstaben=True, ziffern=False, sonderzeichen=False)
        assert any(c.isupper() for c in pw)

    def test_passwort_ohne_grossbuchstaben(self):
        pw = self.gen.generate(20, grossbuchstaben=False)
        assert all(not c.isupper() for c in pw)

    def test_passwort_mit_ziffern(self):
        pw = self.gen.generate(20, ziffern=True, grossbuchstaben=False, sonderzeichen=False)
        assert any(c.isdigit() for c in pw)

    def test_passwort_ohne_ziffern(self):
        pw = self.gen.generate(20, ziffern=False)
        assert all(not c.isdigit() for c in pw)

    def test_passwort_mit_sonderzeichen(self):
        pw = self.gen.generate(50, sonderzeichen=True)
        assert any(c in string.punctuation for c in pw)

    def test_mindestlaenge_wird_erzwungen(self):
        with pytest.raises(ValueError):
            self.gen.generate(7)

    def test_laenge_8_ist_erlaubt(self):
        assert len(self.gen.generate(8)) == 8

    def test_laenge_null_wirft_fehler(self):
        with pytest.raises(ValueError):
            self.gen.generate(0)

    def test_alle_zeichentypen_deaktiviert_wirft_fehler(self):
        with pytest.raises(ValueError):
            self.gen.generate(10, grossbuchstaben=False, ziffern=False, sonderzeichen=False)


# ============================================================
# Aufgabe 3 – Refactoring
# ============================================================

def verarbeite_bestellung(bestellung: dict) -> dict:

    if not bestellung:
        raise ValueError("Bestellung darf nicht leer sein")

    artikel = bestellung.get("artikel")
    if not artikel:
        raise ValueError("Bestellung muss 'artikel' enthalten")

    gesamtpreis = 0

    for a in artikel:
        preis = a.get("preis")
        menge = a.get("menge")

        if preis is None or menge is None:
            raise ValueError("ungültiger Artikel")
        if preis < 0:
            raise ValueError("negativ")
        if menge <= 0:
            raise ValueError("menge")

        gesamtpreis += preis * menge

    rabatt = bestellung.get("rabatt_prozent", 0)
    if rabatt < 0 or rabatt > 100:
        raise ValueError("Rabatt")

    endpreis = gesamtpreis * (1 - rabatt / 100)

    return {
        "gesamtpreis_brutto": round(gesamtpreis, 2),
        "rabatt_prozent": rabatt,
        "endpreis": round(endpreis, 2),
        "anzahl_artikel": len(artikel),
    }


class TestVerarbeiteBestellung:

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
            "artikel": [{"name": "Monitor", "preis": 300.0, "menge": 1}],
            "rabatt_prozent": 10,
        }
        ergebnis = verarbeite_bestellung(bestellung)
        assert ergebnis["endpreis"] == 270.0

    def test_leere_bestellung_wirft_fehler(self):
        with pytest.raises(ValueError):
            verarbeite_bestellung({})

    def test_negativer_preis_wirft_fehler(self):
        with pytest.raises(ValueError):
            verarbeite_bestellung({
                "artikel": [{"name": "Fehler", "preis": -5.0, "menge": 1}]
            })

    def test_ungültiger_rabatt_wirft_fehler(self):
        with pytest.raises(ValueError):
            verarbeite_bestellung({
                "artikel": [{"name": "Artikel", "preis": 10.0, "menge": 1}],
                "rabatt_prozent": 150,
            })


# ============================================================
# Aufgabe 4 – Zinsen (TDD)
# ============================================================

def berechne_zinsen(kapital: float, zinssatz: float, jahre: int) -> float:
    if kapital < 0 or zinssatz < 0 or jahre < 0:
        raise ValueError("ungültig")
    return kapital * (1 + zinssatz / 100) ** jahre


class TestBerechneZinsen:

    def test_standard(self):
        assert round(berechne_zinsen(1000, 5, 1), 2) == 1050

    def test_null_jahre(self):
        assert berechne_zinsen(1000, 5, 0) == 1000

    def test_null_kapital(self):
        assert berechne_zinsen(0, 5, 5) == 0

    def test_negative(self):
        with pytest.raises(ValueError):
            berechne_zinsen(-1, 5, 1)