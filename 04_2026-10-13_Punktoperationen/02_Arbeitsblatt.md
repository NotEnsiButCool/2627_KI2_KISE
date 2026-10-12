# DS 04 — Arbeitsblatt

**Punktoperationen: Anderes Licht, dieselbe Prüfung · 13.10.2026**

Ein neues Skript im Ordner eurer vier Aufnahmen aus DS 03. Welche Befehle ihr braucht, entscheidet ihr selbst — sie stehen im Werkzeugkasten. Wer festhängt, öffnet die Tipps.

---

## P1 — Macht das Bauteil schwarz-weiß (etwa 15 min)

**Ziel:** Ein Bild, in dem das Bauteil weiß ist und der Untergrund schwarz.

**Auftrag:** Erstellt das Histogramm von `misch`, legt einen Schwellwert fest und macht das Bild schwarz-weiß. Wendet dann **dieselbe** Schwelle auf `dunkel` an. Was kommt heraus — und warum?

Achtet darauf, dass ihr von beiden Aufnahmen denselben Bildausschnitt betrachtet: euer Bauteil mit etwas Untergrund ringsum.

**Ergebnis:** Unser Schwellwert:

| | `misch` | `dunkel` |
|---|---|---|
| Ausschnitt (Zeilen, Spalten) | | |
| Mittelwert | | |
| Streuung | | |
| Anteil weiß bei unserer Schwelle | % | % |

Woran liegt es? Ein Satz, der sich auf das Histogramm bezieht:

---

## P2 — Weg 1: Passt das Bild an (etwa 17 min)

**Ziel:** Die dunkle Aufnahme nutzt die Helligkeit so wie `misch` — gleicher Mittelwert, gleiche Streuung. Dann sollte eure Schwelle aus P1 wieder greifen.

**Auftrag:** Bearbeitet `dunkel` mit einer Punktoperation *B* = *c* · *A* + *d*. Findet *c* und *d*. Prüft danach, ob eure Schwelle wieder ungefähr dieselbe Maske liefert wie bei `misch`.

**Ergebnis:**

| Rechnung | Mittelwert | Streuung | Anteil weiß in % | Maske wie bei `misch`? |
|---|---|---|---|---|
| `misch` (das Ziel) | | | | — |
| | | | | |
| | | | | |
| | | | | |

Unsere Rechnung: *B* = … · *A* +

Welcher Teil der Rechnung ändert die Streuung, welcher nur den Mittelwert? Belegt es mit euren Zahlen.

**Untersucht dann zwei Fragen:**

- Ist durch eure Rechnung Information dazugekommen — gibt es jetzt mehr verschiedene Grauwerte als vorher? Belegt es am Histogramm.

- Was passiert, wenn ihr es übertreibt? Wie viel Prozent der Pixel sind dann nicht mehr zu retten, und warum?

---

## P3 — Weg 2: Passt die Schwelle an (etwa 14 min)

**Ziel:** Der Rechner findet die Schwelle selbst — für jede Aufnahme neu.

**Auftrag:** Bestimmt den Schwellwert automatisch mit dem Otsu-Algorithmus, erst für `dunkel`, dann für alle vier Aufnahmen. Tippt **vorher**, bei welchen Aufnahmen es schiefgeht.

Unser Tipp:

**Ergebnis:**

| Aufnahme | Schwelle | Anteil weiß in % | Maske brauchbar? |
|---|---|---|---|
| `hell` | | | |
| `seitlich` | | | |
| `misch` | | | |
| `dunkel` | | | |

Brauchbar heißt: Das Bauteil ist als eine Fläche zu erkennen, der Untergrund bleibt schwarz. Tragt euer Ergebnis in die Tabelle an der Tafel ein.

Wählt eine Aufnahme, bei der es schiefgeht. Was zeigt ihr Histogramm, das bei `misch` anders ist?

---

## P4 — Prüfungsformat: Kennlinie zuordnen (wer fertig ist)

> Eine dunkle Aufnahme wurde mit drei Punktoperationen bearbeitet. Oben stehen die drei Kennlinien A, B und C, unten die drei Histogramme danach.

![Drei Kennlinien A, B, C, das Histogramm vorher und drei Histogramme danach](02_Arbeitsblatt_Kennlinien.png)

a) Der hellere Berg liegt vorher beim Grauwert 48. Wo liegt er nach A, B und C?

   A: … B: … C:

b) Ordnet zu und begründet jeweils mit **einem** Merkmal des Histogramms.

   Histogramm 1 → … weil

   Histogramm 2 → … weil

   Histogramm 3 → … weil

c) Dieselben drei Kennlinien, angewendet auf den Grauwert 200: Bei welchen geht Information verloren?

---

## Wer noch Zeit hat

- Macht `seitlich` heller, ohne dass ein einziger Pixel über 255 landet — mit welchem Werkzeug geht das, mit welchem nicht?
- Probiert den Histogrammausgleich auf `dunkel` und danach eure Schwelle. Was ist aus dem Untergrund geworden?
- Bringt `misch` auf Werte zwischen 0 und 1. Was wird aus Mittelwert und Streuung?
