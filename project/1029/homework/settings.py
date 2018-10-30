#__author__:asus
#date:2018/10/30

class Config(object):
    #MD5
    SALT=b"sdf1123df"
    #session的盐
    SECRET_KEY=b"asdsad123123asd"
    #控制文件上传大小为7M
    MAX_CONTENT_LENGTH=1024*1024*7