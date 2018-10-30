#__author__:asus
#date:2018/10/30
from flask import Blueprint ,render_template,request,redirect,session
import pymysql
import os
import shutil   #解压
import uuid     #生成随机字符串
ind=Blueprint('ind',__name__)

@ind.before_request
def process_request():
    if not session.get("user_info"):
        return redirect("/login")
    return None

@ind.route('/index')
def index():
    return render_template('index.html')
@ind.route('/user_list')
def user_list():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', database='s9day118')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select id,user,nickname from userinfo')
    date_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('user_list.html',date_list=date_list)

@ind.route('/detail/<int:nid>')
def detail(nid):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', database='s9day118')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select id,line,ctime from record where user_id=%s',(nid,))
    record_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('detail.html',record_list=record_list)

@ind.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=="GET":
        return render_template("upload.html")
    file_obj=request.files.get('code')
    #1.检查上传文件的后缀名
    name_ext=file_obj.filename.rsplit('.',maxsplit=1)
    if len(name_ext)<2:
        return "请上传zip压缩文件"
    if name_ext[1]!='zip':
        return "请上传zip压缩文件"
    #2.接收用户上传文件 获取上传文件并写入到服务器本地
    # file_path=os.path.join("files",file_obj.filename)
    # file_obj.save(file_path)
    #3.解压zip文件
    #2+3接收文件并解压到指定目录
    target_path=os.path.join('files',str(uuid.uuid4()))
    shutil._unpack_zipfile(file_obj.stream,target_path)
    #4.遍历某个目录下的所有文件
    total_num=0
    for base_path,folder_list,file_list in os.walk(target_path):
        for file_name in file_list:
            file_path = os.path.join(base_path,file_name)
            file_ext=file_path.rsplit('.',maxsplit=1)
            if len(file_ext) !=2:
                continue
            if file_ext[1]!='py':
                continue
            file_num=0
            with open(file_path,'rb') as f:
                for line in f:
                    line=line.strip()
                    if not line:
                        continue
                    if line.startswith(b'#'):
                        continue
                    file_num+=1
            total_num+=file_num
    #4.5 获取当前时间
    import datetime
    ctime=datetime.datetime.now()
    #4.6 查询是否上传
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', database='s9day118')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select id from record where ctime=%s and user_id=%s',
                   (ctime, session['user_info']['id']))
    date=cursor.fetchone()
    cursor.close()
    conn.close()

    if date:
        return "今天代码已上传"
    #5.上传代码信息
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset='utf8', database='s9day118')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('insert into record(line,ctime,user_id) values (%s,%s,%s)', (total_num,ctime,session['user_info']['id']))
    conn.commit()
    cursor.close()
    conn.close()

    return "上传成功"
