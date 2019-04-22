from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password,make_password
from django import forms
from.forms import bio_form,register_form,SignUpForm
from.models import register,about,UserModel
# Create your views here.
def home_view(request):
    return render(request,'htmlfiles/educationandcareer.html')

def registratio_view(request):
    print("method called")
    if request.method=="POST":
        print("posrt called")
        form=register_form(request.POST)
        print("form checked")
        print(form)
        if form.is_valid():
            print("form accepted")
            Name=form.cleaned_data['Name']
            Phno=form.cleaned_data['Phno']
            DOB=form.cleaned_data['DOB']
            Adress=form.cleaned_data['Adress']
            Qualification=form.cleaned_data['Qualification']
            Email=form.cleaned_data['Email']
            Password=form.cleaned_data['Password']
            u=register(Name=Name,Phno=Phno,DOB=DOB,Adress=Adress,Qualification=Qualification,Email=Email,Password=make_password(Password))
            u.save()
            print("saved user")
            return redirect('bio/')
    elif request.method=="GET":
        print("view called")
        print(request.method)
        form=register_form()
    return render(request,'htmlfiles/Registration.html',{'form':form})


def about_view(request):
    return render(request,'htmlfiles/about.html')

def university_view(request):
    return render(request,'htmlfiles/university.html')

def courses_view(request):
    return render(request,'htmlfiles/courses.html')

def login_view(request):
    return render(request,'htmlfiles/login.html')

def registrationcarry_view(request):
    if request.method=='POST':
        print("posted")
        form=bio_form(request.POST)
        print("request post")
        print(form)
        if form.is_valid():
            print("form accepted")
            INTREST=form.cleaned_data['INTREST']
            Hobbies=form.cleaned_data['Hobbies']
            Bio=form.cleaned_data['Bio']
            r=about(INTREST=INTREST,Hobbies=Hobbies,Bio=Bio)
            r.save()
            print("saved")
            return redirect('login/')
    elif request.method=='GET':
        print("view called")
        print(request.method)
        form=bio_form()
    return render(request,'htmlfiles/bio.html')


def test(request):
    if request.method=='POST':
        print("posted")
        form=SignUpForm(request.POST)
        print("request post")
        if form.is_valid():
            print("form accepted")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username=form.cleaned_data['username']
            t= UserModel(name=name, email=email,password=make_password(password),username=username)
            t.save()
            print("saved user")
            return redirect('bio/')
    elif request.method == "GET":
            print("view called")
            print(request.method)
            form = SignUpForm()
    return render(request, 'htmlfiles/test_form.html', {'form': form})