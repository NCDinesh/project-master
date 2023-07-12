from django.db import models

# Create your models here.
class Student_user(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    rollno = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100,default=None)

class Teacher_user(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    subject = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

# class subjectname(models.Model):
#     sub_name = models.CharField(max_length=100)
#     sub_id=models.IntegerField(default=None)