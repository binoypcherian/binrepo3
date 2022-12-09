from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Create your views here.
def fun6(request):
    if request.method=='POST':
        username1 = request.POST['username']
        firstname1 = request.POST['firstname']
        lastname1 = request.POST['lastname']
        email1 = request.POST['email']
        password11 = request.POST['password']
        password12 = request.POST['password1']
        if password11==password12:
            if User.objects.filter(username=username1).exists():
                # print ("Username already exists")
                messages.info(request,"Username Already Taken")
                return redirect('fun6')
            elif User.objects.filter(email=email1).exists():
                # print("Email already exists")
                messages.info(request,"Email-ID Already Taken")
                return redirect('fun6')
            else:
                user1=User.objects.create_user(username=username1, first_name=firstname1, last_name=lastname1, email=email1, password=password11)
                user1.save()
                return redirect('fun7')
        else:
            # print("Passwords not Matching")
            messages.info(request,"Passwords not Matching")
            return redirect('fun6')
    return render(request,'register.html')

def fun7(request):
    if request.method=='POST':
        username01 = request.POST['user_login']
        password01 = request.POST['pass_login']
        user2=auth.authenticate(username=username01,password=password01)
        if user2 is not None:
            auth.login(request,user2)
            return redirect ('/')
        else:
            messages.info(request, "Invalid Login Credentials")
            return redirect('fun7')
    return render(request, 'login.html')

def fun8(request):
    auth.logout(request)
    return redirect ('/')