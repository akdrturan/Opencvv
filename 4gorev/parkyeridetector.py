import cv2
import numpy as np
import pickle


cap=cv2.VideoCapture("parkvideo.mp4")


def check(frame1):
    for pos in liste:
        x,y=pos

        crop=frame1[y:y+15,x:x+26]
        count=cv2.countNonZero(crop)
        if count<150:
            color = (0,255,0)
        else:
            color=(0,0,255)
        cv2.rectangle(frame,pos,(pos[0]+26,pos[1]+15),color,2)
"""frame1 dıye bir degsıken olusturulur. x,y degerlerını pos degıskenıne atıyoruz. daha sonra her elemanı pos degsıkenıne atıyoruz
belırtılen bolge 26x15 bolgelık alan kesılıryanı seçılır. ve crop degıskenıne atanır. daha sonra cv2.countNonZero ilgili bolgenın
pixel yogunlugu sayılır. ve ona gore olusturulacak dıkdortgenın rengı belırlenır. """

with open ("isaretli" , "rb") as f:  ##ısaretlenmıs dosyanı buraya getırdık.
    liste=pickle.load(f)

while True:
    ret, frame = cap.read()
    if not ret:
        break 
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gri,(3,3),1)
    tresh=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    median=cv2.medianBlur(tresh,5)
    dilates=cv2.dilate(median,np.ones((3,3)),iterations=1)
    
    check(dilates)

    cv2.imshow("ass",frame)
    cv2.imshow("asss",gri)

    cv2.imshow("assa",blur)


    if cv2.waitKey(30) & 0xFF==ord("q") :
        break

cap.release()
cv2.destroyAllWindows()  
