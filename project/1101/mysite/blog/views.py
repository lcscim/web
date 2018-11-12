from django.shortcuts import render
from .models import Blog,BlogType
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from read_statistics.utils import read_statistics_once_read
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment

def get_page_list_common_data(request,blogs_all_list):
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

    '''
    #获取博客分类方法一
    blog_types=BlogType.objects.all()
    blog_types_list=[]
    for blog_type in blog_types:
        blog_type.blog_count = Blog.objects.filter(blog_type=blog_type).count()
        blog_types_list.append(blog_type)
    '''

    #获取博客时间分类方法一
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')
    blog_dates_dict={}
    for blog_date in blog_dates:
        blog_count=Blog.objects.filter(created_time__year=blog_date.year,
                                       created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date]=blog_count

    context = {}
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['page_range'] = page_range
    context['blog_date'] = blog_dates_dict
    return context

def blog_list(request):
    blogs_all_list=Blog.objects.all()
    context=get_page_list_common_data(request,blogs_all_list)
    return render(request, 'blog_list.html', context)

def blog_detail(request,blog_pk):
    blog_message=Blog.objects.filter(id=blog_pk).first()
    read_cookie_key = read_statistics_once_read(request,blog_message)

    blog_content_type = ContentType.objects.get_for_model(blog_message)
    comments = Comment.objects.filter(content_type=blog_content_type,object_id=blog_message.pk)

    context={}
    context['blog_message']=blog_message
    context['comments'] = comments
    context['previous_blog']=Blog.objects.filter(created_time__gt=blog_message.created_time).last()
    context['next_blog']=Blog.objects.filter(created_time__lt=blog_message.created_time).first()
    response = render(request, 'blog_detail.html', context)
    response.set_cookie(read_cookie_key,'true')
    return response
def blogs_with_type(request,blog_type_pk):
    blog_type=BlogType.objects.filter(pk=blog_type_pk).first()
    blogs_all_list=Blog.objects.filter(blog_type=blog_type)

    context = get_page_list_common_data(request,blogs_all_list)
    context['blog_type'] = blog_type
    return render(request, 'blogs_with_type.html', context)

def blogs_with_date(request,year,month):
    blogs_all_list=Blog.objects.filter(created_time__year=year,created_time__month=month)
    context = get_page_list_common_data(request,blogs_all_list)
    return render(request, 'blogs_with_date.html', context)
