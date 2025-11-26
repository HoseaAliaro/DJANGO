from django.shortcuts import render,redirect,get_object_or_404
from . forms import StudentForm
from django.http import HttpResponse
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . forms import *
from django.contrib.auth.decorators import login_required



# Create your views here.
def Home(request):
    return render(request,'MyApp/index.html')
@login_required
def stdForm(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('home')
    else:
        form=StudentForm()
        context={'form':form}
    return render(request,'MyApp/stdform.html',context)


#Custom forms
@login_required
def regStudent(request):
    if request.method=='POST':
       firstName=request.POST['fname']
       secondName=request.POST['lname']
       email=request.POST['email']
       regNo=request.POST['regNo']
       age=request.POST['age']
       std=Student(firstName=firstName,secondName=secondName,email=email,regNo=regNo,age=age)
       std.save()
       return HttpResponse('Success')
    else:
        return render (request,'MyApp/student_form.html')

@login_required    
def retrieveStd(request):
    std_data=Student.objects.all()
    context={'std_data':std_data}
    return render(request,'MyApp/std_details.html',context)

#updating student
@login_required
def updateStd(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
       new_fname=request.POST.get('fname')
       new_lname=request.POST.get('lname')
       new_email=request.POST.get('email')
       new_age=request.POST.get('age')
       new_regNo=request.POST.get('regNo')
       student.fname=new_fname
       student.lname=new_lname
       student.email=new_email
       student.age=new_age
       student.regNo=new_regNo
       student.save()
       return redirect ('fetch_std')
    else:
        context={'student':student}
        return render(request, 'MyApp/updateStd.html',context)
    
#delete data
@login_required
def deleteStd(request,pk):
    del_std=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        del_std.delete()
        return redirect('fetch_std')
    
    return render(request,'MyApp/deleteStd.html')

#user authentification

def userRegistration(request):
    if request.method=='POST':
        form=CustomUser(request.POST)
        if form.is_valid():
           form.save()
        return redirect('login')
    else:
        form=CustomUser()
    context={'form': form}
    return render(request,'MyApp/regist.html',context)
    
#user loginfunction

def login_view(request):
    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(request,username=username,password=password)

       if user is not None:
            login(request, user)
            return redirect('fetch_std')
       
    return render(request,'MyApp/login.html')


def logout_view(request):
    logout(request)
    return redirect('signin')

@login_required
def createPerson(request):
    if request.method=='POST':
        name=request.POST.get('name')
        photo=request.FILES.get('photo')
        cv=request.FILES.get('cv')
        person=Person(name=name,profile_pic=photo,cv=cv)
        person.save()
        return redirect('home')
    else:
        context={'p': Person}
    return render(request,'MyApp/media.html',context)



