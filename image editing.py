import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('kunjippa.jpeg')
#img[60:160,100:300]=255
#cv.imshow('image',img)
plt.imshow(img)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows 