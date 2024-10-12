import cv2
import numpy as np

canvas=np.zeros((300,500,3), np.uint8) +255

cv2.putText(canvas,"deneme1",(100,100),cv2.FONT_ITALIC,2,(100,50,75),cv2.LINE_AA)
cv2.imshow("pencere", canvas)


cv2.waitKey(0)
cv2.destroyAllWindows()