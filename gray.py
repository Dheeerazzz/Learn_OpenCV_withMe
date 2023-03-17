import cv2 as cv
img=cv.imread('dog.jpg')
cv.imshow("color-dog",img)

#converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("grayscale-dog",gray)

cv.waitKey(0)

#blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blurred-dog",blur)
cv.waitKey(0)

#bgr to hsv
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv-dog",hsv)
cv.waitKey(0)


