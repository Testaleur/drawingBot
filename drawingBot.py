import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import convertArrayWithPalette

imageSize = 40

def loadImage(path) :
    try: 
        img  = Image.open(path)
        return img.convert("RGB")
    except IOError:
        print(f"Error: Unable to load image at {path}")
        return None

def transposeImg(img) :
    transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    transposed_img.save("transposed.png")

def display(img1, img2 = None, img3 = None) :
    img1_np = np.array(img1)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(img1_np)
    plt.title("Original image")
    plt.axis("off")
    if img2 :
        img2_np = np.array(img2)
        plt.subplot(1, 3, 2)
        plt.imshow(img2_np)
        plt.title("Modified image with lab")
        plt.axis("off")
    if img3 :
        img3_np = np.array(img3)
        plt.subplot(1, 3, 3)
        plt.imshow(img3_np)
        plt.title("Modified image with euclidian distance")
        plt.axis("off")
    plt.show()


def imagePixeled(imagePath):
    imageLoaded = loadImage(imagePath)
    if imageLoaded.width > 50 or imageLoaded.height > 50:
        imageLoaded.thumbnail((imageSize, imageSize))
    imagePaletteLab = convertArrayWithPalette.newImagePaletteLAB(imageLoaded)
    imagePaletteClassic = convertArrayWithPalette.newImagePaletteClassic(imageLoaded)
    return imagePaletteLab

    # display(imageLoaded, imagePaletteLab, imagePaletteClassic)