from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    return render(request,'home.html')

def studentSignup(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        email=request.POST.get('email','')
        pwd=request.POST.get('pwd','')
        cPwd=request.POST.get('cPwd','')
        stream=request.POST.get('stream','')
        myuser=User.objects.create_user(username,email,pwd)
        myuser.first_name=fname
        myuser.last_name=lname
        group = Group.objects.get(name='Student')
        myuser.groups.add(group)
        myuser.is_student = True
        myuser.save()
    return render(request,'student.html')

def teacherSignup(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        email=request.POST.get('email','')
        pwd=request.POST.get('pwd','')
        cPwd=request.POST.get('cPwd','')
        dept=request.POST.get('dept','')
        myuser=User.objects.create_user(username,email,pwd)
        myuser.first_name=fname
        myuser.last_name=lname
        group = Group.objects.get(name='Teacher')
        myuser.groups.add(group)
        myuser.is_teacher=True
        myuser.save()
    return render(request, 'teacher.html')

def handleLogin(request):
    if request.method=='POST':
        loginUsername=request.POST['loginUsername']
        loginPassword=request.POST['loginPassword']

        user=authenticate(username=loginUsername,password=loginPassword)
        login(request,user)
    return render(request,'stentry.html')