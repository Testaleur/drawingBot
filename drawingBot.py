import numpy as np
import matplotlib.pyplot as plt
from math import pi
from PIL import Image
import palettes

disneyImagePath = "disneyLogo.png"

def loadImage(path) :
    try: 
        img  = Image.open(path) 
        return img
    except IOError:
        print(f"Error: Unable to load image at {path}")
        return None

def transposeImg(img) :
    transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    transposed_img.save("transposed.png")

def display(img1, img2 = None) :
    img1_np = np.array(img1)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img1_np)
    plt.title("Original image")
    plt.axis("off")
    if img2 :
        img2_np = np.array(img2)
        plt.subplot(1, 2, 2)
        plt.imshow(img2_np)
        plt.title("Modified image")
        plt.axis("off")
    plt.show()

if __name__ == '__main__':
    #load and display
    disneyLogo = loadImage(disneyImagePath)
    width, heigth = disneyLogo.size
    disneyLogo = disneyLogo.convert("RGB")

    #working on pixels
    disneyLogoCopy = disneyLogo.copy()
    disneyLogoPixels = disneyLogoCopy.load()
    mainPixel = disneyLogoPixels[0,0]
    print(f'main pixel : {mainPixel}')
    for n in range(width):
        for m in range(heigth) :
            pixel = disneyLogoPixels[n,m]
            # if(pixel[0]+pixel[1]+pixel[2] >= 3*200) : #white or almost
            #     disneyLogoPixels[n,m] = (255, 0, 0)
            if(pixel != mainPixel) : #not blue
                disneyLogoPixels[n,m] = (255, 0, 0)
    # display(disneyLogo, disneyLogoCopy)

    # display our palette
    paletteRGB = palettes.getPalette()
    print(f'number of colors : {len(paletteRGB)}')
    paletteWidth = len(paletteRGB)*50
    paletteHeight = 100
    palette = Image.new(mode="RGB", size=(paletteWidth, paletteHeight))
    palettePixels = palette.load()
    for i in range(2,paletteWidth - 2):
        for j in range(2,paletteHeight - 2):
            colorInt = i//50
            palettePixels[i,j] = paletteRGB[colorInt]
    palette_np = np.array(palette)
    plt.figure(figsize=(12, 5))
    plt.imshow(palette_np)
    plt.title("Palette")
    plt.axis("off")
    plt.show()

# x = np.arange(0,2*pi,0.1)
# y = np.sin(x)
# z = np.cos(x)
# if __name__ == '__main__':
#     plt.figure("Sinus & Cosinus")
#     plt.plot(x,y,"-r", label="sin(x)")
#     plt.plot(x,z,"-g", label="cos(x)")
#     plt.legend()
#     plt.show()