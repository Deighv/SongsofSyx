from PyInput_KeyCodes import *
from helperFunctions import *

print("Quick, tab over to Syx!")
countdown = 2
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)
MoveIntoCorner()
MoveScreenUpxTimes(28,-112)
MoveScreenRightxTimes(1,0)