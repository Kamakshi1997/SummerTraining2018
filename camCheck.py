#!/usr/bin/python3 
import cv2
cam=cv2.VideoCapture(0)
if cam.isOpened():
	print("working")
else:
	ptint ("no")
