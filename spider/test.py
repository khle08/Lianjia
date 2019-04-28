import multiprocessing
import threading
import os
class MyThread(threading.Thread): # 继承threading的Thread类
    def __init__(self, num):
        threading.Thread.__init__(self) # 必须执行父类的构造方法
        self.num = num # 传入参数 num

    def run(self):  # 定义每个线程要运行的函数
        while self.num > 0:
            print("当前线程数:", threading.activeCount())
            self.num -= 1

for x in range(5):
    t = MyThread(2) # 生成实例,传入参数
    t.start() #启动线程