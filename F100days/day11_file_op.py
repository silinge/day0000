# def mainly():
#     f = open('sample_file\day11_op.txt', 'r', encoding='utf-8')
#     print(f.read())
#     f.close()
#
# if __name__ == '__main__':
#     mainly()

# def mainly():
#     f = None
#     try:
#         f = open('sample_file\day11_op.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件,')
#     except LookupError:
#         print('指定了未知的编码.')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误')
#     finally:
#         if f:
#             f.close()
# if __name__ == '__main__':
#     mainly()

# def mainly():
#     try:
#         with open("sample_file/day11_op.txt", 'r', encoding='utf-8') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件')
#     except LookupError:
#         print('指定了未知的的编码')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误.')
#
# if __name__ == '__main__':
#     mainly()

# import time
#
# def mainly():
#     # 一次性读取整个文件的内容
#     with open('sample_file/day11_op.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#
#     # 通过for - in 循环逐行读取
#     with open('sample_file/day11_op.txt', mode='r', encoding='utf-8') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#     print()
#
#     # 读取文件按行读取到列表中
#     with open('sample_file/day11_op.txt', encoding='utf-8') as f:
#         lines = f.readlines()
#     print(lines)
#
# if __name__ == '__main__':
#     mainly()


'''寻找素数,分别存入a b c 三个文件之中,分为三段, 1-99 - a, 100-999-b, 1000-9999- c'''
# from math import sqrt
#
# def is_prime(n):
#     '''判断素数的函数'''
#     assert n > 0
#     for factor in range(2, int(sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False
#
# def mainly():
#     filenames = ('sample_file/a.txt', 'sample_file/b.txt', 'sample_file/c.txt')
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename, 'w', encoding='utf-8'))
#         for number in range(1, 10000):
#             if is_prime(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('写入文件时发生错误')
#     finally:
#         for fs in fs_list:
#             fs.close()
#         print('Complete.')
#
# if __name__ == '__main__':
#     mainly()

# def mainly():
#     try:
#         with open('pic1.jpg', 'rb') as fs1:
#             data = fs1.read()
#             print(type(data)) # < class 'bytes' >
#
#         with open('pic2.jpg', 'wb') as fs2:
#             fs2.write(data)
#
#     except FileNotFoundError as e:
#         print('指定文件无法打开')
#     except IOError as e:
#         print('读写文件出现错误.')
#     print('程序执行结束')
#
# if __name__ == '__main__':
#     mainly()
#
# import json
#
# def mainly():
#     mydict = {
#         'name':'福尔摩斯',
#         'age': 41,
#         'whatsapp': 'canuhearme',
#         'cars':[
#             {'brand':'BENZ', 'max_speed':300},
#             {'brand':'VolkSwagon', 'max_speed':30},
#             {'brand':'BMW', 'max_speed':200}
#         ]
#     }
#     try:
#         with open('sample_file/day11_data.json', 'w', encoding='utf-8') as fs:
#             json.dump(mydict, fs)
#             '''json的四个重要参数, dump 将python对象按照json的格式序列化到文件中.
#             dumps 将python对象处理成json格式反序列化成对象
#             load 将文件中的JSON数据反序列化成对象
#             loads 将字符串的内容反序列化成python对象
#             '''
#     except IOError as e:
#         print(e)
#     print('已保存.')
#
# if __name__ == '__main__':
#     mainly()

# import  requests
# # import json
# #
# # def mainly():
# #     resp = requests.get('https://www.bing.com')
# #     data_model = json.loads(resp.text)
# #     for news in data_model['newslist']:
# #         print(news['title'])
# #
# # if __name__ == '__main__':
# #     mainly()

# import csv
#
# filename = 'sample_file/example_day11.csv'
#
# try:
#     with open(filename) as f:
#         reader = csv.reader(f)
#         data = list(reader)
# except FileNotFoundError:
#     print('无法打开文件', filename)
# else:
#     for item in data:
#         print("%-30s%-20s%-10s"%(item[0], item[1], item[2]))

# 写入csv
# import csv
#
# class Teacher(object):
#
#     def __init__(self, name, age, title):
#         self._name = name
#         self._age = age
#         self._title = title
#         self._index = 1
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @property
#     def title(self):
#         return self._title
#
# filename = "sample_file/example_day11.csv"
# teachers = [Teacher('武则天', 1200, '探花'), Teacher('华盛顿', 300, '将军')]
#
# try:
#     with open(filename, 'w') as f:
#         writer = csv.writer(f)
#         for teacher in teachers:
#             writer.writerow([teacher.name, teacher.age, teacher.title])
# except BaseException as e:
#     print('无法写入文件:', filename)
#
# else:
#     print("保存数据完成.")
# input_again = True
# 异常处理可以避免程序崩溃
# while input_again:
#     try:
#
#         a = int(input('a= '))
#         b = int(input('b= '))
#         print(f'{a}/{b}={a/b}')
#         input_again = False
#     except ValueError:
#         print('请输入整数')
#     except ZeroDivisionError:
#         print('除数不能为0')

# input_again = True
#
# while input_again:
#     try:
#         a = int(input('a= '))
#         b = int(input('b= '))
#         print("%d / %d = %.4f"%(a, b, a/b))
#         input_again = False
#     except (ValueError, ZeroDivisionError) as msges:
#         print(msges)

# import time
# import sys
#
# filename = input('输入文件名称')
# '''sample_file/day11_op.txt'''
# try:
#     with open(filename, encoding='utf-8') as f:
#         lines = f.readlines()
# except FileNotFoundError as msg:
#     print('无法打开文件', filename)
#     print(msg)
# except UnicodeDecodeError:
#     print('非文本文件无法解码')
#     sys.exit()
# else:
#     for line in lines:
#         print(line.rstrip())
#         time.sleep(0.5)
# finally:
#     print('无论发生什么,最后出现的都是我.表示这真的是最后了.')

# def f1():
#     raise AssertionError('发生异常')
#
# def f2():
#     f1()
# def f3():
#     f2()
#
# f3()

# import time
#
# def mainly():
#     with open('sample_file/day11_op.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#
#     # 通过for in 循环逐行读取
#     with open('sample_file/day11_op.txt', mode='r', encoding='utf-8') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#     print()
#
#     # 读取文件按行读取到列表中
#     with open('sample_file/day11_op.txt', encoding='utf-8') as f:
#         lines = f.readlines()
#     print(lines)
#
# if __name__ == '__main__':
#     mainly()

# birth = input('请输入你的生日(1900000):')
# with open('sample_file/pi_million_digits.txt') as f:
#     lines = f.readlines()
#     pi_string = ' '
#     for line in lines:
#         pi_string += line.strip()
#     if birth in pi_string:
#         print(f'Found you, {birth}.')

# from math import sqrt
#
# def is_prime(n):
#     for factor in range(2, int(sqrt(n))+1):
#         if n % factor == 0:
#             return False
#     return True
# # with open('sample_file/prime.txt', 'a') as f:
# with open('sample_file/prime.txt', 'w') as f:
#     for num in range(2, 154):
#         if is_prime(num):
#             f.write(str(num) + '\n')
#
# print('done!')

# import base64
# with open('123.jpg', 'rb') as f:
#     data = f.read()
#     print(type(data))
#     print(data)
#     print('字节数', len(data))
#     # 将图片处理成base-64编码
#     print(base64.b64encode(data))
#
# with open('1234.jpg', 'wb') as f:
#     f.write(data)
# print('Done')

# import json
# import csv
#
# json_str = '{"name":"李白", "age":1300, "title":"诗仙"}'
# result = json.loads(json_str)
# print(result)
# print((type(result)))
# print(result['name'])
# print(result['age'])
#
# # 把转换得到的字典作为关键字参数传入Teacher的构造器
# teacher = csv.Teacher(**result)
# print(teacher)
# print(teacher.name)
# print(teacher.age)
# print(teacher.title)
#
# # 请思考如何将下面JSON格式的天气数据转换成对象并获取我们需要的信息
# # 稍后我们会讲解如何通过网络API获取我们需要的JSON格式的数据
#
# '''
#     {
#         "wendu":"29",
#         "ganmao":"各项气象条件适宜, 发生感冒机率较低.但请避免长期处于空调房中,以防感冒.",
#         "forecast":[
#                     {
#                         "fengxiang":"南风",
#                         "fengli":"3-4级",
#                         "high":"高温 32℃",
#                         "type":"多云",
#                         "low":"低温 17℃",
#                         "date":"16日星期二"
#                     },
#                     "aqi":"71",
#                     "city":"北京"
#     }
# '''

# import json
#
# teacher_dict = {'name':'八戒', 'age':25, 'title':'walker'}
# json_str = json.dumps(teacher_dict)
# print(json_str)
# print(type(json_str))
# fruits_list=['apple', 'orange', 'strawberry', 'banana', 'pitaya']
# json_str = json.dumps(fruits_list)
# print(json_str)
# print(type(json_str))
