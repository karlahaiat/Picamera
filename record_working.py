import picamera
import signal
import time
import os
import glob

filenums = []

def filename_list():
        global filenum #global so variable can be used outside of function
        if glob.glob('/home/pi/rec/*.h264'):   #find all h264 files in rec folder
                for filenames in glob.glob('/home/pi/rec/*.h264'):
                        filenames = filenames.strip('/home/pi/rec/')
                        filenames = filenames.replace('.h264', " ") #remove everything but the number
                        filenum = int(filenames) #get interger from video number
                        filenums.append(filenum)  #make interger the filenum
                filenum =  max(filenums)   #find the biggest number
                return filenum
        else:
                filenum = 0  #if no video exists set filenum to zero

#uncomment if you want to see if the camera runs before you start recording
#you need to use vcn right now to see stream...
#camera.start_preview(fullscreen=False, window=(100, 20, 640,480))


def sigusr_handler(signum,frame): #defining signal
	filename_list()
	if camera.recording:  #if camera is recording when signal is run, stop
		print('stop recording')
		camera.stop_recording()
	else:
		#uncomment if you want to see preview of screen when it starts recording
		#camera.start_preview(fullscreen=False, window=(100, 20, 640,480))
		for i in range(filenum + 1, 1000): 
			filename_list() #check what filenum we are at and add 1 if necessary
			camera.start_recording('/home/pi/rec/%d.h264' % i)
			print('Started recording %d.h264' % i)
			time.sleep(600) #record for 10 minutes
			print('Stopped recording %d.h264' % i) 
			camera.stop_recording() #stop recording so file is saved, and loop again to record another 10 minutes. The loop can run up to 1000 times unless it is paused

with picamera.PiCamera() as camera:
  #camera.resolution = (1280, 720)
  # Set a framerate of 1/6fps, then set shutter
  # speed to 6s and ISO to 800
  #camera.framerate = .066
  #camera.shutter_speed = .033
  #camera.exposure_mode = 'off'
  #camera.iso = 1600
  # Give the camera a good long time to measure AWB
  # (you may wish to use fixed AWB instead)
  #time.sleep(10)

	while True:
		try:
			sig = signal.signal(signal.SIGUSR1, sigusr_handler)
			if sig == 1: #if signal is detected, run the signal function
				sigusr_handler()
			else:  #if camera is recording stop
				if camera.recording:
					camera.stop_recording()
				else:
					time.sleep(1) #if camera isnt recording, wait for signal

		finally:
			if camera.recording:
				camera.stop_recording()

