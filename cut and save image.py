import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('kunjippa.jpeg')
b,g,r=cv.split(img)
cv.imshow('image',img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)
plt.imshow(img)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows 