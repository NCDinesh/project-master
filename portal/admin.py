from django.contrib import admin
from .models import Student_user,Teacher_user, subjectname

admin.site.register(Student_user)
admin.site.register(Teacher_user)
admin.site.register(subjectname)

# Register your models here.
