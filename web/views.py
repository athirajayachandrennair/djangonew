from django.shortcuts import render,redirect
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login as log,logout


def index(request):
    return render(request,'index.html')




def login(request):
    return  render(request,'login.html')


def loguser(request):
    if request.method=='POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            log(request,user)
            return  redirect('loggeduser')
        else:
            return render(request,'login.html')
    else:
        return  render(request,'index.html')


def loggeduser(request):
    return  render(request,'user.html')

def logoutuser(request):
    logout(request)
    return redirect('index')