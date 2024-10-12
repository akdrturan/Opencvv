import cv2
import numpy as np
import pytesseract
import imutils

img=cv2.imread("plaka.jpg")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
filtre=cv2.bilateralFilter(gri,7,200,200)

kose=cv2.Canny(filtre,40,200)

kontour , a = cv2.findContours(kose,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=imutils.grab_contours((kontour,a))
cnt=sorted(cnt,key=cv2.contourArea,reverse=True)[:10]

ekran=0
for i in cnt:
    eps=0.018*cv2.arcLength(i,True)
    aprx=cv2.approxPolyDP(i,eps,True)
    if len(aprx)==4:
        ekran=aprx
        break

"""Bu kod bloğu, en büyük 10 kontur içindeki dört köşeli bir şekli (muhtemelen araç plakasını temsil eden bir dikdörtgen) bulur. 
Bu işlem, konturların köşelerini yakınlaştırarak ve köşe sayısını kontrol ederek gerçekleştirilir. 
Daha sonra, bulunan dört köşeli kontur, ekran değişkenine atanır.
Bu işlem, genellikle plaka gibi dikdörtgen şekilli nesneleri tespit etmek için kullanılır."""

maske=np.zeros(gri.shape,np.uint8)
yenimaske=cv2.drawContours(maske,[ekran],0,(255,255,255),-1)

"0: Konturun indeksi. Burada sadece bir kontur olduğu için 0 olarak belirtilmiştir."
"bu ıslemden sonra tum sekıl sıyah ekran olacak sadece ılgılı contour beyaz olacak"

yazi=cv2.bitwise_and(img,img,mask=maske)

"""Eğer maske pikseli beyazsa (255), o pikselin değeri orijinal görüntüdeki değerle aynı kalır.
Eğer maske pikseli siyahsa (0), o pikselin değeri sonuç görüntüsünde siyah olur."""

(x,y)=np.where(maske==255)
(ustx,usty)=(np.min(x),np.min(y))
(altx,alty)=(np.max(x),np.max(y))

kirp=gri[ustx:altx+1,usty:alty+1]



cv2.imshow("orj",img)
cv2.imshow("3",filtre)
cv2.imshow("4",kose)

cv2.imshow("yazi",yazi)
cv2.imshow("kirp",kirp)


cv2.waitKey(0)
cv2.destroyAllWindows()

