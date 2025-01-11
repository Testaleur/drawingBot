import numpy as np
from PIL import Image
import palettes
import RGBtoLAB
import distanceSecondMethod

# get the RGB palette
paletteRGB = palettes.getPaletteRGB()

# dictionnary to stock the conversion, not to calculate the pixel each time (for speed)
rgbToLabData = {}
classicDistanceData = {}

def newImagePaletteLAB(originalImage):
    imageCopy = originalImage.copy()
    imageCopyPixels = imageCopy.load()
    width, heigth = imageCopy.size
    for n in range(width):
        for m in range(heigth) :
            pixel = imageCopyPixels[n,m]
            key = str(pixel)
            pixelConversion = rgbToLabData.get(key, False)
            if(pixelConversion): # we already calculated and saved it
                imageCopyPixels[n,m] = pixelConversion
            else : # not calculated yet
                intPositionPalette = RGBtoLAB.equivalentColorFromPalette(pixel) # LAB version
                closestPixel = paletteRGB[intPositionPalette]
                imageCopyPixels[n,m] = closestPixel
                # add to the data
                rgbToLabData[key] = closestPixel
    return imageCopy

def newImagePaletteClassic(originalImage):
    imageCopy = originalImage.copy()
    imageCopyPixels = imageCopy.load()
    width, heigth = imageCopy.size
    for n in range(width):
        for m in range(heigth) :
            pixel = imageCopyPixels[n,m]
            key = str(pixel)
            pixelConversion = classicDistanceData.get(key, False)
            if(pixelConversion): # we already calculated and saved it
                imageCopyPixels[n,m] = pixelConversion
            else : # not calculated yet
                intPositionPalette = distanceSecondMethod.equivalentColorFromPalette(pixel) # classic distance version
                closestPixel = paletteRGB[intPositionPalette]
                imageCopyPixels[n,m] = closestPixel
                # add to the data
                classicDistanceData[key] = closestPixel
    return imageCopy