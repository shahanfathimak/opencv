import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('kunjippa.jpeg')
pts=np.array=[[[[100,400]],[[200,100]],[[300,400]],[[400,100]]],dtype=np.int32]
cv.polylines(img,[pts],false,(255,0,0),5)
cv.imshow('image',img)
img2=plt.imread('kunjippa.jpeg')
plt.imshow(img2)
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()