#code for testing and continuous recording
import picamera
import signal
import time
import os

with picamera.PiCamera() as camera:
	filenum = 0
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
	for i in range(filenum, len(os.listdir('/home/pi/'))):
		if os.path.exists('%d.h264' % i):
			filenum = i + 1

	camera.start_preview(fullscreen=False, window=(600,90,640,680))
	#camera.start_preview()
	camera.start_recording('%d.h264' %filenum)

	def sigusr_handler(signum, frame):
		global filenum
		if camera.recording:
			print('Stopped Recording')
			camera.stop_recording()
		else:
			filenum += 1
			camera.start_recording('%d.h264' % filenum)
			print('Started recording to %d.h264' % filenum)

	try:
		signal.signal(signal.SIGUSR1, sigusr_handler)
		# Do nothing while we wait for the signal handler to be called
		while True:
			time.sleep(1)
	finally:
		if camera.recording:
			camera.stop_recording()

