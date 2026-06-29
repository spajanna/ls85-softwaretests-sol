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
- [x] 🟡 Ich kenne manche Begriffe, aber nicht alle
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
| Testet einzelne Funktionen oder Methoden isoliert | Unit-Test|
| Prüft das Zusammenspiel mehrerer Module |Integrationstest |
| Testet das gesamte System gegen die Anforderungen | Systemtest|
| Der Auftraggeber prüft, ob seine Anforderungen erfüllt sind |Abnahmetest |

**Teststufen:**  · Integrationstest · Systemtest · Abnahmetest (User Acceptance Test)

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
| Unit-Test | die functionen zum berechenen der rabatte |
| Integrationstest | die berechnung der rabatte so wie die richtige anzeige des preises im ui |
| Systemtest |man versucht testweise waren mit rabat zu kaufen |
| Abnahmetest |der kunde versucht waren zu kaufen |

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
| Login mit korrekten Zugangsdaten klappt |x | |
| Seite lädt in unter 2 Sekunden | | x|
| Bestellung wird korrekt in der Datenbank gespeichert |x | |
| System ist bei 1000 gleichzeitigen Nutzern stabil | |x |
| Passwort-Reset-Mail wird verschickt | x| |
| Alle Texte sind auf Deutsch (Lokalisierung) | |x |

---

## Aufgabe 4 – Regressionstests 🟡

**Szenario:**  
Dein Team hat den Rabattrechner aus Baustein 01 korrigiert.
Jetzt soll eine neue Funktion "Mengenrabatt" (ab 10 Stück = 5 % extra Rabatt) hinzugefügt werden.

**a)** Was ist ein Regressionstest? ein regresssionstest fängt beim endpunkt an und testet sich zurück bis zum anfangspunkt

**b)** Welche bestehenden Tests müssten nach der Änderung als Regressionstests erneut ausgeführt werden? unit test, itegrations test und systemtest

**c)** Warum ist das automatisierte Ausführen von Regressionstests besonders wertvoll? kann schnell fehler finden

---

## Aufgabe 5 – IHK-Stil 🟡

**Prüfungsszenario:**

Ein Ausbildungsbetrieb entwickelt eine Zeiterfassungssoftware.
Das Entwicklungsteam hat folgende Testmaßnahmen geplant:

- Entwickler testen ihre eigenen Funktionen mit isolierten Tests
- Anschließend werden die Module Zeiterfassung, Benutzerverwaltung und Auswertung gemeinsam getestet
- Das HR-Team führt abschließend einen formalen Abnahmetest durch

**(a)** Ordnen Sie diese drei Maßnahmen den Teststufen im V-Modell zu. *(3 Punkte)*

1 unit test, 2 systemtest, 3 abnametest

**(b)** Nennen Sie eine weitere Teststufe, die im Plan fehlt, und beschreiben Sie, was dort getestet werden sollte. *(3 Punkte)*
Integrationstest - das zusammenspiel von den verschidenen modulen

**(c)** Das HR-Team meldet beim Abnahmetest, dass Urlaubstage falsch berechnet werden. Auf welcher Teststufe hätte dieser Fehler idealerweise gefunden werden sollen? Begründen Sie. *(4 Punkte)*
im integrationstest da dort das berechnen der urlaubstage zusammen mit den vorhandenen urlaubstagen berechnet wird und spter dargestellt

---

## Aufgabe 6 – Transfer: Teststrategie analysieren 🔴

**Transferaufgabe:**

Ein Betrieb hat folgendes Testkonzept für seine neue Zeiterfassungssoftware:

> „Unsere Entwickler testen ihre Funktionen kurz durch Ausführen des Programms.
> Sobald das System läuft, lassen wir das HR-Team damit arbeiten und
> schauen, ob Beschwerden kommen."

**a)** Analysiere kritisch: Welche Teststufen fehlen in diesem Konzept? Benenne sie mit Fachbegriff.
systemtest und Integrationstest

**b)** Beschreibe die konkreten Risiken für jeden fehlenden Test.
Was könnte im Produktivbetrieb passieren?
das zusammenspiel der zwischen den modulen könnte fhelerhaft sein

**c)** Entwirf ein verbessertes Testkonzept nach dem V-Modell für diese Software
mit den Modulen: `zeiterfassung.py`, `benutzerverwaltung.py`, `auswertung.py`.
Ordne konkrete Testbeispiele jeder Teststufe zu.

erst wird jede function selbstständig gestested danach wird ihr zusammenspiel getested danach wird einmal das gesammte system getesten danach wird es von HR getested

**d)** Begründe: Wäre ein ausschließlicher Regressionstest nach einer Änderung ausreichend?
Warum oder warum nicht?

je mehr testts und testarten desto besser

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

1. Auf welcher Teststufe werden Schnittstellen zwischen Modulen getestet?
2. Wer führt typischerweise den Abnahmetest durch?
3. Was ist der Unterschied zwischen einem Systemtest und einem Abnahmetest?
4. Nenne ein Beispiel für einen nicht-funktionalen Test.
5. Wann werden Regressionstests eingesetzt?

---

## Reflexion 🚦

- [ ] 🟢 Ich kann alle Teststufen erklären und anwenden
- [x] 🟡 Ich verstehe das Konzept, aber die Abgrenzung ist noch nicht ganz klar
- [ ] 🔴 Ich brauche noch Unterstützung

**Was nimmst du mit?**

> Tests sind toll!

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
