# Picamera

1. pause_save.py for video feed without time splitting

2. record_working.py code that splits the video every 10 minutes and saves all videos to a folder named rec

3. transform.py converts the videos in the rec folder. You can change this by going in the code if you want the location the videos are taken from to change. 

The code is mostly detailed in comments, but let me know if you don’t understand something. 

With the new splitting code, I have changed a couple other things in the Pi. I changed the aliases on the pi. To access the aliases go to $sudo nano .bashrc and scroll to the bottom. To update any changes done to .bashrc, reboot the pi or type $ source .bashrc.

Aliases:

start= start the record_working script. This will not record anything, just start the script and window to see if the camera is running. To start recording you have to send a signal:

toggle= this replaces the pause command. It just sends a signal to toggle between recording and pausing. You must run toggle after start to start recording on the script with split videos. After you recover the camera, run the toggle command to pause the video. The last video should get saved up to the point at which it was recorded, it does not need to run the full 10 minutes.

record= this alias runs the pause_save.py script. The video will start recording when this is opened. To toggle between pause and record, just type toggle. 

convert= converts the .h264 video files to mp4, located in the rec directory. You can change the code to change location. If you want maybe I will write a script for converting in the pi directory, if you plan on using the pause_save.py script at some point.

