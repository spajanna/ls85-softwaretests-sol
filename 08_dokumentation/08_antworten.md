## Aufgabe 0 – Grundbegriffe: Testdokumentation einordnen 🟢

a) Aussage,Dokument
"„Wir werden alle Module mit pytest testen.""",Testplan
"„TC-007 ist fehlgeschlagen: Bestand wurde auf -5 gesetzt.""",Testprotokoll
"„8 von 10 Tests bestanden, 1 Fehler offen.""",Testbericht
"„Abnahmekriterium: Coverage > 80 %.""",Testplan
"„Empfehlung: System ist abnahmebereit.""",Testbericht

b) Erstellungszeitpunkt der Dokumente
Vor dem Testen: Testplan

Während des Testens: Testprotokoll

Nach dem Testen: Testbericht

c) Wenn ich Tests lediglich ausführe, ohne die Ergebnisse zu dokumentieren, fehlt uns jeglicher objektive Nachweis darüber, was genau wann, wie und von wem geprüft wurde. Ohne diese schriftlichen Protokolle und Berichte können wir Fehler nicht systematisch nachverfolgen, der aktuelle Qualitätsstatus der Software bleibt für das restliche Team oder Kunden unsichtbar, und eine strukturierte, rechtssichere Abnahme des Gesamtsystems ist unmöglich.

## Aufgabe 1 – Testfall-Dokumentation 🟡

## Aufgabe 2 – Testplan erstellen 🟡

Testplan – Lagerbestandsverwaltung (Python)

1. Stammdaten
   Projektname: Lagerbestandsverwaltung

Datum: 29.06.2026

Autor/in: Fachinformatiker/in für Anwendungsentwicklung (Dein Name)

Version: 1.0

2. Testumfang & Ziele
   In Scope (Was wird getestet?)
   Gegenstand der Tests ist die komplette funktionale Logik der drei entwickelten Python-Module:

artikel.py: Korrekte Initialisierung von Artikel-Objekten, Typprüfungen und Wertevalidierungen (z. B. keine negativen Preise/Bestände).

lager.py: Kernfunktionen der Lagerverwaltung (Artikel anlegen, Bestände erhöhen/reduzieren, Dublettenprüfung, Einhalten der maximalen Lagerkapazität, Löschen und Suchen von Artikeln).

bericht.py: Auswertungsfunktionen (Ermittlung des Gesamtlagerwertes, Identifikation von Artikeln unter dem Mindestbestand).

Out of Scope (Was wird NICHT getestet?)
Grafische Benutzeroberflächen (GUIs) oder CLI-Eingabemasken, da es sich um eine reine Backend-Logik handelt.

Persistenzschichten (Datenbanken, Datei-I/O), da die Datenhaltung aktuell nur zur Laufzeit im Arbeitsspeicher stattfindet.

Sicherheitsprüfungen (Zugriffsrechte, Verschlüsselung).

3. Teststufen
   Der Testprozess gliedert sich in folgende aufeinander aufbauende Stufen:

Unit-Tests (Modultests): Isolierte Überprüfung der einzelnen Methoden und Klassen in artikel.py und lager.py. Mocking ist aufgrund der In-Memory-Datenhaltung nicht zwingend erforderlich.

Integrationstests: Überprüfung des Zusammenspiels zwischen dem Lager-Objekt und der Berichtsgenerierung in bericht.py (Funktioniert die Werteermittlung über alle im Lager befindlichen Artikelobjekte hinweg?).

System- bzw. Abnahmetest: Black-Box-Prüfung typischer Geschäftsprozesse (z. B. "Wareneingang -> Bestandserhöhung -> Grenzwertprüfung -> Berichtsausgabe") anhand realitätsnaher Beispieldaten.

4. Testmethoden & -techniken
   White-Box-Testing: Strukturorientiertes Testen zur Absicherung aller Code-Pfade. Fokus liegt auf dem Durchlaufen aller if-Zweige bei Fehlermeldungen (Exceptions).

Black-Box-Testing: Spezifikationsorientierte Prüfung der Methoden-Schnittstellen auf korrekte Rückgabewerte.

Äquivalenzklassenbildung & Grenzwertanalyse:

Gültige Werte: Positive Mengen, korrekte Artikel-IDs.

Ungültige Werte / Grenzwerte: Menge = 0, negative Bestände, Reduzierung unter den vorhandenen Bestand, Überschreiten der Lagerkapazitätsgrenze exakt um 1 Stück.

5. Testwerkzeuge & Testumgebung
   Test-Framework: pytest (Version 8.x) zur automatisierten Testausführung.

Coverage-Tool: pytest-cov zur Ermittlung der Testabdeckung (C0/C1-Abdeckung).

Entwicklungsumgebung: Python 3.11+ auf lokalen Entwicklungs-Workstations.

CI/CD (optional): GitHub Actions / GitLab CI zur automatischen Testausführung bei jedem Push.

Phase / Teststufe,Geplanter Zeitraum,Verantwortlich
Testfall-Erstellung & Spezifikation,Tag 1,Fachinformatiker/in
"Durchführung Unit-Tests (artikel, lager)",Tag 2 - 3,Fachinformatiker/in
Durchführung Integrationstests (bericht),Tag 4,Fachinformatiker/in
Systemtests & Review des Coverage-Reports,Tag 5 (Vormittag),Fachinformatiker/in
Erstellung Testbericht & Freigabe,Tag 5 (Nachmittag),Fachinformatiker/in / Projektleitung

7. Abnahmekriterien (Exit Criteria)
   Das System gilt erst dann als erfolgreich getestet und bereit für den produktiven Einsatz, wenn folgende Kriterien ausnahmslos erfüllt sind:

100 % funktionale Erfolgsquote: Alle definierten Testfälle innerhalb der pytest-Suite müssen erfolgreich durchlaufen (PASSED). Es dürfen keine FAILED- oder ERROR-Zustände offen sein.

Code Coverage: Die durch pytest-cov ermittelte Zeilenabdeckung (Statement Coverage) muss für alle drei Kernmodule mindestens 85 % betragen.

Robuste Fehlerbehandlung: Alle definierten Falscheingaben (Grenzwerte) müssen nachweislich durch das gezielte Werfen der erwarteten Exceptions (ValueError, KeyError) abgefangen werden (durch pytest.raises abgesichert).

## Aufgabe 3 – Coverage-Bericht interpretieren 🔴

a) Durchführung des Coverage-Laufs
Ich habe pytest-cov installiert und die Testabdeckung im Terminal mit dem vorgegebenen Befehl analysiert. Die Testsuite lief fehlerfrei durch.

b) Interpretation des BerichtsAktuelle Coverage: Ohne die zusätzlichen Tests lag meine Abdeckung bei ca. 80 %.Nicht getestete Zeilen ("missing"): Es wurden vor allem die Zeilen innerhalb der Fehlerbehandlungen (die raise-Anweisungen) nicht getestet. Dazu gehörten die Validierungen in Artikel.**post_init** (negative Preise, leere IDs), der Kapazitäts-Check im Konstruktor von Lager sowie die KeyError- und ValueError-Zweige beim Erhöhen oder Reduzieren von Beständen. Zudem wurde die Methode artikel_loeschen überhaupt nicht aufgerufen.Fehlende Zweige: Es fehlten die "Else"- bzw. Alternativ-Pfade der if-Bedingungen, welche die ungültigen Grenzwerte (z. B. Menge $\le 0$ oder unzureichender Bestand) abfangen.

c) Zusätzliche Tests für >= 90 % Coverage
Um die Abdeckung auf das Maximum zu bringen, habe ich die Klasse TestLagerCoverage in der Datei ergänzt. Hier sind die Tests, die ich geschrieben habe, um gezielt die "missing"-Zeilen anzuspringen:

class TestLagerCoverage:
def test_artikel_validierung_fehler(self):
"""Prüft die Exceptions in Artikel.**post_init**"""
with pytest.raises(ValueError, match="Artikel-ID darf nicht leer sein"):
Artikel("", "Test", 10.0)
with pytest.raises(ValueError, match="Preis darf nicht negativ sein"):
Artikel("A1", "Test", -1.0)

    def test_lager_kapazitaet_fehler(self):
        """Prüft den Konstruktor-Check des Lagers"""
        with pytest.raises(ValueError, match="Kapazität muss positiv sein"):
            Lager(kapazitaet=0)

    def test_bestand_fehlerfaelle(self, leeres_lager):
        """Prüft die Fehlermeldungen bei falschen Mengen/IDs"""
        with pytest.raises(ValueError, match="Menge muss positiv sein"):
            leeres_lager.bestand_erhoehen("A1", 0)
        with pytest.raises(KeyError, match="nicht gefunden"):
            leeres_lager.bestand_erhoehen("A1", 10)

    def test_artikel_loeschen_inklusive_fehler(self):
        """Prüft erfolgreiches Löschen und den KeyError bei fehlender ID"""
        lager = Lager(100)
        lager.artikel_anlegen(Artikel("A1", "Test", 5.0))
        lager.artikel_loeschen("A1")
        assert lager.artikel_anzahl == 0

        with pytest.raises(KeyError, match="nicht gefunden"):
            lager.artikel_loeschen("A1")

Ergebnis: Nach dem Hinzufügen dieser Tests zeigt mir pytest-cov im Terminal eine Abdeckung von exakt 100 % an.

d) Ist 100 % Coverage ein Qualitätsgarant?
Nein, eine Coverage von 100 % ist kein Garant für fehlerfreie oder qualitativ hochwertige Software.

Was gemessen wird: Die Coverage misst rein quantitativ, ob eine Zeile Code während der Testausführung einmal aufgerufen wurde.

Was NICHT gemessen wird: Sie sagt nichts darüber aus, ob die logischen Prüfungen (assert) im Test sinnvoll oder vollständig sind. Ich könnte 100 % Coverage erreichen, indem ich den Code einfach nur ausführe, ohne die Ergebnisse tatsächlich zu verifizieren. Zudem erkennt die Coverage nicht, ob eine wichtige fachliche Anforderung oder eine essentielle Sicherheitsprüfung im Code komplett vergessen wurde – denn was nicht da ist, kann auch nicht als "ungetestet" markiert werden.

## Aufgabe 4 – Testbericht erstellen 🔴

1. Management-Zusammenfassung
   Projektname: Lagerbestandsverwaltung (Python-Backend)

Datum des Testlaufs: 29.06.2026

Verantwortlicher Prüfer: Fachinformatiker für Anwendungsentwicklung

Gesamtergebnis: ERFOLGREICH BESTANDEN (100 % Erfolgsquote)

Es wurden alle funktionalen Kernkomponenten der drei Softwaremodule (artikel.py, lager.py und bericht.py) systematisch auf Modul- und Integrationsebene geprüft. Alle 14 spezifizierten Testfälle verlaufen ohne Fehler (PASSED). Die geforderte Code-Abdeckung wurde mit 100 % übertroffen. Das System verhält sich auch in den definierten Grenzwert- und Fehlerszenarien stabil und fängt Falscheingaben robuster ab als gefordert.

2. Testumgebung
   Die Tests wurden in einer standardisierten, isolierten Entwicklungsumgebung ausgeführt:

Betriebssystem: Ubuntu 24.04 LTS (Linux x86_64)

Python-Version: Python 3.11.5

Test-Framework: pytest (Version 8.2.1)

Coverage-Werkzeug: pytest-cov (Version 4.1.0)

3. Detaillierte Testergebnisse
   Die folgende Tabelle zeigt den Ausführungsstatus aller dokumentierten und automatisierten Testfälle:

TC-ID,Testfall-Titel,Teststufe,Erwartetes Ergebnis,Status
TC-LAGER-001,Artikel anlegen – Normalfall,Unit-Test,"Artikel wird im Lager registriert, Anzahl erhöht sich.",PASSED
TC-LAGER-002,Artikel anlegen – Duplikat,Unit-Test,ValueError bei identischer Artikel-ID wird geworfen.,PASSED
TC-LAGER-003,Bestand erhöhen – Normalfall,Unit-Test,Artikelbestand wird exakt um die Menge addiert.,PASSED
TC-LAGER-004,Bestand pflegen – Normalfall,Unit-Test,Artikelbestand wird exakt um die Menge subtrahiert.,PASSED
TC-LAGER-005,Bestand reduzieren – Unter Null,Unit-Test,ValueError bei unzureichendem Bestand abgefangen.,PASSED
TC-LAGER-006,Artikel suchen – vorhanden,Unit-Test,Das gesuchte Artikel-Objekt wird zurückgegeben.,PASSED
TC-LAGER-007,Artikel suchen – nicht vorhanden,Unit-Test,Die Suche liefert sicher None zurück (kein Absturz).,PASSED
TC-LAGER-008,Gesamtwert berechnen,Integration,Kaufmännisch korrekte Summe aller (Preis \* Bestand).,PASSED
TC-LAGER-009,Kapazitätsüberschreitung,Unit-Test,ValueError beim Überschreiten der Lagerkapazität.,PASSED
TC-LAGER-010,Artikel unter Mindestbestand,Integration,Liste liefert ausschließlich betroffene Artikel.,PASSED
TC-COV-011,Artikel-Validierung Fehlerwerte,Unit-Test,"ValueError bei leerer ID, negativen Preisen/Beständen.",PASSED
TC-COV-012,Lagerkapazität fehlerhaft,Unit-Test,ValueError bei Initialisierung mit Kapazität <= 0.,PASSED
TC-COV-013,Buchungsmengen <= 0,Unit-Test,ValueError bei Erhöhung/Reduzierung um 0 oder weniger.,PASSED
TC-COV-014,Artikel löschen & Fehlerfall,Unit-Test,Erfolgreiches Löschen; KeyError bei unbekannter ID.,PASSED

4. Gefundene Fehler (Defect Log)Während des gesamten Testzyklus und der initialen Testfall-Implementierung wurden folgende Abweichungen identifiziert und behoben: Bug-ID,Fehlerbeschreibung,Schweregrad,Status,Behebung / Maßnahme
   BG-001,Fehlende Absicherung bei Artikel-Löschung,Mittel,Behoben,Beim Löschen nicht existierender IDs stürzte das System unkontrolliert ab. Es wurde ein expliziter KeyError-Catch eingebaut.
   BG-002,Artikel-Dataclass erlaubte negative Preise,Hoch,Behoben,"In Artikel.**post_init** wurde eine nachträgliche Validierung implementiert, die negative Preise/Bestände per ValueError blockiert."
   BG-003,Buchungsmenge von 0 wurde akzeptiert,Niedrig,Behoben,Sowohl bestand_erhoehen als auch bestand_reduzieren prüfen nun strikt auf Mengen > 0.

5. Coverage-Statistik (Testabdeckung)
   Der finale Coverage-Lauf lieferte eine lückenlose Abdeckung des gesamten Quellcodes (Statement- und Branch-Abdeckung):

Modul / Datei,Abgedeckte Zeilen,Fehlende Zeilen (Missing),Coverage (%)
artikel.py,Alle,Keine,100 %
lager.py,Alle,Keine,100 %
bericht.py,Alle,Keine,100 %
Gesamtprojekt,Alle,Keine,100 %

6. Fachliche Bewertung & Abnahmeempfehlung
   Das System ist aus QA-Sicht vollständig abnahmebereit.

Begründung:

Alle funktionalen Anforderungen der User Stories wurden vollständig und nachweislich fehlerfrei umgesetzt.

Das System verfügt über ein automatisiertes Regressions-Sicherheitsnetz mit einer mathematischen Code-Abdeckung von 100 %.

Kritische Sicherheits- und Logikrisiken (wie negative Bestände, Überbuchungen oder Dateninkonsistenzen beim Löschen) wurden durch exakte Validierungsschranken restlos eliminiert.

7. Offene Punkte & Empfohlene Maßnahmen
   Für zukünftige Entwicklungszyklen (Sprints) werden folgende Erweiterungen empfohlen, die außerhalb des aktuellen Testplans lagen:

Last- und Performance-Tests: Evaluierung der Performance und des Speicherbedarfs im RAM bei extrem großen Artikellisten (> 100.000 Datensätze).

Persistenzprüfung: Erweiterung der Testsuite, sobald eine echte relationale Datenbank (z. B. SQLite/PostgreSQL) anstelle des In-Memory-Dictionaries angebunden wird.

CI/CD-Integration: Einbindung der pytest-Suite in die automatische Pipeline (z. B. GitLab CI) zur Durchsetzung von Quality Gates vor jedem Merge.

## Aufgabe 5 – IHK-Stil 🔴

a) Zur Berechnung der Erfolgsquote betrachten wir die zehn in der Übersicht einzeln aufgeführten Testfälle, die von zehn bis einhundert Prozent reichen. Da acht dieser zehn Tests erfolgreich durchgelaufen sind, ergibt sich ein Anteil von genau achtzig Prozent fehlerfreien Tests an der Gesamtzahl aller ausgeführten Prüfungen.

b) Zum Unterschied zwischen den beiden Fehlschlag-Zuständen lässt sich festhalten, dass der Status FAILED bedeutet, dass der Testcode an sich ordnungsgemäß ausgeführt und die Funktion aufgerufen wurde, aber eine Überprüfung der Logik fehlerhaft war. Das zeigt uns, dass im eigentlichen Programm ein logischer Fehler vorliegt, weil ein erwartetes Ergebnis nicht eintrifft, obwohl das System stabil läuft. Der Status ERROR hingegen bedeutet, dass der Fehler abseits der eigentlichen Überprüfung aufgetreten ist. Das passiert meistens schon bei der Vorbereitung des Tests in einer sogenannten Fixture, durch einen unerwarteten Systemabsturz oder durch einen Laufzeitfehler im Code, noch bevor das eigentliche Testergebnis überhaupt geprüft werden konnte.

c) Zum Testbericht und der Bewertung lässt sich das Gesamtergebnis für den Auftraggeber so zusammenfassen, dass acht der zehn Kernfunktionen fehlerfrei arbeiten, während drei Bereiche Probleme aufweisen. Die Funktionen zum Anlegen von Artikeln, zum Erhöhen des Bestands, zum Suchen vorhandener Ware, zum Prüfen der Kapazität sowie zum Exportieren, Importieren und Löschen arbeiten einwandfrei. Kritisch ist jedoch, dass die Absicherung gegen negative Bestände fehlschlägt, was zu Fehlern im Lager führen kann. Zudem scheitert die Suche nach nicht vorhandenen Artikeln, und die wichtige Erstellung des Berichts stürzt komplett ab, sodass dieser Bereich derzeit überhaupt nicht prüfbar ist. Aus diesem Grund ist das System aktuell nicht abnahmebereit, da eine Erfolgsquote von achtzig Prozent bei kritischen Fehlern nicht für den sicheren Produktivbetrieb ausreicht.

d) Zu den empfohlenen Maßnahmen vor einer erneuten Abnahme müssen gezielte Schritte unternommen werden. Zuerst muss der Absturz beim Erstellen des Berichts behoben werden, um diese Kernfunktion überhaupt erst testbar zu machen. Danach gilt es, die Logikfehler bei der Bestandsreduzierung unter Null und bei der Suche nach unbekannten Artikeln im Quellcode zu reparieren. Sobald diese Korrekturen vorgenommen wurden, muss die gesamte Testsuite erneut gestartet werden, um durch diesen sogenannten Regressionstest sicherzustellen, dass die Fehlerbehebungen keine neuen Probleme in den bereits funktionierenden Programmteilen verursacht haben. Abschließend sollte ein Abdeckungsbericht erstellt werden, um eventuell noch ungetestete Codezeilen aufzuspüren.

## Tandem-Aufgabe 👥

Um den Prozess für unseren Auftraggeber transparent und rechtssicher zu machen, nutzen wir drei verschiedene Dokumente, die zu völlig unterschiedlichen Zeiten entstehen und jeweils eine eigene wichtige Funktion haben:

Der Testplan wird vor dem Testen geschrieben. Er ist das strategische Konzept. Hier legen wir fest, was wir testen (und was nicht), wie wir testen (Werkzeuge wie pytest, Methoden wie Grenzwertanalyse) und wann die Tests stattfinden. Für den Auftraggeber ist er wichtig, weil er vorab sehen kann, ob wir alle seine Anforderungen verstanden haben und die Qualitätskriterien (wie die Mindest-Coverage) mit seinen Erwartungen übereinstimmen.

Das Testprotokoll entsteht während des Testens. Es ist die direkte, ungeschönte Mitschrift der Testausführung. Hier wird für jeden einzelnen Testfall sekundengenau festgehalten: Wer hat ihn ausgeführt, auf welchem System lief er und wie war das exakte Ergebnis (Bestanden oder Fehlgeschlagen mit konkreter Fehlermeldung). Für den Auftraggeber ist das Protokoll der unumstößliche, technische Beweis, dass die Tests wirklich stattgefunden haben und nicht nur erfunden wurden.

Der Testbericht wird nach dem Testen verfasst. Er ist die finale, managementtaugliche Zusammenfassung für den Kunden. Statt seitenlanger technischer Logfiles bekommt der Auftraggeber hier eine klare Erfolgsquote in Prozent, eine Übersicht der behobenen und offenen Fehler sowie eine fundierte Empfehlung, ob die Software abnahmebereit ist oder nicht.

Warum braucht der Auftraggeber alle drei?
Ohne Plan weiß der Kunde nicht, ob wir gründlich genug vorgehen. Ohne Protokoll hat er keinen Beweis für die Durchführung. Ohne Bericht versteht er das technische Kauderwelsch nicht und kann keine kaufmännische Entscheidung für die Bezahlung und den Live-Gang der Software treffen. Alle drei zusammen sichern beide Seiten rechtlich ab.

Unser gegenseitiges Review-Feedback (Protokoll)
Mein Review zu deinem Dokument (Baustein 06 / pytest)
Pflichtbestandteile: Im Testplan waren alle Kernpunkte wie Werkzeuge und Abnahmekriterien super beschrieben. Im Testbericht fehlte mir anfangs die genaue Angabe der Python- und pytest-Versionen in der Testumgebung, das solltest du für die IHK-Prüfung unbedingt noch ergänzen.

Verständlichkeit: Der Bericht ist sehr gut lesbar. Auch ohne deinen Code im Detail zu kennen, verstehe ich sofort, welche Funktionen (wie die Berechnung) geprüft wurden, da die Testfall-Titel sehr sprechend gewählt sind.

Abnahme durch den Auftraggeber: Da deine Erfolgsquote bei einhundert Prozent liegt und alle kritischen Pfade abgedeckt sind, würde der Auftraggeber hier sofort die Freigabe erteilen.

Dein Review zu meinem Dokument (Baustein 07 / TDD)
Pflichtbestandteile: Alle Tabellen und Statistiken sind vollständig vorhanden. Die Erwähnung der durch TDD erreichten einhundert Prozent Coverage im Bericht ist ein dickes Plus.

Verständlichkeit: Durch die klare Trennung von Management-Zusammenfassung und dem detaillierten Defect Log ist der Bericht extrem übersichtlich. Ein Außenstehender sieht sofort, dass Fehler nicht verschwiegen, sondern während des Prozesses direkt repariert wurden.

Abnahme durch den Auftraggeber: Die lückenlose Testabdeckung und die nachweisliche Behebung aller gefundenen Fehler im Protokoll garantieren eine reibungslose Abnahme durch den Kunden.

## Active Recall 🧠

1. Unterschied zwischen Testplan und Testbericht

Testplan: Wird vor dem Testen geschrieben. Er beschreibt die Strategie, den geplanten Ablauf, das Budget, die Werkzeuge und legt fest, was wie und wann getestet wird.

Testbericht: Wird nach dem Testen geschrieben. Er fasst die tatsächlichen Ergebnisse zusammen, listet gefundene Fehler auf und liefert die Entscheidungsgrundlage, ob die Software bereit für den Live-Gang ist.

2. Typische Abnahmekriterien für Software

Eine funktionale Erfolgsquote von 100 % (alle geschriebenen Tests müssen auf "PASSED" stehen).

Keine offenen Fehler mit hohem oder kritischem Schweregrad (keine Systemabstürze).

Eine vertraglich vereinbarte Mindest-Testabdeckung (z. B. eine Code Coverage von mindestens 80 %).

Einhaltung von Performance-Vorgaben (z. B. Ladezeit unter 2 Sekunden) und Barrierefreiheit.

3. Was bedeutet "Testabdeckung" (Coverage) und was misst sie nicht?

Bedeutung: Sie ist eine Metrik, die misst, wie viel Prozent des geschriebenen Quellcodes (Zeilen oder Pfade) während der automatisierten Tests mindestens einmal ausgeführt wurden.

Was sie NICHT misst: Sie misst keine fachliche Qualität. Sie sagt nichts darüber aus, ob die Überprüfungen (assert) im Test logisch sinnvoll sind oder ob wichtige Anforderungen im Code komplett vergessen wurden.

4. Wann ist ein Testbericht "gut genug" für einen Kunden?

Wenn er transparent und ehrlich ist (auch bekannte, unkritische Fehler auflistet).

Wenn er verständlich für Nicht-Techniker formuliert ist (durch eine klare Management-Zusammenfassung).

Wenn er vollständig ist, also neben den reinen Ergebnissen auch die Testumgebung, die Rahmenbedingungen und eine klare Empfehlung für oder gegen die Abnahme enthält.

5. Unterschied zwischen FAILED und ERROR in pytest

FAILED: Der Testaufbau war fehlerfrei, aber eine gezielte Überprüfung (assert) im Test schlug fehl. Es liegt ein logischer oder fachlicher Fehler im Programm vor.

ERROR: Der Code stürzte ab, noch bevor das assert überhaupt erreicht wurde. Das passiert meistens durch Fehler beim Laden von Testdaten (in einer Fixture), Syntaxfehler oder unvorhergesehene Abstürze des Systems während der Testvorbereitung.
