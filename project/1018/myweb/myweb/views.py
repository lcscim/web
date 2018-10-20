#__author__:asus
#date:2018/10/18
from django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse
def login(req):
    v = reverse('join')
    print(v)
    return HttpResponse(v)

def add_user(req,a1):
    v=reverse('n1',kwargs={'a1':a1})
    print(v)
    return HttpResponse(v)