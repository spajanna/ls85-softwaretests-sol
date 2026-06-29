# Baustein 02 – Testarten 🟢

> **Schwierigkeit:** 🟢 Grundlagen  
> **Zeitrahmen:** ca. 90 Minuten  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/buC7L4PjPh" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 02: Testarten</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [*] 🟢 Ich kenne die verschiedenen Testarten bereits
- [ ] 🟡 Ich kenne manche Begriffe, aber nicht alle
- [ ] 🔴 Das Thema ist mir neu

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … die vier Teststufen (Unit, Integration, System, Abnahmetest) benennen und erklären
- 🟢 … das V-Modell skizzieren und die Testebenen korrekt einordnen
- 🟢 … den Unterschied zwischen funktionalen und nicht-funktionalen Tests beschreiben
- 🟡 … erklären, was Regressionstests sind und wann sie eingesetzt werden
- 🟡 … Testarten einem Praxisszenario korrekt zuordnen

---

## Hintergrund

Software wird selten als Ganzes entwickelt und dann einmal getestet.
In der Praxis gibt es mehrere Teststufen, die aufeinander aufbauen – ähnlich wie bei der
Qualitätskontrolle in der Fertigung: Erst werden Einzelteile geprüft, dann Baugruppen,
dann das Gesamtprodukt, und schließlich der Kunde nimmt ab.

Das **V-Modell** visualisiert diesen Zusammenhang zwischen Entwicklungs- und Teststufen.

---

## Aufgabe 1 – Die vier Teststufen 🟢

Lies die Beschreibungen und ordne sie den Teststufen zu.

| Beschreibung | Teststufe |
|-------------|-----------|
| Testet einzelne Funktionen oder Methoden isoliert | Unit-Test |
| Prüft das Zusammenspiel mehrerer Module | Integrationstest |
| Testet das gesamte System gegen die Anforderungen | Systemtest |
| Der Auftraggeber prüft, ob seine Anforderungen erfüllt sind | Abnahmetest |

**Teststufen:** Unit-Test · Integrationstest · Systemtest · Abnahmetest (User Acceptance Test)

Trage die Tabelle ausgefüllt in `starter.py` als Kommentar ein.

---

## Aufgabe 2 – Praxisszenario Webshop 🟢

Ein Team entwickelt einen einfachen Online-Webshop mit folgenden Komponenten:
- `preisberechnung.py` – berechnet Gesamtpreis mit Rabatt
- `warenkorb.py` – verwaltet Artikel im Warenkorb
- `bestellprozess.py` – verarbeitet eine Bestellung (Warenkorb + Zahlung + Lager)
- Gesamtsystem: Benutzer legt Artikel in Warenkorb und bestellt

**a)** Nenne je ein Testbeispiel für jede Teststufe in diesem Webshop.

| Teststufe | Konkretes Testbeispiel |
|-----------|----------------------|
| Unit-Test | Teste preisberechnung.py: Ein Artikel kostet 100 €, Rabatt 10 %. Erwartetes Ergebnis: Gesamtpreis = 90 € |
| Integrationstest | Teste Zusammenspiel von warenkorb.py und preisberechnung.py: Zwei Artikel werden in den Warenkorb gelegt, danach wird der Gesamtpreis inklusive Rabatt korrekt berechnet. |
| Systemtest | Teste den kompletten Webshop-Ablauf: Benutzer legt Artikel in den Warenkorb, geht zur Kasse, bezahlt und die Bestellung wird erfolgreich abgeschlossen. |
| Abnahmetest | Kunde oder Product Owner prüft: Als Benutzer möchte ich Artikel kaufen können. Ein echter Kaufprozess wird aus Nutzersicht durchgeführt und akzeptiert, wenn Warenkorb, Preis, Zahlung und Bestellbestätigung korrekt funktionieren. |

**b)** In `code/starter.py` findest du die Funktion `berechne_gesamtpreis()`.
Schreibe einen einfachen manuellen Test (mit `print()`), der folgende Fälle prüft:
- Normaler Einkauf ohne Rabatt
- Einkauf mit 10 % Rabatt
- Leerer Warenkorb (Sonderfall!)

---

## Aufgabe 3 – Funktional vs. nicht-funktional 🟢

Ordne die folgenden Testszenarien zu:

| Testszenario | Funktional | Nicht-funktional |
|-------------|-----------|-----------------|
| Login mit korrekten Zugangsdaten klappt | * | |
| Seite lädt in unter 2 Sekunden | | * |
| Bestellung wird korrekt in der Datenbank gespeichert | * | |
| System ist bei 1000 gleichzeitigen Nutzern stabil | | * |
| Passwort-Reset-Mail wird verschickt | * | |
| Alle Texte sind auf Deutsch (Lokalisierung) | | * |

---

## Aufgabe 4 – Regressionstests 🟡

**Szenario:**  
Dein Team hat den Rabattrechner aus Baustein 01 korrigiert.
Jetzt soll eine neue Funktion "Mengenrabatt" (ab 10 Stück = 5 % extra Rabatt) hinzugefügt werden.

**a)** Was ist ein Regressionstest? Erkläre mit eigenen Worten.
Ein Regressionstest prüft, ob nach einer Änderung am Code noch alles funktioniert, was vorher schon funktioniert hat.
In diesem Fall:
Der Rabattrechner wurde geändert, weil ein neuer Mengenrabatt ab 10 Stück eingebaut wird. Regressionstests sollen sicherstellen, dass dadurch die alten Funktionen nicht kaputtgehen, zum Beispiel normale Preisberechnung oder 10-%-Rabatt.

**b)** Welche bestehenden Tests müssten nach der Änderung als Regressionstests erneut ausgeführt werden? Liste mindestens 3 auf.
1- Normaler Einkauf ohne Rabatt -> Prüfen, ob die normale Preisberechnung weiterhin korrekt ist.
2- Einkauf mit 10 % Rabatt ->	Prüfen, ob der bisherige Rabatt weiterhin richtig berechnet wird.
3- Leerer Warenkorb -> Prüfen, ob der Sonderfall weiterhin 0.0 ergibt und keine Exception wirft.

**c)** Warum ist das automatisierte Ausführen von Regressionstests besonders wertvoll?
weil sie schnell und zuverlässig zeigen, ob durch eine neue Änderung alte Funktionen kaputtgegangen sind.

---

## Aufgabe 5 – IHK-Stil 🟡

**Prüfungsszenario:**

Ein Ausbildungsbetrieb entwickelt eine Zeiterfassungssoftware.
Das Entwicklungsteam hat folgende Testmaßnahmen geplant:

- Entwickler testen ihre eigenen Funktionen mit isolierten Tests
- Anschließend werden die Module Zeiterfassung, Benutzerverwaltung und Auswertung gemeinsam getestet
- Das HR-Team führt abschließend einen formalen Abnahmetest durch

**(a)** Ordnen Sie diese drei Maßnahmen den Teststufen im V-Modell zu. *(3 Punkte)*
- Entwickler testen ihre eigenen Funktionen mit isolierten Tests -> Unit-Test / Komponententest
- Module Zeiterfassung, Benutzerverwaltung und Auswertung werden gemeinsam getestet -> Integrationstest
- HR-Team führt abschließend einen formalen Abnahmetest durch	-> Abnahmetest / Akzeptanztest

**(b)** Nennen Sie eine weitere Teststufe, die im Plan fehlt, und beschreiben Sie, was dort getestet werden sollte. *(3 Punkte)*
Systemtest fehlt. Beim Systemtest wird die komplette Zeiterfassungssoftware als Gesamtsystem getestet. Dabei prüft man zum Beispiel:
- Kann ein Mitarbeiter Arbeitszeiten erfassen?
- Werden Pausen korrekt berechnet?
- Werden Urlaubstage richtig angezeigt?

**(c)** Das HR-Team meldet beim Abnahmetest, dass Urlaubstage falsch berechnet werden. Auf welcher Teststufe hätte dieser Fehler idealerweise gefunden werden sollen? Begründen Sie. *(4 Punkte)*
Systemtest. Die falsche Berechnung von Urlaubstagen betrifft eine fachliche Funktion der gesamten Zeiterfassungssoftware. Beim Systemtest wird geprüft, ob das komplette System aus Benutzersicht korrekt funktioniert. Dazu gehört auch, ob Urlaubstage richtig berechnet, gespeichert und angezeigt werden.

---

## Aufgabe 6 – Transfer: Teststrategie analysieren 🔴

**Transferaufgabe:**

Ein Betrieb hat folgendes Testkonzept für seine neue Zeiterfassungssoftware:

> „Unsere Entwickler testen ihre Funktionen kurz durch Ausführen des Programms.
> Sobald das System läuft, lassen wir das HR-Team damit arbeiten und
> schauen, ob Beschwerden kommen."

**a)** Analysiere kritisch: Welche Teststufen fehlen in diesem Konzept? Benenne sie mit Fachbegriff.

**b)** Beschreibe die konkreten Risiken für jeden fehlenden Test.
Was könnte im Produktivbetrieb passieren?

**c)** Entwirf ein verbessertes Testkonzept nach dem V-Modell für diese Software
mit den Modulen: `zeiterfassung.py`, `benutzerverwaltung.py`, `auswertung.py`.
Ordne konkrete Testbeispiele jeder Teststufe zu.

**d)** Begründe: Wäre ein ausschließlicher Regressionstest nach einer Änderung ausreichend?
Warum oder warum nicht?

Schreibe deine Analyse in `02_antworten.md`.

---

## Tandem-Aufgabe 👥

**Szenario für zwei Personen:**

Ihr seid das Testteam für eine Schulverwaltungssoftware.
Eure Aufgabe: Erstellt gemeinsam einen Überblick über alle Testmaßnahmen.

- Person A: Entwirft die Unit-Tests und Integrationstests (welche Module, welche Schnittstellen?)
- Person B: Plant den Systemtest und Abnahmetest (welche Szenarien, wer testet?)
- Zusammen: Prüft, ob alle kritischen Funktionen abgedeckt sind

Haltet euer Ergebnis als Tabelle in `02_antworten.md` fest.

**Erkläre deinem Tandempartner:** Warum bauen Teststufen aufeinander auf und warum kann man nicht direkt mit dem Systemtest oder Abnahmetest starten? Dein Tandempartner hält dagegen und ihr diskutiert 2–3 Minuten.

---

## Active Recall – Mini-Quiz 🧠

*Beantworte diese Fragen aus dem Gedächtnis (Unterlagen geschlossen):*
Beispiel: 
Nach Änderungen am Code, um zu prüfen, ob alte Funktionen noch funktionieren.

1. Auf welcher Teststufe werden Schnittstellen zwischen Modulen getestet?
Integrationstest

2. Wer führt typischerweise den Abnahmetest durch?
Kunde, Fachabteilung oder Product Owner

3. Was ist der Unterschied zwischen einem Systemtest und einem Abnahmetest?
Systemtest: prüft das komplette System technisch/fachlich. Abnahmetest: prüft, ob der Kunde das System akzeptiert.

4. Nenne ein Beispiel für einen nicht-funktionalen Test.
Seite lädt in unter 2 Sekunden oder System bleibt bei 1000 Nutzern stabil.

5. Wann werden Regressionstests eingesetzt?
Nach Änderungen am Code, um zu prüfen, ob alte Funktionen noch funktionieren.

---

## Reflexion 🚦

- [*] 🟢 Ich kann alle Teststufen erklären und anwenden
- [ ] 🟡 Ich verstehe das Konzept, aber die Abgrenzung ist noch nicht ganz klar
- [ ] 🔴 Ich brauche noch Unterstützung

**Was nimmst du mit?**

> Ich nehme mit, dass verschiedene Teststufen wichtig sind und aufeinander aufbauen: Erst einzelne Funktionen testen, dann Schnittstellen, dann das Gesamtsystem und am Ende die Abnahme. Außerdem sind Regressionstests wichtig, damit nach Änderungen alte Funktionen weiterhin funktionieren.
---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
