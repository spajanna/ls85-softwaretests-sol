**Aufgabe 6:**

a)
Im Testkonzept fehlen wichtige Teststufen des V-Modells.

Es fehlen Unit-Tests, weil einzelne Funktionen nicht gezielt und isoliert getestet werden.
Außerdem fehlen Integrationstests, weil nicht geprüft wird, ob zeiterfassung.py, benutzerverwaltung.py und auswertung.py richtig zusammenarbeiten.
Auch ein richtiger Systemtest fehlt, bei dem die komplette Software systematisch geprüft wird.
Der Einsatz durch das HR-Team ist außerdem kein sauber geplanter Abnahmetest, sondern eher „ausprobieren im Alltag“.
Auch Regressionstests nach Änderungen sind nicht eingeplant.

b)
Ohne Unit-Tests können einfache Rechenfehler unbemerkt bleiben, zum Beispiel bei Pausen, Überstunden oder Urlaubstagen.

Ohne Integrationstests kann es passieren, dass die Module einzeln funktionieren, aber zusammen falsche Daten austauschen. Zum Beispiel könnte die Auswertung die erfassten Zeiten falsch übernehmen.

Ohne Systemtest merkt man vielleicht erst im Betrieb, dass komplette Abläufe nicht funktionieren, etwa Anmeldung, Zeiterfassung und Monatsauswertung zusammen.

Ohne echten Abnahmetest erkennt das HR-Team zu spät, dass fachliche Anforderungen fehlen oder falsch umgesetzt wurden.

Ohne Regressionstests können nach Änderungen alte Funktionen kaputtgehen, obwohl sie vorher funktioniert haben.

c)
Ein besseres Testkonzept nach dem V-Modell wäre:

Zuerst werden Unit-Tests durchgeführt. In zeiterfassung.py wird zum Beispiel geprüft, ob aus Startzeit, Endzeit und Pause die richtige Arbeitszeit berechnet wird. In benutzerverwaltung.py wird getestet, ob ein Benutzer korrekt angelegt wird. In auswertung.py wird geprüft, ob Wochenstunden richtig berechnet werden.

Danach folgen Integrationstests. Dabei wird getestet, ob ein Benutzer aus der Benutzerverwaltung Zeiten erfassen kann und ob diese Daten anschließend korrekt in der Auswertung erscheinen.

Anschließend kommt der Systemtest. Hier wird die komplette Software getestet: Ein Mitarbeiter meldet sich an, erfasst Arbeitszeiten, trägt Pausen ein und am Monatsende wird eine korrekte Auswertung erstellt.

Zum Schluss führt das HR-Team einen formalen Abnahmetest durch. Dabei prüft HR mit realistischen Fällen, ob die Software fachlich passt, zum Beispiel bei Urlaub, Krankheit, Überstunden und Monatsberichten.

Nach Änderungen sollten zusätzlich Regressionstests laufen, damit alte Funktionen weiterhin korrekt bleiben.

d)
Nein, nur Regressionstests reichen nicht aus.

Regressionstests prüfen hauptsächlich, ob alte Funktionen nach einer Änderung noch funktionieren. Sie testen aber nicht automatisch, ob eine neue Funktion korrekt entwickelt wurde.

Wenn zum Beispiel eine neue Urlaubsberechnung eingebaut wird, müssen dafür neue Unit-Tests, Integrationstests und Systemtests geschrieben werden. Regressionstests sind wichtig, aber sie ersetzen kein vollständiges Testkonzept.

**Aufgabe Tandem**

| Bereich | Verantwortlich | Teststufe | Konkrete Testmaßnahme |
|---|---|---|---|
| Schülermodul | Person A | Unit-Test | Prüfen, ob ein neuer Schüler mit Name, Klasse und Geburtsdatum korrekt angelegt wird. |
| Notenmodul | Person A | Unit-Test | Prüfen, ob eine Note korrekt gespeichert und einem Schüler zugeordnet wird. |
| Fehlzeitenmodul | Person A | Unit-Test | Prüfen, ob eine Fehlzeit mit Datum und Grund korrekt gespeichert wird. |
| Benutzerverwaltung | Person A | Unit-Test | Prüfen, ob sich Lehrer mit gültigen Zugangsdaten anmelden können. |
| Schülermodul + Notenmodul | Person A | Integrationstest | Prüfen, ob eine Note dem richtigen Schüler zugeordnet und später wieder angezeigt wird. |
| Schülermodul + Fehlzeitenmodul | Person A | Integrationstest | Prüfen, ob Fehlzeiten beim richtigen Schüler gespeichert und in der Übersicht angezeigt werden. |
| Benutzerverwaltung + Rechteverwaltung | Person A | Integrationstest | Prüfen, ob Lehrer nur ihre eigenen Klassen sehen und bearbeiten dürfen. |
| Gesamte Schulverwaltungssoftware | Person B | Systemtest | Ein Lehrer meldet sich an, wählt eine Klasse aus, trägt Noten ein und kontrolliert die Schülerübersicht. |
| Fehlzeitenverwaltung | Person B | Systemtest | Eine Lehrkraft trägt eine Fehlzeit ein, entschuldigt sie später und prüft, ob der Status korrekt angezeigt wird. |
| Zeugnis/Auswertung | Person B | Systemtest | Das System erstellt aus gespeicherten Noten eine korrekte Auswertung oder Zeugnisübersicht. |
| Abnahme durch Schule | Person B | Abnahmetest | Lehrer, Sekretariat und Schulleitung testen typische Arbeitsabläufe mit realistischen Daten. |
| Fachliche Prüfung | Person B | Abnahmetest | Die Schule prüft, ob Noten, Fehlzeiten, Klassenlisten und Benutzerrechte den Anforderungen entsprechen. |
| Kritische Funktionen | Zusammen | Überprüfung | Prüfen, ob Login, Rechte, Schülerdaten, Noten, Fehlzeiten, Auswertungen und Datenschutz abgedeckt sind. |

## Erklärung für den Tandempartner

Teststufen bauen aufeinander auf, weil Fehler so früher und einfacher gefunden werden. Zuerst prüft man einzelne Funktionen mit Unit-Tests, danach das Zusammenspiel der Module mit Integrationstests und erst dann das komplette System. Wenn man direkt mit Systemtest oder Abnahmetest startet, ist oft unklar, wo genau ein Fehler liegt. Außerdem würde das HR-/Schulteam Zeit verlieren, wenn grundlegende technische Fehler erst bei der Abnahme auffallen.