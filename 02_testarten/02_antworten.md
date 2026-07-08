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

# Ergebnis der Tandem-Aufgabe: Testkonzept Schulverwaltungssoftware

## 📊 Überblick über die Testmaßnahmen

| Teststufe             | Verantwortlich         | Fokus / Module / Szenarien                                                                            | Konkretes Beispiel im Schulkontext                                                                                                                                   |
| :-------------------- | :--------------------- | :---------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Unit-Test**         | Person A (Entwicklung) | Isolierte Funktionen in Modulen wie `notenberechnung.py`, `stundenplan.py`, `schueler_db.py`.         | Es wird geprüft, ob die Funktion `berechne_notenschnitt([2, 3, 1])` exakt `2.0` ausgibt.                                                                             |
| **Integrationstest**  | Person A (Entwicklung) | Schnittstellen und Datenfluss zwischen den Modulen (z.B. Übergabe von Noten an die Schülerdatenbank). | Es wird getestet, ob das Modul `notenberechnung.py` die Schülerschnittstelle nutzt und die berechnete Zeugnisnote fehlerfrei in `schueler_db.py` abspeichert.        |
| **Systemtest**        | Person B (Testteam)    | End-to-End-Szenarien des Gesamtsystems auf einer Testumgebung (Funktionalität, Last, DSGVO).          | Ein automatisierter Test simuliert, dass 50 Lehrer gleichzeitig am Zeugnistag Noten eintragen, um zu prüfen, ob der Server stabil bleibt und Berechtigungen greifen. |
| **Abnahmetest (UAT)** | Person B (Endnutzer)   | Formale Prüfung durch die echten Anwender gegen die Praxisanforderungen vor dem Go-Live.              | Schulleitung, Sekretariat und Lehrkräfte testen den realen Ablauf einer "Schülereinschulung" und der "Zeugnisgenerierung" und erteilen die Freigabe.                 |

---

## Tandem Aufgabe

## 🗣️ Zusammenfassung der Diskussion: Warum Teststufen aufeinander aufbauen

**Gegenargument (Warum nicht direkt System-/Abnahmetest?):** Man könnte meinen, dass ein direkter Start mit dem System- oder Abnahmetest Zeit spart, da man hierbei die Software sofort so testet, wie sie am Ende auch benutzt wird. Wenn das Gesamtsystem funktioniert, müssten die Einzelteile logischerweise auch stimmen.

**Unsere Erkenntnis (Warum das in der Praxis scheitert):**

1. **Unmöglichkeit der Fehlersuche (Nadel im Heuhaufen):** Wenn beim Abnahmetest das Zeugnis-PDF leer bleibt, weiß niemand, wo der Fehler liegt. Ist die Datenbankverbindung kaputt? Stimmt die Berechnung nicht? Oder hakt es beim PDF-Export? Unit- und Integrationstests isolieren die Fehlerquellen im Vorfeld.
2. **Kostenexplosion (Rule of Ten):** Ein Fehler, der erst im Abnahmetest durch die Schulleitung entdeckt wird, muss den gesamten Weg zurück in die Entwicklung. Die Behebung, das erneute Deployment und das erneute Testen kosten das Zehnfache an Zeit und Geld im Vergleich zu einem Unit-Test, der den Fehler sofort beim Tippen der Codezeile bemerkt hätte.
3. **Mangelnde Testabdeckung:** Beim Systemtest kann man unmöglich alle mathematischen Sonderfälle (z.B. Notenberechnung bei exakt 4,495 oder Division durch Null bei fehlenden Prüfungen) simulieren. Das geht effizient und lückenlos nur auf der untersten Ebene (Unit-Tests).

**Fazit:** Die Teststufen bilden ein Sicherheitsnetz. Die unteren Stufen sichern das Fundament (die Bausteine), während die oberen Stufen das fertige Gebäude (die Prozesse) prüfen. Ohne Fundament stürzt das System beim finalen Test unkontrolliert ein.
