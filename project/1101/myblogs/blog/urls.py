#__author__:asus
#date:2018/11/8
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^article/(?P<article_id>[0-9]+)/$',views.index,name='article_page'),

]