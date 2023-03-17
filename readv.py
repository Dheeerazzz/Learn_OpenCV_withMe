#to read a video
import cv2 as cv

capture=cv.VideoCapture('thalapathy.mp4')
while True:
        isTrue,frame=capture.read()
        cv.imshow('video',frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

capture.release()
cv.destroyAllWindows()
