
import shutil
import pydirectinput
from PyInput_KeyCodes import *
from os import walk
from pathlib import Path

print("Quick, tab over to Syx!")
countdown = 2
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

NumberOfSaves = 1655
while NumberOfSaves > 0:
    print(str(NumberOfSaves) + " Recordings Left To Go!") 
    NumberOfSaves -= 1

    HoldAndReleaseKey(F6, .02) #Load our most recent save (preloaded into saves, then managed at the bottom)
    time.sleep(10) #Wait for save to load
    pydirectinput.click(button='right') #return UI


    #region Index Canera Location
    #need to set the camera to a reliable place so we can navigate from there
    pydirectinput.moveTo(2320, 25, 0) #Force into Capital View
    pydirectinput.click()

    #Index camera z level
    HoldAndReleaseKey(N, .02) #zoom 
    HoldAndReleaseKey(N, .02) #make sure we're all the way in
    HoldAndReleaseKey(N, .02) 
    HoldAndReleaseKey(N, .02) 
    HoldAndReleaseKey(N, .02) 
    HoldAndReleaseKey(B, .02) #Zoom Out
    HoldAndReleaseKey(B, .02) #More

    #Index Camera to SW Corner
    print("Animals go in the corner.")
    print("The corner!  Why didn't I think of that?")
    #Might be faster with the click-on-minimap trick below
    #In case we're over the black box outside the map, scoot out a bit
    HoldAndReleaseKey2(D, W, 1) 
    #Move to SW Corner to Index Camera Location
    HoldAndReleaseKey2(A, S, 6) 
    #endregion


    #region Move into Recording Position
    pydirectinput.moveTo(2530, 105, 0) #click into place using the minimap, way faster than slow scroll, but also an option and a technique for recording (see history)
    pydirectinput.click()
    pydirectinput.moveTo(2530, 105, 0) #hone in
    pydirectinput.click()
    pydirectinput.moveTo(2530, 85, 0) #hone in
    pydirectinput.click()
    #endregion


    #region Start Recording, Start Game, wait, stop recording
    print("It's Recording Time!")

    HoldAndReleaseKey(TWO, .02) #speed
    #Hide the UI
    pydirectinput.moveTo(2400, 230, 0) #Not sure what's up with these pixel values, I'm running 4k and we're aiming for the right bar
    pydirectinput.click()
    #HoldAndReleaseKey(F12, .01) #testing positioning with a screenshot
    HoldAndReleaseKey(LEFT_BRACKET, .02) #Record if your record button is [
    time.sleep(20) #Record for this long
    HoldAndReleaseKey(LEFT_BRACKET, .02) #stop recording
    pydirectinput.click(button='right') #return UI
    HoldAndReleaseKey(Z, .02) #stop game (I remapped spacebar, use SPACEBAR)
    print("Stopped.")
    #endregion

    #region Move Files so Quickload will load next in line and allow us to repeat
    #FYI Saves are encoded like:
    #Name-IterationOfSaveProbablyIncludesDaysAgoInHex-Version-0-PopulationCountInHex.save
    #There's another script to decode the save names so you can rename+sort them numerically so the below trick works

    #The saves here will be disposed after use, so have a backup of your cleaned up saves.. or make the script not do that
    folderWithAllOurSavesThatWillBeDeletedInThisProcess = "..\\..\\saves\\saves arp auto\\"

    #clean save folder so only our new one is there to be quickloaded
    [f.unlink() for f in Path("..\\..\\saves\\saves\\").glob("*") if f.is_file()] #delete save we just recorded to make room for the next

    #Get list of file names
    filenames = next(walk(folderWithAllOurSavesThatWillBeDeletedInThisProcess), (None, None, []))[2]  
   
    #Get lowest file name (earliest save that hasn't been moved out)
    moveFile = folderWithAllOurSavesThatWillBeDeletedInThisProcess + filenames[0]

    #move file into saves to be quickloaded next
    shutil.move(moveFile, "..\\..\\saves\\saves\\quicksave-1b674b0-420031-0-3ff7.save") #move in next latest save as a quicksave so we can load it
    #EndRegion


#stich together with ffmpeg, slap the soundtrack back over the top of the city noises, baby you've got a compilation going
