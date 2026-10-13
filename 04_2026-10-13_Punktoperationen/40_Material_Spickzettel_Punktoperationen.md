# Werkzeugkasten — Punktoperationen und Schwellwert

Hier stehen Werkzeuge, keine Lösungen. Welche ihr für einen Auftrag braucht und in welcher Reihenfolge, entscheidet ihr selbst. In den Beispielen heißt das Bild `bild` — setzt eure eigenen Namen ein.

```python
import cv2
import matplotlib.pyplot as plt
```

---

## Bilder laden und vorbereiten

| Werkzeug | Was es tut |
|---|---|
| `bild = cv2.cvtColor(cv2.imread("datei.jpg"), cv2.COLOR_BGR2GRAY)` | lädt eine Aufnahme und macht ein Graubild daraus |
| `bild.shape` | Größe: (Höhe, Breite) |
| `bild[Y0:Y1, X0:X1]` | schneidet einen Ausschnitt aus: erst Zeilen (von oben nach unten), dann Spalten |
| `plt.imshow(bild, cmap="gray", vmin=0, vmax=255)` und `plt.show()` | zeigt ein Graubild an; `vmin`/`vmax` legen fest, dass 0 schwarz und 255 weiß ist |

Ohne `vmin=0, vmax=255` macht matplotlib den dunkelsten Pixel schwarz und den hellsten weiß — dann sieht jedes Bild gleich hell aus.

## Histogramm und Kennwerte

| Werkzeug | Was es tut |
|---|---|
| `plt.hist(bild.ravel(), bins=256, range=(0, 256))` | Histogramm: wie viele Pixel welchen Grauwert haben |
| `histtype="step", label="…"` und `plt.legend()` | mehrere Histogramme in einem Diagramm, als Linien mit Beschriftung |
| `plt.xlim(von, bis)` | zeigt nur einen Bereich der x-Achse — zum Vergrößern |
| `plt.xlabel("Grauwert")` | beschriftet die x-Achse |
| `bild.mean()` · `bild.std()` | Mittelwert · Streuung aller Pixel |

## Masken

| Werkzeug | Was es tut |
|---|---|
| `bild >= 150` | für jeden Pixel True oder False — eine Maske; `plt.imshow(maske, cmap="gray")` zeigt True weiß |
| `maske.sum()` · `maske.size` | Anzahl der True-Pixel · Anzahl aller Pixel |
| `(bild == 255).sum()` | zählt, wie viele Pixel genau einen Wert haben — jeder Vergleich geht: `>`, `<`, `==` |

## Mit Bildern rechnen

Ein Graubild ist eine Matrix *A*: Zeile *y*, Spalte *x*, jeder Eintrag eine Zahl. Schreibweise: Skalar klein (*c*, *d*), Vektor mit Strich (*p̄*), Matrix groß (*A*, *B*).

| Mathematik | Python | Was passiert |
|---|---|---|
| *B* = *A* + *d* | `neu = bild + 60.0` | jeder Eintrag um *d* größer |
| *B* = *c* · *A* | `neu = bild * 2.0` | jeder Eintrag *c*-mal so groß |
| *B* = *c* · *A* + *d* | `neu = bild * 2.0 + 60.0` | erst mal, dann plus |
| *b*<sub>yx</sub> | `bild[y, x]` | ein einzelner Eintrag |

Jede Rechnung mit einem Bild gilt für jeden Pixel einzeln:

```python
neu = bild + 20.0      # addieren
neu = bild - 20.0      # subtrahieren
neu = bild * 1.5       # multiplizieren
neu = bild / 255       # teilen
neu = bild ** 2.0      # hoch: Potenz
```

Schreibt die Zahl **mit Punkt** (`20.0`, nicht `20`). Dann rechnet Python mit Kommazahlen, und ein Pixel kann auch über 255 oder unter 0 liegen — mit `(neu > 255).sum()` lässt sich das zählen. Eine Bilddatei kennt nur 0 bis 255.

## Die Schwelle finden lassen: Otsu

```python
schwelle, maske = cv2.threshold(bild, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```

| Teil des Befehls | Bedeutung |
|---|---|
| `bild` | ein Graubild, so wie es geladen wurde (keine Kommazahlen) |
| `0` | hier stünde eine feste Schwelle — Otsu sucht sie selbst, die Zahl wird nicht benutzt |
| `255` | der Wert für Weiß in der Maske |
| `cv2.THRESH_BINARY + cv2.THRESH_OTSU` | in Schwarz und Weiß teilen, die Schwelle bestimmt Otsu |
| `schwelle, maske` | zurück kommen die gefundene Schwelle und die Maske aus 0 und 255 |

Weiße Pixel in dieser Maske zählt `(maske > 0).sum()`.

## Dasselbe für mehrere Aufnahmen

```python
NAMEN = ["datei_a.jpg", "datei_b.jpg"]

for name in NAMEN:
    bild = cv2.cvtColor(cv2.imread(name), cv2.COLOR_BGR2GRAY)
    # was hier eingerückt steht, passiert für jede Aufnahme
    print(name)
```

## Für „Wer noch Zeit hat"

| Werkzeug | Was es tut |
|---|---|
| `cv2.equalizeHist(bild)` | Histogrammausgleich: verteilt die Grauwerte über den ganzen Bereich 0 bis 255 |
| `bild.min()` · `bild.max()` | kleinster · größter Wert |

---

## Keine eigenen Aufnahmen?

Ladet im Kurs-Repository im Ordner `03_2026-10-06_Histogramm_Farbraeume` die Datei `sys03_notfall.zip` herunter und entpackt sie in den Ordner eures Skripts. Die Dateien heißen dann `notfall/00_halter_hell_01.jpg`, `…_seitlich_01.jpg`, `…_misch_01.jpg` und `…_dunkel_01.jpg`. Ein passender Ausschnitt: Zeilen 185 bis 790, Spalten 220 bis 1100.

---

## Wenn etwas nicht geht

| Meldung oder Bild | Lösung |
|---|---|
| Nach einer Rechnung sieht das Bild fleckig aus | Ohne Punkt gerechnet: Ein Pixel fasst nur 0 bis 255, was darüber hinausgeht, fängt wieder bei 0 an — aus 250 + 60 wird 54. Mit Punkt rechnen: `60.0` |
| Das Bild sieht nach jeder Rechnung gleich aus | `vmin=0, vmax=255` in `plt.imshow` fehlt |
| Der Ausschnitt ist leer oder viel kleiner als gedacht | Erst die Zeilen, dann die Spalten. Mit `.shape` prüfen |
| `'NoneType' object has no attribute …` | Dateiname falsch, oder in VS Code ist nicht der Ordner mit euren Bildern geöffnet |
| Fehler bei `cv2.threshold` | Otsu braucht ein Graubild, wie es geladen wurde — kein Bild, mit dem schon mit Punkt gerechnet wurde, und kein Farbbild |
| Die Maske ist komplett weiß oder schwarz | Kein Programmfehler. Schaut auf das Histogramm und die Schwelle |
| `No module named 'cv2'` | In VS Code ist nicht der Interpreter eurer Umgebung gewählt |
