
##1.pyinstaller
- 下载pyinstaller采用命令行操作的办法:

	在cmd命令行中，输入代码：
		pip install pyinstaller
	或者采用更新、升级的方法：
		pip install --upgrade pyinstaller
- 使用pyinstaller打包py文件成exe程序

	将cmd的目录切换至（命令：cd 文件路径(注意空格)）需要打包的py文件目录下

	并输入代码，格式为使用命令：pyinstaller -F 文件名（带后缀py）：
		
		pyinstaller -F test.py
	常用参数说明：

		–icon=图标路径
		-F 打包成一个exe文件
		-w 使用窗口，无控制台
		-c 使用控制台，无窗口
		-D 创建一个目录，里面包含exe以及其他一些依赖性文件
		pyinstaller -h 来查看参数
	回车后，代码迅速操作，直到操作结束。

	pyinstaller 改变生成exe程序的图标
		pyinstaller -F --icon=my.ico test.py
	my.ico 是一个图标名，和当前的test.py文件在同一个目录下

#9.9

##1.高阶函数
1. 函数名可以作为参数输入
2. 函数名可以作为返回值

##2.闭包
定义：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包

##3.装饰器
python装饰器就是用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数，使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能。

	#既不需要侵入，也不需要函数重复执行
	import time
	
	def deco(func):		//deco函数就是最原始的装饰器，它的参数是一个函数，然后返回值也是一个函数。
	    def wrapper():
	        startTime = time.time()
	        func()
	        endTime = time.time()
	        msecs = (endTime - startTime)*1000
	        print("time is %d ms" %msecs)
	    return wrapper
	
	
	@deco	//在函数func()前面加上@deco，func()函数就相当于被注入了计时功能，现在只要调用func()，它就已经变身为“新的功能更多”的函数了。 
	def func():
	    print("hello")
	    time.sleep(1)
	    print("world")
	
	if __name__ == '__main__':
	    f = func #这里f被赋值为func，执行f()就是执行func()
	    f()
装饰器的参数不一定是函数，但返回值一定是一个函数（包裹函数），而且包裹函数与原函数参数必须一致

##4.生成器
- 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
- 列表生成式

	a=[x for x in range(10)]  x可以为函数如fun(x)，但必须与for的名称相同
- 创建list和generator的区别仅在于最外层的[]和()

		>>> L = [x * x for x in range(10)]
		>>> L
		[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
		>>> g = (x * x for x in range(10))
		>>> g
		<generator object <genexpr> at 0x1022ef630>
	要一个一个打印出来，可以通过next()函数获得generator的下一个返回值

		>>> next(g)
		0
		>>> next(g)
		1
		>>> next(g)
		4
		>>> next(g)
		9
- 每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
- 我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
- 要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
		
		def fib(max):
		    n, a, b = 0, 0, 1
		    while n < max:
		        yield b
		        a, b = b, a + b
		        n = n + 1
		    return 'done'
##5.包package
按目录组织模块的方法，导入时如下

	from web.web2 import logger		//导入web包下的web2包中的logger模块
每个包下面都有一个__init__.py文件

假如module不在同一个目录下需添加文件所在路径

	import sys
	import os
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	sys.path.append(BASE_DIR)
##6.目录结构
- bin/:存放一些可执行文件
- foo/:存放项目的所有源代码，名称可以根据实际自定

	1. 源代码中所有模块 包 都应在此目录，不要置于顶层目录
	2. 其子目录tests/存放单元测试代码
	3. 程序的入口最好命名为main.py
- docs/:存放一些文档
- setup.py:安装部署打包的脚本
- requirements.txt:存放软件依赖的外部Python包序列
- readme:项目说明文件

##7.hashlib模块
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。示例

	import hashlib
	md5 = hashlib.md5()
	md5.update('how to use md5 in python hashlib?')
	print md5.hexdigest()
如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
##8.decode和encode
- decode的作用是将其他编码的字符串转换成unicode编码
- encode的作用是将unicode编码转换成其他编码的字符串
- decode():是解码，encode()是编码
##9.日志模块logging
logging模块是Python内置的标准模块，主要用于输出运行日志，可以设置输出日志的等级、日志保存路径、日志文件回滚等；相比print，具备如下优点：

1. 可以通过设置不同的日志等级，在release版本中只输出重要信息，而不必显示大量的调试信息；
2. print将所有信息都输出到标准输出中，严重影响开发者从标准输出中查看其它数据；logging则可以由开发者决定将信息输出到什么地方，以及怎么输出；

默认输出：
	import logging
	logging.basicConfig(level=logging.DEBUG, 
	                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
	                    datefmt='%a,%d %b %Y %H:%M:%S',		
	                    filename='test.log',	//设置文件名称
	                    filemode='w')	//，默认操作模式为a，如果有内容继续添加
	
	logging.debug("debug message")
	logging.info("info message")
	logging.warning("hello error")
	logging.error("error message")
	logging.critical("critical message")

文档的内容为： Sun,09 Sep 2018 21:23:39 - september.py[line:10] - DEBUG: debug message

#9.10

##1.eval()
将字符串string对象转化为有效的表达式参与求值运算返回计算结果

	eval（expression，globals=None, locals=None）返回的是计算结果

其中：

    expression是一个参与计算的python表达式
    globals是可选的参数，如果设置属性不为None的话，就必须是dictionary对象了
    locals也是一个可选的对象，如果设置属性不为None的话，可以是任何map对象
##2.序列化与反序列化
把对象（变量）从内存中变成可以存储或传输的过程称之为序列化。反过来把变量内容从序列化对象读取到新内存里称之为反序列化
##3.json模块
JSON编码器和解码器，处理json格式文本
- json.dumps()将obj序列化为str使用此转换表格式化的JSON 
- json.loads()反序列化
- json.dump(obj,f) 
- json.load(obj)

序列化
	import json
	dic = {'name':'alex','age':'18'}
	data = json.dumps(dic)
	f=open('JSON_text','w')
	f.write(data)
	f.close()
	#使用dump的效果
	import json
	dic = {'name':'alex','age':'18'}
	f=open('JSON_text','w')
	data = json.dump(dic，f)
	f.close()	
反序列化
	import json
	f=open("JSON_text",'r')
	data = f.read()
	data = json.loads(data)
	print(data)
	f.close()
	#使用load效果
	import json
	f=open("JSON_text",'r')
	data = json.load(f)
	print(data)
	f.close()	
##4.pickle Python对象序列化
该pickle模块实现了用于序列化和反序列化Python对象结构的二进制协议。用于存放（pickling）读取（unpickling）
- pickle.dumps()序列化
- pickle.loads()反序列化
- pickle.dump()
- pickle.load()


	import pickle
	def foo():
	    print("ok")
	data = pickle.dumps(foo)
	f=open('PICKLE_text','wb')
	f.write(data)
	f.close()
	#使用dump
	import pickle
	def foo():
	    print("ok")
	f = open('PICKLE_text', 'wb')
	data = pickle.dump(foo,f)
	f.close()

	import pickle
	def foo():
	    print("ok")
	f=open("PICKLE_text",'rb')
	data = f.read()
	data = pickle.loads(data)
	data()
	f.close()
	#使用load
	import pickle
	def foo():
	    print("ok")
	f=open("PICKLE_text",'rb')
	data = pickle.load(f)
	data()
	f.close()
注意：反序列化语句中必须需要原函数如上，foo
##5.shelve模块
Python对象持久性

	import shelve
	f = shelve.open(r'shelve.txt')
	f['info'] = {'name':'lcscim','age':'52'}
	f.close()
	
	import shelve
	f = shelve.open(r'shelve.txt')
	print(f.get('info')['age'])
	f.close()
##6.XML模块
是实现不同语言程序进行交换的协议跟json差不多。操作XML有以下方法：
- DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
- SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
- ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。

正常情况下，优先考虑SAX，因为DOM实在太占内存。

	import xml.etree.cElementTree as ET
	tree = ET.parse('XML_text')
	root = tree.getroot()
	print(root.tag)#获取文件的标签
	for neighbor in root.iter('neighbor'):
	    #递归迭代它下面的所有子树（它的子节点，它们的子节点等）
	    print(neighbor.attrib)
	for country in root.findall('country'):
	    #仅查找具有标记的元素，这些元素是当前元素的直接子元素
	    rank = country.find('rank').text
	    # Element.find()查找具有特定标记的第一个子项
	    #Element.text访问该元素的文本内容
	    name = country.get('name')
	    # Element.get()访问元素的属性
	    print(name,rank)
##7.面向对象
- 定义类的第一个函数参数必须有self
- 类对象指针，创建类的对象，有一个指向类的指针
- self代指调用方法对象

构造方法：创建类对象时自动调用构造方法__init__()

	class Bar:
	    def __init__(self,name):
			#self.name为字段
	        self.name1 = name
	    def foo(self):
	        print(self.name1)
	z = Bar('lcscim')
	print(z.name1)
	z.foo()
###7.1继承：
- 简单表示
		class F:
		    def f1(self):
		        print('F.f1')
		    def f2(self):
		        print('F.f2')
		
		class S(F):
		    def s1(self):
		        print('S.s1')
		    def s2(self):
		        print('S.s2')
		s = S()
		s.s1()
		s.f1()
- 重写父类方法

		class F:
		    def f1(self):
		        print('F.f1')
		    def f2(self):
		        print('F.f2')
		
		class S(F):
		    def s1(self):
		        print('S.s1')
		    def f1(self):
		        print('S.f1')
		s = S()
		s.s1()
		s.f1()
		s.f2()
- super访问父类方法

	- super(子类，self).父类中的方法（）
	- 父类名.父类中的方法（self，。。。）

		class F:
		    def f1(self):
		        print('F.f1')
		    def f2(self):
		        print('F.f2')
		
		class S(F):
		    def s1(self):
		        print('S.s1')
		    def f1(self):
		        super(S,self).f2()
		        #super访问父类方法，第一个参数为当前类，第二个为self
		        print('S.f1')
		        F.f2(self)#也可访问父类f2方法，建议第一种super
		s = S()
		s.s1()
		s.f1()
- 支持多继承

	- 左侧优先
	- 一条道走到黑
	- 同一个基类，基类最后执行

- 多态，Python原生多态

#9.12

##1.类字段
	class Bar:
	    def __init__(self,name):
			#self.name为字段
	        self.name1 = name
	    def foo(self):
	        print(self.name1)
- 普通字段，保存在对象中，执行只能通过对象访问
- 静态字段，保存在类中，执行可以通过对象访问也可通过类访问

	class Bar:
		#静态字段
		country = 'china'
	    def __init__(self,name):
			#self.name为字段 普通字段
	        self.name1 = name
##2.类方法
- 普通方法 保存在类中由对象调用，self表示对象
- 静态方法 可通过类名.直接调用

		class Foo:
		    def bar(self):
		        print('bar')
		
		    @staticmethod
		    def sta():
		        print('static')
		
		    @staticmethod
		    #静态方法前都有@staticmethod标识
		    def sta2(x,y):
		        print(x,y)
		Foo.sta()
		#静态方法
		Foo.sta2(1,2)
		#带有参数的静态方法
		foo = Foo()
		foo.bar()
		#非静态方法
- 类方法 保存在类中由类直接调用，cls表示当前类。类方法是静态方法的变种

	class Foo:
	    def bar(self):
	        print('bar')
	    @staticmethod
	    def sta():
	        print('static')
	    @staticmethod
	    #静态方法前都有@staticmethod标识
	    def sta2(x,y):
	        print(x,y)
	    #类方法前都有@classmethod标识
	    @classmethod
	    def classmd(cls):
	        print(cls)
	        print('classmethod')
	
	Foo.classmd()
	Foo.sta()
应用场景：如果对象中需要保存一些值，执行某些功能时，需要使用对象中的值，用普通方法

不需要任何对象的值，静态方法
##3.成员修饰符

- 公有成员 外部可以访问
- 私有成员 外部不可访问，在名称前加两个下划线

私有变量
		class Foo:
		    def __init__(self,name,age):
		        self.name = name
		        #self.age = age
		        #变量名前加‘__’表示私有变量，外部无法直接访问
		        self.__age = age
		    def shou(self):#内部可以访问__age
		        return self.__age
		
		foo = Foo('lcscim',52)
		print(foo.name)
		#print(foo.__age) 无法直接访问
		print(foo.shou())

		class Foo:
		    __age = 21
		    def __init__(self):
		        pass
		    def sta(self):
		        return Foo.__age
		    @staticmethod
		    def stat():
		        return Foo.__age
		foo = Foo().sta()
		print(foo)
		fo = Foo.stat()
		print(fo)
私有方法

	class Foo:
	    def __f1(self):
	        return 123
	    def f2(self):
	        return self.__f1()
	
	print(Foo().f2())
注意:继承无法访问父类的私有方法
##4.特殊成员
在创建类对象后再加一个括号即可访问__call__方法
		class Foo:
		    def __init__(self):
		        print('1')
		    def __call__(self, *args, **kwargs):
		        print('2')
		Foo()()
- __init__  类()自动执行
- __del__   析构方法 对象不再使用时由解释器自动在内存中进行销毁
- __call__  对象() 或 类()()自动执行
- __int__   int(对象)
- __str__   str(对象)

		class Foo:
		    def __init__(self):
		        pass
		    def __str__(self):
		        return 'lcscim'
		print(str(Foo()))
- __add__   对象相加时调用，其余运算方法类似
- __dict__  将对象中所有封装的内容以字典形式返回，如果是对象名.__dict__返回对象的成员，如果是类返回类的成员

		class Foo:
		    def __init__(self,name,age):
		        self.name = name
		        self.age = age
		
		foo = Foo('lcscim',25)
		d = foo.__dict__
		print(d)
	返回
		{'name': 'lcscim', 'age': 25}
- __getitem__ #通过对象[]获取值，其余类似
- __setitem__
- __delitem__

		class Foo:
		    def __init__(self,name,age):
		        self.name = name
		        self.age = age
		    def __getitem__(self, item):
		        
		        return item
		    def __setitem__(self, key, value):
		        print(key,value)
		    def __delitem__(self, key):
		        print(key)
		
		foo = Foo('lcscim',25)
		foo[8]
		foo[9] = 123
		del foo[10]
- __iter__ 如果类中有该方法，表示创建的对象可迭代，__iter__的返回值是一个迭代器

		class Foo:
		    def __init__(self,name,age):
		        self.name = name
		        self.age = age
		    def __iter__(self):
		        return iter([11,22,33,44])
		
		foo = Foo('lcscim',52)
		for i in foo:
		    print(i)
##5.类执行过程
- Python的一切事物都是对象
- 所有的类都是type对象
- 创建类对象时首先执行type的init方法，在执行type的call方法，在执行类的init方法

##6.异常处理
assert（断言），当跟在assert后的条件为假的时候，程序自动崩溃并抛出AssertionError异常，常用在确保程序某个条件一定为真时才让程序正常工作的情况下

try-except语句，语法：

	try：
		检测范围
	except Exception[as reason]:	//Exception是异常名，reason是指异常信息，
		c出现异常(Exception)后的处理代码
	finally：
		无论如何都会被执行的代码
	例如：
	try:
		f = open('nofile.txt')
		print(f.read())
		f.close()
	except OSError as reason:
		print('出错了，原因是：'+str(reason))

raise语句引发异常,主动触发异常

	raise [异常名（'要显示异常的具体信息'）]
##7.反射
通过字符串的形式操作对象中的成员：

- getattr
- hasattr
- setattr
- delattr

		class Foo:
		    def __init__(self,name,age):
		        self.name = name
		        self.age = age
		    def show(self):
		        return '%s-%s'%(self.name,self.age)
		
		foo = Foo('lcscim',52)
		print(getattr(foo,'name'))
		print(hasattr(foo,'name'))
		print(getattr(foo,'show'))
		print(setattr(foo,'name','laochang'))
		print(foo.name)
反射在模块中也可以使用

示例：

	#模块
	def f1():
	    print('你好')
	def f2():
	    print('我好')
	def f3():
	    print('大家好')
	#引用
	import s2
	
	inp = input('请输入')
	if hasattr(s2,inp):
	    foo = getattr(s2,inp)
	    foo()
	else:
	    print('404')

#9.16

##1.单例模式
单例，永远使用同一个实例。

	class Foo:
	    def __init__(self,name,age):
	        self.name = name
	        self.age = age
	    def show(self):
	        print(self.name,self.age)
	v = None
	while True:
	    if v:
	        v.show()
	    else:
	        v=Foo('lcscim',18)
	        v.show()
单列模式：

	class Foo:
	    __v = None
	    @classmethod
	    def get_v(cls):
	        if cls.__v:
	            return cls.__v
	        else:
	            cls.__v = Foo()
	            return cls.__v
	obj = Foo.get_v()
	print(obj)
	obj1 = Foo.get_v()
	print(obj1)
	#创建的两个对象指向同一个内存

#9.30

##1.动态导入模块
需要importlib模块。比如：
	
	#分别为模块名和参数
	module = 'src.userinfo'
	func = 'add'
	#通过反射的方式获取
	import importlib
	m = importlib.import_module(module)
	fun = getattr(m,func)
	func()
