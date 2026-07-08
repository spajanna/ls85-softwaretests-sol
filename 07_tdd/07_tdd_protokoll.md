## Aufgabe 0 – Grundbegriffe: TDD-Zyklus einordnen 🟢

a) Richtige Reihenfolge:
Die korrekte Abfolge im TDD-Zyklus lautet C → B → D → E → A.

C: Test für eine neue Funktion schreiben

B: Test ausführen → er schlägt fehl (🔴 Red)

D: Minimalen Code schreiben, bis der Test grün wird (🟢 Green)

E: Alle Tests erneut ausführen → sie bleiben grün

A: Code refactorn: Namen verbessern, Dopplungen beseitigen

b) Für mich bedeutet diese Regel ganz einfach: Ich darf im gesamten Entwicklungsprozess keinen produktiven Programmcode schreiben, es sei denn, ich habe vorher einen Unit-Test geschrieben, der genau diesen Code verlangt und der ohne ihn fehlschlägt. Ich schreibe also niemals Logik "auf Vorrat", sondern lasse mich bei jedem Schritt strikt von meinen Tests leiten.

c) Warum ich im Green-Schritt bewusst „hässlichen“ Code schreibe:
Im "Green"-Schritt fokussiere ich mich ausschließlich auf Geschwindigkeit. Mein einziges Ziel in dieser Phase ist es, das System so schnell wie möglich wieder in einen funktionierenden, sicheren Zustand (grün) zu bringen. Schöne Designentscheidungen, saubere Architektur oder Performance-Optimierungen ignoriere ich hier absichtlich, um mich nicht ablenken zu lassen.

Was ich im nächsten Schritt damit mache: Dieser unschöne Code bleibt natürlich nicht so. Im direkt darauffolgenden "Refactor"-Schritt (Schritt A) nehme ich mir die Zeit, diesen Code systematisch aufzuräumen, zu säubern und zu professionalisieren. Meine zuvor geschriebenen Tests dienen mir dabei als Sicherheitsnetz, damit ich beim Umbauen nichts unbemerkt kaputtmache.

d) Was ich unter einem „Baby Step“ verstehe:
Ein „Baby Step“ bedeutet für mich, dass ich eine komplexe Entwicklungsaufgabe in die kleinstmöglichen, logischen Teilschritte und minimalen Testfälle zerlege. Anstatt zu versuchen, eine große Funktion sofort komplett fehlerfrei zu bauen, taste ich mich Schritt für Schritt an das Ziel heran – zum Beispiel, indem ich erst die Fehlerbehandlung teste und baue, und danach den ersten Standardfall.

Warum diese Vorgehensweise für mich sinnvoll ist: Diese Arbeitsweise nimmt mir beim Programmieren enorm viel mentalen Stress. Wenn mein Test fehlschlägt, weiß ich sofort, dass der Fehler nur in den letzten zwei oder drei Zeilen liegen kann, die ich gerade eben hinzugefügt habe. Außerdem sorgt es dafür, dass meine Codebasis zu jedem Zeitpunkt voll funktionsfähig und testbar bleibt.

## Aufgabe 1 – TDD-Zyklus verstehen 🟡

Zyklus 1: Die erste Anforderung (Wert 3)

1. 🔴 Red (Fehlschlag)
   Ich habe den ersten Test test_runden_3_ergibt_5 geschrieben. Da die Funktion runden_auf_naechste_fuenf im Produktivcode noch überhaupt nicht existierte, brach der Testlauf sofort mit einem NameError ab.

Zustand der Tests: 🔴 ROT (1 Error)

2. 🟢 Green (Erfolg)
   Ich habe die Funktion angelegt. Nach der TDD-Logik habe ich den absolut minimalsten Code geschrieben, um den Test grün zu machen – ich gebe also einfach hart codiert die Zahl 5 zurück:

def runden_auf_naechste_fuenf(zahl):
return 5

3. 🔵 Refactor (Bereinigung)
   Da der Code nur aus einer einzigen Zeile besteht, gibt es hier noch keine Dopplungen oder unschönen Strukturen aufzuräumen.

Zyklus 2: Die zweite Anforderung (Wert 7)

1. 🔴 Red (Fehlschlag)
   Ich habe den zweiten Test test_runden_7_ergibt_10 hinzugefügt. Da meine Funktion bisher immer stur 5 zurückgibt, schlägt der neue Test fehl, weil 5 != 10.

Zustand der Tests: 🔴 ROT (1 Passed, 1 Failed)

2. 🟢 Green (Erfolg)
   Ich passe den Code so an, dass beide Tests gerade eben so bestehen. Ich nutze eine einfache if-Abfrage für die bisherigen Fälle:

def runden_auf_naechste_fuenf(zahl):
if zahl <= 3:
return 5
return 10

    Zustand der Tests: 🟢 GRÜN (2 Passed)

3. 🔵 Refactor (Bereinigung)
   Ich merke langsam, dass hart codierte Rückgaben bei mehr Mustern unübersichtlich werden. Da ich aber erst zwei Fälle habe, warte ich noch einen Zyklus, um das mathematische Muster sicher zu bestätigen.

Zyklus 3: Der Grenzwert (Wert 10)

1. 🔴 Red (Fehlschlag)
   Ich füge den Test test_runden_10_ergibt_10 hinzu. Mein Code würde aktuell für die Zahl 10 in den else-Zweig laufen und 10 zurückgeben. Halt – dieser Test wird überraschenderweise sofort grün, da meine aktuelle "hässliche" Logik zufällig schon 10 liefert!

TDD-Korrektur: Um den TDD-Zyklus sauber zu halten und echten Code zu erzwingen, schreibe ich stattdessen sofort den nächsten Fall mit auf: test_runden_11_ergibt_15. Meine aktuelle Funktion liefert hier 10 statt 15.

Zustand der Tests: 🔴 ROT (3 Passed, 1 Failed)

2. 🟢 Green (Erfolg)
   Ich ziehe jetzt die mathematische Logik hinzu, um alle bisherigen harten Bedingungen zu ersetzen, anstatt noch mehr if-Bedienungen zu stapeln. Ich nutze die Ganzzahldivision und den Modulo-Operator:

import math

def runden_auf_naechste_fuenf(zahl): # Mathematischer Ansatz zum Aufrunden auf das nächste Vielfache von 5
return math.ceil(zahl / 5) \* 5

Zustand der Tests: 🟢 GRÜN (4 Passed)

3. 🔵 Refactor (Bereinigung)
   Die mathematische Formel math.ceil(zahl / 5) \* 5 ist extrem sauber, extrem kompakt und deckt alle bisherigen Anforderungen elegant ab. Es gibt aktuell nichts weiter zu optimieren.

Zyklus 4: Die Null (Wert 0)

1. 🔴 Red / Green Check
   Ich schreibe den Test test_runden_0_ergibt_0. Ich führe die Testsuite aus. Da math.ceil(0 / 5) \* 5 mathematisch exakt 0 ergibt, fängt mein Sicherheitsnetz den Test sofort ab und er ist direkt grün.

Zustand der Tests: 🟢 GRÜN (5 Passed)

Zyklus 5: Die negativen Zahlen (Wert -3)

1. 🔴 Red (Fehlschlag)
   Ich möchte sicherstellen, dass die Funktion auch mit Minuswerten umgehen kann (z.B. -3 aufgerundet zur nächsten 5, was 0 sein sollte). Ich schreibe test_runden_minus_3_ergibt_0.

Zustand der Tests: Ich führe aus – und der Test ist direkt 🟢 GRÜN (6 Passed), da math.ceil(-3 / 5) gleich 0 ist und 0 \* 5 = 0 ergibt.

Fazit meines TDD-Durchlaufs:
Durch das schrittweise Vorgehen habe ich mich von einer simplen, hart codierten Rückgabe zu einer allgemeingültigen mathematischen Formel herangearbeitet. Die Tests haben mir bei jedem Umbau (Refactoring) die Sicherheit gegeben, dass alte Funktionalitäten nicht beschädigt wurden. Meine Funktion ist nun vollständig und robust implementiert!

## Aufgabe 3 – Refactoring unter Tests 🔴

a) Bevor ich am Code irgendetwas verändert habe, habe ich die Testsuite mit pytest laufen lassen. Alle fünf bestehenden Tests in der Klasse TestVerarbeiteBestellung (test_normale_bestellung, test_bestellung_mit_rabatt, test_leere_bestellung_wirft_fehler, test_negativer_preis_wirft_fehler, test_ungültiger_rabatt_wirft_fehler) waren zu 100 % grün. Das gab mir das notwendige Sicherheitsnetz für den Umbau.

b) Ich habe die ehemals lange, tief verschachtelte Funktion in drei kleine, fokussierte Einheiten zerlegt, die jeweils genau eine Aufgabe übernehmen (Single Responsibility Principle):

Extraktion der Basis-Validierung (\_validiere_basis_bestellung): Die Prüfungen, ob die Bestellung existiert, der Schlüssel "artikel" vorhanden ist und die Liste nicht leer ist, habe ich in eine eigene Hilfsfunktion ausgelagert. Das bereinigt den Einstiegspunkt der Hauptfunktion.

Extraktion der Artikel-Validierung und -Berechnung (\_validiere_and_berechne_artikel): Die komplette for-Schleife, die jeden einzelnen Artikel auf Preise, Mengen und Negativwerte prüft, wurde ausgelagert. Sie wirft bei Fehlern sofort die passenden Exceptions und gibt im Erfolgsfall den Zwischenpreis (Preis × Menge) zurück.

Einsatz von List-Comprehensions und sum(): In der Hauptfunktion verarbeite_bestellung konnte ich die manuelle Schleife und den aufaddierenden Counter durch ein sauberes, pythonisches sum(...) ersetzen.

Namensanpassung: Die Variablenbezeichnungen wurden beibehalten oder geschärft (z. B. art als Abkürzung in der Comprehension), um den Code sofort lesbar zu machen, ohne dass man verschachtelte if-Bedingungen analysieren muss.

c)

d) Diese Tests haben geholfen, Regressionen zu verhindern
Während des Umbaus haben mir vor allem zwei Testfälle massiv dabei geholfen, keine Fehler (Regressionen) einzubauen:

test_negativer_preis_wirft_fehler: Beim Extrahieren der Artikelprüfung in \_validiere_and_berechne_artikel musste ich sicherstellen, dass die Exceptions immer noch exakt so geworfen werden wie vorher. Als ich bei einem internen Probelauf versehentlich den match-String für den Fehler veränderte, schlug dieser Test sofort Alarm.

test_bestellung_mit_rabatt und test_normale_bestellung: Diese beiden Tests gaben mir die absolute Sicherheit, dass meine mathematische Umstellung von der klassischen for-Schleife hin zu der moderneren sum()-Funktion fehlerfrei war und die kaufmännischen Endpreise nach wie vor centgenau gerundet und berechnet werden.

## Aufgabe 4 – IHK-Stil 🔴

a) In meiner TDD-Entwicklung durchlaufe ich strikt die folgenden drei Phasen:

🔴 Red (Fehlschlag-Phase): Ich schreibe als Erstes einen neuen, kleinen Unit-Test für eine Funktionalität, die es im Code noch gar nicht gibt. Wenn ich die Testsuite ausführe, muss dieser Test fehlschlagen (oder einen Kompilier-/NameError werfen). Das beweist mir, dass der Test sinnvoll ist und die neue Logik wirklich noch fehlt.

🟢 Green (Erfolgs-Phase): Ich schreibe den absolut minimalen produktiven Code, der nötig ist, um diesen neuen Test (und alle bisherigen) erfolgreich zu bestehen. In dieser Phase achte ich bewusst noch nicht auf perfekten Stil oder Architektur, sondern nur darauf, dass die Testanzeige so schnell wie möglich wieder grün wird.

🔵 Refactor (Bereinigungs-Phase): Sobald die Tests grün sind, räume ich den neu geschriebenen Code auf. Ich entferne Dopplungen (DRY-Prinzip), verbessere Variablennamen und optimiere die Struktur. Die Tests dienen mir dabei als Sicherheitsnetz – sie müssen nach jedem kleinen Umbauschritt sofort wieder ausgeführt werden und grün bleiben.

b) Diese Tests habe ich in meiner Testdatei definiert, um die verschiedenen Äquivalenzklassen und mathematischen Grenzwerte abzusichern:

Python
import pytest

class TestBerechneZinsen:
def test_basis_zinsberechnung(self):
"""Standardfall (Gültige Äquivalenzklasse): 1000 € zu 5 % für 1 Jahr."""
assert berechne_zinsen(1000.0, 5.0, 1) == 1050.0

    def test_zinseszins_mehrere_jahre(self):
        """Zinseszins (Gültige Äquivalenzklasse): Komplexere Berechnung über 3 Jahre."""
        # 1000 * (1.02)^3 = 1061.208 -> kaufmännisch gerundet 1061.21
        assert berechne_zinsen(1000.0, 2.0, 3) == 1061.21

    def test_null_jahre_liefert_ausgangskapital(self):
        """Grenzwert (Gültige Äquivalenzklasse): Wenn die Jahre 0 sind, passiert nichts."""
        assert berechne_zinsen(500.0, 4.5, 0) == 500.0

    def test_negative_werte_werfen_value_error(self):
        """Fehlerfall (Ungültige Äquivalenzklasse): Negatives Kapital darf nicht erlaubt sein."""
        with pytest.raises(ValueError, match="nicht negativ sein"):
            berechne_zinsen(-100.0, 3.0, 2)

c) Basierend auf meinen zuvor geschriebenen Tests habe ich die Funktion wie folgt in Python umgesetzt:

Python
def berechne_zinsen(kapital: float, zinssatz: float, jahre: int) -> float:
"""
Berechnet die Zinsen inklusive Zinseszins.
Formel: Kapital \* (1 + Zinssatz / 100) ^ Jahre
"""
if kapital < 0 or zinssatz < 0 or jahre < 0:
raise ValueError("Eingabewerte dürfen nicht negativ sein.")

    ergebnis = kapital * (1 + zinssatz / 100) ** jahre
    return round(ergebnis, 2)

d) Wenn ich TDD im Arbeitsalltag einsetze, sehe ich darin folgende Kernaspekte:

Zwei Vorteile:

Höhere Codequalität und weniger Bugs (Regressionen): Da ich für jede Zeile Code bereits ein automatisiertes Sicherheitsnetz habe, fallen Fehler sofort beim Schreiben auf. Das Verhindern von unbemerkten Folgefehlern spart bei späteren Code-Änderungen enorm viel Zeit.

Besseres Softwaredesign: Weil ich den Code aus der Sicht des "Nutzers" (des Tests) schreibe, bevor die Logik existiert, werden Schnittstellen automatisch modularer, schlanker und besser durchdacht.

Ein Nachteil:

Hoher initialer Zeitaufwand und Gewöhnungsphase: Das Schreiben von Tests vor dem eigentlichen Code fühlt sich anfangs langsamer an und erfordert extrem viel Disziplin. Besonders bei hohem Termindruck in Projekten ist die Versuchung groß, den TDD-Zyklus zu verlassen, obwohl sich die investierte Zeit hintenraus durch weniger Debugging-Aufwand meist wieder amortisiert.

## Tandem-Aufgabe 👥

Die „Goldene TDD-Regel“ besagt ganz einfach: Ich schreibe keine einzige Zeile produktiven Code, es sei denn, es gibt einen zuvor geschriebenen Unit-Test, der genau diesen Code verlangt und der ohne ihn fehlschlägt. In der Praxis – und genau das haben wir ja gerade beim Ping-Pong-Spielen gemerkt – ist es verdammt schwer, diese Regel konsequent einzuhalten. Das hat vor allem folgende Gründe:

Der "Ich-weiß-doch-schon-wie-es-geht"-Reflex: Als Entwickler hat man die Lösung oft sofort im Kopf. Beim dividieren will man automatisch sofort das if divisor == 0: raise ValueError hinschreiben, weil man weiß, dass man nicht durch Null teilen darf. Aber laut TDD darf man das erst tun, wenn die andere Person einen Test schreibt, der genau diesen Fehler provoziert. Man muss sich also extrem bremsen.

Die Ungeduld im Green-Schritt: Wenn man an der Reihe ist, den Code "grün" zu machen, neigt man dazu, die Funktion direkt komplett und "schön" zu Ende zu schreiben, anstatt wirklich nur den minimalen Schritt zu machen.

Meine Erfahrung aus unserer Übung:
Es hat am Anfang echt Überwindung gekostet, beim ersten Test für addieren einfach nur stumpf return 5 in die Funktion zu schreiben. Man fühlt sich fast ein bisschen albern dabei. Aber man merkt im Verlauf des Ping-Pongs schnell, wie sicher das Vorgehen ist. Weil wir uns gegenseitig kontrolliert haben, ist kein Code reingekommen, der nicht durch einen Test abgesichert war.

## Active Recall 🧠

1. Was ist die "Goldene TDD-Regel"?
   Für mich bedeutet diese Regel das eiserne Gesetz im TDD: Ich darf im gesamten Entwicklungsprozess keinen produktiven Programmcode schreiben, es sei denn, es existiert bereits ein zuvor geschriebener Unit-Test, der genau diesen Code verlangt und der ohne ihn fehlschlägt. Ich baue also niemals Features oder Logik "auf Vorrat", sondern lasse mich bei jeder Zeile Code strikt von einem fehlschlagenden Test leiten.

2. Was bedeutet "Baby Steps" im TDD-Kontext?
   Unter „Baby Steps“ verstehe ich das Vorgehen, eine komplexe Aufgabe in die kleinstmöglichen, logischen Teilschritte und minimalsten Testfälle zu zerlegen. Anstatt zu versuchen, eine Funktion sofort in ihrer vollen Pracht und mit allen Sonderfällen zu schreiben, taste ich mich Schritt für Schritt heran (z. B. erst die Fehlerbehandlung, dann der einfachste Erfolgsfall). Das senkt meine mentale Belastung und hält den Code zu jedem Zeitpunkt lauffähig.

3. Warum darf man beim Green-Step "hässlichen" Code schreiben?
   Im "Green"-Schritt habe ich nur ein einziges, scharf fokussiertes Ziel: Ich will das System so schnell wie möglich wieder in einen funktionierenden, sicheren Zustand (grün) bringen. Designentscheidungen, perfekte Architektur oder Performance-Optimierungen blende ich hier absichtlich aus, um mich nicht zu verzetteln. Hässlicher Code ist hier völlig okay, weil ich genau weiß, dass ich ihn im nächsten Schritt sofort aufräumen werde.

4. Was ist das Ziel der Refactor-Phase?
   Das Ziel dieser Phase ist es, den im "Green"-Schritt entstandenen, eventuell unschönen Code zu professionalisieren, ohne dabei seine Funktionalität zu verändern. Ich entferne Dopplungen (DRY-Prinzip), verbessere Variablennamen und optimiere die Struktur. Das Geniale dabei ist: Die zuvor geschriebenen Tests dienen mir als absolutes Sicherheitsnetz – sie müssen nach jedem kleinen Handgriff sofort wieder ausgeführt werden und grün bleiben.

5. Wie hilft TDD dabei, über den Code nachzudenken, bevor man ihn schreibt?
   TDD zwingt mich dazu, die Perspektive zu wechseln. Bevor ich mich in die Implementierungsdetails stürze, muss ich mir als "Nutzer" meiner eigenen Funktion Gedanken machen: Wie soll die Schnittstelle aussehen? Welche Parameter übergebe ich? Was erwarte ich als Rückgabewert und wie verhält sich die Funktion im Fehlerfall? Dadurch plane ich den Code automatisch modularer, schlanker und logischer, noch bevor die erste Zeile der eigentlichen Logik existiert.
