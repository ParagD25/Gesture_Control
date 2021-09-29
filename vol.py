import time
import numpy as np
import cv2

capture=cv2.VideoCapture(0)

while True:
    
    success,img=capture.read()
    cv2.imshow('Gesture',img)
    cv2.waitKey(1)
