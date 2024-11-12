import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('kunjippa.jpeg')
cv.imshow('image',img)
print(img.shape)
scale=50
width=int(img.shape[1]*scale/100)
height=img.shape[0]
dim=(width,height)
print(width)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()