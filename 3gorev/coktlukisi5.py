import cv2
import face_recognition


kisi1=face_recognition.load_image_file("haluk1.jpeg")
kisi1encoding=face_recognition.face_encodings(kisi1)[0]

kisi2=face_recognition.load_image_file("tarkan1.jpeg")
kisi2encoding=face_recognition.face_encodings(kisi2)[0]
## kisiye ait veriler alınıyor ve bunlar encode edılıyor 
## yani kutuphanenın tanımladıgı yontemi bir parametreye atıyor.

encodinglist=[kisi1encoding,kisi2encoding]
#datayı tek lısteye attık

namelist=["haluk", "tarkan"]


image=cv2.imread("tarkan-haluk.PNG")
test1=face_recognition.load_image_file("tarkan-haluk.PNG")
facelocations=face_recognition.face_locations(test1)
faceencodings=face_recognition.face_encodings(test1,facelocations)
##Bu işlev, yüz tanıma sistemlerinde yüzleri benzersiz bir şekilde temsil etmek için kullanılır. Elde edilen kodlamalar, yüzleri karşılaştırmak ve kimlik doğrulama işlemlerinde kullanılabilir 12.

##face_locations: Bulunan yüzlerin konumlarını içeren bir liste. Her yüz için dört koordinat (üst, sağ, alt, sol) verilir. Bu koordinatlar, yüzün sınırlarını belirler.
for facelog , faceencodin in zip(facelocations,faceencodings):
    ustsoly,altsagx,altsagy,ustsolx=facelog

    matchfaces=face_recognition.compare_faces(encodinglist,faceencodin)
    name="bilinmeyen"

    if True in matchfaces:
        matchindex=matchfaces.index(True)
        name=namelist[matchindex]

        cv2.rectangle(image,(ustsolx,ustsoly),(altsagx,altsagy),(0,255,0),3)
        cv2.putText(image,name,(ustsolx,ustsoly),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))

        cv2.imshow("da",image)
        print(name)

cv2.waitKey()
cv2.destroyAllWindows()
