from skimage import io, color
import numpy as np
from math import sqrt
import palettes

#no conversion to lab this time, regular euclidian distance

def deltaE(pixel1, pixel2): #distance between 2 rgb
    px1np = np.array(pixel1)
    px2np = np.array(pixel2)
    return np.linalg.norm(px1np - px2np)

paletteRGB = palettes.getPaletteRGB()

def equivalentColorFromPalette(RGBpixel): # return the closest color of the palette
    paletteInt = 0
    distancesList = list(map(lambda colorPalette: deltaE(RGBpixel, colorPalette), paletteRGB))
    minDistance = min(distancesList)
    paletteInt = distancesList.index(minDistance) # == right color of the palette
    # print(f'Min distance : {minDistance}, palette int : {paletteInt}')
    return paletteInt




