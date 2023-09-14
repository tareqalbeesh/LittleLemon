from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def restaurant_view(request:HttpRequest):
    return render(request,'index.html',{})