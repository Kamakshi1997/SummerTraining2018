#!usr/bin/python3
import numpy as np
import cv2
x=cv2.imread("Desktop/index.jpeg",1)
y=x[10:50,30:80]
x[60:100,40:90]=y
cv2.imshow("hello",x)
cv2.waitKey(0)
cv2.destroyAllWindows()
