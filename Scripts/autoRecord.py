
import shutil
import pydirectinput
from PyInput_KeyCodes import *
from os import walk
from pathlib import Path

timing = .1
print("Quick, tab over to Syx!")
countdown = 2
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)
    
NumberOfSaves = 10
while NumberOfSaves > 0:
    print(str(NumberOfSaves) + " Recordings Left To Go!") 
    NumberOfSaves -= 1
    print("Load our Save")
    HoldAndReleaseKey(F6, timing) #Load our most recent save (preloaded into saves, then managed at the bottom)
    time.sleep(10) #Wait for save to load
    pydirectinput.click(button='right',duration=timing)


    #region Index Canera Location
    #need to set the camera to a reliable place so we can navigate from there
    print("Force into Capital View")
    pydirectinput.moveTo(3480, 38, 0) #Force into Capital View
    pydirectinput.click(duration=timing)

    #Index camera z level
    print("Set Camera Z Level")
    HoldAndReleaseKey(N, timing) #zoom 
    HoldAndReleaseKey(N, timing) #make sure we're all the way in
    HoldAndReleaseKey(N, timing) 
    HoldAndReleaseKey(N, timing) 
    HoldAndReleaseKey(N, timing) 
    HoldAndReleaseKey(B, timing) #Zoom Out
    HoldAndReleaseKey(B, timing) #More
    #Index Camera to SW Corner
    print("Animals go in the corner.")
    print("The corner!  Why didn't I think of that?")
    #Might be faster with the click-on-minimap trick below
    #In case we're over the black box outside the map, scoot out a bit
    print("Jog out in case we're over the outer border")
    HoldAndReleaseKey2(D, W, 1) 
    #Move to SW Corner to Index Camera Location
    HoldAndReleaseKey2(A, S, 6) 
    #endregion


    #region Move into Recording Position
    print("Move into Recording Position")
    pydirectinput.moveTo(3830, 105, 0) #click into place using the minimap, way faster than slow scroll, but also an option and a technique for recording (see history)
    #These pixel values change if you're using windows scaling
    pydirectinput.click(duration=timing)
    time.sleep(.01)
    pydirectinput.moveTo(3835, 105, 0) #hone in
    pydirectinput.click(duration=timing)
    time.sleep(.01)
    pydirectinput.moveTo(3665, 227, 0) #hone in
    pydirectinput.click(duration=timing)
    time.sleep(.01)



    #region Start Recording, Start Game, wait, stop recording
    print("It's Recording Time!")

    HoldAndReleaseKey(TWO, timing) #speed
    time.sleep(.2)
    #Hide the UI
    print("Hide UI")
    pydirectinput.moveTo(3600, 344, 0)
    pydirectinput.click(duration=timing)
    time.sleep(.2)

    #HoldAndReleaseKey(F12, .01) #testing positioning with a screenshot
    HoldAndReleaseKey(LEFT_BRACKET, timing) #Record if your record button is [
    print("Started Recording")
    time.sleep(21) #Record for this long
    print("Waiting")
    HoldAndReleaseKey(LEFT_BRACKET, timing) #stop recording
    print("Stopped Recording")
    time.sleep(1) #Give OBS 1 second
    pydirectinput.click(button='right',duration=timing) #return UI
    print("Showing UI")
    HoldAndReleaseKey(Z, timing) #stop game (I remapped spacebar, use SPACEBAR) or don't do this step at all
    #endregion

    #region Move Files so Quickload will load next in line and allow us to repeat
    #The saves here will be disposed after use, so have a backup of your cleaned up saves.. or make the script not do that
    folderWithAllOurSavesThatWillBeDeletedInThisProcess = "..\\..\\saves\\saves arp auto\\"

    #clean save folder so only our new one is there to be quickloaded
    [f.unlink() for f in Path("..\\..\\saves\\saves\\").glob("*") if f.is_file()] #delete save we just recorded to make room for the next
    print("Removing Files from Save Folder")
    #Get list of file names
    filenames = next(walk(folderWithAllOurSavesThatWillBeDeletedInThisProcess), (None, None, []))[2]  
   
    #Get lowest file name (earliest save that hasn't been moved out)
    moveFile = folderWithAllOurSavesThatWillBeDeletedInThisProcess + filenames[0]

    #move file into saves to be quickloaded next
    shutil.move(moveFile, "..\\..\\saves\\saves\\quicksave-1b674b0-420031-0-3ff7.save") #move in next latest save as a quicksave so we can load it
    print("Moved in file " + moveFile)
    #EndRegion
    print("goto 10")

#stich together with ffmpeg, slap the soundtrack back over the top of the city noises, baby you've got a compilation going
