import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(), (30,30), (370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

b_and=cv.bitwise_and(rectangle,circle)
cv.imshow("bitwise-and",b_and)

b_not=cv.bitwise_not(rectangle)
cv.imshow("bitwise-not",b_not)

b_or=cv.bitwise_or(rectangle,circle)
cv.imshow("bitwise-or",b_or)

b_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise-xor",b_xor)


cv.waitKey(0)