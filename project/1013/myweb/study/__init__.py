# import pymysql
# pymysql.install_as_MySQLdb()
# NAME即数据库的名字，在mysql连接前该数据库必须已经创建，而上面的sqlite数据库下的db.sqlite3则是项目自动创建
#
# USER和PASSWORD分别是数据库的用户名和密码。
#
# 设置完后，再启动我们的Django项目前，我们需要激活我们的mysql。
#
# 然后，启动项目，会报错：no module named MySQLdb
#
# 这是因为django默认你导入的驱动是MySQLdb，可是MySQLdb对于py3有很大问题，所以我们需要的驱动是PyMySQL
#
# 所以，我们只需要找到项目名文件下的__init__,在里面写入：
#
# import pymysql
# pymysql.install_as_MySQLdb()
#
# 问题解决！