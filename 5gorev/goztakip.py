import cv2
import dlib

detector=dlib.get_frontal_face_detector() ## yuzu tanıyan model
model=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") ##yuzdekı (lokalıtzasyon)noktaların tanımlandıgı model


cap=cv2.VideoCapture(0)

def mid ( p1,p2):
    return(int((p2[0]+p1[0])/2), int((p2[1]+p1[1])/2))   ##ortalama alıcı 

while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)      ##gri goruntu olusturulur


    faces=detector(frame)       ##orjınal goruntu detector nesnesının ıcını atılır
    for face in faces:          ##face için dongu hazırlanılır.
        points=model(gri,face)  ##tespıt edılen yuzler gri goruntu uzerıne alınır.
        points_list=[(p.x,p.y) for p in points.parts()] ##.parts ile point içindeki kordınatlar p uzerııne kaydedılır.lısteye yazdırılır.
    #print(points_list)

    """# Yüz landmark noktalarının koordinatlarını saklayacak bir liste oluşturma
points_list = []

# Her bir landmark noktası için yapılacak işlemler
for p in points.parts():
    # Noktanın x ve y koordinatlarını bir tuple içinde gruplama ve listeye ekleme
    points_list.append((p.x, p.y))"""

    p1,p2=points_list[37],points_list[38]
    p3,p4=points_list[40],points_list[41]

    p5,p6=points_list[43],points_list[44]
    p7,p8=points_list[46],points_list[47]


    ##cv2.circle(frame,(p1[0],p1[1]),3,(0,0,255),-1)
    ##cv2.circle(frame,(p2[0],p2[1]),3,(0,0,255),-1)

    po_ust_sol=mid(p1,p2)
    po_alt_sol=mid(p3,p4)

    cv2.circle(frame,(po_ust_sol[0],po_ust_sol[1]),3,(255,0,0),-1)
    cv2.circle(frame,(po_alt_sol[0],po_alt_sol[1]),3,(255,0,0),-1)


    po_ust_sag=mid(p5,p6)
    po_alt_sag=mid(p7,p8)

    cv2.circle(frame,(po_ust_sag[0],po_ust_sag[1]),3,(255,0,0),-1)
    cv2.circle(frame,(po_alt_sag[0],po_alt_sag[1]),3,(255,0,0),-1)


    ##print(po_alt_sol[1]-po_ust_sol[1])


    cv2.imshow("asd",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()



""" yukadarda yapılan tanımlamalar ıle    p5,p6=points_list[43],points_list[44]
    p7,p8=points_list[46],points_list[47] tanımlandı . sımdı ekrana yazdırma kısımına gelınce bu fonksıyonları kullanıp 
    frame uzerıde gosterınce işlem tamamlanmıs oluyor. ayrıca ek birseye gerek kalmıyor"""