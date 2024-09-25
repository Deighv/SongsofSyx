from PyInput_KeyCodes import *
from helperFunctions import *

print("Quick, tab over to Syx!")
countdown = 2
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

times = 5
while times > 0:
    print(times)
    print("Load our Save")
    HoldAndReleaseKey(F6, timing) #Load our most recent save
    time.sleep(10) #Wait for save to load
    pydirectinput.click(button='right',duration=timing)
    #index our location
    SetZoomLevel()
    MoveIntoCorner()
    MoveScreenUpxTimes(11,176)
    MoveScreenRightxTimes(4,200)

    #ScreenshotWithoutUi()
    HoldAndReleaseKey(SPACE, timing) #speed
    HideUI()
    print("Record!")
    
    pydirectinput.moveTo(1080,12, 0) #hide cursor glow and get over 1 speed
    time.sleep(timing)
    
    pydirectinput.click(duration=timing)
    time.sleep(0.1) #until click noise is done
    #could do mod to disable that noise, call it good with a few frames off
    #Or, mod+edit each clip to start at same time
    HoldAndReleaseKey(F10, timing) 
    
    print("Waiting")
    time.sleep(5) #Record for this long
    HoldAndReleaseKey(F10, timing)
    print("Stopped Recording")
    time.sleep(1) #give OBS a second
    pydirectinput.click(button='right',duration=timing) #return UI to accept keeb commands
    HoldAndReleaseKey(Z, timing)
    times -= 1