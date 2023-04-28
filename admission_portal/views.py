from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Personal_info
from .models import Course_listing
from django.contrib.auth.decorators import login_required

def Admission_Login(request):
    if request.user.is_authenticated:
        return redirect('admission_portal')

    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admission_portal')
            else:
                messages.info(request, 'invalid login details')
                return redirect('admission_login')

        else:
            return render(request, 'admission_login.html')

def Admission_logout(request):
    logout(request)
    return redirect('admission_login')


def Admission_register(request):
    if request.user.is_authenticated:
        return redirect('admission_portal')

    else:
        if request.method=='POST':
            username=request.POST['admission_username']
            first_name=request.POST['admission_first_name']
            last_name=request.POST['admission_last_name']
            email=request.POST['admission_email']
            password=request.POST['admission_password']
            password2=request.POST['admission_password2']
            if password==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'user already exists')
                    return redirect('admission_register')

                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'email have been registered before now')
                    return redirect('admission_register')

                else:
                    new_user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                    new_user.save()
                    return redirect('admission_login')

            else:
                messages.info(request,'password does not match')
                return redirect('admission_register')
        else:
            return render(request, 'admission_create_account.html')


@login_required(login_url='admission_login')
def Admission_portal(request):
    personal_info=Personal_info.objects.all()
    return render(request, 'admission_portal.html',{'personal_infos':personal_info})

@login_required(login_url='admission_login')
def Admission_documents(request):
    return render(request, 'admission_documents.html')

@login_required(login_url='admission_login')
def Apply(request):
    course_listing=Course_listing.objects.all()
    return render(request, 'apply.html',{'course_listings':course_listing})

@login_required(login_url='admission_login')
def Online_application_review(request):
    if request.method=='POST':
        Student_id=request.POST['Student_id']
        Given_name=request.POST['Given_name']
        Family_name=request.POST['Family_name']
        Middle_name=request.POST['Middle_name']
        Preffered_first_name=request.POST['Preffered_first_name']
        Preffered_family_name=request.POST['Preffered_family_name']
        Address=request.POST['Address']
        City=request.POST['City']
        Phone=request.POST['Phone']
        Email=request.POST['Email']
        Kin_given_name=request.POST['Kin_given_name']
        Kin_middle_name=request.POST['Kin_middle_name']
        Kin_family_name=request.POST['Kin_family_name']
        Kin_address=request.POST['Kin_address']
        Kin_city=request.POST['Kin_city']
        Kin_information_authorization=request.POST['Kin_information_authorization']
        School_name=request.POST['School_name']
        School_city=request.POST['School_city']
        Declaration_authorization=request.POST['Declaration_authorization']
        Signature=request.POST['Signature']
        Signature_date=request.POST['Signature_date']
        personal_info= Personal_info(Student_id=Student_id,Given_name=Given_name, Family_name=Family_name,
        Middle_name=Middle_name,Preffered_family_name=Preffered_family_name,Preffered_first_name=Preffered_first_name,
        Address=Address,City=City, Phone=Phone, Email=Email,Kin_given_name=Kin_given_name,
        Kin_middle_name=Kin_middle_name,Kin_family_name=Kin_family_name,Kin_city=Kin_city,Kin_address=Kin_address,
        Kin_information_authorization=Kin_information_authorization,School_city=School_city,School_name=School_name,
        Declaration_authorization=Declaration_authorization,Signature=Signature,Signature_date=Signature_date)
        personal_info.save()
        return redirect('admission_portal')

    else:
        return render(request, 'online_application_review.html')


@login_required(login_url='admission_login')
def Online_application_review_edit(request,pk):
    personal_info=Personal_info.objects.get(pk=pk)
    if request.method=='POST':
        pass

    else:
        form=Personal_info(instance=personal_info)
        return render (request, 'online_application_review.html',{'form':form})
        



@login_required(login_url='admission_login')
def Online_application(request):
    personal_info=Personal_info.objects.all()
    return render(request, 'online_application.html',{'personal_infos':personal_info})