import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('kunjippa.jpeg')
cv.putText(img,'learn open cv python',(100,100),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
cv.imshow('image',img)
        
img2=plt.imread('kunjippa.jpeg')
plt.imshow(img2)
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()