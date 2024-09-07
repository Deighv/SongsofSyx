import subprocess
import itertools
import datetime
import math
from os import walk, system
import ffmpeg
#So I'm dumb and scripted recording for 20 hours with all my audio channels turned on in OBS which is messing up the other script as its not expecting multiple audio channels
#and my other audio channels somehow don't have audio for the first few seconds lol
#supposedly -map -0:a shouldn't match the previously defined -0:a:1 but lol documentation 
#(or as implicated above and in other scripts, I am regarded)
#Adding this to the repo in case anyone else makes the same mistake, or I do twice.. which is more likely
#if you have multiple audio channels and you do need them, you can tweak the below to compress them into one (see ffmpeg map docs)
#or hit me up on discord and use your best boyfriend voice about it

folderWithRecordings = "C:\\CleanupClips\\" #Folder with your clips and this script
filenamesToStart = next(walk(folderWithRecordings), (None, None, []))[2]  
filenamesToStart = [fi for fi in filenamesToStart if fi.endswith(".mkv")] #just our videos (it runs through them alphabetically)
filenamesToStart = [fi for fi in filenamesToStart if not fi.startswith("clean_")] #Ignore the outputs in our folder
runInBatchesOf = int(1656) #no need to really do batches here I just lazily reused the same code and yeahhhh this took me about 6 hours...
NumberOfClips =  len(filenamesToStart)
NumberOfRuns = math.floor(NumberOfClips/runInBatchesOf)

print(NumberOfRuns)
index = 0
while index <= NumberOfRuns: #This can overflow and I know
    fromThis = int((runInBatchesOf*index)) #The number file in the group we want to start at
    toThis = int(fromThis+runInBatchesOf) #The number file in the group we want to end at
    ourFiles = []
  
    for x in range(fromThis, toThis):
        newName = "clean_" + filenamesToStart[x]
        system("ffmpeg -i " + filenamesToStart[x] +" -map 0:v:0 -map 0:a:1 -map -0:a:2 -map -0:a:3 -map -0:a:4 -map -0:a:5 -map -0:a:6 "+ newName + " -y")
    exit()
