import cv2
import numpy as np
img=np.zeros((20,20,3),np.uint8) +255  ##+255 arka renk planı, 20,20 pencerenın buyuklugu, 3 renk 

img[0,1]=(0,0,0)
img[0,2]=(0,50,0)
img[0,3]=(0,100,0)
img[0,4]=(0,150,0)
img[9,5]=(0,200,0)
img[0,6]=(0,250,200)

img=cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)## yukardan alınan kucuk pencereyı dahada buyuttu !!
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroy.AllWindows()