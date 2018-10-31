#__author__:asus
#date:2018/9/25
import threading,queue
from time import sleep
from random import randint
class Production(threading.Thread):
    def run(self):
        while True:
            r=randint(0,20)
            q.put(r)
            print("生产出来%s号包子"%r)
            sleep(1)
class Proces(threading.Thread):
    def run(self):
        while True:
            re=q.get()
            print("吃掉%s号包子"%re)
if __name__=="__main__":
    q=queue.Queue(10)
    threads=[Production(),Production(),Production(),Proces()]
    for t in threads:
        t.start()