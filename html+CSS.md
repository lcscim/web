#10.1
http://www.cnblogs.com/yuanchenqi/articles/5976755.html
##1.HTML
- 制作服务端

		import socket
		def main():
		    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		    sock.bind(('localhost',8089))
		    sock.listen(5)
		
		    while True:
		        connection, address = sock.accept()
		        buf = connection.recv(1024)
		        connection.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n","utf8"))
		        connection.sendall(bytes("<h1>Hello,World</h1>","utf8"))
		        connection.close()
		if __name__ == '__main__':
		    main()
	此时在浏览器上访问：localhost：8089即可获得
- HTML 是什么？

	htyper text markup language  即超文本标记语言
	超文本: 就是指页面内可以包含图片、链接，甚至音乐、程序等非文字元素。
	标记语言: 标记（标签）构成的语言.
	网页==HTML文档，由浏览器解析，用来展示的
	
	静态网页：静态的资源，如xxx.html
	动态网页：html代码是由某种开发语言根据用户请求动态生成的
	
	html文档树形结构图：![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161025132859984-662031019.png)
- 什么是标签

	- 是由一对尖括号包裹的单词构成 例如: <html> *所有标签中的单词不可能以数字开头.
	- 标签不区分大小写.<html> 和 <HTML>. 推荐使用小写.
	- 标签分为两部分: 开始标签<a> 和 结束标签</a>. 两个标签之间的部分 我们叫做标签体.
	- 有些标签功能比较简单.使用一个标签即可.这种标签叫做自闭和标签.例如: <br/> <hr/> <input /> <img />
	- 标签可以嵌套.但是不能交叉嵌套. <a><b></a></b>
- 标签的属性

	- 通常是以键值对形式出现的. 例如 name="alex"
	- 属性只能出现在开始标签 或 自闭和标签中.
	- 属性名字全部小写. *属性值必须使用双引号或单引号包裹 例如 name="alex"
	- 如果属性值和属性名完全一样.直接写属性名即可. 例如 readonly
- <!DOCTYPE html>标签

	由于历史的原因，各个浏览器在对页面的渲染上存在差异，甚至同一浏览器在不同版本中，对页面的渲染也不同。在
	W3C标准出台以前，浏览器在对页面的渲染上没有统一规范，产生了差异(Quirks mode或者称为Compatibility 
	Mode)；由于W3C标准的推出，浏览器渲染页面有了统一的标准(CSScompat或称为Strict mode也有叫做Standars
	mode)，这就是二者最简单的区别。
	      W3C标准推出以后，浏览器都开始采纳新标准，但存在一个问题就是如何保证旧的网页还能继续浏览，在标准出来以前，
	很多页面都是根据旧的渲染方法编写的，如果用的标准来渲染，将导致页面显示异常。为保持浏览器渲染的兼容性，使以
	前的页面能够正常浏览，浏览器都保留了旧的渲染方法（如：微软的IE）。这样浏览器渲染上就产生了Quircks mode
	和Standars mode，两种渲染方法共存在一个浏览器上。
	
	window.top.document.compatMode：
	//BackCompat：怪异模式，浏览器使用自己的怪异模式解析渲染页面。 
	//CSS1Compat：标准模式，浏览器使用W3C的标准解析渲染页面。
	       这个属性会被浏览器识别并使用，但是如果你的页面没有DOCTYPE的声明，那么compatMode默认就是BackCompat,
	
	这也就是恶魔的开始 -- 浏览器按照自己的方式解析渲染页面，那么，在不同的浏览器就会显示不同的样式。
	
	    如果你的页面添加了<!DOCTYPE html>那么，那么就等同于开启了标准模式，那么浏览器就得老老实实的按照W3C的
	
	标准解析渲染页面，这样一来，你的页面在所有的浏览器里显示的就都是一个样子了。
	
	这就是<!DOCTYPE html>的作用。
- <meta>

     meta标签的组成：meta标签共有两个属性，它们分别是http-equiv属性和name 属性，不同的属性又有不同的参数值，这些不同的参数值就实现了不同的网页功能。

    1: name属性主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的。     
		#用于搜索引擎发现网站关键词
		<meta name="keywords" content="meta总结,html meta,meta属性,meta跳转">	
		#用于在搜索界面显示当前网站的简要信息
		<meta name="description" content="老男孩培训机构是由一个老的男孩创建的">
    2: http-equiv顾名思义，相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确和精确地显示网页内容，与之对应的属性值为content，              content中的内容其实就是各个参数的变量值。   
		#如果未指定URL表明2秒后刷新当前页面，指定表明2秒后跳转到该页面
		<meta http-equiv="Refresh" content="2;URL=https://www.baidu.com"> //(注意后面的引号，分别在秒数的前面和网址的后面)

		<meta http-equiv="content-Type" charset=UTF8">

		<meta http-equiv = "X-UA-Compatible" content = "IE=EmulateIE7" />
	#注意：X-UA-Compatible 针对IE浏览器
	3.非meta标签
		#指定网站的标题即浏览器的标签页标题文字
	    <title>oldboy</title>
		#指定在浏览器标签页显示的图标
	    <link rel="icon" href="http://www.jd.com/favicon.ico">
		#链接外部的CSS样式
	    <link rel="stylesheet" href="css.css">
		#关联外部的js代码
	    <script src="hello.js"></script>　 
##1.1body标签
一 基本标签（块级标签和内联标签）

	<hn>: n的取值范围是1~6; 从大到小. 用来表示标题.
	<p>: 段落标签. 包裹的内容被换行.并且也上下内容之间有一行空白.
	<b> <strong>: 加粗标签.
	<strike>: 为文字加上一条中线.
	<em>: 文字变成斜体.
	<sup>和<sub>: 上角标 和 下角表.
	<br>:换行.
	<hr>:水平线
	<div><span>

	- 块级标签：<p><h1><table><ol><ul><form><div>
	
	- 内联标签：<a><input><img><sub><sup><textarea><span>
	
	block（块）元素的特点
		
		 总是在新行上开始；
		 宽度缺省是它的容器的100%，除非设定一个宽度。
		 它可以容纳内联元素和其他块元素
		
	inline元素的特点
		
		和其他元素都在一行上；
		宽度就是它的文字或图片的宽度，不可改变
		内联元素只能容纳文本或者其他内联元素
		
	特殊字符具体特殊字符可以搜索
		
	     &lt; &gt；&quot；&copy;&reg;
		<,>
二 图形标签: <img> 

	src: 要显示图片的路径.
	alt: 图片没有加载成功时的提示.
	title: 鼠标悬浮时的提示信息.
	width: 图片的宽
	height:图片的高 (宽高两个属性只用一个会自动等比缩放.)

三 超链接标签(锚标签)<a>

	href:要连接的资源路径 格式如下: href="http://www.baidu.com" 
	target: _blank : 在新的窗口打开超链接. 框架名称: 在指定框架中打开连接内容.
	name: 定义一个页面的书签.
	用于跳转 href : #id.（锚）
 
四 列表标签：

	<ul>: 无序列表
	<ol>: 有序列表
	     <li>:列表中的每一项.
	<dl>  定义列表
	     <dt> 列表标题
	     <dd> 列表项

五 表格标签: <table>

	border: 表格边框.
	cellpadding: 内边距
	cellspacing: 外边距.
	width: 像素 百分比.（最好通过css来设置长宽）
	<tr>: table row  每行
	     <th>: table head cell	标题列，效果是加粗
	     <td>: table data cell	数值列
	rowspan:  单元格竖跨多少行
	colspan:  单元格横跨多少列（即合并单元格）
	<th>: table header <tbody>(不常用): 为表格进行分区.

六 表单标签<form>
	表单用于向服务器传输数据。
	
	表单能够包含 input 元素，比如文本字段、复选框、单选框、提交按钮等等。
	
	表单还可以包含textarea、select、fieldset和 label 元素。

	1.表单属性

　　		HTML 表单用于接收不同类型的用户输入，用户提交表单时向服务器传输数据，从而实现用户与Web服务器的交互。表单标签, 要提交的所有内容都应该在该标签中.

            action: 表单提交到哪. 一般指向服务器端一个程序,程序接收到表单提交过来的数据（即表单元素值）作相应处理，比如https://www.sogou.com/web

            method: 表单的提交方式 post/get 默认取值 就是 get（信封）

                  get: 1.提交的键值对.放在地址栏中url后面. 2.安全性相对较差. 3.对提交内容的长度有限制.
                  post:1.提交的键值对 不在地址栏. 2.安全性相对较高. 3.对提交内容的长度理论上无限制.
                  get/post是常见的两种请求方式.

	2.表单元素

    <input>  标签的属性和对应值              

	type:    text 文本输入框
	
             password 密码输入框

             radio 单选框，属性name的值必须相同才能实现

             checkbox 多选框  

             submit 提交按钮            

             button 按钮(需要配合js使用.) button和submit的区别？
			 #button需要配合js代码使用用来触发某种效果，submit是用来提交数据

             file 提交文件：form表单需要加上属性enctype="multipart/form-data"   
	
	name:    表单提交项的键.注意和id属性的区别：name属性是和服务器通信时使用的名称；而id属性是浏览器端使用的名称，该属性主要是为了方便客户端编程，而在css和javascript中使用的
	value:   表单提交项的值.对于不同的输入类型，value 属性的用法也不同：
	
		type="button", "reset", "submit" - 定义按钮上的显示的文本
		type="text", "password", "hidden" - 定义输入字段的初始值
		type="checkbox", "radio", "image" - 定义与输入相关联的值　　
		checked:  radio 和 checkbox 默认被选中
		readonly: 只读. text 和 password
		disabled: 对所用input都好使.
	
	上传文件注意两点：
	
	 1 请求方式必须是post
	 2 enctype="multipart/form-data"
	 上传文件                 
	          <select> 下拉选标签属性
	
	
	          name:表单提交项的键.
	
	          size：选项个数
	
	          multiple：multiple 
	
	                 <option> 下拉选中的每一项 属性：
	
	                       value:表单提交项的值.   selected: selected下拉选默认被选中
	
	                 <optgroup>为每一项加上分组
	
	<textarea> 文本域              
	
		name:    表单提交项的键.
		cols:    文本域默认有多少列
		rows:    文本域默认有多少行
	<label>  实现点击姓名就可达到点击输入框的效果  
	
		<label for="www">姓名</label>
		<input id="www" type="text">

	<fieldset>	组合表单中的相关元素，标签将表单内容的一部分打包，生成一组相关表单的字段。
	当一组表单元素放到 <fieldset> 标签内时，浏览器会以特殊方式来显示它们，它们可能有特殊的边界、3D 效果，或者甚至可创建一个子表单来处理这些元素。

		<fieldset>
		    <legend>登录吧</legend>  该标签为 fieldset 元素定义标题。
		    <input type="text">
		</fieldset>

#10.2
https://www.cnblogs.com/yuanchenqi/articles/6000358.html
##1.HTTP协议
###1.1 HTTP概述

HTTP（hypertext transport protocol），即超文本传输协议。这个协议详细规定了浏览器和万维网服务器之间互相通信的规则。

HTTP就是一个通信规则，通信规则规定了客户端发送给服务器的内容格式，也规定了服务器发送给客户端的内容格式。其实我们要学习的就是这个两个格式！客户端发送给服务器的格式叫“请求协议”；服务器发送给客户端的格式叫“响应协议”。

特点：

	HTTP叫超文本传输协议，基于请求/响应模式的！
	HTTP是无状态协议。
URL：统一资源定位符，就是一个网址：协议名://域名:端口/路径，例如：http://www.oldboy.cn:80/index.html
###1.2 请求协议
请求协议的格式如下：

请求首行；  // 请求方式 请求路径 协议和版本，例如：GET /index.html HTTP/1.1
请求头信息；// 请求头名称:请求头内容，即为key:value格式，例如：Host:localhost
空行；     // 用来与请求体分隔开
请求体。   // GET没有请求体，只有POST有请求体。
浏览器发送给服务器的内容就这个格式的，如果不是这个格式服务器将无法解读！在HTTP协议中，请求有很多请求方法，其中最为常用的就是GET和POST。不同的请求方法之间的区别，后面会一点一点的介绍。

1. GET请求

	HTTP默认的请求方法就是GET
	     * 没有请求体
	     * 数据必须在1K之内！
	     * GET请求数据会暴露在浏览器的地址栏中
	
	GET请求常用的操作：
	       1. 在浏览器的地址栏中直接给出URL，那么就一定是GET请求
	       2. 点击页面上的超链接也一定是GET请求
	       3. 提交表单时，表单默认使用GET请求，但可以设置为POST
		#告诉服务器支持那种方式
		Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
		#指定数据压缩方式
		Accept-Encoding:gzip, deflate, sdch
		#接受语言
		Accept-Language:zh-CN,zh;q=0.8
		#设置缓存
		Cache-Control:no-cache
		Connection:keep-alive
		Cookie:csrftoken=z5H43ZwARx7AIJ82OEizBOWbsAQA2LPk
		#发送目标位置
		Host:127.0.0.1:8090
		Pragma:no-cache
		Upgrade-Insecure-Requests:1
		#当前浏览器信息
		User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36
		Name
		login/
		1 requests ❘ 737 B transferred ❘ Finish: 5 ms ❘ DOMContentLoaded: 14 ms ❘ Load: 14 ms

	- GET 127.0.0.1:8090/login  HTTP/1.1：GET请求，请求服务器路径为  127.0.0.1:8090/login ，协议为1.1；
	- Host:localhost：请求的主机名为localhost；
	- *User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0：与浏览器和OS相关的信息。有些网站会显示用户的系统版本和浏览器版本信息，这都是通过获取User-Agent头信息而来的；
	- Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8：告诉服务器，当前客户端可以接收的文档类型，其实这里包含了*/*，就表示什么都可以接收；
	- Accept-Language: zh-cn,zh;q=0.5：当前客户端支持的语言，可以在浏览器的工具选项中找到语言相关信息；
	- Accept-Encoding: gzip, deflate：支持的压缩格式。数据在网络上传递时，可能服务器会把数据压缩后再发送；
	- Accept-Charset: GB2312,utf-8;q=0.7,*;q=0.7：客户端支持的编码；
	- Connection: keep-alive：客户端支持的链接方式，保持一段时间链接，默认为3000ms；
	- Cookie: JSESSIONID=369766FDF6220F7803433C0B2DE36D98：因为不是第一次访问这个地址，所以会在请求中把上一次服务器响应中发送过来的Cookie在请求中一并发送去过；这个Cookie的名字为JSESSIONID。

	#注意
	HTTP无状态：无状态是指协议对于事务处理没有记忆能力，服务器不知道客户端是什么状态。从另一方面讲，打开一个服务器上的网页
	和你之前打开这个服务器上的网页之间没有任何联系
	如果你要实现一个购物车，需要借助于Cookie或Session或服务器端API（如NSAPI and ISAPI）记录这些信息，请求服务器结算页面时同时将这些信息提交到服务器
	当你登录到一个网站时，你的登录状态也是由Cookie或Session来“记忆”的，因为服务器并不知道你是否登录
	优点：服务器不用为每个客户端连接分配内存来记忆大量状态，也不用在客户端失去连接时去清理内存，以更高效地去处理WEB业务
	缺点：客户端的每次请求都需要携带相应参数，服务器需要处理这些参数
	
	容易犯的误区：
	1、HTTP是一个无状态的面向连接的协议，无状态不代表HTTP不能保持TCP连接，更不能代表HTTP使用的是UDP协议（无连接）
	2、从HTTP/1.1起，默认都开启了Keep-Alive，保持连接特性，简单地说，当一个网页打开完成后，客户端和服务器之间用于传输
	HTTP数据的TCP连接不会关闭，如果客户端再次访问这个服务器上的网页，会继续使用这一条已经建立的连接
	3、Keep-Alive不会永久保持连接，它有一个保持时间，可以在不同的服务器软件（如Apache）中设定这个时间
2. POST请求

	(1). 数据不会出现在地址栏中
	(2). 数据的大小没有上限
	(3). 有请求体
	(4). 请求体中如果存在中文，会使用URL编码！

		username=%E5%BC%A0%E4%B8%89&password=123

	我们都知道Http协议中参数的传输是"key=value"这种简直对形式的，如果要传多个参数就需要用“&”符号对键值对进行分割。如"?name1=value1&name2=value2"，这样在服务端在收到这种字符串的时候，会用“&”分割出每一个参数，然后再用“=”来分割出参数值。

 

	针对“name1=value1&name2=value2”我们来说一下客户端到服务端的概念上解析过程: 
  	上述字符串在计算机中用ASCII吗表示为： 
	  6E616D6531 3D 76616C756531 26 6E616D6532 3D 76616C756532。 
	   6E616D6531：name1 
	   3D：= 
	   76616C756531：value1 
	   26：&
	   6E616D6532：name2 
	   3D：= 
	   76616C756532：value2 
	   服务端在接收到该数据后就可以遍历该字节流，首先一个字节一个字节的吃，当吃到3D这字节后，服务端就知道前面吃得字节表示一个key，再想后吃，如果遇到26，说明从刚才吃的3D到26子节之间的是上一个key的value，以此类推就可以解析出客户端传过来的参数。

	   现在有这样一个问题，如果我的参数值中就包含=或&这种特殊字符的时候该怎么办。 
	比如说“name1=value1”,其中value1的值是“va&lu=e1”字符串，那么实际在传输过程中就会变成这样“name1=va&lu=e1”。我们的本意是就只有一个键值对，但是服务端会解析成两个键值对，这样就产生了奇异。

	如何解决上述问题带来的歧义呢？解决的办法就是对参数进行URL编码 
	   URL编码只是简单的在特殊字符的各个字节前加上%，例如，我们对上述会产生奇异的字符进行URL编码后结果：“name1=va%26lu%3D”，这样服务端会把紧跟在“%”后的字节当成普通的字节，就是不会把它当成各个参数或键值对的分隔符。

	使用表单可以发POST请求，但表单默认是GET
	
		<form action="" method="post">
		  关键字：<input type="text" name="keyword"/>
		  <input type="submit" value="提交"/>
		</form>
	输入yuan后点击提交，查看请求内容如下：

		Request Headers
		Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
		Accept-Encoding:gzip, deflate
		Accept-Language:zh-CN,zh;q=0.8
		Cache-Control:no-cache
		Connection:keep-alive
		Content-Length:13
		Content-Type:application/x-www-form-urlencoded
		Cookie:csrftoken=z5H43ZwARx7AIJ82OEizBOWbsAQA2LPk
		Host:127.0.0.1:8090
		Origin:http://127.0.0.1:8090
		Pragma:no-cache
		Referer:http://127.0.0.1:8090/login/
		Upgrade-Insecure-Requests:1
		User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) 
		           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36

		Form Data
		username:yuan

	POST请求是可以有体的，而GET请求不能有请求体。

	- Referer: http://localhost:8080/hello/index.jsp：请求来自哪个页面，例如你在百度上点击链接到了这里，那么Referer:http://www.baidu.com；如果你是在浏览器的地址栏中直接输入的地址，那么就没有Referer这个请求头了；
	- Content-Type: application/x-www-form-urlencoded：表单的数据类型，说明会使用url格式编码数据；url编码的数据都是以“%”为前缀，后面跟随两位的16进制。
	- Content-Length:13：请求体的长度，这里表示13个字节。
	- keyword=hello：请求体内容！hello是在表单中输入的数据，keyword是表单字段的名字。

	Referer请求头是比较有用的一个请求头，它可以用来做统计工作，也可以用来做防盗链。
	统计工作：我公司网站在百度上做了广告，但不知道在百度上做广告对我们网站的访问量是否有影响，那么可以对每个请求中的Referer进行分析，如果Referer为百度的很多，那么说明用户都是通过百度找到我们公司网站的。
	防盗链：我公司网站上有一个下载链接，而其他网站盗链了这个地址，例如在我网站上的index.html页面中有一个链接，点击即可下载JDK7.0，但有某个人的微博中盗链了这个资源，它也有一个链接指向我们网站的JDK7.0，也就是说登录它的微博，点击链接就可以从我网站上下载JDK7.0，这导致我们网站的广告没有看，但下载的却是我网站的资源。这时可以使用Referer进行防盗链，在资源被下载之前，我们对Referer进行判断，如果请求来自本网站，那么允许下载，如果非本网站，先跳转到本网站看广告，然后再允许下载。
###1.3响应内容
响应协议的格式如下：

	响应首行；
	响应头信息；
	空行；
	响应体。
响应内容是由服务器发送给浏览器的内容，浏览器会根据响应内容来显示。遇到<img src=''>会开一个新的线程加载，所以有时图片多的话，内容会先显示出来，然后图片才一张张加载出来。

	Request URL:http://127.0.0.1:8090/login/
	Request Method:GET
	Status Code:200 OK
	Remote Address:127.0.0.1:8090
	Response Headers
	view source
	Content-Type:text/html; charset=utf-8
	Date:Wed, 26 Oct 2016 06:48:50 GMT
	Server:WSGIServer/0.2 CPython/3.5.2
	X-Frame-Options:SAMEORIGIN
	
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	</head>
	<body>
	<form action="/login/" method="post">
	  用户名：<input type="text" name="username"/>
	  <input type="submit" value="提交"/>
	</form>    
	</body>
	</html>

- HTTP/1.1 200 OK：响应协议为HTTP1.1，状态码为200，表示请求成功，OK是对状态码的解释；
- Server:WSGIServer/0.2 CPython/3.5.2：服务器的版本信息；
- Content-Type: text/html;charset=UTF-8：响应体使用的编码为UTF-8；
- Content-Length: 724：响应体为724字节；
- Set-Cookie: JSESSIONID=C97E2B4C55553EAB46079A4F263435A4; Path=/hello：响应给客户端的Cookie；
- Date: Wed, 25 Sep 2012 04:15:03 GMT：响应的时间，这可能会有8小时的时区差；
3.2　状态码
响应头对浏览器来说很重要，它说明了响应的真正含义。例如200表示响应成功了，302表示重定向，这说明浏览器需要再发一个新的请求。

- 200：请求成功，浏览器会把响应体内容（通常是html）显示在浏览器中；
- 404：请求的资源没有找到，说明客户端错误的请求了不存在的资源；
- 500：请求资源找到了，但服务器内部出现了错误；
- 302：重定向，当响应码为302时，表示服务器要求浏览器重新再发一个请求，服务器会发送一个响应头Location，它指定了新请求的URL地址；
- 304：

	当用户第一次请求index.html时，服务器会添加一个名为Last-Modified响应头，这个头说明了
	index.html的最后修改时间，浏览器会把index.html内容，以及最后响应时间缓存下来。当用户第
	二次请求index.html时，在请求中包含一个名为If-Modified-Since请求头，它的值就是第一次请
	求时服务器通过Last-Modified响应头发送给浏览器的值，即index.html最后的修改时间，
	If-Modified-Since请求头就是在告诉服务器，我这里浏览器缓存的index.html最后修改时间是这个,
	您看看现在的index.html最后修改时间是不是这个，如果还是，那么您就不用再响应这个index.html
	内容了，我会把缓存的内容直接显示出来。而服务器端会获取If-Modified-Since值，与index.html
	的当前最后修改时间比对，如果相同，服务器会发响应码304，表示index.html与浏览器上次缓存的相
	同，无需再次发送，浏览器可以显示自己的缓存页面，如果比对不同，那么说明index.html已经做了修
	改，服务器会响应200。

	![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161026162455218-1166783413.png)	
         
3.3　其他响应头

告诉浏览器不要缓存的响应头：

- Expires: -1；
- Cache-Control: no-cache；
- Pragma: no-cache；
自动刷新响应头，浏览器会在3秒之后请求http://www.baidu.com：

- Refresh: 3;url=http://www.baidu.com 
3.4　HTML中指定响应头

在HTMl页面中可以使用<meta http-equiv="" content="">来指定响应头，例如在index.html页面中给出<meta http-equiv="Refresh" content="3;url=http://www.baidu.com">，表示浏览器只会显示index.html页面3秒，然后自动跳转到http://www.baidu.com.

##2.CSS协议
https://www.cnblogs.com/yuanchenqi/articles/5977825.html

CSS是Cascading Style Sheets的简称，中文称为层叠样式表，用来控制网页数据的表现，可以使网页的表现与数据内容分离。
##2.1css的四种引入方式
1. 行内式
	
	行内式是在标记的style属性中设定CSS样式。这种方式没有体现出CSS的优势，不推荐使用。
	<p style="background-color: rebeccapurple">hello yuan</p>
2. 嵌入式

	嵌入式是将CSS样式集中写在网页的<head></head>标签对的<style></style>标签对中。格式如下：

		<head>
		    <meta charset="UTF-8">
		    <title>Title</title>
		    <style>
		        p{
		            background-color: #2b99ff;
		        }
		    </style>
		</head>
3. 链接式
	
	将一个.css文件引入到HTML文件中

	<link href="mystyle.css" rel="stylesheet" type="text/css"/>
4. 导入式
	
	将一个独立的.css文件引入HTML文件中，导入式使用CSS规则引入外部CSS文件，<style>标记也是写在<head>标记中，使用的语法如下：    

		<style type="text/css">
	          @import"mystyle.css"; 此处要注意.css文件的路径
		</style>　
	注意：

		导入式会在整个网页装载完后再装载CSS文件，因此这就导致了一个问题，如果网页比较大则会儿出现先显示无样式的页面，闪烁一下之后，再出现网页的样式。这是导入式固有的一个缺陷。使用链接式时与导入式不同的是它会以网页文件主体装载前装载CSS文件，因此显示出来的网页从一开始就是带样式的效果的，它不会象导入式那样先显示无样式的网页，然后再显示有样式的网页，这是链接式的优点。
		尽量不要使用
##2.2 css的选择器（Selector）
“选择器”指明了{}中的“样式”的作用对象，也就是“样式”作用于网页中的哪些元素

1. 基础选择器

	- ＊ ：           通用元素选择器，匹配任何元素                    * { margin:0; padding:0; }
	
	- E  ：          标签选择器，匹配所有使用E标签的元素               p { color:green; }
	
	- .info和E.info: class选择器，匹配所有class属性中包含info的元素   .info { background:#ff0; }    p.info { background:blue; }
	
	- #info和E#info  id选择器，匹配所有id属性等于footer的元素         #info { background:#ff0; }   p#info { background:#ff0; }

2. 组合选择器

	- E,F         多元素选择器，同时匹配所有E元素或F元素，E和F之间用逗号分隔         div,p { color:#f00; }
	
	- E F         后代元素选择器，匹配所有属于E元素后代的F元素，E和F之间用空格分隔    li a { font-weight:bold;
	
	- E > F       子元素选择器，匹配所有E元素的子元素F                            div > p { color:#f00; }
	
	- E + F       毗邻元素选择器，匹配所有紧随E元素之后的同级元素F                  div + p { color:#f00; }  

		<!DOCTYPE html>
		<html lang="en">
		<head>
		    <meta charset="UTF-8">
		    <title>Title</title>
		    <style>
		
		        .div1>p{
		            background-color: aqua;
		            color: deeppink;
		        }
		
		        .main2>div{
		            background-color: blueviolet;
		            color: chartreuse;
		        }
		    </style>
		</head>
		<body>
		
		      <div class="div1">hello1
		          <div class="div2">hello2
		              <div>hello4</div>
		              <p>hello5</p>
		          </div>
		          <p>hello3</p>
		      </div>
		      <p>hello6</p>
		
		<hr>
		
		     <div class="main2">1
		       <div>2
		           <div>
		           </div>
		       </div>
		       <div>
		           </div>
		     </div>
		</body>
		</html>
	#注意嵌套规则：

	1. 块级元素可以包含内联元素或某些块级元素，但内联元素不能包含块级元素，它只能包含其它内联元素。
	2. 有几个特殊的块级元素只能包含内联元素，不能包含块级元素。如h1,h2,h3,h4,h5,h6,p,dt
	3. li内可以包含div
	4. 块级元素与块级元素并列、内联元素与内联元素并列。

3. 属性选择器

	- E[att]         匹配所有具有att属性的E元素，不考虑它的值。（注意：E在此处可以省略，比如“[cheacked]”。以下同。）   p[title] { color:#f00; }
	
	- E[att=val]     匹配所有att属性等于“val”的E元素                                 div[class=”error”] { color:#f00; }
	
	- E[att~=val]    匹配所有att属性具有多个空格分隔的值、其中一个值等于“val”的E元素      td[class~=”name”] { color:#f00; }
	
	- E[attr^=val]    匹配属性值以指定值开头的每个元素                     div[class^="test"]{background:#ffff00;}
	
	- E[attr$=val]    匹配属性值以指定值结尾的每个元素                     div[class$="test"]{background:#ffff00;}
	
	- E[attr*=val]    匹配属性值中包含指定值的每个元素                     div[class*="test"]{background:#ffff00;}

4. 伪类(Pseudo-classes)

	CSS伪类是用来给选择器添加一些特殊效果。

	anchor伪类：专用于控制链接的显示效果

	- a:link（没有接触过的链接）,用于定义了链接的常规状态。
	- a:hover（鼠标放在链接上的状态）,用于产生视觉效果。
	- a:visited（访问过的链接）,用于阅读文章，能清楚的判断已经访问过的链接。
	- a:active（在链接上按下鼠标时的状态）,用于表现鼠标按下时的链接状态。
	- 伪类选择器 : 伪类指的是标签的不同状态:
	      a ==> 点过状态 没有点过的状态 鼠标悬浮状态 激活状态
		  a:link {color: #FF0000} /* 未访问的链接 */
		  a:visited {color: #00FF00} /* 已访问的链接 */
		  a:hover {color: #FF00FF} /* 鼠标移动到链接上 */
		  a:active {color: #0000FF} /* 选定的链接 */ 格式: 标签:伪类名称{ css代码; }
	before after伪类 ：

	- :before    p:before       在每个<p>元素之前插入内容
	- :after     p:after        在每个<p>元素之后插入内容
	
	- p:before        在每个 <p> 元素的内容之前插入内容                    p:before{content:"hello";color:red}
	- p:after         在每个 <p> 元素的内容之前插入内容                    p:after{ content:"hello"；color:red}

#10.3

https://www.cnblogs.com/yuanchenqi/articles/5977825.html

##1.CSS的常用属性
1. 颜色属性

	<div style="color:blueviolet">ppppp</div>
	<div style="color:#ffee33">ppppp</div>
	<div style="color:rgb(255,0,0)">ppppp</div>
	<div style="color:rgba(255,0,0,0.5)">ppppp</div>
2. 字体属性

	font-size: 20px/50%/larger
	font-family:'Lucida Bright'
	font-weight: lighter/bold/border/ 
	<h1 style="font-style: oblique">老男孩</h1>
3. 背景属性

	background-color: cornflowerblue
	background-image: url('1.jpg');
	background-repeat: no-repeat;(repeat:平铺满)
	background-position: right top（20px 20px）;(横向：left center right)(纵向：top center bottom)
	
	      简写：<body style="background: 20px 20px no-repeat #ff4 url('1.jpg')">
	
	              <div style="width: 300px;height: 300px;background: 20px 20px no-repeat #ff4 url('1.jpg')"> 
	
	注意：如果将背景属性加在body上，要记得给body加上一个height，否则结果异常，这是因为body为空，无法撑起背景图片；另外，如果此时要设置一个width＝100px，你也看不出效果，除非你设置出html。   


4. 文本属性

	font-size: 10px;
	text-align: center;   横向排列
	line-height: 200px;   文本行高 通俗的讲，文字高度加上文字上下的空白区域的高度 50%:基于字体大小的百分比
	vertical-align:－4px  设置元素内容的垂直对齐方式 ,只对行内元素有效，对块级元素无效
	text-indent: 150px;   首行缩进
	letter-spacing: 10px;
	word-spacing: 20px;
	text-transform: capitalize;

5. 边框属性

	border-style: solid;
	border-color: chartreuse;
	border-width: 20px;
	简写：border: 30px rebeccapurple solid;
6. 列表属性

	ul,ol{   list-style: decimal-leading-zero;
	         list-style: none; <br>         list-style: circle;
	         list-style: upper-alpha;
	         list-style: disc; }
7. dispaly属性

	none
	block
	inline
	display:inline-block可做列表布局，其中的类似于图片间的间隙小bug可以通过如下设置解决：

	#outer{
	            border: 3px dashed;
	            word-spacing: -5px;
	        }
8. 外边距和内边   

	margin:            用于控制元素与元素之间的距离；margin的最基本用途就是控制元素周围空间的间隔，从视觉角度上达到相互隔开的目的。
	padding:           用于控制内容与边框之间的距离；   
	Border(边框)     围绕在内边距和内容外的边框。
	Content(内容)   盒子的内容，显示文本和图像。
	- 元素的宽度和高度:

	Remark重要: 当您指定一个CSS元素的宽度和高度属性时，你只是设置内容区域的宽度和高度。要知道，完全大小的元素，你还必须添加填充，边框和边距。.

	margin:10px 5px 15px 20px;-----------上 右 下 左
	margin:10px 5px 15px;----------------上 右左 下
	margin:10px 5px;---------------------上下  右左
	margin:10px;    ---------------------上右下左
	下面的例子中的元素的总宽度为300px：
	
	width:250px;
	padding:10px;
	border:5px solid gray;
	margin:10px;   
	思考1:
	
	    边框在默认情况下会定位于浏览器窗口的左上角，但是并没有紧贴着浏览器的窗口的边框，这是因为body本身也是一个盒子（外层还有html），在默认情况下，   body距离html会有若干像素的margin，具体数值因各个浏览器不尽相同，所以body中的盒子不会紧贴浏览器窗口的边框了，为了验证这一点，加上：
		body{
		    border: 1px solid;
		    background-color: cadetblue;
		}
		>>>>解决方法：
		
		body{
		    margin: 0;
		}
	思考2：
	
		margin collapse（边界塌陷或者说边界重叠）
		
		外边距的重叠只产生在普通流文档的上下外边距之间，这个看起来有点奇怪的规则，其实有其现实意义。设想，当我们上下排列一系列规则的块级元素（如段     落P）时，那么块元素之间因为外边距重叠的存在，段落之间就不会产生双倍的距离。又比如停车场
		
		1兄弟div：上面div的margin-bottom和下面div的margin-top会塌陷，也就是会取上下两者margin里最大值作为显示值
		
		2父子div    
		
		       if  父级div中没有 border，padding，inline content，子级div的margin会一直向上找，直到找到某个标签包括border，padding，inline content              中的其中一个，然后按此div 进行margin ；
		
		View Code
		解决方法：
		
		1: border:1px solid transparent
		2:  padding:1px
		3: over-flow:hidden; 
##2.float属性
先来了解一下block元素和inline元素在文档流中的排列方式。

　　block元素通常被现实为独立的一块，独占一行，多个block元素会各自新起一行，默认block元素宽度自动填满其父元素宽度。block元素可以设置width、height、margin、padding属性；

　　inline元素不会独占一行，多个相邻的行内元素会排列在同一行里，直到一行排列不下，才会新换一行，其宽度随元素的内容而变化。inline元素设置width、height属性无效。inline元素的margin和padding属性。水平方向的padding-left, padding-right, margin-left, margin-right都产生边距效果；但竖直方向的padding-top, padding-bottom, margin-top, margin-bottom不会产生边距效果。

常见的块级元素有 div、form、table、p、pre、h1～h5、dl、ol、ul 等。
常见的内联元素有span、a、strong、em、label、input、select、textarea、img、br等
     

所谓的文档流，指的是元素排版布局过程中，元素会自动从左往右，从上往下的流式排列。

脱离文档流，也就是将元素从普通的布局排版中拿走，其他盒子在定位的时候，会当做脱离文档流的元素不存在而进行定位。

只有绝对定位absolute和浮动float才会脱离文档流。

     ---部分无视和完全无视的区别？需要注意的是，使用float脱离文档流时，其他盒子会无视这个元素，但其他盒子内的文本依然会为这个元素让出位置，环绕在周围(可以说是部分无视)。而对于使用absolute position脱离文档流的元素，其他盒子与其他盒子内的文本都会无视它。(可以说是完全无视)

浮动的表现
      定义：浮动的框可以向左或向右移动，直到它的外边缘碰到包含框或另一个浮动框的边框为止。由于浮动框不在文档的普通流中，所以文档的普通流中的浮动框之后的块框表现得就像浮动框不存在一样。（注意这里是块框而不是内联元素；浮动框只对它后面的元素造成影响）

注意 当初float被设计的时候就是用来完成文本环绕的效果，所以文本不会被挡住，这是float的特性，即float是一种不彻底的脱离文档流方式。无论多么复杂的布局，其基本出发点均是：“如何在一行显示多个div元素”。

现象1:

      假如某个div元素A是浮动的，如果A元素上一个元素也是浮动的，那么A元素会跟随在上一个元素的后边(如果一行放不下这两个元素，那么A元素会被挤到下一行)；如果A元素上一个元素是标准流中的元素，那么A的相对垂直位置不会改变，也就是说A的顶部总是和上一个元素的底部对齐。此外，浮动的框之后的block元素元素会认为这个框不存在，但其中的文本依然会为这个元素让出位置。 浮动的框之后的inline元素，会为这个框空出位置，然后按顺序排列。

现象2:

(1)左右结构div盒子重叠现象，一般是由于相邻两个DIV一个使用浮动一个没有使用浮动。如上面的例1：相邻的两个盒子box2向左浮动、box3未浮动。一个使用浮动一个没有导致DIV不是在同个“平面”上，但内容不会照成覆盖现象，只有DIV形成覆盖现象。

解决方法：要么都不使用浮动；要么都使用float浮动；要么对没有使用float浮动的DIV设置margin样式。

(2)上下结构div盒子重叠现象

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	<style type="text/css">
	         * {
	             margin:0;padding:0;
	         }
	        .container{
	            border:1px solid red;width:300px;
	        }
	        #box1{
	            background-color:green;float:left;width:100px;height:100px;
	        }
	        #box2{
	            background-color:deeppink; float:right;width:100px;height:100px; 
	        }
	         #box3{
	             background-color:pink;height:40px;
	         }
	</style>
	</head>
	<body>
	
	        <div class="container">
	                <div id="box1">box1 向左浮动</div>
	                <div id="box2">box2 向右浮动</div>
	        </div>
	        <div id="box3">box3</div>
	</body>
	</body>
	</html>
例子如上：.container和box3的布局是上下结构，上图发现box3跑到了上面，与.container产生了重叠，但文本内容没有发生覆盖，只有div发生覆盖现象。这个原因是因为第一个大盒子里的子元素使用了浮动，脱离了文档流，导致.container没有被撑开。box3认为.container没有高度（未被撑开），因此跑上去了。

解决方法：

1、要么给.container设置固定高度，一般情况下文字内容不确定多少就不能设置固定高度，所以一般不能设置“.container”高度(当然能确定内容多高，这种情况下“.container是可以设置一个高度即可解决覆盖问题。

2、要么清除浮动。

- 清除浮动：

	在非IE浏览器（如Firefox）下，当容器的高度为auto，且容器的内容中有浮动（float为left或right）的元素，在这种情况下，容器的高度不能自动伸长以适应内容的高度，使得内容溢出到容器外面而影响（甚至破坏）布局的现象。这个现象叫浮动溢出，为了防止这个现象的出现而进行的CSS处理，就叫CSS清除浮动。
	
	clear语法：
	clear : none | left | right | both
	
	取值：
	none : 默认值。允许两边都可以有浮动对象
	left : 不允许左边有浮动对象
	right : 不允许右边有浮动对象
	both : 不允许有浮动对象
	
	但是需要注意的是：clear属性只会对自身起作用，而不会影响其他元素。如果一个元素的右侧有一浮动对象，而这个元素设置了不允许右边有浮动对象，即clear：right，则这个元素会自动下移一格，达到本元素右边没有浮动对象的目的。
	
	
	方式1(推荐):
	
	.clearfix:after {             <----在类名为“clearfix”的元素内最后面加入内容； 
	content: ".";                 <----内容为“.”就是一个英文的句号而已。也可以不写。 
	display: block;               <----加入的这个元素转换为块级元素。 
	clear: both;                  <----清除左右两边浮动。 
	visibility: hidden;           <----可见度设为隐藏。注意它和display:none;是有区别的。visibility:hidden;仍然占据空间，只是看不到而已； 
	line-height: 0;               <----行高为0； 
	height: 0;                    <----高度为0； 
	font-size:0;                  <----字体大小为0； 
	} 
	.clearfix { *zoom:1;}         <----这是针对于IE6的，因为IE6不支持:after伪类，这个神奇的zoom:1让IE6的元素可以清除浮动来包裹内部元素。
	复制代码
	整段代码就相当于在浮动元素后面跟了个宽高为0的空div，然后设定它clear:both来达到清除浮动的效果。 
	之所以用它，是因为，你不必在html文件中写入大量无意义的空标签，又能清除浮动。 
	
	话说回来，你这段代码真是个累赘啊，这样写不利于维护。 
	只要写一个.clearfix就行了，然后在需要清浮动的元素中 添加clearfix类名就好了。 
	如：
	
		<div class="head clearfix"></div>
	方式2：
	
		overflow:hidden;
	overflow：hidden的含义是超出的部分要裁切隐藏，float的元素虽然不在普通流中，但是他是浮动在普通流之上的，可以把普通流元素+浮动元素想象成一个立方体。如果没有明确设定包含容器高度的情况下，它要计算内容的全部高度才能确定在什么位置hidden，这样浮动元素的高度就要被计算进去。这样包含容器就会被撑开，清除浮动。
##3.position(定位)
1. static

	static 默认值，无定位，不能当作绝对定位的参照物，并且设置标签对象的left、top等值是不起作用的的。

2. position: relative／absolute
	    relative 相对定位。相对定位是相对于该元素在文档流中的原始位置，即以自己原始位置为参照物。有趣的是，即使设定了元素的相对定位以及偏移值，元素还占有着原来的位置，即占据文档流空间。对象遵循正常文档流，但将依据top，right，bottom，left等属性在正常文档流中偏移位置。而其层叠通过z-index属性定义。
	
	注意：position：relative的一个主要用法：方便绝对定位元素找到参照物。
	
	    absolute 绝对定位。
	      定义：设置为绝对定位的元素框从文档流完全删除，并相对于最近的已定位祖先元素定位，如果元素没有已定位的祖先元素，那么它的位置相对于最初的包含块（即body元素）。元素原先在正常文档流中所占的空间会关闭，就好像该元素原来不存在一样。元素定位后生成一个块级框，而不论原来它在正常流中生成何种类型的框。
	
	重点：如果父级设置了position属性，例如position:relative;，那么子元素就会以父级的左上角为原始点进行定位。这样能很好的解决自适应网站的标签偏离问题，即父级为自适应的，那我子元素就设置position:absolute;父元素设置position:relative;，然后Top、Right、Bottom、Left用百分比宽度表示。
	
	      另外，对象脱离正常文档流，使用top，right，bottom，left等属性进行绝对定位。而其层叠通过z-index属性定义。
	
	总结：参照物用相对定位，子元素用绝对定位，并且保证相对定位参照物不会偏移即可。

3. position:fixed
        fixed：对象脱离正常文档流，使用top，right，bottom，left等属性以窗口为参考点进行定位，当出现滚动条时，对象不会随着滚动。而其层叠通过z-index属性 定义。 注意点： 一个元素若设置了 position:absolute | fixed; 则该元素就不能设置float。这 是一个常识性的知识点，因为这是两个不同的流，一个是浮动流，另一个是“定位流”。但是 relative 却可以。因为它原本所占的空间仍然占据文档流。

       在理论上，被设置为fixed的元素会被定位于浏览器窗口的一个指定坐标，不论窗口是否滚动，它都会固定在这个位置。

4. 仅使用margin属性布局绝对定位元素

	此情况，margin-bottom 和margin-right的值不再对文档流中的元素产生影响，因为该元素已经脱离了文档流。另外，不管它的祖先元素有没有定位，都是以文档流中原来所在的位置上偏移参照物。  
	　　图9中，使用margin属性布局相对定位元素。
	　　层级关系为：
	　　<div ——————————— position:relative;
	　　<div—————————-没有设置为定位元素，不是参照物
	　　<div———————-没有设置为定位元素，不是参照物
	　　<div box1
	　　<div box2 ——–position:absolute; margin-top:50px; margin-left:120px;
	　　<div box3
	　　效果图：![](https://images0.cnblogs.com/blog2015/449469/201507/292243208766594.jpg)