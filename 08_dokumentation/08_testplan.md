# 08_testplan.md – Testplan: Lagerverwaltungssystem

## 1. Projekt

| Feld | Wert |
|------|------|
| Projektname | Lagerverwaltungssystem (LS 8.5) |
| Testgegenstand | Klasse `Lager` und `Artikel` in Python |
| Autor | [Name] |
| Version | 1.0 |
| Datum | [Datum] |

## 2. Testziele

- Korrekte Abbildung der Lagerlogik (anlegen, buchen, suchen, löschen)
- Validierung aller Eingaben (Preis, Menge, Kapazität)
- Fehlerbehandlung bei Grenzfällen (leeres Lager, Kapazitätsgrenze, Duplikate)

## 3. Teststufen

| Stufe | Umfang |
|-------|--------|
| Unit-Test | Jede Methode von `Lager` und `Artikel` einzeln |
| Integrationstest | Zusammenspiel `artikel_anlegen` → `bestand_erhoehen` → `gesamtwert` |
| Systemtest | Gesamter Lifecycle: Artikel anlegen → Bestand verwalten → Löschen |
| Abnahmetest | Fachabteilung prüft: Werden Bestände korrekt geführt? |

## 4. Testmethoden

- **Black-Box**: Testfälle aus der Spezifikation abgeleitet
- **White-Box**: Coverage-Analyse mit pytest-cov (Ziel: >= 90 %)
- **Grenzwertanalyse**: Kapazität (0, 1, 500, 1000), Bestand (0, -1)

## 5. Testumgebung

- Python 3.x
- pytest 9.x
- pytest-cov für Coverage-Messung

## 6. Testfälle (Übersicht)

| TC-ID | Kurzbeschreibung | Priorität |
|-------|-----------------|-----------|
| TC-LAGER-001 | Artikel anlegen – Normalfall | Hoch |
| TC-LAGER-002 | Artikel anlegen – Duplikat | Hoch |
| TC-LAGER-003 | Bestand erhöhen – Normalfall | Hoch |
| TC-LAGER-004 | Bestand reduzieren – Normalfall | Hoch |
| TC-LAGER-005 | Bestand reduzieren – unter Null | Hoch |
| TC-LAGER-006 | Artikel suchen – vorhanden | Mittel |
| TC-LAGER-007 | Artikel suchen – nicht vorhanden | Mittel |
| TC-LAGER-008 | Gesamtwert berechnen | Hoch |
| TC-LAGER-009 | Kapazitätsüberschreitung | Hoch |
| TC-LAGER-010 | Artikel unter Mindestbestand | Mittel |
| TC-LAGER-011 | Ungültige Lager-Kapazität | Niedrig |
| TC-LAGER-012 | Artikel mit leerer ID | Niedrig |
| TC-LAGER-013 | Negativer Preis | Niedrig |

## 7. Zeitplan

| Phase | Dauer |
|-------|-------|
| Testentwurf | 30 Min |
| Testdurchführung | 30 Min |
| Coverage-Analyse | 15 Min |
| Testbericht | 15 Min |

## 8. Akzeptanzkriterien

- Alle Testfälle TC-LAGER-001 bis TC-LAGER-010: **PASSED**
- Code Coverage >= 90 %
- Keine offenen Fehler mit Priorität „Hoch"
