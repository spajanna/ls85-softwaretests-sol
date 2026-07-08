"""
Baustein 07 – Test-Driven Development (TDD)
Startvorlage – komplett bearbeitet und einsatzbereit.

TDD-Regel: Kein Code ohne vorherigen Test!

Ausführen:
    pytest 07_tdd/code/starter.py -v
"""

import pytest
import string
import random
import math


# ============================================================
# Aufgabe 1 – runden_auf_naechste_fuenf (TDD-Übung)
# ============================================================

def runden_auf_naechste_fuenf(zahl: int) -> int:
    """Rundet eine Ganzzahl auf das nächste Vielfache von 5 auf."""
    return math.ceil(zahl / 5) * 5


class TestRundenAufNaechsteFuenf:
    """Aufgabe 1 – Entwickle die Funktion Schritt für Schritt nach TDD."""

    def test_runden_3_ergibt_5(self):
        """Zyklus 1: Erster Basis-Testlauf."""
        assert runden_auf_naechste_fuenf(3) == 5

    def test_runden_7_ergibt_10(self):
        """Zyklus 2: Test für die nächste Stufe."""
        assert runden_auf_naechste_fuenf(7) == 10

    def test_runden_10_ergibt_10(self):
        """Zyklus 3: Bereits ein Vielfaches von 5."""
        assert runden_auf_naechste_fuenf(10) == 10

    def test_runden_0_ergibt_0(self):
        """Zyklus 4: Sonderfall 0."""
        assert runden_auf_naechste_fuenf(0) == 0

    def test_runden_negativ(self):
        """Zyklus 5: Verhalten bei negativen Zahlen."""
        assert runden_auf_naechste_fuenf(-3) == 0
        assert runden_auf_naechste_fuenf(-5) == -5
        assert runden_auf_naechste_fuenf(-7) == -5


# ============================================================
# Aufgabe 2 – PasswortGenerator (TDD Praxisprojekt)
# ============================================================

class PasswortGenerator:
    """
    Anforderungen:
    - generate(laenge, grossbuchstaben, ziffern, sonderzeichen) -> str
    - Standard: laenge=12, grossbuchstaben=True, ziffern=True, sonderzeichen=False
    - Mindestlänge: 8 Zeichen (sonst ValueError)
    - Gibt einen String der gewünschten Länge zurück
    """

    def generate(self, laenge: int = 12, grossbuchstaben: bool = True, 
                 ziffern: bool = True, sonderzeichen: bool = False) -> str:
        
        if laenge < 8:
            raise ValueError(f"Passwort zu kurz. Mindestlänge ist 8 Zeichen, war: {laenge}")
        
        if not any([True, grossbuchstaben, ziffern, sonderzeichen]):
            # Da Kleinbuchstaben immer als Fallback dienen, fangen wir das ab,
            # wenn man alle Zeichentypen explizit unterdrücken wollen würde.
            pass

        pool = list(string.ascii_lowercase)
        garantierte_zeichen = []

        if grossbuchstaben:
            pool.extend(string.ascii_uppercase)
            garantierte_zeichen.append(random.choice(string.ascii_uppercase))
        if ziffern:
            pool.extend(string.digits)
            garantierte_zeichen.append(random.choice(string.digits))
        if sonderzeichen:
            sz_liste = "!@#$%^&*()_+-=[]{}|;:,.<>?"
            pool.extend(sz_liste)
            garantierte_zeichen.append(random.choice(sz_liste))

        if not pool:
            raise ValueError("Keine Zeichentypen für die Generierung ausgewählt.")

        if len(garantierte_zeichen) > laenge:
            raise ValueError("Länge reicht nicht aus, um alle Kriterien zu erfüllen.")

        # Rest auffüllen
        anzahl_rest = laenge - len(garantierte_zeichen)
        passwort_basis = garantierte_zeichen + random.choices(pool, k=anzahl_rest)
        
        # Durchmischen, um Musterbildung zu vermeiden
        random.shuffle(passwort_basis)
        return "".join(passwort_basis)


class TestPasswortGenerator:
    """Aufgabe 2 – TDD: Tests zuerst, dann Implementierung."""

    # User Story 1: Konfigurierbare Länge
    def test_passwort_hat_korrekte_laenge(self):
        generator = PasswortGenerator()
        assert len(generator.generate(laenge=15)) == 15

    def test_passwort_standardlaenge_ist_12(self):
        generator = PasswortGenerator()
        assert len(generator.generate()) == 12

    # User Story 2: Großbuchstaben
    def test_passwort_mit_grossbuchstaben(self):
        generator = PasswortGenerator()
        pw = generator.generate(grossbuchstaben=True, ziffern=False, sonderzeichen=False)
        assert any(c.isupper() for c in pw)

    def test_passwort_ohne_grossbuchstaben(self):
        generator = PasswortGenerator()
        pw = generator.generate(grossbuchstaben=False, ziffern=False, sonderzeichen=False)
        assert not any(c.isupper() for c in pw)

    # User Story 3: Ziffern
    def test_passwort_mit_ziffern(self):
        generator = PasswortGenerator()
        pw = generator.generate(grossbuchstaben=False, ziffern=True, sonderzeichen=False)
        assert any(c.isdigit() for c in pw)

    def test_passwort_ohne_ziffern(self):
        generator = PasswortGenerator()
        pw = generator.generate(grossbuchstaben=False, ziffern=False, sonderzeichen=False)
        assert not any(c.isdigit() for c in pw)

    # User Story 4: Sonderzeichen
    def test_passwort_mit_sonderzeichen(self):
        generator = PasswortGenerator()
        pw = generator.generate(grossbuchstaben=False, ziffern=False, sonderzeichen=True)
        sz_liste = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        assert any(c in sz_liste for c in pw)

    # User Story 5: Mindestlänge
    def test_mindestlaenge_wird_erzwungen(self):
        generator = PasswortGenerator()
        with pytest.raises(ValueError, match="Mindestlänge"):
            generator.generate(laenge=7)

    def test_laenge_8_ist_erlaubt(self):
        generator = PasswortGenerator()
        assert len(generator.generate(laenge=8)) == 8

    # User Story 6: Fehlermeldungen
    def test_laenge_null_wirft_fehler(self):
        generator = PasswortGenerator()
        with pytest.raises(ValueError, match="Mindestlänge"):
            generator.generate(laenge=0)


# ============================================================
# Aufgabe 3 – Refactoring unter Tests
# ============================================================

def _validiere_basis_bestellung(bestellung: dict) -> None:
    """Hilfsfunktion zur strukturellen Überprüfung der Bestellung."""
    if not bestellung:
        raise ValueError("Bestellung darf nicht leer sein")
    if "artikel" not in bestellung:
        raise ValueError("Bestellung muss 'artikel' enthalten")
    if not bestellung["artikel"]:
        raise ValueError("Artikelliste darf nicht leer sein")


def _validiere_und_berechne_artikel(artikel: dict) -> float:
    """Hilfsfunktion für die Validierung einzelner Artikelposten."""
    if "preis" not in artikel:
        raise ValueError(f"Artikel '{artikel.get('name', '?')}' hat keinen Preis")
    if "menge" not in artikel:
        raise ValueError(f"Artikel '{artikel.get('name', '?')}' hat keine Menge")
    if artikel["preis"] < 0:
        raise ValueError("Preis darf nicht negativ sein")
    if artikel["menge"] <= 0:
        raise ValueError("Menge muss positiv sein")
    return artikel["preis"] * artikel["menge"]


def verarbeite_bestellung(bestellung: dict) -> dict:
    """
    Refactorte Version: Modularer, lesbarer und ohne tiefe Schachtelungen.
    """
    _validiere_basis_bestellung(bestellung)

    rabatt = bestellung.get("rabatt_prozent", 0)
    if not 0 <= rabatt <= 100:
        raise ValueError(f"Rabatt muss zwischen 0 und 100 liegen, war: {rabatt}")

    gesamtpreis = sum(_validiere_und_berechne_artikel(art) for art in bestellung["artikel"])
    endpreis = gesamtpreis * (1 - rabatt / 100)

    return {
        "gesamtpreis_brutto": round(gesamtpreis, 2),
        "rabatt_prozent": rabatt,
        "endpreis": round(endpreis, 2),
        "anzahl_artikel": len(bestellung["artikel"]),
    }


class TestVerarbeiteBestellung:
    """Diese Tests bleiben nach dem Refactoring garantiert grün."""

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

def berechne_zinsen(kapital: float, zinssatz: float, jahre: int) -> float:
    """Einfache Zinsberechnung mit Zinseszins: Kapital * (1 + Zinssatz/100) ^ Jahre"""
    if kapital < 0 or zinssatz < 0 or jahre < 0:
        raise ValueError("Eingabewerte dürfen nicht negativ sein.")
    return round(kapital * (1 + zinssatz / 100) ** jahre, 2)


class TestBerechneZinsen:
    """TDD-Absicherung für die IHK-Aufgabe."""

    def test_basis_zinsberechnung(self):
        """Prüft einfache Zinsrechnung nach einem Jahr."""
        assert berechne_zinsen(1000.0, 5.0, 1) == 1050.0

    def test_zinseszins_mehrere_jahre(self):
        """Prüft Zinseszins-Effekt über 3 Jahre hinweg."""
        assert berechne_zinsen(1000.0, 2.0, 3) == 1061.21

    def test_null_jahre_liefert_ausgangskapital(self):
        """Ohne Anlagedauer darf sich das Kapital nicht verändern."""
        assert berechne_zinsen(500.0, 4.5, 0) == 500.0

    def test_negative_werte_werfen_value_error(self):
        """Sichert die Robustheit gegen invalide mathematische Zustände ab."""
        with pytest.raises(ValueError):
            berechne_zinsen(-100.0, 2.0, 1)