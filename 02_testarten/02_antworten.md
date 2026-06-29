## Aufgabe 3 – Funktional vs. nicht-funktional 🟢

Ordne die folgenden Testszenarien zu:

| Testszenario | Funktional | Nicht-funktional |
|-------------|-----------|-----------------|
| Login mit korrekten Zugangsdaten klappt | funk | |
| Seite lädt in unter 2 Sekunden | | nicht funk |
| Bestellung wird korrekt in der Datenbank gespeichert | funk | |
| System ist bei 1000 gleichzeitigen Nutzern stabil | | nicht funk|
| Passwort-Reset-Mail wird verschickt | funk | |
| Alle Texte sind auf Deutsch (Lokalisierung) | |nicht funk |

---

## Aufgabe 4 – Regressionstests 🟡

**Szenario:**  
Dein Team hat den Rabattrechner aus Baustein 01 korrigiert.
Jetzt soll eine neue Funktion "Mengenrabatt" (ab 10 Stück = 5 % extra Rabatt) hinzugefügt werden.

**a)** Was ist ein Regressionstest? Erkläre mit eigenen Worten.
Nach der Aenderungen sollte alle Teste wieder ausgefuehrt werden, damit sicher zu sein, dass was neues nicht was altes gebrochen hat.

**b)** Welche bestehenden Tests müssten nach der Änderung als Regressionstests erneut ausgeführt werden? Liste mindestens 3 auf.
Alle: Unit, Integration, System

**c)** Warum ist das automatisierte Ausführen von Regressionstests besonders wertvoll?
Automatisierung spart Zeit. Regressionstests gewaehrleisten, dass das System immer noch arbeitsfaehig ist.
---

## Aufgabe 5 – IHK-Stil 🟡

**Prüfungsszenario:**

Ein Ausbildungsbetrieb entwickelt eine Zeiterfassungssoftware.
Das Entwicklungsteam hat folgende Testmaßnahmen geplant:

- Entwickler testen ihre eigenen Funktionen mit isolierten Tests
- Anschließend werden die Module Zeiterfassung, Benutzerverwaltung und Auswertung gemeinsam getestet
- Das HR-Team führt abschließend einen formalen Abnahmetest durch

**(a)** Ordnen Sie diese drei Maßnahmen den Teststufen im V-Modell zu. *(3 Punkte)*
1Entwickler testen ihre eigenen Funktionen mit isolierten Tests - UnitTests
2Anschließend werden die Module Zeiterfassung, Benutzerverwaltung und Auswertung gemeinsam getestet - Integrationtest
3Das HR-Team führt abschließend einen formalen Abnahmetest durch AbnahmeTest

**(b)** Nennen Sie eine weitere Teststufe, die im Plan fehlt, und beschreiben Sie, was dort getestet werden sollte. *(3 Punkte)*
System Test, wie das System funktioniert.

**(c)** Das HR-Team meldet beim Abnahmetest, dass Urlaubstage falsch berechnet werden. Auf welcher Teststufe hätte dieser Fehler idealerweise gefunden werden sollen? Begründen Sie. *(4 Punkte)*
Unit Test
---

## Aufgabe 6 – Transfer: Teststrategie analysieren 🔴

**Transferaufgabe:**

Ein Betrieb hat folgendes Testkonzept für seine neue Zeiterfassungssoftware:

> „Unsere Entwickler testen ihre Funktionen kurz durch Ausführen des Programms.
> Sobald das System läuft, lassen wir das HR-Team damit arbeiten und
> schauen, ob Beschwerden kommen."

**a)** Analysiere kritisch: Welche Teststufen fehlen in diesem Konzept? Benenne sie mit Fachbegriff.
Unit Test, Integrationtest, Systemtest.

**b)** Beschreibe die konkreten Risiken für jeden fehlenden Test.
Was könnte im Produktivbetrieb passieren?
Eine Funktion berechnet was falsch -> Dieser Fehler wird in den Integration-Bereich uebergeben und ihn beeinflussen. -> Daraus bekommt man ein unstabiles System -> User hat eine Krise. 

**c)** Entwirf ein verbessertes Testkonzept nach dem V-Modell für diese Software
mit den Modulen: `zeiterfassung.py`, `benutzerverwaltung.py`, `auswertung.py`.
Ordne konkrete Testbeispiele jeder Teststufe zu.

1. Jede Klasse soll Unit-Tests haben.
2. Integrationtest
3. Systemtest
4. Abnahmetest

**d)** Begründe: Wäre ein ausschließlicher Regressionstest nach einer Änderung ausreichend?
Warum oder warum nicht?
Nicht ausreichend. Regressionstest prueft den Alten-Code, nicht der neue. Es sollte auch test fuer die neue Funktionalitaet gemacht werden.

