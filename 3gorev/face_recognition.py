import dlib
import cv2
import face_recognition


cap=cv2.VideoCapture(0)
kadir=face_recognition.load_image_file("kadir.png")
kadir_enc=face_recognition.face_encodings(kadir)[0]
detector=dlib.get_frontal_face_detector()

while True:
    ret , frame=cap.read()

    face_loc=[]
    faces=detector(frame)
    for face in faces:
        x=face.left()
        y=face.top()
        w=face.right()
        h=face.bottom()
        face_loc.append((y,w,x,h))
     


   ## face_loc=face_recognition.face_locations(frame)
    face_encoding=face_recognition.face_encodings(frame,face_loc)


    i=0
    for face in  face_encoding:
        y,w,h,x = face_loc[i]
        sonuc=face_recognition.compare_faces([kadir_enc],face)
        if sonuc[0]==True:
            cv2.rectangle(frame,(x,y),(w,h),(255,25,150),3,cv2.FONT_HERSHEY_SIMPLEX)
            cv2.putText(frame,"kadir",(x,h+35),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255))
        else:
            cv2.rectangle(frame,(x,y),(w,h),(255,25,150),3,cv2.FONT_HERSHEY_SIMPLEX)
            cv2.putText(frame,"elsee",(x,h+35),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255))
            
        print(sonuc)

    cv2.imshow("1",frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
