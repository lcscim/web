from django.shortcuts import render,redirect,HttpResponse
from app01 import models
# Create your views here.
from django.forms import Form
from django.forms import fields

class ClassForm(Form):
    title=fields.RegexField('全栈\d+')
def class_list(req):
    cls_list=models.Classes.objects.all()
    return render(req,'class_list.html',{'cls_list':cls_list})

def add_class(req):
    if req.method=='GET':
        obj=ClassForm()
        return render(req,'add_class.html',{'obj':obj})
    else:
        obj=ClassForm(req.POST)
        if obj.is_valid():
            models.Classes.objects.create(**obj.cleaned_data)
            return redirect('/class_list/')
        return render(req, 'add_class.html', {'obj': obj})
def edit_class(req,nid):
    if req.method=="GET":
        row=models.Classes.objects.filter(id=nid).first()
        #initial=表示不验证，data表示直接验证
        obj=ClassForm(initial={'title':row.title})
        return render(req,'edit_class.html',{'nid':nid,'obj':obj})
    else:
        obj=ClassForm(req.POST)
        if obj.is_valid():
            models.Classes.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/class_list/')
        return render(req,'edit_class.html',{'nid':nid,'obj':obj})