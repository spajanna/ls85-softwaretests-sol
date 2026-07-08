# Baustein 07 – Test-Driven Development (TDD) 🔴

> **Schwierigkeit:** 🔴 Transfer  
> **Zeitrahmen:** ca. 150 Minuten  
> **Voraussetzung:** Baustein 05 und 06 abgeschlossen  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/DA4KdSKMba" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 07: TDD</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich habe bereits nach TDD entwickelt
- [ ] 🟡 Ich habe von TDD gehört und verstehe das Konzept
- [ ] 🔴 TDD ist mir unbekannt

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … den Red-Green-Refactor-Zyklus erklären und visuell darstellen
- 🟡 … einen fehlschlagenden Test schreiben, bevor der Code existiert
- 🟡 … minimalen Code schreiben, der genau diesen Test grün macht
- 🔴 … Refactoring durchführen ohne bestehende Tests zu brechen
- 🔴 … Vor- und Nachteile von TDD für echte Berufsszenarien bewerten

---

## Hintergrund: Der TDD-Zyklus

```
         🔴 RED
      Test schreiben
    (schlägt fehl – ok!)
          │
          ▼
       🟢 GREEN
  Minimalen Code schreiben
  (nur so viel, dass Test grünt)
          │
          ▼
      🔵 REFACTOR
   Code verbessern ohne
   Funktionalität zu ändern
          │
          └──────► zurück zu RED
```

**Goldene TDD-Regel:** Kein Produktionscode ohne vorher einen fehlschlagenden Test!

**Baby Steps:** Immer nur einen Test auf einmal. Kein "ich implementiere schon mal alles durch".

---

## Aufgabe 0 – Grundbegriffe: TDD-Zyklus einordnen 🟢

**Einstieg: Den Zyklus verstehen**

**a)** Bringe die folgenden Schritte in die richtige TDD-Reihenfolge:

| Schritt | Aktion                                                      |
| ------- | ----------------------------------------------------------- |
| A       | Code refactorn: Namen verbessern, Dopplungen beseitigen     |
| B       | Test ausführen → er schlägt fehl (🔴 Red)                   |
| C       | Test für eine neue Funktion schreiben                       |
| D       | Minimalen Code schreiben, bis der Test grün wird (🟢 Green) |
| E       | Alle Tests erneut ausführen → sie bleiben grün              |

Richtige Reihenfolge: \_\_\_

**b)** Was bedeutet die „Goldene TDD-Regel"? Formuliere sie mit eigenen Worten.

**c)** Warum schreibt man beim Green-Schritt bewusst „hässlichen" (minimalen) Code?
Was passiert damit im nächsten Schritt?

**d)** Was ist ein „Baby Step" im TDD-Kontext?
Warum ist diese Vorgehensweise sinnvoll?

Trage deine Antworten in `07_tdd_protokoll.md` ein.

---

## Aufgabe 1 – TDD-Zyklus verstehen 🟡

**Szenario:** Du sollst eine Funktion `runden_auf_naechste_fuenf(zahl)` entwickeln,
die eine Zahl auf das nächste Vielfache von 5 aufrundet.

Beispiele:

- `runden_auf_naechste_fuenf(3)` → `5`
- `runden_auf_naechste_fuenf(7)` → `10`
- `runden_auf_naechste_fuenf(10)` → `10`
- `runden_auf_naechste_fuenf(0)` → `0`

**Gehe exakt nach dem TDD-Zyklus vor – Schritt für Schritt:**

**Zyklus 1:**

1. 🔴 Schreibe `test_runden_3_ergibt_5` – führe aus – er **muss** rot sein (Funktion existiert nicht)
2. 🟢 Implementiere genau so viel Code, dass dieser Test grünt
3. 🔵 Gibt es schon etwas zu verbessern? (wahrscheinlich noch nicht)

**Zyklus 2:**

1. 🔴 Schreibe `test_runden_7_ergibt_10`
2. 🟢 Passe Code an (minimal!)
3. 🔵 Refactoring?

**Zyklus 3–5:** Wiederhole für 10, 0, und negative Zahlen.

**Dokumentiere in `07_tdd_protokoll.md`:** Was war nach jedem Schritt der Zustand der Tests?

---

## Aufgabe 2 – TDD Praxisprojekt: Passwort-Generator 🔴

Entwickle nach TDD einen `PasswortGenerator` mit folgenden Anforderungen
(aber NUR die, für die du vorher einen Test geschrieben hast!):

**Anforderungen (als User Stories):**

1. Als Benutzer möchte ich ein Passwort mit konfigurierbarer Länge generieren können.
2. Als Benutzer möchte ich wählen, ob Großbuchstaben enthalten sein sollen.
3. Als Benutzer möchte ich wählen, ob Ziffern enthalten sein sollen.
4. Als Benutzer möchte ich wählen, ob Sonderzeichen enthalten sein sollen.
5. Als Benutzer möchte ich, dass eine Mindestlänge von 8 Zeichen erzwungen wird.
6. Als Benutzer möchte ich, dass bei ungültigen Parametern eine klare Fehlermeldung erscheint.

**Vorgehensweise:**

- Schreibe für jede User Story **zuerst** den Test
- Implementiere dann den Code
- Refactore wenn nötig
- Commit nach jedem Green-Zustand: `[LS85] 07 TDD: User Story 1 – Passwortlänge`

Starte mit `code/starter.py` – die Testklasse ist bereits vorbereitet.

---

## Aufgabe 3 – Refactoring unter Tests 🔴

In `starter.py` findest du eine funktionierende (aber schlecht strukturierte) Funktion `verarbeite_bestellung()`.
Alle Tests dafür sind bereits grün.

**a)** Führe die vorhandenen Tests aus – sie müssen alle grün sein.

**b)** Refactore den Code: Extrahiere sinnvolle Hilfsfunktionen, verbessere Namen, beseitige Duplikation.

**c)** Führe die Tests nach jedem Refactoring-Schritt erneut aus.
**Ziel: Alle Tests bleiben grün während du den Code verbesserst.**

**d)** Protokolliere in `07_tdd_protokoll.md`:

- Welche Änderungen hast du gemacht?
- Welche Tests haben dabei geholfen, Regressionen zu verhindern?

---

## Aufgabe 4 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Entwickler soll eine Funktion `berechne_zinsen(kapital, zinssatz, jahre)` entwickeln.
Er entscheidet sich für TDD.

**(a)** Beschreiben Sie die drei Phasen des TDD-Zyklus und was in jeder Phase konkret zu tun ist. _(3 Punkte)_

**(b)** Schreiben Sie für `berechne_zinsen()` mindestens vier Tests **bevor** Sie die Funktion implementieren.
Die Tests sollen verschiedene Äquivalenzklassen und Fehlerfälle abdecken. _(6 Punkte)_

**(c)** Implementieren Sie `berechne_zinsen()` so, dass alle Tests in (b) grün werden. _(4 Punkte)_

**(d)** Nennen Sie zwei Vorteile und einen Nachteil von TDD im Berufsalltag. _(3 Punkte)_

---

## Tandem-Aufgabe 👥

**Ping-Pong TDD:**

Person A schreibt einen Test → Person B implementiert minimalen Code, der grünt, und schreibt den nächsten Test → Person A implementiert → ...

**Aufgabe:** Entwickelt gemeinsam nach diesem Muster einen einfachen `Taschenrechner` mit:
`addieren`, `subtrahieren`, `multiplizieren`, `dividieren`

Wechselt nach jedem Test die Rollen.

Am Ende: Wieviele Tests habt ihr? Ist der Code gut strukturiert?

**Erkläre deinem Tandempartner:** Erkläre, was die „Goldene TDD-Regel" bedeutet und warum es in der Praxis schwer ist, sie konsequent einzuhalten. Teile deine eigene Erfahrung aus dieser Übung.

---

## Active Recall 🧠

_Unterlagen zu:_

1. Was ist die "Goldene TDD-Regel"?
2. Was bedeutet "Baby Steps" im TDD-Kontext?
3. Warum darf man beim Green-Step "hässlichen" Code schreiben?
4. Was ist das Ziel der Refactor-Phase?
5. Wie hilft TDD dabei, über den Code nachzudenken, bevor man ihn schreibt?

---

## Reflexion 🚦

- [ x ] 🟢 Ich kann TDD anwenden und habe den Zyklus verinnerlicht
- [ ] 🟡 Ich verstehe TDD, fällt mir aber noch schwer "zuerst den Test zu schreiben"
- [ ] 🔴 Ich brauche mehr Übung oder Erklärungen

**Was war für dich die größte Herausforderung bei TDD?**

> Für mich war die größte Herausforderung definitiv die mentale Umstellung und die nötige Disziplin, mich selbst zu bremsen. Als Entwickler hat man oft sofort die komplette Lösung im Kopf und will die Funktion direkt in einem Rutsch fertig programmieren – inklusive aller Sonderfälle und der Fehlerbehandlung. Sich dann bei TDD zu zwingen, erst einen fehlschlagenden Test zu schreiben, danach nur eine einzige Zeile "harten" Code einzutippen (wie ein simples return 5) und das Spiel Schritt für Schritt zu wiederholen, fühlt sich anfangs total unnatürlich an. Man muss den Drang, "vorauszuprogrammieren", extrem kontrollieren.

**Würdest du TDD im Betrieb einsetzen? Warum / Warum nicht?**

> Ja, ich würde TDD im Betrieb einsetzen, allerdings situationsabhängig.

Warum ja: Für komplexe Business-Logik, mathematische Berechnungen (wie bei der Zins- oder Versandkostenberechnung) oder Kernkomponenten, die absolut stabil sein müssen, ist TDD genial. Es gibt mir beim späteren Refactoring oder bei Erweiterungen die Sicherheit, dass ich nichts unbemerkt kaputtmache, und sorgt für ein sauberes, modulares Code-Design. Man spart sich dadurch riesige Debugging-Sessions im Nachgang.

Warum nicht überall: Bei reinen Prototypen ("Wegwerf-Code"), bei der schnellen Gestaltung von Benutzeroberflächen (UIs) oder wenn sich die Anforderungen im Minutentakt ändern, halte ich den TDD-Aufwand im echten Projektalltag für zu starr. Da frisst das ständige Umschreiben der Tests zu Beginn zu viel Zeit. Der Mix macht es für mich aus!

---

_Bei Problemen → [Stuck Protocol](../stuck_protocol.md)_
