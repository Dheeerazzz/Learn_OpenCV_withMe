import cv2 as cv
img=cv.imread('dog.jpg')
#cv.imshow('dog',img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)  #1 always refer to width and 0 refers height
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

rescaleFrame(img)
cv.imshow('dog',img)

cv.waitKey(0)