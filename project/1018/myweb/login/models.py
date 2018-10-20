#__author__:asus
#date:2018/10/18
from django.db import models
class UserGroup(models.Model):
    title=models.CharField(max_length=32)

class UserInfo(models.Model):
    nid=models.BigAutoField(primary_key=True)
    user=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    age=models.IntegerField(null=True)
    #自动生成ug_+id的外键名
    ug=models.ForeignKey("UserGroup",on_delete=models.CASCADE,null=True)