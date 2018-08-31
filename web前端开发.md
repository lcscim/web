#8.31
1. html5速查宝典http://man.fishc.com/html5
2. css3速查宝典http://man.fishc.com/css3
3. html注释<!--内容-->
4. css注释 /* 内容 */
5. JavaScript单行注释//，多行/* */

##1.web前端开发
前端就是那些在客户端的应用，通常是指浏览器。最常用于前端的开发技术是HTML+CSS+JavaScript，前端开发人员通常综合使用这些技术开发。

后端开发就是编写那些运行在服务器上的代码，通常来说这部分的工作需要和数据库打交道，比如读写数据，文件，实现业务逻辑等

HTML指的是超文本标记语言（Hyper Text Markup Language）
##2.第一个程序
示例：

	<!DOCTYPE html>    <!--是一个声明，表示该文档是由 HTML5 进行编写的。必须是 HTML 文档的第一行，位于 <html> 标签之前-->
	<html>
		<head>
			<meta charset="utf-8"><!--页面编码-->
			<meta name="viewport" content="width=device-width,initial-scale=1.0"><!--实现页面自适应-->
			<meta name="Keywords" content="关键词，用来快速搜所">
			<meta name="Description" content="内容描述">
			<meta name="author" content="作者">
			<meta http-equiv="Refresh" content="5;http://www.baidu.com"><!--用于刷新页面content第一个参数是时间，第二个为目标网页-->
			<title>第一个程序</title>
			<style type="text/css">	<!--设置样式-->
				h1 {color: red}
				p {color: blue}
			</style>
		</head>
		<body>
			<h1>Hello World</h1>
			<img alt="test" src="腊梅花茶_06.jpg" width="256px">
			<a href="http://www.baidu.com" target="_blank">百度</a>
			<p>I love fishc</p>
		</body>
	</html>