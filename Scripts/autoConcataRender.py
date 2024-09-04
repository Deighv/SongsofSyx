import argparse
import subprocess
import itertools
import datetime
import time
import shutil
import math
import decimal
from os import walk
import ffmpeg
import os

Fade_Rectifier=1

folderWithRecordings = "C:\\RecordingsSendIt\\" #this is just the folder we're in really..
filenamesToStart = next(walk(folderWithRecordings), (None, None, []))[2]  
filenamesToStart = [fi for fi in filenamesToStart if fi.endswith(".mkv")] #just the videos
filenamesToStart = [fi for fi in filenamesToStart if not fi.startswith("output")] #not our outputs
runInBatchesOf = int(15) #many Filters uses many RAMs, lowered this until CPU was maxed (just below peak ram use)
NumberOfClips =  len(filenamesToStart)
NumberOfRuns = math.floor(NumberOfClips/runInBatchesOf)+1


print(NumberOfRuns)
index = -1
while index <= NumberOfRuns: 
    index +=1 
    
    output_filename = "output"+str(index)+".mkv" #name our output file
    
    fromThis = int(0+(runInBatchesOf*index)) #The number file in the group we want to start at
    toThis = int(runInBatchesOf+(runInBatchesOf*index)) #The number file in the group we want to end at
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
    
    # Get the lengths of the videos in seconds
    file_lengths = [
        float(ffmpeg.probe(f)["format"]["duration"])
        for f in segments
    ]

    width = 3840
    height = 2160

    # File inputs from the list
    files_input = [['-i', f] for f in segments]

    # Prepare the filter graph
    video_fades = ""
    audio_fades = ""
    last_fade_output = "0v"
    last_audio_output = "0:a"
    video_length = 0
    normalizer = ""
    scaler_default = f",scale=w={width}:h={height}:force_original_aspect_ratio=1,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2"

    for i in range(len(segments)):
        """     # Videos normalizer
        scaler = scaler_default if i > 0 else ""
        normalizer += f"[{i}:v]settb=AVTB,setsar=sar=1,fps=60{scaler}[{i}v];" """

        if i == 0:
            continue

        #Video graph: chain the xfade operator together
        video_length += file_lengths[i - 1] - Fade_Rectifier
        next_fade_output = "v%d%d" % (i - 1, i)
        video_fades += "[%s][%dv]xfade=duration=%d:offset=%.5f[%s];" % (last_fade_output, i, Fade_Rectifier, video_length, next_fade_output)
        last_fade_output = next_fade_output #the .5 above is the video timing

        #Audio graph:
        next_audio_output = "a%d%d" % (i - 1, i)
        audio_fades += f"[{last_audio_output}][{i}:a]acrossfade=d=%d[{next_audio_output}];" % (Fade_Rectifier)
        last_audio_output = next_audio_output

    video_fades += f"[{last_fade_output}]format=pix_fmts=yuv420p[final];"

    # Assemble the FFMPEG command arguments
    ffmpeg_args = ['ffmpeg',
                *itertools.chain(*files_input),
                '-filter_complex', normalizer + video_fades + audio_fades[:-1], #this is the audio timing
                '-map', '[final]',
                '-map', f"[{last_audio_output}]",
                '-y',
                output_filename]

    print(" ".join(ffmpeg_args))
    # Run FFMPEG
    subprocess.run(ffmpeg_args)
