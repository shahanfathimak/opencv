import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('kunjippa.jpeg')
pts=np.array([[[400,100]],[[100,400]],[[700,400]]], dtype=np.int32)
cv.polylines(img,[pts],True,(255,255,0),5)
cv.imshow('image',img)
img2=plt.imread('kunjippa.jpeg')
plt.imshow(img2)
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()