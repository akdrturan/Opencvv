import numpy as np
import cv2

cap=cv2.VideoCapture("video1.mp4") ##gelecek goruntunun kaynagı
while True:

    ret, frame = cap.read()
    if ret==0:
        break
    frame=cv2.flip(frame,1)
    cv2.imshow("deneme1" , frame)

    if  cv2.waitKey(30) & 0xFF ==ord("q"): ##30 sanıyede kaç kare yakalayacagını belırtmektedır. 1000=1sn
        break
cap.release()
cv2.destroyAllWindows()   