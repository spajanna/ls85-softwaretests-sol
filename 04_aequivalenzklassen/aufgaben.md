# Baustein 04 – Äquivalenzklassen & Grenzwertanalyse 🟡

> **Schwierigkeit:** 🟡 Anwendung  
> **Zeitrahmen:** ca. 120 Minuten  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/Pages/ResponsePage.aspx?id=AVtDSgxpSk2SjJ-w6Dswu9p-7diy21FJmEKm_woHizhURTVaWUNOQjA1WERLUDRMTVdVTElEUkMwTS4u" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 04: Äquivalenzklassen</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [*] 🟢 Ich weiß, was Äquivalenzklassen sind
- [ ] 🟡 Ich habe den Begriff schon gehört
- [ ] 🔴 Das ist mir komplett neu

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … erklären, was eine Äquivalenzklasse ist
- 🟢 … gültige und ungültige Äquivalenzklassen eines Eingabebereichs ermitteln
- 🟡 … Grenzwerte identifizieren und daraus Testfälle ableiten
- 🟡 … eine vollständige Äquivalenzklassentabelle erstellen
- 🔴 … begründen, warum diese Methoden die Anzahl notwendiger Testfälle sinnvoll reduzieren

---

## Hintergrund

Vollständiges Testen ist unmöglich (Prinzip 2 aus Baustein 01).
Äquivalenzklassen helfen, die unendlich vielen Eingabemöglichkeiten auf
eine handhabbare Anzahl sinnvoller Vertreter zu reduzieren.

**Grundidee:** Alle Eingaben innerhalb einer Klasse verhalten sich gleich –
es reicht, einen repräsentativen Wert je Klasse zu testen.

**Grenzwertanalyse** ergänzt dies: Fehler entstehen besonders häufig an den Grenzen
(z. B. bei `>= 18` werden oft 17, 18 und 19 verwechselt).

---

## Aufgabe 0 – Grundbegriffe: Äquivalenzklassen erkennen 🟢

**Einstieg ohne Code:**

**a)** Eine Ampel-Steuerung akzeptiert nur Ganzzahlen von 1 bis 5 als Prioritätsstufe.
Benenne ohne viel Nachdenken: Was sind gültige, was ungültige Eingaben?

**b)** Erkläre in einem Satz, was eine Äquivalenzklasse ist –
so als würdest du es einem Mitschüler ohne IT-Kenntnis erklären.

**c)** Nenne je ein Beispiel aus dem Berufsalltag für:
- Eine gültige Äquivalenzklasse
- Eine ungültige Äquivalenzklasse
- Einen Grenzwert, der besonders kritisch sein könnte

**d)** Warum reicht es aus, nur **einen** repräsentativen Wert pro Klasse zu testen?
Erkläre die Grundannahme dahinter.

Trage deine Antworten in `04_antworten.md` ein.

---

## Aufgabe 1 – Äquivalenzklassen für ein Bestellformular 🟡

Eine E-Commerce-Anwendung hat folgende Validierungsregeln für das Bestellfeld "Menge":
- Typ: ganzzahlig
- Minimum: 1
- Maximum: 999
- Sonderfall: 0 ist explizit verboten ("Mindestbestellmenge")

**a)** Ermittle alle Äquivalenzklassen und trage sie in die Tabelle ein:

| AK-Nr | Klasse | Repräsentativer Wert | Gültig / Ungültig |
|-------|--------|---------------------|-------------------|
| AK1 | | | |
| AK2 | | | |
| AK3 | | | |
| AK4 | | | |

**b)** Ergänze die Tabelle um Grenzwerttestfälle:

| GW-Nr | Grenzwert | Erwartetes Ergebnis |
|-------|-----------|---------------------|
| GW1 | 0 | Ungültig |
| GW2 | 1 | Gültig |
| GW3 | | |
| GW4 | | |
| GW5 | | |

**c)** Implementiere in `code/starter.py` die Funktion `validiere_menge()` und schreibe manuelle Tests für alle Äquivalenzklassen und Grenzwerte.

---

## Aufgabe 2 – Äquivalenzklassen für Passwortstärke 🟡

Eine Anwendung prüft Passwörter nach folgenden Regeln:
- Länge: 8–64 Zeichen
- Muss mindestens einen Großbuchstaben enthalten
- Muss mindestens eine Ziffer enthalten
- Darf keine Leerzeichen enthalten

**a)** Erstelle die Äquivalenzklassentabelle für alle vier Regeln kombiniert.
Hinweis: Jede Regel erzeugt eigene gültige/ungültige Klassen!

**b)** Wähle repräsentative Testwerte aus und begründe deine Wahl.

**c)** Implementiere `pruefe_passwort()` in `starter.py` und teste alle Klassen.

---

## Aufgabe 3 – Grenzwertanalyse: Altersverifikation 🟡

Eine Plattform hat drei Kategorien:
- Unter 12: Kinder-Modus (eingeschränkt)
- 12–17: Jugend-Modus (teils eingeschränkt)
- Ab 18: Vollzugang

**a)** Bestimme alle Grenzwerte und erstelle eine Grenzwerttabelle mit:
- Unterer Grenzwert der Klasse
- Wert genau an der Grenze
- Oberer Grenzwert der Klasse

**b)** Welche Fälle würden erfahrene Tester zusätzlich einbeziehen?
(Denke an ungültige Werte wie negative Zahlen, 0, 150, Kommazahlen)

---

## Aufgabe 4 – IHK-Stil 🔴

**Prüfungsszenario:**

Eine Prüfungssoftware berechnet das Prüfungsergebnis:

- Eingabe: Punktzahl (ganzzahlig, 0–100)
- Ausgabe: Note (1–6) nach folgendem Schema:
  - 92–100: Note 1
  - 81–91:  Note 2
  - 67–80:  Note 3
  - 50–66:  Note 4
  - 30–49:  Note 5
  - 0–29:   Note 6

**(a)** Ermitteln Sie alle Äquivalenzklassen (gültige und ungültige). *(4 Punkte)*

**(b)** Erstellen Sie eine vollständige Grenzwerttabelle für alle Notengrenzen. *(6 Punkte)*

**(c)** Welche Eingabewerte würden Sie als Tester wählen, um mit möglichst wenigen Testfällen alle Klassen und Grenzwerte abzudecken? Begründen Sie Ihre Wahl. *(4 Punkte)*

Implementiere die Funktion `berechne_note()` und teste alle Fälle aus (a)–(c) in `starter.py`.

---

## Tandem-Aufgabe 👥

**Spiegeltest – Gegenseitiges Überprüfen:**

Jede Person wählt eine Funktion aus dem Berufsalltag (Beispiele: Telefonnummernvalidierung, PLZ-Prüfung, Datumseingabe, Kreditkartennummer).

Erstellt unabhängig voneinander Äquivalenzklassen und Grenzwerttabellen.
Dann vergleicht: Was hat die andere Person gefunden, was du übersehen hast?

Diskutiert: Würden eure Testfälle denselben Fehler finden?

**Erkläre deinem Tandempartner:** Erkläre das Prinzip der Äquivalenzklassenbildung so, als würdest du es einem Nicht-IT-Kollegen erklären müssen – ohne Fachbegriffe, nur mit einem Alltagsbeispiel. Dein Tandempartner gibt Feedback: War es verständlich?

---

## Active Recall 🧠

*Unterlagen zu:*

1. Was ist der Kerngedanke hinter Äquivalenzklassen?
Man teilt mögliche Eingaben in Gruppen ein und testet pro Gruppe einen typischen Wert.
2. Warum testet man immer auch ungültige Klassen?
Weil das Programm auch falsche Eingaben sicher erkennen und ablehnen muss.  
3. An welchen Stellen entstehen besonders häufig Programmfehler? (Stichwort: Grenzwerte)
Fehler entstehen oft an Grenzen, z. B. genau bei Mindestwert, Maximalwert oder direkt daneben.
4. Wie viele Testfälle braucht man mindestens für vollständige Äquivalenzklassenabdeckung?
Mindestens einen Testfall pro Äquivalenzklasse.

---

## Reflexion 🚦

- [*] 🟢 Ich kann eigenständig Äquivalenzklassen und Grenzwerte ermitteln
- [ ] 🟡 Das Konzept ist klar, aber ich brauche noch Übung
- [ ] 🔴 Ich brauche weitere Erklärungen oder Beispiele

**Was nimmst du mit?**

> Ich nehme mit, dass man Eingaben in gültige und ungültige Gruppen einteilt und pro Gruppe typische Werte testet. Besonders wichtig sind Grenzwerte, weil Fehler oft genau an Mindest- oder Maximalwerten entstehen.

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
