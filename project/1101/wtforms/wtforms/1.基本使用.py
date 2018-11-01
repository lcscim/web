#__author__:asus
#date:2018/11/1
from flask import Flask,request,render_template,redirect
from wtforms import Form
from wtforms.fields import simple
from wtforms import validators  #是否为空验证规则

app=Flask(__name__)

class LoginForm(Form):
    name=simple.StringField(
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.Length(min=6,max=18,message='用户名的长度必须大于%(min)d且小于%(max)d')
        ],
        render_kw={'placeholder':'请输入用户名'}
    )
    pwd=simple.PasswordField(
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.Length(min=6,message='用户名的长度必须大于%(min)d'),
            validators.Regexp(regex="^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,16}$",
                              message='正则表达式密码8-16 必须英文和数字混合'),
        ],
        render_kw={'placeholder':'请输入密码'}
    )

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        form=LoginForm()
        return render_template('login.html',form=form)
    form=LoginForm(formdata=request.form)
    if form.validate():
        print("验证成功")
        print(form.data)
        return redirect("https://www.baidu.com")
    else:
        return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run()
