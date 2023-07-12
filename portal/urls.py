from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path('signin',views.signin ,name="signin"),
    path('login_student',views.login_student, name="login_student"),
    path('login_teacher',views.login_teacher, name="login_teacher"),
    path('signup_student',views.signup_student, name="signup_student"),
    path('signup_teacher',views.signup_teacher, name="signup_teacher"),
    path('home',views.home, name="home"),
    path("logout/",views.logout ,name="logout"),
    path("student_index/",views.student_index ,name="student_index"),
]