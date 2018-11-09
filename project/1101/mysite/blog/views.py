from django.shortcuts import render
from .models import Blog,BlogType

def blog_list(request):
    context=Blog.objects.all()
    blog_type=BlogType.objects.all()
    return render(request, 'blog_list.html', {'context':context,'blog_types':blog_type})

def blog_detail(request,blog_pk):

    context=Blog.objects.filter(id=blog_pk).first()
    return render(request, 'blog_detail.html', {'context': context, })

def blogs_with_type(request,blog_type_pk):
    blog_type=BlogType.objects.filter(pk=blog_type_pk).first()
    context=Blog.objects.filter(blog_type=blog_type)
    return render(request, 'blogs_with_type.html', {'context':context,'blog_type':blog_type,})