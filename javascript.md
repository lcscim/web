#10.5
https://www.cnblogs.com/yuanchenqi/articles/5980312.html

##1.JavaScript概述 
- JavaScript的历史

	- 1992年Nombas开发出C-minus-minus(C--)的嵌入式脚本语言(最初绑定在CEnvi软件中).后将其改名ScriptEase.(客户端执行的语言)
	- Netscape(网景)接收Nombas的理念,(Brendan Eich)在其Netscape Navigator 2.0产品中开发出一套livescript的脚本语言.Sun和Netscape共同完成.后改名叫Javascript
	- 微软随后模仿在其IE3.0的产品中搭载了一个JavaScript的克隆版叫Jscript.
	- 为了统一三家,ECMA(欧洲计算机制造协会)定义了ECMA-262规范.国际标准化组织及国际电工委员会（ISO/IEC）也采纳 ECMAScript 作为标准（ISO/IEC-16262）。从此，Web 浏览器就开始努力（虽然有着不同的程度的成功和失败）将 ECMAScript 作为 JavaScript 实现的基础。EcmaScript是规范.
- ECMAScript  
	
	尽管 ECMAScript 是一个重要的标准，但它并不是 JavaScript 唯一的部分，当然，也不是唯一被标准化的部分。实际上，一个完整的 JavaScript 实现是由以下 3 个不同部分组成的：
	
	- 核心（ECMAScript） 
	- 文档对象模型（DOM） Document object model (整合js，css，html)
	- 浏览器对象模型（BOM） Broswer object model（整合js和浏览器）
	- Javascript 在开发中绝大多数情况是基于对象的.也是面向对象的. 
	![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161023211134529-32650400.png)
	简单地说，ECMAScript 描述了以下内容：
	
	- 语法 
	- 类型 
	- 语句 
	- 关键字 
	- 保留字 
	- 运算符 
	- 对象 (封装 继承 多态) 基于对象的语言.使用对象.
- JavaScript的引入方式

	{#1 直接编写#}
	    <script>
	        alert('hello yuan')
	    </script>
	{#2 导入文件#}
	    <script src="hello.js"></script>　　
##2. JavaScript的基础
###2.1变量
	x=5
	y=6
	z=x+y
在代数中，我们使用字母（比如 x）来保存值（比如 5）。

通过上面的表达式 z=x+y，我们能够计算出 z 的值为 11。

在 JavaScript 中，这些字母被称为变量。

0 变量是弱类型的(很随便)；

1 声明变量时不用声明变量类型. 全都使用var关键字;

	var a;
2 一行可以声明多个变量.并且可以是不同类型.

	var name="yuan", age=20, job="lecturer";
3 (了解) 声明变量时 可以不用var. 如果不用var 那么它是全局变量.

4 变量命名,首字符只能是字母,下划线,$美元符 三选一，且区分大小写，x与X是两个变量

5 变量还应遵守以下某条著名的命名规则：


	Camel 标记法
	首字母是小写的，接下来的字母都以大写字符开头。例如：
	var myTestValue = 0, mySecondValue = "hi";
	Pascal 标记法
	首字母是大写的，接下来的字母都以大写字符开头。例如：
	Var MyTestValue = 0, MySecondValue = "hi";
	匈牙利类型标记法
	在以 Pascal 标记法命名的变量前附加一个小写字母（或小写字母序列），说明该变量的类型。例如，i 表示整数，s 表示字符串，如下所示“
	Var iMyTestValue = 0, sMySecondValue = "hi";

注意：

    function func1(){
        
        var a = 123;
        b=456
    }

    func1();
    
	//    alert(a);
	//    alert(b);
	// 不推荐
###2.2基础规范
1 每行结束可以不加分号. 没有分号会以换行符作为每行的结束

	a=1;b=2;
	a=1 b=2;------错误
	
	a=1
	b=2
	
	//推荐
	a=1;
	b=2;
	
	{
	 a=1;
	 b=2;
	    //推荐加tab
	    a=1;
	    b=2;
	}

2 注释 支持多行注释和单行注释. /* */  //

3 使用{}来封装代码块
###2.3常量和标识符
常量 ：直接在程序中出现的数据值

标识符：

- 由不以数字开头的字母、数字、下划线(_)、美元符号($)组成
- 常用于表示函数、变量等的名称
- 例如：_abc,$abc,abc,abc123是标识符，而1abc不是
- JavaScript语言中代表特定含义的词称为保留字，不允许程序再定义为标识符

![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020152532717-389530735.png)
![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020153916560-1468649784.png)
###2.4 数据类型
![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161023225846513-154917493.png)
![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161023224930873-196677017.png)
- 数字类型(Number)
	
	简介
	最基本的数据类型
	不区分整型数值和浮点型数值
	所有数字都采用64位浮点格式存储，相当于Java和C语言中的double格式
	能表示的最大值是±1.7976931348623157 x 10308 
	能表示的最小值是±5 x 10 -324 
	   整数：
	           在JavaScript中10进制的整数由数字的序列组成
	           精确表达的范围是 -9007199254740992 (-253) 到 9007199254740992 (253)
	           超出范围的整数，精确度将受影响
	  浮点数：
	           使用小数点记录数据
	           例如：3.4，5.6
	           使用指数记录数据
	           例如：4.3e23 = 4.3 x 1023
	
	  16进制和8进制数的表达
	           16进制数据前面加上0x，八进制前面加0
	           16进制数是由0-9,A-F等16个字符组成
	           8进制数由0-7等8个数字组成
	           16进制和8进制与2进制的换算
	
	# 2进制: 1111 0011 1101 0100   <-----> 16进制:0xF3D4 <-----> 10进制:62420
	# 2进制: 1 111 001 111 010 100 <-----> 8进制:0171724
- 字符串(String)

	简介
	是由Unicode字符、数字、标点符号组成的序列
	字符串常量首尾由单引号或双引号括起
	JavaScript中没有字符类型
	常用特殊字符在字符串中的表达
	字符串中部分特殊字符必须加上右划线\
	常用的转义字符 \n:换行  \':单引号   \":双引号  \\:右划线
	
	String数据类型的使用
	
		- 特殊字符的使用方法和效果
		- Unicode的插入方法
	
	<script>
	        var str="\u4f60\u597d\n欢迎来到\"JavaScript世界\"";
	        alert(str);
	</script>
- 布尔型(Boolean)

	简介
	Boolean类型仅有两个值：true和false，也代表1和0，实际运算中true=1,false=0
	布尔值也可以看作on/off、yes/no、1/0对应true/false
	Boolean值主要用于JavaScript的控制语句，例如
	    if (x==1){
	    y=y+1;
	    }else    {
	    y=y-1;
	    }

- Null & Undefined

	Undefined 类型
	
	Undefined 类型只有一个值，即 undefined。当声明的变量未初始化时，该变量的默认值是 undefined。
	
	当函数无明确返回值时，返回的也是值 "undefined";
	
	Null 类型
	
	另一种只有一个值的类型是 Null，它只有一个专用值 null，即它的字面量。值 undefined 实际上是从值 null 派生来的，因此 ECMAScript 把它们定义为相等的。
	
	尽管这两个值相等，但它们的含义不同。undefined 是声明了变量但未对其初始化时赋予该变量的值，null 则用于表示尚未存在的对象（在讨论 typeof 运算符时，简单地介绍过这一点）。如果函数或方法要返回的是对象，那么找不到该对象时，返回的通常是 null。
	
	var person=new Person()
	
	var person=null
	

- 数据类型转换

	JavaScript属于松散类型的程序语言
	变量在声明的时候并不需要指定数据类型
	变量只有在赋值的时候才会确定数据类型
	表达式中包含不同类型数据则在计算过程中会强制进行类别转换
	
	数字 + 字符串：数字转换为字符串
	
	数字 + 布尔值：true转换为1，false转换为0
	
	字符串 + 布尔值：布尔值转换为字符串true或false


- 强制类型转换函数

	函数parseInt：   强制转换成整数   例如parseInt("6.12")=6  ; parseInt(“12a")=12 ; parseInt(“a12")=NaN ;parseInt(“1a2")=1
	#当字符串转为数字失败时显示NaN属于number。nan在表达式中结果一定为false除了不等于！= 
	
	函数parseFloat： 强制转换成浮点数  parseFloat("6.12")=6.12
	
	函数eval：       将字符串强制转换为表达式并返回结果 eval("1+1")=2 ; eval("1<2")=true
- 类型查询函数(typeof)
	
	ECMAScript 提供了 typeof 运算符来判断一个值是否在某种类型的范围内。可以用这种运算符判断一个值是否表示一种原始类型：如果它是原始类型，还可以判断它表示哪种原始类型。
	
	函数typeof ：查询数值当前类型  (string / number / boolean / object )
	
	例如typeof("test"+3)      "string"
	例如typeof(null)          "object "
	例如typeof(true+1)        "number"
	例如typeof(true-false)    "number"
##3.ECMAScript 运算符
###3.1ECMAScript 算数运算符
加(＋)、 减(－)、 乘(*) 、除(/) 、余数(% )  加、减、乘、除、余数和数学中的运算方法一样  例如：9/2=4.5，4*5=20，9%2=1

-除了可以表示减号还可以表示负号  例如：x=-y

+除了可以表示加法运算还可以用于字符串的连接  例如："abc"+"def"="abcdef"
 递增(＋＋) 、递减(－－)

假如x=2，那么x++表达式执行后的值为3，x--表达式执行后的值为1
i++相当于i=i+1，i--相当于i=i-1
递增和递减运算符可以放在变量前也可以放在变量后：--i
    
var i=1;
console.log(i++);
console.log(++i);
console.log(i--);
console.log(--i);
# i++先赋值后加，++i先加减后赋值

一元加减法：

    var a=1;
    var b=1;
    a=-a;  //a=-1

    var c="10";
    alert(typeof (c));
    c=+c;    //类型转换
    alert(typeof (c));
    -------------------
    var d="yuan";
    d=+d;
    alert(d);//NaN:属于Number类型的一个特殊值,当遇到将字符串转成数字无效时,就会得到一个NaN数据
    alert(typeof(d));//Number

    //NaN特点:
    
    var n=NaN;
    
    alert(n>3);
    alert(n<3);
    alert(n==3);
    alert(n==NaN);
    
    alert(n!=NaN);//NaN参与的所有的运算都是false,除了!=

###3.2ECMAScript 逻辑运算符

等于 ( == )  、不等于( != ) 、 大于( > ) 、 小于( < )  大于等于(>=) 、小于等于(<=)
与 (&&) 、或(||) 、非(!)
1 && 1 = 1  1 || 1 = 1
1 && 0 = 0  1 || 0 = 1
0 && 0 = 0  0 || 0 = 0

!0=1
!1=0

逻辑 AND 运算符(&&)
逻辑 AND 运算的运算数可以是任何类型的，不止是 Boolean 值。

如果某个运算数不是原始的 Boolean 型值，逻辑 AND 运算并不一定返回 Boolean 值：

如果某个运算数是 null，返回 null。 
如果某个运算数是 NaN，返回 NaN。 
如果某个运算数是 undefined，返回undefined。 
逻辑 OR 运算符(||)
与逻辑 AND 运算符相似，如果某个运算数不是 Boolean 值，逻辑 OR 运算并不一定返回 Boolean 值

###3.3ECMAScript 赋值运算符

赋值 = 
JavaScript中=代表赋值，两个等号==表示判断是否相等
例如，x=1表示给x赋值为1
if (x==1){...}程序表示当x与1相等时
if(x==“on”){…}程序表示当x与“on”相等时
 配合其他运算符形成的简化表达式
例如i+=1相当于i=i+1，x&=y相当于x=x&y

实例：              

2 == “2”        
2 === “2”        
4 != “4”            
4 !== “4”        

var a = 2; var b = 4;
var c = a<b | --b>--a;
var c = a<b || --b>--a; 
 var c = a<b &&--b>--a;
var c = a<b & --b>--a; 

###3.4ECMAScript等性运算符
执行类型转换的规则如下：

如果一个运算数是 Boolean 值，在检查相等性之前，把它转换成数字值。false 转换成 0，true 为 1。 
如果一个运算数是字符串，另一个是数字，在检查相等性之前，要尝试把字符串转换成数字。 
如果一个运算数是对象，另一个是字符串，在检查相等性之前，要尝试把对象转换成字符串。 
如果一个运算数是对象，另一个是数字，在检查相等性之前，要尝试把对象转换成数字。 
在比较时，该运算符还遵守下列规则：

值 null 和 undefined 相等。 
在检查相等性时，不能把 null 和 undefined 转换成其他值。 
如果某个运算数是 NaN，等号将返回 false，非等号将返回 true。 
如果两个运算数都是对象，那么比较的是它们的引用值。如果两个运算数指向同一对象，那么等号返回 true，否则两个运算数不等。 
![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161023233321013-877495606.png)   

###3.5 ECMAScript 关系运算符(重要)

var bResult = "Blue" < "alpha";
alert(bResult); //输出 true　　
在上面的例子中，字符串 "Blue" 小于 "alpha"，因为字母 B 的字符代码是 66，字母 a 的字符代码是 97。

比较数字和字符串

另一种棘手的状况发生在比较两个字符串形式的数字时，比如：

	var bResult = "25" < "3";
	alert(bResult); //输出 "true"
上面这段代码比较的是字符串 "25" 和 "3"。两个运算数都是字符串，所以比较的是它们的字符代码（"2" 的字符代码是 50，"3" 的字符代码是 51）。

不过，如果把某个运算数该为数字，那么结果就有趣了：

	var bResult = "25" < 3;
	alert(bResult); //输出 "false"
这里，字符串 "25" 将被转换成数字 25，然后与数字 3 进行比较，结果不出所料。

总结：

比较运算符两侧如果一个是数字类型,一个是其他类型,会将其类型转换成数字类型.
比较运算符两侧如果都是字符串类型,比较的是最高位的asc码,如果最高位相等,继续取第二位比较.
###3.6Boolean运算符(重要)

	var temp=new Object();// false;[];0; null; undefined;object(new Object();)
	
	    if(temp){
	        console.log("yuan")
	    }else {
	        console.log("alex")
	    }

全等号和非全等号

等号和非等号的同类运算符是全等号和非全等号。这两个运算符所做的与等号和非等号相同，只是它们在检查相等性前，不执行类型转换。

##4.控制语句
###4.1if 控制语句

	if-else基本格式
	if (表达式){
	语句１;
	......
	}else{
	语句２;
	.....
	}
	功能说明
	如果表达式的值为true则执行语句1,
	否则执行语句2
![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020163908654-382264302.png)
	var x= (new Date()).getDay();
	//获取今天的星期值，0为星期天
	var y;
	
	if ( (x==6) || (x==0) ) {
	y="周末";
	}else{
	y="工作日";
	}
	
	alert(y);
	
	//等价于
	
	y="工作日";
	if ( (x==6) || (x==0) ) {
	y="周末";
	}

if 可以单独使用

	if语句嵌套格式
	if (表达式1) {
	    语句1;
	}else if (表达式2){
	    语句2;
	}else if (表达式3){
	    语句3;
	} else{
	    语句4;
	}
![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020164919248-1127492807.png)
                    
	if (x==1){
	    y="星期一";
	}else if (x==2){
	    y="星期二";
	...
	}else if (x==6){
	    y="星期六";
	}else if (x==0){
	    y="星期日";
	}else{
	    y="未定义";

###4.2switch  选择控制语句

	switch基本格式
	switch (表达式) {
	    case 值1:语句1;break;
	    case 值2:语句2;break;
	    case 值3:语句3;break;
	    default:语句4;
	}

![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020165151420-915008211.png)
	
	switch(x){
	case 1:y="星期一";    break;
	case 2:y="星期二";    break;
	case 3:y="星期三";    break;
	case 4:y="星期四";    break;
	case 5:y="星期五";    break;
	case 6:y="星期六";    break;
	case 7:y="星期日";    break;
	default: y="未定义";
	}

switch比else if结构更加简洁清晰，使程序可读性更强,效率更高。

首先要看一个问题，if 语句适用范围比较广，只要是 boolean 表达式都可以用 if 判断；而 switch 只能对基本类型进行数值比较。两者的可比性就仅限在两个基本类型比较的范围内。
说到基本类型的数值比较，那当然要有两个数。然后重点来了——
if 语句每一句都是独立的，看下面的语句：
if (a == 1) ...
else if (a == 2) ...
这样 a 要被读入寄存器两次，1 和 2 分别被读入寄存器一次。于是你是否发现其实 a 读两次是有点多余的，在你全部比较完之前只需要一次读入寄存器就行了，其余都是额外开销。但是 if 语句必须每次都把里面的两个数从内存拿出来读到寄存器，它不知道你其实比较的是同一个 a。
于是 switch case 就出来了，把上面的改成 switch case 版本：
switch (a) {
        case 0:
                break;
        case 1:
}
                
总结:

1.switch用来根据一个整型值进行多路分支，并且编译器可以对多路分支进行优化
2.switch-case只将表达式计算一次,然后将表达式的值与每个case的值比较,进而选
  择执行哪一个case的语句块
3.if..else 的判断条件范围较广，每条语句基本上独立的，每次判断时都要条件加载
  一次。
所以在多路分支时用switch比if..else if .. else结构要效率高。

###4.3 for  循环控制语句

	for循环基本格式
	for (初始化;条件;增量){
	    语句1;
	    ...
	}
	功能说明
	实现条件循环，当条件成立时，执行语句1，否则跳出循环体
![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020165544795-930677647.png)

	for (var i=1;i<=7;i++){
	    document.write("<H"+i+">hello</H "+i+"> ");
	    document.write("<br>");
	}
	----------------------------------------------
	    var arr=[1,"hello",true]//var dic={"1":"111"}
	    for (var i in arr){
	        console.log(i)
	        console.log(arr[i])
	    }

注意：

    doms=document.getElementsByTagName("p");

    for (var i in doms){
       console.log(i); // 0 1 2 length item namedItem
       //console.log(doms[i])
    }

	//循环的是你获取的th一个DOM元素集，for in用来循环对象的所有属性，dom元素集包含了你上面输出的属性。
	//如果你只要循环dom对象的话，可以用for循环:
	
	    for (var i=0;i<doms.length;i++){
	        console.log(i) ; // 0 1 2
	        //console.log(doms[i])
	    }

结论：for i in 不推荐使用.

###4.4 while  循环控制语句

	while循环基本格式
	while (条件){
	语句1；
	...
	}
	功能说明
	运行功能和for类似，当条件成立循环执行语句花括号{}内的语句，否则跳出循环
![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020165834920-189719722.png)
	var i=1;
	while (i<=7) {
	    document.write("<H"+i+">hello</H "+i+"> ");
	    document.write("<br>");
	    i++;
	}
	//循环输出H1到H7的字体大小

	<script language="JavaScript">
	/* sayhello是定义的函数名，前面必须加上function和空格*/
	function sayHello(){
	    var hellostr;
	    var myname=prompt("请问您贵姓？","苑"); 
	    hellostr="您好，"+myname+'先生，欢迎进入"探索之旅"！';
	    alert(hellostr); 
	    document.write(hellostr);
	}
	 //这里是对前面定义的函数进行调用
	sayHello();
	</script>

练习：分别用for循环和while循环计算出1-100的和？

###4.5 异常处理

	try {
	    //这段代码从上往下运行，其中任何一个语句抛出异常该代码块就结束运行
	}
	catch (e) {
	    // 如果try代码块中抛出了异常，catch代码块中的代码就会被执行。
	    //e是一个局部变量，用来指向Error对象或者其他抛出的对象
	}
	finally {
	     //无论try中代码是否有异常抛出（甚至是try代码块中有return语句），finally代码块中始终会被执行。
	}
	注：主动抛出异常 throw Error('xxxx')　　
##5.其余见JavaScript 的基础学习()
- instanceof 查看变量类型是否与相应类型相同，相同返回TRUE

    var s ="hello";
    var i = 8;
    //typeof只能判断基本数据类型
    alert(typeof (s));
    alert(typeof (i));
    var s2 = new String("hello");
    alert(typeof (s2));
    alert(s2 instanceof String);
    var n = new Number(2);
    alert(typeof (n));
    alert(n instanceof String);
- trim（）方法去掉空格

##6.jQuery相关方法
http://jquery.cuishifeng.cn
- 滚动界面练习

	1. onscroll事件
	2. $(..).scrollTop() 获取匹配元素相对滚动条顶部的距离。
	3. 如何获取某个标签距离顶部的高度
	4. $(..).offset()    获取匹配元素在当前视口的相对偏移。返回的对象包含两个整型属性：top 和 left，以像素计
	5. $(..).height()	 永远获取自己的高度；	获取当前标签自己的高度
	6. $(..).innerHeight（） 永远获取自己的高度+padding，获取第一个元素内部区域的高度（包括补白不包括边框）。
	7. $(..).outHeight（）
		1. 参数1：false   永远获取自己的高度+padding+border
		2. 参数1：TRUE   永远获取自己的高度+padding+border+margin

- 加载

	1. ready()方法 。当DOM载入就绪可以查询及操纵时绑定一个要执行的函数。
	2. 在DOM中使用onload方法
	3. 在jQuery中onclick方法是click方法
	4. bind方法。为每个匹配元素的特定事件绑定事件处理函数。jQuery 3.0中已弃用此方法，请用 on()代替。
	5. .mouseover()表示鼠标放置在标签上
	6. .mousedown()表示鼠标点击下标签
	7. index()获取当前标签对象

- css样式

	- cursor属性指定鼠标图标在该标签上的样式，move值为十字形
	- show() 显示元素 参数是显示的时间
	- hide() 隐藏元素 。。。。。。。。
	- toggle() 显示和隐藏切换
	- fadein() 淡入   参数是时间
	- fadeout() 淡出
	- fadetoggle() 淡入淡出切换
	- fadeto() 淡入淡出切换 第一个参数是时间，第二个是透明度
	- slideDown() 通过高度变化（向下增大）来动态地显示所有匹配的元素，在显示完成后可选地触发一个回调函数。
	- slideDown() 向上收
	- slidetoggle() 向上或向下切换

- 自定义拓展方法方法

	- $.extend()	

		    $.extend({
		        getmax:function (a,b) {
		            return a<b?a:b;
		        }
		    });
			#必须使用该方法调用
		    alert($.getmax(5,8));
	- $.fn.extend()

		    $.fn.extend({
		        print:function () {
		
		            console.log($(this).html());
		        }
		    });
		    //获取当前标签的HTML内容
			#带有标签的使用标签调用
		    $("p").print();
	- 对拓展方法限定作用域
		#将方法放到自执行匿名函数中
		(function () {
		        $.fn.extend({
		            print:function () {
		                console.log($(this).html());
		            }
		        });
		    })();
		
		    $("p").print();



