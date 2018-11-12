from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import get_seven_days_read_data,get_today_hot_data,get_yesterday_hot_data,get_7_days_hot_blogs
from blog.models import Blog
from django.core.cache import cache
from django.contrib import auth
from django.urls import reverse
from .forms import LoginForm

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates,read_nums = get_seven_days_read_data(blog_content_type)

    #获取7天热门博客缓存数据
    hot_blogs_for_7_days = cache.get('hot_blogs_for_7_days')
    if hot_blogs_for_7_days is None:
        hot_blogs_for_7_days = get_7_days_hot_blogs()
        cache.set('hot_blogs_for_7_days',hot_blogs_for_7_days,3600)
        print('calc')
    else:
        print('use cache')

    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['hot_blogs_for_7_days'] = hot_blogs_for_7_days
    return render(request,'home.html',context)

def login(request):
    '''
     username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(request,username=username,password=password)
    referer = request.META.get('HTTP_REFERER',reverse('home'))
    if user is not None:
        auth.login(request,user)
        return redirect(referer)
    else:
        return render(request,'error.html',{'message':'用户名或密码不正确'})
    :param request:
    :return:
    '''
    if request.method=='POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from',reverse('home')))
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request,'login.html',context)