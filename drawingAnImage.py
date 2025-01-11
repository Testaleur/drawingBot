from pynput.mouse import Button, Controller
import time
import keyboard

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
        # posInit = mouse.position
        # mouse.press(Button.left)
        # for i in range(100):
        #     mouse.position = nextPosition(mouse.position, posInit)
        #     time.sleep(0.05)
        # mouse.release(Button.left)
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