import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

face_cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv.imread('harry.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(gray,1.3,4)
print(face)
for x,y,w,h in face:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows