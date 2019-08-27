# import time
#
# class Clock(object):
#     def __init__(self, hour=0, minute=0, second=0):
#         """构造器
#         :param hour:
#         :param minute:
#         :param second:
#         """
#
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def run(self):
#         """
#         走字
#         :return:
#         """
#         self._second +=1
#         if self._second ==60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def __str__(self):
#         """
#         显示手机
#         :return:
#         """
#         return '%02d:%02d:%02d'% \
#                (self._hour, self._minute, self._second)
#
# def make_clock():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock)
#         time.sleep(1)
#         clock.run()
#
# if __name__ == '__main__':
#     make_clock()
# from math import sqrt
#
# class Point(object):
#
#     def __init__(self, x=0, y=0):
#         '''
#         构造器
#         :param x: 横坐标
#         :param y: 纵坐标
#         '''
#         self.x = x
#         self.y = y
#
#     def move_to(self, x, y):
#         '''
#         移动到指定位置
#         :param x: 新的横坐标
#         :param y: 新的纵坐标
#         :return:
#         '''
#         self.x = x
#         self.y = y
#
#     def move_by(self, dx, dy):
#         '''
#         移动指定的增量
#         :param dx: 横坐标的增量
#         :param dy: 纵坐标的增量
#         :return:
#         '''
#         self.x += dx
#         self.y += dy
#
#     def distance_to(self, other):
#         '''
#         计算与另一个点的距离
#         :param other: 另一个点
#         :return:
#         '''
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
#
#     def __str__(self):
#         return f'({str(self.x)}, {str(self.y)})'
#
# def get_point():
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     p2.move_by(-2, 3)
#     print(p2)
#     print(p1.distance_to(p2))
#
# if __name__ == '__main__':
#     get_point()

# class Test:
#     def __init__(self, foo):
#         self.__foo = foo
#
#     def __bar(self):
#         print(self.__foo)
#         print('__bar')
#
# def foo_t():
#     test = Test('Hello')
#     test._Test__bar()
#     print(test._Test__foo)
#
# if __name__ == '__main__':
#     foo_t()

#计算泳池的造价

# import math
#
# class Circle(object):
#
#     def __init__(self, radius):
#         self._radius = radius
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, radius):
#         self._radius = radius if radius > 0 else 0
#
#     @property
#     def perimeter(self):
#         return 2*math.pi * self._radius
#
#     @property
#     def area(self):
#         return math.pi *self._radius * self._radius
#
# if __name__ == '__main__':
#     radius = float(input('输入用泳池的半径：'))
#     small = Circle(radius)
#     big = Circle(radius + 3)
#     print('围墙的造价是： %.2f元'%(big.perimeter*32.5)) #(r+3)*2*Π*32.5
#     print("过道的造价是： %.2f元"%((big.area - small.area)*25))

#定义使用时钟
# import time
# import os
#
# class Clock(object):
#     '''
#     python中的函数没有重载的概念的
#     因为python中的函数的参数没有类型而且支持缺省参数和可变参数
#     用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
#     '''
#     def __init__(self, **kw):
#         if 'hour' in kw and 'minute' in kw and 'second' in kw:
#             self._hour = kw['hour']
#             self._minute = kw['minute']
#             self._second = kw['second']
#         else:
#             tm = time.localtime(time.time())
#             self._hour = tm.tm_hour
#             self._minute = tm.tm_min #这里不一样 不一样
#             self._second = tm.tm_sec #不一样
#
#     def run_co(self):
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute +=1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour +=1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show_t(self):
#         return '%02d:%02d:%02d'%(self._hour, self._minute, self._second)
#
# if __name__ == '__main__':
#     clock = Clock()
#     t1 = 0
#     while t1 <= 30:
#         os.system('cls') #cls or clear
#         print(clock.show_t())
#         time.sleep(1)
#         clock.run_co()
#         t1 +=1

#猜大小
# from random import randint
#
# class GuessMachine(object):
#
#     def __init__(self):
#         self._answer = None
#         self._counter = None
#         self._hint = None
#
#     def reset(self):
#         self._answer = randint(1, 100)
#         self._counter = 0
#         self._hint = None
#
#     def guess(self, your_answer):
#         self._counter +=1
#         if your_answer > self._answer:
#             self._hint = "大了"
#         elif your_answer < self._answer:
#             self._hint = "小了"
#         else:
#             self._hint = '恭喜你'
#             return True
#         return False
#
#     @property
#     def counter(self):
#         return self._counter
#     @property
#     def hint(self):
#         return self._hint
#
# if __name__ == '__main__':
#     gm = GuessMachine()
#     play_again = True
#     while play_again:
#         game_over = False
#         gm.reset()
#         while not game_over:
#             your_answer = int(input('输入一个整数： '))
#             game_over = gm.guess(your_answer)
#             print(gm.hint)
#         if gm.counter > 7:
#             print("检查一下智商")
#         play_again = input("once more? (yes|no)") == "yes"

# do another way

# def bar(self, name):
#     self._name = name
#
# def foo(self, course_name):
#     print(f'{self._name}正在学习{course_name}')
#
# def all_is():
#     Student = type('Student', (object,), dict(__init__ = bar, study = foo))
#     stu1 = Student('Joey')
#     stu1.study('how you doing class')
#
# if __name__ == '__main__':
#     all_is()

# 定义使用类

# class Rect(object):
#     '''
#     矩形类
#     '''
#
#     def __init__(self, width=0, height=0):
#         '''
#         构造器
#         :param width:
#         :param height:
#         '''
#         self.__width = width
#         self.__height = height
#
#     def perimeter(self):
#         '''
#         计算周长
#         :return:
#         '''
#         return (self.__width + self.__height) * 2
#     def area(self):
#         '''
#         面积
#         :return:
#         '''
#         return self.__width * self.__height
#     def __str__(self):
#         '''
#         矩形对象的字符串表达式
#         :return:
#         '''
#
#         return f'矩形[{self.__width}, {self.__height}]'
#
#     def __del__(self):
#         '''析构器'''
#         print('清除对象')
#
# if __name__ == '__main__':
#     rect1 = Rect()
#     print(rect1)
#     print(rect1.perimeter())
#     print(rect1.area())
#     rect2 = Rect(23, 4)
#     print(rect2)
#     print(rect2.perimeter())
#     print(rect2.area())

# def _foo():
#     print('test')
#
# class Student(object):
#     '''
#     __init__ 是一个特殊的方法用于在创建对象是进行初始化操作
#     通过这个方法我们可以为学生对象绑定name age 属性
#     '''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def study(self, course_name):
#         print(f"{self.name} 正在学习 {course_name}")
#
#     def watch_v(self):
#         if self.age < 18:
#             print(f"{self.name} 只能观看《海绵宝宝》。")
#         else:
#             print(f"{self.name} 正在观看《唐顿庄园》。")
#
# def mainly():
#     stu1 = Student('福尔摩斯', 44)
#     stu1.study('犯罪心理学')
#     stu1.watch_v()
#     stu2 = Student('哪吒', 3)
#     stu2.study('溜冰鞋实践')
#     stu2.watch_v()
# if __name__ == '__main__':
#     mainly()