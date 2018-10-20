#__author__:asus
#date:2018/10/11
from django.shortcuts import render,HttpResponse
# info_list=[]
from mysite import models
def userInfor(req):

    if req.method=="POST":
        u=req.POST.get("username",None)
        s=req.POST.get("sex",None)
        e=req.POST.get("email",None)

        # info={"username":username,"sex":sex,"email":email}
        # info_list.append(info)
        models.UserInfo.objects.create(
            username=u,
            sex=s,
            email=e,
        )
    info_list = models.UserInfo.objects.all()
    return render(req,"index.html",{"info_list":info_list})
def login(req):
    if req.method=="POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        if username=="alex" and password=="123":
            return HttpResponse("登陆成功")

    return render(req,"login.html")
def blogs(req):
    if req.method=="POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        if username=="alex" and password=="123":
            return HttpResponse("登陆成功")

    return render(req,"login.html")
