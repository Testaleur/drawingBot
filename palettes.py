from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

paletteListe = [ "#000000", 
    "#4c4c4c",
    "#c1c1c1",
    "#ffffff",
    "#740b07",
    "#ef130b",
    "#c23800",
    "#ff7100",
    "#ffe400",
    "#e8a200",
    "#005510",
    "#00cc00",
    "#0e0865",
    "#231fd3",
    "#00569e",
    "#00b2ff",
    "#550069" ]

def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def turnIntoRGB(listHEX):
    return [hex_to_rgb(elt.lstrip('#')) for elt in listHEX]

paletteListeRGB = turnIntoRGB(paletteListe)

paletteWidth = len(paletteListeRGB)*50
paletteHeight = 100
palette = Image.new(mode="RGB", size=(paletteWidth, paletteHeight))
palettePixels = palette.load()
for i in range(2,paletteWidth - 2):
    for j in range(2,paletteHeight - 2):
        colorInt = i//50
        palettePixels[i,j] = paletteListeRGB[colorInt]
palette_np = np.array(palette)

def getPalette() :
    return palette_np

def getPaletteRGB() :
    return paletteListeRGB

# display our palette
# plt.figure(figsize=(12, 5))
# plt.imshow(palette_np)
# plt.title("Palette")
# plt.axis("off")
# plt.show()