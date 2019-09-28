# class Person(object):
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     #访问器 getter方法
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     #修改器 - setter方法
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#     def play(self):
#         if self._age <= 16:
#             print(f'{self._name}正在玩飞行棋。')
#         else:
#             print(f"{self._name}正在玩斗地主。")
#
# def mainly():
#     person = Person("哈罗德", 30)
#     person.play()
#     person.age = 10
#     person.play()
#     person.name = 'Zoe'
#     person.play()
#
# if __name__ == '__main__':
#     mainly()

# class Person(object):
#     # 限定Person对象只能绑定_name, _age 和_gender属性
#     __slots__ = ('_name', '_age', '_gender')
#
#     def __init__(self, name, age, gender):
#         self._name = name
#         self._age = age
#         self._gender = gender
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
#     def gender(self):
#         return self._gender
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#     @name.setter
#     def name(self, name):
#         self._name = name
#     @gender.setter
#     def gender(self, gender):
#         self._gender = gender
#
#     def play(self):
#         if self._age <= 18:
#             print(f'{self._name}正在玩Umo, {self._gender} it is。')
#         else:
#             print(f'{self._name}正在玩宝可梦， maybe {self._gender} or not。')
#
# def mainly():
#     person = Person('Ted', 24, 'boy')
#     person.play()
#     person._gender = 'Man'
#     person.age = 10
#     person.play()
#     person._gender = 'Girl'
#     person._name = "Robbin"
#     person.play()
#
# if __name__ == '__main__':
#     mainly()

# from math import sqrt
#
# class Triangle(object):
#
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b
#
#     def perimeter(self):
#         return self._a + self._b +self._c
#
#     def area(self):
#         half = self.perimeter()/2
#         return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))
#
# def mainly():
#     # a, b, c = 9, 12, 15
#     a, b, c = 9, 8, 14
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         # same as print(Triangle.perimeter(t))
#         print(t.area())
#     else:
#         print('That is not triangle.')
#
# if __name__ == '__main__':
#     mainly()

# from time import time, localtime, sleep
# #
# # class Clock(object):
# #     '''
# #     数字时钟
# #     '''
# #     def __init__(self, hour=0, minute=0, second=0):
# #         self._hour = hour
# #         self._minute = minute
# #         self._second = second
# #
# #     @classmethod
# #     def now(cls):
# #         ctime = localtime(time())
# #         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
# #
# #     def run(self):
# #         '''走吧'''
# #         self._second += 1
# #         if self._second == 60:
# #             self._second = 0
# #             self._minute +=1
# #             if self._minute == 60:
# #                 self._minute =0
# #                 self._hour += 1
# #                 if self._hour == 24:
# #                     self._hour = 0
# #     def show(self):
# #         '''display time here'''
# #         return '%02d:%02d:%02d'%(self._hour, self._minute, self._second)
# #
# # def mainly():
# #     # 通过类方法创建对象并获取系统时间
# #     clock = Clock.now()
# #     timer = 0
# #     while timer < 31:
# #         print(clock.show())
# #         sleep(1)
# #         clock.run()
# #         timer +=1
# #
# # if __name__ == '__main__':
# #     mainly()

# class Person(object):
#     '''
#     man
#     '''
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         print(f"{self._name} just play.")
#
#     def watch_v(self):
#         if self._age >= 19:
#             print(f"{self._name} is watching game of throne.")
#         else:
#             print(f"{self._name} is watching person of interests.")
#
# class Student(Person):
#     """Students"""
#
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade
#
#     @property
#     def grade(self):
#         return self._grade
#
#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
#
#     def study(self, course):
#         print(f"{self._grade}的{self._name}正在学习{course}")
#
# class Teacher(Person):
#     """teacher"""
#
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title
#
#     @property
#     def title(self):
#         return self._title
#
#     def teach(self, course):
#         print(f"{self._name, self._title}正在讲{course}.")
#
# def mainly():
#     stu = Student('萨米恩', 17, '高三')
#     stu.study('法语')
#     stu.watch_v()
#     t = Teacher('斯威夫特', 43, 'Doc')
#     t.watch_v()
#
# if __name__ == '__main__':
#     mainly()

# from abc import ABCMeta, abstractmethod
#
# class Pet(object, metaclass=ABCMeta):
#     """pet"""
#
#     def __init__(self, nickname):
#         self._nickname = nickname
#
#     @abstractmethod
#     def make_voice(self):
#         """make sound"""
#         pass
#
# class Dog(Pet):
#     '''dog'''
#
#     def make_voice(self):
#         print(f"{self._nickname}wang, wang, wang.")
#
# class Cat(Pet):
#     """cat"""
#     def make_voice(self):
#         print(f"{self._nickname}miao, miao, miao.")
#
# def mainly():
#     pets = [Dog('小强'), Cat('Tom'), Dog('Monkey')]
#     for pet in pets:
#         pet.make_voice()
#
# if __name__ == '__main__':
#     mainly()

# from abc import ABCMeta, abstractmethod
# from random import randint, randrange
#
# class Fighter(object, metaclass=ABCMeta):
#     '''战斗者'''
#     # 通过__slots__魔法限定对象可以绑定的成员的变量
#     __slots__ = ('_name', '_hp')
#     def __init__(self, name, hp):
#         '''
#         初始化方法
#         :param name:
#         :param hp:生命值
#         '''
#         self._name = name
#         self._hp = hp
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def hp(self):
#         return self._hp
#
#     @hp.setter
#     def hp(self, hp):
#         self._hp = hp if hp >= 0 else 0
#
#     @property
#     def alive(self):
#         return self._hp > 0
#
#     @abstractmethod
#     def attack(self, other):
#         '''
#         攻击
#         :param other: 被攻击对象
#         :return:
#         '''
#         pass
#
# class Ultraman(Fighter):
#     '''
#     奥特曼
#     '''
#     __slots__ = ('_name', '_hp', '_mp')
#
#     def __init__(self, name, hp, mp):
#         '''
#         初始化方法
#         :param name: 名字
#         :param hp: 生命值
#         :param mp: 魔法值
#         '''
#         super().__init__(name, hp)
#         self._mp = mp
#
#     def attack(self, other):
#         other.hp -= randint(15, 25)
#
#     def huge_attack(self, other):
#         '''
#         必杀技 打掉对方至少50点 或四分之三的血
#         :param other: 被攻击对象
#         :return: 成功返回True 或者False
#         '''
#
#         if self._mp >= 50:
#             self._mp -= 50
#             injury = other.hp * 3 // 4
#             injury = injury if injury >= 50 else 50
#             other.hp -= injury
#             return True
#         else:
#             self.attack(other)
#             return False
#
#     def magic_attack(self, others):
#         '''
#         魔法攻击
#         :param others: 被攻击的群体
#         :return: 是否成功
#         '''
#         if self._mp >= 20:
#             self._mp -= 20
#             for temp in others:
#                 if temp.alive:
#                     temp.hp -= randint(10, 15)
#             return True
#         else:
#             return False
#
#     def resume(self):
#         '''
#         恢复魔法值
#         :return:
#         '''
#         incr_point = randint(1, 10)
#         self._mp += incr_point
#         return incr_point
#
#     def __str__(self):
#         return f'~~~{self._name}~~~\n' + f"生命值：{self._hp}\n" + f'魔法值：{self._mp}\n'
#
# class Monster(Fighter):
#     """
#     小怪兽
#     """
#     __slots__ = ('_name', '_hp')
#
#     def attack(self, other):
#         other.hp -= randint(10, 20)
#
#     def __str__(self):
#         return f'~~~{self._name}小怪兽~~~\n' + f'生命值：{self._hp}\n'
#
# def is_any_alive(monsters):
#     """
#         判断有没有小怪兽是活的
#         :return:
#     """
#     for monster in monsters:
#         if monster.alive > 0:
#             return True
#     return False
#
# def select_alive_one(monsters):
#     '''选中一只活着的小怪兽'''
#     monsters_len = len(monsters)
#     while True:
#         index = randrange(monsters_len)
#         monster = monsters[index]
#         if monster.alive > 0:
#             return monster
#
# def display_info(ultraman, monsters):
#     ''' 显示信息'''
#     print(ultraman)
#     for monster in monsters:
#         print(monster, end='')
#
# def mainly():
#     u = Ultraman('霍华德', 1000, 120)
#     m1 = Monster('多米尼克', 250)
#     m2 = Monster('撒马利', 500)
#     m3 = Monster('藤真', 750)
#     ms = [m1, m2, m3]
#     fight_round = 1
#     while u.alive and is_any_alive(ms):
#         print(f"========{fight_round}========")
#         m = select_alive_one(ms) #选中一只小怪兽
#         skill = randint(1, 10) #通过随机选择使用哪种技能
#         if skill <= 6: #60%的概率使用普通攻击
#             print(f'{u.name}使用普通攻击打了{m.name}.')
#             u.attack(m)
#             print(f"{u.name}的魔法值恢复了{u.resume()}")
#         elif skill <= 9: #30%的概率使用魔法攻击 可能会因为魔法值不足而失败
#             if u.magic_attack(ms):
#                 print(f"{u.name}使用了魔法攻击。")
#             else:
#                 print(f"{u.name}使用魔法失败")
#         else: #10%概率使用终极必杀技 如果魔法值不足则使用普通攻击
#             if u.huge_attack(m):
#                 print(f"{u.name}使用必杀技虐了{m.name}")
#             else:
#                 print(f"{u.name}使用普通攻击打了{m.name}")
#                 print(f"{u.name}的魔法值恢复了{u.resume()}点。")
#         if m.alive > 0: #如果选中的小怪兽没死，就回击
#             print(f"{m.name}回击了{u.name}")
#             m.attack(u)
#         display_info(u, ms) #显示每个回合结束之后双方的信息
#         fight_round += 1
#     print('\n========The end========\n')
#     if u.alive > 0:
#         print(f"{u.name}奥特曼胜利。")
#     else:
#         print('小怪兽胜利。')
#
# if __name__ == '__main__':
#     mainly()

# 扑克牌游戏

# from random import randrange
#
# class Card(object):
#     '''one card'''
#
#     def __init__(self, suite, face):
#         self._suite = suite
#         self._face = face
#
#     @property
#     def face(self):
#         return self._face
#
#     @property
#     def suite(self):
#         return self._suite
#
#     def __str__(self):
#         all_suites = ('bp', 'rp', 'bf', 'rs')
#         if self._face == 1:
#             face_str = 'A'
#         elif self._face == 11:
#             face_str = 'J'
#         elif self._face == 12:
#             face_str = 'Q'
#         elif self._face == 13:
#             face_str = 'K'
#         else:
#             face_str = str(self._face)
#         return f'{all_suites[self._suite], face_str}'
#
# class Poker(object):
#     '''one pack of card'''
#
#     def __init__(self):
#         self._cards = []
#         self._current = 0
#         for suite in range(4):
#             for face in range(1, 14):
#                 card = Card(suite, face)
#                 self._cards.append(card)
#
#     @property
#     def cards(self):
#         return self._cards
#
#     def shuffle(self):
#         '''洗牌 随机乱序'''
#         self._current = 0
#         cards_len = len(self._cards)
#         for index in range(cards_len):
#             pos = randrange(cards_len)
#             self._cards[index], self._cards[pos] = self._cards[pos], self._cards[index]
#
#     @property
#     def next(self):
#         '''hit me 发牌'''
#         card = self._cards[self._current]
#         self._current += 1
#         return card
#
#     @property
#     def has_next(self):
#         '''还没有发牌'''
#         return self._current < len(self._cards)
#
# class Player(object):
#     '''玩家'''
#
#     def __init__(self, name):
#         self._name = name
#         self._cards_on_hand = []
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def cards_on_hand(self):
#         return self._cards_on_hand
#
#     def get(self, card):
#         '''摸牌'''
#         self._cards_on_hand.append(card)
#
#     def arrange(self, card_key):
#         '''玩家整理牌'''
#         self._cards_on_hand.sort(key=card_key)
#
# def get_key(card):
#     return (card.suite, card.face)
#
# def mainly():
#     p = Poker()
#     p.shuffle()
#     players = [Player('关羽'), Player('秦琼'), Player('岳飞')]
#     for _ in range(13):
#         for player in players:
#             player.get(p.next)
#         for player in players:
#             print(player.name + ':', end=' ')
#             player.arrange(get_key)
#             for card in player.cards_on_hand:
#                 print(card, end=' ')
#             print()
#
# if __name__ == '__main__':
#     mainly()

# 算工资
#
# from abc import ABCMeta, abstractmethod
#
# class Employee(object, metaclass=ABCMeta):
#     '''员工'''
#
#     def __init__(self, name):
#         '''初始化
#         '''
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#     @abstractmethod
#     def get_salary(self):
#         '''月薪
#         '''
#         pass
# class Manager(Employee):
#     '''经理'''
#     def get_salary(self):
#         return 15000.0
# class Programmer(Employee):
#     '''程序员'''
#
#     def __init__(self, name, working_hour=0):
#         super().__init__(name)
#         self._working_hour = working_hour
#
#     @property
#     def working_hour(self):
#         return self._working_hour
#     @working_hour.setter
#     def working_hour(self, working_hour):
#         self._working_hour = working_hour if working_hour > 0 else 0
#
#     def get_salary(self):
#         return 150.0 * self._working_hour
#
# class Salesman(Employee):
#     '''销售员'''
#
#     def __init__(self, name, sales=0):
#         super().__init__(name)
#         self._sales = sales
#
#     @property
#     def sales(self):
#         return self._sales
#
#     @sales.setter
#     def sales(self, sales):
#         self._sales = sales if sales > 0 else 0
#
#     def get_salary(self):
#         return 1200.0 + self._sales * 0.05
#
# def mainly():
#     emps = [
#         Manager('刘备'), Programmer('孔明'),
#         Manager('曹操'), Salesman('郭嘉'),
#         Salesman('曹洪'), Programmer('司马懿'),
#         Programmer('周瑜')
#     ]
#     for emp in emps:
#         if isinstance(emp, Programmer):
#             emp.working_hour = int(input(f'请输入{emp.name}本月的工作时间(hour)：'))
#         elif isinstance(emp, Salesman):
#             emp.sales = float(input(f'请输入{emp.name}的销售额(元）：'))
#         #根据员工类别表现了计算工资要求的不同数据 多态
#         print(f'{emp.name}本月的工资是：{emp.get_salary()}')
#
# if __name__ == '__main__':
#     mainly()

# from math import sqrt
#
# class Point(object):
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
#
#     def move_to(self, x, y):
#         self._x = x
#         self._y = y
#
#     def move_by(self, dx, dy):
#         self._x += dx
#         self._y -= dy
#
#     def distance_to(self, other):
#         dx = self._x - other._x
#         dy = self._y - other._y
#         return sqrt(dx ** 2 + dy ** 2)
#
#     def __str__(self):
#         return f'{str(self._x), str(self._y)}'
#
# class Line(object):
#     def __init__(self, start=Point(0, 0), end = Point(0, 0)):
#         self._start = start
#         self._end = end
#
#     @property
#     def start(self):
#         return self._start
#
#     @start.setter
#     def start(self, start):
#         self._start = start
#
#     @property
#     def end(self):
#         return self.end
#     @end.setter
#     def end(self, end):
#         self._end = end
#
#     @property
#     def length(self):
#         return self._start.distance_to(self._end)
#
# if __name__ == "__main__":
#     p1 = Point(3, 8)
#     print(p1)
#     p2 = Point(-3, -20)
#     print(p2)
#     line = Line(p1, p2)
#     print(line.length)
#     line.start.move_to(3, 5)
#     line.end = Point(22, 1)
#     print(line.length)

# class Car(object):
#     __slots__=("_brand", "_max_speed")
#
#     def __init__(self, brand, max_speed):
#         self._brand = brand
#         self._max_speed = max_speed
#
#     @property
#     def brand(self):
#         return self._brand
#
#     @brand.setter
#     def brand(self, brand):
#         self._brand = brand
#
#     @brand.deleter
#     def brand(self):
#         del self._brand
#
#     @property
#     def max_speed(self):
#         return self._max_speed
#
#     @max_speed.setter
#     def max_speed(self, max_speed):
#         if max_speed < 0:
#             raise ValueError("Invalid max speed for car.")
#         self._max_speed = max_speed
#
#     def __str__(self):
#         return f'Car:[品牌={self.brand}, 最高时速={self.max_speed}]'
#
# car = Car('QQ', 25)
# print(car)
# car.max_speed = 250
# car.brand = 'Audi'
# print(car)
# # car.current_speed = 100  slots 限制了属性的修改 current 这个是没有的
# # 如果提供了删除器可以执行下面的代码
# del car.brand
# print(Car.brand)
# print(Car.brand.fget)
# print(Car.brand.fset)
# print(Car.brand.fdel)

# class Car(object):
#     def __init__(self, brand, max_speed):
#         self.set_brand(brand)
#         self.set_max_speed(max_speed)
#
#     def get_brand(self):
#         return self._brand
#     def set_brand(self, brand):
#         self._brand = brand
#
#     def get_max_speed(self):
#         return self._max_speed
#
#     def set_max_speed(self, max_speed):
#         if max_speed < 0:
#             raise ValueError('Invalid max speed for car.')
#         self._max_speed = max_speed
#     def __str__(self):
#         return f'Car:[品牌={self._brand}, 最高时速={self._max_speed}'
#
#     #用已有的修改器和访问器定义属性
#     brand = property(get_brand, set_brand)
#     max_speed = property(get_max_speed, set_max_speed)
#
# car = Car('volkswagen', 50)
# print(car)
# car.max_speed = -10
# print(car)
# car.max_speed = 300
# car.brand = 'BMW'
#
# print(car)
# print(Car.brand)
# print(Car.brand.fget)
# print(Car.brand.fset)

# from time import time, localtime, sleep
#
# class Clock(object):
#     '''数字始终'''
#
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
#
#     def run(self):
#         '''走你'''
#
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         '''display time'''
#         return '%02d:%02d:%02d'%(self._hour, self._minute, self._second)
#
# def mainly():
#     clock = Clock.now()
#     t = 1
#     while t < 15:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#         t += 1
#
# if __name__ == '__main__':
#     mainly()

'''对象之间的因爱关系和运算符号重载'''

# class Car(object):
#
#     def __init__(self, brand, max_speed):
#         self._brand = brand
#         self._max_speed = max_speed
#         self._current_speed = 0
#
#     @property
#     def brand(self):
#         return self._brand
#
#     def accelerate(self, delta):
#         self._current_speed += delta
#         if self._current_speed > self._max_speed:
#             self._current_speed = self._max_speed
#
#     def brake(self):
#         self._current_speed = 0
#
#     def __str__(self):
#         return f'{self._brand}当前时速{self._current_speed}.'
#
# class Student(object):
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     def drive(self, car):
#         print(f'{self._name}驾驶着{car._brand}欢快的去往新大陆。')
#         car.accelerate(30)
#         print(car)
#         car.accelerate(50)
#         print(car)
#         car.accelerate(50)
#         print(car)
#
#     def study(self, course_name):
#         print(f'{self._name}正在学习{course_name}')
#
#     def watch_mov(self):
#         if self._age < 19:
#             print(f'{self._name}只能观看小哪吒。')
#         else:
#             print(f'{self._name}正在观看红灯记。')
#
#     # 重载大于>运算符
#     def __gt__(self, other):
#         return self._age > other._age
#
#     # 重载小于<运算符
#     def __lt__(self, other):
#         return self._age < other._age
#
# if __name__ == '__main__':
#     stu1 = Student('张飞', 25)
#     stu1.study('octave')
#     stu1.watch_mov()
#     stu2 = Student('秦琼', 10)
#     stu2.study('数学')
#     stu2.watch_mov()
#     car = Car('BMW', 140)
#     stu2.drive(car)
#     print(stu1 > stu2)
#     print(stu2 > stu1)

# class A(object):
#
#     def foo(self):
#         print('foo of A')
#
# class B(A):
#     pass
#
# class C(A):
#
#     def foo(self):
#         print('foo of C')
#
# class D(B, C):
#     pass
#
# class E(D):
#
#     def foo(self):
#         print('foo in E')
#         super().foo()
#         super(B, self).foo()
#         super(C, self).foo()
#
# if __name__ == '__main__':
#     d = D()
#     d.foo()
#     e = E()
#     e.foo()

# from abc import ABCMeta, abstractmethod
#
# class Employee(object, metaclass=ABCMeta):
#
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @abstractmethod
#     def get_salary(self):
#         pass
#
# class Manager(Employee):
#
#     # 想一想：如果不定义构造方法怎么样
#     def __init__(self, name):
#         # 如果不调用父类构造器怎么样
#         super().__init__(name)
#
#     def get_salary(self):
#         return 12000
#
# class Programer(Employee):
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def set_working_hour(self, working_hour):
#         self._working_hour = working_hour
#
#     def get_salary(self):
#         return 100 * self._working_hour
#
# class Salesman(Employee):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def set_sales(self, sales):
#         self._sales = sales
#
#     def get_salary(self):
#         return 1500 + self._sales * 0.05
#
# if __name__ == '__main__':
#     emps = [Manager('李隆基'), Programer('姜维'), Salesman('赵云')]
#     for emp in emps:
#         if isinstance(emp, Programer):
#             working_hour = int(input(f'请输入{emp.name}本月工作时间。'))
#             emp.set_working_hour(working_hour)
#         elif isinstance(emp, Salesman):
#             sales = float(input(f'输入本月的{emp.name}销售额：'))
#             emp.set_sales(sales)
#
#         print(f'{emp.name}本月工资为：%.2f元。'%(emp.get_salary()))

# class Father(object):
#     def __init__(self, name):
#         self._name = name
#
#     def gamble(self):
#         print(f'{self._name}正在打麻将。')
#
#     def eat(self):
#         print(f'{self._name}在大吃大喝。')
#
# class Monk(object):
#     def __init__(self, name):
#         self._name = name
#
#     def eat(self):
#         print(f'{self._name}正在吃斋。')
#
#     def chant(self):
#         print(f'{self._name}正在念经。')
#
# class Musican(object):
#     def __init__(self, name):
#         self._name = name
#
#     def eat(self):
#         print(f"{self._name}正在胡吃海喝。")
#
#     def play_instrument(self):
#         print(f"{self._name}正在拉小提琴。")
#
# class Son(Father, Monk, Musican):
#
#     def __init__(self, name):
#         Father.__init__(self, name)
#         Monk.__init__(self, name)
#         Musican.__init__(self, name)
#
# son = Son('吕布')
# son.gamble()
# son.eat()
# son.chant()
# son.play_instrument()

# from abc import ABCMeta, abstractmethod
#
# class Pet(object, metaclass=ABCMeta):
#
#     def __init__(self, nickname):
#         self._nickname = nickname
#
#     @abstractmethod
#     def make_voice(self):
#         pass
#
# class Dog(Pet):
#
#     def make_voice(self):
#         print(f'{self._nickname}：汪汪汪。')
#
# class Cat(Pet):
#
#     def make_voice(self):
#         print(f"{self._nickname}:喵喵喵？")
#
# def petss():
#     pets= [Dog('Tom'), Cat('Jerry'), Dog('小强')]
#     for pet in pets:
#         pet.make_voice()
#
# if __name__ == '__main__':
#     petss()

# from math import gcd
#
# class Rathional(object):
#
#     def __init__(self, num, den=1):
#         if den == 0:
#             raise ValueError('分母不能为0.')
#         self._num = num
#         self._den = den
#         self.normalize()
#
#     def simplify(self):
#         x = abs(self._num)
#         y = abs(self._den)
#         factor = gcd(x, y)
#         if factor > 1:
#             self._num //= factor
#             self._den //= factor
#
#         return self
#
#     def normalize(self):
#         if self._den < 0:
#             self._den = -self._den
#             self._num = -self._num
#         return self
#
#     def __add__(self, other):
#         new_num = self._num * other._den + other._num * self._den
#         new_den = self._den * other._den
#         return Rathional(new_num, new_den).simplify().normalize()
#
#     def __sub__(self, other):
#         new_num = self._num * other._den + other._num * self._den
#         new_den = self._den * other._den
#         return Rathional(new_num, new_den).simplify().normalize()
#     def __mul__(self, other):
#         new_num = self._num * other._num
#         new_den = self._den * other._den
#         return Rathional(new_num, new_den).simplify().normalize()
#     def __truediv__(self, other):
#         new_num = self._num * other._den
#         new_den = self._den * other._num
#         return Rathional(new_num, new_den).simplify().normalize()
#
#     def __str__(self):
#         if self._num == 0:
#             return '0'
#         elif self._den == 1:
#             return str(self._num)
#         else:
#             return f'({self._num, self._den})'
#
#
# if __name__ == '__main__':
#     r1 = Rathional(3, 4)
#     print(r1)
#     r2 = Rathional(8, -4)
#     print(r2)
#     print(r2.simplify())
#     print(f'{r1} + {r2} = {r1 + r2}')
#     print(f'{r1} - {r2} = {r1 - r2}')
#     print(f'{r1} * {r2} = {r1 * r2}')
#     print(f'{r1} / {r2} = {r1 / r2}')
#
# from abc import ABCMeta, abstractmethod
# from math import pi
#
# class Shape(object, metaclass=ABCMeta):
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self._radius = radius
#
#     def perimeter(self):
#         return 2 * pi * self._radius
#
#     def area(self):
#         return '%.4f'%(pi * self._radius ** 2)
#
#     def __str__(self):
#         return 'The Circle it is.'
#
# class Rect(Shape):
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#
#     def perimeter(self):
#         return 2 * (self._width + self._height)
#
#     def area(self):
#         return self._width * self._height
#
#     def __str__(self):
#         return 'The Rect it is.'
#
# if __name__ == '__main__':
#     shapes = [Circle(6), Circle(4.5), Rect(12, 5)]
#     for shape in shapes:
#         print(shape)
#         print('周长:', shape.perimeter())
#         print('面积:', shape.area())

# from math import sqrt
#
# class Triangle(object):
#
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b # 判断是不是能构成三角形
#
#     def perimeter(self):
#         return self._a + self._b + self._c
#
#     def area(self):
#         p = self.perimeter() / 2
#         return sqrt(p*(p - self._a) * (p - self._b) * (p - self._c))
#
#
# if __name__ == '__main__':
# # 用字符串的split方法将字符串拆分成一个列表
# # 通过map 函数对列表中的每个字符进行映射处理小数
#
#     a, b, c = map(float, input('请输入三条边：').split())
#     # 先判断是否构成三角形
# # 然后创建对象
#     if Triangle.is_valid(a, b, c):
#         tri = Triangle(a, b, c)
#         print('周长：', tri.perimeter())
#         print('面积：', tri.area())
#         print(Triangle.perimeter(tri))
#         # 两种方式效果都一样
#
#     else:
#         print('不能构成三角形。')