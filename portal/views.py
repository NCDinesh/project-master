from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Student_user, Teacher_user
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):
    return render(request,"signin.html")

def login_student(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username ,password=password)

        if user is not None:
            check = Student_user.objects.filter(username=username , password=password).first()
            if check is not None:
                auth.login(request,user)
                return HttpResponse("Student is logged in")
            
            else: 
                messages.info(request,"Either username or password is invalid")
        
        else:
            messages.info(request,"Either username or password is invalid")
            return redirect('login_student')
    return render(request,"login_student.html")

    
    
def login_teacher(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username ,password=password)

        if user is not None:
            check = Teacher_user.objects.filter(username=username , password=password).first()
            if check is not None:
                auth.login(request,user)
                return redirect('/')
            
            else: 
                messages.info(request,"Either username or password is invalid")
        
        else:
            messages.info(request,"Either username or password is invalid")
            return redirect('login_teacher')
    return render(request,"login_teacher.html")

def signup_student(request):
    ms=['EDC',"ECT", "EMX"]
    if request.method == "POST":
        fullname = request.POST["fullname"]
        rollno = request.POST["rollNo"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        subjects= request.POST.getlist('subjects')


        if password1 == password2:
            if Student_user.objects.filter(email=email).exists():
                messages.info(request,"Email alrealdy taken")
                return redirect("signup_student")
            
            elif Student_user.objects.filter(username=username).exists():
                messages.info(request,"Username alrealdy taken")
                return redirect("signup_student")
            
            elif Student_user.objects.filter(rollno=rollno).exists():
                messages.info(request,"Roll no alrealdy taken")
                return redirect("signup_student")
            
            elif Student_user.objects.filter(fullname=fullname).exists():
                messages.info(request,"Full name alrealdy taken")
                return redirect("signup_student")
            
            else:
                
                user_data = Student_user.objects.create(fullname=fullname, rollno=rollno, username=username, email=email, password=password1,subjects=subjects)
                user_data.save()


                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()

                user_login = auth.authenticate(username=username,password=password1)
                auth.login(request,user_login)
                return HttpResponse("Student is logged in")

        else:
            messages.info(request, "Password not matching")
            return redirect("signup_student")

    return render(request,"signup_student.html")



def signup_teacher(request):

    
    if request.method == "POST":
        fullname = request.POST["fullname"]
        subject = request.POST["subject"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        

        if password1 == password2:
            if Teacher_user.objects.filter(email=email).exists():
                messages.info(request,"Email alrealdy taken")
                return redirect("signup_teacher")
            
            elif Teacher_user.objects.filter(username=username).exists():
                messages.info(request,"Username alrealdy taken")
                return redirect("signup_teacher")
            
            elif Teacher_user.objects.filter(subject=subject).exists():
                messages.info(request,"Subject alrealdy taken")
                return redirect("signup_teacher")
            
            elif Teacher_user.objects.filter(fullname=fullname).exists():
                messages.info(request,"Full name alrealdy taken")
                return redirect("signup_teacher")
            
            else:
                user_data = Teacher_user.objects.create(fullname=fullname, subject=subject, username=username, email=email, password=password1)
                user_data.save()
            


                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()

    
                
                user_login = auth.authenticate(username=username,password=password1)
                auth.login(request,user_login)
                return redirect('/')

        else:
            messages.info(request, "Password not matching")
            return redirect("signup_teacher")

    return render(request,"signup_teacher.html")

def home(request):
    return HttpResponse("HomePage")

def logout(request):
    
    auth.logout(request)
    return redirect("signin")

@login_required(login_url='signin')
def index(request):
    data = Student_user.objects.filter(subjects__icontains='EMX')

    # for n in data:
    #     for sub in n.subjects:
    #         if sub=="EDC":
                

    return render(request,"index.html",{'data':data})