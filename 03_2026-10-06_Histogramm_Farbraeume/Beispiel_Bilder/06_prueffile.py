# Import Bib
import cv2
import matplotlib.pyplot as plt

# Import Beispielbilder
NAMEN = ["03_lagerbock_hell_01.jpg",          # eure vier Dateinamen
         "03_lagerbock_dunkel_01.jpg",
         "03_lagerbock_seitlich_01.jpg",
         "03_lagerbock_misch_01.jpg"]

# In graustufen umwandeln
for name in NAMEN:
    bild = cv2.imread(name)
    grau = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)
    print(name, grau.shape)

#Erstellung des Histograms
plt.hist(grau.ravel(), bins=256, range=(0, 256), histtype="step", label=name)




