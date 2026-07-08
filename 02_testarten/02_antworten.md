# 02_antworten.md – Baustein 02: Testarten

## Aufgabe 2a – Testbeispiele Webshop

| Teststufe | Konkretes Testbeispiel |
|-----------|------------------------|
| Unit-Test | `berechne_gesamtpreis()` mit 2 Artikeln, 0 % Rabatt → erwartet 69.97 |
| Integrationstest | Warenkorb + Bestellprozess: Artikel hinzufügen, Bestellung auslösen, prüfen ob Bestellung in DB gespeichert |
| Systemtest | Gesamter Bestellablauf: Browser öffnen → einloggen → Artikel suchen → in Warenkorb legen → bestellen → Bestellbestätigung erhalten |
| Abnahmetest | Fachabteilung testet: „Kann ich als Kunde 3 USB-Hubs bestellen, mit PayPal zahlen und eine Bestätigungsmail erhalten?" |

---

## Aufgabe 3 – Funktional vs. nicht-funktional

| Testszenario | Funktional | Nicht-funktional |
|-------------|-----------|------------------|
| Login mit korrekten Zugangsdaten klappt | x | |
| Seite lädt in unter 2 Sekunden | | x |
| Bestellung wird korrekt in Datenbank gespeichert | x | |
| System ist bei 1000 gleichzeitigen Nutzern stabil | | x |
| Passwort-Reset-Mail wird verschickt | x | |
| Alle Texte sind auf Deutsch (Lokalisierung) | | x |

---

## Aufgabe 4 – Regressionstests

**(a)** Ein Regressionstest prüft, ob nach einer Code-Änderung bestehende
Funktionen immer noch korrekt arbeiten. Man führt alte Tests erneut aus,
um sicherzustellen, dass keine neuen Fehler durch die Änderung entstanden sind.

**(b)** Nach dem Hinzufügen von „Mengenrabatt" müssten folgende Tests wiederholt werden:
1. `berechne_rabatt(100, 20)` → 80.0 (Standard-Rabatt intakt?)
2. `berechne_rabatt(0, 10)` → 0.0 (Grenzfall)
3. `berechne_rabatt(50, 0)` → 50.0 (kein Rabatt = kein Effekt?)

**(c)** Automatisierte Regressionstests sind wertvoll, weil sie:
- Nach jedem Commit automatisch laufen
- Zeit sparen (manuelles Testen wäre bei jeder Änderung zu aufwändig)
- Früh warnen, bevor der Code ins Produktivsystem kommt

---

## Aufgabe 5 – IHK-Stil

**(a)** Zuordnung:
1. Entwickler testen eigene Funktionen isoliert → **Unit-Test**
2. Module gemeinsam testen → **Integrationstest**
3. HR-Team führt Abnahmetest durch → **Abnahmetest**

**(b)** Fehlende Teststufe: **Systemtest**
Dort sollte das gesamte System gegen die Anforderungen getestet werden
(Vollständiger Workflow: Zeiterfassung → Auswertung → Bericht), bevor
der Kunde den Abnahmetest macht.

**(c)** Der Fehler hätte idealerweise auf **Systemtest-Ebene** gefunden werden
müssen. Im Systemtest wird das Gesamtsystem gegen die fachlichen
Anforderungen getestet – und falsche Urlaubstage sind eine fachliche
Fehlfunktion, die im Zusammenspiel aller Module sichtbar wird.

---

## Aufgabe 6 – Transfer

**(a)** Fehlende Teststufen:
- **Integrationstest**: Schnittstellen zwischen den Modulen werden nicht geprüft.
- **Systemtest**: Das Gesamtsystem wird nicht systematisch getestet.

**(b)** Risiken:
- Integration: Zeiterfassung schreibt Daten, aber Auswertung liest falsches Format → stille Datenkorruption.
- System: Die Software läuft 3 Wochen, bis jemand merkt, dass Urlaubstage falsch berechnet werden → hohe Folgekosten.

**(c)** Verbessertes V-Modell-Konzept für Zeiterfassung:
- **Unit-Test**: `berechne_arbeitszeit()` testen, `benutzer_anlegen()` testen
- **Integrationstest**: Zeiterfassung → Datenbank → Auswertung als Kette
- **Systemtest**: Mitarbeiter erfasst Zeit → Vorgesetzter genehmigt → Auswertung zeigt korrekte Monatsübersicht
- **Abnahmetest**: Betriebsrat prüft auf Einhaltung der Arbeitszeitgesetze

**(d)** Regressionstests allein reichen nicht: Sie stellen nur sicher, dass
Altes noch funktioniert, aber nicht, dass die Neuerung korrekt ist.
Es braucht immer auch neue Tests für die geänderte Funktionalität.

---

## Tandem-Aufgabe

Wir haben diskutiert, warum Teststufen aufeinander aufbauen:
- Unit-Tests prüfen Einzelteile, Integrationstests prüfen Verbindungen.
- Ohne Unit-Tests ist ein fehlgeschlagener Integrationstest nicht lokalisierbar
  (liegt's an Modul A oder B oder an der Schnittstelle?).
- System- und Abnahmetest machen nur Sinn, wenn die darunterliegenden Stufen
  stabil sind – sonst testet man ständig bekannte Fehler neu.

| Stufe | Wer testet? | Was? |
|-------|-------------|------|
| Unit-Test | Entwickler | `berechne_note()`, `validiere_menge()` |
| Integrationstest | Entwickler | Notenberechnung + Datenbank-Abfrage |
| Systemtest | QA-Team | Gesamter Prüfungsablauf: Login → Prüfung → Ergebnis |
| Abnahmetest | Lehrer | „Bekomme ich die richtige Note für meine Punktzahl?" |

---

## Active Recall

1. Auf Integrationstest-Ebene.
2. Der Auftraggeber / Kunde / Fachabteilung.
3. Systemtest prüft gegen die Spezifikation („Wurde es richtig gebaut?"),
   Abnahmetest prüft gegen die tatsächlichen Bedürfnisse („Wurde das Richtige gebaut?").
4. Performance-Test (Ladezeit < 2s), Lasttest (1000 Nutzer gleichzeitig).
5. Regressionstests werden nach jeder Code-Änderung ausgeführt, um
   sicherzustellen, dass bestehende Funktionen nicht kaputtgegangen sind.
