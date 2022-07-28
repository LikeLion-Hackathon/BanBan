from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.contrib import auth 
#from django.contrib.auth.models import User

"""def login(request):
    # POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, passsword=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패. 다시 시도')
            #return render(request, 'login.html') #로그인실패시
    
    # GET 요청이 들어오면 login form을 담고 있는 login.html을 띄워줌
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
"""

def signup(request):
    return render(request,'signup.html')

def success(request):
    return render(request,'success.html')