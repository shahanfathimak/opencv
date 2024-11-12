import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print('Cannot connect to the camera.')
        break
    cv.imshow('Video', frame)
    gray=cv.cvtcolor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('Video',gray)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()