import time
import shutil
import pydirectinput
from PyInput_KeyCodes import *
from os import walk
from pathlib import Path
import mouse

timing = .25

def SetZoomLevel():
    print("Set Camera Z Level")
    HoldAndReleaseKey(N, .1) #zoom 
    HoldAndReleaseKey(N, .1) #make sure we're all the way in
    HoldAndReleaseKey(N, .1) 
    HoldAndReleaseKey(N, .1) 
    HoldAndReleaseKey(N, .1) 
    HoldAndReleaseKey(B, .1) #Zoom Out
    HoldAndReleaseKey(B, .1) #More

def MoveIntoCorner():
    print("Animals go in the corner.")
    print("The corner!  Why didn't I think of that?")
    #In case we're over the black box outside the map, scoot out a bit
    pydirectinput.moveTo(1930, 55, 0)
    mouse.press(button='middle')
    mouse.move(-1900, 1160, duration = timing, absolute=False)
    mouse.release(button='middle')
    loop = 0
    #into the corner
    while loop < 12:
        pydirectinput.moveTo(21, 65, 0)
        mouse.press(button='middle')
        mouse.move(1500, 1160, duration = timing, absolute=False)
        mouse.release(button='middle')
        loop +=1
    time.sleep(timing)

def MoveScreenRightxTimes(times, pixels=30):
    while times >= 1:
        pydirectinput.moveTo(1600, 600, 0)
        mouse.press(button='middle')
        time.sleep(timing)
        mouse.move(-pixels, 0, duration = timing, absolute=False)
        time.sleep(timing)
        mouse.release(button='middle')
        times -= 1

def MoveScreenUpxTimes(times, pixels=28): #28 since y is 1232, need evenly divisible
    while times >= 1:
        pydirectinput.moveTo(1600, 600, 0)
        mouse.press(button='middle')
        time.sleep(timing)
        mouse.move(0, pixels, duration = timing, absolute=False)
        print("moving")
        time.sleep(timing)
        mouse.release(button='middle')
        times -= 1


def MoveIntoCapitalView():
    print("Force into Capital View")
    pydirectinput.moveTo(1984, 25, 0) #Force into Capital View
    pydirectinput.click(duration=timing)

def MoveScreenLeftxTimes(times, pixels=30):
    while times >= 1:
        pydirectinput.moveTo(1, 600, 0)
        mouse.press(button='middle')
        time.sleep(timing)
        mouse.move(pixels, 0, duration = timing, absolute=False)
        time.sleep(timing)
        mouse.release(button='middle')
        times -= 1
def HideUI():
    pydirectinput.moveTo(2051, 195, 0) #hide ui
    pydirectinput.click(duration= timing)
    pydirectinput.moveTo(1095, 616, 0)
    time.sleep(timing)

def ScreenshotWithoutUi():
    pydirectinput.moveTo(2051, 195, 0) #hide ui
    pydirectinput.click(duration= timing)
    time.sleep(timing)
    HoldAndReleaseKey(F12, timing) 
    time.sleep(0.5)
    pydirectinput.click(button='right',duration=timing) #show ui