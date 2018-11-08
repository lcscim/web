from django.shortcuts import render,HttpResponse,redirect
from . import models
# Create your views here.

def index(request):
    # return HttpResponse('hello')
    articles=models.Article.objects.all()
    return render(request, 'blog/blog.html',{'articles':articles})

def article_page(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request,"blog/article_page.html",{"article":article})
