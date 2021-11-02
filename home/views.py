from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User 
from .models import OrderForm
# Create your views here.

def index(request):
    return render(request,'home/index.html') 

def login_user(request):
    if request.method=="POST":
        Email=request.POST['Email']
        Password=request.POST['Password']
        # saving data in backend
        order=OrderForm(Email=Email,Password=Password)
        order.save()    
        # Creating user
        # myuser=User.objects.create_user(username,Email,Password)
        # myuser.save()
        return render(request,'home/hello.html') 
    else:
        return render(request,'home/login.html') 

        

def hello(request):
    return render(request,'home/hello.html') 