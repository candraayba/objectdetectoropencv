import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_recording(time.strftime("%X") + '.avi')
    camera.wait_recording(3)
    camera.stop_recording()
