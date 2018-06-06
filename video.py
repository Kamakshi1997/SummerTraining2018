#!/usr/bin/pyhton3
import cv2
#starting with camera
cap=cv2.VideoCapture(0)
#checking height and width of current camera
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.release()



