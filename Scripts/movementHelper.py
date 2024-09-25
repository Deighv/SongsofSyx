import time
import shutil
import pydirectinput
from PyInput_KeyCodes import *
from os import walk
from pathlib import Path
import mouse

def MoveIntoCorner():
    pydirectinput.moveTo(1930, 55, 0)
    mouse.press(button='middle')
    mouse.move(-1900, 1160, absolute=False)
    mouse.release(button='middle')
    #New Faster Move Into Corner
    loop = 0
    while loop < 5:
        pydirectinput.moveTo(1930, 55, 0)
        mouse.press(button='middle')
        mouse.move(-1900, 1160, absolute=False)
        mouse.release(button='middle')
        loop +=1
 