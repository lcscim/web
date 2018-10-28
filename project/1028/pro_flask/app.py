from flask import Flask,redirect,render_template,request,session,url_for
from flask import jsonify,make_response,Markup,flash,get_flashed_messages
import functools
app = Flask(__name__)
app.config.from_object("settings.DevelopmentConfig")

STUDENT_DICT={
    1:{'name':'王龙泰','age':'38','gender':'中'},
    2:{'name':'小东北','age':'73','gender':'男'},
    3:{'name':'田硕','age':'84','gender':'男'},
}

@app.before_request
def xxxx():
    if request.path=='/login':
        return None
    if session.get('user'):
        return None
    return  redirect('/login')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user=request.form.get('user')
    pwd=request.form.get('pwd')
    if user=='oldboy'and pwd=='666':
        session['user']=user
        return redirect('index')
    return render_template('login.html',error='用户名或密码错误')

@app.route('/index')
def index():
    return render_template('index.html',stu_dic=STUDENT_DICT)

@app.route('/delete/<int:nid>')
def delete(nid):
    del STUDENT_DICT[nid]
    return redirect(url_for('index'))

@app.route('/detail/<int:nid>')
def detail(nid):
    info = STUDENT_DICT[nid]
    return render_template('detail.html',info=info)

@app.route('/tpl')
def tpl():
    context={
        'users':['aaa','bbb','ccc'],
        'txt':'<input type="text">',
    }
    return render_template('tpl.html',**context)
@app.route('/page1')
def page1():
    # session['uuuu']=123
    flash('存储临时数据',category='error')
    #表示临时放一次数据category='error'表示对其进行分类
    return "session"

@app.route('/page2')
def page2():
    # print(session['uuuu'])
    print(get_flashed_messages(category_filter=['error']))
    #get_flashed_messages()取一次就没有了
    return "session"

if __name__ == '__main__':
    app.run()
