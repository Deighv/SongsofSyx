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
    if os.path.isfile(folderWithRecordings+"zOutput.mkv"):
        print("Found New Output!")
    else:
        quit()   
    #Get lowest file name (earliest clip that hasn't been moved out)
    nextClip = folderWithRecordings + filenames[0]
    print(filenames[0])
    rollingOutput ="zOutput.mkv"
    roDuration = float(ffmpeg.probe(rollingOutput)["format"]["duration"])-1.5 #I think this runs out of video to fade without the -1.5
    #roTrim = str(roDuration+2) #I don't believe this +2 it had... well, I believe it now
    roDuration = str(roDuration) #lol ffmpeg..
    print("ffmpeg -i "+rollingOutput+" -i " +nextClip+ " -filter_complex ""xfade=offset=" +roDuration+ ":duration=1.5;acrossfade=duration=1.5"" zNewOutput.mkv")
    os.system("ffmpeg -i "+rollingOutput+" -i " +nextClip+ " -filter_complex ""xfade=offset=" +roDuration+ ":duration=1.5;acrossfade=duration=1.5"" zNewOutput.mkv")
    #os.system("ffmpeg -i "+rollingOutput+" -i " +nextClip+ " -filter_complex ""[0v][1v]xfade=transition=fade:duration=2:offset=" +roDuration+ "[video];[0:a]atrim=0:"+ roTrim +"[0A];[0A][1:a]acrossfade=d=2:c1=tri:c2=tri[audio]"" -map ""[video]"" -map ""[audio]"" zNewOutput.mkv")  
    print("Attempted Concat at " + str(datetime.datetime.now()))
    derp = 0
    while not os.path.isfile(folderWithRecordings+"zNewOutput.mkv"):
        time.sleep(1) #if that file isn't happening, hang the script
        derp +=1
        if derp > 10:       
            print("no zNewOutput.mkv found at " + str(datetime.datetime.now()))    
            quit()
    print("Found New Output! at " + str(datetime.datetime.now()))
    os.remove(folderWithRecordings+"zOutput.mkv") #We have zNewOutput.mkv now!
    shutil.move(nextClip, "C:\\Rendered\\"+filenames[0]) #move our old files aside
    os.rename(folderWithRecordings+"zNewOutput.mkv", folderWithRecordings+"zOutput.mkv")
    print(datetime.datetime.now())
