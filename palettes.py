from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

paletteListe = [ 
    "#ffffff",
    "#c1c1c1",
    "#ef130b",
    "#ff7100",
    "#ffe400",
    "#00cc00",
    "#08fc94",
    "#00b2ff",
    "#231fd3",
    "#a300ba",
    "#df69a7",
    "#ffac8e",
    "#a0522d",
    "#63300d",
    "#c9754c",
    "#853453",
    "#540067",
    "#0e0864",
    "#00559c",
    "#00775c",
    "#004519",
    "#e5a000",
    "#c03700",
    "#730b07",
    "#4f4f4f",
    "#000000"
]

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
    for j in range(2,paletteHeight//2):
        colorInt = (i//50)//2
        palettePixels[i,j] = paletteListeRGB[colorInt]
    for j in range(paletteHeight//2 + 1, paletteHeight - 2):
        colorInt = 25 - (i//50)//2
        palettePixels[i,j] = paletteListeRGB[colorInt]
palette_np = np.array(palette)

def getPalette() :
    return palette_np

def getPaletteRGB() :
    return paletteListeRGB

#display our palette
# plt.figure(figsize=(12, 5))
# plt.imshow(palette_np)
# plt.title("Palette")
# plt.axis("off")
# plt.show()