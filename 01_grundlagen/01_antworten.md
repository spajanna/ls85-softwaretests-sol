
**01_grundlagen**

| Maßnahme | Statisch | Dynamisch |
|----------|----------|-----------|
| Code Review durch einen Kollegen | x        |           |
| Programm mit Testdaten ausführen |          | x         |
| Syntaxprüfung durch den Editor | x        |           |
| Walkthroughs im Team |          | x         |
| Unit-Tests laufen lassen |          | x         |
| Checklisten für Codestruktur | x        |           |

---

**02_testarten**

**Warum reichen statische Tests allein nicht aus?**
Die Bedingungen und Module ändern können. Wird das Modul in einer anderen Umgebung eingesetzt, gibt es ggf. andere Faktoren als im Ursprungsmodul/umgebung.
---
**03_testmethoden**

Vollständiges Testen ist nicht möglich..
- Entwickler haben eine andere Sicht auf die Dinge. Kunden hingegen ihre eigene. Das erschwert das grundlegende Testen ungemein, da Kunden aufgrund ihrer eigenen herangehensweisen und Unwissenheit Fehler zum Teil selbst definieren.

Fehler häufen sich (Defect Clustering)
- 80% der Fehler stecken in 20% des Codes. Oft sind es folgefehler der Grund einer Anhäufung.

Welches Prinzip überrascht mich am meisten?
- Beware of the Pesticide Paradox bisher einfach noch nicht gehört..
---
**04_aequivalenzklassen**

**(a)** Nennen Sie zwei konkrete Risiken, die durch das Weglassen von Tests entstehen. *(2 Punkte)*
- Fehler werden zu spät und vom Kunden selbst erkannt. Finanzieller Schaden.
- Fehler durch Code-Review sind nicht direkt erkennbar.

**(b)** Unterscheiden Sie die Begriffe „Defekt" und „Versagen" anhand eines Beispiels aus dem Lagerverwaltungssystem. *(4 Punkte)*
- Defekt ist eine fehlerhafte Stelle im Code. Z.B. falsche SQL-Abfrage oder Datenbank fehlerhaft angesprochen.
- Versagen ist das Aufreten des Fehlers zur Laufzeit. Z.B. falsche Daten oder Erreichbarkeit der DB nicht gegeben.

**(c)** Erläutern Sie, warum frühzeitiges Testen (Grundprinzip 3) wirtschaftlich sinnvoll ist. Nutzen Sie das Schlagwort „Rule of Ten". *(4 Punkte)*
- Wirtschaftlich sinnvoll ist das frühzeitige Testen aufgrund der "Rule of Ten", die besagt, dass im Vorfeld gefundene Fehler 10 Mal günstiger sind zu beheben als später in einer Produktivumgebung.

