import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('kunjippa.jpeg')
cv.imshow('image',img)
print(img.shape)
scale=180
width=int(img.shape[1]*scale/100)
height=int(img.shape[0]*scale/100)
dim=(width,height)
res=cv.resize(img,dim,interpolation=cv.INTER_AREA)
cv.imshow('image1',res)

cv.waitKey(0)
cv.destroyAllWindows()