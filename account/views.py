from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')

def studentSignup(request):
    return render(request,'student.html')