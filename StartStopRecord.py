import numpy as np
import cv2
import time

# Start Camera
cap = cv2.VideoCapture(0)

# Define Frame and output name
out = cv2.VideoWriter("Video " + time.strftime("%X") + ".avi", -1, 20.0, (640,480))

# Recording
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release Camera
cap.release()

# Release output 
out.release()

# Destroy Window
cv2.destroyAllWindows()
