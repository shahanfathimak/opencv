import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('kunjippa.jpeg')
cv.imshow('image',img)
print(img.shape)
width=img.shape[1]
height=img.shape[0]
scale=50
dim=(width,height)
print(width)

cv.waitKey(0)
cv.destroyAllWindows()