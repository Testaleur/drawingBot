from pynput.mouse import Button, Controller
import time
import keyboard
import drawingBot
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import palettes

imagePath = "images/" + "wattouat.png"
imgToDraw = drawingBot.imagePixeled(imagePath)
width, height = imgToDraw.size
imgToDrawPixels = imgToDraw.load()

paletteRGB = palettes.getPaletteRGB()

mouse = Controller()
colorsChoicePositions = [
(462, 723),
(481, 727),
(500, 726),
(518, 727),
(538, 726),
(554, 728),
(577, 728),
(593, 728),
(610, 726),
(629, 726),
(651, 726),
(671, 726),
(687, 728),
(691, 750),
(671, 746),
(656, 744),
(637, 744),
(618, 745),
(593, 746),
(571, 746),
(556, 746),
(534, 746),
(517, 746),
(490, 746),
(481, 746),
(462, 747)
]

running = True
def on_event(event):
    global running
    if (event.name == 'space') and (event.event_type == "down"):
        print("Starting drawing")

        initialPos = mouse.position
        currentPos = mouse.position
        paletteInt = 0

        for i in range(width):
            for j in range(height):
                pixel = imgToDrawPixels[i,j]
                indexPixelColor = paletteRGB.index(pixel)
                if(paletteInt != indexPixelColor): # we need to change color
                    mouse.position = colorsChoicePositions[indexPixelColor]
                    paletteInt = indexPixelColor
                    mouse.press(Button.left) # selection of the color
                    mouse.release(Button.left)
                
                if(mouse.position != currentPos): # we place the mouse back if needed
                    mouse.position = currentPos
                # then we place the pixel
                mouse.press(Button.left)
                mouse.release(Button.left)

                if j < height - 1 : # we move the mouse to the bottom
                    #mouse.position = (currentPos[0], currentPos[1] + 1)
                    pass
                else : # we go back to the top and move to the right
                    # mouse.position = (currentPos[0] + 1, initialPos[1])
                    pass
        print("Stopping drawing")
        running = False

    if event.name == 'esc':  # stop with esc
        print("Stopping listener...")
        mouse.release(Button.left)
        running = False
    
    if event.name == "a" and event.event_type == "down" : 
        print(mouse.position)

keyboard.hook(on_event)
while running:
    pass
keyboard.unhook_all()