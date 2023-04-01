import numpy as np
import cv2

# access camera resource
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #return frame (image) and return false if capture not executed properly

    # display frame
    cv2.imshow('Frame', frame)

    # quit with 'q' ascii value input
    if cv2.waitKey(1) == ord('q'):
        break

# release camera resource
cap.release()
cv2.destroyAllWindows()