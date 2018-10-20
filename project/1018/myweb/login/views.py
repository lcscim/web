#__author__:asus
#date:2018/10/18
from django.shortcuts import HttpResponse,render,redirect
from login import models
def login(req):
    #models.UserGroup.objects.create(title='销售部')
    #models.UserInfo.objects.create(user='root',password='pwd',age=18,ug_id=1)

    group_list=models.UserGroup.objects.all()
    #group=models.UserGroup.objects.filter(id=1)
    #group=models.UserGroup.objects.filter(id=1,title='666')

    #group=models.UserGroup.objects.filter(id__gt=1)
    #group=models.UserGroup.objects.filter(id__lt=1)
    #models.UserGroup.objects.filter(id=2).delete()
    models.UserGroup.objects.filter(id=2).update(title='公关部')
    for row in group_list:
        print(row.id,row.title)
    # models.UserInfo.objects.all()
    #return HttpResponse('...')
    return render(req,'login.html',{'group_list':group_list,})