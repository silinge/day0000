# from random import randint
# # from time import time, sleep
# #
# # def download_task(filename):
# #     print('start%s...'%filename)
# #     time_to_download = randint(5, 10)
# #     sleep(time_to_download)
# #     print(f'{filename}S下载完成, 耗费了{time_to_download}秒.')
# #
# # def mainly():
# #     start = time()
# #     download_task('Pythom从入门到入院.mov')
# #     download_task('China, China.mp4')
# #     end = time()
# #     print(f'总共耗费{end-start}秒.')
# #
# # if __name__ == '__main__':
# #     mainly()

# from multiprocessing import Process
# from os import getpid
# from random import randint
# from time import time, sleep
#
# def download_task(filename):
#     print('启动下载进程, 进程号是[%d].'%getpid())
#     print('开始下载%s...'%filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗时%d秒.'%(filename, time_to_download))
#
# def mainly():
#     start = time()
#     p1 = Process(target=download_task('Python从入门到入狱.mp4'))
#     p1.start()
#     p2 = Process(target=download_task("到台北去看雪.mp3",), )
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费%.3f秒.'%(end - start))
#
# if __name__ == '__main__':
#     mainly()

# from multiprocessing import Process
# from time import sleep
#
# counter = 0
#
# def sub_task(string):
#     global counter
#     while counter < 10:
#         print(string, end='', flush=True)
#         counter += 1
#         sleep(0.1)
# def mainly():
#     Process(target=sub_task('Ping',)).start()
#     Process(target=sub_task('Pong',)).start()
#
# if __name__ == '__main__':
#     mainly()

# from random import randint
# from threading import Thread
# from time import time, sleep
#
# def download(filename):
#     print('开始下载%s...'%filename)
#     time_to_download = randint(5, 11)
#     print('%s下载完成!耗时%d秒.'%(filename, time_to_download))
#
# def mainly():
#     start = time()
#     t1 = Thread(target=download('Python从入门到出院.doc'))
#     t1.start()
#     t2 = Thread(target=download('HIMYM.WMV'))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总耗时%.3f秒'%(end - start))
#
# if __name__ == '__main__':
#     mainly()

# from time import sleep
# from threading import Thread
#
# class Account(object):
#     def __init__(self):
#         self._balance = 0
#
#     def deposit(self, money):
#         #计算余额
#         new_balance = self._balance + money
#         # 模拟受理存款业务需要0.01秒
#         sleep(0.01)
#         # 修改余额
#         self._balance = new_balance
#
#     @property
#     def balance(self):
#         return self._balance
#
# class AddMoneytHread(Thread):
#
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
#     def run(self):
#         self._account.deposit(self._money)
#
# def mainly():
#     account = Account()
#     threads = []
#     # 创建100个存款的线程向同一个账户中存钱
#     for _ in range(100):
#         t = AddMoneytHread(account, 1)
#         threads.append(t)
#         t.start()
#         # 等所有存款的线程都执行完毕
#     for t in threads:
#         t.join()
#     print(f'账户余额是{account.balance}元.')
#
# if __name__ == '__main__':
#     mainly()

# from time import sleep
# from threading import Thread, Lock
#
# class Account(object):
#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()
#
#     def deposit(self, money):
#         # 先获取锁才能执行后续代码
#         self._lock.acquire()
#         try:
#             new_balance = self._balance + money
#             sleep(0.01)
#             self._balance = new_balance
#         finally:
#             # 在finally中执行释放锁的操作保证正常异常锁都能释放
#             self._lock.release()
#     @property
#     def balance(self):
#         return self._balance
#
# class AddMoneyThread(Thread):
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
#
#     def run(self):
#         self._account.deposit(self._money)
#
# def mainly():
#     account = Account()
#     threads = []
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#
#     print(f'账户余额是{account.balance}元.')
#
# if __name__ == '__main__':
#     mainly()

# import tkinter
# import time
# import tkinter.messagebox
#
# def download():
#     # 模拟下载任务需要花费10秒
#     time.sleep(10)
#     tkinter.messagebox.showinfo('提示', '下载完成.')
#
# def show_about():
#     tkinter.messagebox.showinfo('关于', '作者:大鱼')
#
# def mainly():
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('600x460')
#     top.wm_attributes('-topmost', True)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command = download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command = show_about)
#     button2.pack(side='right')
#     panel.pack(side = 'bottom')
#
#     tkinter.mainloop()
#
# if __name__ == '__main__':
#     mainly()

# 多进程复杂任务
# from time import time
#
# def mainly():
#     total = 0
#     number_list = [x for x in range(1, 20000)]
#     start = time()
#     for number in number_list:
#         total += number
#     print(total)
#     end = time()
#     print(f'执行时间是{end-start}S。')
#
# if __name__ == '__main__':
#     mainly()

# from multiprocessing import Process, Queue
# from random import randint
# from time import time
#
# def task_handler(curr_list, result_queue):
#     total = 0
#     for number in curr_list:
#         total += number
#     result_queue.put(total)
#
# def mainly():
#     processes = []
#     number_list = [x for x in range(1, 240001)]
#     result_queue = Queue()
#     index = 0
#     # 启动8个进程将数据切片进行运算
#     for _ in range(6):
#         p = Process(target=task_handler, args=(number_list[index:index + 40000], result_queue))
#         index += 40000
#         processes.append(p)
#         p.start()
#     # 开始记录所有进程执行完花费的时间
#     start = time()
#     for p in processes:
#         p.join()
#     # 合并执行结果
#     total = 0
#     while not result_queue.empty():
#         total += result_queue.get()
#     print(total)
#     end = time()
#     print('执行时间是:%0.5f秒.'%(end - start), sep='')
#     # sep 改变打印文本的间隔 sep='' 就是没有间隔
#
# if __name__ == '__main__':
#     mainly()
# print('a','n','bn','  end .', sep='')
# print('a','n','bn','  end .')
# print('a','n','bn','  end .', sep='22')
# print('a','n','bn','  end .', sep='bo')

# import asyncio
# import threading
#
# # @asyncio.coroutine
# # def hello():
# # Python 3.8, use "async def" instead and await
# async def hello():
#     print('%s: Hello, world!'%threading.current_thread())
#     # 休眠不会阻塞主线程因为使用了异步IO操作
#     # 注意有yield from 才会等待休眠操作执行完成
#     # yield from asyncio.sleep(3)
#     t = await asyncio.sleep(5)
#     print('%s: goodbye, world!'%threading.current_thread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# # 等待两个异步IO操作执行结束
# loop.run_until_complete(asyncio.wait(tasks))
# print('game over!')
# loop.close()

# import asyncio
# import threading
#
# # 通过asnyc修饰的函数不再是普通函数而是一个协程
# # python3.7之后有了新的关键字asnyc和await  参考上一个例子.
# async def hello():
#     print('%s: hello, world!'%threading.current_thread())
#     await asyncio.sleep(5)
#     print('%s: see you again.'%threading.current_thread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello(), hello()]
# # 等待两个异步IO操作
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# import asyncio
# async def wget(host):
#     print('wget %s...'%host)
#     connect = asyncio.open_connection(host, 80)
#     # 异步方式等待连接结果
#     reader, writer = await connect
#     header = 'GET / HTTP /1.0\r\nHost:%s\r\n\r\n'%host
#     writer.write(header.encode('utf-8'))
#     # 异步方式执行写操作
#     await writer.drain()
#     while True:
#         # 异步执行读操作
#         line = await reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s'%(host, line.decode('utf-8').rstrip()))
#     writer.close()
#
# loop = asyncio.get_event_loop()
# hosts_list = ['www.baidu.com', 'www.google.com', 'www.250.com']
# tasks = [wget(host) for host in hosts_list]
# # 下面的方法将异步IO操作放入Eventloop知道执行完毕
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# from time import sleep
# from random import random
#
# def build_deliver_man(man_id):
#     total = 0
#     while True:
#         total += 1
#         print(f'{man_id}号快递员准备接今天的第{total}单。')
#         pkg = yield
#         print(f'{man_id}号快递员收到编号为{pkg}的包裹。')
#         sleep(random()*3)
#
# def package_center(deliver_man, max_per_day):
#     num = 1
#     deliver_man.send(None)
#     while num<= max_per_day:
#         package_id = 'PKG-%d'%num
#         deliver_man.send(package_id)
#         num += 1
#         sleep(0.1)
#     deliver_man.close()
#     print('送完了。')
#
# dm = build_deliver_man(1)
# package_center(dm, 10)

# from time import sleep
# from inspect import getgeneratorstate
#
# def build_deliver_man(man_id):
#     total = 0
#     while True:
#         total += 1
#         print(f'{man_id}号快递员准备接今天的第{total}单。')
#         pkg = yield
#         print(f'{man_id}号快递收到编号为:{pkg}的包裹。')
#         sleep(0.5)
#
# def package_center(deliver_man, max_per_day):
#     num = 1
#     # 等待开始执行
#     print(getgeneratorstate(deliver_man))
#     deliver_man.send(None)
#     # 挂起状态gen_suspended 在yield表达式处暂停
#     print(getgeneratorstate(deliver_man))
#     # next(deliver_man)
#     while num <= max_per_day:
#         package_id = 'PKG-%d'%num
#         deliver_man.send(package_id)
#         num += 1
#
#     deliver_man.close()
#     # 结束状态gen_closed执行完毕
#     print(getgeneratorstate(deliver_man))
#     print('送完了。')
#
# dm = build_deliver_man(2)
# package_center(dm, 6)

# 生成器语法
# seq = [x * x for x in range(10)]
# print(seq)
#
# gen=(x * x for x in range(10))
# print(gen)
#
# for x in gen:
#     print(x)
#
# num = 10
#
# gen = (x ** y for x, y in zip(range(1, num), range(num-1, 0, -1)))
# print(gen)
#
# n = 1
# while n < num:
#     print(next(gen))
#     n += 1

# 生成器 使用yield关键字

# def fib(num):
#     n, a, b = 0, 0, 1
#     while n < num:
#         yield b
#         a, b = b, a+b
#         n += 1
#
# for x in fib(12):
#     print(x)

# 通过下面程序的执行结果可以证实 父进程在创建子进程是复制了进程及其数据结构
# 每个进程都有自己独立的内存空间 所以进程之间共享数据只能通过IPC方式

# from multiprocessing import Process, Queue
# # from time import sleep
# #
# # def sub_task(string, q):
# #     number = q.get()
# #     while number:
# #         print(f'{number}:{string}')
# #         sleep(0.2)
# #         number = q.get()
# #
# # def mainly():
# #     q = Queue(10)
# #     for number in range(1, 11):
# #         q.put(number)
# #     Process(target=sub_task('Ping', q)).start()
# #     Process(target=sub_task('Stop', q)).start()
# #
# # if __name__ == '__main__':
# #     mainly()

# import multiprocessing
# import os
#
# def sub_task(queue):
#     print(f'子进程号是：{os.getpid()}')
#     counter = 0
#     while counter < 100:
#         queue.put('Bong')
#         counter += 1
#
# if __name__ == '__main__':
#     print(f'当前进程号是：{os.getpid()}')
#     queue = multiprocessing.Queue()
#     p = multiprocessing.Process(target=sub_task(queue,))
#     p.start()
#     counter = 0
#     while counter < 1000:
#         queue.put('Ping')
#         counter += 1
#     p.join()
#     print('子任务已经完成。')
#     for _ in range(2000):
#         print(queue.get(), end='')

# 创建进程调用其他程序
# import subprocess
# import sys
#
# def mainly():
#     # 通过sys.argv获取命令行参数
#     if len(sys.argv) > 1:
#         # 第一个命令行参数是程序本身所以从第二个开始取
#         for index in range(1, len(sys.argv)):
#             try:
#                 # 通过subprocess模块的call函数启动子进程
#                 status = subprocess.call(sys.argv[index])
#             except FileNotFoundError:
#                 print(f'不能执行{sys.argv[index]}的命令')
#     else:
#         print('请使用命令行参数指定要执行的进程。')
#
# if __name__ == '__main__':
#     mainly()

# from time import time
#
# def mainly():
#     total = 0
#     number_list = [x for x in range(100, 50000)]
#     start = time()
#     for number in number_list:
#         total += number
#     print(total)
#     end = time()
#     print('Execution time:%.3fs'%(end - start))
#
# if __name__ == '__main__':
#     mainly()

# 使用多线程的情况 模拟多个下载任务

# from random import randint
# from time import time, sleep
# import atexit
# import _thread
#
# def download_task(filename):
#     print(f'开始下载{filename}...')
#     time_to_download = randint(5, 10)
#     print(f'剩余时间是{time_to_download}s')
#     sleep(time_to_download)
#     print(f'{filename}下载完成。')
#
# def shutdown_hook(start):
#     end = time()
#     print('总共耗费了%.4f秒。'%(end - start))
#
# def mainly():
#     start = time()
#     thread1 = _thread.start_new_thread(download_task('Python 从入门到退休.avi'))
#     thread2 = _thread.start_new_thread(download_task('Pekingpeking.wmv'))
#     # 注册关机钩子在程序执行结束前计算执行时间
#     atexit.register(shutdown_hook, start)
#
# if __name__ == '__main__':
#     mainly()

# 执行这里的代码会引发错误，因为主线程结束后下载线程再想执行就会出问题
# 由于_thread模块输入比较底层的线程操作而且不支持守护线程的概念
# 在实际开发中会有诸多不便，推荐使用threading模块提供高级操作进行多线程编程。

# from random import randint
# from threading import Thread
# from time import time, sleep
#
# def download_task(filename):
#     print(f'开始下载{filename}...')
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f'{filename}下载完成，总共耗费了{time_to_download}秒。')
#
# def mainly():
#     start = time()
#     thread1 = Thread(target=download_task('Python从入门到退休.apk'))
#     thread1.start()
#     thread2 = Thread(target=download_task('海尔兄弟.wmv'))
#     thread2.start()
#     thread1.join()
#     thread2.join()
#     end = time()
#     print('总共耗费了%.4f秒。'%(end - start))
#
# if __name__ == '__main__':
#     mainly()

# from random import randint
# from time import time, sleep
# import threading
#
# class DownloadTask(threading.Thread):
#     def __init__(self, filename):
#         super().__init__()
#         self._filename = filename
#
#     def run(self):
#         print(f'开始下载{self._filename}...')
#         time_to_download = randint(5, 11)
#         print(f'剩余时间{time_to_download}秒。')
#         sleep(time_to_download)
#         print(f'{self._filename}下载完成。')
#
# def mainly():
#     start = time()
#     # 将多个下载任务放到多个线程中执行
#     # 通过自定义的线程类创建线程对象， 线程启动后回调run方法。
#     thread1 = DownloadTask('python从入门到退休.ppt')
#     thread1.start()
#     thread2 = DownloadTask('Mohaha.mp3')
#     thread2.start()
#     thread1.join()
#     thread2.join()
#     end = time()
#     print('总共耗费%.4f秒、'%(end - start))
#
# if __name__ == '__main__':
#     mainly()

# import time
# import tkinter
# import tkinter.messagebox
# from threading import Thread
#
# def mainly():
#     class DownloadTaskHandler(Thread):
#
#         def run(self):
#             # 模拟下载任务需要花费10秒钟时间
#             time.sleep(10)
#             tkinter.messagebox.showinfo('提示', '完成！')
#             # 启用下载按钮
#             button1.config(state=tkinter.NORMAL)
#
#     def download():
#         # 禁用下载按钮
#         button1.config(state=tkinter.DISABLED)
#         # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行。)
#         DownloadTaskHandler(daemon=True).start()
#
#     def show_about():
#         tkinter.messagebox.showinfo('关于', '作者：赵敏')
#
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('600x400')
#     top.wm_attributes('-topmost', 1)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载。', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=download)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()
#
# if __name__ == '__main__':
#     mainly()

# 多个线程共享数据没有锁
# from time import sleep
# from threading import Thread, Lock
#
# class Account(object):
#
#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()
#     def deposit(self, money):
#         # 先获取锁才能执行后续代码
#         self._lock.acquire()
#         try:
#             new_balance = self._balance + money
#             sleep(0.5)
#             self._balance = new_balance
#         finally:
#             # 这段代码放在finally中保证释放锁的操作一定要执行。
#             self._lock.release()
#
#     @property
#     def balance(self):
#         return self._balance
#
# class GetMoneyThread(Thread):
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
#
#     def run(self):
#         self._account.deposit(self._money)
#
# def mainly():
#     account = Account()
#     threads = []
#     # 创建50个存钱的线程向同一个账户中存钱
#     for _ in range(100):
#         t = GetMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     # 等存钱的线程们都执行完毕
#     for t in threads:
#         t.join()
#     print(f"账户余额是：{account.balance}元")
#
# if __name__ == '__main__':
#     mainly()

# import time
# import threading
#
# # 多个线程共享数据有锁的情况
# class Account(object):
#
#     def __init__(self):
#         self._balance = 0
#         self._lock = threading.Lock()
#
#     def deposit(self, money):
#         # 获得锁后代码才能继续执行
#         self._lock.acquire()
#         try:
#             new_balance = self._balance + money
#             time.sleep(0.05)
#             self._balance = new_balance
#         finally:
#             # 操作完成后要释放锁
#             self._lock.release()
#
#     @property
#     def balance(self):
#         return self._balance
#
# if __name__ == '__main__':
#     account = Account()
#     # 创建50个存钱线程向同一个账号存钱
#     for _ in range(55):
#         threading.Thread(target=account.deposit, args=(1,)).start()
#         # 等所有的存钱线程都执行完毕
#     time.sleep(2)
#     print(f'账户余额是{account.balance}元。')

# from random import randint
# from time import time, sleep
#
# def download_task(filename):
#     print(f"开始下载{filename}...")
#     time_to_download = randint(6, 12)
#     sleep(time_to_download)
#     print(f"下载完成，耗费了{time_to_download}秒。")
#
# def mainly():
#     start = time()
#     download_task('Python从入门到入墓。')
#     download_task('Peking cold.mp3')
#     end = time()
#     print(f'总共耗费了{end - start}秒。')
#
# if __name__ == '__main__':
#     mainly()

# import time
# import tkinter
# import tkinter.messagebox
#
# def download():
#     # 模仿下载任务需要花费10秒
#     time.sleep(10)
#     tkinter.messagebox.showinfo('提示', '完成')
#
# def show_about():
#     tkinter.messagebox.showinfo('关于', '作者：周芷若')
#
# def mainly():
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('500x450')
#     top.wm_attributes('-topmost', True)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command = download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command = show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()
#
# if __name__ == '__main__':
#     mainly()

# import time
# from threading import Thread, Lock
#
# class Account(object):
#
#     def __init__(self, balance=0):
#         self._balance = balance
#         self._lock = Lock()
#
#     @property
#     def balance(self):
#         return self._balance
#
#     def deposit(self, money):
#         if money > 0:
#             self._lock.acquire()
#             try:
#                 new_balance = self._balance + money
#                 time.sleep(0.02)
#                 self._balance = new_balance
#             finally:
#                 self._lock.release()
#
# class GotMoneyThread(Thread):
#
#     def __init__(self, account):
#         super().__init__()
#         self._account = account
#
#     def run(self):
#         self._account.deposit(1)
#
# def mainly():
#     account = Account(0)
#     tlist = []
#     for _ in range(100):
#         t = GotMoneyThread(account)
#         tlist.append(t)
#         t.start()
#     for t in tlist:
#         t.join()
#
#     print(f'账户余额是{account.balance}元。')
#
# if __name__ == '__main__':
#     mainly()

# from random import randint
# from threading import Thread
# from time import sleep
#
# import pygame
# class Color(object):
#     Black = (0, 0, 0)
#     White = (255, 255, 255)
#     Gray = (230, 230, 232)
#
#     @staticmethod
#     def random_color():
#         r = randint(0, 255)
#         g = randint(0, 249)
#         b = randint(0, 252)
#         return r, g, b
#
# class Car(object):
#
#     def __init__(self, x, y, color):
#         self._x = x
#         self._y = y
#         self._color = color
#
#     def move(self):
#         if self._x + 80 < 950:
#             self._x += randint(1, 10)
#
#     def draw(self, screen):
#         pygame.draw.rect(screen, self._color, (self._x, self._y, 80, 40), 0)
#
# def mainly():
#
#     class BackgroundTask(Thread):
#         def run(self):
#             while True:
#                 screen.fill(Color.Gray)
#                 pygame.draw.line(screen, Color.Black, (130, 0), (130, 600), 4)
#                 pygame.draw.line(screen, Color.Black, (950, 0), (950, 600), 4)
#                 for car in cars:
#                     car.draw(screen)
#                 pygame.display.flip()
#                 sleep(0.05)
#                 for cat in cars:
#                     car.move()
#
#     cars = []
#     for index in range(5):
#         temp = Car(50, 50 + 120*index, Color.random_color())
#         cars.append(temp)
#
#     pygame.init()
#     screen = pygame.display.set_mode((1000, 600))
#     BackgroundTask(daemon=True).start()
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#     pygame.quit()
#
# if __name__ == '__main__':
#     mainly()