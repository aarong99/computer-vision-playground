import cv2
import random 

# get image with path
img = cv2.imread('Porsche-Logo.png', 1)

# print image representation
#print(img)

# print image data type (numpy array)
#print(type(img))

# loop through image array rows and cols and change pixels to random colors
#for i in range(100): #first 100 rows
#    for j in range(img.shape[1]): #range of columns
#        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# copy part of image
tag = img[1500:2000, 700:1400] #copy rows 500 to 700 with columns 600 to 900

# paste into part of image (must be same dimensions)
img[100:600, 500:1200] = tag

# display image wit label and image to display
cv2.imshow('Image', img)

# seconds of wait time for user to press key
cv2.waitKey(0)

# properly destroy running process
cv2.destroAllWindows()