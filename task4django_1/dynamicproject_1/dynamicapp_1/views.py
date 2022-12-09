from django.shortcuts import render
from .models import Place
from .models import Team
# Create your views here.
def fun1(request):
    obj=Place.objects.all
    obj1 = Team.objects.all
    return render(request,'index.html',{'result':obj,'result1':obj1})

def fun2(request):
    return render(request,'news.html')

def fun3(request):
    return render(request,'contact.html')

def fun4(request):
    return render(request,'destinations.html')

def fun5(request):
    return render(request,'elements.html')

