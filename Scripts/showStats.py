import shutil
import pydirectinput
from PyInput_KeyCodes import *
from os import walk
from pathlib import Path
timing=.1
#click on all the stat menus
pydirectinput.moveTo(50,50, 0) #takes 141 seconds
pydirectinput.click(duration=timing)
raceIconLocationsLeft = [(75,365),(75,548),(75,750),(75,932),(75,1120),(75,1302),(75,1690)]
fulFillmentRows = [(990,701),(990,845),(990,990),(990,1138),(990,1285),(990,1430),(990,1570)]
showStatsFor = 2
for value in raceIconLocationsLeft:
    print(value)
    pydirectinput.moveTo(value[0],value[1], 0)
    pydirectinput.moveTo(0,0,0) #reset mouse so popup panel goes away
    pydirectinput.click(duration=timing)
    for valuee in fulFillmentRows:
        pydirectinput.moveTo(valuee[0],valuee[1], 0)
        pydirectinput.moveTo(0,0,0) #reset mouse so popup panel goes away
        pydirectinput.click(duration=timing)
        time.sleep(showStatsFor)

pydirectinput.moveTo(3839,3839,0) #Back to our old friend the corner
pydirectinput.click(button='right',duration=timing) #hide panel
time.sleep(timing)
pydirectinput.click(button='right',duration=timing) #hide panel
time.sleep(timing)
