## Aufgabe 0
### a)
Black-Box-Test: Man testet von außen, ohne den Code zu kennen.  
Frage: Funktioniert das System so, wie es soll?
White-Box-Test: Man testet mit Blick in den Code.  
Frage: Wurden alle wichtigen Code-Stellen und Zweige geprüft?

### b)
| Situation | Methode |
|-----------|---------|
| Ein Kunde testet, ob er sich einloggen kann | Black-Box |
| Ein Entwickler prüft, ob alle if-Zweige durchlaufen werden | White-Box |
| Ein Tester gibt verschiedene Passwörter ein und schaut, was passiert | Black-Box |
| Ein Entwickler misst die Testabdeckung (Coverage) | White-Box |
| Ein externes Testteam prüft das System gegen die Spezifikation | Black-Box |

### c)
Beide Methoden zusammen sind sinnvoll, weil man so sowohl das Verhalten von außen als auch die interne Code-Logik prüft.

**Aufgabe 1**
| TC-Nr | Eingabe (User/PW) | Erwartete Ausgabe | Kategorie |
|---|---|---|---|
| TC01 | admin / geheim123 | True | Gültiger Login |
| TC02 | admin / falsch123 | False | Falsches Passwort |
| TC03 | unbekannt / geheim123 | False | Unbekannter Benutzer |
| TC04 | ad / geheim123 | False | Benutzername zu kurz |
| TC05 | sehrlangerbenutzername123 / geheim123 | False | Benutzername zu lang |
| TC06 | admin! / geheim123 | False | Sonderzeichen im Benutzernamen |


## Aufgabe 2
### a)
1 Start
  | v 2 betrag <= 0? 
  |-- ja --> 3 return "UNGUELTIG" --> 14 Ende 
  | 
  |-- nein 
      v 
4 ist_neukunde? 
  |-- ja --> 5 prioritaet = "HOCH" 
  |          | 
  |          v 
  |-- nein --> 6 prioritaet = "NORMAL" 
             | 
             v
7 gutscheincode == "VIP2024"?
  |-- ja --> 8 prioritaet = "HOCH" 
  |          |
  |          v 
  |-- nein --+
             v 
9 betrag >= 500? 
  |-- nein --> 13 return prioritaet --> 14 Ende 
  | 
  |-- ja 
       v 
10 prioritaet == "HOCH"? 
  |-- ja --> 11 return "EXPRESS" --> 14 Ende 
  | 
  |-- nein --> 12 return "PRIORITAET" --> 14 Ende

### b)
mindestens 4 Testfälle.

### c)
mindestens 4 Testfälle.
