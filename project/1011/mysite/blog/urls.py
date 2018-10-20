#__author__:asus
#date:2018/10/12
from django.contrib import admin
from django.urls import path,include
from mysite import views

urlpatterns = [
    #分发后的子链接为分发前的原链接+分发后的子链接，此处为 127.0.0.1:8080/blog/blog
    path('blog/', views.blogs,name="blogs"),
]