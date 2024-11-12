import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('kunjippa.jpeg')
image=img[60:160,160:300]
cv.imshow('image',image)
plt.imshow(img)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows 