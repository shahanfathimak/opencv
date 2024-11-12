import cv2
import matplotlib.pyplot as plt
img=cv2.imread('kunjippa.jpeg',0)
cv2.imshow('image',img)
hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

cv2.waitKey(3000)
cv2.destroyAllWindows()
