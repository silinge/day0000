# 排序算法 选择 冒泡和归并 和查找算法 顺序和折半。
# def select_sort(origin_items, comp=lambda x, y:x<y):
#     # 简单的选择排序
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         min_index = i
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#     return items

# def bubble_sort(origin_items, comp=lambda x, y: x > y):
#     # 高质量冒泡排序 搅拌排序
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         swapped = False
#         for j in range(i, len(items) - 1 - i):
#             if comp(items[j], items[j + 1]):
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#             for j in range(len(items) - 2 - i, i, -1):
#                 if comp(items[j - 1], items[j]):
#                     items[j], items[j - 1] = items[j - 1], items[j]
#                     swapped = True
#         if not swapped:
#             break
#     return items

# def merge_sort(items, comp=lambda x, y: x <= y):
#     # 归并排序 分治法
#     if len(items) < 2:
#         return items[:]
#     mid = len(items) // 2
#     left = merge_sort(items[:mid], comp)
#     right = merge_sort(items[mid:], comp)
#     return merge(left, right, comp)
# 接着merge交代一下
# def merge(items1, items2, comp):
#     # 合并 ，将两个有序的列表合并成一个有序的列表
#     items = []
#     index1, index2 = 0, 0
#     while index1 < len(items1) and index2 < len(items2):
#         if comp(items1[index1], items2[index2]):
#             items.append(items1[index1])
#             index1 += 1
#         else:
#             items.append(items2[index2])
#             index2 += 1
#     items += items1[index1:]
#     items += items2[index2:]
#     return items

# def seq_search(items, key):
#     # 顺序查找
#     for index, item in enumerate(items):
#         if item == key:
#             return index
#     return -1

# def bin_search(items, key):
#     # 折半查找
#     start, end = 0, len(items) - 1
#     while start <= end:
#         mid = (start - end)//2
#         if key > items[mid]:
#             start = mid + 1
#         elif key < items[mid]:
#             end = mid - 1
#         else:
#             return mid
#     return -1

# 使用推导式（生成式）语法
# prices = {
#     'APPL':199.02,
#     'GOOG':1187.32,
#     'IBMD':146.24,
#     'ORCL':44.32,
#     'ACM':166.09,
#     'FACE':219.11,
#     'SYMC':20.15
# }
#
# # 用股票价格大于100元的股票构造一个新的字典
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)

# 嵌套式列表
# names = ['诸葛亮', '郭靖', '张三丰', '孙悟空', '武松']
# courses = ['哲学', '物理', '生物']
# # 录入5个学生的三门课程成绩
# # 错误 参考http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses)] * len(names)
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
# print(scores)

# import heapq
# list1 = [34, 25, 14, 89, 63, 56, 78, 55, 90]
# list2 = [
#     {'name':'IBM', 'shares':100, 'price':90.3},
#     {'name':'AAPL', 'shares':50, 'price':543.33},
#     {'name':'FB', 'shares':200, 'price':220.3},
#     {'name':'HBO', 'shares':35, 'price':31.83},
#     {'name':'YHOO', 'shares':40, 'price':16.30},
#     {'name':'ACME', 'shares':80, 'price':110.73}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x:x['price']))
# print(heapq.nlargest(2, list2, key=lambda x:x['shares']))

# 迭代工具 排列组合笛卡尔积
# import itertools
#
# itertools.permutations('ABCDEF')
# itertools.combinations('ABCDHIJ', 3)
# itertools.product('XYZOPQ', '123')
# 找出序列中出现次数最多的元素
# from collections import Counter
#
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the'
# ]
#
# counter = Counter(words)
# print(counter.most_common(3))

# 穷举法 验证所有可能 直到找到答案
# 贪婪法 在对问题求解时 总是做出在当前看来
# 最好的选择 不追其最优解 快速找到满意答案
# 分治法 把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，知道可以直接求解的程度，最后合并到原来的问题上的最终答案
# 回溯法 试探法 按选有条件搜索 当到某一步选择并不优或者不达标则退回重选
# 动态规划 基本思想是将问题分解成子问题，先求解保存自子问题 避免大量的重复计算。

# 百钱百鸡 和五人分鱼
# 公鸡5元 母鸡3元 小鸡意愿三只
# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(f'{x}只公鸡，{y}只母鸡，{z}只小鸡。')

# 贪婪法 不追求最优解 快速找到符合条件的答案不追求最佳。
# class Thing(object):
#     '''物品'''
#
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     @property
#     def value(self):
#         '''价格重量比'''
#         return self.price / self.weight
#
# def input_thing():
#     '''输入物品信息'''
#     name_str, price_str, weight_str = input("依次输入物品的名称，价格和重量： ").split()
#     return name_str, input(price_str), int(weight_str)
#
# def mainly():
#     max_weight, num_of_things = map(int, input("价格和重量比： ").split())
#     all_things = []
#     for _ in range(num_of_things):
#         all_things.append(Thing(*input_thing()))
#     all_things.sort(key=lambda x: x.value, reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight <= max_weight:
#             print(f'小偷拿走了{thing.name}')
#             total_weight += thing.weight
#             total_price += thing.price
#     print(f"总价值：{total_price}委内瑞拉币。")
#
# if __name__ == '__main__':
#     mainly()

# 快速排序 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
# def quick_sort(origin_items, comp=lambda x, y: x <= y):
#     items = origin_items[:]
#     _quick_sort(items, 0, len(items) - 1, comp)
#     return items
#
# def _quick_sort(items, start, end, comp):
#     if start < end:
#         pos = _partition(items, start, end, comp)
#         _quick_sort(items, start, pos - 1, comp)
#         _quick_sort(items, pos + 1, end, comp)
#
# def _partition(items, start, end, comp):
#     pivot = items[end]
#     i = start - 1
#     for j in range(start, end):
#         if comp(items[j], pivot):
#             i += 1
#             items[i], items[j] = items[j], items[i]
#     items[i + 1], items[end] = items[end], items[i + 1]
#     return i + 1

# 递归回溯法，试探法 按选优条件向前搜索 当搜索到某一步 发现原先选择并不优或达不到目标是就退回。
# import sys
# import time
# SIZE = 5
# total = 0
#
# def print_board(board):
#     for row in board:
#         for col in row:
#             print(str(col).center(4), end='')
#         print()
#
# def patrol(board, row, col, step=1):
#     if row >= 0 and row < SIZE and \
#         col >= 0 and col < SIZE and \
#         board[row][col] == 0:
#         board[row][col] = step
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f'第{total}种走法。')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col] = 0
# def mainly():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     patrol(board, SIZE - 1, SIZE - 1)
#
# if __name__ == '__main__':
#     mainly()

# def fib(num, temp={}):
#     # 递归计算
#     if num in (1, 2):
#         return 1
#     try:
#         return temp[num]
#     except KeyError:
#         temp[num] = fib(num - 1) + fib(num - 2)
#         return temp[num]
#
# print(fib(10))
# 1123581321345589144233

# 动态规划 子列表元素之和的最大值
# def mainly():
#     items = list(map(int, input().split()))
#     size = len(items)
#     overall, partial = {}, {}
#     overall[size - 1] = partial[size - 1] = items[size - 1]
#     for i in range(size - 2, -1, -1):
#         partial[i] = max(items[i], partial[i + 1] + items[i])
#         overall[i] = max(partial[i], overall[i + 1])
#     print(overall[0])
#
# if __name__ == '__main__':
#     mainly()

# items1 = list(map(lambda x: x ** 2, filter(lambda x:x % 2, range(1, 10))))
# items2 = [x ** 2 for x in range(1, 10) if x % 2]
# import time
# def record_time(func):
#     # 自定义装饰函数的装饰器
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         print(f'{func.__name__}:{time() - start()}秒。')
#         return result
#     return wrapper

# from functools import wraps
# from time import time
#
# def record(output):
#     # 自定义带参数的装饰器
#
#     def decorate(func):
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time()
#             result = func(*args, **kwargs)
#             output(func.__name__, time() - start)
#             return result
#
#         return wrapper
#
#     return decorate

# from functools import wraps
# from time import time
#
# class Record():
#     # 自定义装饰器类
#
#     def __init__(self, output):
#         self.output = output
#
#     def __call__(self, func):
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time()
#             result = func(*args, **kwargs)
#             self.output(func.__name__, time() - start)
#             return result
#
#         return wrapper
#

# from functools import wraps
#
# def singleton(cls):
#     # 装饰类的装饰器
#     instances = {}
#
#     @wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrapper
#
# @singleton
# class President():
#     '''总统类'''
#     pass

# from functools import wraps
# from threading import Lock
#
# def singleton(cls):
#     '''线程安全的单例装饰器'''
#     instances = {}
#     locker = Lock()
#
#     @wraps(cls)
#     def wrapper(*args, **kwargs)
#         if cls not in instances:
#             with locker:
#                 if cls not in instances:
#                     instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrapper
#
# from abc import ABCMeta, abstractmethod
#
# class Employee(metaclass=ABCMeta):
#     '''员工类'''
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def get_salary(self):
#         '''结算月薪'''
#         pass
# class Manager(Employee):
#     '''部门经理'''
#     def get_salary(self):
#         return 15000.0
#
# class Programmer(Employee):
#     '''程序员类 继承雇员类的属性'''
#     def __init__(self, name, working_hour=0):
#         self.working_hour = working_hour
#         super().__init__(name)
#
#     def get_salary(self):
#         return 200.0 * self.working_hour
#
# class Salesman(Employee):
#     '''销售员类'''
#
#     def __init__(self, name, sales_amount):
#         self.sales_amount = sales_amount
#         super().__init__(name)
#
#     def get_salary(self):
#         return 1800.0 + self.sales_amount * 0.05
#
# class EmployeeFactory():
#     '''创建员工的工厂'''
#
#     @staticmethod
#     def create(emp_type, *args, **kwargs):
#         '''创建员工'''
#
#         emp_type = emp_type.upper()
#         emp = None
#         if emp_type == 'M':
#             emp = Manager(*args, **kwargs)
#         elif emp_type == 'P':
#             emp = Programmer(*args, **kwargs)
#         elif emp_type == 'S':
#             emp = Salesman(*args, **kwargs)
#         return emp
#
# def mainly():
#     '''主函数'''
#     emps = [
#         EmployeeFactory.create('M', '曹操'),
#         EmployeeFactory.create('P', '张飞', 140),
#         EmployeeFactory.create('P', '周瑜', 90),
#         EmployeeFactory.create('S', '司马懿', 100000),
#     ]
#     for emp in emps:
#         print(f'{emp.name}:{emp.get_salary()}元。')
#
# if __name__ == '__main__':
#     mainly()

# from enum import Enum, unique
# import random
#
# @unique
# class Suite(Enum):
#     '''花色'''
#     SPADE, HEART, CLUB, DIAMOND = range(4)
#
#     def __lt__(self, other):
#         return self.value < other.value
#
# class Card():
#     '''牌'''
#
#     def __init__(self, suite, face):
#         '''初始化方法'''
#         self.suite = suite
#         self.face = face
#
#     def show(self):
#         '''显示牌面'''
#         suites = ['B','R','F','S']
#         faces = ['','A','2','3','4','5','6','7','8','9','10','J','Q','K']
#         return f'{suites[self.suite.value]}{faces[self.face]}'
#
#     def __str__(self):
#         return self.show()
#     def __repr__(self):
#         return self.show()
#
# class Poker():
#     # 扑克
#     def __init__(self):
#         self.index = 0
#         self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
#
#     def shuffle(self):
#         # 洗牌
#         random.shuffle(self.cards)
#         self.index = 0
#     def deal(self):
#         '''发牌'''
#         card = self.cards[self.index]
#         self.index += 1
#         return card
#     @property
#     def has_more(self):
#         return self.index < len(self.cards)
#
# class Player():
#     '''玩家'''
#
#     def __init__(self, name):
#         self.name = name
#         self.cards = []
#
#     def get_one(self, card):
#         # more牌
#         self.cards.append(card)
#
#     def sort(self, comp=lambda card: (card.suite, card.face)):
#         '''整理手上的牌'''
#         self.cards.sort(key=comp)
#
# def mainly():
#     # 主函数
#     poker = Poker()
#     poker.shuffle()
#     players = [Player('姜子牙'), Player('李白'), Player('郭靖'), Player('如懿')]
#     while poker.has_more:
#         for player in players:
#             player.get_one(poker.deal())
#
#     for player in players:
#         player.sort()
#         print(player.name, end=':')
#         print(player.cards)
#
# if __name__ == '__main__':
#     mainly()

# python使用自动化内存管理，该机制以引用计算为基础。同时引入标记-清除和分代收集两种机制为辅的策略。

# typedef struct_object {
    # 引用计数
    # int ob_refcnt
    # 对象指针
    # struct_typeobject *ob_type;
# }PyObject;

# 增加引用计数的宏定义
# define Py_INCREF(op) ((op)->ob_refcnt++)
# 减少引用计数的宏定义
# define Py_DECREF(op)
# if (--(op)->ob_refcnt != 0)
#     ;
# else
#     _Py_Dealloc((PyObject *)(op))

# class SetOnceMappingMixin:
#     '''自定义混入类'''
#     __slots__ = ()
#
#     def __setitem__(self, key, value):
#         if key in self:
#             raise KeyError(str(key) + ' already set')
#         return super().__setitem__(key, value)
#
# class SetOnceDict(SetOnceMappingMixin, dict):
#     '''自定义字典'''
#     pass
# my_dict = SetOnceDict()
# try:
#     my_dict['username'] = '大长今'
#     my_dict['username'] = '雅典娜'
# except KeyError:
#     pass
#
# print(my_dict)

# import threading
#
# class SingletonMeta(type):
#     '''自定义元类'''
#
#     def __init__(cls, *args, **kwargs):
#         cls.__instance = None
#         cls.__lock = threading.Lock()
#         super().__init__(*args, **kwargs)
#
#     def __call__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             with cls.__lock:
#                 if cls.__instance is None:
#                     cls.__instance = super().__call__(*args, **kwargs)
#         return cls.__instance
#
# class President(metaclass=SingletonMeta):
#     '''总统 单例类'''
#
# pass

# 可插拔的哈希算法
# class StreamHasher():
#     # 哈希摘要生成器 策略模式
#
#     def __init__(self, alg='md5', size=4096):
#         self.size = size
#         alg = alg.lower()
#         self.hasher = getattr(__import__('hashlib'), alg.lower())()
#
#     def __call__(self, stream):
#         return self.to_digest(stream)
#
#     def to_digest(self, stream):
#         '''生成十六进制形式的摘要'''
#         for buf in iter(lambda : stream.read(self.size), b''):
#             self.hasher.update(buf)
#
#         return self.hasher.hexdigest()
#
# def mainly():
#     hasher1 = StreamHasher()
#     with open('Python-3.7.1.tgz', 'rb') as stream:
#         print(hasher1.to_digest(stream))
#
#     hasher2 = StreamHasher('sha1')
#     with open('Python-3.7.1.tgz', 'rb') as stream:
#         print(hasher2(stream))
#
# if __name__ == '__main__':
#     mainly()

# def fib(num):
#     '''生成器'''
#     a, b = 0, 1
#     for _ in range(num):
#         a, b = b, a + b
#         yield a
#
# class Fib(object):
#     '''迭代器'''
#     def __init__(self, num):
#         self.num = num
#         self.a, self.b = 0, 1
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx < self.num:
#             self.a, self.b = self.b, self.a + self.b
#             self.ibx += 1
#             return self.a
#
#         raise StopIteration()

# 并发进程 多线程 多进程 异步IO

# import glob
# import os
# import threading
#
# from PIL import Image
# PREFIX = 'thumbails'
#
# def generate_thumbnail(infile, size, format='PNG'):
#     '''成指定图片文件的缩略图'''
#     file, ext=os.path.splitext(infile)
#     file = file[file.rfind('/') + 1:]
#     outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
#     img = Image.open(size, Image.ANTIALIAS)
#     img.save(outfile, format)
#
# def mainly():
#     if not os.path.exists(PREFIX):
#         os.mkdir(PREFIX)
#     for infile in glob.glob('images/*.png'):
#         for size in (32, 64, 128):
#     # '''创建并启动线程'''
#             threading.Thread(
#                 target=generate_thumbnail,
#                 args=(infile, (size, size))
#             ).start()
#
# if __name__ == '__main__':
#     mainly()
# 多个线程竞争资源情况
# import time
# import threading
# from concurrent.futures import ThreadPoolExecutor
#
# class Account(object):
#     # 银行账户
#
#     def __init__(self):
#         self.balance = 0.0
#         self.lock = threading.Lock()
#
#     def deposit(self, money):
#         # 通过锁保护临界资源
#         with self.lock:
#             new_balance = self.balance + money
#             time.sleep(0.005)
#             self.balance = new_balance
#
# class AddMoneyThread(threading.Thread):
#     # 自定义线程类
#     def __init__(self, account, money):
#         self.account = account
#         self.money = money
#         # 自定义线程的初始化方法必须调用父类的初始化方法
#         super().__init__()
#
#     def run(self):
#         # 线程启动之后要执行的操作
#         self.account.deposit(self.money)
#
# def mainly():
#     # 主函数
#     account = Account()
#     # 创建线程池
#     pool = ThreadPoolExecutor(max_workers=10)
#     futures = []
#     for _ in range(100):
#         '''
#         创建线程的第一种方式
#         threading.Thread(
#             target=account.deposit, args=(1, )
#             ).start()
#         创建线程的第二种方式
#         AddMoneyThread(account, 1).start()
#         创建线程的第三种方式
#         调用线程池的线程来执行特定的任务
#         '''
#         future = pool.submit(account.deposit, 1)
#         futures.append(future)
#
#     # 关闭线程池
#     pool.shutdown()
#     for future in futures:
#         future.result()
#     print(account.balance)
#
# if __name__ == '__main__':
#     mainly()

'''启动5个线程向账户里面存钱，5个线程从账号取钱 取钱余额不足就暂停进行等待，
暂停的时候释放锁 而存钱的进程将钱存进去后要通知取钱的线程，使其从暂停的状态被唤醒，可以使用threading模块的Condition来实现线程调度，
该对象也是基于锁来创建的。代码如下所示：'''
'''
多个线程竞争一个资源，保护临界资源-锁（Lock/RLock)
多个线程竞争多个资源（线程数>资源数 信号量semaphore
多个线程的调度，暂停线程执行/唤醒等待中的线程 Condition
'''
#
# from concurrent.futures import ThreadPoolExecutor
# from random import randint
# from time import sleep
#
# import threading
#
# class Account():
#     '''银行账户'''
#     def __init__(self, balance=0):
#         self.balance = balance
#         lock = threading.Lock()
#         self.condition = threading.Condition(lock)
#
#     def withdraw(self, money):
#         '''取钱'''
#         with self.condition:
#             while money > self.balance:
#                 self.condition.wait()
#             new_balance = self.balance - money
#             sleep(0.02)
#             self.balance = new_balance
#
#     def deposit(self, money):
#         '''存钱'''
#         with self.condition:
#             new_balance = self.balance + money
#             sleep(0.02)
#             self.balance = new_balance
#             self.condition.notify_all()
#
# def add_money(account):
#     while True:
#         money = randint(5, 10)
#         account.deposit(money)
#         print(threading.current_thread().name, ':', money, '====>', account.balance)
#         sleep(0.5)
#
# def sub_money(account):
#     while True:
#         money = randint(10, 300)
#         account.withdraw(money)
#         print(threading.current_thread().name,':',money,'====>',account.balance)
#         sleep(1)
#
# def mainly():
#     account=Account()
#     with ThreadPoolExecutor(max_workers=10) as pool:
#         for _ in range(5):
#             pool.submit(add_money, account)
#             pool.submit(sub_money, account)
#
# if __name__ == '__main__':
#     mainly()
''' 多进程可以有效的解决GIL的问题，实现多进程主要的类Process， 其他辅助的类跟threading模块中的类似
进程间的共享数据可以使用管道，套接字等，在multiprocessing模块中有一个Queue类，它基于管道和锁的机制
提供多个进程共享的队列。

多进程和进程池的使用
多线程因为GIL的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑使用多进程
time python3 example22.py
real 
user
sys
使用
'''
# import  concurrent.futures
# import math
#
# primes = [
#     1116281,
#     1297337,
#     104395303,
#     472882027,
#     533000389,
#     817504243,
#     982451653,
#     112272535095293,
#     112582705942171,
#     1122722535095293,
#     115280095190773,
#     115797848077099,
#     1099726899285419
# ]*5
#
# def is_prime(n):
#     '''判断素数'''
#     if n % 2 == 0:
#         return False
#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# def mainly():
#     '''主函数'''
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         for number, prime in zip(primes, executor.map(is_prime, primes)):
#             print(f'{number} is prime: {prime}')
#
# if __name__ == '__main__':
#     mainly()

'''异步处理 从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，我们并不能保证
任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否愿意将cpu处理的时间让位给另一项
任务，异步任务通常通过多任务协作处理的方式来实现，由于执行时间和顺序不确定，因此需要通过回调式编程或者
future对象来获取任务执行的结果。python3通过asyncio模块和await async关键字来支持异步处理。'''

# import asyncio
#
# def num_generator(m, n):
#     '''指定范围的数字生成器'''
#     yield from range(m, n+1)
#
# async def prime_filter(m, n):
#     '''素数过滤器'''
#     primes = []
#     for i in num_generator(m, n):
#         flag = True
#         for j in range(2, int(i**0.5 + 1)):
#             if i % j == 0:
#                 flag = False
#                 break
#         if flag:
#             print('Prime =>', i)
#             primes.append(i)
#         await asyncio.sleep(0.05)
#     return tuple(primes)
#
# async def square_mapper(m, n):
#     '''平方映射器'''
#     squares = []
#     for i in num_generator(m, n):
#         print('Square =>', i*i)
#         squares.append(i*i)
#
#         await asyncio.sleep(0.001)
#     return squares
#
# def mainly():
#     '''主函数'''
#     loop = asyncio.get_event_loop()
#     future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
#     future.add_done_callback(lambda x: print(x.result()))
#     loop.run_until_complete(future)
#     loop.close()
#
# if __name__ == '__main__':
#     mainly()

# python 第三方库aiohttp 但是3.8还不支持
# import asyncio
# import re
# import aiohttp
#
# PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
# async def fetch_page(session, url):
#     async with session.get(url, ssl=False) as resp:
#         return await resp.text()
#
# async def show_title(url):
#     async with aiohttp.ClientSeeion() as session:
#         html = await fetch_page(session, url)
#         print(PATTERN.search(html).group('title'))
#
# def mainly():
#     urls = ('https://www.pthon.org/',
#             'https://git-scm.com/'
#             'https://www.jd.com/'
#             'https://www.z.com/'
#             'https://www.taobao.com/'
#             )
#     loop = asyncio.get_event_loop()
#     tasks = [show_title(url) for url in urls]
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()
#
# if __name__ == '__main__':
#     mainly()
'''
查找 顺序查找和二分查找
O(c) 常量时间复杂度 哈希存储 布隆过滤器
O(log_2 n)对数时间复杂度 折半查找
O(n) 线性时间复杂度 顺序查找
O(n*log_2 n):对数线性时间复杂度 高级排序算法 归并排序 快速排序
O(n**2)平方时间复杂度 简单排序算法 冒泡算法 选择排序 插入排序
O(n**3)立方时间复杂度 Floyd算法 矩阵乘法运算
O(2** n) 几何级数时间复杂度 汉诺塔
O(3** n) 几何级数时间复杂度
O(n！) 阶乘时间复杂度 旅行经销商问题
'''
# import numpy
# from math import log2, factorial
# from matplotlib import pyplot
#
# def seq_search(items: list, elem) -> int:
#     '''顺序查找'''
#     for index, item in enumerate(items):
#         if elem == item:
#             return index
#     return -1
#
# def bin_search(items, elem):
#     '''二分查找'''
#     start, end = 0, len(items) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if elem > items[mid]:
#             start = mid + 1
#         elif elem < items[mid]:
#             end = mid - 1
#         else:
#             return mid
#     return -1
#
# def mainly():
#     num = 6
#     styles = ['r-','g-*',"b-o","y-x","c-^","m-+","k-d"]
#     legends = ["对数",'线性',"线性对数","平方","立方","几何级数","阶乘"]
#     x_data = [x for x in range(1, num+1)]
#     y_data1 = [log2(y) for y in range(1, num + 1)]
#     y_data2 = [y for y in range(1, num + 1) ]
#     y_data3 = [y * log2(y) for y in range(1, num + 1)]
#     y_data4 = [y ** 2 for y in range(1, num + 1)]
#     y_data5 = [y ** 3 for y in range(1, num + 1)]
#     y_data6 = [3 ** y for y in range(1, num + 1)]
#     y_data7 = [factorial(y) for y in range(1, num + 1)]
#     y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
#     for index, y_data in enumerate(y_datas):
#         pyplot.plot(x_data, y_data, styles[index])
#     pyplot.legend(legends)
#     pyplot.xticks(numpy.arange(1, 7, step=1))
#     pyplot.yticks(numpy.arange(0, 751, step=50))
#     pyplot.show()
#
# if __name__ == '__main__':
#     mainly()

# 排序 冒泡排序 选择排序 归并排序 快速排序
# 冒泡排序 O(n ** 2) 两两比较 大的下沉
'''
# 35,97,12,68,55,63,81,44
# 35,12,68,55,63,81,44,[97]
# 35,12,68,55,63,44,[81]
# 35,12,55,63,44,[68]
# 
# 选择排序 O(n**2)每次从剩下元素中选择最小的
# 归并排序 O(n * log_2 n) 高级排序算法
# 35,97,12,68,55,73,81,40
# [35,97,12,68],[55,73,81,40]
# [35,97],[12,68],[55,73],[81,40]
# [35],[97],[12],[68],[55],[73],[81],[40]
# [35,97],[12,68],[55,73],[40,81]
# [12,35,68,97],[40,55,73,81]
# [12,35,40,55,68,73,81,97]
# 
# 快速排序 以枢轴为界将列表中的元素划分为两个部分，左边比枢轴小，右边都比枢轴大
# 35，97，12，68，55，73，81，40
# 35,12,[40],68,55,73,81,[97]
# [12],35,[40],55,[68],73,81,[97]
# [12],35,[40],55,[68],73,[81],[97]
# '''
#
# class Person(object):
#     '''人'''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name}:{self.age}'
#
#     def __repr__(self):
#         return self.__str__()
#
# def select_sort(origin_items, comp=lambda x, y: x < y):
#     '''简单选择排序'''
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         min_index = 1
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#
#     return items
#
# '''
# 函数的设计要尽量无副作用 不影响调用者
# 9 1 2 3 4 5 6 7 8
# 9 2 3 4 5 6 7 8 1
# 前面的参数叫做位置参数，传参时只需要对号入座即可
# 后面的参数叫命名关键字参数，传参时必须给出参数名和参数值
# *args 可变参数 元组
# **kwargs 关键字参数，字典
# '''
#
# def bubble_sort(origin_items, *, comp=lambda x, y: x > y):
#     '''冒泡排序'''
#     items = origin_items[:]
#     for i in range(1, len(items)):
#         swapped = False
#         for j in range(i - 1, len(items) - i):
#             if comp(items[j], items[j + 1]):
#                 items[j], items[j + 1] = items[j +1], items[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#             for j in range(len(items) - i - 1, i -1, -1):
#                 if comp(items[j - 1], items[j]):
#                     items[j], items[j - 1] = items[j - 1], items[j]
#                     swapped = True
#         if not swapped:
#             break
#     return items
#
# def merge_sort(items, comp=lambda x, y: x <= y):
#     '''归并排序'''
#     if len(items) < 2:
#         return items[:]
#     mid = len(items) // 2
#     left = merge_sort(items[:mid], comp)
#     right = merge_sort(items[mid:], comp)
#     return merge(left, right, comp)
#
# def merge(items1,items2,comp=lambda x, y: x <= y):
#     '''合并 将两个有序列表合并成一个新的有序列表'''
#     items = []
#     index1,index2 = 0, 0
#     while index1 < len(items1) and index2 < len(items2):
#         if comp(items1[index1], items2[index2]):
#             items.append(items1[index1])
#             index1 += 1
#         else:
#             items.append(items2[index2])
#             index2 += 1
#     items += items1[index1:]
#     items += items2[index2:]
#     return items
#
# def quick_sort(origin_items, comp=lambda x, y: x <= y):
#     '''快速排序'''
#     items = origin_items[:]
#     _quick_sort(items, 0, len(items) - 1, comp)
#     return items
#
# def _quick_sort(items, start, end, comp):
#     '''划分'''
#     if start < end:
#         pos = _partition(items, start, end, comp)
#         _quick_sort(items, start, pos - 1, comp)
#         _quick_sort(items, pos + 1, end, comp)
#
# def _partition(items, start, end, comp):
#     '''划分'''
#     pivot = items[end]
#     i = start - 1
#     for j in range(start, end):
#         if comp(items[j], pivot):
#             i += 1
#             items[i], items[j] = items[j], items[i]
#
#     items[i + 1], items[end] = items[end], items[i + 1]
#     return i + 1
#
# def mainly():
#     '''主函数'''
#     items = [35, 97, 12, 68, 55, 73, 81, 40]
#     print(bubble_sort(items))
#     print(select_sort(items))
#     print(merge_sort(items))
#     print(quick_sort(items))
#     items2 = [
#         Person('ZHOU', 32),Person('QIAN', 22),
#         Person('SUN', 34), Person('LI',18)
#     ]
#
#     print(bubble_sort(items2, comp=lambda p1, p2:p1.age > p2.age))
#     print(select_sort(items2, comp=lambda p1, p2:p1.name < p2.name))
#     print(merge_sort(items2, comp=lambda p1, p2:p1.age <= p2.age))
#     print(quick_sort(items2, comp=lambda p1, p2:p1.age <= p2.age))
#     items3 = ['apple', 'orange', 'watermelon', 'durian', 'pear']
#     print(bubble_sort(items3))
#     print(bubble_sort(items3, comp = lambda x, y: len(x) > len(y)))
#     print(merge_sort(items3))
#
# if __name__ == '__main__':
#     mainly()

'''
函数递归调用 函数直接或间接的调用了自身
收敛条件
递归公式
n! = n * (n - 1)!
f(n) = f(n - 1) + f(n - 2)
1 1 2 3 5 8 13 21 34 55
'''
#
# from contextlib import contextmanager
# from time import perf_counter
#
# def fac(num):
#     '''阶乘'''
#     assert num >= 0
#     if num in (0, 1):
#         return 1
#     return num * fac(num - 1)
#
# def fib2(num):
#     '''普通函数'''
#     a, b = 1, 1
#     for _ in range(num - 1):
#         a, b = b, a+b
#     return a
#
# def fib3(num):
#     '''生成器'''
#     a, b = 0, 1
#     for _ in range(num - 1):
#         a, b = b, a + b
#     yield a
#
# '''动态规划 保存可能进行重复运算的中间结果 空间换时间'''
#
# def fib(num, results={}):
#     '''斐波那契'''
#     assert num>0
#     if num in (1, 2):
#         return 1
#     try:
#         return results[num]
#     except KeyError:
#         results[num] = fib(num - 1) + fib(num - 2)
#         return results[num]
#
# @contextmanager
# def timer():
#     try:
#         start = perf_counter()
#         yield
#     finally:
#         end = perf_counter()
#         print(f"{end - start}秒。")
#
# def mainly():
#     for val in fib3(20):
#         print(val)
#
#     gen = fib3(20)
#     for _ in range(10):
#         print(next(gen))
#
#     for num in range(1, 121):
#         with timer():
#             print(f"{num}:{fib(num)}")
#         print(fac(5))
#         print(fac(-6))
#
# if __name__ == '__main__':
#     mainly()

'''
贪婪法 在对问题求解时 总是做出在当前看来是最好的选择
不追求最优解，快速找到满意解
'''
# class Thing(object):
#
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     @property
#     def value(self):
#         return self.price / self.weight
#
# def input_thing():
#     '''输入物品信息'''
#     name_str, price_str, weight_str = input().split()
#     return name_str, int(price_str), int(weight_str)
#
# def mainly():
#     max_weight, num_of_things = map(int, input().split())
#     all_things = []
#     for _ in range(num_of_things):
#         all_things.append(Thing(*input_thing()))
#     all_things.sort(key=lambda x:x.value, reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight <= max_weight:
#             print(f"小偷拿走了{thing.name}")
#             total_weight += thing.weight
#             total_price += thing.price
#
#     print(f"总价值：{total_price}委内瑞拉币。")
#
# if __name__ == '__main__':
#     mainly()

# 200 4
# 西瓜 20 300
# 牛肉 2 80
# 手机 1 4000
# 皮鞋 3 500
# 小偷拿走了牛肉
# 总价值：2委内瑞拉币。

'''
递归回溯法 试探法 按选优条件向前搜索 当搜索到某一步，发现
原先选择并不优或达不到目标时，就退一步重新选择，骑士巡逻
'''

# import os
# import sys
# import time
# SIZE = 5
# total = 0
#
# def print_board(board):
#     os.system('cls')
#     for row in board:
#         for col in row:
#             print(str(col).center(4), end='')
#         print()
#
# def patrol(board, row, col, step=1):
#     if row >= 0 and row < SIZE and \
#         col >= 0 and col < SIZE and \
#         board[row][col] == 0:
#         board[row][col] = step
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f"第{total}种走法： ")
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 2, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col]=0
#
# def mainly():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     patrol(board, SIZE - 1, SIZE - 1)
#
# if __name__ == '__main__':
#     mainly()

'''
编码和解码base64
0-9A-Za-z+/
1100 0101 1001 0011 0111 0110
00110001 00011001 00001101 00110110
base64
b64encode / b64decode

序列化和反序列化
序列化将对象变成字节序列（bytes)或者字符序列str串行化/腌咸菜
反序列化 把字节序列或者字符序列还原成对象
python库
json 字符形式的序列化
pickle 字节形式的序列化
dumps/ loads
'''

# import base64
# import json
# import redis
#
# from example02 import Person #提示有错 但是导入成功了 随便吧。
#
# class PersonJsonEncoder(json.JSONEncoder):
#     def default(self, o):
#         return o.__dict__
#
# def mainly():
#     cli = redis.StrictRedis(host='120.77.222.217', port=6479, password='123123')
#     data = base64.b64decode(cli.get('guido'))
#     with open('guido2.jpg', 'wb') as file_stream:
#         file_stream.writable(data)
#
#     with open('guido.jpg', 'rb') as file_stream:
#         result = base64.b64encode(file_stream.read())
#     cli.set('guido', result)
#     persons = [
#         Person('李白', 49), Person('孙膑', 28), Person('包拯', 55), Person('郭靖', 35)
#     ]
#
#     persons = json.loads(cli.get('persons'))
#     print(persons)
#     cli.set('persons', json.dumps(persons, cls=PersonJsonEncoder))
#
# if __name__ == '__main__':
#     mainly()
#
# if __name__ == '__main__':
#     mainly()

'''
哈希摘要 数字签名指纹 单向哈希函数 没有反函数不可逆
应用领域 
数据库中的用户敏感信息保存成哈希摘要
给数据生成签名验证数据没有被恶意篡改
云存储服务的妙传功能 去重功能
'''

# class StreamHasher():
#     '''摘要生成器'''
#
#     def __init__(self, algorithm='md5', size=4096):
#         '''初始化方法
#         @:params:
#         algorithm 哈希摘要算法
#         size 每次读取数据的大小
#         '''
#
#
#         self.size = size
#         cls = getattr(__import__('hashlib'), algorithm.lower())
#         self.hasher = cls()
#
#     def digest(self, file_stream):
#         '''生成十六进制的摘要字符'''
#         # data = file_stream.read()
#         # while data:
#         #     self.hasher.update(data)
#         #     data = file_stream.read(self.size)
#
#         for data in iter(lambda: file_stream.read(self.size), b''):
#             self.hasher.update(data)
#
#         return self.hasher.hexdigest()
#
#     def __call__(self, file_stream):
#         return self.digest(file_stream)
#
# def mainly():
#     hasher1 = StreamHasher()
#     hasher2 = StreamHasher('sha1')
#     hasher3 = StreamHasher('sha256')
#     with open('E:\day0000\F100days\example02.py', 'rb') as file_stream:
#         print(hasher1.digest(file_stream))
#         file_stream.seek(0,0)
#         print(hasher2.digest(file_stream))
#         file_stream.seek(0,0)
#         print(hasher3(file_stream))
#
# if __name__ == '__main__':
#     mainly()

'''
加密和解密
对称加密 加密和解密是同一个密钥 DES AES
非对称加密 加密和解密是不同的密钥 RSA
pip install pycrypto 
pycrypto 安装老出错 用pycryptodome 一样用
'''

# import base64
# from hashlib import md5
# from Crypto.Cipher import AES
# from Crypto import Random
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP

'''
AES加密的密钥 长度32个字节
Key = md5(b'wao45ti0').hexdigest()
AES加密的初始向量 随机生成
iv = Random.new().read(AES.block_size)
'''
# def mainly():
    # 生成密钥对
    # key_pair = RSA.generate(1024)
    # 导入公钥
    # pub_key = RSA.importKey(key_pair.publickey().exportKey())
    # 导入私钥
    # pri_key = RSA.importKey(key_pair.exportKey())
    # message1 = b'Life is short, you need python.'
    # 加密数据
    # data = pub_key.encrypt(message1.encode(), None)
    # encryptor = PKCS1_OAEP.new(pub_key)
    # encrypted = encryptor.encrypt(message1)
    # 对加密数据进行BASE64编码
    # message2 = base64.b64encode(encrypted[0])
    # print(message2)
    # 对加密数据进行BASE64解码
    # data = base64.b64decode(message2)
    # 解密数据
    # decrypot = PKCS1_OAEP.new()
    # message3 = pri_key.decrypt(data)
    # print(message3.decode())
    # AES - 对称加密
    # str1 = 'haha ** 2'
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # 加密
    # str2 = cipher.encrypt(str1)
    # print(str2)
    # 解密
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # str3 = cipher.decrypt(str2)
    # print(str3.decode())

# if __name__ == '__main__':
#     mainly()

'''
装饰器 装饰器中放置的通常都是横切关注（cross-concern)功能
横切就是很多地方都会用到但跟正常业务又逻辑没有必然联系的功能
装饰器实际上是实现了设计模式中的代理模式 AOP-面向切面编程
'''

# from functools import wraps
# from random import randint
# from time import time, sleep
#
# import pymysql
#
# def record(output):
#
#     def decorate(func):
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time()
#             ret_value = func(*args, **kwargs)
#             output(func.__name__, time() - start)
#             return ret_value
#
#         return wrapper
#     return decorate
#
# def output_to_console(fname, duration):
#     print('%s:%.3f秒'%(fname, duration))
#
# def output_to_file(fname, duration):
#     with open('afile.txt', 'a') as file_stream:
#         file_stream.write('%s:%.3f秒\n'%(fname, duration))
#
# def output_to_do(fname, duration):
#     con = pymysql.connect(host='localhost', port=3306, database='test',charset='utf8',
#                           user='root',password='12345', autocommit=True)
#
#     try:
#         with con.cursor() as cursor:
#             cursor.execute('insert in to tb_record values (default, %s, %s)',
#                            (fname, '%.3f'%duration))
#
#     finally:
#         con.close()
#
# @record(output_to_console)
# def random_delay(min, max):
#     sleep(randint(min, max))
#
# def mainly():
#     for _ in range(3):
#         print(random_delay.__name__)
#         random_delay(3, 5)
#     for _ in range(3):
#         # 取消掉装饰器
#         random_delay.__wrapped__(3, 5)
#
# if __name__ == '__main__':
#     mainly()

'''
装饰类的装饰器 单例模式 一个类只能创建出唯一的对象
上下文语法：__enter__/__exit__
'''

# import threading
# from functools import wraps
#
# def singleton(cls):
#     # 单例装饰器
#     instances = {}
#     lock = threading.Lock()
#
#     @wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             with lock:
#                 if cls not in instances:
#                     instances[cls] = cls(*args, **kwargs)
#
#         return instances[cls]
#
#     return wrapper
#
# @singleton
# class President():
#
#     def __init__(self, name, country):
#         self.name = name
#         self.country = country
#
#     def __str__(self):
#         return f'{self.country}:{self.name}'
#
# def mainly():
#     print(President.__name__)
#     p1 = President('华盛顿', '美国')
#     p2 = President('尼克松', '美国')
#     print(p1 == p2)
#     print(p1)
#     print(p2)
#
# if __name__ == '__main__':
#     mainly()

'''
变量的作用域以及python搜索变量的顺序
LEGB Local--Embedded--Global--Built-in
global 声明或定义全局变量 要么直接使用现有的全局作用域变量 要么定义一个变量放到全局作用域
nonlocal -声明使用嵌套作用域的变量 如果嵌套作用域没有对应的变量直接报错
'''

# x = 100
#
# def foo():
#     global x
#     x = 200
#     def bar():
#         x = 300
#         print(x)
#
#     bar()
#     print(x)
#
# foo()
# print(x)

"""
面向对象的三大支柱 封装 继承 多态
面向对象的设计原则SOLID原则
面向对象的设计模式 GoF设计模式（单例 工厂 代理 策略 迭代器）
月薪结算系统 部门经理每月15000 程序员每小时200 销售员底薪1800加5%提成
"""

# from abc import ABCMeta, abstractmethod
#
# class Employee(metaclass=ABCMeta):
#     """员工抽象类"""
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def get_salary(self):
#         """结算月薪 抽象方法"""
#         pass
#
# class Manager(Employee):
#     def get_salary(self):
#         return 15000.0
#
# class Programmer(Employee):
#     def __init__(self, name, working_hour = 0):
#         self.working_hour = working_hour
#         super().__init__(name)
#
#     def get_salary(self):
#         return 200.0 * self.working_hour
#
# class Salesman(Employee):
#
#     def __init__(self, name, sales = 0.0):
#         self.sales = sales
#         super().__init__(name)
#
#     def get_salary(self):
#         return 1800.0 + self.sales * 0.05
#
# class EmployeeFactory():
#     """创建员工的工厂（工厂模式 通过工厂实现对象使用者和对象之间的解耦合）"""
#
#     @staticmethod
#     def create(emp_type, *args, **kwargs):
#         """创建员工"""
#         emp_type = emp_type.upper()
#         emp = None
#         if emp_type =='M':
#             emp = Manager(*args, **kwargs)
#         elif emp_type == 'P':
#             emp = Programmer(*args, **kwargs)
#         elif emp_type == 'S':
#             emp = Salesman(*args, **kwargs)
#         return emp
#
# def mainly():
#     emps = [
#         EmployeeFactory.create('M', '李世民'),
#         EmployeeFactory.create('P', '魏征', 140),
#         EmployeeFactory.create('P', '李白', 85),
#         EmployeeFactory.create('S', '包拯', 250000),
#     ]
#
#     for emp in emps:
#         print('%s:%.2f元'%(emp.name, emp.get_salary()))
#
# if __name__ == '__main__':
#     mainly()

'''
面向对象
枚举 一个变量的值只有有限个选择，最适合的类型就是枚举
通过枚举我们可以定义符号常量，符合常量优于字面常量
'''
#
# from enum import Enum, unique
# import random
#
# @unique
# class Suite(Enum):
#     '''花色 枚举'''
#     SPADE, HEART, CLUB, DIAMOND = range(4)
#
#     def __lt__(self, other):
#         return self.value < other.value
#
# class Card():
#     '''牌'''
#
#     def __init__(self, suite, face):
#         self.suite = suite
#         self.face = face
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __str__(self):
#         suites = ("S", "H", "C", "B")
#         faces = ('', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
#         return f'{suites[self.suite.value]}{faces[self.face]}'
#
# class Poker():
#     """poke"""
#
#     def __init__(self):
#         self.index = 0
#         self.cards = [Card(suite, face)
#                       for suite in Suite
#                       for face in range(1, 14)]
#
#     def shuffle(self):
#         '''洗牌'''
#         self.index = 0
#         random.shuffle(self.cards)
#
#     def deal(self):
#         """发牌"""
#         card = self.cards[self.index]
#         self.index += 1
#         return card
#
#     @property
#     def has_more(self):
#         """是否有更多的牌"""
#         return self.index < len(self.cards)
#
# class Player():
#     """玩家"""
#
#     def __init__(self, name):
#         self.name = name
#         self.cards = []
#
#     def get_card(self, card):
#         """摸牌"""
#         self.cards.append(card)
#
#     def arrange(self):
#         """整理"""
#         self.cards.sort(key=lambda card: (card.suite, card.face))
#
# def mainly():
#     poker = Poker()
#     poker.shuffle()
#     players = [
#         Player('汉武帝'), Player('李世民'),
#         Player('赵匡胤'), Player('玄烨')
#     ]
#
#     while poker.has_more:
#         for player in players:
#             player.get_card(poker.deal())
#         for player in players:
#             player.arrange()
#             print(player.name, end=':')
#             print(player.cards)
#
# if __name__ == '__main__':
#     mainly()

"""
迭代器 - __iter__ / __next__
itertools 生成可迭代序列的工具模块
"""

# import itertools
# from math import sqrt
#
# def is_prime(num):
#     '''判断素数'''
#     for factor in range(2, int(sqrt(num)) + 1):
#         if num % factor == 0:
#             return False
#     return True
#
# class PrimeIter(object):
#     """素数迭代器"""
#
#     def __init__(self, min_value, max_value):
#         assert 2 <= min_value <= max_value
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.min_value += 1
#         while self.min_value <= self.max_value:
#             if is_prime(self.min_value):
#                 return self.min_value
#             self.min_value += 1
#         raise StopIteration()
#
# class FibIter(object):
#
#     def __init__(self, num):
#         self.num = num
#         self.a, self.b = 0, 1
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx < self.num:
#             self.a, self.b = self.b, self.a + self.b
#             self.idx += 1
#             return self.a
#         raise StopIteration()
#
# def mainly():
#     prime_iter = PrimeIter(2, 10000)
#     for val in prime_iter:
#         print(val)
#
# if __name__ == '__main__':
#     mainly()

"""
魔术方法
如果要把自定义对象放到set或者用作dict的键
那么必须要重写__hash__ and __eq__两个魔术方法
前者用来计算对象的哈希码，后者又来判断两个对象是否相同
哈希码不同的对象一定是不同的对象，但哈希码相同未必是相同的对象 哈希码冲撞
所以在哈希码相同的时候还要通过__eq__来判定对象是否相同
"""

# class Student():
#     __slots__ = ('stuid', 'name', 'gender')
#
#     def __init__(self, stuid, name):
#         self.stuid = stuid
#         self.name = name
#
#     def __hash__(self):
#         return hash(self.stuid) + hash(self.name)
#
#     def __eq__(self, other):
#         return self.stuid == other.stuid and self.name == other.name
#
#     def __str__(self):
#         return f'{self.stuid}:{self.name}'
#
#     def __repr__(self):
#         return self.__str__()
#
# class School():
#
#     def __init__(self, name):
#         self.name = name
#         self.students = {}
#
#     def __setitem__(self, key, student):
#         self.students[key] = student
#
#     def __getitem__(self, key):
#         return self.students[key]
#
# def mainly():
#     stu = Student(1500, '关羽')
#     stu.gender = 'Male'
#     # stu.birth = '1990-11-22'
#     print(stu.name)
#     school = School('LaoBai_online')
#     school[1001] = Student(1002, '貂蝉')
#     school[1002] = Student(1001, '西施')
#     school[1004] = Student(1003, '如懿')
#     print(school[1004])
#     print(school[1001])
#
# if __name__ == '__main__':
#     mainly()

"""
多重继承 一个类有两个或者两个以上的父类
MRO 方法解析顺序 method resolution order
当出现菱形继承 钻石继承的时候 子类到底继承哪个父类的方法
python 2 深度优先搜索
python 3 c3算法 类似于广度优先搜索
"""

# class A():
#     def say_hello(self):
#         print('Hello, this is A')
#
# class B(A):
#     pass
#
# class C(A):
#
#     def say_hello(self):
#         print("Hello, C")
#
# class D(B, C):
#     pass
#
# class SetOnceMappingMixin():
#     """自定义混入类"""
#     __slots__ = ()
#
#     def __setitem__(self, key, value):
#         if key in self:
#             raise KeyError(str(key) + ' already set ')
#         return super().__setitem__(key, value)
#
# class SetOnceDict(SetOnceMappingMixin, dict):
#     """自定义字典"""
#     pass
#
# def mainly():
#     print(D.mro())
#     print(D.__mro__)
#     D().say_hello()
#     print(SetOnceDict.__mro__)
#     my_dict = SetOnceDict()
#     my_dict['username'] = '李白'
#     # my_dict['username'] = '长今'
#
# if __name__ == '__main__':
#     mainly()

"""
元 meta
元数据 描述数据的数据 metadata
元类 描述类的类 metaclass 继承自type
"""

# import threading
#
# class SingletonMeta(type):
#     """自定义元类"""
#
#     def __init__(cls, *args, **kwargs):
#         cls.__instance = None
#         cls.lock = threading.Lock()
#         super().__init__(*args, **kwargs)
#
#     def __call__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             with cls.lock:
#                 if cls.__instance is None:
#                     cls.__instance = super().__call__(*args, **kwargs)
#         return cls.__instance
#
# class President(metaclass=SingletonMeta):
#     """总统 单例类"""
#
#     def __init__(self, name, country):
#         self.name = name
#         self.country = country
#
#     def __str__(self):
#         return f'{self.country}:{self.name}'
#
# def mainly():
#     """主函数"""
#     p1 = President('李世民', 'Tang')
#     p2 = President('刘彻', 'Han')
#     p3 = President('玄烨', 'Qing')
#     p4 = President.__call__('赵匡胤', 'Song')
#     print(p1 == p2)
#     print(p1 == p3)
#     print(p1 == p4)
#     print(p1, p2, p3, p4, sep='\n')
#
# if __name__ == '__main__':
#     mainly()

"""
扩展性系统性能
垂直扩展 增加单节点处理能力
水平扩展 将单节点变成多节点（读写分离/分布式集群）
并发编程 加速程序执行 改善用户体验
耗时间的任务都尽可能独立执行 不要阻塞代码的其他部分
多线程
创建Thread对象指定target和args属性并通过start方法启动线程
继承Thread类并重写run方法来定义线程执行的任务
创建线程池对象ThreadPoolExecutor并通过submit来提交要执行的任务
第三种方式可以通过Future对象的result方法在将来获得线程的执行结果
也可以通过done方法判定线程是否执行结束
多进程 异步IO
"""

# import glob
# import os
# import time
#
# from concurrent.futures import ThreadPoolExecutor
# from threading import Thread
#
# from PIL import Image

# class ThumbnailThread(Thread):
#
#     def __init__(self, infile):
#         self.infile = infile
#         super().__init__()
#
#     def run(self):
#         file, ext = os.path.splitext(self.infile)
#         filename = file[file.rfind('/') + 1:]
#         for size in (32, 64, 128):
#             outfile = f'thumbnail/{filename}_{size}.png'
#             image = Image.open(self.infile)
#             image.thumbnail((size, size))
#             image.save(outfile, format='PNG')

# def gen_thumbnail(infile):
#     file, ext = os.path.splitext(infile)
#     filename = file[file.rfind('/') + 1:]
#     for size in (32, 64, 128):
#         outfile = f'thumbnails/{filename}_{size}_{size}.png'
#         image = Image.open(infile)
#         image.thumbnail((size, size))
#         image.save(outfile, format='PNG')

# def mainly():
#     start = time.time()
#     threads = []
#     for infile in glob.glob('images/*'):
#         # t = Thread(target=gen_thumbnail, args = (infile, )
#         t = ThumbnailThread(infile)
#         t.start()
#         threads.append()
#
#     for t in threads:
#         t.join()
#     end = time.time()
#     print(f'耗时：{end - start}秒')

# def mainly():
#     pool = ThreadPoolExecutor(max_workers=30)
#     futures = []
#     start = time.time()
#     for infile in glob.glob('images/*'):
#         '''
#         submit方法是一个阻塞式方法，如果线程还没有结束
#         即便工作线程已经用完，submit方法也会接受提交的任务
#         '''
#         future = pool.submit(gen_thumbnail, infile)
#         futures.append(future)
#     for future in futures:
#         '''
#         result方法是一个阻塞式的方法 如果线程还没有结束
#         暂时取不到线程的执行结果 代码就会在此处阻塞
#         '''
#         future.result()
#
#     end = time.time()
#     print(f'耗时：{end - start}秒')
#     '''
#     shutdown也是非阻塞式的方法 但是如果已经提交的任务还没有执行完
#     线程池是不会停止工作的 shutdown之后再提交任务就不会执行而且产生异常
#     '''
#     pool.shutdown()
#
# if __name__ == '__main__':
#     mainly()

'''
线程间通信 共享数据 非常简单因为可以共享同一个进程的内存
进程间通信 共享数据 比较麻烦因为操作系统会保护分配给进程的内存
要实现多进程的通信通常可以用系统管理 套接字 三方服务来实现
multiprocessing.Queue
守护线程 daemon thread
守护进程 firewalld / httpd / mysqld
在系统停机的时候不保留的进程 不会因为进程还没有执行结束而阻碍系统停止
'''

# from threading import Thread
# from time import sleep
#
# def output(content):
#     while True:
#         print(content, end='')
#
# def mainly():
#     Thread(target=output, args=('Ping', ), daemon=True).start()
#     Thread(target=output, args=('Pong', ), daemon=True).start()
#     sleep(5)
#
# if __name__ == '__main__':
#     mainly()

'''
多个线程竞争一个资源 保护临界资源 锁 lock/rlock
多个线程竞争多个资源 线程数 资源数 信号量 semaphore 
多个线程的调度 暂停线程执行 唤醒等待中的线程 condition
'''

# from concurrent.futures import ThreadPoolExecutor
# from random import randint
# from time import sleep
#
# import threading
#
# class Account():
#     """银行账户"""
#
#     def __init__(self, balance = 0):
#         self.balance = balance
#         lock = threading.Lock()
#         self.condition = threading.Condition(lock)
#
#     def withdraw(self, money):
#         """取钱"""
#         with self.condition:
#             while money > self.balance:
#                 self.condition.wait()
#             new_balance = self.balance - money
#             sleep(0.001)
#             self.balance = new_balance
#
#     def deposit(self, money):
#         """存钱"""
#         with self.condition:
#             new_balance = self.balance + money
#             sleep(0.001)
#             self.balance = new_balance
#             self.condition.notify_all()
#
# def add_money(account):
#     while True:
#         money = randint(5, 10)
#         account.deposit(money)
#         print(threading.current_thread().name, ':', money, '<===', account.balance)
#         sleep(0.5)
#
# def sub_money(account):
#     while True:
#         money = randint(10, 30)
#         account.withdraw(money)
#         print(threading.current_thread().name, ':', money, '<===', account.balance)
#         sleep(1)
#
#
# def mainly():
#     account = Account()
#     with ThreadPoolExecutor(max_workers=10) as pool:
#         for _ in range(5):
#             pool.submit(add_money, account)
#             pool.submit(sub_money, account)
#
# if __name__ == '__main__':
#     mainly()

"""
多进程和进程池的使用
多线程因为GIL的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑使用多进程
"""

# import concurrent.futures
# import math
#
# PRIMES = [
#     1116281,
#     1297337,
#     104395303,
#     472882027,
#     533000389,
#     817504243,
#     982451653,
#     112272535095293,
#     112582705942171,
#     112272535095293,
#     115280095190773,
#     1157978480077099,
#     1099726899285419
# ] * 5
#
# def is_prime(n):
#     """判断素数"""
#     if n % 2 == 0:
#         return False
#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# def mainly():
#     """主函数"""
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print('%d is prime: %s'%(number, prime))
#
# if __name__ == '__main__':
#     mainly()

"""
协程（coroutine） 可以在需要时进行切换的相互协作的子程序
"""

# import asyncio
# from example15 import is_prime
# is_prime is just here

# def num_generator(m, n):
#     """ 指定范围的数字生成器"""
#     yield from range(m, n + 1)
#
# async def prime_filter(m, n):
#     """素数过滤器"""
#     primes = []
#     for i in num_generator(m, n):
#         if is_prime(i):
#             print('Prime =>', i)
#             primes.append(i)
#
#         await asyncio.sleep(0.005)
#     return tuple(primes)
#
# async def square_mapper(m, n):
#     """平方映射器"""
#     squares = []
#     for i in num_generator(m, n):
#         print('Square =>', i * i)
#         squares.append(i * i)
#
#         await asyncio.sleep(0.005)
#     return squares
#
# def mainly():
#     """主函数"""
#     loop = asyncio.get_event_loop()
#     future = asyncio.gather(prime_filter(2, 2000), square_mapper(1, 2000))
#     future.add_done_callback(lambda x: print(x.result()))
#     loop.run_until_complete(future)
#     loop.close()
#
# if __name__ == '__main__':
#     mainly()

"""
aiohttp 异步HTTP网络访问
异步I/O 异步编程 只使用一个线程 单线程来处理用户请求
用户请求一旦被接纳 剩下的都是I/O操作，通过多路I/O复用也可以达到并发的效果
这种做法与多线程相比可以让CPU利用率更高，因为没有线程切换的开销
redis/node.js 单线程 + 异步I/O
celery 将要执行的耗时间的任务异步化处理
异步I/O事件循环 uvloop
"""

# import asyncio
# import re
# import aiohttp
#
# async def fetch(session, url):
#     async with session.get(url, ssl=False) as resp:
#         return await resp.text()
#
# async def mainly():
#     pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
#     urls = ('https://www.python.org/',
#             'https://www.bing.com/',
#             # 'https://www.google.com/',
#             'https://www.qq.com/',
#             'https://www.z.com/',
#             "https://www.youtube.com/"
#             )
#     async with aiohttp.ClientSession() as session:
#         for url in urls:
#             html = await fetch(session, url)
#             print(pattern.search(html).group('title'))
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(mainly())
#     loop.close()

"""
单元测试 针对程序最小的功能模块 函数和方法的测试
测试方法
白盒测试 程序自己写的测试
黑盒测试 测试人员或QA 不知道代码实现细节 只关注功能
编写PYTHON单元测试 定义类继承testcase 写测试方法(test_ 开头)
执行单元测试
unittest.main()
python3 -m unittest test.py
第三方库 nose2 / pytest
pip install pytest pytest-cov
pytest -v --cov

pip install nose cov-core
noses -v --cov
"""
# from unittest import TestCase
#
# def seq_search(items: list, elem) -> int:
#     '''顺序查找'''
#     for index, item in enumerate(items):
#         if elem == item:
#             return index
#     return -1
# def bin_search(items, elem):
#     """二分查找"""
#     start, end = 0, len(items) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if elem > items[mid]:
#             start = mid + 1
#         elif elem < items[mid]:
#             end = mid - 1
#         else:
#             return mid
#     return -1
#
# class TestExample01(TestCase):
#     """测试查找函数的测试用例"""
#     '''执行每个测试函数之前要执行的方法'''
#     def setUp(self):
#         self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
#         self.data2 = [12, 35, 40, 55, 68, 73, 81, 97]
#     '''执行每个测试函数之后要执行的方法'''
#     def tearDown(self):
#         pass
#
#     def test_seq_search(self):
#         '''测试顺序查找'''
#         self.assertEqual(0, seq_search(self.data1, 35))
#         self.assertEqual(2, seq_search(self.data1, 12))
#         self.assertEqual(6, seq_search(self.data1, 81))
#         self.assertEqual(7, seq_search(self.data1, 40))
#         self.assertEqual(-1, seq_search(self.data1, 99))
#         self.assertEqual(-1, seq_search(self.data1, 7))
#
#     def test_bin_search(self):
#         """测试二分查找"""
#         self.assertEqual(1, bin_search(self.data2, 35))
#         self.assertEqual(0, bin_search(self.data2, 12))
#         self.assertEqual(6, bin_search(self.data2, 81))
#         self.assertEqual(2, bin_search(self.data2, 40))
#         self.assertEqual(7, bin_search(self.data2, 97))
#         self.assertEqual(-1, bin_search(self.data2, 7))
#         self.assertEqual(-1, bin_search(self.data2, 99))

# from unittest import TestCase
#
# def select_sort(origin_items, comp=lambda x, y: x < y):
#     """简单选择排序"""
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         min_index = 1
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#
#     return items
#
# def merge(items1, items2, comp=lambda x, y: x <= y):
#     """合并 将两个有序列表合并成一个新的有序列表"""
#     items = []
#     index1, index2 = 0, 0
#     while index1 < len(items1) and index2 < len(items2):
#         if comp(items1[index1], items2[index2]):
#             items.append(items1[index1])
#             index1 += 1
#         else:
#             items.append(items2[index2])
#             index2 += 1
#     items += items1[index1:]
#     items += items2[index2:]
#     return items
#
# class TestExample02(TestCase):
#     '''测试顺序函数的测试用例'''
#
#     def setUp(self):
#         self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
#         self.items1 = [12, 35, 68, 97]
#         self.items2 = [40, 55, 73, 81]
#
#     def test_merge(self):
#         items = merge(self.items1, self.items2)
#         for i in range(len(items) - 1):
#             self.assertLessEqual(items[i], items[i + 1])
#
#     def test_select_sort(self):
#         '''测试顺序查找'''
#         items = select_sort(self.data1)
#         for i in range(len(items) - 1):
#             self.assertLessEqual(items[i], items[i + 1])
#