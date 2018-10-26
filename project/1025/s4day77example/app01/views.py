from django.shortcuts import render,redirect,HttpResponse
from app01 import models
# Create your views here.
from django.forms import Form
from django.forms import fields
from django.forms import widgets

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

class StudentForm(Form):
    name=fields.CharField(
        min_length=2,
        max_length=6,
        widget=widgets.TextInput(attrs={'class':'form-control'})
    )
    email=fields.EmailField(widget=widgets.TextInput(attrs={'class':'form-control'}))
    age=fields.IntegerField(min_value=18,max_value=25,widget=widgets.TextInput(attrs={'class':'form-control'}))
    cls_id=fields.IntegerField(
        widget=widgets.Select(choices=models.Classes.objects.values_list('id','title'),attrs={'class':'form-control'})
    )

def student_list(req):
    if req.method=='GET':
        stu_list=models.Student.objects.all()
        return render(req,'student_list.html',{'stu_list':stu_list})
    else:
        pass

def add_student(req):
    if req.method=='GET':
        obj=StudentForm()
        return render(req,'add_student.html',{'obj':obj})
    else:
        obj=StudentForm(req.POST)
        if obj.is_valid():
            models.Student.objects.create(**obj.cleaned_data)
            return redirect('/student_list/')
        return render(req,'add_student.html',{'obj':obj})

def edit_student(req,nid):
    if req.method=='GET':
        row=models.Student.objects.filter(id=nid).values('name','email','age','cls_id').first()

        obj=StudentForm(initial=row)
        return render(req,'edit_student.html',{'nid':nid,'obj':obj})
    else:
        obj = StudentForm(req.POST)
        if obj.is_valid():
            models.Student.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/student_list/')
        return render(req, 'edit_student.html', {'nid': nid, 'obj': obj})


