#__author__:asus
#date:2018/11/8
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$',views.index),
]