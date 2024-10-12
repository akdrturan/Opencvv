import cv2
import numpy as np

vid=cv2.VideoCapture("video2.mp4")
backsub=cv2.createBackgroundSubtractorMOG2()
c=0
# Yeni boyutlar
new_width = 640
new_height = 480

while True:
    ret , frame=vid.read()
    if ret ==1:
        fgmask=backsub.apply(frame)

    fgmask = cv2.resize(fgmask, (new_width, new_height))
    frame = cv2.resize(frame, (new_width, new_height))

    cv2.line(frame,(0,350),(640,350),(0,255,0),3)
    cv2.line(frame,(0,300),(640,300),(0,0,255),3)


    contours,hiers=cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    try: hiers=hiers[0]
    except: hiers=[]

    for contour, hier in zip(contours,hiers):
        (x,y,w,h)=cv2.boundingRect(contour)
        if w>100 and h>100:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

        if y>300 and y<350:

            c=c+1

    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"car="+str(c),(90,100),font,2,(255,255,0),2,cv2.LINE_AA) 



    cv2.imshow("vaid",frame)
    cv2.imshow("vid",fgmask)

    if cv2.waitKey(10) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows



## kod eksık tam calısmıyor!!