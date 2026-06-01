# 07_tdd_protokoll.md – TDD-Protokoll

## Aufgabe 1 – runden_auf_naechste_fuenf

### Zyklus 1: `test_runden_3_ergibt_5`
- **ROT**: Test erwartet `runden_auf_naechste_fuenf(3) == 5` → schlägt fehl (Funktion nicht implementiert)
- **GRÜN**: `return 5` – minimalste Implementierung
- **REFACTOR**: Noch kein Bedarf

### Zyklus 2: `test_runden_7_ergibt_10`
- **ROT**: Test erwartet `runden_auf_naechste_fuenf(7) == 10`
- **GRÜN**: `return ((zahl + 4) // 5) * 5`
- **REFACTOR**: Formel funktioniert für 3 und 7

### Zyklus 3: `test_runden_10_ergibt_10`
- **ROT**: Test erwartet `runden_auf_naechste_fuenf(10) == 10`
- **GRÜN**: Formel gibt korrekt 10 zurück
- **REFACTOR**: Kein Bedarf

### Zyklus 4: `test_runden_0_ergibt_0`
- **ROT**: Test erwartet `runden_auf_naechste_fuenf(0) == 0`
- **GRÜN**: `((0 + 4) // 5) * 5 = (4 // 5) * 5 = 0 * 5 = 0` ✓
- **REFACTOR**: Kein Bedarf

### Zyklus 5: `test_runden_negativ`
- **ROT**: `-3` und `-7` testen
- **GRÜN**: Formel liefert `((zahl + 4) // 5) * 5` auch für negative Zahlen korrekte Ergebnisse
  - `((-3 + 4) // 5) * 5 = (1 // 5) * 5 = 0`
  - `((-7 + 4) // 5) * 5 = (-3 // 5) * 5 = -1 * 5 = -5`
- **REFACTOR**: Kein Bedarf – eine Zeile, mathematisch sauber

---

## Aufgabe 2 – PasswortGenerator

### User Story 1: Konfigurierbare Länge
- **Tests**: `test_passwort_hat_korrekte_laenge` (10 Zeichen), `test_passwort_standardlaenge_ist_12`
- **GRÜN**: Generator erstellt Passwort mit `random.choices` und gibt String zurück

### User Story 2: Großbuchstaben
- **Tests**: `test_passwort_mit_grossbuchstaben`, `test_passwort_ohne_grossbuchstaben`
- **GRÜN**: Großbuchstaben-Pool wird bedingt zum Zeichenpool hinzugefügt

### User Story 3: Ziffern
- **Tests**: `test_passwort_mit_ziffern`, `test_passwort_ohne_ziffern`
- **GRÜN**: Ziffern-Pool wird bedingt hinzugefügt

### User Story 4: Sonderzeichen
- **Tests**: `test_passwort_mit_sonderzeichen`
- **GRÜN**: Sonderzeichen-Pool wird bedingt hinzugefügt

### User Story 5: Mindestlänge
- **Tests**: `test_mindestlaenge_wird_erzwungen` (laenge=7 → ValueError), `test_laenge_8_ist_erlaubt`
- **GRÜN**: `if laenge < 8: raise ValueError`

### User Story 6: Fehlermeldungen
- **Tests**: `test_laenge_null_wirft_fehler`, `test_alle_zeichentypen_deaktiviert_wirft_fehler`
- **GRÜN**: Prüfung auf mindestens einen aktiven Zeichentyp

---

## Aufgabe 3 – Refactoring verarbeite_bestellung

**Ausgangszustand**: Eine einzelne Funktion mit 55 Zeilen, tiefer Verschachtelung,
gemischter Verantwortung (Validierung + Berechnung + Rückgabe).

**Refactoring-Schritte**:
1. `_validiere_bestellung()` – Prüft Bestellstruktur (leer, artikel-Feld, leere Liste)
2. `_validiere_artikel()` – Prüft Einzelartikel (preis, menge, negative Werte)
3. `_berechne_gesamtpreis()` – Summiert preis × menge
4. `_validiere_rabatt()` – Prüft Rabattbereich 0–100

**Ergebnis**: 4 kleine, fokussierte Hilfsfunktionen + 1 orchestrale Hauptfunktion.
Alle 5 bestehenden Tests bleiben grün.

---

## Aufgabe 4 – berechne_zinsen (TDD)

### TDD-Zyklus:
1. **ROT**: `test_einfache_verzinsung_1_jahr` schreibt → erwartet `berechne_zinsen(1000, 5, 1) == 1050.00`
2. **GRÜN**: Implementiere `kapital * (1 + zinssatz/100) ** jahre`
3. **ROT**: `test_mehrere_jahre` → `1000 * 1.05^3 = 1157.63`
4. **GRÜN**: Formel deckt alle Fälle ab
5. **ROT**: `test_negatives_kapital_wirft_fehler` → ValueError erwarten
6. **GRÜN**: Validierung für negative Werte eingebaut

**Tests (5 Stück)**:
- `test_einfache_verzinsung_1_jahr` – Basisfall
- `test_mehrere_jahre` – Zinseszins
- `test_null_kapital` – Grenzfall
- `test_null_zinssatz` – Kein Zins
- `test_negatives_kapital_wirft_fehler` – Fehlerfall
