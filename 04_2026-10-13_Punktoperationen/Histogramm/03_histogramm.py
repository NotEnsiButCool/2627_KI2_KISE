import cv2
import matplotlib.pyplot as plt

### Bilder laden und vorbereiten 

von = 0
bis = 256

bild = cv2.cvtColor(cv2.imread("C:/0-Programmieren_Local/KI2/GITREPO/2627_KI2_KISE/04_2026-10-13_Punktoperationen/Histogramm/hell.png"), cv2.COLOR_BGR2GRAY)

print(bild.shape)

# plt.imshow(bild, cmap="gray", vmin=0, vmax=255)
# plt.show()


bild = bild[190:480, 530:880]

plt.imshow(bild, cmap="gray", vmin=0, vmax=255)
plt.show()

###########

### Histogramm und Kennwerte

plt.hist(bild.ravel(), bins=256, range=(0, 256), histtype="step", label="…" )	# Histogramm: wie viele Pixel welchen Grauwert haben
             	                                                                # mehrere Histogramme in einem Diagramm, als Linien mit Beschriftung
plt.legend()
plt.xlim(von, bis)	                                # zeigt nur einen Bereich der x-Achse — zum Vergrößern
plt.xlabel("Grauwert")	                            # beschriftet die x-Achse
bild.mean() 
bild.std()
plt.show()

print("Mittelwert:", bild.mean())
print("Standardabweichung:", bild.std())

###

### Maske

schwellwert = 210
bild = bild >= schwellwert
plt.imshow(bild, cmap="gray")
plt.show()





