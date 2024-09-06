import subprocess
import itertools
import datetime
import math
from os import walk
import ffmpeg
#This assumes all your clips are the same fps, resolution, etc
#I need speed more than flexibility
folderWithRecordings = "C:\\WorkInProgress\\" #Folder with your clips and this script
filenamesToStart = next(walk(folderWithRecordings), (None, None, []))[2]  
filenamesToStart = [fi for fi in filenamesToStart if fi.endswith(".mkv")] #just our videos (it runs through them alphabetically)
filenamesToStart = [fi for fi in filenamesToStart if not fi.startswith("output")] #Ignore the outputs in our folder
#I did this in multiple runs so it'd be faster and I kept compiling the larger clips down (and changing the output name/above output), you could just do all the clips in one go and send it
#But there is a parameter limit of 255~
runInBatchesOf = int(30) #many Filters uses many RAMs, adjust this until you're using just under your max ram, varies with clip size
NumberOfClips =  len(filenamesToStart)
NumberOfRuns = math.floor(NumberOfClips/runInBatchesOf) #If you are doing batches you'll be happy if this is a round number, otherwise you'll have to up your index and override your toThis number

print(NumberOfRuns)
index = 0
while index <= NumberOfRuns: #This can overflow and I know
    
    output_filename = "output.mkv" #name our output file, if you're doing this in batches you'll want to drop a timestamp in here
    
    fromThis = int((runInBatchesOf*index)) #The number file in the group we want to start at
    toThis = int(fromThis+runInBatchesOf) #The number file in the group we want to end at
    ourFiles = []
    for x in range(fromThis, toThis):
        print(filenamesToStart[x])
        ourFiles += [filenamesToStart[x]] 
    #so we know what files went into what render    
    with open('render.log', 'a') as f:
        print(output_filename, file=f)
        print(ourFiles, file=f)
        print(datetime.datetime.now(), file=f)
        print("----------------------------------------------------", file=f)
    segments = ourFiles
    print(ourFiles)
    
    
    # Get the lengths of the videos in seconds
    file_lengths = []
    for x in range(fromThis, toThis):  #good old slow, easy to debug for loops
        file = folderWithRecordings+filenamesToStart[x]
        internal_videoLength = ffmpeg.probe(file)["format"]["duration"]
        internal_videoLength = float(internal_videoLength)
        file_lengths += [internal_videoLength]
    print("file lengths:")
    print(file_lengths)
    # File inputs from the list
    files_input = [['-i', f] for f in segments]

    #thanks https://gist.github.com/royshil/369e175960718b5a03e40f279b131788
    #There are bugs in the OP
    #but thanks to everyone's hard work combined, here we are!
    
    # Prepare the filter graph
    video_fades = ""
    audio_fades = ""
    last_fade_output = "0:v"
    last_audio_output = "0:a"
    video_length = 0
    fade_duration = 1.0
    
    for i in range(len(segments) -1):
        #Video Graph
        video_length += file_lengths[i]
        video_length = video_length - fade_duration #subract our fade distance each round
        next_fade_output = "v%d%d" % (i, i + 1)
        video_fades += "[%s][%d:v]xfade=duration=1.0:offset=%.3f[%s]; " % \
            (last_fade_output, i + 1, video_length , next_fade_output)
        last_fade_output = next_fade_output

        #Audio Graph
        next_audio_output = "a%d%d" % (i, i + 1)
        audio_fades += "[%s][%d:a]acrossfade=d=1[%s]%s " % \
            (last_audio_output, i + 1, next_audio_output, ";" if (i+1) < len(segments)-1 else "")
        last_audio_output = next_audio_output
        
        """ next_audio_output = "a%d%d" % (i, i)
        audio_fades += f"[{last_audio_output}][{i}:a]acrossfade=d=%d[{next_audio_output}];" % (fade_duration)
        last_audio_output = next_audio_output """        

    # Assemble the FFMPEG command arguments
    ffmpeg_args = ['ffmpeg', #Linux peeps ['/usr/local/bin/ffmpeg'
                *itertools.chain(*files_input),
                '-filter_complex', video_fades + audio_fades,
                '-map', '[%s]' % last_fade_output,
                '-map', '[%s]' % last_audio_output,
                '-y',
                output_filename]
    #Save our command to our log
    with open('render.log', 'a') as f:
        print(datetime.datetime.now(), file=f)
        print(" ".join(ffmpeg_args), file=f)
    print(" ".join(ffmpeg_args))
    #exit() #check out the ffmpeg command
    #Run ffmpeg, prepare for takeoff
    subprocess.run(ffmpeg_args) 
    #index +=1 #uncomment for running in batches or it won't loop
    exit() #comment this or it definitely won't loop
