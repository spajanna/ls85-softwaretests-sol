## Aufgabe 0 – Grundbegriffe: pytest-Ausgabe lesen 🟢

**a**) Testanzahl und Erfolg: Es wurden insgesamt 5 Tests gesammelt und ausgeführt. Davon waren 3 Tests erfolgreich (PASSED).

**b**) FAILED bedeutet, dass der Test bis zum Ende lief, aber eine Behauptung (assert) nicht zutraf. Die Logik liefert also ein falsches Ergebnis. ERROR bedeutet, dass der Test gar nicht erst ordnungsgemäß bis zur Prüfung kam, weil bereits bei der Testvorbereitung (z. B. in einem fehlerhaften Fixture) oder durch einen fatalen Laufzeitfehler (z. B. ein NameError oder TypeError) abgebrochen wurde.

**c**) Der Test test_dividieren schlägt fehl. Ein möglicher Grund könnte ein Rundungsfehler bei Fließkommazahlen sein oder dass die mathematische Berechnung im Code schlicht fehlerhaft implementiert wurde.

**d**) Die Tests befinden sich in der Datei test_rechner.py. Das erkennt man an dem Präfix vor dem doppelten Doppelpunkt (::), welches den Dateipfad aufzeigt.

**e**) Ausführungsbefehl: Der Befehl lautet pytest test_rechner.py -v (oder allgemein pytest -v). Das Flag -v steht für verbose und bewirkt, dass jeder Testfall einzeln mit seinem Namen und dem genauen Status aufgelistet wird, anstatt nur als kurzer Punkt.

## Aufgabe 1 – Von unittest zu pytest migrieren 🟡

**a**) Bei pytest fällt die gesamte Klassenstruktur weg (class ... (unittest.TestCase)), und es müssen keine speziellen Assert-Methoden wie self.assertEqual gelernt werden. Man nutzt das ganz normale Python-Schlüsselwort assert. Es vereinfacht sich der Boilerplate-Code enorm. Es fehlt nichts, da pytest im Hintergrund alle erweiterten Prüfungen und detaillierten Fehlermeldungen selbstständig übernimmt.

**b**) PASSED zeigt an, dass die Assert-Bedingung wahr war. FAILED bedeutet, dass das Assert fehlgeschlagen ist. ERROR verweist auf einen Absturz außerhalb einer Assert-Prüfung.

## Aufgabe 2 – Fixtures 🟡

**a**)

import pytest

class BenutzerkontoService:
def **init**(self):
self.datenbank = {}

    def benutzer_anlegen(self, username, passwort):
        self.datenbank[username] = passwort
        return True

# ============================================================

# Aufgabe 2a) – Das pytest Fixture

# ============================================================

# ============================================================

# Aufgabe 2b) – Das pytest Fixture

# ============================================================

@pytest.fixture
def kontoservice():
"""
Fixture, das einen fertig eingerichteten BenutzerkontoService
bereitstellt und einen Standard-Testuser registriert.
"""
service = BenutzerkontoService()
service.benutzer_anlegen("testuser", "Test1234!")
return service

def test_benutzer_existiert_nach_setup(kontoservice):
"""Prüft, ob der Standarduser aus dem Fixture vorhanden ist."""
assert "testuser" in kontoservice.datenbank

def test_neuer_benutzer_laesst_sich_anlegen(kontoservice):
"""Prüft, ob der Service weitere Benutzer aufnehmen kann."""
erfolg = kontoservice.benutzer_anlegen("neuerehe", "Geheim123!")
assert erfolg is True
assert "neuerehe" in kontoservice.datenbank

**c**) Um den Gültigkeitsbereich des Fixtures zu erweitern, fügt man dem Dekorator das Argument scope="module" hinzu, sodass die Definition @pytest.fixture(scope="module") lautet. Durch diese Änderung wird die Funktion kontoservice() nicht mehr vor jeder einzelnen Testmethode isoliert aufgerufen, sondern exakt ein einziges Mal für die gesamte Testdatei ausgeführt, woraufhin sich alle darin enthaltenen Tests dieselbe Instanz des Services teilen.

Ein solcher Modul-Scope ist im Testalltag immer dann sinnvoll, wenn der Setup-Prozess im Fixture extrem zeitaufwändig oder ressourcenintensiv ist, wie es beispielsweise beim Aufbau einer echten Datenbankverbindung, dem Starten eines lokalen Webservers oder dem Einlesen riesiger Konfigurationsdateien der Fall ist. Da pytest das Objekt für die gesamte Testsuite dieses Moduls im Speicher zwischenspeichert, lässt sich die Gesamtlaufzeit der Tests drastisch verkürzen.

Allerdings muss man dabei penibel darauf achten, dass die Tests den Zustand des geteilten Objekts nicht manipulieren oder verändern, da Modifikationen durch einen Test unweigerlich Seiteneffekte auf nachfolgende Tests haben und so das Prinzip der Testisolation verletzen würden.

## Aufgabe 3 – Parametrisierung 🟡

**a**)
@pytest.mark.parametrize("punkte, erwartete_note", [

# Note 1: Grenze oben, Vertreter, Grenze unten

(100, 1), (95, 1), (92, 1),

# Note 2: Grenze oben, Vertreter, Grenze unten

(91, 2), (85, 2), (81, 2),

# Note 3: Grenze oben, Vertreter, Grenze unten

(80, 3), (75, 3), (67, 3),

# Note 4: Grenze oben, Vertreter, Grenze unten

(66, 4), (60, 4), (50, 4),

# Note 5: Grenze oben, Vertreter, Grenze unten

(49, 5), (40, 5), (30, 5),

# Note 6: Grenze oben, Vertreter, Grenze unten

(29, 6), (15, 6), (0, 6)
])
def test_berechne_note_grenzen_und_vertreter(punkte, erwartete_note):
assert berechne_note(punkte) == erwartete_note

**b**)
@pytest.mark.parametrize("menge, erwartet_gueltig", [ # Gültige Äquivalenzklasse & Grenzwerte
(1, True), # Minimale Grenze
(2, True), # Knapp über Minimum
(500, True), # Vertreter Mitte
(998, True), # Knapp unter Maximum
(999, True), # Maximale Grenze

    # Ungültige Äquivalenzklasse: Zu klein
    (0, False),     # Grenzwert verboten
    (-1, False),    # Negativer Vertreter

    # Ungültige Äquivalenzklasse: Zu groß
    (1000, False),  # Grenzwert zu hoch
    (1500, False),  # Klar drüber

    # Ungültige Äquivalenzklasse: Falscher Datentyp
    (5.5, False),   # Float statt Int
    ("100", False), # String statt Int
    (True, False)   # Boolean (wird oft fälschlich als 1 gewertet)

])
def test_validiere_menge_alle_klassen(menge, erwartet_gueltig):
assert validiere_menge(menge) == erwartet_gueltig

**c**)
Wenn ich diese beiden parametrisierten Testfunktionen in meiner Testdatei ausführe, generiert das Framework aus den übergebenen Datentabellen insgesamt 30 eigenständige Testläufe. Für die Notenberechnung habe ich exakt 18 Einzeltests definiert, um alle kritischen Kanten und Vertreter abzudecken, während die Mengenvalidierung auf 12 separate Testdurchläufe kommt.

In meiner Terminal-Ausgabe wird jede Zeile mit den konkreten Eingabeparametern in eckigen Klammern aufgelistet und einzeln mit dem Status PASSED quittiert. Da es sich hier um reine In-Memory-Logik ohne Datenbank- oder Netzwerkzugriffe handelt, benötigt die gesamte Ausführung aller 30 Testfälle auf meinem System nur einen winzigen Bruchteil einer Sekunde – die reine Ausführungszeit liegt bei etwa 0,02 bis 0,05 Sekunden.

## Aufgabe 4 – pytest.raises 🟡

**a**)
def test_abheben_negativer_betrag_fehlermeldung():
"""Prüft, ob beim Abheben eines Minusbetrags die korrekte Meldung kommt."""
konto = Kontorechner()
with pytest.raises(ValueError, match="positiv sein"):
konto.abheben(-20.0)

def test_abheben_ueberziehung_fehlermeldung():
"""Prüft die Fehlermeldung, wenn das Konto nicht genug Guthaben aufweist."""
konto = Kontorechner()
konto.einzahlen(50.0)
with pytest.raises(ValueError, match="Unzureichendes Guthaben"):
konto.abheben(100.0)

def test_note_punkte_zu_hoch_fehlermeldung():
"""Prüft die Fehlermeldung bei der Notenberechnung mit über 100 Punkten."""
with pytest.raises(ValueError, match="zwischen 0 und 100 liegen"):
berechne_note(101)

**b**)
Der funktionale Unterschied zwischen den beiden Frameworks liegt vor allem in der Syntax und der Lesbarkeit des Codes. Während unittest.assertRaises mich dazu zwingt, entweder eine unübersichtlichere Callback-Struktur zu nutzen oder die Assertion eng an die Objektinstanz der Testklasse zu binden, fügt sich pytest.raises als nativer Python-Context-Manager mit dem with-Statement nahtlos in den Code ein. Zudem bietet pytest über das match-Argument eine extrem elegante Möglichkeit, Fehlermeldungen direkt per Teilstring oder regulärem Ausdruck zu überprüfen, was bei unittest deutlich sperriger über assertRaisesRegex gelöst werden muss.

Ich bevorzuge ganz klar die Variante von pytest. Sie ist deutlich kompakter, verringert den Boilerplate-Code auf ein Minimum und liest sich wie natürlicher Python-Code, was die Wartung und das Schreiben von Tests im Entwicklungsalltag massiv erleichtert.

## Tandem-Aufgabe 👥

1. Zentrale Verwaltung und Wiederverwendbarkeit (DRY-Prinzip)
   Wenn wir ein Objekt in zehn verschiedenen Tests brauchen, müssten wir ohne Fixture in jedem einzelnen Test denselben Setup-Code schreiben. Ändert sich später die Funktionsweise oder der Konstruktor der Klasse, müssten wir alle zehn Tests anfassen. Mit dem Fixture ändern wir den Code genau an einer zentralen Stelle.

2. Intelligentes Scope-Management
   Ein normales Objekt im Test lebt nur so lange, wie der Test läuft. Pytest-Fixtures bieten uns aber die Kontrolle über den Lebenszyklus (Scope). Wir können festlegen, ob das Objekt für jeden Test neu erzeugt wird (scope="function"), oder ob es für das ganze Modul (scope="module") oder sogar die gesamte Test-Session (scope="session") bestehen bleibt. Das spart enorm viel Zeit bei schweren Operationen wie Datenbankverbindungen.

3. Saubere Trennung von Vorbereitung und Logik
   Der Testcode bleibt extrem fokussiert. Er verlangt das Fixture einfach als Argument und kann sofort mit den eigentlichen Behauptungen (assert) loslegen.
