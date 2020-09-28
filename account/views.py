from django.shortcuts import render,redirect
from django.http.response import StreamingHttpResponse,HttpResponse
import cv2,os,urllib.request
from django.conf import settings
import numpy as np
from uuid import uuid4
from .models import user
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def uniqueid():
    id= str(uuid4().int>>64)[:8]
    id = int(id)
    return id

def signup(request):
    return render(request,'signup.html')

def login1(request):
    if request.method == 'POST':
        email1 = request.POST["email3"],
        password1 = request.POST["password2"]
        u = authenticate(request,username =email1 ,password =password1)
        print(u)

        if u is not None:
            id = user.objects.get(email = email1)
            return redirect('home/'+ str(id.user_id))
        else:
            messages.error(request, 'Incorrect Password or Email.')
            return render(request,'signup.html')
    else:
        return render(request,'login.html')

def creat_user(request):
    if request.method == 'POST':
        id = uniqueid()
        u = user.objects.create(user_id=id,
        f_name = request.POST['first_name'],
        l_name = request.POST['last_name'],
        birthdate = request.POST['birthdate'],
        mobile_no = request.POST['mobile'],
        email = request.POST['email'],
        password = request.POST['password']
        )
        u.save()
        createdataset(id)
        return render(request,'login.html')
    else:
        return render(request,'signup.html')

def logout1(request):
    logout(request)
    return redirect('index')          

def createdataset(id):
    userId = id
    
    faceDetect = cv2.CascadeClassifier(os.path.join(settings.BASE_DIR,'static/xml/haarcascade_frontalface_alt.xml'))
    
    cam = cv2.VideoCapture(0)

    id = userId
    
    sampleNum = 0
    
    while(True):
        
        ret, img = cam.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        
        for(x,y,w,h) in faces:
            sampleNum = sampleNum+1
            cv2.imwrite(os.path.join(settings.BASE_DIR,'static/img/user/user.'+str(id)+'.'+str(sampleNum)+'.jpg'), gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)
            cv2.waitKey(250)

        img = cv2.putText(img,str(sampleNum),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        cv2.imshow("Face",img)
      
        cv2.waitKey(1)
        
        if(sampleNum>35):
            break
    
    trainer()
    cam.release()
    cv2.destroyAllWindows()
    return redirect('login.html')

def trainer():
    import os
    from PIL import Image

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = os.path.join(settings.BASE_DIR,'static/img/user')

    def getImagesWithID(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
        faces = []
        Ids = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1]) # -1 so that it will count from backwards and slipt the second index of the '.' Hence id
            faces.append(faceNp)
            Ids.append(ID)
        return np.array(Ids), np.array(faces)

    ids, faces = getImagesWithID(path)
    recognizer.train(faces, ids)
    recognizer.save(os.path.join(settings.BASE_DIR,'static/xml/trainingData.yml'))
    cv2.destroyAllWindows()
    return redirect('/') 

def detectface(request):
    
    faceDetect = cv2.CascadeClassifier(os.path.join(settings.BASE_DIR,'static/xml/haarcascade_frontalface_alt.xml'))
    cam = cv2.VideoCapture(0)
    # creating recognizer
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read(os.path.join(settings.BASE_DIR,'static/xml/trainingData.yml'))
    getId = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    userId = 0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)

            getId,conf = rec.predict(gray[y:y+h, x:x+w]) #This will predict the id of the face

            #print conf;
            if conf<35:
                userId = getId
                cv2.putText(img, "Detected",(x,y+h), font, 2, (0,255,0),2)
            else:
                cv2.putText(img, "Unknown",(x,y+h), font, 2, (0,0,255),2)

            # Printing that number below the face
            # @Prams cam image, id, location,font style, color, stroke

        cv2.imshow("Face",img)
        if(cv2.waitKey(1) == ord('q')):
            break
        elif(userId != 0):
            cv2.waitKey(1000)
            cam.release()
            cv2.destroyAllWindows()
            print(userId)
            cam.release()
            cv2.destroyAllWindows()
            return redirect('home/'+ str(userId))

            #return render(request,'home.html/'+str(userId))
    cam.release()
    cv2.destroyAllWindows()
    return redirect('/')

def home(request,id):
    u = user.objects.get(user_id = id)

    return render(request,'home.html',{'u':u})