import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('kunjippa.jpeg')
cv.imshow('image',img)
img2 = cv.cvtColor(img,cv.color_BGR2GRAY)
cv.imshow('image',img2)

cv.waitKey(0)
cv.destroyAllWindows()