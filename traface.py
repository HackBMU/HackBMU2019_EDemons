import cv2
import numpy as np 
from os import listdir
from os.path import isfile,join

data_path="C:\Users\Asus\Pictures\Camera Roll\New folder"
only_files=[f for f in listdir(data_path) 
               if isfile(join(data_path,f))]
Training_Data,Lables=[], []
for  i, files in enumerate(only_files):
    image_path=data_path+only_files[i]
    images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images,dtype=np.uint8))
    Lables.append(i)
Lables=np.asarray(Lables,dtype=np.int32)
model = cv2.face.LBPHFaceRecognizer_create();
model.train(np.asarray(Training_Data),np.asarray(Lables))
print("Be Happy your model get trained")

face_classifier=cv2.CascadeClassifier("C:\Users\Asus\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
def face_detector(coming_img,size=.5):
    gray=cv2.cvtColor(coming_img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    if faces is ():
        return coming_img,[]
    for (x,y,w,h) in faces:
        cv2.rectangle(coming_img,(x,y),(x+w,y+h),(0,255,255),2)
        roi=coming_img[y:y+h,x:x+w]
        roi=cv2.resize(roi,(200,200))
    return coming_img,roi
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    image,face=face_detector(frame)
    
    try:
         face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
         result = model.predict(face)

         if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            display_string = str(confidence)+'% Confidence it is user'
         cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)


         if confidence >83:
            cv2.putText(image, "Tum Hi ho mere AAKA", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', image)

         else:
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Cropper', image)


    except:
         cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
         cv2.imshow('Face Cropper', image)
         pass
     
    if cv2.waitKey(1)==13:
        break
    
cap.release()
cv2.destroyAllWindows()
