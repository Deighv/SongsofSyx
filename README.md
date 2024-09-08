Feel free to use these saves and scripts in any way you see fit, I retain no rights or license.  If you'd like to credit me I'd be grateful! https://www.youtube.com/@deighv



## Scripts:

### autoCommit.ps1 -
This will backup every save into a git repo.  Think of the content possibilities when you can go back to every 15 minute increment of your base!  I have 2200 saves from Split River Plains, about 8-9gb in total. Somehow github was okay with this on a free account.  I did this by creating a repo in github, cloning it so the .git folder was in my songsofsyx\saves\saves folder, then running the powershell script inside that folder.  You'll have to log into github via browser so it can piggyback your credentials from there.  I feel like historically that used to be a huge pain but for some reason that's just working for me. Hopefully your mileage does not vary.

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

### drawHearts.py -
Run and tab into Syx (I just f5 from vscode), example of how to macro the UI and draw things even while the UI is hidden.

### showStats.py
Similar to above but running through Plebe stats.

### See Recording Scripts for Managing the Recording Outputs

Add me on Discord if you'd like a hand getting any of these things set up: deighv. (with the .)
