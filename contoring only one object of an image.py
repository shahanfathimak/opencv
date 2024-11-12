import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('fruity.jpg')
cv.imshow('img',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('img2',gray)
ret,thresh=cv.threshold(gray,235,255,cv.THRESH_BINARY_INV)
cv.imshow('img3',thresh)
contour,_=cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img,contour,-1,(0,255,0),5)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows