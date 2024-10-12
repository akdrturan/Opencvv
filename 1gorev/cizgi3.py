import cv2
import numpy as np

canvas=np.ones((500,500,3),np.uint8) +255 ##ones ve zeros arka plan rengı

cv2.line(canvas,(100,200),(300,350),(0,0,255),6)

cv2.rectangle(canvas,(200,250),(65,450),(25,85,59),6)

cv2.circle(canvas,(400,250),65,(250,0,0),6)
cv2.imshow("cizgi",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()