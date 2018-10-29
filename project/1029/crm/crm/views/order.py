#__author__:asus
#date:2018/10/29
import threading
import time
import greenlet

# DIC={}

# def task(i):
#     ident=greenlet.getcurrent()
#     #ident=threading.get_ident()
#     if ident in DIC:
#         DIC[ident]['xxxx']=i
#     else:
#         DIC[ident]={'xxxx':i}
#     time.sleep(2)
#     print(DIC[ident]['xxxx'],i)

try:
    get_ident=greenlet.getcurrent
except Exception as e:
    get_ident=threading.get_ident

class Local(object):
    DIC={}
    def __getattr__(self, item):
        ident=get_ident()
        if ident in self.DIC:
            return self.DIC[ident].get(item)
        return None
    def __setattr__(self, key, value):
        ident=get_ident()
        if ident in self.DIC:
            self.DIC[ident][key]=value
        else:
            self.DIC[ident]={key:value}

obj=Local()
def task(i):
    obj.xxxx=i
    time.sleep(2)
    print(obj.xxxx,i)

for i in range(10):
    t=threading.Thread(target=task,args=(i,))
    t.start()