#!/usr/bin/python3
import cv2
import numpy as np
img=cv2.imread('Desktop/index.jpeg',1)
#drawing objects on an image
cv2.line(img,(0,0),(300,524),(0,0,255),2)
cv2.rectangle(img,(150,60),(250,80),(0,255,0),3)
cv2.circle(img,(146,60),50,(255,0,0),-1)
#cv2.imwrite('Desktop/index1.jpeg',img)
cv2.imshow('wname',img)
#Concatenating two images in a single window (along x axis=0, along y axis=1
newimg1=img[10:100,0:308]
newimg2=img[0:164,0:308]
vis = np.concatenate((newimg1,newimg2), axis=0)
print img.shape
#cv2.imshow('wname',newimg1)
cv2.imshow('wname2',vis)
cv2.waitKey(0)
cv2.destroyAllwindows()

