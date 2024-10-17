from PyInput_KeyCodes import *
from helperFunctions import *

print("Quick, tab over to Syx!")
countdown = 2
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

pydirectinput.moveTo(1080,20, 0) #move cursor up to time for sync
HoldAndReleaseKey2(LEFT_ALT, W, 35)
time.sleep(35)