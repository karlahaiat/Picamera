import time
import os
import subprocess
from subprocess import call

filenum = 1

os.chdir('/home/pi/rec/')
#if mp4 file already exists. don't do anything
for i in range(filenum, len(os.listdir('/home/pi/rec/'))):
	if os.path.exists('%d.mp4' % i):
		time.sleep(1)
		print('%d.mp4 already exists' % filenum)
		filenum= i + 1

	#if mp4 for the video file doesn't exist, convert to mp4
	else:
		for j in range(filenum, len(os.listdir('/home/pi/rec/'))):
        		if os.path.exists('%d.h264' % j):
                		input= "/home/pi/rec/{}.h264" .format(filenum)
				output="/home/pi/rec/{}.mp4" .format(filenum)
				print('converting %d.h264' % filenum)
				conv=call(["MP4Box", "-add", input, output])
				if conv != 0:
					print('Could not convert file %d.h264' % filenum)
				else:
					print('%d.h264 has been converted' % filenum)
				filenum = j + 1

				#if next file exists, break out of conversion loop
				if os.path.exists('%d.mp4' % j):
                			break

				
