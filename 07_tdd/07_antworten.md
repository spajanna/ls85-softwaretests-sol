## Aufgabe 0
### a) Richtige TDD-Reihenfolge

C → B → D → E → A

1. Test für eine neue Funktion schreiben
2. Test ausführen → er schlägt fehl (Red)
3. Minimalen Code schreiben, bis der Test grün wird (Green)
4. Alle Tests erneut ausführen → sie bleiben grün
5. Code refactorn

### b) Goldene TDD-Regel

Man schreibt zuerst einen fehlschlagenden Test, bevor man neuen Produktivcode schreibt.

### c) Warum minimaler Code im Green-Schritt?

Im Green-Schritt geht es nur darum, den Test schnell zum Laufen zu bringen. Der Code darf erstmal einfach oder unschön sein. Im Refactoring-Schritt wird er danach verbessert, ohne das Verhalten zu ändern.

### d) Baby Step

Ein Baby Step ist ein sehr kleiner Entwicklungsschritt: ein kleiner Test, wenig Code, sofort wieder testen. Das ist sinnvoll, weil Fehler schneller gefunden werden und man ständig Feedback bekommt.

## Aufgabe 4
### d)
Vorteile:

- Fehler werden früh gefunden.
- Man hat automatisch Regressionstests für spätere Änderungen.

Nachteil:

- Am Anfang wirkt TDD langsamer, weil man erst Tests schreiben muss.

## Aufgabe Tandem
Wir haben insgesamt **5 Tests** geschrieben.  
Der Code ist gut strukturiert, weil jede Rechenart eine eigene Methode hat und der Fehlerfall bei Division durch 0 klar behandelt wird.

### Erklärung für den Tandempartner
Die Goldene TDD-Regel bedeutet: Man schreibt erst einen Test, der fehlschlägt, und danach nur so viel Code, bis dieser Test grün wird. In der Praxis ist das schwer, weil man oft direkt die komplette Lösung schreiben möchte. In der Übung merkt man aber, dass kleine Schritte helfen: Man sieht sofort, welcher Test rot oder grün ist, und findet Fehler schneller.