
import shutil
import pydirectinput
import vlc
from PyInput_KeyCodes import *
from os import walk
from pathlib import Path

timing = .1
print("Quick, tab over to Syx!")
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

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
pydirectinput.click(duration=timing)
time.sleep(timing)
pydirectinput.moveTo(3835, 105, 0) #hone in
pydirectinput.click(duration=timing)
time.sleep(timing)
pydirectinput.moveTo(3665, 227, 0) #hone i n
pydirectinput.click(duration=timing)
time.sleep(timing)


#Loaded, Camera in position, Game Stopped, UI Present

#region Start Recording, Start Game, wait, stop recording
print("It's Recording Time!")
HoldAndReleaseKey(TWO, timing) #speed
time.sleep(timing)
print("Hide UI")
pydirectinput.moveTo(3600, 344, 0)
pydirectinput.click(duration=timing)
time.sleep(.2)


HoldAndReleaseKey(LEFT_BRACKET, timing) #Record if your record button is [
print("Started Recording")
#6.35758 minutes pass in game per second irl at "5x" (the one that you'd think is 2x by the arrows)
#timing is over so that reveal happens at
print("Waiting for the year 1250")
#how long to wait for the clock strike, minus all our stuff that needs to happen first.. so much timing..
#thanks self-induced scope creep :D
TimeFromStartTo1250 = 1543
#this lands at 22:58 at 1519, need to wait 59 more minutes in game - 9 seconds
#welp, I want half second increments... (that we wound up not using)
#alright, we're going long enough that the time is a moving target
#we need to get lucky
while TimeFromStartTo1250 > 0:
    TimeFromStartTo1250 -= .5
    if TimeFromStartTo1250%10 == 0:
        print(str(TimeFromStartTo1250) + " seconds remaining")
    time.sleep(.5)

#Play One more Round
media = vlc.MediaPlayer("C:\\Recordings\\2024-09-01_21-43-27.mkv")
#I hope this is legit, it is a song from the game :|
media.play()
#Draw some hearts, this takes 17.78 seconds, we're rounding to 18
pydirectinput.click(button='right',duration=timing) #show UI briefly to click
pydirectinput.moveTo(2042, 2125, 0) #build tool
pydirectinput.click(duration=timing)
pydirectinput.moveTo(1941, 1809, 0) #roads
pydirectinput.click(duration=timing)
pydirectinput.moveTo(1715, 192, 0) #roads
pydirectinput.click(duration=timing)
print("Hide UI")
pydirectinput.moveTo(3600, 344, 0)
pydirectinput.click(duration=timing)
clickLocations = [(1537, 593),(1566, 563),(1593, 537),(1622, 508),(1646, 507),(1677, 507),(1706, 536),(1706, 564),(1678, 593),(1706, 621),(1706, 649),(1678, 675),(1649, 676),(1622, 675),(1593, 648),(1565, 620)]
drawTimes = 0
while drawTimes < 5:
    for value in clickLocations:
        print(value)
        pydirectinput.moveTo(value[0]+(drawTimes*224),value[1], 0)
        time.sleep(.01)
        pydirectinput.click(duration=timing)
    drawTimes += 1
#Let this cook for 105 seconds ##only takes 70 seconds now..
#lets move 15 seconds
time.sleep(90)

#move mouse up to calendar to show rollover
pydirectinput.moveTo(1920, 52, 0)
pydirectinput.click(button='right',duration=timing) #return UI
#Super Slow Mo
HoldAndReleaseKey(SPACE, timing) #speed
HoldAndReleaseKey(SPACE, timing) #speed super slow mo
#ROLLOVER WOO --this is when the thing actually shows
time.sleep(20)  #lasts about ~7 minutes at super slowmo

HoldAndReleaseKey(SPACE, timing) #speed up
time.sleep(1)#speed up slow
HoldAndReleaseKey(TWO, timing) #speed
time.sleep(46) #remainder of song but some extra
HoldAndReleaseKey(LEFT_BRACKET, timing) #stop recording
print("WE DID IT!")
time.sleep(1) #Give OBS ONE second
HoldAndReleaseKey(Z, timing) #stop game
#endregion 
