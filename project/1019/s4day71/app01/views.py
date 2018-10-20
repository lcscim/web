from django.shortcuts import render,redirect,HttpResponse
from app01 import models
# Create your views here.
from django.views import View
from utils import pager
class test(View):
    def get(self,req):

        # models.UserType.objects.create(title='普通用户')
        # models.UserType.objects.create(title='二逼用户')
        # models.UserType.objects.create(title='牛逼用户')
        # models.UserInfo.objects.create(name='李冰冰',age=18,ut_id=1)
        # models.UserInfo.objects.create(name='任泉',age=18,ut_id=2)
        # models.UserInfo.objects.create(name='吴奇隆',age=18,ut_id=2)
        # models.UserInfo.objects.create(name='范冰冰',age=18,ut_id=3)
        # models.UserInfo.objects.create(name='雷猴',age=18,ut_id=3)
        # models.UserInfo.objects.create(name='文字',age=18,ut_id=3)
        # models.UserInfo.objects.create(name='萨德',age=18,ut_id=3)
        # models.UserInfo.objects.create(name='问问群',age=18,ut_id=1)
        #正向操作，由外键所在的数据库去查找关联的数据库
        # result=models.UserInfo.objects.all()
        # for obj in result:
        #     print(obj.id,obj.name,obj.ut_id,obj.ut.title)
        #反向操作，由关联的数据库去查找外键所在的数据库
        # result=models.UserType.objects.all().first()
        # for obj in result.userinfo_set.all():
        #     print(obj.name,obj.age)
        # models.UserInfo.objects.all()
        # models.UserInfo.objects.filter(id_gt=1)
        #models.UserInfo.objects.all().values('id','name',"ut__title")
        # models.UserInfo.objects.filter(id_gt=1).values('id','name')
        # models.UserInfo.objects.all().values_list('id','name')
        # models.UserInfo.objects.filter(id_gt=1).values_list('id','name')
        return HttpResponse('hello get')
    def post(self,req):
        return HttpResponse('hello post')


class custom(View):
    def get(self,req):
        # 每10页显示一张内容
        # current_page=req.GET.get('page')
        # current_page=int(current_page)
        # per_page=10
        # start=(current_page-1)*per_page
        # end=current_page*per_page
        # result=models.UserInfo.objects.all()[start:end]
        current_page=req.GET.get('page')
        #获取所有元素的个数
        all_count=models.UserInfo.objects.all().count()
        page_info=pager.PageInfo(current_page,all_count,10,'/custom.html')
        result=models.UserInfo.objects.all()[page_info.start():page_info.end()]
        return render(req, 'custom.html', {'result': result,'page_list':page_info})
    def post(self,req):
        return HttpResponse('hello post')




