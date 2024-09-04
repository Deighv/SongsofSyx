import shutil
import pydirectinput
from PyInput_KeyCodes import *
from os import walk
from pathlib import Path
import datetime
timing = .1
print("Quick, tab over to Syx!")
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

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



HoldAndReleaseKey(TWO, timing) 
HoldAndReleaseKey(LEFT_BRACKET, timing) #start recording so we can see how long it takes to finish building
howlong = datetime.datetime.now() #how long does this take
print(howlong)
#Draw some hearts, this takes 17.78 seconds
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
#move to these, click, then adjust the x by +224px, do 4 more times
howlongnow = datetime.datetime.now()
print(str(howlongnow - howlong))
