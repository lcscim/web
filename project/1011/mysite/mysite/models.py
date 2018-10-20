#__author__:asus
#date:2018/10/11
from django.db import models

class UserInfo(models.Model):
    username=models.CharField(max_length=64)
    sex=models.CharField(max_length=64)
    email=models.CharField(max_length=64)