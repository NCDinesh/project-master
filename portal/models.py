from django.db import models

# Create your models here.
class Student_user(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    rollno = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100,default=None)
    classe = models.CharField(max_length=100)
    

class Teacher_user(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    subject = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class subjectname(models.Model):
    sub_name1 = models.CharField(max_length=100)
    sub_name2 = models.CharField(max_length=100)
    sub_name3 = models.CharField(max_length=100)
    sub_name4 = models.CharField(max_length=100)
    sub_name5 = models.CharField(max_length=100)
    sub_name6 = models.CharField(max_length=100)
    sub_name7 = models.CharField(max_length=100)
    sub_name8 = models.CharField(max_length=100)
    