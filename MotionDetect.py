#!usr/bin/python3
import cv2
#starting webcam
cap=cv2.VideoCapture(0)
#checking webCam and performing task
while cap.isOpened():
	status,frame=cap.read()
	#True/False,img Frame

	#detecting only blue
	only_blue=cv2.inRange(frame,(40,0,0),(255,20,20))
	cv2.imshow('blue',only_blue)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cv2.destroyAllWindows()
cap.release()

   
