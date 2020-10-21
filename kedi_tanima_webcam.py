import cv2

vid=cv2.VideoCapture(0)#webcamden kareleri alma

cat_cascade=cv2.CascadeClassifier("D:\\OpenCv\\haarcascade\\catcascade.xml")#eğilitmiş dosyayı dahil etme

def besle():
    print("kediyi besle")

a=0
while 1: #sonsuz döngüyle
    ret,frame=vid.read()#webcamden gelen görüntülere okuma işlemi
    frame = cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cats=cat_cascade.detectMultiScale(gray,1.3,5)#cat_cascade sayesinde kedilerin olduğu alan bulunup koordinatları değişkene atılıyor.
    for(x,y,w,h)in cats:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)#cats koordinatlarına kare çizdiriliyor
        a=x
    cv2.imshow("image",frame)
    if a!=0:
        besle()
        
    a=0
    if cv2.waitKey(5)&0XFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
    
                     
