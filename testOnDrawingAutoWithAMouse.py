from pynput.mouse import Button, Controller
import time
import keyboard
from math import sin

mouse = Controller()

## get position
# print(mouse.position)
## set position
# mouse.position = (10, 20)
## move
# mouse.move(3, 0)
# wait
# time.sleep(0.1)
# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)
# # Double click
# mouse.click(Button.left, 2)

running = True

def nextPosition(mousePos,initPos):
    newX = mousePos[0]+2
    newY = initPos[1] + 40*sin(100*(newX - initPos[0])/initPos[0])
    return (newX,newY)

def on_event(event):
    global running
    if (event.name == 'space') and (event.event_type == "down"):
        print("Starting drawing")
        posInit = mouse.position
        mouse.press(Button.left)
        for i in range(100):
            mouse.position = nextPosition(mouse.position, posInit)
            time.sleep(0.05)
        mouse.release(Button.left)
        print("Stopping drawing")
        running = False

    if event.name == 'esc':  # stop with es  
        print("Stopping listener...")
        mouse.release(Button.left)
        running = False

keyboard.hook(on_event)
while running:
    pass
keyboard.unhook_all()