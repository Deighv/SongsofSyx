from PyInput_KeyCodes import *
from helperFunctions import *

print("Quick, tab over to Syx!")
countdown = 2
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

HoldAndReleaseKey2(LEFT_ALT, W, 15)
time.sleep(15)