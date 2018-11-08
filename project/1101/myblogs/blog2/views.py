from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'blog2/blog2.html',{'result':'hello.blog2',})