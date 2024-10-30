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

#Loads last Save in initial top left recording position, must be nearish top left corner
#This records about 685x385 tiles
#Also when you load your save it'll be in a slightly different place than where you saved but its consistent lol
#Record Horizontally or Vertically
RecordHorizontally = True    
ScreensToRecord = 25
if not RecordHorizontally:
    ScreensToRecord = 30
ScreenNumber = 1
while ScreenNumber <= ScreensToRecord:
    print("On Screen "+ str(ScreenNumber)) 
    
    print("Load Save")
    HoldAndReleaseKey(F6, timing) #Load our most recent save
    time.sleep(11) #Wait for save to load
    pydirectinput.click(duration=timing) #enter save

    #if RecordHorizontally:
    #could use quicksave/quickload    
    if RecordHorizontally:
        match ScreenNumber: #move over X
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

        match ScreenNumber: #move over Y
            case 1|2|3|4|5: #On the first run, we're in the right spot
                print("Good Y")
            case 6|7|8|9|10:
                MoveScreenUpxTimes(7,-176) #down One Scene #move over one scene
            case 11|12|13|14|15:
                MoveScreenUpxTimes(14,-176) #move over two scenes
            case 16|17|18|19|20:
                MoveScreenUpxTimes(21,-176)  #three scenes, ah ah ah
            case 21|22|23|24|25:
                MoveScreenUpxTimes(28,-176) 

    if not RecordHorizontally:
        print("Record Vertically") #3 Scenes Wide, 10 scenes tall, which is a bit over what is available
        #30 scenes total, 3x10
        MoveIntoCorner()
        SetZoomLevel()
        MoveScreenUpxTimes(1,-19)
        MoveScreenRightxTimes(15,214)
        match ScreenNumber: #move over X
            case 1|4|7|10|13|16|19|22|25|28: 
                print("Good X")
            case 2|5|8|11|14|17|20|23|26|29:
                MoveScreenRightxTimes(10,219) #Right one Scene
            case 3|6|9|12|15|18|21|24|27|30:
                MoveScreenRightxTimes(20,219)  #right two scenes  
        
        match ScreenNumber: #move over Y
            case 1|2|3: #On the first run, we're in the right spot
                print("Good Y")
            case 4|5|6:
                MoveScreenUpxTimes(7,-176) #down (under) one scene
            case 7|8|9:
                MoveScreenUpxTimes(14,-176) #down (under) two scenes
            case 10|11|12:
                MoveScreenUpxTimes(21,-176) #down (under) three scenes
            case 13|14|15:
                MoveScreenUpxTimes(28,-176) 
            case 16|17|18:
                MoveScreenUpxTimes(35,-176) 
            case 19|20|21:
                MoveScreenUpxTimes(42,-176) 
            case 22|23|24:
                MoveScreenUpxTimes(49,-176) 
            case 25|26|27:
                MoveScreenUpxTimes(56,-176) 
            case 28|29|30:
                MoveScreenUpxTimes(63,-176) 
    
    pydirectinput.click(button='right',duration=timing) #make sure the mouse is focused on the screen
    HoldAndReleaseKey(SPACE, timing) #remapped 1 to space
    HoldAndReleaseKey(SPACE, timing) #play in slowmo
    HideUI()
    time.sleep(timing) #wait for click to end
    pydirectinput.moveTo(1,1, 0) #hide cursor glow
    time.sleep(timing)
    HoldAndReleaseKey(F10, timing) #start recording
    #pydirectinput.moveTo(1080,40, 0) #show gameclock to get time sync to edit to
    #time.sleep(1) 
    #No idea how long you can run this before things become noticeably out of sync
    HoldAndReleaseKey2(LEFT_ALT, W, 60) #pan up, turn off shadows+drop brightness to 10-15% or you'll get shader artifacting
    time.sleep(timing)
    #time.sleep(60) Static
    HoldAndReleaseKey(F10, timing)
    

    #HoldAndReleaseKey(F9, timing) #Trigger 60 Second Replay Buffer
    #clips are exactly 60.0240 long, but have screen dragging? clicks, etc embedded
    #Replay buffer timing seems to drift even worse than manual record
    print("Saving")
    pydirectinput.click(button='right',duration=timing) #return UI to accept keeb commands
    HoldAndReleaseKey(Z, timing) #remapped Z to pause
    time.sleep(2) #give OBS a few
    print("Saved")
    print("goto 10") 
    ScreenNumber += 1
#Commands to stitch together with ffmpeg todo: automate
#ffmpeg -threads 16 -i 01.mkv -i 02.mkv -i 03.mkv -i 04.mkv -i 05.mkv -i 06.mkv -i 07.mkv -i 08.mkv -i 09.mkv -i 10.mkv -i 11.mkv -i 12.mkv -i 13.mkv -i 14.mkv -i 15.mkv -i 16.mkv -i 17.mkv -i 18.mkv -i 19.mkv -i 20.mkv -i 21.mkv -i 22.mkv -i 23.mkv -i 24.mkv -i 25.mkv -filter_complex "xstack=grid=5_5" output.mkv
#Shrink it because nothing can handle that many pixels:
#ffmpeg -i output.mkv -s 7680x4320 -c:a copy output2.mkv
#Stitch Vertical ffmpeg -threads 16 -i 01.mkv -i 02.mkv -i 03.mkv -i 04.mkv -i 05.mkv -i 06.mkv -i 07.mkv -i 08.mkv -i 09.mkv -i 10.mkv -i 11.mkv -i 12.mkv -i 13.mkv -i 14.mkv -i 15.mkv -i 16.mkv -i 17.mkv -i 18.mkv -i 19.mkv -i 20.mkv -i 21.mkv -i 22.mkv -i 23.mkv -i 24.mkv -i 25.mkv -i 26.mkv -i 27.mkv -i 28.mkv -i 29.mkv -i 30.mkv -filter_complex "xstack=grid=3_10" output.mkv
#Trim Pixels from Top ffmpeg -threads 16 -i output.mkv -filter:v "crop=in_w:in_h-32:0:out_h" -c:a copy VerticalTrimmed.mkv
#ffmpeg -threads 16 -i VerticalTrimmed.mkv -s 4320x7680 -c:a copy Vertical8k.mkv