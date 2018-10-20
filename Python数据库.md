#9.27
https://www.cnblogs.com/wupeiqi/articles/5433893.html	--总目录
http://www.cnblogs.com/wupeiqi/articles/5713315.html
http://www.cnblogs.com/wupeiqi/articles/5713323.html
http://www.cnblogs.com/wupeiqi/articles/5729934.html
http://www.cnblogs.com/wupeiqi/articles/5716963.html

##1.数据管理系统DBMS 软件
##2.安装MySQL
MySQL是一个关系型数据库管理系统，由瑞典MySQL AB 公司开发，目前属于 Oracle 旗下公司。MySQL 最流行的关系型数据库管理系统，在 WEB 应用方面MySQL是最好的 RDBMS (Relational Database Management System，关系数据库管理系统) 应用软件之一。

想要使用MySQL来存储并操作数据，则需要做几件事情：
　　a. 安装MySQL服务端
　　b. 安装MySQL客户端
　　b. 【客户端】连接【服务端】
　　c. 【客户端】发送命令给【服务端MySQL】服务的接受命令并执行相应操作(增删改查等)

下载
        http://dev.mysql.com/downloads/mysql/

Window版本

1、下载

	MySQL Community Server 5.7.16
	http://dev.mysql.com/downloads/mysql/
2、解压

如果想要让MySQL安装在指定目录，那么就将解压后的文件夹移动到指定目录，如：C:\mysql-5.7.16-winx64

3、初始化

MySQL解压后的 bin 目录下有一大堆的可执行文件，执行如下命令初始化数据：

	cd c:\mysql-5.7.16-winx64\bin
	mysqld --initialize-insecure
4、启动MySQL服务

执行命令从而启动MySQL服务

	# 进入可执行文件目录
	cd c:\mysql-5.7.16-winx64\bin
	# 启动MySQL服务
	mysqld
5、启动MySQL客户端并连接MySQL服务

由于初始化时使用的【mysqld --initialize-insecure】命令，其默认未给root账户设置密码

	# 进入可执行文件目录
	cd c:\mysql-5.7.16-winx64\bin
	# 连接MySQL服务器
	mysql -u root -p
	# 提示请输入密码，直接回车

到此为止，MySQL服务端已经安装成功并且客户端已经可以连接上，以后再操作MySQL时，只需要重复上述4、5步骤即可。但是，在4、5步骤中重复的进入可执行文件目录比较繁琐，如想日后操作简便，可以做如下操作。

a. 添加环境变量

将MySQL可执行文件添加到环境变量中，从而执行执行命令即可

	
	【右键计算机】--》【属性】--》【高级系统设置】--》【高级】--》【环境变量】--》【在第二个内容框中找到 变量名为Path 的一行，双击】 --> 【将MySQL的bin目录路径追加到变值值中，用 ； 分割】
	
	# 启动MySQL服务，在终端输入
	mysqld
	# 连接MySQL服务，在终端输入：
	mysql -u root -p
b. 将MySQL服务制作成windows服务

上一步解决了一些问题，但不够彻底，因为在执行【mysqd】启动MySQL服务器时，当前终端会被hang住，那么做一下设置即可解决此问题：

	# 制作MySQL的Windows服务，在终端执行此命令：
	"c:\mysql-5.7.16-winx64\bin\mysqld" --install
	# 移除MySQL的Windows服务，在终端执行此命令：
	"c:\mysql-5.7.16-winx64\bin\mysqld" --remove
注册成服务之后，以后再启动和关闭MySQL服务时，仅需执行如下命令：
	# 启动MySQL服务
	net start mysql
	# 关闭MySQL服务
	net stop mysql

##3.介绍
1. 概念

	数据库，相当于文件夹
	数据库表，相当于文件
	数据行，相当于文件中的一行数据
2. 命令

	1、显示数据库，查看当前MySQL有哪些数据根目录有哪些文件夹
	
		SHOW DATABASES;
		#默认数据库：
		　　mysql - 用户权限相关数据
		　　test - 用于用户测试数据
		　　information_schema - MySQL本身架构相关数据

	2、创建数据库
	
		create database 数据库名；
		
		# utf-8
		CREATE DATABASE 数据库名称 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
		# gbk
		CREATE DATABASE 数据库名称 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;
	3、使用数据库
	
		USE 数据库名; 	使用数据库
		SHOW TABLES;	显示当前使用的数据库中所有表：
		create table 表名(nid int,name varchar(20));    创建数据表并指定内容
		select * from 表名; 		查看表中所有数据
		insert into 表名(nid,name) values(1,'alex');		向表中插入数据
		desc 表名； 展示所有数据
3. 授权

	1、用户管理，只适用于MySQL用户表,密码要加引号

		创建用户
		    create user '用户名'@'IP地址' identified by '密码';
		删除用户
		    drop user '用户名'@'IP地址';
		修改用户
		    rename user '用户名'@'IP地址'; to '新用户名'@'IP地址';;
		修改密码
		    set password for '用户名'@'IP地址' = Password('新密码')

		PS：用户权限相关数据保存在mysql数据库的user表中，所以也可以直接对其进行操作（不建议）
		#使用创建的用户登录
		C:\mysql5.7.21\bin\mysql -u 用户名 -h IP地址 -p
	2、授权管理
	
		show grants for '用户'@'IP地址'                  -- 查看权限
		grant  权限 on 数据库.表 to   '用户'@'IP地址'      -- 授权
		revoke 权限 on 数据库.表 from '用户'@'IP地址'      -- 取消权限
		#例如，给lcscim@127.0.0.1添加对于表test.tb1的选择权限
		grant select on test.tb1 to lcscim@127.0.0.1;

		#具体权限如下	
            all privileges  除grant外的所有权限
            select          仅查权限
            select,insert   查和插入权限
            ...
            usage                   无访问权限
            alter                   使用alter table
            alter routine           使用alter procedure和drop procedure
            create                  使用create table
            create routine          使用create procedure
            create temporary tables 使用create temporary tables
            create user             使用create user、drop user、rename user和revoke  all privileges
            create view             使用create view
            delete                  使用delete
            drop                    使用drop table
            execute                 使用call和存储过程
            file                    使用select into outfile 和 load data infile
            grant option            使用grant 和 revoke
            index                   使用index
            insert                  使用insert
            lock tables             使用lock table
            process                 使用show full processlist
            select                  使用select
            show databases          使用show databases
            show view               使用show view
            update                  使用update
            reload                  使用flush
            shutdown                使用mysqladmin shutdown(关闭MySQL)
            super                   􏱂􏰈使用change master、kill、logs、purge、master和set global。还允许mysqladmin􏵗􏵘􏲊􏲋调试登陆
            replication client      服务器位置的访问
            replication slave       由复制从属使用
	
       #对于目标数据库以及内部其他：
            数据库名.*           数据库中的所有
            数据库名.表          指定数据库中的某张表
            数据库名.存储过程     指定数据库中的存储过程
            *.*                所有数据库

            用户名@IP地址         用户只能在改IP下才能访问
            用户名@192.168.1.%   用户只能在改IP段下才能访问(通配符%表示任意)
            用户名@%             用户可以再任意IP下访问(默认IP地址为%)
			此时需要加引号

            grant all privileges on db1.tb1 TO '用户名'@'IP'

            grant select on db1.* TO '用户名'@'IP'

            grant select,insert on *.* TO '用户名'@'IP'

            revoke select on db1.tb1 from '用户名'@'IP'
		#特殊的：
	
			flush privileges，将数据读取到内存中，从而立即生效。
		
		# 启动免授权服务端
		mysqld --skip-grant-tables
		
		# 客户端
		mysql -u root -p
		
		# 修改用户名密码
		update mysql.user set authentication_string=password('666') where user='root';
		flush privileges;
4. sql语句

	数据库级别：

		show databases;		展示数据库
		create database 数据表名；	创建数据库
		CREATE DATABASE 数据库名称 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
		
		use 数据库名；	打开数据库
		drop 数据库名；	删除数据库
	表级别

		show tables;		展示库里的数据表
		desc tbl;			展示表结构

		create table tb1(nid int not null auto_increment primary key,
							name varchar(16),age int default 19)
		engine=innodb default charset=utf8;
		#创建表名为tb1，nid不为空，自增为主键。。。engine=innodb指定数据库引擎


#9.29

##1.数据表基本
1、创建表

	create table 表名(
	    列名  类型  是否可以为空，
	    列名  类型  是否可以为空
	)ENGINE=InnoDB DEFAULT CHARSET=utf8

        是否可空，null表示空，非字符串
            not null    - 不可空
            null        - 可空

        默认值，创建列时可以指定默认值，当插入数据时如果未主动设置，则自动添加默认值
            create table tb1(
                nid int not null defalut 2,
                num int not null
            )

自增，如果为某列设置自增列，插入数据时无需设置此列，默认将自增（表中只能有一个自增列）
            create table tb1(
                nid int not null auto_increment primary key,
                num int null
            )
            或
            create table tb1(
                nid int not null auto_increment,
                num int null,
                index(nid)
            )
            注意：1、对于自增列，必须是索引（含主键）。
                 2、对于自增可以设置步长和起始值
                     show session variables like 'auto_inc%';
                     set session auto_increment_increment=2;
                     set session auto_increment_offset=10;

                     shwo global  variables like 'auto_inc%';
                     set global auto_increment_increment=2;
                     set global auto_increment_offset=10;

主键，一种特殊的唯一索引，不允许有空值，如果主键使用单个列，则它的值必须唯一，如果是多列，则其组合必须唯一。
            create table tb1(
                nid int not null auto_increment primary key,
                num int null
            )
            或
            create table tb1(
                nid int not null,
                num int not null,
                primary key(nid,num)
            )

外键，一个特殊的索引，只能是指定内容
            creat table color(
                nid int not null primary key,
                name char(16) not null
            )

            create table fruit(
                nid int not null primary key,
                smt char(32) null ,
                color_id int not null,
                constraint fk_cc foreign key (color_id) references color(nid)
            )

2、删除表

	drop table 表名
3、清空表

	delete from 表名
	truncate table 表名	清空表内容，速度快，自增回到原点
4、修改表


	添加列：alter table 表名 add 列名 类型
	删除列：alter table 表名 drop column 列名
	修改列：
	        alter table 表名 modify column 列名 类型;  -- 类型
	        alter table 表名 change 原列名 新列名 类型; -- 列名，类型
	  
	添加主键：
	        alter table 表名 add primary key(列名);
	删除主键：
	        alter table 表名 drop primary key;
	        alter table 表名  modify  列名 int, drop primary key;
	  
	添加外键：alter table 从表 add constraint 外键名称（形如：FK_从表_主表） foreign key 从表(外键字段) references 主表(主键字段);
	删除外键：alter table 表名 drop foreign key 外键名称
	  
	修改默认值：ALTER TABLE testalter_tbl ALTER i SET DEFAULT 1000;
	删除默认值：ALTER TABLE testalter_tbl ALTER i DROP DEFAULT;
5、基本数据类型

	MySQL的数据类型大致分为：数值、时间和字符串

        #bit[(M)]
            二进制位（101001），m表示二进制位的长度（1-64），默认m＝1

        #tinyint[(m)] [unsigned] [zerofill]

            小整数，数据类型用于保存一些范围的整数数值范围：
            有符号：
                -128 ～ 127.
            无符号：
                0 ～ 255

            特别的： MySQL中无布尔值，使用tinyint(1)构造。

        #int[(m)][unsigned][zerofill]

            整数，数据类型用于保存一些范围的整数数值范围：
                有符号：
                    -2147483648 ～ 2147483647
                无符号：
                    0 ～ 4294967295

            特别的：整数类型中的m仅用于显示，对存储范围无限制。例如： int(5),当插入数据2时，select 时数据显示为： 00002

        #bigint[(m)][unsigned][zerofill]
            大整数，数据类型用于保存一些范围的整数数值范围：
                有符号：
                    -9223372036854775808 ～ 9223372036854775807
                无符号：
                    0  ～  18446744073709551615

        #decimal[(m[,d])] [unsigned] [zerofill]
            准确的小数值，m是数字总个数（负号不算），d是小数点后个数。 m最大值为65，d最大值为30。

            特别的：对于精确数值计算时需要用此类型
                   decaimal能够存储精确值的原因在于其内部按照字符串存储。

        #FLOAT[(M,D)] [UNSIGNED] [ZEROFILL]
            单精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。
                无符号：
                    -3.402823466E+38 to -1.175494351E-38,
                    0
                    1.175494351E-38 to 3.402823466E+38
                有符号：
                    0
                    1.175494351E-38 to 3.402823466E+38

            **** 数值越大，越不准确 ****

        #DOUBLE[(M,D)] [UNSIGNED] [ZEROFILL]
            双精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。

                无符号：
                    -1.7976931348623157E+308 to -2.2250738585072014E-308
                    0
                    2.2250738585072014E-308 to 1.7976931348623157E+308
                有符号：
                    0
                    2.2250738585072014E-308 to 1.7976931348623157E+308
            **** 数值越大，越不准确 ****


        #char (m)  定长查找速度快，占空间
            char数据类型用于表示固定长度的字符串，可以包含最多达255个字符。其中m代表字符串的长度。
            PS: 即使数据小于m长度，也会占用m长度
        #varchar(m)	变长查找速度慢，节省空间
            varchars数据类型用于变长的字符串，可以包含最多达255个字符。其中m代表该数据类型所允许保存的字符串的最大长度，只要长度小于该最大值的字符串都可以被保存在该数据类型中。

            注：虽然varchar使用起来较为灵活，但是从整个系统的性能角度来说，char数据类型的处理速度更快，有时甚至可以超出varchar处理速度的50%。因此，用户在设计数据库时应当综合考虑各方面的因素，以求达到最佳的平衡

        #text
            text数据类型用于保存变长的大字符串，可以组多到65535 (2**16 − 1)个字符。

        #mediumtext
            A TEXT column with a maximum length of 16,777,215 (2**24 − 1) characters.

        #longtext
            A TEXT column with a maximum length of 4,294,967,295 or 4GB (2**32 − 1) characters.


        #enum 枚举类型，单选
            An ENUM column can have a maximum of 65,535 distinct elements. (The practical limit is less than 3000.)
            示例：
                CREATE TABLE shirts (
                    name VARCHAR(40),
                    size ENUM('x-small', 'small', 'medium', 'large', 'x-large')
                );
                INSERT INTO shirts (name, size) VALUES ('dress shirt','large'), ('t-shirt','medium'),('polo shirt','small');

        #set 集合类型，多选
            A SET column can have a maximum of 64 distinct members.
            示例：
                CREATE TABLE myset (col SET('a', 'b', 'c', 'd'));
                INSERT INTO myset (col) VALUES ('a,d'), ('d,a'), ('a,d,a'), ('a,d,d'), ('d,a,d');

        #DATE
            YYYY-MM-DD（1000-01-01/9999-12-31）

        #TIME
            HH:MM:SS（'-838:59:59'/'838:59:59'）

        #YEAR
            YYYY（1901/2155）

        #DATETIME

            YYYY-MM-DD HH:MM:SS（1000-01-01 00:00:00/9999-12-31 23:59:59    Y）

        #TIMESTAMP

            YYYYMMDD HHMMSS（1970-01-01 00:00:00/2037 年某时）

二进制数据：TinyBlob、Blob、MediumBlob、LongBlob

更多参考：

http://www.runoob.com/mysql/mysql-data-types.html
http://dev.mysql.com/doc/refman/5.7/en/data-type-overview.html

##2.表内容操作
1、增

	insert into 表 (列名,列名...) values (值,值,值...)
	insert into 表 (列名,列名...) values (值,值,值...),(值,值,值...)
	insert into 表 (列名,列名...) select (列名,列名...) from 表
2、删

	delete from 表
	delete from 表 where id＝1 and name＝'alex'
3、改

	update 表 set name ＝ 'alex' where id>1
4、查

	select * from 表
	select * from 表 where id > 1
	select nid,name,gender as gg from 表 where id > 1
5、其他


	a、条件
	    select * from 表 where id > 1 and name != 'alex' and num = 12;
	 
	    select * from 表 where id between 5 and 16;
	 
	    select * from 表 where id in (11,22,33)
	    select * from 表 where id not in (11,22,33)
	    select * from 表 where id in (select nid from 表)
	 
	b、通配符
	    select * from 表 where name like 'ale%'  - ale开头的所有（%，多个字符串）
	    select * from 表 where name like 'ale_'  - ale开头的所有（_，一个字符）
	 
	c、限制 
	    select * from 表 limit 5;            - 前5行
	    select * from 表 limit 4,5;          - 从第4行开始的5行
	    select * from 表 limit 5 offset 4    - 从第4行开始的5行
	 
	d、排序
	    select * from 表 order by 列 asc              - 根据 “列” 从小到大排列
	    select * from 表 order by 列 desc             - 根据 “列” 从大到小排列
	    select * from 表 order by 列1 desc,列2 asc    - 根据 “列1” 从大到小排列，如果相同则按列2从小到大排序
	 
	e、分组
	    select num from 表 group by num
	    select num,nid from 表 group by num,nid
	    select num,nid from 表  where nid > 10 group by num,nid order nid desc
	    select num,nid,count(*),sum(score),max(score),min(score) from 表 group by num,nid
	 	对聚合条件进行筛选用having
	    select num from 表 group by num having max(id) > 10
	 
	    特别的：group by 必须在where之后，order by之前
	 
	f、连表
	    无对应关系则不显示
	    select A.num, A.name, B.name from A,B Where A.nid = B.nid
	 
	    无对应关系则不显示
	    select A.num, A.name, B.name from A inner join B on A.nid = B.nid
	 
	    A表所有显示，如果B中无对应关系，则值为null
	    select A.num, A.name, B.name from A left join B on A.nid = B.nid
	 
	    B表所有显示，如果B中无对应关系，则值为null
	    select A.num, A.name, B.name from A right join B on A.nid = B.nid
	 
	g、组合
	    组合，自动处理重合
	    select nickname from A union select name from B
	 
	    组合，不处理重合
	    select nickname from A union all select name from B

##3.其他

导出现有数据库数据：

	mysqldump -u用户名 -p密码 数据库名称 >导出文件路径           # 结构+数据
	mysqldump -u用户名 -p密码 -d 数据库名称 >导出文件路径       # 结构 
导入现有数据库数据：

	mysqldump -uroot -p密码  数据库名称 < 文件路径  
- 一些其他函数和方法

	DISTINCT		去重
	AVG(num)		求平均数
##4.习题及答案
- 习题

	http://www.cnblogs.com/wupeiqi/articles/5729934.html
- 答案

	http://www.cnblogs.com/wupeiqi/articles/5748496.html


#9.30
http://www.cnblogs.com/wupeiqi/articles/5713330.html

##1.python 操作MySQL
- 下载

	pip install mysql
- 简单使用

		import pymysql
		#链接数据库
		conn = pymysql.connect(host='localhost',port=3306,user='root',password='',db='test')
		#创建游标
		course=conn.cursor();
		#提交语句
		course.execute('delete from class where class.caption = "自学"')
		#确认提交
		conn.commit()
		#关闭游标
		course.close()
		#关闭链接
		conn.close()
	注意必须以参数形式传递字符串，如果多个占位符，则参数为元组，如果为列表则为executemany().
	如果查找不需要commit
1、执行SQL

	#!/usr/bin/env python
	# -*- coding:utf-8 -*-
	import pymysql
	  
	# 创建连接
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
	# 创建游标
	cursor = conn.cursor()
	  
	# 执行SQL，并返回收影响行数
	effect_row = cursor.execute("update hosts set host = '1.1.1.2'")
	  
	# 执行SQL，并返回受影响行数
	#effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))
	  
	# 执行SQL，并返回受影响行数
	#effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
	  
	  
	# 提交，不然无法保存新建或者修改的数据
	conn.commit()
	  
	# 关闭游标
	cursor.close()
	# 关闭连接
	conn.close()
2、获取新创建数据自增ID

	#!/usr/bin/env python
	# -*- coding:utf-8 -*-
	import pymysql
	  
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
	cursor = conn.cursor()
	cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
	conn.commit()
	cursor.close()
	conn.close()
	  
	# 获取最新自增ID
	new_id = cursor.lastrowid

3、获取查询数据

	#!/usr/bin/env python
	# -*- coding:utf-8 -*-
	import pymysql
	  
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
	cursor = conn.cursor()
	cursor.execute("select * from hosts")
	  
	# 获取第一行数据
	row_1 = cursor.fetchone()
	  
	# 获取前n行数据
	# row_2 = cursor.fetchmany(3)
	# 获取所有数据
	# row_3 = cursor.fetchall()
	  
	conn.commit()
	cursor.close()
	conn.close()
	注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：
	
	cursor.scroll(1,mode='relative')  # 相对当前位置移动
	cursor.scroll(2,mode='absolute') # 相对绝对位置移动
4、fetch数据类型

	关于默认获取的数据是元祖类型，如果想要或者字典类型的数据，即：
	cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

	#!/usr/bin/env python
	# -*- coding:utf-8 -*-
	import pymysql
	  
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
	  
	# 游标设置为字典类型
	cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
	r = cursor.execute("call p1()")
	  
	result = cursor.fetchone()
	  
	conn.commit()
	cursor.close()
	conn.close()

注意：

- sql注入错误

	#必须以这种形式传值，否则会出现sql注入错误。比如内容是'name" or 1=1 -- '
	inp1 = input('请输入账号')
	inp2 = input('请输入密码')
	course.execute('select username,password from test where username = "%s" and password = "%s"',(inp1,inp2))

##2.视图
视图是一个虚拟表（非真实存在），其本质是【根据SQL语句获取动态的数据集，并为其命名】，用户使用时只需使用【名称】即可获取结果集，并可以将其当作表来使用。

SELECT * FROM (SELECT nid,NAME FROM tb1 WHERE nid > 2) AS A WHERE A. NAME > 'alex';

1. 创建视图

	--格式：CREATE VIEW 视图名称 AS  SQL语句
	CREATE VIEW v1 AS SELET nid,name FROM A WHERE nid > 4;
2. 删除视图


	--格式：DROP VIEW 视图名称
	DROP VIEW v1
3. 修改视图

	-- 格式：ALTER VIEW 视图名称 AS SQL语句
	ALTER VIEW v1 AS SELET A.nid,B.NAME FROM A LEFT JOIN B ON A.id =  B.nid LEFT JOIN C ON A.id = C.nid WHERE A.id > 2 AND C.nid < 5
4. 使用视图

	使用视图时，将其当作表进行操作即可，由于视图是虚拟表，所以无法使用其对真实表进行创建、更新和删除操作，仅能做查询用。
	select * from v1

##3.存储过程
存储过程是一个SQL语句集合，当主动去调用存储过程时，其中内部的SQL语句会按照逻辑执行。

1. 创建存储过程

	- 无参数

		#创建存储过程
		delimiter //
		create procedure p1()
		BEGIN
		    select * from t1;
		END//
		delimiter ;
		
		#执行存储过程
		call p1()

	对于存储过程，可以接收参数，其参数有三类：
	
		in        仅用于传入参数用
		out       仅用于返回值用
		inout     既可以传入又可以当作返回值
	- 有参数

		delimiter \\
		create procedure p1(
		    in i1 int,
		    in i2 int,
		    inout i3 int,
		    out r1 int
		)
		BEGIN
			#DECLARE相当于声明变量类型
		    DECLARE temp1 int;
		    DECLARE temp2 int default 0;
		    
		    set temp1 = 1;
		
		    set r1 = i1 + i2 + temp1 + temp2;
		    
		    set i3 = i3 + 100;
		
		end\\
		delimiter ;
		
		-- 执行存储过程
		#有返回值的变量必须以@开头
		set @t1 =4;
		set @t2 = 0;
		CALL p1 (1, 2 ,@t1, @t2);
		SELECT @t1,@t2;
	- 结果集

        delimiter //
        create procedure p1()
        begin
            select * from v1;
        end //
        delimiter ;
	- 结果集+out值

		delimiter //
        create procedure p2(
            in n1 int,
            inout n3 int,
            out n2 int,
        )
        begin
            declare temp1 int ;
            declare temp2 int default 0;

            select * from v1;
            set n2 = n1 + 100;
            set n3 = n3 + n1 + 100;
        end //
        delimiter ;
3. 执行存储过程

		# 无参数
		call proc_name()
		# 有参数，全in
		call proc_name(1,2)
		# 有参数，有in，out，inout
		set @t1=0;
		set @t2=3;
		call proc_name(1,2,@t1,@t2)

	pymysql执行存储过程

		#!/usr/bin/env python
		# -*- coding:utf-8 -*-
		import pymysql
		conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
		cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
		# 执行存储过程callproc
		cursor.callproc('p1', args=(1, 22, 3, 4))
		# 获取执行完存储的参数
		cursor.execute("select @_p1_0,@_p1_1,@_p1_2,@_p1_3")
		result = cursor.fetchall()
		conn.commit()
		cursor.close()
		conn.close()
		print(result)

#10.1
http://www.cnblogs.com/wupeiqi/articles/5713323.html
##1.触发器
对某个表进行【增/删/改】操作的前后如果希望触发某个特定的行为时，可以使用触发器，触发器用于定制用户对表的行进行【增/删/改】前后的行为。

1、创建基本语法

	# 插入前
	CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON tb1 FOR EACH ROW
	BEGIN
	    ...
	END
	
	# 插入后
	CREATE TRIGGER tri_after_insert_tb1 AFTER INSERT ON tb1 FOR EACH ROW
	BEGIN
	    ...
	END
	
	# 删除前
	CREATE TRIGGER tri_before_delete_tb1 BEFORE DELETE ON tb1 FOR EACH ROW
	BEGIN
	    ...
	END
	
	# 删除后
	CREATE TRIGGER tri_after_delete_tb1 AFTER DELETE ON tb1 FOR EACH ROW
	BEGIN
	    ...
	END
	
	# 更新前
	CREATE TRIGGER tri_before_update_tb1 BEFORE UPDATE ON tb1 FOR EACH ROW
	BEGIN
	    ...
	END
	
	# 更新后
	CREATE TRIGGER tri_after_update_tb1 AFTER UPDATE ON tb1 FOR EACH ROW
	BEGIN
	    ...
	END
	
	delimiter //
	CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON tb1 FOR EACH ROW
	BEGIN
	
	IF NEW. NAME == 'alex' THEN
	    INSERT INTO tb2 (NAME)
	VALUES
	    ('aa')
	END
	END//
	delimiter ;
	
	
	
	delimiter //
	CREATE TRIGGER tri_after_insert_tb1 AFTER INSERT ON tb1 FOR EACH ROW
	BEGIN
	    IF NEW. num = 666 THEN
	        INSERT INTO tb2 (NAME)
	        VALUES
	            ('666'),
	            ('666') ;
	    ELSEIF NEW. num = 555 THEN
	        INSERT INTO tb2 (NAME)
	        VALUES
	            ('555'),
	            ('555') ;
	    END IF;
	END//
	delimiter ;

特别的：NEW表示即将插入的数据行，OLD表示即将删除的数据行。

2、删除触发器

	DROP TRIGGER tri_after_insert_tb1;
3、使用触发器

触发器无法由用户直接调用，而知由于对表的【增/删/改】操作被动引发的。

	insert into tb1(num) values(666)
##2.函数
MySQL中提供了许多内置函数，例如：

    CHAR_LENGTH(str)
        返回值为字符串str 的长度，长度的单位为字符。一个多字节字符算作一个单字符。
        对于一个包含五个二字节字符集, LENGTH()返回值为 10, 而CHAR_LENGTH()的返回值为5。

    CONCAT(str1,str2,...)
        字符串拼接
        如有任何一个参数为NULL ，则返回值为 NULL。
    CONCAT_WS(separator,str1,str2,...)
        字符串拼接（自定义连接符）
        CONCAT_WS()不会忽略任何空字符串。 (然而会忽略所有的 NULL）。

    CONV(N,from_base,to_base)
        进制转换
        例如：
            SELECT CONV('a',16,2); 表示将 a 由16进制转换为2进制字符串表示

    FORMAT(X,D)
        将数字X 的格式写为'#,###,###.##',以四舍五入的方式保留小数点后 D 位， 并将结果以字符串的形式返回。若  D 为 0, 则返回结果不带有小数点，或不含小数部分。
        例如：
            SELECT FORMAT(12332.1,4); 结果为： '12,332.1000'
    INSERT(str,pos,len,newstr)
        在str的指定位置插入字符串
            pos：要替换位置其实位置
            len：替换的长度
            newstr：新字符串
        特别的：
            如果pos超过原字符串长度，则返回原字符串
            如果len超过原字符串长度，则由新字符串完全替换
    INSTR(str,substr)
        返回字符串 str 中子字符串的第一个出现位置。

    LEFT(str,len)
        返回字符串str 从开始的len位置的子序列字符。

    LOWER(str)
        变小写

    UPPER(str)
        变大写

    LTRIM(str)
        返回字符串 str ，其引导空格字符被删除。
    RTRIM(str)
        返回字符串 str ，结尾空格字符被删去。
    SUBSTRING(str,pos,len)
        获取字符串子序列

    LOCATE(substr,str,pos)
        获取子序列索引位置

    REPEAT(str,count)
        返回一个由重复的字符串str 组成的字符串，字符串str的数目等于count 。
        若 count <= 0,则返回一个空字符串。
        若str 或 count 为 NULL，则返回 NULL 。
    REPLACE(str,from_str,to_str)
        返回字符串str 以及所有被字符串to_str替代的字符串from_str 。
    REVERSE(str)
        返回字符串 str ，顺序和字符顺序相反。
    RIGHT(str,len)
        从字符串str 开始，返回从后边开始len个字符组成的子序列

    SPACE(N)
        返回一个由N空格组成的字符串。

    SUBSTRING(str,pos) , SUBSTRING(str FROM pos) SUBSTRING(str,pos,len) , SUBSTRING(str FROM pos FOR len)
        不带有len 参数的格式从字符串str返回一个子字符串，起始于位置 pos。带有len参数的格式从字符串str返回一个长度同len字符相同的子字符串，起始于位置 pos。 使用 FROM的格式为标准 SQL 语法。也可能对pos使用一个负值。假若这样，则子字符串的位置起始于字符串结尾的pos 字符，而不是字符串的开头位置。在以下格式的函数中可以对pos 使用一个负值。

        mysql> SELECT SUBSTRING('Quadratically',5);
            -> 'ratically'

        mysql> SELECT SUBSTRING('foobarbar' FROM 4);
            -> 'barbar'

        mysql> SELECT SUBSTRING('Quadratically',5,6);
            -> 'ratica'

        mysql> SELECT SUBSTRING('Sakila', -3);
            -> 'ila'

        mysql> SELECT SUBSTRING('Sakila', -5, 3);
            -> 'aki'

        mysql> SELECT SUBSTRING('Sakila' FROM -4 FOR 2);
            -> 'ki'

    TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str) TRIM(remstr FROM] str)
        返回字符串 str ， 其中所有remstr 前缀和/或后缀都已被删除。若分类符BOTH、LEADIN或TRAILING中没有一个是给定的,则假设为BOTH 。 remstr 为可选项，在未指定情况下，可删除空格。

        mysql> SELECT TRIM('  bar   ');
                -> 'bar'

        mysql> SELECT TRIM(LEADING 'x' FROM 'xxxbarxxx');
                -> 'barxxx'

        mysql> SELECT TRIM(BOTH 'x' FROM 'xxxbarxxx');
                -> 'bar'

        mysql> SELECT TRIM(TRAILING 'xyz' FROM 'barxxyz');
                -> 'barx'

更多函数：
- 中文 http://doc.mysql.cn/mysql5/refman-5.1-zh.html-chapter/functions.html#encryption-functions
- 官方 https://dev.mysql.com/doc/refman/5.7/en/functions.html

1、自定义函数

	delimiter \\
	create function f1(
	    i1 int,
	    i2 int)
	returns int
	BEGIN
	    declare num int;
	    set num = i1 + i2;
	    return(num);
	END \\
	delimiter ;

2、删除函数


	drop function func_name;
3、执行函数

	# 获取返回值
	declare @i VARCHAR(32);
	select UPPER('alex') into @i;
	SELECT @i;
	
	# 在查询中使用
	select f1(11,nid) ,name from tb2;
##3.事务
事务用于将某些操作的多个SQL作为原子性操作，一旦有某一个出现错误，即可回滚到原来的状态，从而保证数据库数据完整性。

	delimiter \\
	create PROCEDURE p1(
	    OUT p_return_code tinyint
	)
	BEGIN 
	  DECLARE exit handler for sqlexception 
	  BEGIN 
	    -- ERROR 
	    set p_return_code = 1; 
	    rollback; 
	  END; 
	 
	  DECLARE exit handler for sqlwarning 
	  BEGIN 
	    -- WARNING 
	    set p_return_code = 2; 
	    rollback; 
	  END; 
	 
	  START TRANSACTION; 
	    DELETE from tb1;
	    insert into tb2(name)values('seven');
	  COMMIT; 
	 
	  -- SUCCESS 
	  set p_return_code = 0; 
	 
	  END\\
	delimiter ;

	set @i =0;
	call p1(@i);
	select @i;
##4.索引
索引，是数据库中专门用于帮助用户快速查询数据的一种数据结构。类似于字典中的目录，查找字典内容时可以根据目录查找到数据的存放位置，然后直接获取即可。

	                    30
	 
	        10                        40
	 
	   5         15            35             66
	 
	1   6     11    19      21      39     55     100
　　

MySQL中常见索引有：

- 普通索引	- 加速查找
- 唯一索引	- 加速查找，约束列数据不能重复，可以为null
- 主键索引	- 加速查找，约束列数据不能重复，不可以为null
- 组合索引	- 多列可以创建一个索引文件

1、普通索引

	普通索引仅有一个功能：加速查询

	create table in1(
	    nid int not null auto_increment primary key,
	    name varchar(32) not null,
	    email varchar(64) not null,
	    extra text,
	    index ix_name (name)
	)
	#创建索引
	create index index_name on table_name(column_name)
	#删除索引
	drop index_name on table_name;
	#查看索引
	show index from table_name;
	注意：对于创建索引时如果是BLOB 和 TEXT 类型，必须指定length。

	create index ix_extra on in1(extra(32));
2、唯一索引

唯一索引有两个功能：加速查询 和 唯一约束（可含null）

	create table in1(
	    nid int not null auto_increment primary key,
	    name varchar(32) not null,
	    email varchar(64) not null,
	    extra text,
	    unique ix_name (name)
	)
	#创建索引
	create unique index 索引名 on 表名(列名)
	#删除索引
	drop unique index 索引名 on 表名
3、主键索引

主键有两个功能：加速查询 和 唯一约束（不可含null）

	create table in1(
	    nid int not null auto_increment primary key,
	    name varchar(32) not null,
	    email varchar(64) not null,
	    extra text,
	    index ix_name (name)
	)
	
	OR
	
	create table in1(
	    nid int not null auto_increment,
	    name varchar(32) not null,
	    email varchar(64) not null,
	    extra text,
	    primary key(ni1),
	    index ix_name (name)
	)
	#创建主键
	alter table 表名 add primary key(列名);
	#删除主键
	alter table 表名 drop primary key;
	alter table 表名  modify  列名 int, drop primary key;
4、组合索引

组合索引是将n个列组合成一个索引

其应用场景为：频繁的同时使用n列来进行查询，如：where n1 = 'alex' and n2 = 666。

	create table in3(
	    nid int not null auto_increment primary key,
	    name varchar(32) not null,
	    email varchar(64) not null,
	    extra text
	)
	#创建组合索引
	create index ix_name_email on in3(name,email);

如上创建组合索引之后，查询：

	name and email  -- 使用索引
	name                 -- 使用索引
	email                 -- 不使用索引
	注意：对于同时搜索n个条件时，组合索引的性能好于多个单一索引合并。
##5.其他 
1、条件语句

	delimiter \\
	CREATE PROCEDURE proc_if ()
	BEGIN
	    
	    declare i int default 0;
	    if i = 1 THEN
	        SELECT 1;
	    ELSEIF i = 2 THEN
	        SELECT 2;
	    ELSE
	        SELECT 7;
	    END IF;
	
	END\\
	delimiter ;
2、循环语句
	#while循环
	delimiter \\
	CREATE PROCEDURE proc_while ()
	BEGIN
	
	    DECLARE num INT ;
	    SET num = 0 ;
	    WHILE num < 10 DO
	        SELECT
	            num ;
	        SET num = num + 1 ;
	    END WHILE ;
	
	END\\
	delimiter ;
	#repeat循环
	delimiter \\
	CREATE PROCEDURE proc_repeat ()
	BEGIN
	
	    DECLARE i INT ;
	    SET i = 0 ;
	    repeat
	        select i;
	        set i = i + 1;
	        until i >= 5
	    end repeat;
	
	END\\
	delimiter ;
	#loop循环
	BEGIN
	    
	    declare i int default 0;
	    loop_label: loop
	        
	        set i=i+1;
	        if i<8 then
	            iterate loop_label;
	        end if;
	        if i>=10 then
	            leave loop_label;
	        end if;
	        select i;
	    end loop loop_label;
	END

3、动态执行SQL语句

	delimiter \\
	DROP PROCEDURE IF EXISTS proc_sql \\
	CREATE PROCEDURE proc_sql ()
	BEGIN
	    declare p1 int;
	    set p1 = 11;
	    set @p1 = p1;
	
	    PREPARE prod FROM 'select * from tb2 where nid > ?';
	    EXECUTE prod USING @p1;
	    DEALLOCATE prepare prod; 
	
	END\\
	delimiter ;
##6.索引相关
http://www.cnblogs.com/wupeiqi/articles/5716963.html

- 覆盖索引

	只需要在索引中就可以获取到数据时
- 合并索引

	对于两个同一个表的两个不同索引同时使用
		select * from tb where name=‘Alex’；
		select * from tb where age=18；	--可以查找
		select * from tb where name=‘Alex’ and age=18；
	与组合索引不同，
		select * from tb where name=‘Alex’；
		select * from tb where age=18；	--不可以查找
		select * from tb where name=‘Alex’ and age=18；

	具体使用根据情况
- 执行计划，相对比较准确的表达出当前SQL运行状况

	查看是否走索引：

	explain SQL语句；
	1. explain SQL语句
		type:ALL 		- 全数据表扫描
		type:index		- 全索引表扫描
	2. limit

		select * from tb where name=‘Alex’ limit 1；- 表示当前还是全局扫描只不过执行了一句就停止了
	-------------出现ALL，和index，都还有优化的余地------------
	3. range表名有索引进行范围查找

		注意：!= 和 > 符号不走索引
	4. 正确使用索引

	数据库表中添加索引后确实会让查询速度起飞，但前提必须是正确的使用索引来查询，如果以错误的方式使用，则即使建立索引也会不奏效。即使建立索引，索引也不会生效：

		- like '%xx'
			# %在前不走索引，在后面走索引 
		    select * from tb1 where name like '%cn';
		- 使用函数
		    select * from tb1 where reverse(name) = 'wupeiqi';
		- or
		    select * from tb1 where nid = 1 or email = 'seven@live.com';
		    特别的：当or条件中有未建立索引的列才失效，以下会走索引
		            select * from tb1 where nid = 1 or name = 'seven';
		            select * from tb1 where nid = 1 or email = 'seven@live.com' and name = 'alex'
		- 类型不一致
		    如果列是字符串类型，传入条件是必须用引号引起来，不然...
		    select * from tb1 where name = 999;
		- !=
		    select * from tb1 where name != 'alex'
		    特别的：如果是主键，则还是会走索引
		        select * from tb1 where nid != 123
		- >
		    select * from tb1 where name > 'alex'
		    特别的：如果是主键或索引是整数类型，则还是会走索引
		        select * from tb1 where nid > 123
		        select * from tb1 where num > 123
		- order by
		    select email from tb1 order by name desc;
		    当根据索引排序时候，选择的映射如果不是索引，则不走索引
		    特别的：如果对主键排序，则还是走索引：
		        select * from tb1 order by nid desc;
		 
		- 组合索引最左前缀
		    如果组合索引为：(name,email)
		    name and email       -- 使用索引
		    name                 -- 使用索引
		    email                -- 不使用索引
- 其他注意事项

	- 避免使用select *
	- count(1)或count(列) 代替 count(*)
	- 创建表时尽量时 char 代替 varchar
	- 表的字段顺序固定长度的字段优先
	- 组合索引代替多个单列索引（经常使用多个条件查询时）
	- 尽量使用短索引
	- 使用连接（JOIN）来代替子查询(Sub-Queries)
	- 连表时注意条件类型需一致
	- 索引散列值（重复少）不适合建索引，例：性别不适合

- limit分页

无论是否有索引，limit分页是一个值得关注的问题

	每页显示10条：
	当前 118 120， 125
	
	倒序：
	            大      小
	            980    970  7 6  6 5  54  43  32
	
	21 19 98     
	下一页：
	
	    select 
	        * 
	    from 
	        tb1 
	    where 
	        nid < (select nid from (select nid from tb1 where nid < 当前页最小值 order by nid desc limit 每页数据 *【页码-当前页】) A order by A.nid asc limit 1)  
	    order by 
	        nid desc 
	    limit 10;
	
	
	
	    select 
	        * 
	    from 
	        tb1 
	    where 
	        nid < (select nid from (select nid from tb1 where nid < 970  order by nid desc limit 40) A order by A.nid asc limit 1)  
	    order by 
	        nid desc 
	    limit 10;
	
	
	上一页：
	
	    select 
	        * 
	    from 
	        tb1 
	    where 
	        nid < (select nid from (select nid from tb1 where nid > 当前页最大值 order by nid asc limit 每页数据 *【当前页-页码】) A order by A.nid asc limit 1)  
	    order by 
	        nid desc 
	    limit 10;
	
	
	    select 
	        * 
	    from 
	        tb1 
	    where 
	        nid < (select nid from (select nid from tb1 where nid > 980 order by nid asc limit 20) A order by A.nid desc limit 1)  
	    order by 
	        nid desc 
	    limit 10;
##7.慢日志记录
- 方式一：直接在内存中修改

	查看当前配置信息：
		show variables like '%query%'

	修改当前配置：
		set global 变量名 = 值
- 方式二：写一个配置文件，如：C:\mysql5.7.21\my-default.ini

	mysqld --default-files = C:\mysql5.7.21\my-default.ini

	
		
		

	

	

