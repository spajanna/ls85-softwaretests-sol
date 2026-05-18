
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

---
**05_unit_tests**

**a)** Formuliere eine überzeugende Argumentation (5–8 Sätze) für systematisches Testen.
Nutze mindestens drei der sieben Grundprinzipien und ein reales Beispiel
(Ariane-5, Therac-25, Y2K oder ein eigenes Beispiel aus dem Berufsalltag).
- Testen generell zeigt die Anwesenheit von Fehlern. Vollständiges Testen ist zwar nicht möglich, aber Testen, besonders frühzeitiges Testen erspart dem Unternehmen nicht nur Kosten, sondern auch eine schlechte Reputation.
Die Einführung von Softwaretests für unser Produkt sichert uns eine gleichbleibende Qualität und ebnet uns den Weg in Richtung Zertifizierungen. Dies würde unseren Kundenstamm maßgeblich erweitern.


**b)** Dein Betrieb entwickelt eine neue Funktion `berechne_urlaubstage(eintrittsdatum, arbeitstage_pro_woche)`.
- Identifiziere einen möglichen Fehler (Error), Defekt (Defect) und ein Versagen (Failure) für diese Funktion.
  - Fehler: arbeitstage_pro_woche könnten auch negativ sein
  - Defekt: fehlende Prüfung, ob arbeitstage_pro_woche auch negativ, wenn ja, ABBRUCH
  - Failure: ungültiges Ergebnis der Berechnung
- Beschreibe die Konsequenzen eines unentdeckten Defekts in einem Lohnabrechnungssystem.
    - rechtliche Konsequenzen wegen Verstoß gegen das Arbeitnehmerschutzgesetz -> Strafzahlungen für das Unternehmen

**c)** Bewerte: Ist Grundprinzip 7 ("Keine Fehler = Gutes System") für diesen Fall relevant? Begründe.
Prinzip 7 ist immer relevant, da nie komplett alle Fehler gefunden werden können.

## Tandem-Aufgabe 👥

**Erkläre deinem Tandempartner:**

> "Stell dir vor, du bist frisch im Betrieb und musst einem Azubi aus einem anderen Beruf erklären, was der Unterschied zwischen einem Bug und einem Fehler ist. Du hast nur 2 Minuten und ein konkretes Beispiel aus dem Alltag."

- Partner A erklärt (2 Minuten)
  - Fehler ist der falsche Grundgedanke und Bug ist die Stelle im Code, der diesen Gedanken umgesetzt hat.
- Partner B hört zu und stellt eine Rückfrage
  - Woher kommt der Name Bug?
- Partner B erklärt zurück mit anderen Worten
  - Der Begriff Bug kommt von Motten, die früher in die Elektronik geflogen sind und Kurzschlüsse verursachten. 
- Zusammen: Welche Formulierung war klarer? Warum?
  - Bug als Fehlerhafte Stelle im Code


## Reflexion 🚦

*Nach dem Bearbeiten: Wie schätzt du dich jetzt ein?*

- [x] 🟢 Ich verstehe alle Konzepte und kann sie erklären
- [ ] 🟡 Ich verstehe die meisten Konzepte, habe aber noch Fragen
- [ ] 🔴 Ich brauche noch mehr Zeit oder Unterstützung





