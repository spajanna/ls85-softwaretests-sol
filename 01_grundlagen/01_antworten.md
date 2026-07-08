# 01_antworten.md – Baustein 01: Grundlagen der Softwaretests

## Aufgabe 2b – Warum reicht statisches Testen allein nicht aus?

Statisches Testen (Code-Reviews, Linter) erkennt nur syntaktische und
strukturelle Probleme, aber kein Laufzeitverhalten. Dynamische Tests
führen den Code tatsächlich aus und decken logische Fehler, Grenzfälle
und unerwartetes Verhalten auf, die statisch unsichtbar bleiben.

---

## Aufgabe 4 – IHK-Stil

**(a)** Zwei Risiken ohne Tests:
1. Produktionsausfälle durch unentdeckte Fehler (z. B. falsche Lagerbestände).
2. Hohe Kosten durch späte Fehlerbehebung (Rule of Ten).

**(b)** Defekt vs. Versagen:
- **Defekt**: Im Code der `berechne_gesamtpreis()` fehlt die Prüfung auf
  negative Artikelpreise.
- **Versagen**: Ein Kunde bestellt Artikel, erhält eine negative Rechnung
  und das System stürzt ab.

**(c)** Rule of Ten:
Ein Fehler, der in der Anforderungsphase 1 € kostet, verursacht in der
Wartung 1000 €. Frühzeitiges Testen (Prinzip 3) spart daher massiv Kosten,
weil Fehler direkt dort gefunden werden, wo sie entstehen.

---

## Aufgabe 5 – Transfer

**(a)** Argumentation für systematisches Testen:
Tests sind keine Zeitverschwendung, sondern Qualitätssicherung.
Prinzip 3 (Frühzeitiges Testen) zeigt: Je früher ein Fehler erkannt wird,
desto günstiger ist die Behebung – der Absturz der Ariane 5 (1996)
passierte wegen eines ungetesteten Zahlenüberlaufs und kostete 370 Mio. $.
Prinzip 2 (Vollständiges Testen ist unmöglich) bedeutet nicht, dass wir
gar nicht testen sollten – im Gegenteil: Wir müssen klug priorisieren.
Prinzip 7 („Keine Fehler" ≠ gutes System) erinnert uns: Die Software
muss auch die richtigen Anforderungen erfüllen.

**(b)** Möglicher Fehler für `berechne_urlaubstage()`:
- **Error**: Entwickler verwendet `eintrittsdatum - aktuelles_datum` statt
  einer korrekten Kalenderdifferenz.
- **Defect**: `urlaubstage = (heute - eintritt).days // 365 * arbeitstage_pro_woche`
  – ignoriert Schaltjahre und kündigt nur ganzzahlige Jahre.
- **Failure**: Ein Mitarbeiter bekommt 5 statt 6 Urlaubstage ausbezahlt.
- **Konsequenz**: Bei 1000 Mitarbeitern × 1 Tag × 200 € = 200.000 €
  Auszahlungsfehler pro Jahr.

**(c)** Prinzip 7 ist relevant: Selbst wenn `berechne_urlaubstage()` fehlerfrei
läuft (keine Exceptions), könnte der Algorithmus dennoch falsch sein
(z. B. gesetzliche Vorgaben nicht erfüllen). Fehlerfreiheit garantiert
keine Korrektheit.

---

## Tandem-Aufgabe

Wir haben Error/Defect/Failure mit einem Alltagsbeispiel erklärt:
- Error = Rezept falsch gelesen
- Defect = falsche Zutatenmenge im Rezept
- Failure = Kuchen schmeckt nicht

Die klarere Formulierung: „Der Error ist der Denkfehler des Kochs,
der Defect der Fehler im Rezept, das Failure der ungenießbare Kuchen."

---

## Active Recall

1. Error = falsche Handlung des Entwicklers (menschliches Versagen).
   Defect = die fehlerhafte Stelle im Code.
   Failure = das sichtbare Fehlverhalten zur Laufzeit.
2. Vollständiges Testen ist unmöglich (Prinzip 2), weil die Kombination
   aller Eingaben, Zustände und Systemkonfigurationen unendlich ist.
3. Reale Beispiele: Ariane-5-Absturz (Integer-Overflow), Therac-25
   (Strahlungsüberdosis durch Race-Condition), Y2K-Bug (2-stellige Jahreszahl).
