from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User1

def login(request):
    if request.method=="POST":
        username=request.POST.get("email")
        password=request.POST.get("pwd")
        form=User1.objects.filter(username=username,password=password)
        if form:
            return redirect("user_page")
        else:
            return HttpResponse("Invalid login")
    return render(request,"login.html")

def signup(request):
    if request.method=="POST":
        name=request.POST.get("name")
        username=request.POST.get("email")
        password=request.POST.get("pwd")
        form=User1.objects.create(name=name,username=username,password=password)
        if form:
            return redirect('login')
    return render(request,"signup.html")

def user_page(request):
    return render(request,"user_page.html")