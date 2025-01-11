from skimage import io, color
import numpy as np
from math import sqrt
import palettes

def RGBtoLAB(RGBpixel):
    normalized_pixel = np.array(RGBpixel) / 255.0
    normalized_pixel = normalized_pixel.reshape((1, 1, 3))
    lab_pixel = color.rgb2lab(normalized_pixel)
    return lab_pixel[0, 0]

def deltaE(pixel1, pixel2): #distance between 2 lab
    px1np = np.array(pixel1)
    px2np = np.array(pixel2)
    return np.linalg.norm(px1np - px2np)

paletteRGB = palettes.getPaletteRGB()
paletteLAB = list(map(RGBtoLAB, paletteRGB))

def equivalentColorFromPalette(RGBpixel): # return the closest color of the palette
    paletteInt = 0
    LABpixel = RGBtoLAB(RGBpixel)
    distancesList = list(map(lambda colorPalette: deltaE(LABpixel, colorPalette), paletteLAB))
    minDistance = min(distancesList)
    paletteInt = distancesList.index(minDistance) # == right color of the palette
    # print(f'Min distance : {minDistance}, palette int : {paletteInt}')
    return paletteInt





