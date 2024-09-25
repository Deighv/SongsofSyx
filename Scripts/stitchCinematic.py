
import shutil
import pydirectinput
from PyInput_KeyCodes import *
from os import walk
from pathlib import Path
from helperFunctions import *
import keyboard
#This entire script operates on the assumption you're running Syx base resolution, 2190x1232
timing = .1
print("Quick, tab over to Syx!")
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)
    
NumberOfSaves = 1
while NumberOfSaves <= 25:
    print("On Screen "+ str(NumberOfSaves)) 
    
    print("Load our Save")
    HoldAndReleaseKey(F6, timing) #Load our most recent save
    time.sleep(10) #Wait for save to load
    pydirectinput.click(button='right',duration=timing)

    #region Index Canera Location
    MoveIntoCapitalView()
    SetZoomLevel()
    MoveIntoCorner()

    #move into initial recording position
    MoveScreenUpxTimes(11,176)
    MoveScreenRightxTimes(4,200)

    match NumberOfSaves: #move over X
        case 1|6|11|16|21: #On the first run, we're in the right spot
            print("Good X")
        case 2|7|12|17|22:
            MoveScreenRightxTimes(10,219) #Right One Scene
        case 3|8|13|18|23:
            MoveScreenRightxTimes(20,219)  #move over two scenes
        case 4|9|14|19|24:
            MoveScreenRightxTimes(30,219)  #three scenes, ah ah ah
        case 5|10|15|20|25:
            MoveScreenRightxTimes(40,219)    

    match NumberOfSaves: #move over Y
        case 1|2|3|4|5: #On the first run, we're in the right spot
            print("Good Y")
        case 6|7|8|9|10:
            MoveScreenUpxTimes(7,176) #Up One Scene #move over one scene
        case 11|12|13|14|15:
            MoveScreenUpxTimes(14,176) #move over two scenes
        case 16|17|18|19|20:
            MoveScreenUpxTimes(21,176)  #three scenes, ah ah ah
        case 21|22|23|24|25:
            MoveScreenUpxTimes(28,176) 

    #HoldAndReleaseKey(TWO, timing) #speed
    HideUI()
    print("Record!")
    
    pydirectinput.moveTo(1080,12, 0) #hide cursor glow and get over 1 speed
    time.sleep(timing)
    
    pydirectinput.click(duration=timing)
    time.sleep(0.1) #until click noise is done
    #could do mod to disable that noise, call it good with a few frames off
    #Or, use end of play as when to edit clip
    HoldAndReleaseKey(F10, timing) 
    
    print("Waiting")
    time.sleep(60) #Record for this long
    
    HoldAndReleaseKey(F10, timing)
    print("Stopped Recording")
    time.sleep(1) #give OBS a second
    pydirectinput.click(button='right',duration=timing) #return UI to accept keeb commands
    HoldAndReleaseKey(Z, timing)
    print("goto 10") 
    NumberOfSaves += 1
#Commands to stitch together with ffmpeg todo: automate
#Note, I'm recording bottom left to top right, ffmpeg wants top left to bottom right, so files need to be renamed/input order needs to be reversed
#ffmpeg -threads 16 -i 01.mkv -i 02.mkv -i 03.mkv -i 04.mkv -i 05.mkv -i 06.mkv -i 07.mkv -i 08.mkv -i 09.mkv -i 10.mkv -i 11.mkv -i 12.mkv -i 13.mkv -i 14.mkv -i 15.mkv -i 16.mkv -i 17.mkv -i 18.mkv -i 19.mkv -i 20.mkv -i 21.mkv -i 22.mkv -i 23.mkv -i 24.mkv -i 25.mkv -filter_complex "xstack=grid=5_5" output.mkv
#Shrink it because nothing can handle that many pixels:
#ffmpeg -i output.mkv -s 7680x4320 -c:a copy output2.mkv