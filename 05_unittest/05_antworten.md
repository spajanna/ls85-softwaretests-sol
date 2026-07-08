## Aufgabe 0 – Grundbegriffe: Unit-Test lesen und verstehen 🟢

**a)** Was testet jeder dieser Tests? Beschreibe in je einem Satz.
Der erste Test stellt sicher, dass ein gesetzter Rabatt in Prozent den Gesamtpreis der hinzugefügten Artikel mathematisch korrekt mindert. Der zweite Test überprüft, ob ein neu erstelltes, leeres Bestellsystem standardmäßig einen Gesamtpreis von exakt Null zurückgibt. Der dritte Test stellt sicher, dass das System die Eingabe eines unzulässigen, negativen Rabattwerts blockiert und dies mit einem ValueError quittiert.

**b)** Welche Klasse und welche Methoden werden in den Tests verwendet?
In den Tests wird die Testklasse TestBestellsystem verwendet, welche von unittest.TestCase erbt. Seitens der Anwendungslogik werden die Klasse Bestellsystem sowie deren Methoden artikel_hinzufuegen, rabatt_setzen und gesamtpreis aufgerufen.

**c)** Was bedeutet `assertAlmostEqual` und warum wird es hier statt `assertEqual` verwendet?
In den Tests wird die Testklasse TestBestellsystem verwendet, welche von unittest.TestCase erbt. Seitens der Anwendungslogik werden die Klasse Bestellsystem sowie deren Methoden artikel_hinzufuegen, rabatt_setzen und gesamtpreis aufgerufen.

**d)** Was passiert, wenn `test_negativer_rabatt_wirft_fehler` fehlschlägt?
Was wäre dann das Problem in der Implementierung?
Wenn dieser Test fehlschlägt, bedeutet das, dass bei der Übergabe eines negativen Werts kein ValueError ausgelöst wurde. Das Problem in der Implementierung wäre demnach eine fehlende oder fehlerhafte Validierungslogik in der Methode rabatt_setzen, wodurch unzulässige Werte unbemerkt verarbeitet würden.

## Aufgabe 1 – Erste Unit-Tests schreibe

**a)** Die Analyse der Klasse Kontorechner zeigt, dass sie über ein Property für den Kontostand sowie die beiden Methoden einzahlen und abheben verfügt. Das Property erlaubt das Auslesen des aktuellen Guthabens, während die Einzahlungsfunktion den Kontostand um positive Beträge erhöht und bei Werten kleiner oder gleich Null eine Ausnahme auslöst. Die Abhebungsfunktion verringert das Guthaben, sichert das System jedoch gleichzeitig gegen negative Beträge sowie gegen eine unzulässige Kontoüberziehung ab.

**b**) Nach der Ausführung der Tests lassen sich die Symbole in der Konsole eindeutig interpretieren. Ein einfacher Punkt steht für einen erfolgreich bestandenen Test, bei dem alle Erwartungen erfüllt wurden. Das große F symbolisiert ein Failure und zeigt an, dass das Programm zwar ohne Absturz lief, aber ein falsches Ergebnis geliefert hat, sodass eine Überprüfung fehlschlug. Das große E steht für einen Error und signalisiert, dass der Testlauf durch einen unerwarteten Laufzeitfehler im Code selbst vorzeitig abgebrochen wurde.

## Aufgabe 2 – setUp und tearDown 🟡

Beim Testen der Einkaufsliste ruft das Framework vor jeder einzelnen Testmethode zuerst die setUp-Methode auf, um ein frisches Testobjekt der Einkaufsliste bereitzustellen. Danach wird der eigentliche Testcode ausgeführt, und unmittelbar im Anschluss gibt die tearDown-Methode die definierte Abschlussmeldung im Terminal aus. Der Einsatz von setUp ist dabei wesentlich effizienter als das manuelle Instanziieren in jedem einzelnen Test, da er doppelten Code vermeidet und eine strikte Testisolation garantiert. Kein Test kann so die Daten eines nachfolgenden Tests beeinflussen, da jede Methode mit einer komplett unberührten Instanz startet.

## Aufgabe 3 – assertRaises richtig nutzen 🟡

Die korrekte Anwendung von assertRaises lässt sich auf zwei Wegen realisieren. Bei der ersten Variante wird die Methode als klassischer Funktionsaufruf genutzt, dem die Ausnahme, die Funktion als Callable und danach die Argumente separat übergeben werden, wie es bei self.assertRaises(ValueError, berechne_note, 101) der Fall ist. Die zweite Variante nutzt assertRaises als Context Manager über ein with-Statement, unter dem der fehlerhafte Code direkt aufgerufen wird, wie bei with self.assertRaises(ValueError): berechne_note(-1).

## Aufgabe 4 – IHK-Stil 🔴

Für die Mehrwertsteuerfunktion lassen sich vier sinnvolle Testszenarien definieren. Der erste Fall nutzt ein Standard-Netto von 100.0 und einen Steuersatz von 19.0, was eine Steuer von 19.0 ergibt. Der zweite Fall prüft den reduzierten Satz mit 200.0 Netto und 7.0 Prozent Steuer, woraus 14.0 resultieren. Der dritte Fall simuliert eine steuerfreie Lieferung mit 50.0 Netto und 0.0 Prozent Steuer, was zu 0.0 führt. Der vierte Fall provoziert durch einen negativen Nettobetrag von minus 10.0 bei 19.0 Prozent Steuer bewusst einen ValueError. Beim Testen von Kommazahlen ist die Methode assertEqual hochgradig problematisch, da Computer Brüche im Binärsystem darstellen und dabei minimale Rundungsfehler entstehen. Als Alternative muss zwingend assertAlmostEqual genutzt werden, da diese Methode die Werte innerhalb einer engen Toleranzgrenze vergleicht und fälschliche Testabbrüche durch winzige Abweichungen in den hinteren Nachkommastellen verhindert.

## Active Recall 🧠

Die gesuchte Basisklasse, von der alle eigenen Testklassen im Framework zwingend erben müssen, heißt unittest.TestCase. Um alle im aktuellen Verzeichnis befindlichen Tests automatisch aufzuspüren und in einem Rutsch auszuführen, nutzt man auf der Kommandozeile den Befehl python -m unittest discover.

Der funktionale Unterschied zwischen den beiden Überprüfungsmethoden liegt darin, dass assertEqual eine strikte, bitgenaue Identität der beiden Werte verlangt, während assertAlmostEqual speziell für Fließkommazahlen gedacht ist und minimale, technisch bedingte Rundungsfehler bis zu einer bestimmten Nachkommastelle toleriert.

Bezüglich des Testablaufs wird die Vorbereitungsmethode setUp nicht etwa nur ein einziges Mal für die gesamte Klasse, sondern strikt einmal vor jeder einzelnen Testmethode aufgerufen, um eine saubere Testisolation zu garantieren.

In der Testergebnis-Ausgabe steht das Zeichen F für ein Failure, was bedeutet, dass der Code zwar fehlerfrei durchgelaufen ist, aber eine eingebaute Überprüfung ein falsches Ergebnis geliefert hat, während ein E für einen Error steht und signalisiert, dass der Testlauf durch einen unvorhergesehenen Absturz oder eine unerwartete Ausnahme im Programmcode vorzeitig abgebrochen wurde.
