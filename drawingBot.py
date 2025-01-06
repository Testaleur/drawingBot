import numpy as np
import matplotlib.pyplot as plt
from math import pi
from PIL import Image

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

def display(img) :
    img_np = np.array(img)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img_np)
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    #load and display
    disneyLogo = loadImage(disneyImagePath)
    disneyLogo = disneyLogo.convert("RGB")
    print(disneyLogo)
    display(disneyLogo)

    #working on pixels
    disneyLogoPixels = disneyLogo.load()
    print([disneyLogoPixels[0,n] for n in range(10)])

# x = np.arange(0,2*pi,0.1)
# y = np.sin(x)
# z = np.cos(x)
# if __name__ == '__main__':
#     plt.figure("Sinus & Cosinus")
#     plt.plot(x,y,"-r", label="sin(x)")
#     plt.plot(x,z,"-g", label="cos(x)")
#     plt.legend()
#     plt.show()