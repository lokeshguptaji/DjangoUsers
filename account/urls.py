from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path('',views.home,name='home'),
     path('student/',views.studentSignup,name='student'),
     path('teacher/',views.teacherSignup,name='teacher'),
     path('login/',views.handleLogin,name='handleLogin'),
]
