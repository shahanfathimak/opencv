import cv2
import matplotlib.pyplot as plt
img=cv2.imread('kunjippa.jpeg',0)
cv2.imshow('image',img)
ret,thresh2=cv2.threshold(img,120,255,THRESH_BINARY)
cv2.imshow('THRESH BINARY',thresh2)

cv2.waitKey(3000)
cv2.destroyAllWindows()
