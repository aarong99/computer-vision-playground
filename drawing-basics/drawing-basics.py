import numpy as np
import cv2

# access camera resource
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #return frame (image) and return false if capture not executed properly
    width = int(cap.get(3)) #get width property of capture
    height = int(cap.get(4))#get heigh property of capture

    # draw a line
    img = cv2.line(frame, )

    # display frame
    cv2.imshow('Frame', image)

    # quit with 'q' ascii value input
    if cv2.waitKey(1) == ord('q'):
        break

# release camera resource
cap.release()
cv2.destroyAllWindows()