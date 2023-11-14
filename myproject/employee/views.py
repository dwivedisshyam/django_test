from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return HttpResponse("Hello, world. You're at the employee index.")

def home(request): 
    data = {
        "user":{
            "name":"Shyam"
        }   
    }

    return render(request, "employee/home.html",data) 