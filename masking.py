import cv2 as cv
import numpy as np

img=cv.imread('dog.jpg')
blank=np.zeros(img.shape[:2],dtype='uint8')
mask=cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(2000,2000),255,-1)
cv.imshow("mask",mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked image",masked)



cv.waitKey(0)