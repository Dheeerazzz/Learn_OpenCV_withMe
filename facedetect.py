import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('linkedin.jpeg')
# plt.imshow('img')
# cv.imshow("pspk",img)
# cv.resize(img,(1000,1000),interpolation=cv.INTER_AREA)
# cv.waitKey(0)
print(img.shape)
#plt.imshow(img)
a=cv.resize(img,(500,600))
cv.imshow("pspk",a)
gray=cv.cvtColor(a,cv.COLOR_BGR2GRAY)
cv.imshow("pspk",gray)

haar_cascade=cv.CascadeClassifier('haar_faces.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3 )
print(len(faces_rect))

for i in faces_rect:
    x,y,w,h=[index for index in i]
    cv.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('detected faces',gray)
cv.waitKey(0)