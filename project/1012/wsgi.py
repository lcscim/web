#__author__:asus
#date:2018/10/12
from wsgiref.simple_server import make_server
import time
#不管用没用到都得在方法里添加形参
def f1(req):
    cur_time = time.ctime(time.time())
    f3 = open("index.html", "rb")
    data3=f3.read()
    data3 = str(data3,"utf8").replace("!cur_time!",str(cur_time))
    return [data3.encode("utf8")]

def routers():
    urlpatterns = (
        #每一个元组都需要在最后面添加逗号
        ('/index',f1),
    )
    return urlpatterns

def application(environ, start_response):

    print(environ['PATH_INFO'])
    path=environ['PATH_INFO']
    start_response('200 OK', [('Content-Type', 'text/html')])
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return ["<h1>404</h1>".encode("utf8")]

httpd = make_server('', 8080, application)
print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()