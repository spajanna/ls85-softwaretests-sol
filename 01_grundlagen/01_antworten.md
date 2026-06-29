### Aufgabe 4
## (a) Zwei Risiken ohne Tests

- **Falsche Lagerbestände:** Waren werden als verfügbar angezeigt, obwohl sie nicht mehr da sind.
- **Produktionsausfall / Geschäftsproblem:** Fehler im Produktivsystem können Bestellungen, Lieferungen oder Buchungen blockieren.

## (b) Defekt vs. Versagen

Ein **Defekt** ist der Fehler im Code oder in der Logik.  
Ein **Versagen** ist die sichtbare Auswirkung beim Benutzer.

**Beispiel:**  
Im Code wird beim Wareneingang die Menge falsch berechnet. Das ist der **Defekt**.  
Wenn der Mitarbeiter danach sieht, dass statt 100 Stück nur 10 Stück im Lager angezeigt werden, ist das das **Versagen**.

## (c) Warum frühzeitiges Testen wirtschaftlich sinnvoll ist

Frühzeitiges Testen spart Kosten, weil Fehler früher gefunden und schneller behoben werden können.

Nach der **Rule of Ten** wird ein Fehler ungefähr **zehnmal teurer**, je später er entdeckt wird.  
Ein Fehler in der Planung oder Entwicklung ist also viel billiger zu beheben als ein Fehler im Produktivsystem, der Kunden betrifft und eventuell Daten korrigiert werden müssen.

------------

### Aufgabe 5
## a) Argumentation für systematisches Testen

Auch wenn bisher scheinbar alles gut gegangen ist, bedeutet das nicht, dass keine Fehler im System vorhanden sind.  
Ein Grundprinzip des Testens sagt: **Testen zeigt die Anwesenheit von Fehlern, aber nicht deren Abwesenheit**.  
Außerdem ist **vollständiges Testen nicht möglich**, deshalb müssen wir systematisch die wichtigsten und riskantesten Fälle testen.  
Wenn wir früh testen, sparen wir Zeit und Geld, weil Fehler in der Entwicklung viel billiger zu beheben sind als später im Produktivsystem.  
Ein bekanntes Beispiel ist **Ariane 5**: Durch einen Softwarefehler stürzte die Rakete kurz nach dem Start ab, was enorme Kosten verursachte.  
Auch bei uns könnte ein kleiner Fehler, zum Beispiel in der Urlaubsberechnung oder Lohnabrechnung, später große Auswirkungen auf Mitarbeitende und das Unternehmen haben.  
Deshalb sollten wir Tests nicht als Zeitverlust sehen, sondern als Absicherung gegen teure Fehler und Ausfälle.


## b) Error, Defect und Failure bei `berechne_urlaubstage(eintrittsdatum, arbeitstage_pro_woche)`

### Error

Ein Entwickler denkt fälschlicherweise, dass jeder Mitarbeiter immer **5 Arbeitstage pro Woche** hat.

### Defect

Im Code wird deshalb fest mit 5 Arbeitstagen gerechnet, obwohl der Parameter `arbeitstage_pro_woche` übergeben wird.

**Beispiel:**

`urlaubstage = 30`

statt:

`urlaubstage = 30 / 5 * arbeitstage_pro_woche`

### Failure

Ein Mitarbeiter mit **4 Arbeitstagen pro Woche** bekommt im System fälschlicherweise **30 Urlaubstage** statt anteilig **24 Urlaubstage** angezeigt.

### Konsequenzen im Lohnabrechnungssystem

Ein unentdeckter Defekt kann dazu führen, dass Mitarbeitende zu viele oder zu wenige Urlaubstage erhalten.  
Dadurch können falsche Lohnabrechnungen, Streitigkeiten mit Mitarbeitenden und zusätzlicher Korrekturaufwand entstehen.  
Im schlimmsten Fall entstehen rechtliche oder finanzielle Probleme für den Betrieb.


## c) Bewertung von Grundprinzip 7

Ja, Grundprinzip 7 ist hier relevant.  
Nur weil die Funktion keine technischen Fehler zeigt, heißt das nicht automatisch, dass sie fachlich korrekt oder nützlich ist.  
Wenn die Funktion zum Beispiel fehlerfrei läuft, aber Teilzeitkräfte falsch berechnet, ist das System trotzdem schlecht.  
Ein gutes System muss also nicht nur ohne Absturz funktionieren, sondern auch die fachlichen Anforderungen korrekt erfüllen.