from django.shortcuts import render
from .models import Blog,BlogType
from django.core.paginator import Paginator
from django.conf import settings



def blog_list(request):
    blogs_all_list=Blog.objects.all()
    pagintor =Paginator(blogs_all_list,settings.EACH_PAGE_BLOGS_NUMBER) #每10篇进行分页
    page_num=request.GET.get("page",1)  #获取url页面参数
    page_of_blogs=pagintor.get_page(page_num)

    currentr_page_num = page_of_blogs.number    #获取当前页面
    #获取当前页面前后各加两页范围
    page_range = list(range(max(currentr_page_num-2,1),currentr_page_num))+\
        list(range(currentr_page_num,min(currentr_page_num+2,pagintor.num_pages)+1))
    #加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0,'...')
    if pagintor.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    #加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != pagintor.num_pages:
        page_range.append(pagintor.num_pages)
    context={}
    blog_types=BlogType.objects.all()
    blog_date=Blog.objects.dates('created_time','month',order='DESC')
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = blog_types
    context['page_range'] = page_range
    context['blog_date'] = blog_date
    return render(request, 'blog_list.html', context)

def blog_detail(request,blog_pk):

    blog_message=Blog.objects.filter(id=blog_pk).first()
    previous_blog=Blog.objects.filter(created_time__gt=blog_message.created_time).last()
    next_blog=Blog.objects.filter(created_time__lt=blog_message.created_time).first()
    context={}
    context['blog_message']=blog_message
    context['previous_blog']=previous_blog
    context['next_blog']=next_blog

    return render(request, 'blog_detail.html', context)

def blogs_with_type(request,blog_type_pk):
    blog_type=BlogType.objects.filter(pk=blog_type_pk).first()
    context=Blog.objects.filter(blog_type=blog_type)

    pagintor = Paginator(context, settings.EACH_PAGE_BLOGS_NUMBER)  # 每10篇进行分页
    page_num = request.GET.get("page", 1)  # 获取url页面参数
    page_of_blogs = pagintor.get_page(page_num)

    currentr_page_num = page_of_blogs.number  # 获取当前页面
    # 获取当前页面前后各加两页范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, pagintor.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if pagintor.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != pagintor.num_pages:
        page_range.append(pagintor.num_pages)

    blog_types=BlogType.objects.all()
    return render(request, 'blogs_with_type.html', {'context':page_of_blogs,'blog_type':blog_type,'blog_types':blog_types,'page_range':page_range})

def blogs_with_date(request,year,month):
    blogs_all_list=Blog.objects.filter(created_time__year=year,created_time__month=month)
    pagintor = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 每10篇进行分页
    page_num = request.GET.get("page", 1)  # 获取url页面参数
    page_of_blogs = pagintor.get_page(page_num)

    currentr_page_num = page_of_blogs.number  # 获取当前页面
    # 获取当前页面前后各加两页范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, pagintor.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if pagintor.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != pagintor.num_pages:
        page_range.append(pagintor.num_pages)

    blog_types = BlogType.objects.all()
    blog_date = Blog.objects.dates('created_time', 'month', order='DESC')
    return render(request, 'blogs_with_date.html',
                  {'context': page_of_blogs, 'blog_types': blog_types, 'page_range': page_range,
                   'blog_date': blog_date})
