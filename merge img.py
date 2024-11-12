import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('kunjippa.jpeg')
b, g, r = cv.split(img)

# Display individual channels
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

# Merge channels back
img2 = cv.merge([r, g, b])

# Display the merged image
cv.imshow('merge', img2)
plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()