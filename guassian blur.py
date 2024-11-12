import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('fruits.jpg')
ksize=(8,8)
blur=cv.blur(img,ksize)
cv.imshow('img',img)
cv.imshow('img2',blur)

cv.waitKey(0)
cv.destroyAllWindows
