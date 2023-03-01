from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from home.forms import signupform

from datetime import datetime
from home.models import Contact, Info , Signup
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm 
import os
import torch
from PIL import Image
from django.core.files.storage import FileSystemStorage
import pandas 
# Create your views here.

def Index(request):             #create function to create page
    # return HttpResponse("this is homepage")
    # context = {"katappa" : "hum ne chura dal diya" ,"bahubali" : "bahubali me..."}
    # return render(request , 'index.html', context)\
    # messages.success(request, "this is a message ")
   
    if request.method == 'POST':
        return redirect("info")
    else:

        return render(request , 'index.html')


def About(about):
    return render(about , 'about.html')




def Services(services):
    return render(services , 'services.html')
 

def Contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # contact =Contact(name=name, email=email, phone=phone ,date = datetime.today(), time = datetime.now())
        contact =Contact(name=name, email=email, phone=phone, desc=desc ,date = datetime.today(), time = datetime.now())
        contact.save()
        # messages.success(request, "your message has been sent!")
    return render(request, 'contact.html')








def Infos(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        proj  = request.POST.get('proj')
        info =Info(name=name, email=email, phone=phone, proj = proj)
        info.save()
        # messages.success(request, "your message has been sent!")
    

        if (proj == 'drone'):
            return redirect('drone')
        elif (proj == 'pothole'):
            return redirect('home')
        elif (proj == 'facemask'):
            return redirect('home')
        elif (proj == 'tooth'):
            return redirect('home')
        
    else:
        return render(request, 'info.html')


###################################################################################################################################


media = 'media'


def Makeprediction(path):
    
    
    model = torch.hub.load('ultralytics/yolov5', 'custom', path="static\\best.pt") 
    img = Image.open(path)
    result = model(img)
    CLASSES = ['Drone']
    available=[]    
    try:
        drone_count = result.pandas().xyxy[0].name.value_counts()[CLASSES[0]]
        # print('abc',drone_count)
        available.append(drone_count)
    except Exception as e:
        available.append(0)
    for index in range(len(CLASSES)):
        a = f""" {available[index]} - {CLASSES[index]} is detected"""
        print(a)
    return a

def Drone(request):
    if request.method == "POST" and request.FILES['upload']:
        if 'upload' not in request.FILES:
            err= "No images Selected"
            return render(request, 'drone.html',{'err':err})
        f = request.FILES['upload']
        if f == '':
            err='No files selected'
            return render (request, 'drone.html',{'err':err})
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file =fss.save(upload.name, upload)
        file_url=fss.url(file)
        predictions=Makeprediction(os.path.join(media, file))
        return render (request, 'drone.html', {'pred': predictions, 'file_url': file_url})

    else:
        return render(request, 'drone.html')

def Poth_makeprediction(path):
    
    
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=r"static/best.pt") 
    img = Image.open(path)
    result = model(img)
    CLASSES = ['Drone']
    available=[]    
    try:
        drone_count = result.pandas().xyxy[0].name.value_counts()[CLASSES[0]]
        # print('abc',drone_count)
        available.append(drone_count)
    except Exception as e:
        available.append(0)
    for index in range(len(CLASSES)):
        a = f""" {available[index]} - {CLASSES[index]} is detected"""
        print(a)
    return a

def Pothole(request):
    if request.method == "POST" and request.FILES['upload']:
        if 'upload' not in request.FILES:
            err= "No images Selected"
            return render(request, 'pthole.html',{'err':err})
        f = request.FILES['upload']
        if f == '':
            err='No files selected'
            return render (request, 'poyhole.html',{'err':err})
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file =fss.save(upload.name, upload)
        file_url=fss.url(file)
        predictions=Makeprediction(os.path.join(media, file))
        return render (request, 'pothole.html', {'pred': predictions, 'file_url': file_url})

    else:
        return render(request, 'pothole.html')
#############################################################################
def Signups(request):
    if request.method == 'POST':
        form  = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = signupform()
    return render(request, 'signup.html', {'form':form})
        

def Login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            user = authenticate(username = username, password = password)
            if user is not None:
                 login(request,user)
                 return redirect('../')
            else: 
                messages.info(request, "username or password is incorrect")
    return render(request, 'login.html')

def Logout(requst):
    logout(requst)
    return redirect('home')