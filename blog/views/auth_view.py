from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as LOGIN
from django.contrib import messages

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None: 
            LOGIN(request, user)
            return redirect("home")
        # else:
        #     return redirect("login")
    return render(request,'auth/login_page.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.create(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect("login")
    return render(request,'auth/register_page.html')