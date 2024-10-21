To download a save, either clone the repository or click on a save and hit 'view raw', and move the contents to your save folder

Feel free to use these saves and scripts in any way you see fit, I retain no rights or license.  If you'd like to credit me I'd be grateful! https://www.youtube.com/@deighv



## Scripts:

### autoCommit.ps1 -
This will backup every save into a git repo.  I did this by creating a repo in github, cloning it so the .git folder was in my songsofsyx\saves\saves folder, then running the powershell script inside that folder.  You'll have to log into github via browser so it can piggyback your credentials from there.  I feel like historically that used to be a huge pain but for some reason that's just working for me. Hopefully your mileage does not vary.

To Do: Rename Saves with Date + Add More Info to them. Add More info to commit message

### create-autoCommit.exe.ps1
Creates an executable for autoCommit if you want to run it on startup/that's easier for you- run it in your songsofsyx\saves\saves folder.

### autoRecord.py -
Relies on PyInput_KeyCodes.py

Run this script, tab over to Syx, it will:

Load the alphabetically lowest save from a folder.  
Sets your Camera to a consistent location by panning to the corner
Use the minimap to hone into a location (set your pixel values accordingly),
Then you can perform any number of actions
  Hide the UI
  Record
  Move the Camera along set paths
  Click on UI Elements
  Script out building, etc
  Stop Recording
After the script will pull in the next lowest save, and repeat the process.

### stitchCinematic.py

This uses similar functionality to autoRecord, but cleaned up.  Many functions have been moved to helperFunctions.py
Great naming, I know.

This script will:
Reload the same save 25 times, each time going to the same start point, then panning out to record 25 separate scenes- 5 scenes wide by 5 scenes tall

At the end of the script are a series of ffmpeg commands to stitch together those scenes to create one cohesive video

Then, since nothing can play a video with that resolution- although someone *please* try to upload that to Youtube and see what blows up

There is another ffmpeg script to drop it to 8k  

	If you want to change the start corner from where it records, modify lines 33 and 34
	The methods there take -Number of Times To Move the Pixels to Move, Number of Pixels to Move
	If you go beyond the Number of Pixels to Move I use for either, you'll likely have problems due to camera smoothness, acceleration, something, built into the game, making positioning inconsistent

This script assumes you're running Syx base resolution of 2130x1232
I installed that resolution into my monitor using the Nvidia Control Panel so I could use it fullscreen.  I hear this can damage your monitor.  

Barring that, you can change the hard coded values with some math, or code it out- if a hardcoded x pixel value is 1930, divide that by the max 2190, multiply by your screen width (ie 1920) and round up/down, you'll have a good approximate.  Will need to be done for every hardcoded x and y pixel value.

### drawHearts.py -
Run and tab into Syx (I just f5 from vscode), example of how to macro the UI and draw things even while the UI is hidden.

### showStats.py
Similar to above but running through Plebe stats.

### See Recording Scripts for Managing the Recording Outputs

Add me on Discord if you'd like a hand getting any of these things set up: deighv. (with the .)
