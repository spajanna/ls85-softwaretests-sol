Zustand nach TDD:

- Zyklus 1: neuer Test zuerst rot, danach grün
- Zyklus 2: neuer Test zuerst rot, danach grün
- Zyklus 3: neuer Test zuerst rot, danach grün
- Zyklus 4: neuer Test zuerst rot, danach grün
- Zyklus 5: negativer Fall ergänzt, danach allgemeine Lösung refactored

----------------

Vor dem Refactoring wurden alle vorhandenen Tests ausgeführt.

Erwartetes Ergebnis: Alle Tests sind grün.

## Änderungen

1. Die Prüfung der Bestellung wurde in `validiere_bestellung()` ausgelagert.
2. Die Prüfung einzelner Artikel wurde in `validiere_artikel()` ausgelagert.
3. Die Berechnung des Gesamtpreises wurde in `berechne_gesamtpreis()` ausgelagert.
4. Die Rabattprüfung wurde in `validiere_rabatt()` ausgelagert.
5. Die Hauptfunktion `verarbeite_bestellung()` ist jetzt kürzer und besser lesbar.

## Tests nach jedem Schritt

Nach jeder kleinen Änderung wurden die Tests erneut ausgeführt.

Erwartetes Ergebnis: Alle Tests bleiben grün.