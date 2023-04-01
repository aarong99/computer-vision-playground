import cv2

# get image with path
img = cv2.imread('Porsche-Logo.png', 1)

# resize image by pixels
#img = cv2.resize(img, (400,400))

# resize image by scale
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# rotate image 
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# write new photo with current edits
#cv2.imwrite('new_img.jpg', img)

# display image wit label and image to display
cv2.imshow('Image', img)

# seconds of wait time for user to press key
cv2.waitKey(0)

# properly destroy running process
cv2.destroAllWindows()