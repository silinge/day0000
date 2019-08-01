#阶乘
# def factorial(n):
#     result = 1
#     for num in range(1, n+1):
#         result *= num
#     return result
#
# print(factorial(7)//factorial(3)//factorial(4))

# 求最大公约数和最小公倍数

# def gcd(x, y):
#     if x>y:
#         (x, y) = (y, x)
#     for factor in range(x, 1, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#     return 1
#
# def lcm(x, y):
#     return x * y // gcd(x, y)
#
# print(gcd(12, 30))
# print(lcm(12, 30))

'''
python 内置函数
数学相关： abs /divmod/ pow/ round/min/ max/ sum
序列：len/range/ next/ filter/ map/sorted/ slice/ reversed
类型转换：chr/ord/str/bool/int/float/complex/bin/oct/hex
数据结构： dict/list/ set/ tuple
其他函数： all/ any/ id/ input/ open/ print/ type
'''

# def myfilter(mystr):
#     return len(mystr) == 5
#
# print(chr(0x79e7))
# print(hex(ord("秦")))
# print(abs(-250.12))
# print(round(-233.14))
# print(pow(2, 8, 9)) # x**y%z
# print(pow(2, 5))
# fruits = ["apple", "banana", 'pear', 'peach', "grape"]
# print(fruits[slice(2, 4)])
# fruits2 = list(filter(myfilter, fruits))
# print(fruits)
# print(fruits2)

'''
python 常用模块
运行时服务相关模块 copy/ pickle / sys/ 
数学相关模块： decimal/ math/ random/
字符串处理模块 codecs /re/
文件处理相关模块 shutil/ gzip/
操作系统服务模块 datetime/ os/ time/ logging/ io/
进程和线程 multiprocessing/ threading/ queue
网络模块 ftplib/ http/ smtplib/ urllib
web编程相关模块 cgi / webbrowser
数据处理模块 base64 / csv/ html.parser/ json/ xml/
'''
#
# import time
# import shutil
# import os
#
# seconds = time.time()
# print(seconds)
# localtime = time.localtime(seconds)
# print(localtime)
# print(localtime.tm_year)
# print(localtime.tm_mon)
# print(localtime.tm_mday)
# asctime = time.asctime(localtime)
# print(asctime)
# strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
# print(strtime)
# mydate = time.strptime('2019-07-03', '%Y-%m-%d')
# print(mydate)
#
# shutil.copy('C:/Users/name/py101.py', 'C:/Users/name/Desktop/first.py')
# os.system('ls -1')
# os.chdir('/Users/Name')
# os.system('ls -1')
# os.mkdir('test')

# '''
# 函数的参数
# 默认参数 可变参数 关键字参数 命名关键字参数
# '''
#
# def f1(a, b=5, c=10):
#     return a + b*2 + c*3
# print(f1(1, 2, 3))
# print(f1(100, 200))
# print(f1(100))
# print(f1(c=2, b=3, a=1))
#
# def f2(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
#
# print(f2(1, 2, 3))
# print(f2(1,2,3,4,6))
# print(f2())
#
# def f3(**kw):
#     if 'name' in kw:
#         print(f"欢迎您{'name'}")
#         print("欢迎您%s！"%kw['name'])
#     elif 'tel' in kw:
#         print("联系电话是%s"%kw['tel'])
#     else:
#         print('nothing here')
# param = {'name':'Z.XV', 'age':'19'}
# f3(**param)
# f3(name='zxv', age=29, tel = '01012314572')
# f3(last_name='zxv', age=29, tel = '01012314572')
# f3(name='zxv', age=29, Phone = '01012314572')
# f3(name='zxv', age=29,  mobile= '01012314572')

# 局部作用域
# def foo1():
#     a = 5
#
# foo1()
# # print(a)
#
# # 全局作用域
# b = 10
#
# def foo2():
#     print(b)
#
# foo2()
#
# def foo3():
#     b = 100
#     print(b)
#
# foo3()
# print(b)
#
# def foo4():
#     global b #全局变量
#     b = 150
#     print(b)
#
# foo4()
# print(b)

# from math import factorial as fac
# m = int(input("输入一个整数"))
# n = int(input("输入一个整数"))
# # a, b = int(input("依次输入2个整数"))
# if m < n :
#     m, n = n, m
# print(fac(m)//fac(n)//fac(m-n))
# a, b = int(input("依次输入2个整数"))
# a, b = input("依次输入2个整数")
