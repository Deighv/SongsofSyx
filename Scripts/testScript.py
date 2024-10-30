from PyInput_KeyCodes import *
from helperFunctions import *

print("Quick, tab over to Syx!")
countdown = 4
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

HideUI()
MoveScreenUpxTimes(28,-176) 