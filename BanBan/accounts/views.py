from django.shortcuts import render, redirect 
from django.contrib import auth 

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, passsword=password)

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