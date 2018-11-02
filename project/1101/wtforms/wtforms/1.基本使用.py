#__author__:asus
#date:2018/11/1
from flask import Flask,request,render_template,redirect
from wtforms import Form
from wtforms.fields import simple
from wtforms import validators  #是否为空验证规则
from wtforms.fields import html5
from wtforms import widgets
from wtforms.fields import core

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
class RegisterForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='alex'
    )

    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    pwd_confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码输入不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    gender = core.RadioField(
        label='性别',
        choices=(
            (1, '男'),
            (2, '女'),
        ),
        coerce=int
    )
    city = core.SelectField(
        label='城市',
        choices=(
            ('bj', '北京'),
            ('sh', '上海'),
        )
    )

    hobby = core.SelectMultipleField(
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )

    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))
        #如果需要去数据库取东西，需要在该类中的init方法中调用否则不会实时更新
    def validate_pwd_confirm(self, field):
        """
        自定义pwd_confirm字段规则，例：与pwd字段是否一致
        :param field:
        :return:
        """
        # 最开始初始化时，self.data中已经有所有的值

        if field.data != self.data['pwd']:
            # raise validators.ValidationError("密码不一致") # 继续后续验证
            raise validators.StopValidation("密码不一致")  # 不再继续后续验证

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm(data={'gender': 1})
        return render_template('register.html', form=form)
    else:
        form = RegisterForm(formdata=request.form)
        if form.validate():
            print('用户提交数据通过格式验证，提交的值为：', form.data)
        else:
            print(form.errors)
        return render_template('register.html', form=form)


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
