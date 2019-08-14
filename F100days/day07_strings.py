# def main():
#     str1 = "Hello, python3.7"
#     print(len(str1))
#     print(str1.capitalize())
#     print(str1.upper())
#     print(str1.find('yt'))
#     print(str1.find("py"))
#     print(str1.index("el"))
#     print(str1.index("on"))
#     print(str1.startswith("Hel"))
#     print(str1.startswith("llo"))
#     print(str1.endswith('.'))
#     print(str1.endswith('7'))
#     print(str1.center(40, 'b'))
#     print(str1.rjust(40, '-'))
#     str2 = "Abcedff987654"
#     print(str2[2])
#     print(str2[3:6])
#     print(str2[5:])
#     print(str2[4::2])
#     print(str2[::3])
#     print(str2[::-2])
#     print(str2[-4:-2])
#     print(str2.isdigit())
#     print(str2.isalnum())
#     print(str2.isalpha())
#     str3 = "   whatsupbeijing@amail.com    "
#     print(str3)
#     print(str3.strip())
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     list1 = [1, 23, 4, 100, 1234]
#     print(list1)
#     list2 = ['hello'] * 5
#     print(list2)
#     print(len(list1))
#     print(list1[0])
#     print(list1[4])
#     print(list1[2])
#     print(list1[-1])
#     print(list1[-4])
#     list1[3] = 230
#     list1.append(300)
#     list1.insert(1, 250)
#     list1 += [1000, 2000]
#     print(list1)
#     print(len(list1))
#     list1.remove(4)
#     if 1234 in list1:
#         list1.remove(1234)
#
#     del list1[0]
#     print(list1)
#     list1.clear()
#     print(list1)
#
# if __name__ == '__main__':
#     main()

# def main():
#     fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'watermelon', 'banana', 'peach', 'pine']
#     fruits += ['pitaya', 'pear', 'mango']
#     for fruit in fruits:
#         print(fruit.title(), end=' ')
#
#     print()
#
#     fruits2 = fruits[2:5]
#     print(fruits2)
#
#     fruits3 = fruits[:]
#     print(fruits3)
#
#     fruits4 = fruits[-6:-2]
#     print(fruits4)
#
#     fruits5 = fruits[::-1]
#     print(fruits)
#
# if __name__ == '__main__':
#     main()

# import sys
#
# def formi():
#     f = [x for x in range(1, 10)]
#     print(f)
#
#     f = [x + y for x in 'ABCDEF' for y in '1234567']
#     print(f)
#     f = [x**2 for x in range(1, 100)]
#     print(sys.getsizeof(f))
#     print(f)
#
#     f = (x **2 for x in range(1, 100))
#     print(sys.getsizeof(f))
#     print(f)
#     for val in f:
#         print(val)
#
# if __name__ == '__main__':
#     formi()

# def dlist():
#     list1 = ['orange', 'apple', 'zoo', 'vocabulary', 'dianhua']
#     list2 = sorted(list1)
#     list3 = sorted(list2, reverse = True)
#     list4 = sorted(list3, key=len)
#     print(list1)
#     print(list2)
#     print(list3)
#     print(list4)
#     list1.sort(reverse=True)
#     print(list1)
#
# if __name__ == '__main__':
#     dlist()

# def tup():
#     t = ('Williams', 33, True, 'CN, BEIJING')
#     print(t)
#     print(t[1])
#     print(t[2])
#     for member in t:
#         print(member)
#
#     t = ['Harry', 54, True, 'UK, London']
#     print(t)
#     person = list(t)
#     person[1] = 22
#     person[0]= 'Tom'
#     print(person)
#
#     fruits_list = ["Banana", 'Peach', 'Pear']
#     fruits_tuple = tuple(fruits_list)
#     print(fruits_tuple)
#
#
# if __name__ == '__main__':
#     tup()

# def sets():
#     set1 = {1, 2, 3, 4, 4, 4, 3, 1, 0}
#     print(set1)
#     print('Length = ', len(set1))
#     set2 = set(range(2, 8))
#     print(set2)
#     set1.add(6)
#     set1.add(9)
#     set2.update([13, 21])
#     print(set1)
#     print(set2)
#     set2.discard(4)
#
#     if 4 in set2:
#         set2.remove(5)
#     print(set2)
#
#     for elem in set2:
#         print(elem ** 2, end=' ')
#     print()
#     set3 =set((1, 2, 3, 3, 2, 1))
#     print(set3.pop())
#     print(set3)
#     print(set1 & set2) #print(set1.intersection(set2))
#     print(set1 | set2)
#     # print(set1.union(set2))
#     print(set1 - set2)
#     # print(set1.difference(set2))
#     print(set1 ^ set2)
#     # print(set1.symmetric_difference(set2))
#     print(set2<= set1)
#     # print(set2.issubset(set1))
#     print(set3<= set1)
#     print(set1 >= set2)
#     # print(set1.issuperset(set2))
#     print(set1 >= set3)
#
# if __name__ == '__main__':
#     sets()

# def dictiona():
#     scores = {'梅西' : 99, '贝克': 90, '姚明': 91}
#     print(scores['姚明'])
#     print(scores['贝克'])
#     for elem in scores:
#         print(f'{elem}\t--->\t{scores[elem]}')
#     scores['贝克'] = 66
#     scores['舒马赫'] = 87
#     scores.update(特朗普= 63, 普京=65)
#     print(scores)
#     if '鲁尼' in scores:
#         print(scores['鲁尼'])
#     print(scores.get('鲁尼'))
#     print(scores.get('鲁尼', 68))
#     print(scores.popitem())
#     print(scores.popitem())
#     print(scores.pop('梅西', 100))
#     scores.clear()
#     print(scores)
#
# if __name__ == '__main__':
#     dictiona()

# led scroll

# import os
# import time
#
# def scroll():
#     content= "我等的人她在多远的未来。"
#     for i in range(1, 21):
#         os.system('cls') #os.system('clear')
#         print(content)
#         time.sleep(0.5)
#         content = content[1:] + content[0]
#         i += 1
#
# if __name__ == '__main__':
#     scroll()

#cription
# import random
# def cription(code_len = 5):
#     all_chars = '0123456789@#$%^&*()'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     print(code)
#
# # if __name__ == '__main__':
# #     cription()
# cription(6)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
# def main():
#     for val in fib(25):
#         print(val)
#
# if __name__ == '__main__':
#     main()

# 设计一个函数返回给定文件名的后缀
# def get_suffix(filename, has_dot = False):
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#
#     else:
#         return ''

# 设计一个函数返回传入的列表中做大值和第二大值
# def max_two(x):
#     m1, m2 = (x[0], x[1]) if x[0]> x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2 # 注意这个return的缩进
#
# n = range(5, 199)
# print(max_two(n))
# print(n[0])
# print(max(n))

#计算指定年月日是第几天
# def is_leap_year(year):
#     return year % 4 ==0 and year % 100 != 0 or year % 400 == 0
#
# def which_day(year, month, date):
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)] # 以闰年true false 来选择使用哪一项天数集
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date #, is_leap_year(year), days_of_month
#
# def main():
#     print(which_day(2008, 12, 8))
#     print(which_day(2018, 2, 8))
#     print(which_day(2020, 4, 8))
# if __name__ == '__main__':
#     main()

# def yanghui():
#     num = int(input("Enter a number for rows: "))
#     yh = [[]]*num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#
#         print()
#
# if __name__ == '__main__':
#     yanghui()

# from random import randrange, randint, sample
#
# def display(balls):
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end=' ')
#         print('%02d'%ball, end=' ')
#     print()
#
# def random_select():
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     for _ in range(6):
#         index = randrange(len(red_balls))
#         selected_balls.append(red_balls[index])
#         del red_balls[index]
#         #如果是sample函数是这样的
#         # selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls
#
# def numb():
#     n = int(input('选择几注： '))
#     for _ in range(n):
#         display(random_select())
#
# if __name__ == '__main__':
#     numb()

#约瑟夫环的问题 15个和尚和15个道士遇到海难，只能活其中15个，30人围成圈数数，
# 从1开始数到9，9这个人下海，第10个人接着数1，一直重复，结果15个道士留下来了，他们是怎么选位置的。

# def dao():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
#         index %= 30
#     for person in persons:
#         print("Dao" if person else 'Monk', end='>>')
#
# if __name__ == '__main__':
#     dao()

#井字棋
# import os
#
# def print_board(board):
#     print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
#     print('-+-+-')
#     print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
#     print('-+-+-')
#     print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])
#
# def nine_cheeses():
#     init_board = {
#         'TL': ' ', 'TM': ' ', 'TR': ' ',
#         'ML': ' ', 'MM': ' ', 'MR': ' ',
#         'BL': ' ', 'BM': ' ', 'BR': ' ',
#     }
#     begin = True
#     while begin:
#         curr_board = init_board.copy()
#         begin = False
#         turn = 'x'
#         counter = 0
#         os.system('clear')
#         print_board(curr_board)
#         while counter < 9:
#             move = input(f"It is {turn}\'s turn to move, enter your position: ")
#             if curr_board[move] == ' ':
#                 counter += 1
#                 curr_board[move] = turn
#                 if turn == 'x':
#                     turn = 'o'
#                 else:
#                     turn = 'x'
#             os.system('clear')
#             print_board(curr_board)
#         choice = input("Once more?(yes|no)")
#         begin = choice == 'yes'
#
# if __name__ == '__main__':
#     nine_cheeses()

# avgscore
# def avgs():
#     number = int(input('Num of students: '))
#     names = [None]*number
#     scores = [None]*number
#     for index in range(len(names)):
#         names[index] = input(f'请输入第{index + 1}个学生的名字： ')
#         scores[index] = float(input(f'请输入第{index + 1}个学生的成绩： '))
#     total = 0
#     for index in range(len(names)):
#         print('%s:%.1f分'%(names[index], scores[index]))
#         total += scores[index]
#     print('平均成绩是：%.1f分'%(total/number))
#
# if __name__ == '__main__':
#     avgs()

#字典的处理
#
# def dicti():
#     scores = {'Robbin' : 98, 'Barney' : 59, 'Ted' : '89'}
#     print(scores['Robbin'])
#     print(scores['Ted'])
#     for elem in scores:
#         print(f'{elem}\t--->\t{scores[elem]}')
#     scores['Marshall'] = 78
#     scores['Barney'] = 60
#     scores.update(Tomas = 55, Tracy = 97)
#     print(scores)
#     if 'Lily' in scores:
#         print(scores["Lily"])
#     print(scores.get('Lily'))
#     print(scores.get('Lily', 68))
#     print(scores.popitem())
#     print(scores.popitem())
#     print(scores.pop('Robbin', 10))
#     scores.clear()
#     print(scores)
#
# if __name__ == '__main__':
#     dicti()

# def dictii():
#     stu = {'name':'Robbin', 'age':28, 'gender':True}
#     print(stu)
#     print(stu.keys())
#     print(stu.values())
#     print(stu.items())
#     for elem in stu.items():
#         print(elem)
#         print(elem[1], elem[0])
#     if 'age' in stu:
#         stu['age'] = 20
#     print(stu)
#     stu.setdefault('score', 68)
#     print(stu)
#     stu.setdefault('score', 77)
#     print(stu)
#     stu['score'] = 100
#     print(stu)
#
# if __name__ == '__main__':
#     dictii()

# 斐波那契
# def fibi():
#     f = [1, 1]
#     for i in range(2, 10):
#         f += [f[i -1] + f[i -2]]
#         #f.append(f[i-1] + f[i-2])
#     for val in f:
#         print(val, end=' ')
#
# if __name__ == '__main__':
#     fibi()

#find max
# def find_max():
#     fruits = ['grape', 'banana', 'apple', 'orange', 'pitaya', 'pear']
#     # print(max(fruits))
#     # print(min(fruits))
#     # max_v = min_v = fruits[0]
#     # for index in range(1, len(fruits)):
#     #     if fruits[index] > max_v:
#     #         max_v = fruits[index]
#     #     elif fruits[index] < min_v:
#     #         min_v = fruits[index]
#     # print(f'Max is {max_v}')
#     # print(f'Min is {min_v}')
#     max_1, max_2 = (fruits[0], fruits[1]) if fruits[0] > fruits[1] else (fruits[1], fruits[0])
#     for index in range(2, len(fruits)):
#         if fruits[index] > max_1:
#             max_2 = max_1
#             max_1 = fruits[index]
#         elif fruits[index] > max_2:
#             max_2 = fruits[index]
#         # return max_1, max_2
#     print(max_1, max_2)
# if __name__ == '__main__':
#     find_max()

# def list_c():
#     fruits = ['pineapple', '@pple', 'watermelon', 'waxberry']
#     print(fruits)
#     print(fruits[0])
#     print(fruits[2])
#     print(fruits[-1])
#     print(fruits[-3])
#     fruits[1] = 'orange'
#     print(fruits)
#     fruits.append('pitaya')
#     fruits.insert(2, 'banana')
#     print(fruits)
#     del fruits[4]
#     fruits.pop()
#     fruits.pop(1)
#     fruits.remove('banana')
#     print(fruits)
#
# if __name__ == '__main__':
#     list_c()

# def list_d():
# #     fruits = ['lemon', 'almond', 'betelnut', 'yale', 'avovado']
# #     fruits += ['plum', 'pomelo', 'sorgo', 'persimmon']
# #     for fruit in fruits:
# #         print(fruit.title(), end=' ')
# #     print()
# #
# #     fruits2=fruits[1:5]
# #     print(fruits2)
# #     fruits3 = fruits[:]
# #     print(fruits3)
# #     fruits4 = fruits3[-4:-1]
# #     print(fruits4)
# #     fruits5 = fruits[::-2]
# #     print(fruits5)
# #
# # if __name__ == '__main__':
# #     list_d()
#
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a+b
#         yield a
#
# def list_e():
#     list1 = list(range(1, 11))
#     print(list1)
#     list2 = [x * x for x in range(1, 11)]
#     print(list2)
#     list3 = [m + n for m in 'ABCDEFG' for n in '12345']
#     print(list3)
#     print(len(list3))
#     gen = (m + n for m in 'abcdefgh' for n in '543210')
#     print(gen)
#     for elem in gen:
#         print(elem, end=' ')
#     print()
#     gen = fib(12)
#     print(gen)
#     for elem in gen:
#         print(elem, end=' ')
#     print()
#
# if __name__ == '__main__':
#     list_e()

# import os
# import time
#
# def strs():
#     str = "你是不能不漂荡的风，我是芒草走不动，等到风景都看透，可惜不是你，我听见风来自地铁和人海。"
#     while True:
#         print(str)
#         time.sleep(0.5)
#         str = str[1:] + str[0:1]
#         # os.system('clear')
#         # for windows use cls
#         os.system('cls')
#
# if __name__ == '__main__':
#     strs()

# score sheets

# def sheets():
#     names = ['哈罗德', '里瑟', '罗蒙', '肖', '莱尼尔']
#     subjec = ['English', 'Math', 'Computer']
#     scores = [[0]*3]*5
#     # for row, name in enumerate(names):
#     #     print(f"input {name}'s score")
#     #     for col, subje in enumerate(subjec):
#     #         scores[row][col] = float(input(subje + ': '))
#
#     for row, name in enumerate(names):
#         print(f"input {name}'s score")
#         scores[row] = [None] * len(subjec)
#         for col, subje in enumerate(subjec):
#             score = float(input(subje + ": "))
#             scores[row][col] = score
#
#     print(scores)
#
# if __name__ == '__main__':
#     sheets()

# 定义和使用集合

# def sets():
#     set1 = {1, 2, 3, 4, 4, 4, 5, 3, 2, 1}
#     print(set1)
#     print(f'Length = {len(set1)}')
#     set2 = set(range(2, 9))
#     print(set2)
#     set1.add(6)
#     set1.add(8)
#     set2.update([11, 13])
#     print(set1)
#     print(set2)
#     set2.discard(5)
#
#     if 4 in set2:
#         set2.remove(4)
#     print(set2)
#
#     for elem in set2:
#         print(elem **2, end=' ')
#     print()
#
#     set3 = set((2,3, 3, 2, 4)) #转化的同时是要排序的，234 然后pop 出了第一位的数字
#     print(set3.pop())
#     print(set3)
#
# if __name__ == '__main__':
#     sets()

# def set_two():
#     set1 = set(range(1, 7))
#     print(set1)
#     set2 = set(range(2, 13, 2))
#     print(set2)
#     set3 = set(range(1, 6))
#     print(set1 & set2)
#     print(set1 | set2)
#     print(set1 - set2)
#     print(set1 ^ set2)
#     print(set2 <= set1)
#     print(set3 <= set1)
#     print(set1 >= set2)
#     print(set1 >= set3)
#     print(set1.intersection(set2))
#     print(set1.union(set2))
#     print(set1.difference(set2))
#     print(set1.symmetric_difference(set2))
#     print(set2.issubset(set1))
#     print(set3.issubset(set1))
#     print(set1.issuperset(set2))
#     print(set1.issuperset(set3))
#
# if __name__ == '__main__':
#     set_two()

# 井字棋

# import os
#
# def print_board(board):
#     print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
#     print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
#     print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])\
#
# def play_s():
#     init_board = {
#         'TL': ' ', 'TM': ' ', 'TR': ' ',
#         'ML': ' ', 'MM': ' ', 'MR': ' ',
#         'BL': ' ', 'BM': ' ', 'BR': ' '
#     }
#     begin = True
#     while begin:
#         curr_board = init_board.copy()
#         begin = False
#         turn = 'x'
#         counter = 0
#         os.system('cls') #cls for windows clear for other os
#         print_board(curr_board)
#         while counter < 9:
#             move = input('该%s走棋了， 请输入位置： '%turn)
#             if curr_board[move] == ' ':
#                 counter +=1
#                 curr_board[move] = turn
#                 if turn == 'x':
#                     turn = 'o'
#                 else:
#                     turn = 'x'
#             os.system('cls')
#             print_board(curr_board)
#         choice = input("Once more(yes|no)")
#         begin = choice == 'yes'
#
# if __name__ == '__main__':
#     play_s()

# 元组的定义和使用
# def tupleone():
#     t = ('Robbin', 45, True, 'NY')
#     print(t)
#     print(t[1])
#     print(t[3])
#     for member in t:
#         print(member)
#     t = ('Ted', 48, True, "Chicago")
#     print(t)
#     person = list(t)
#     print(person)
#     person[0] = 'Marshall'
#     person[1] = 18
#     print(person)
#     fruits_list = ['apple', 'banana', 'orange']
#     fruits_tuple = tuple(fruits_list)
#     print(fruits_tuple)
#     print(fruits_tuple[1])
#
# if __name__ == '__main__':
#     tupleone()

# 杨辉三角
# def yang_triangle():
#     num = int(input("Number of rows: "))
#     yh = [[]]*num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row -1][col] + yh[row -1][col - 1]
#             print(yh[row][col], end='\t')
#         print()
# if __name__ == '__main__':
#     yang_triangle()