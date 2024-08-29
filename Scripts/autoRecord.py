import pydirectinput
from PyInput_KeyCodes import *
print("Quick tab over to Syx!")
countdown = 2
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)


#region First Criteria: need to be able to set the camera to a reliable place
#region index camera z level
HoldAndReleaseKey(N, .02) #zoom 
HoldAndReleaseKey(N, .02) #make sure we're all the way in
HoldAndReleaseKey(N, .02) #all the way in if it's stepped out
HoldAndReleaseKey(N, .02) #all the way in
HoldAndReleaseKey(N, .02) #allllll the way in
HoldAndReleaseKey(B, .02) #Zoom Out
HoldAndReleaseKey(B, .02) #More
#endregion

#Region Index Camera to SW Corner
print("Animals go in the corner.")
print("The corner!  Why didn't I think of that?")
#In case we're over the black box over the SW corner, scoot out a bit
HoldAndReleaseKey2(D, W, 1) 
#Move to SW Corner to Index Camera Location
HoldAndReleaseKey2(A, S, 6) 
#EndRegion

#needs further testing!
#Panning speed is tied to framerate, if it goes down so will your camera speed, leaving you in a different spot.  You may need to lower your max fps or resolution to get a consistent place
#even then, work in progress
#Region Move into Recording Position
#Move into position with slow pan remapped to J K L I
print("Move Right for 25 Seconds")
time.sleep(.2) #Make sure we're ready for commands
HoldAndReleaseKey(L, 25)
time.sleep(.2)
print("Move Up for 8.5 Seconds")
HoldAndReleaseKey(I, 8.5)
#EndRegion

#Region Start Recording, Start Game, wait, stop recording



print("Start Recording, Set Speed")

HoldAndReleaseKey(TWO, .01) #Set Speed, gotta do this before you hide the UI
#Hide the UI
pydirectinput.moveTo(2400, 230, 0) #I have *no* idea what is up with these pixels, I'm running 4k and the game renders internally as 2190x1232
pydirectinput.click()
HoldAndReleaseKey(LEFT_BRACKET, .01) #Record if your record button is [
time.sleep(5) #Record for this long, 5 for testing
HoldAndReleaseKey(LEFT_BRACKET, .01)
pydirectinput.click(button='right') #return UI
HoldAndReleaseKey(Z, .01) #Set Speed (I set spacebar to speed 1 hence this being Z)
print("Stop Recording, Stop Speed")
#EndRegion

#Region Move Files so Quickload will load next larger save/next in line, Repeat process
###############
#EndRegion

#stich together with ffmpeg, slap the soundtrack back over the top of the city noises, baby you've got a compilation going
