# 04_antworten.md – Baustein 04: Äquivalenzklassen & Grenzwertanalyse

## Aufgabe 0 – Grundbegriffe

**(a)** Ampel-Steuerung (1–5):
- Gültig: 1, 2, 3, 4, 5
- Ungültig: 0, 6, -1, 1.5, "drei"

**(b)** Eine Äquivalenzklasse ist eine Gruppe von Eingabewerten, die sich
gleich verhalten – wenn einer funktioniert, funktionieren alle.

**(c)** Beispiele aus dem Berufsalltag:
- Gültig: Bestellmenge 1–999 (AK: ganze Zahlen)
- Ungültig: Bestellmenge 0, 1000, -5, "Hallo"
- Kritischer Grenzwert: 0 → 1 (von ungültig zu gültig)

**(d)** Die Grundannahme: Alle Werte einer Klasse durchlaufen denselben
Code-Pfad und produzieren dasselbe Ergebnis. Einen zu testen genügt.

---

## Aufgabe 1 – Bestellformular „Menge"

**(a)** Äquivalenzklassen:

| AK-Nr | Klasse | Repräsentativer Wert | Gültig / Ungültig |
|-------|--------|---------------------|-------------------|
| AK1 | Ganze Zahlen 1–999 | 500 | Gültig |
| AK2 | Ganze Zahlen ≤ 0 | 0 | Ungültig |
| AK3 | Ganze Zahlen ≥ 1000 | 1000 | Ungültig |
| AK4 | Nicht-ganzzahlig / anderer Typ | "abc" | Ungültig |

**(b)** Grenzwerte:

| GW-Nr | Grenzwert | Erwartetes Ergebnis |
|-------|-----------|---------------------|
| GW1 | 0 | Ungültig |
| GW2 | 1 | Gültig |
| GW3 | 999 | Gültig |
| GW4 | 1000 | Ungültig |
| GW5 | -1 | Ungültig |

---

## Aufgabe 3 – Altersverifikation

**(a)** Grenzwerttabelle:

| Kategorie | Grenzen | Werte zum Testen |
|-----------|---------|------------------|
| Kinder (<12) | 0–11 | 0, 11 |
| Jugend (12–17) | 12, 17 | 12, 17 |
| Vollzugang (18+) | 18, max | 18, 120 |
| Ungültig | < 0 | -1 |

**(b)** Zusätzliche Fälle: -1 (negativ), 0 (Grenze), 150 (unrealistisch),
Kommazahlen (17.5 → Typfehler), leere Eingabe.

---

## Aufgabe 4 – IHK-Stil

**(a)** Äquivalenzklassen:
- Gültig: [0–29] (Note 6), [30–49] (Note 5), [50–66] (Note 4),
          [67–80] (Note 3), [81–91] (Note 2), [92–100] (Note 1)
- Ungültig: < 0, > 100, nicht ganzzahlig

**(b)** Grenzwerttabelle:

| Punkte | Note | Bemerkung |
|--------|------|-----------|
| -1 | ValueError | Unterer ungültiger Grenzwert |
| 0 | 6 | Untere Grenze Klasse 6 |
| 29 | 6 | Obere Grenze Klasse 6 |
| 30 | 5 | Untere Grenze Klasse 5 |
| 49 | 5 | Obere Grenze Klasse 5 |
| 50 | 4 | Untere Grenze Klasse 4 |
| 66 | 4 | Obere Grenze Klasse 4 |
| 67 | 3 | Untere Grenze Klasse 3 |
| 80 | 3 | Obere Grenze Klasse 3 |
| 81 | 2 | Untere Grenze Klasse 2 |
| 91 | 2 | Obere Grenze Klasse 2 |
| 92 | 1 | Untere Grenze Klasse 1 |
| 100 | 1 | Obere Grenze (gültig) |
| 101 | ValueError | Oberer ungültiger Grenzwert |

**(c)** Minimale Testfall-Auswahl: 15 Werte decken alle Klassen und Grenzen ab:
`[-1, 0, 29, 30, 49, 50, 66, 67, 80, 81, 91, 92, 100, 101, "abc"]`
Begründung: Jeweils der untere und obere Grenzwert pro Note,
plus die beiden ungültigen Grenzen (–1, 101) und einen Typfehler.
