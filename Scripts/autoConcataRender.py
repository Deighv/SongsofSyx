import datetime
import time
import shutil
import math
import decimal
from os import walk
import ffmpeg
import os

folderWithRecordings = "C:\\Rendering\\" #this is just the folder we're in really..
#start with zOutput.mkv as your first file, and have the rest named alphabetically, if they start going into z you'll have problems...
filenamesToStart = next(walk(folderWithRecordings), (None, None, []))[2]  
NumberOfClips =  len(filenamesToStart)
print(NumberOfClips)
NumberOfClips -= 1 #one of these is our starter zOutput.mkv
while NumberOfClips > 0:
    print(str(NumberOfClips) + " Clips to Compile!") 
    NumberOfClips -= 1
    print(datetime.datetime.now())
    filenames = next(walk(folderWithRecordings), (None, None, []))[2] 
    #Get list of file names
    if os.path.isfile("C:\\Rendering\\zOutput.mkv"):
        print("Found New Output!")
   
    #Get lowest file name (earliest clip that hasn't been moved out)
    nextClip = folderWithRecordings + filenames[0]
    print(filenames[0])
    rollingOutput ="zOutput.mkv"
    roDuration = math.floor(decimal.Decimal(ffmpeg.probe(rollingOutput)["format"]["duration"]))-2 #I think this runs out of video to fade sometimes?
    #roTrim = str(roDuration+2) #I don't believe this +2 it had... well, I believe it now
    #print("Trim Duration is " + str(roTrim))
    roDuration = str(roDuration) #lol ffmpeg..
    print("roDuration Duration is " + roDuration)
    print("Clip is up to" + roDuration + " something long")
    os.system("ffmpeg -i "+rollingOutput+" -i " +nextClip+ " -filter_complex ""xfade=offset=" +roDuration+ ":duration=2;acrossfade=duration=2"" zNewOutput.mkv")
    #ffmpeg -i 1.mp4 -i 2.mp4 -filter_complex "xfade=offset=4.5:duration=1;acrossfade=duration=1" output.mp4
    print(nextClip + " is the next clip")
    #os.system("ffmpeg -i "+rollingOutput+" -i " +nextClip+ " -filter_complex ""[0v][1v]xfade=transition=fade:duration=2:offset=" +roDuration+ "[video];[0:a]atrim=0:"+ roTrim +"[0A];[0A][1:a]acrossfade=d=2:c1=tri:c2=tri[audio]"" -map ""[video]"" -map ""[audio]"" zNewOutput.mkv")  

    print("Attempted Concat at " + str(datetime.datetime.now()))
    derp = 1
    while not os.path.isfile("C:\\Rendering\\zNewOutput.mkv"):
        time.sleep(7) #if that file isn't happening, hang the script
        derp +=1
        if derp > 5:
            quit()
        print("no zNewOutput.mkv found at " + str(datetime.datetime.now()))    
    print("Found New Output! at " + str(datetime.datetime.now()))
    os.remove("C:\\Rendering\\zOutput.mkv") #We have zNewOutput.mkv now!
    shutil.move(nextClip, "C:\\Rendered\\"+filenames[0])
    os.rename("C:\\Rendering\\zNewOutput.mkv", "C:\\Rendering\\zOutput.mkv")
    
    print(datetime.datetime.now())
#Pull In Next Lowest Video  - Check
#Get Length -Check
#Run ffmpeg Command on zOutput.mkv to zNewOutput.mkv - Check
##---Fix ffmpeg command
#Delete zOutput.mkv - Check
#Move Lowest Video into Processed Folder - Check
#Rename zNewOutput.mkv to zOutput.mkv - Check
#Goto 10
