import subprocess
import itertools
import datetime
import math
from os import walk
import ffmpeg
import numpy as np

fade_duration=1.0

folderWithRecordings = "C:\\Folderwithyourrecordingsandthisscript\\" #this is just the folder we're in really..
filenamesToStart = next(walk(folderWithRecordings), (None, None, []))[2]  
filenamesToStart = [fi for fi in filenamesToStart if fi.endswith(".mkv")] #just the videos
filenamesToStart = [fi for fi in filenamesToStart if not fi.startswith("output")] #not our outputs
#I did this in multiple runs so it'd be faster and kept compiling the larger clips down, you could just do all the clips in one go and send it
runInBatchesOf = int(22) #many Filters uses many RAMs, adjust this until you're using just under your max ram, varies with clip size
NumberOfClips =  len(filenamesToStart)
NumberOfRuns = math.floor(NumberOfClips/runInBatchesOf) 


print(NumberOfRuns)
index = 0
while index <= NumberOfRuns: #This can overflow and I know
    
    output_filename = "readypls.mkv" #name our output file
    
    fromThis = int((runInBatchesOf*index)) #The number file in the group we want to start at
    toThis = int(fromThis+runInBatchesOf) #The number file in the group we want to end at
    ourFiles = []
    for x in range(fromThis, toThis):
        print(filenamesToStart[x])
        ourFiles += [filenamesToStart[x]] 
        
    with open('render.log', 'a') as f:
        print(output_filename, file=f)
        print(ourFiles, file=f)
        print(datetime.datetime.now(), file=f)
        print("----------------------------------------------------", file=f)
    segments = ourFiles
    print(ourFiles)
    #thanks https://gist.github.com/royshil/369e175960718b5a03e40f279b131788
    
    # Get the lengths of the videos in seconds

    file_lengths = []
    for x in range(fromThis, toThis):
        file = folderWithRecordings+filenamesToStart[x]
        video_length = ffmpeg.probe(file)["format"]["duration"]
        #video_length = float(video_length)
        file_lengths += [video_length]
    print(file_lengths)
    file_lengths = list(np.float64(file_lengths))

    width = 3840
    height = 2160

    # File inputs from the list
    files_input = [['-i', f] for f in segments]

    # Prepare the filter graph
    video_fades = ""
    audio_fades = ""
    last_fade_output = "0:v"
    last_audio_output = "0:a"
    video_length = 0
    fade_duration = 1.0

    for i in range(len(segments) - 1):
        # Video graph: chain the xfade operator together
        video_length += file_lengths[i]
        next_fade_output = "v%d%d" % (i, i + 1)
        video_fades += "[%s][%d:v]xfade=duration=1.0:offset=%.3f[%s]; " % \
            (last_fade_output, i + 1, video_length - fade_duration*(i+1), next_fade_output)
        last_fade_output = next_fade_output

        # Audio graph:
        next_audio_output = "a%d%d" % (i, i + 1)
        audio_fades += "[%s][%d:a]acrossfade=d=1[%s]%s " % \
            (last_audio_output, i + 1, next_audio_output, ";" if (i+1) < len(segments)-1 else "")
        last_audio_output = next_audio_output

    # Assemble the FFMPEG command arguments
    ffmpeg_args = ['ffmpeg',
                *itertools.chain(*files_input),
                '-filter_complex', video_fades + audio_fades,
                '-map', '[%s]' % last_fade_output,
                '-map', '[%s]' % last_audio_output,
                '-y',
                output_filename]

    # Run FFMPEG
    print(" ".join(ffmpeg_args))
    subprocess.run(ffmpeg_args)
    #index +=1
    exit()
