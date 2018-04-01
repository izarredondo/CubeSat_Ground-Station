# Program to record video and output video file
# Will reboot the system if no camera is detected
#
# Izabella Arredondo
# UTC Spring 2017


import picamera
import os
import subprocess
import time

# variable to hold number of files in video storage directory 
# incremented by 1 to avoid overwrites
fileCount = len(os.listdir('/home/pi/Desktop/PiCamVideos')) + 1


try:
        # initialize camera object 
        camera = picamera.PiCamera()
        
        # begin recording and save to PiCamVideos folder as a .h264 file 
        # with name of the number of total video files plus one 
        camera.start_recording('/home/pi/Desktop/PiCamVideos/%s.h264' % fileCount)
        # record for 290 seconds
        camera.wait_recording(290)
        # end recording
        camera.stop_recording()
        
# if no camera is detected        
except picamera.PiCameraError:
        print("Camera Not Detected")
        # sleep for 3 minutes
        time.sleep(180)
        # reboot system
        os.system("sudo reboot")
    
finally:
        # close camera resources to ensure file save 
	camera.close()
