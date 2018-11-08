from django.contrib import admin

# Register your models here.

from .models import Article
#使用自带的后台管理
admin.site.register(Article)

