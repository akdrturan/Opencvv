import cv2 
import pickle

try:
    with open("isaretli", "rb") as f :
        liste=pickle.load(f)
    
#with açıklama, bir dosya veya kaynak gibi belirli bir kaynağın depolaması için kullanılır.
## try bir hata fonksıyonudur. yanı deneme ve hata ayıklar. with ıle olan dosya yoksa except satırına atlar ve ordan bos
##bir liste acar.
except:

    liste=[]
"""isaretli isminde bir dosya acılıyor. rb=readbinay anlamına gelıyor. olusturulan bu dosya f dıye bir degıskene atanıyor
pickle: Python'da tekrar sonuçları seri hale getirmek ve eski hale getirmek için kullanılan bir modüldür. 
Bu sayede programlar arasında veri alışverişi veya kayıtlı olarak saklanması gibi koşullar için kullanılır."""

def mouse(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        liste.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:
        for i , pos in enumerate(liste):
            x1,y1=pos
            if x1<x<x1+26 and y1<y<y1+15:
                liste.pop(i)
    with open("isaretli","wb") as f:            ## Bu, programın çalışması sırasında verilerin kalıcı olarak depolanmasını veya başka bir programda kullanılmasını sağlar.
        pickle.dump(liste,f)
"""events maus hareketlerının paramatlerelerını belırler. x-y kordınatları ıcın kullanılacak parametrelerdır.
ilk olarak sol butona basıldıgında ilgili konumu liste degıskenının ıcıne at.sag butona basılması halınde y1-x1 konumlarını 
pos degıskenınıne at ve bunu lıste degıskenıne at. ve ındexlerını de i ile kodla. egerkı konum belırtılen alanda ıse lıstenden 
olusturulan ındex numaralı degerı sıldır. 


i değişkeni, listenin indeksini temsil eder.
pos değişkeni, listenin her bir elemanını temsil eder."""

while True:
    img=cv2.imread("park.png")
    #print(liste)

    for l in liste:
        cv2.rectangle(img,l,(l[0]+26,l[1]+15),(255,0,0),2)



    cv2.imshow("img",img)
    cv2.setMouseCallback("img",mouse) ##maus hareketının etkılı olmasını ıstedıgımız yer 

    if cv2.waitKey(1) &0xFF == ord("q"):

        break

cv2.destroyAllWindows()