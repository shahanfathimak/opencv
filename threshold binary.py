import cv2
import matplotlib.pyplot as plt
img=cv2.imread('kunjippa.jpeg',0)
cv2.imshow('image',img)
ret,thresh2=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
ret,thresh3=cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
ret,thresh4=cv2.threshold(img,120,255,cv2.THRESH_TRUNC)
ret,thresh5=cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
ret,thresh6=cv2.threshold(img,120,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('THRESH BINARY',thresh2)
cv2.imshow('THRESH BINARY',thresh3)
cv2.imshow('THRESH BINARY',thresh4)
cv2.imshow('THRESH BINARY',thresh5)
cv2.imshow('THRESH BINARY',thresh6)

cv2.waitKey(3000)
#cv2.destroyAllWindows()
