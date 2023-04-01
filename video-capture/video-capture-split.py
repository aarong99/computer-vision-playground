import numpy as np
import cv2

# access camera resource
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #return frame (image) and return false if capture not executed properly
    width = int(cap.get(3)) #get width property of capture
    height = int(cap.get(4))#get heigh property of capture

    # create new black canvas of same shape
    image = np.zeros(frame.shape, np.uint8)

    # get half scale frame
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # paste smaller frame in top left corner of new canvas
    image[:height//2, :width//2] = smaller_frame
    # and bottom left 
    image[height//2:, :width//2] = smaller_frame
    # and top right
    image[:height//2, width//2:] = smaller_frame
    # and bottom right
    image[height//2:, width//2:] = smaller_frame

    # display frame
    cv2.imshow('Frame', image)

    # quit with 'q' ascii value input
    if cv2.waitKey(1) == ord('q'):
        break

# release camera resource
cap.release()
cv2.destroyAllWindows()