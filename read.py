import cv2 as cv
img=cv.imread('dog.jpg')   #stores image into 'img' as pixels
cv.imshow('dog2',img)    #displays image in a new window
cv.waitKey(0)   #to make the window wait until user closesit by himself