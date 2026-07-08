# 08_testbericht.md – Testbericht: Lagerverwaltungssystem

## 1. Zusammenfassung

| Feld | Wert |
|------|------|
| Projekt | Lagerverwaltungssystem (LS 8.5) |
| Testdatum | [Datum] |
| Tester | [Name] |
| Getestete Version | 1.0 |

**Ergebnis**: 22/22 Tests bestanden, Coverage 100 %.
Das Lagerverwaltungssystem ist **abnahmebereit**.

## 2. Testumgebung

- Python 3.14
- pytest 9.0.3
- pytest-cov

## 3. Testergebnisse

| TC-ID | Titel | Status |
|-------|-------|--------|
| TC-LAGER-001 | Artikel anlegen – Normalfall | PASSED |
| TC-LAGER-002 | Artikel anlegen – Duplikat | PASSED |
| TC-LAGER-003 | Bestand erhöhen – Normalfall | PASSED |
| TC-LAGER-004 | Bestand reduzieren – Normalfall | PASSED |
| TC-LAGER-005 | Bestand reduzieren – unter Null | PASSED |
| TC-LAGER-006 | Artikel suchen – vorhanden | PASSED |
| TC-LAGER-007 | Artikel suchen – nicht vorhanden | PASSED |
| TC-LAGER-008 | Gesamtwert berechnen | PASSED |
| TC-LAGER-009 | Kapazitätsüberschreitung | PASSED |
| TC-LAGER-010 | Artikel unter Mindestbestand | PASSED |
| TC-LAGER-011 | Ungültige Lager-Kapazität | PASSED |
| TC-LAGER-012 | Artikel mit leerer ID | PASSED |
| TC-LAGER-013 | Negativer Preis | PASSED |
| TC-LAGER-014 | Negativer Bestand | PASSED |
| TC-LAGER-015 | Bestand erhöhen – Artikel nicht gefunden | PASSED |
| TC-LAGER-016 | Bestand erhöhen – ungültige Menge | PASSED |
| TC-LAGER-017 | Bestand reduzieren – Artikel nicht gefunden | PASSED |
| TC-LAGER-018 | Bestand reduzieren – ungültige Menge | PASSED |
| TC-LAGER-019 | Artikel löschen – Normalfall | PASSED |
| TC-LAGER-020 | Artikel löschen – nicht gefunden | PASSED |
| TC-LAGER-021 | Gesamtwert bei leerem Lager | PASSED |
| TC-LAGER-022 | Keine Artikel unter Mindestbestand | PASSED |

**Gesamt**: 22/22 = 100 % bestanden

## 4. Gefundene Defekte

Keine.

## 5. Coverage

| Modul | Coverage |
|-------|----------|
| `08_dokumentation/code/starter` (Artikel + Lager) | 100 % |

## 6. Abnahmeempfehlung

**Abnahmebereit**: Ja

Die Lagerverwaltung erfüllt alle spezifizierten Anforderungen.
Alle Validierungen (Preis, Bestand, Kapazität, Duplikate) greifen korrekt.
Coverage von 100 % bestätigt, dass jeder Codepfad getestet wurde.

## 7. Offene Punkte

Keine.
