import pydirectinput
from PyInput_KeyCodes import *
print("Quick tab over to Syx!")
countdown = 2
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

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


#Region Start Recording, Start Game, wait, stop recording
print("It's Recording Time")

HoldAndReleaseKey(TWO, .01) #speed
#Hide the UI
pydirectinput.moveTo(2400, 230, 0) #Not sure what's up with these pixel values, I'm running 4k and we're aiming for the right bar
pydirectinput.click()
#HoldAndReleaseKey(F12, .01) #testing positioning with a screenshot
HoldAndReleaseKey(LEFT_BRACKET, .01) #Record if your record button is [
time.sleep(60) #Record for this long
HoldAndReleaseKey(LEFT_BRACKET, .01) #stop recording
pydirectinput.click(button='right') #return UI
HoldAndReleaseKey(Z, .01) #stop game (I remapped spacebar, check pyInput for values [SPACEBAR])
print("Stoped.")
#EndRegion

#Region Move Files so Quickload will load next larger save/next in line, Repeat process
#Saves are encoded like:
#Name-IterationOfSaveProbablyIncludesDaysAgoInHex-Version-0-PopulationCountInHex.save
###############
#EndRegion

#stich together with ffmpeg, slap the soundtrack back over the top of the city noises, baby you've got a compilation going
