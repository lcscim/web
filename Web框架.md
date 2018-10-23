#10.11
- {{}}中是变量
- （%%}中是语句
https://www.cnblogs.com/yuanchenqi/articles/6083427.html
##1. Django的流程
1. 安装

	 #安装： pip3 install django
          添加环境变量
    #1  创建project
       django-admin startproject mysite
       ---mysite
          ---settings.py
          ---url.py
          ---wsgi.py
       ---- manage.py(启动文件)  
    #2  创建APP       
       python mannage.py startapp  app01
    #3  settings配置
       TEMPLATES
       STATICFILES_DIRS=(
            os.path.join(BASE_DIR,"statics"),
        )
       STATIC_URL = '/static/' 
       #  我们只能用 STATIC_URL，但STATIC_URL会按着你的STATICFILES_DIRS去找#4  根据需求设计代码
           url.py
           view.py
    #5  使用模版
       render(req,"index.html")   
    #6  启动项目
       python manage.py runserver  127.0.0.1:8090
    #7  连接数据库，操作数据
       model.py
2. django的命令行工具

	#在命令行中如此操作，pycharm除外
	<1> 创建一个django工程 : django-admin.py startproject 工程名
	<2>在mysite目录下创建blog应用: python manage.py startapp 应用名
	#在pycharm中
	<3>启动django项目：python manage.py runserver 8080
	<4>生成同步数据库的脚本：python manage.py makemigrations 工程名 
               同步数据库:  python manage.py migrate 工程名
	<5>当我们访问http://127.0.0.1:8080/admin/时就会显示

	注：在urls文件中

		from django.contrib import admin
		from django.urls import path
		from mysite import views	导入包
		
		urlpatterns = [
		    path('admin/', admin.site.urls),
			#网站目录，和启用方法
		    path('index/', views.userInfor),
		]

#10.12

##1. Django URL (路由系统)
- 无名分组
	
	urlpatterns = [
	    url(正则表达式, views视图函数，参数，别名),
	]
	参数说明：
	
		一个正则表达式字符串
		一个可调用对象，通常为一个视图函数或一个指定视图函数路径的字符串
		可选的要传递给视图函数的默认参数（字典形式）
		一个可选的name参数
		
		#正则表达式
		- ^s表示必须以s开头
		- s$表示必须以s结尾
	示例
	
		from django.conf.urls import url
		from django.contrib import admin
		from app01 import views
		urlpatterns = [
			#匹配路径名必须是articles/2003/。
		    url(r'^articles/2003/$', views.special_case_2003),
			# [0-9]{4} =》  0-9任意一个重复四次，加一个小括号表示这个数字可以用变量接受  year_archive方法必须接受两个参数一个req另一个就是括号内
		    url(r'^articles/([0-9]{4})/$', views.year_archive),  #no_named group
			#如果两个参数表示再添加两个参数
		    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
			#此时经过分组并且命名，方法内的形参名必须是该分组名
		    url(r'^articles/(?p<year>[0-9]{4})/(?p<month>[0-9]{2})/(?p<day>[0-9]+)/$', views.article_detail),
		
		]
- 有名分组
	
	(?P<id>\d{3})表示分组组名叫id
	
		import re
		#(?P<id>\d{3})/(?P<name>\w{3}) 表示分组
		ret=re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
		print(ret.group())			//123/ooo
		print(ret.group('id'))		//123
		print(ret.group('name'))	//ooo

- 如果传入的参数与分组的参数名相同，后面的覆盖前面的

	url(r'^articles/(?P<name>[0-9]{4})/$', views.year_archive，{"name","alex"}),

##2.Django Views（视图函数）
http请求中产生两个核心对象：

        http请求：HttpRequest对象
        http响应：HttpResponse对象

所在位置：django.http

之前我们用到的参数req就是HttpRequest    检测方法：isinstance(request,HttpRequest)

1. HttpRequest对象的属性和方法：

	# path：       请求页面的全路径，不包括域名
	# method：     请求中使用的HTTP方法的字符串表示。全大写表示。例如
	#                    if  req.method=="GET":
	#                              do_something()
	#                    elseif req.method=="POST":
	#                              do_something_else()
	# GET:         包含所有HTTP GET参数的类字典对象
	# POST：       包含所有HTTP POST参数的类字典对象
	#              服务器收到空的POST请求的情况也是可能发生的，也就是说，表单form通过
	#              HTTP POST方法提交请求，但是表单中可能没有数据，因此不能使用
	#              if req.POST来判断是否使用了HTTP POST 方法；应该使用  if req.method=="POST"
	# COOKIES:     包含所有cookies的标准Python字典对象；keys和values都是字符串。
	# FILES：      包含所有上传文件的类字典对象；FILES中的每一个Key都是<input type="file" name="" />标签中                     name属性的值，FILES中的每一个value同时也是一个标准的python字典对象，包含下面三个Keys：
	#             filename：      上传文件名，用字符串表示
	#             content_type:   上传文件的Content Type
	#             content：       上传文件的原始内容
	# user：       是一个django.contrib.auth.models.User对象，代表当前登陆的用户。如果访问用户当前
	#              没有登陆，user将被初始化为django.contrib.auth.models.AnonymousUser的实例。你
	#              可以通过user的is_authenticated()方法来辨别用户是否登陆：
	#              if req.user.is_authenticated();只有激活Django中的AuthenticationMiddleware
	#              时该属性才可用
	# session：    唯一可读写的属性，代表当前会话的字典对象；自己有激活Django中的session支持时该属性才可用。
	
	#方法
	get_full_path(),   比如：http://127.0.0.1:8000/index33/?name=123 ,req.get_full_path()得到的结果就是/index33/?name=123
	req.path:/index33
2. HttpResponse对象：
  
	对于HttpRequest对象来说，是由django自动创建的，但是，HttpResponse对象就必须我们自己创建。每个view请求处理方法必须返回一个HttpResponse对象。

  	HttpResponse类在django.http.HttpResponse

  	在HttpResponse对象上扩展的常用方法：

	页面渲染：         	render()（推荐）<br>                		
						render_to_response(),
	页面跳转：         	redirect("路径")
	
	locals()：    可以直接将函数中所有的变量传给模板
	- render(req,"login.html")
	- render_to_response("login.html",{"name":"alex"})	,可向login.html中的{{name}}变量进行修改
	- render_to_response("login.html",locals())		这样可以直接在login.html中使用方法中的变量{{ 函数中的变量名 }}



#10.14

##1.tips

- form表单提交数据会刷新页面，此时就需要使用jQuery的ajax 
- 在前端也有json  

	- json.parse(字符串)		把字符串变为json对象
	- json.stringify(对象)	把对象变为字符串

- 在前端location.reload()表示刷新当前页面
- 在前端location.href(路径)表示跳转到目标路径
- 使用ajax时如果返回服务器中的data值中有列表，就需要再添加一行traditional:true,这样才能发送成功

- 一些插件

	- bootstrap		https://v4.bootcss.com/
	- fontawesome	http://fontawesome.dashgame.com/

- 在ajax中，接收到的json格式文件对其进行支持，需添加dataType:'JSON',

		$.ajax({
		    url:'/modal_add_teacher/',
		    type: 'POST',
		    data:{'name':name,'class_id_list':class_id_list},
		    traditional:true,//
		    dataType:'JSON',
		    success:function (arg) {
		        if (arg.status){
		            location.reload()
		        } else {
		            alert(arg.message)
		        }
		    }
		})
- 响应式 @media (Max-wide:700px){ ... } 表示窗口宽度小于700px时加载大括号中的样式
- css属性min-width: 1190px;表示当浏览器窗口宽度小于1190px时会在屏幕下方出现滚动条
- css属性overflow: scroll;表示当内容超出窗口长度出现滚动条
- cookie是保存在电脑上的键值对

	obj=redirect('/exp/')
    obj.set_cookie('ticket','asdasdasdasd'，max_age=10,expires=value)
	#max_age=10,expires=value,这两个都代表时间制，第一个是多少秒后失效，第二个表示什么时间失效
    return obj
	
	签过名的：
		#set_signed_cookie设置签名cookie
		obj=redirect('/exp/')
	    obj.set_signed_cookie('ticket','asdasdasdasd',salt='jjjjjjjj')
	    return obj
		#get_signed_cookie('ticket',salt='jjjjjjjj')获取签名cookie
		req.get_signed_cookie('ticket',salt='jjjjjjjj')
- 使用命令行创建Django  

	django-admin startproject + 项目名
	
	到根目录下使用命令 Python manage.py startapp app02  创建了名为APP02的子项目

- URL使用正则表达式必须导入URL模块from django.conf.urls import url  叫做动态路由
	
	url('edit/(\w+).html', views.edit),
	#正则表达式前加?P<a1>表示指定方法参数a1,a2  位置就可以随便放了。否则必须按顺序
	url('edit/(?P<a1>\w+)/(?P<a2>\w+)/', views.edit),
	def edit(req,a1,a2):
    return HttpResponse(a1+a2)
- 路由除结尾的/ 使用终止符$更合适，此时就不用/结尾

	url('index$', views.index),
- from django.urls import reverse
	...
    v = reverse('join')
    print(v)	
    #返回url中  name=‘join’的路径
	v=reverse('n1',kwargs={'a1':a1})
    print(v)
	#返回当前路径
	v=reverse('n1',args=(456,))
    print(v)
	#可手工设置值
- 伪静态就是自己设定网页路径结尾即手动设置.html
###1.1 Django数据库
Django中默认的数据库是sqlite要使用MySQL需对设置进行修改
1. 首先创建数据库
2. 在setting文件中修改
	DATABASES = {
	    'default': {
	    'ENGINE': 'django.db.backends.mysql',
	    'NAME':'数据库名',
	    'USER': 'root',
	    'PASSWORD': 'xxx',
	    'HOST': 地址,
	    'PORT': 端口,
	    }
	}
3. 在根目录的__init__中添加

	import pymysql
	pymysql.install_as_MySQLdb()
4. 生成数据表,在models中写入

	from django.db import models
	class UserInfo(models.Model):
	    nid=models.AutoField(primary_key=True)
	    username=models.CharField(max_length=32)
	    password=models.CharField(max_length=64)
5. 最后在setting中添加项目文件注册

	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    #'logins'
	]
6. 创建数据表		重要

	Python manage.py makemigrations +项目名
	python manage.py migrate
7. 创建外键
	#需要填上这两个参数on_delete=models.CASCADE,null=True，此时外键名为ug_id
	ug=models.ForeignKey("UserGroup",on_delete=models.CASCADE,null=True)
8. 添加数据
	from django.shortcuts import HttpResponse,render,redirect
	from login import models
	def login(req):
		#添加数据
	    models.UserGroup.objects.create(title='销售部')
	    models.UserInfo.objects.create(user='root',password='pwd',age=18,ug_id=1)
		
		
	    return render(req,'login.html',{'group_list':group_list,})
9. 查询数据
	#查询所有数据
	group_list=models.UserGroup.objects.all(）
	#查询id=1的数据
	group=models.UserGroup.objects.filter(id=1)
	#查询id=1 and title='666'的
    group=models.UserGroup.objects.filter(id=1,title='666')
    #查询id>1的数据
    group=models.UserGroup.objects.filter(id__gt=1)
	#查询id<1的数据
    group=models.UserGroup.objects.filter(id__lt=1)
10. 删除

	models.UserGroup.objects.filter(id=2).delete()
11. 更新

	models.UserGroup.objects.filter(id=2).update(title='公关部')
###1.2 CBV和FBV
- CBV就是以类的方式使用
	#在url文件中
	from django.conf.urls import url
	from app01 import views
	urlpatterns = [
	    path('admin/', admin.site.urls),
		#Login是个类，使用时必须使用as_view()方法
	    url(r'^login.html$', views.Login.as_view()),
	]
	#在views文件中，该类必须继承自view
	from django.views import View
	class Login(View):
	    def get(self,req):
	        return HttpResponse('hello')
	    def post(self,req):
	        return HttpResponse('world')
###1.3 ORM操作数据库
- 正向操作，由外键所在的数据库去查找关联的数据库中的相关内容
    
	result=models.UserInfo.objects.all()
    for obj in result:
       print(obj.id,obj.name,obj.ut_id,obj.ut.title)
- 反向操作，由关联的数据库去查找外键所在的数据库中的相关内容
    
	result=models.UserType.objects.all().first()
    for obj in result.userinfo_set.all():
         print(obj.name,obj.age)
- 获取数据
	#获取多个数据，filter(id_gt=1)表示条件 id>1 返回是对象。结果可以跨表操作
	models.UserInfo.objects.all()
    models.UserInfo.objects.filter(id_gt=1)
	#返回是字典，不可跨表操作
    models.UserInfo.objects.all().values('id','name')
    models.UserInfo.objects.filter(id_gt=1).values('id','name')
		#如果要跨表在查询的时候需添加,下同
		models.UserInfo.objects.all().values('id','name'，"ut__title")
	#返回是元组，不可跨表操作
	models.UserInfo.objects.all().values_list('id','name')
	models.UserInfo.objects.filter(id_gt=1).values_list('id','name')
	
- 分页，即分批获取数据

	models.UserInfo.objects.all()[0:10]
	models.UserInfo.objects.all()[20:30]
- django内置分页

	- views中	
		from django.shortcuts import render
		from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
		L = []
		for i in range(999):
		    L.append(i)
		def index(request):
		    current_page = request.GET.get('p')	//传入个参数代表当前页数
		    paginator = Paginator(L, 10)	//第一个参数是要分页的对象，第二个是要求几个分为一页
		    # per_page: 每页显示条目数量
		    # count:    数据总个数
		    # num_pages:总页数
		    # page_range:总页数的索引范围，如: (1,10),(1,200)
		    # page:     page对象
		    try:
		        posts = paginator.page(current_page)
		        # has_next              是否有下一页
		        # next_page_number      下一页页码
		        # has_previous          是否有上一页
		        # previous_page_number  上一页页码
		        # object_list           分页之后的数据列表
		        # number                当前页
		        # paginator             paginator对象
		    except PageNotAnInteger:
		        posts = paginator.page(1)
		    except EmptyPage:
		        posts = paginator.page(paginator.num_pages)
		    return render(request, 'index.html', {'posts': posts})
	- HTML中

		<!DOCTYPE html>
		<html>
		<head lang="en">
		    <meta charset="UTF-8">
		    <title></title>
		</head>
		<body>
		<ul>
		    {% for item in posts %}
		        <li>{{ item }}</li>
		    {% endfor %}
		</ul>
		
		<div class="pagination">
		      <span class="step-links">
		        {% if posts.has_previous %}
		            <a href="?p={{ posts.previous_page_number }}">Previous</a>
		        {% endif %}
		          <span class="current">
		            Page {{ posts.number }} of {{ posts.paginator.num_pages }}.
		          </span>
		          {% if posts.has_next %}
		              <a href="?p={{ posts.next_page_number }}">Next</a>
		          {% endif %}
		      </span>
		
		</div>
		</body>
		</html>


###1.4 操作表 进阶操作（了不起的双下划线）
- 获取个数

    models.Tb1.objects.filter(name='seven').count()

- 大于，小于

    models.Tb1.objects.filter(id__gt=1)              # 获取id大于1的值
    models.Tb1.objects.filter(id__gte=1)              # 获取id大于等于1的值
    models.Tb1.objects.filter(id__lt=10)             # 获取id小于10的值
    models.Tb1.objects.filter(id__lte=10)             # 获取id小于10的值
    models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值

- in 

    models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
    models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in

- isnull 是否为空
    Entry.objects.filter(pub_date__isnull=True)

- contains是否包含

    models.Tb1.objects.filter(name__contains="ven")
    models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
    models.Tb1.objects.exclude(name__icontains="ven")

- range

    models.Tb1.objects.filter(id__range=[1, 2])   # 范围bettwen and

    其他类似

    startswith，istartswith, endswith, iendswith,

- order by 排序

    models.Tb1.objects.filter(name='seven').order_by('id')    # asc 从小到大
    models.Tb1.objects.filter(name='seven').order_by('-id')   # desc 从大到小

- group by

    from django.db.models import Count, Min, Max, Sum
    models.Tb1.objects.filter(c1=1).values('id').annotate(c=Count('num'))
    SELECT "app01_tb1"."id", COUNT("app01_tb1"."num") AS "c" FROM "app01_tb1" WHERE "app01_tb1"."c1" = 1 GROUP BY "app01_tb1"."id"

- limit 、offset

    models.Tb1.objects.all()[10:20]

- regex正则匹配，iregex 不区分大小写

    Entry.objects.get(title__regex=r'^(An?|The) +')
    Entry.objects.get(title__iregex=r'^(an?|the) +')

- date

    Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
    Entry.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1))

- year

    Entry.objects.filter(pub_date__year=2005)
    Entry.objects.filter(pub_date__year__gte=2005)

- month

    Entry.objects.filter(pub_date__month=12)
    Entry.objects.filter(pub_date__month__gte=6)

- day

    Entry.objects.filter(pub_date__day=3)
    Entry.objects.filter(pub_date__day__gte=3)
- week_day

    Entry.objects.filter(pub_date__week_day=2)
    Entry.objects.filter(pub_date__week_day__gte=2)

- hour

    Event.objects.filter(timestamp__hour=23)
    Event.objects.filter(time__hour=5)
    Event.objects.filter(timestamp__hour__gte=12)
- minute

    Event.objects.filter(timestamp__minute=29)
    Event.objects.filter(time__minute=46)
    Event.objects.filter(timestamp__minute__gte=29)

- second

    Event.objects.filter(timestamp__second=31)
    Event.objects.filter(time__second=2)
    Event.objects.filter(timestamp__second__gte=31)

- F访问数据库中的数据

    from django.db.models import F
    models.Tb1.objects.update(num=F('num')+1)


- Q用于构造复杂的查询条件

    方式一：
    Q(nid__gt=10)
    Q(nid=8) | Q(nid__gt=10)
    Q(Q(nid=8) | Q(nid__gt=10)) & Q(caption='root')
    方式二：
    con = Q()
    q1 = Q()
    q1.connector = 'OR'
    q1.children.append(('id', 1))
    q1.children.append(('id', 10))
    q1.children.append(('id', 9))
    q2 = Q()
    q2.connector = 'OR'
    q2.children.append(('c1', 1))
    q2.children.append(('c1', 10))
    q2.children.append(('c1', 9))
    con.add(q1, 'AND')
    con.add(q2, 'AND')

    models.Tb1.objects.filter(con)
##2.相关资料
Django【基础篇】
https://www.cnblogs.com/wupeiqi/articles/5237704.html
Django【进阶篇】
https://www.cnblogs.com/wupeiqi/articles/5246483.html
Django之Model操作
https://www.cnblogs.com/wupeiqi/articles/6216618.html
Django之Form组件
https://www.cnblogs.com/wupeiqi/articles/6144178.html

#10.22
##1.注意
- 一个关系表的两项 都是另一个数据表的主键
	from django.db import models
	
	class UserInfo(models.Model):
	    nickname=models.CharField(max_length=32)
	    username=models.CharField(max_length=32)
	    password=models.CharField(max_length=64)
	    gender_choices={
	        (1,'男'),
	        (2,'女'),
	    }
	    gender=models.IntegerField(choices=gender_choices)
	
	# 反向操作时会造成冲突
	#obj对象男是u2u_set.all(),女是u2u_set.all()
	#解决办法related_query_name
	#此时就是a_set.all()  男 b_set.all()
	# 或者related_name  常用作替换反响查找名
	# 此时就是a.all()  男 b.all()
	class U2U(models.Model):
	    g=models.ForeignKey('UserInfo',on_delete=models.CASCADE,related_name='a')
	    b=models.ForeignKey('UserInfo',on_delete=models.CASCADE,related_name='b')


