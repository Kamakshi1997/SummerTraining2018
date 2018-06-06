#!/usr/bin/pyhton3
import cv2
#starting with camera
cap=cv2.VideoCapture(0)
#saving height and width of current camera
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#  deciding video format              XVID for .avi format video
video_format=cv2.VideoWriter_fourcc(*'XVID')
#  saving video data as per format 
#                filename , video format , FPS , video w , h 
video_output=cv2.VideoWriter('adhoc.avi',video_format,50.0,(int(width),int(height)))
while cap.isOpened():
	status,frame=cap.read()
	cv2.imshow('live_frame',frame)
	video_output.write(frame)

	if cv2.waitKey(1) &  0xFF  ==  ord('q'):
		break


cv2.destroyAllWindows()
cap.release()





