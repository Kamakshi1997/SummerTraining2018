#!/usr/bin/python3
import cv2
cam=cv2.VideoCapture(0)
while cam.isOpened():
	print("working...")
	status,frame=cam.read()
	newimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#x=cv2.imwrite("Desktop/cam2.jpeg",frame)
	#for i in range(100):
		#x.append(frame)
	cv2.imshow('cam0',frame)
	cv2.imshow('cam1',newimg)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
cam.release()

