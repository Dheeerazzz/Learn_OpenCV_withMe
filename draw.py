import cv2 as cv
import numpy as np


blank=np.zeros((500,500,3),dtype='uint8')  # to create a blank image
#cv.imshow('blank',blank)

#to change color of entire window
# blank[:]=0,0,255  #color to be applied
# cv.imshow('Green',blank)

#to change color of selected portion of window
# blank[200:300,300:400]=0,0,255  #color to be applied
# cv.imshow('Green',blank)
# cv.waitKey(0)

#to draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow('rect',blank)
cv.waitKey(0)