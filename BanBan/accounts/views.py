from django.shortcuts import render, redirect 
from django.contrib import auth 
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, passsword=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html') #로그인실패시

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    return render(request,'signup.html')

def success(request):
    return render(request,'success.html')