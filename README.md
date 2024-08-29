Feel free to use these saves and scripts in any way you see fit, I retain no rights or license.  If you'd like to credit me I'd be grateful! https://www.youtube.com/@deighv

## Scripts:

### autoCommit.ps1 -
This will backup every save into a git repo.  Think of the content possibilities when you can go back to every 15 minute increment of your base!  I have 2200 saves from Split River Plains, about 8-9gb in total. Somehow github was okay with this on a free account.  I did this by creating a repo in github, cloning it so the .git folder was in my songsofsyx\saves\saves folder, then running the powershell script inside that folder.  You'll have to log into github via browser so it can piggyback your credentials from there.  I feel like historically that used to be a huge pain but for some reason that's just working for me. Hopefully your mileage does not vary.

To Do: Rename Saves with Date + Add More Info to them. Add More info to commit message

### create-autoCommit.exe.ps1
Creates an executable for autoCommit if you want to run it on startup/that's easier for you- run it in your songsofsyx\saves\saves folder.

### autoRecord.py -
Relies on PyInput_KeyCodes.py
Work in progress, but:

Run this script, tab over to Syx, it will:

Set your camera to a corner with a consistent zoom, then move your camera to a consistent set location of your choosing, with some tweaking, begin recording for a set amount of time, then stop recording.  Assuming we have the same shortcuts configured.  Note, Syx is picky when it comes to the keys it's okay with being macrod

So far the final camera frame is down to a couple pixels for consistency, I believe this is due to what frames the final move commands start and end on. Could probably fix with stabilization in post but this is already going to be hilarious to record+process.  Pull requests are open :)

Consider setting a hotspot day 1.
