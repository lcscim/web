#__author__:asus
#date:2018/11/17
from django.shortcuts import render,redirect,HttpResponse

def home(request):
    return render(request, 'home.html')

def count(request):
    context = len(request.GET.get('text'))
    return render(request,'count.html',{'context':context})