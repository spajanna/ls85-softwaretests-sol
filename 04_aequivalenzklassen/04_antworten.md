**a)**
Ganze Zahlen von 1 bis 5 (also 1, 2, 3, 4, 5).
Ganze Zahlen kleiner als 1 (z. B. 0, -1), ganze Zahlen größer als 5 (z. B. 6, 100), Dezimalzahlen (2.5) sowie keine Zahlen/Texte ("A").

**b)**
Eine Äquivalenzklasse ist einfach eine Gruppe von Eingaben, die vom Programm alle komplett gleich behandelt werden – so wie bei einer Sortiermaschine für Postleitzahlen alle Briefe für dieselbe Stadt in dieselbe Kiste fliegen. Wenn einer ankommt, kommen die anderen aus der Kiste auch an.

**c)** Nenne je ein Beispiel aus dem Berufsalltag für:

- Eine gültige Äquivalenzklasse
  Rabattcode-Feld akzeptiert genau 8-stellige Textcodes.
- Eine ungültige Äquivalenzklasse
  Eingabe eines Geburtsdatums, das in der Zukunft liegt.
- Einen Grenzwert, der besonders kritisch sein könnte
  Das maximale Upload-Limit für eine Datei (z. B. exakt 20,00 MB).

**d)**
Die Grundannahme lautet: Homogenität. Wenn das Programm für einen Wert aus der Klasse korrekt funktioniert (oder den erwarteten Fehler wirft), verhält es sich für alle anderen Werte aus exakt derselben Klasse genauso. Alles andere wäre pure Zeitverschwendung beim Testen.

## Aufgabe 1 – Äquivalenzklassen für ein Bestellformular 🟡

**a)** Ermittle alle Äquivalenzklassen und trage sie in die Tabelle ein:

AK-Nr,Klasse,Repräsentativer Wert,Gültig / Ungültig
AK1,Ganzzahlen von 1 bis 999,42,Gültig
AK2,Ganzzahlen kleiner als 1 (inkl. 0),-5 (oder 0),Ungültig
AK3,Ganzzahlen größer als 999,1005,Ungültig
AK4,"Keine Ganzzahlen (Strings, Floats)","4.5 (oder ""zehn"")",Ungültig

**b)** Ergänze die Tabelle um Grenzwerttestfälle:

GW-Nr,Grenzwert,Erwartetes Ergebnis
GW1,0,Ungültig
GW2,1,Gültig
GW3,2,Gültig (Grenznähe)
GW4,998,Gültig (Grenznähe)
GW5,999,Gültig
GW6,1000,Ungültig

## Aufgabe 2 – Äquivalenzklassen für Passwortstärke

**a**) ID,Bedingung / Aspekt,Definition der Klasse,Testwert,Status
AK1,Länge (zu kurz),< 8 Zeichen,Ab1,Ungültig
AK2,Länge (korrekt),8–64 Zeichen,Sicheres1,Gültig
AK3,Länge (zu lang),> 64 Zeichen,A1...[65 Zeichen],Ungültig
AK4,Großbuchstabe,Kein Großbuchstabe vorhanden,passwort1,Ungültig
AK5,Ziffer,Keine Ziffer vorhanden,Passwort,Ungültig
AK6,Leerzeichen,Enthält Leerzeichen,Pass wort1,Ungültig

**b**) Die ungültigen Werte isolieren jeweils exakt einen Fehler, damit man beim Fehlschlagen des Tests sofort weiß, welche Validierungsregel kaputt ist.

## Aufgabe 3 – Grenzwertanalyse: Altersverifikation

**a**) Klasse,Unterer Grenzwert / Davor,Exakt auf der Grenze,Oberer Grenzwert / Danach
Kinder (< 12),11 (Kinder-Modus),12 (Wechsel zu Jugend),13 (Jugend-Modus)
Jugend (12–17),17 (Jugend-Modus),18 (Wechsel zu Voll),19 (Vollzugang)

**b**)
0 und -1 (Überprüfung der Untergrenze von Lebensalter).

120 oder 150 (Überprüfung auf plausible Obergrenzen für Menschen).

17.5 (Dezimalzahlen, falls das System fälschlicherweise Floats erlaubt).

"achtzehn" (Datentyp-Fehler/SQL-Injection-Versuche).

## Aufgabe 4 – IHK-Stil

**a**) Für die gültigen Bereiche gelten folgende Klassen: Die Klasse AK_G1 umfasst alle Werte von 92 bis 100 Punkten für die Note 1. Die Klasse AK_G2 deckt den Bereich von 81 bis 91 Punkten für die Note 2 ab. Für die Note 3 gilt die Klasse AK_G3 mit Werten von 67 bis 80 Punkten. Die Klasse AK_G4 beinhaltet 50 bis 66 Punkte für die Note 4. Werte von 30 bis 49 Punkten fallen in die Klasse AK_G5 für die Note 5, und die Klasse AK_G6 deckt alle Werte von 0 bis 29 Punkten für die Note 6 ab.

Für die ungültigen Bereiche gibt es drei weitere Klassen: Die Klasse AK_U1 fängt alle Werte kleiner als 0 auf, da dies zu wenige Punkte sind. Die Klasse AK_U2 ist für Werte größer als 100 zuständig, da diese die maximale Punktzahl überschreiten. Die Klasse AK_U3 deckt schließlich alle Eingaben ab, die keine Ganzzahlen sind, wie beispielsweise Kommazahlen oder Textstrings.

**b**)
Grenze,Testwert,Erwartete Note / Ergebnis
Außenbereich Unten,-1,Ungültig
Grenze 0,0,Note 6
Grenze 29/30,29 / 30,Note 6 / Note 5
Grenze 49/50,49 / 50,Note 5 / Note 4
Grenze 66/67,66 / 67,Note 4 / Note 3
Grenze 80/81,80 / 81,Note 3 / Note 2
Grenze 91/92,91 / 92,Note 2 / Note 1
Grenze 100,100,Note 1
Außenbereich Oben,101,Ungültig

**c**)
Um die Anzahl der Testfälle zu minimieren, nutzt man die Grenzwert-Testfälle gleichzeitig als Repräsentanten für die Äquivalenzklassen.

Auswahl: -1, 0, 29, 30, 49, 50, 66, 67, 80, 81, 91, 92, 100, 101.

Begründung: Jeder dieser Werte prüft punktgenau, ob der "Umschaltpunkt" in den if/else-Bedingungen des Codes korrekt gesetzt wurde (z.B. < statt <=). Da sie auf den Kanten liegen, decken sie automatisch jede gültige und ungültige Punkteklasse ab.

**d**)
Der Kerngedanke der Äquivalenzklassenbildung besteht darin, alle denkbaren Eingabewerte in Gruppen aufzuteilen, die vom Programm auf exakt dieselbe Weise verarbeitet werden, sodass ein einziger Testwert pro Gruppe für die Überprüfung völlig ausreicht.

Man testet dabei bewusst auch ungültige Klassen, um die Robustheit der Software sicherzustellen und zu garantieren, dass das System bei Falscheingaben nicht einfach abstürzt, sondern kontrollierte Fehlermeldungen ausgibt.

Typische Fehlerquellen liegen vor allem an den Kanten und Grenzen wie kleiner, größer, kleiner-gleich oder größer-gleich, da sich Entwickler dort besonders leicht um einen Zähler vertun, was man auch als Off-by-one-Error bezeichnet.

Die mathematische Mindestanzahl an Testfällen für eine reine Äquivalenzklassenabdeckung ergibt sich schließlich ganz einfach aus der Summe der Anzahl der gültigen Klassen und der Anzahl der ungültigen Klassen.
