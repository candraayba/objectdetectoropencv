import time

# Install numpy & openCv (http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/)
import numpy as np
import cv2

# Start Camera
cap = cv2.VideoCapture(0)

# Define Frame and output name
out = cv2.VideoWriter("Video " + time.strftime("%X") + ".avi", -1, 20.0, (640,480))


else:
    print 'Undetected Camera'

# Recording
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
    if cv2.waitKey(1) & 0xFF == ord('p'):
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        out.release()
else:
    print 'Undetected Camera'
    break

# Release Camera
cap.release()

# Release output 
out.release()

# Destroy Window
cv2.destroyAllWindows()
