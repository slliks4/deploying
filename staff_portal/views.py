from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method=='GET':
        return render(request, 'staff_login.html')
    
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login_successful.html')
        else:
            messages.info(request, 'user does not exist')
            return redirect('login')

def Logout(request):
    logout(request)
    return redirect('login')

@login_required
def Student_portal(request):
    return render(request, 'student_portal.html')


