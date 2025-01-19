from pynput.mouse import Button, Controller
import time
import keyboard
import drawingBot
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import palettes

imagePath = "images/" + "wattouat.png"
imgToDraw = drawingBot.imagePixeled(imagePath) #image ready to be drawn
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
print("ready to listen")
def on_event(event):
    global running

    if (event.name == 'space') and (event.event_type == "down"):
        print("Starting drawing")

        initialPos = mouse.position
        currentDrawingPos = mouse.position
        paletteInt = 0

        # pixel by pixel version : 
        # for i in range(height):
        #     for j in range(width):
        #         pixel = imgToDrawPixels[i,j]
        #         indexPixelColor = paletteRGB.index(pixel)
        #         if(paletteInt != indexPixelColor): # we need to change color
        #             mouse.position = colorsChoicePositions[indexPixelColor]
        #             paletteInt = indexPixelColor
        #             mouse.press(Button.left) # selection of the color
        #             mouse.release(Button.left)
                
        #         currentDrawingPos = (initialPos[0] + 5*i, initialPos[1] + 5*j)

        #         if(mouse.position != currentDrawingPos): # we place the mouse back if needed
        #             mouse.position = currentDrawingPos
        #         # then we place the pixel

        #         mouse.press(Button.left)
        #         mouse.release(Button.left)

        # second method : color by color
        imgToDrawPixelsNP = np.array([[imgToDrawPixels[j, i] for i in range(height)] for j in range(width)])
        for n in range(len(colorsChoicePositions)):
            currentColor = paletteRGB[n]
            print(currentColor)
            filter = np.all(imgToDrawPixelsNP == currentColor, axis=-1)
            matching_pixels = np.argwhere(filter)
            matching_pixels = [tuple(coord) for coord in matching_pixels]
            matching_pixels = [(int(x), int(y)) for x, y in matching_pixels]

            # Select the color
            mouse.position = colorsChoicePositions[n]
            mouse.press(Button.left)
            mouse.release(Button.left)

            if matching_pixels:
                start_pos = (initialPos[0] + 5 * matching_pixels[0][0], initialPos[1] + 5 * matching_pixels[0][1])
                mouse.position = start_pos
                # start holding
                mouse.press(Button.left)

                for i in range(1, len(matching_pixels)):
                    current_pixel = matching_pixels[i]
                    previous_pixel = matching_pixels[i - 1]

                    currentDrawingPos = (initialPos[0] + 5 * current_pixel[0], initialPos[1] + 5 * current_pixel[1])
                    previousDrawingPos = (initialPos[0] + 5 * previous_pixel[0], initialPos[1] + 5 * previous_pixel[1])

                    # is the pixel next to it the same color?
                    if (current_pixel[0] == previous_pixel[0] and abs(current_pixel[1] - previous_pixel[1]) == 1) or \
                    (current_pixel[1] == previous_pixel[1] and abs(current_pixel[0] - previous_pixel[0]) == 1):
                        mouse.position = currentDrawingPos # drawing the line
                    else:
                        #release the click
                        mouse.release(Button.left)
                        mouse.position = currentDrawingPos
                        mouse.press(Button.left)
                #end for this color
                mouse.release(Button.left)


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