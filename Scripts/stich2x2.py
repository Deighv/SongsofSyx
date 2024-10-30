import pydirectinput
from PyInput_KeyCodes import *
from pathlib import Path
from helperFunctions import *
import keyboard
#This entire script operates on the assumption 
#you're running Syx base resolution, 2190x1232
timing = .1
print("Quick, tab over to Syx!")
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

#This records a 2x2 from the top right scene
ScreensToRecord = 4
ScreenNumber = 1
while ScreenNumber <= ScreensToRecord:
    print("On Screen "+ str(ScreenNumber)) 
    
    print("Load Save")
    HoldAndReleaseKey(F6, timing) #Load our most recent save
    time.sleep(11) #Wait for save to load
    pydirectinput.click(duration=timing) #enter save
    HideUI()
    HoldAndReleaseKey(D,2)#Bump into side, this is coded to record right to left
    if ScreenNumber == 1:
        print("Good X,Y")
    if ScreenNumber == 2:
        MoveScreenRightxTimes(10,-219) #left One Scene
    if ScreenNumber == 3:
        MoveScreenRightxTimes(10,-219) #left One Scene
        MoveScreenUpxTimes(7,-176) #down one scene
    if ScreenNumber == 4:
        MoveScreenUpxTimes(7,-176) #down one scene
    
    pydirectinput.moveTo(1080,12, 0) #hide cursor glow and get over 1 speed
    time.sleep(timing)    
    pydirectinput.click(duration=timing)
    HideUI()
    time.sleep(timing) #wait for click to end
    HoldAndReleaseKey(F10, timing) #start recording
    #No idea how long you can run this before things become noticeably out of sync
    time.sleep(120) #Static
    HoldAndReleaseKey(F10, timing)  
    print("Saving")
    pydirectinput.click(button='right',duration=timing) #return UI to accept keeb commands
    HoldAndReleaseKey(Z, timing) #remapped Z to pause
    time.sleep(2) #give OBS a few
    print("Saved")
    print("goto 10") 
    ScreenNumber += 1



    