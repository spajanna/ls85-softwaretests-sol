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

- [ ] 🟢 Ich kenne die verschiedenen Testarten bereits
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

| Beschreibung                                                | Teststufe |
| ----------------------------------------------------------- | --------- |
| Testet einzelne Funktionen oder Methoden isoliert           |           |
| Prüft das Zusammenspiel mehrerer Module                     |           |
| Testet das gesamte System gegen die Anforderungen           |           |
| Der Auftraggeber prüft, ob seine Anforderungen erfüllt sind |           |

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
| --------- | ---------------------- |

Unit-Test Es wird isoliert geprüft, ob die Funktion in preisberechnung.py bei einem Warenwert von 100 € und 10 % Rabatt exakt 90.0 € zurückgibt.

Integrationstest Es wird getestet, ob warenkorb.py die Liste der hinzugefügten Artikel fehlerfrei an preisberechnung.py übergibt und die Summe korrekt eingelesen wird.

Ein automatisierter Test prüft den kompletten End-to-End-Weg im Shop: Ein (simulierter) Kunde legt Socken in den Warenkorb, geht zur Kasse, bezahlt per PayPal und der Lagerbestand verringert sich um 1.

Der Shopbetreiber (Product Owner) klickt sich selbst durch die Webseite, um zu prüfen, ob das Design den Vorgaben entspricht und der Kaufprozess für echte Kunden intuitiv verständlich ist.

**b)** In `code/starter.py` findest du die Funktion `berechne_gesamtpreis()`.
Schreibe einen einfachen manuellen Test (mit `print()`), der folgende Fälle prüft:

- Normaler Einkauf ohne Rabatt
- Einkauf mit 10 % Rabatt
- Leerer Warenkorb (Sonderfall!)

---

## Aufgabe 3 – Funktional vs. nicht-funktional 🟢

Ordne die folgenden Testszenarien zu:

| Testszenario                                         | Funktional | Nicht-funktional |
| ---------------------------------------------------- | ---------- | ---------------- |
| Login mit korrekten Zugangsdaten klappt              | x          |                  |
| Seite lädt in unter 2 Sekunden                       |            | x                |
| Bestellung wird korrekt in der Datenbank gespeichert | x          |                  |
| System ist bei 1000 gleichzeitigen Nutzern stabil    |            | x                |
| Passwort-Reset-Mail wird verschickt                  | x          |                  |
| Alle Texte sind auf Deutsch (Lokalisierung)          |            | x                |

---

## Aufgabe 4 – Regressionstests 🟡

**Szenario:**  
Dein Team hat den Rabattrechner aus Baustein 01 korrigiert.
Jetzt soll eine neue Funktion "Mengenrabatt" (ab 10 Stück = 5 % extra Rabatt) hinzugefügt werden.

**a)** Was ist ein Regressionstest? Erkläre mit eigenen Worten.

Ein Regressionstest ist das wiederholte Ausführen von bereits bestehenden Testfällen nach einer Codeänderung.

Das Ziel ist es, sicherzustellen, dass durch den neuen Code nicht versehentlich alte, bereits funktionierende Programmteile beschädigt wurden. Man prüft also, ob das System in alten Bereichen immer noch stabil läuft.

**b)** Welche bestehenden Tests müssten nach der Änderung als Regressionstests erneut ausgeführt werden? Liste mindestens 3 auf.

Der Standard-Rabattfall: Test mit 1 Produkt für 100 € und 20 % Rabatt. (Erwartetes Ergebnis muss weiterhin exakt 80.0 € sein – der Mengenrabatt darf hier nicht auslösen).

Der "Kein-Rabatt"-Fall: Test mit 1 Produkt für 50 € und 0 % Rabatt. (Erwartetes Ergebnis: 50.0 €).

Der Sonderfall "Leerer Warenkorb": Test mit 0 Produkten. (Erwartetes Ergebnis: 0.0 € – wichtig, um zu sehen, ob die neue Mengenprüfung bei leeren Listen eine Exception auslöst).

**c)** Warum ist das automatisierte Ausführen von Regressionstests besonders wertvoll?

Je größer eine Software wird, desto mehr alte Testfälle sammeln sich an. Das manuelle Testen aller alten Funktionen nach jedem kleinen Update ist zeitlich und wirtschaftlich unmöglich.

---

## Aufgabe 5 – IHK-Stil 🟡

**Prüfungsszenario:**

Ein Ausbildungsbetrieb entwickelt eine Zeiterfassungssoftware.
Das Entwicklungsteam hat folgende Testmaßnahmen geplant:

- Entwickler testen ihre eigenen Funktionen mit isolierten Tests
- Anschließend werden die Module Zeiterfassung, Benutzerverwaltung und Auswertung gemeinsam getestet
- Das HR-Team führt abschließend einen formalen Abnahmetest durch

**(a)** Ordnen Sie diese drei Maßnahmen den Teststufen im V-Modell zu. _(3 Punkte)_

Entwickler testen ihre eigenen Funktionen isoliert: Unit-Test
Module (Zeiterfassung, Benutzerverwaltung, Auswertung) gemeinsam testen: Integrationstest
HR-Team führt einen formalen Abnahmetest durch: Abnahmetest

**(b)** Nennen Sie eine weitere Teststufe, die im Plan fehlt, und beschreiben Sie, was dort getestet werden sollte. _(3 Punkte)_
Der Systemtest schließt die Lücke zwischen dem Integrationstest und dem Abnahmetest. Hierbei wird die gesamte Zeiterfassungssoftware als integriertes Gesamtprodukt in einer testnahen Umgebung (End-to-End) gegen die ursprünglichen Systemanforderungen (das Lasten-/Pflichtenheft) geprüft. Getestet werden hier neben funktionalen Abläufen auch nicht-funktionale Anforderungen wie die Performance unter Last, Datensicherheit oder das Verhalten bei System-Updates.

**(c)** Das HR-Team meldet beim Abnahmetest, dass Urlaubstage falsch berechnet werden. Auf welcher Teststufe hätte dieser Fehler idealerweise gefunden werden sollen? Begründen Sie. _(4 Punkte)_

Bei der Berechnung von Urlaubstagen handelt es sich um eine isolierte, mathematische und gesetzliche Programmierlogik (z. B. eine einzelne Funktion oder Methode im Code). Gemäß dem Grundprinzip „Frühzeitiges Testen spart Zeit und Geld“ hätte dieser isolierte Logikfehler direkt beim Schreiben des Quellcodes durch einen automatisierten Unit-Test des Entwicklers abgefangen werden müssen.

---

## Aufgabe 6 – Transfer: Teststrategie analysieren 🔴

**Transferaufgabe:**

Ein Betrieb hat folgendes Testkonzept für seine neue Zeiterfassungssoftware:

> „Unsere Entwickler testen ihre Funktionen kurz durch Ausführen des Programms.
> Sobald das System läuft, lassen wir das HR-Team damit arbeiten und
> schauen, ob Beschwerden kommen."

**a)** Analysiere kritisch: Welche Teststufen fehlen in diesem Konzept? Benenne sie mit Fachbegriff.

Automatisierte Unit-Tests (Komponententests): Das "kurze Durchgucken" der Entwickler ist unvollständig, nicht reproduzierbar und rein subjektiv.

Integrationstests: Es gibt keine Stufe, die das Zusammenspiel der einzelnen Module gezielt prüft.

Systemtests: Das Gesamtsystem wird vor der Übergabe an die Nutzer nicht unvoreingenommen gegen die eigentlichen Anforderungen (z. B. Datenschutz, Laststabilität) geprüft.

Formaler Abnahmetest (UAT): Das HR-Team als Testkaninchen im Produktivbetrieb zu nutzen, ist kein Abnahmetest, sondern ein unkontrollierter Live-Betrieb.

**b)** Beschreibe die konkreten Risiken für jeden fehlenden Test.
Was könnte im Produktivbetrieb passieren?

Ohne Unit-Tests: Isolierte Berechnungsfehler (z. B. falsche Rundungen bei Überstunden) bleiben unentdeckt. Im Produktivbetrieb führt das zu fehlerhaften Gehaltsabrechnungen, rechtlichen Konsequenzen und massivem Unmut in der Belegschaft.

Ohne Integrationstests: Die Module funktionieren zwar einzeln, stürzen aber ab, wenn sie Daten austauschen. Im Live-Betrieb könnte die auswertung.py beispielsweise die Daten der zeiterfassung.py nicht lesen, wodurch keine Monatsberichte gedruckt werden können.

Ohne Systemtests: Nicht-funktionale Kriterien wie Datensicherheit (DSGVO) oder Performance wurden nie geprüft. Im Alltag könnte das System zusammenbrechen, wenn sich morgens um 08:00 Uhr alle Mitarbeiter gleichzeitig einloggen, oder unbefugte Mitarbeiter könnten die Zeiten ihrer Kollegen einsehen.

**c)** Entwirf ein verbessertes Testkonzept nach dem V-Modell für diese Software
mit den Modulen: `zeiterfassung.py`, `benutzerverwaltung.py`, `auswertung.py`.
Ordne konkrete Testbeispiele jeder Teststufe zu.

Unit-Test | Isolierte Funktionen der einzelnen .py-Dateien prüfen. | In zeiterfassung.py wird per automatisiertem Test geprüft, ob die Funktion berechne_arbeitszeit("08:00", "16:30", pause=30) exakt 480 Minuten (8 Stunden) zurückgibt.

Integrationstest | Schnittstellen und Datenfluss zwischen den Modulen testen. | Es wird geprüft, ob das Modul auswertung.py die Benutzer-ID aus der benutzerverwaltung.py korrekt übernimmt, um die Stunden dem richtigen Mitarbeiter zuzuordnen.

Systemtest | Das Gesamtsystem auf einer Testumgebung (End-to-End) gegen die Anforderungen prüfen. | Ein automatisierter Lasttest simuliert 500 gleichzeitige Buchungsvorgänge um Punkt 08:00 Uhr, um sicherzustellen, dass der Server stabil bleibt und die DSGVO-Vorgaben (Rollenrechte) eingehalten werden.

Abnahmetest | Formale Prüfung durch die Fachabteilung (HR) vor dem Go-Live. | Ausgewählte HR-Mitarbeiter testen die Software in einer geschützten Sandbox-Umgebung anhand von echten Praxisszenarien (z. B. "Trage einen Krankheitsfall ein") und erteilen offiziell die Freigabe.

**d)** Begründe: Wäre ein ausschließlicher Regressionstest nach einer Änderung ausreichend?
Warum oder warum nicht?

Nein, ein ausschließlicher Regressionstest nach einer Änderung ist nicht ausreichend.

Begründung:
Ein Regressionstest prüft nur die Vergangenheit: Das primäre Ziel eines Regressionstests ist es sicherzustellen, dass bestehende, bereits funktionierende Programmteile durch eine Codeänderung (z. B. ein Update oder einen Bugfix) nicht versehentlich beschädigt wurden („Rückschritt-Test“).

Neue Funktionen bleiben ungetestet: Wenn mit der Änderung ein neues Feature eingebaut wurde (z. B. ein neues Eingabefeld für "Homeoffice-Zeiten" in der Zeiterfassungssoftware), kann ein reiner Regressionstest nicht überprüfen, ob diese neue Funktion überhaupt korrekt arbeitet. Die alten Testfälle wissen schlichtweg nichts von der Existenz des neuen Codes.

Fehlerkorrekturen werden nicht validiert: Selbst wenn die Änderung nur ein Bugfix war, zeigt der Regressionstest zwar, dass ringsherum nichts kaputtgegangen ist – er beweist aber nicht automatisch, dass der spezifische Fehler auch wirklich erfolgreich behoben wurde und unter allen Randbedingungen korrekt funktioniert.

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

_Beantworte diese Fragen aus dem Gedächtnis (Unterlagen geschlossen):_

1. Auf welcher Teststufe werden Schnittstellen zwischen Modulen getestet?

Antwort: Auf dem Integrationstest (bzw. der Integrationsstufe). Hier wird geprüft, ob die Daten sauber von einem Modul zum nächsten übergeben werden.

2. Wer führt typischerweise den Abnahmetest durch?

Antwort: Der Auftraggeber, die Fachabteilung (z. B. das HR-Team, die Buchhaltung) oder die Endnutzer der Software. Die Entwicklung ist hier meist nur noch als technischer Support im Hintergrund aktiv.

3. Was ist der Unterschied zwischen einem Systemtest und einem Abnahmetest?

Antwort: Systemtest: Wird vom Testteam/Entwicklungsteam durchgeführt. Geprüft wird das Gesamtsystem auf einer Testumgebung gegen die technische Spezifikation (Lasten-/Pflichtenheft)

Abnahmetest: Wird vom Kunden/Endnutzer durchgeführt. Geprüft wird die Software in einer realitätsnahen Umgebung gegen die tatsächlichen Geschäftsprozesse und die Usability

4. Nenne ein Beispiel für einen nicht-funktionalen Test.

Antwort:

- Sicherheitstest (Security): Prüfen, ob Passwörter verschlüsselt in der Datenbank liegen.

- Usability-Test: Prüfen, ob die Menüführung für den Nutzer verständlich ist.

5. Wann werden Regressionstests eingesetzt?

Antwort: Nach jeder Codeänderung – also nach einem Bugfix, nach einem Systemupdate, nach einem Refactoring oder wenn neue Funktionen hinzugefügt wurden. Sie dienen als Sicherheitsnetz, um sicherzustellen, dass die bereits funktionierenden "alten" Programmteile nicht unabsichtlich beschädigt wurden.

---

## Reflexion 🚦

- [x] 🟢 Ich kann alle Teststufen erklären und anwenden
- [ ] 🟡 Ich verstehe das Konzept, aber die Abgrenzung ist noch nicht ganz klar
- [ ] 🔴 Ich brauche noch Unterstützung

**Was nimmst du mit?**

> ---

---

_Bei Problemen → [Stuck Protocol](../stuck_protocol.md)_
