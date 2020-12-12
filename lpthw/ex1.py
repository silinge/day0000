# print("Hello 2019")
# print("hello there")
# print("what's up 'hi'.")
# print('I "said" do not, do I?')
# print("one line is OK ", end = "")
# print("see it is on one line?")
# print()
# print("another line blank line is ", )
# for s in "visual studio":
#     if s == "o":
#         continue
#     print(s, end=" ")

# for s in "visual studio":
#     if s == 'o':
#         break
#     print(s, end=">>")
# import random
# t = (1, 2, 3, 54, 5, 4, 333,)
# print(random.sample(t, 3))

# import random
# print(random.randint(1, 101))
# print(random.randrange(1, 100, 2))
# print(random.sample("abcdefjhigk", 5))
# print(random.choice(["apple", "banana", "canary", "davinci"]))
# meet pi
# from random import random
# from math import sqrt
# from time import clock
# import time
# DARTS = 10000
# hits = 0.0
# clock()
# for i in range(1, DARTS+1):
#     x,y = random(), random()
#     dist = sqrt(x**2 + y**2)
#     if dist <= 1.0:
#         hits = hits + 1
# pi = 4 * (hits/DARTS)
# print("Pi值是{}.".format(pi))
# print("运行时间是：{:5.5}s".format(clock()))
# time.perf_counter()
# print("运行时间是：{:5.5}s".format(time.perf_counter()))

# from random import random
# from math import sqrt
# import time
# DARTS = 10000
# hits = 0.0
# for i in range(1, DARTS+1):
#     x, y = random(), random()
#     dist = sqrt(x**2+y**2)
#     if dist <= 1.0:
#         hits = hits + 1
# pi = 4 * (hits/DARTS)
# print("Pi值是{}.".format(pi))
# print("运行时间是{:5}s".format(time.process_time()))

# from random import random
# from math import sqrt
# import time
# DARTS = 10000
# hits = 0.0
# for i in range(1, DARTS+1):
#     x, y = random(), random()
#     dist = sqrt(x**2 + y**2)
#     if dist <= 1.0:
#         hits = hits + 1
# pi = 4 * (hits/DARTS)
# print("pi值是{}.".format(pi))
# print("运行时间{:5.5}s".format(time.perf_counter()))

# from random import random
# from math import sqrt
# import time
# DARTS=10000
# hits = 0.0
# for i in range(1, DARTS+1):
#     x, y = random(), random()
#     dist = sqrt(x**2+y**2)
#     if dist <= 1.0:
#         hits = hits +1
# pi = 4 * (hits/DARTS)
# print("Pi的值是{}、".format(pi))
# print("运行时间{:5.5}s".format(time.perf_counter()))

# from random import randint
# G = randint(0, 9)
# N = 0
#
# while True:
#     guess = eval(input("输入一个整数（0-9）："))
#     N = N + 1
#     if guess > G:
#         print("大了。")
#     elif guess < G:
#         print("小了。")
#     else:
#         print(f"预测了{N}次，猜中了。")
#         break

# allstring = "你是不能不飘荡的风,我是芒草走不动,s'il vous plait vous amiez cef. little little star."
# abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# pun = ",./;'[]!@#$%^&*()_+-=~\\ "
# ch = 0
# en = 0
# pu = 0
# for i in allstring:
#     if i in abc:
#         en += 1
#     elif i in pun:
#         pu += 1
#     else:
#         ch += 1
# print(f"这句话总共有{ch}个中文字符，{en}个英文字符，{pu}个其他字符。")

# def fun1(a, b):
#     temp = a % b
#     while (temp != 0):
#         a = b
#         b = temp
#         temp = a % b
#     return b
#
# def fun2(a, b):
#     return a * b / fun1(a, b)
#
# print(fun1(16, 1000))
# print(fun2(16, 1000))

# def fun1(a, b):
#     temp = a % b
#     while temp != 0:
#         a = b
#         b = temp
#         temp = a % b
#     return b
#
# print(fun1(50, 300))

# from random import *
# Times = 10000
# my_first_choice_n = 0
# my_change_choice_n = 0
# for i in range(Times):
#     car_inDoor = randint(0, 2)
#     my_guess = randint(0,2)
#     if car_inDoor == my_guess:
#         my_first_choice_n += 1
#     else:
#         my_change_choice_n += 1
# print(f"不更改选择{my_first_choice_n/Times}")
# print(f"更改选择：{my_change_choice_n/Times}")

# from random import *
# TIMES = 100000
# my_first_choice_n = 0
# my_change_choice_n = 0
# for i in range(TIMES):
#     car_inDoor = randint(0,2)
#     my_guess = randint(0,2)
#     if car_inDoor == my_guess:
#         my_first_choice_n += 1
#     else:
#         my_change_choice_n += 1
# print(f"不更改选择的几率{my_first_choice_n/TIMES}")
# print(f"更改选择{my_change_choice_n/TIMES}")
# f = lambda x, y : x ** y
# print(type(f))
# print(f(3, 5))

# def vfunc(a, *b):
#     print(type(b))
#     for n in b:
#         a += n
#     return a
# print(vfunc(9, 3, 4, 5, 3, 4, 5))
# n=1
# def func(a, b):
#     global n
#     n = b
#     return a*b
# s = func("dong@dong~", 3)
# print(s)
# print(n)

# from datetime import datetime
# print(datetime.tzinfo)
# from datetime import datetime
# # today = datetime.now()
# today = datetime.utcnow()
# print(today)

# import turtle, datetime
# def drawline(draw):
#     turtle.pendown() if draw else turtle.penup()
#     turtle.fd(40)
#     turtle.right(90)
# def drawDigit(d):
#     drawline(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
#     drawline(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
#     drawline(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
#     drawline(True) if d in [0, 2, 6, 8] else drawline(False)
#     turtle.left(90)
#     drawline(True) if d in [0, 4, 5, 6, 8, 9] else drawline(False)
#     drawline(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
#     drawline(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
#     turtle.left(180)
#     turtle.penup()
#     turtle.fd(20)
# def drawdate(date):
#     for i in date:
#         drawDigit(eval(i))
#
# def main():
#     turtle.setup(800, 400, 240, 240)
#     turtle.penup()
#     turtle.fd(-300)
#     turtle.pensize(5)
#     turtle.pencolor("green")
#     drawdate(datetime.datetime.now().strftime("%Y%m%d"))
#     turtle.hideturtle()
# main()

# import turtle, datetime
# def drawGap():
#     turtle.penup()
#     turtle.fd(5)
#
# def drawLine(draw):
#     drawGap()
#     turtle.pendown() if draw else turtle.penup()
#     turtle.fd(40)
#     drawGap()
#     turtle.right(90)
# def drawDigit(d): #从数字的中心笔划开始 自左向右 再向右
#     drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
#     turtle.left(90)
#     drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
#     turtle.left(180)
#     turtle.penup()
#     turtle.fd(20)
#
# def drawDate(date):
#     turtle.pencolor('Green')
#     for i in date:
#         if i == '-':
#             turtle.write("年", font=("Arial", 24, "normal"))
#             turtle.pencolor('red')
#             turtle.fd(40)
#         elif i == '=':
#             turtle.write('月', font=("Arial", 24, 'normal'))
#             turtle.pencolor("blue")
#             turtle.fd(40)
#         elif i == '+':
#             turtle.write("日", font=("Arial", 24, 'normal'))
#         else:
#             drawDigit(eval(i))
#
# def main():
#     turtle.setup(800, 500, 300, 300)
#     turtle.penup()
#     turtle.fd(-350)
#     turtle.pensize(5)
#     drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
#     turtle.hideturtle()
# main()

# import turtle, datetime
# def drawGap():#绘制数码管间隔
#     turtle.penup()
#     turtle.fd(5)
# def drawLine(draw):
#     drawGap()
#     turtle.pendown() if draw else turtle.penup()
#     turtle.fd(40)
#     drawGap()
#     turtle.right(90)
# def drawDigit(d):
#     drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
#     turtle.left(90)
#     drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
#     drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
#     turtle.left(180)
#     turtle.penup()
#     turtle.fd(20)
# def drawDate(date):
#     turtle.pencolor('blue')
#     for i in date:
#         if i == '-':
#             turtle.write('YEAR', font=("Arial", 18, "normal"))
#             turtle.pencolor("green")
#             turtle.fd(40)
#         elif i == "=":
#             turtle.write("Month", font=("Arial", 18, "normal"))
#             turtle.pencolor('yellow')
#             turtle.fd(40)
#         elif i == '+':
#             turtle.write('Day', font=("Arial", 18, 'normal'))
#             turtle.pencolor('cyan')
#             turtle.fd(40)
#         else:
#             drawDigit(eval(i))
# def main():
#     turtle.setup(800, 800, 240, 240)
#     turtle.penup()
#     turtle.fd(-350)
#     turtle.pensize(5)
#     drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
#     turtle.delay(10)
#     turtle.hideturtle()
# main()

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
# num = eval(input("输入一个整数："))
# print(fact(abs(int(num))))

# def reverse(s):
#     if s == "":
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
# str1 = input("输入一个字符串：")
# print(reverse(str1))

# import turtle
# def kooh(size, n):
#     if n == 0:
#         turtle.fd(size)
#     else:
#         for angle in [0, 60, -120, 60]:
#             turtle.left(angle)
#             kooh(size/3, n-1)
# def main():
#     turtle.setup(800, 800)
#     turtle.speed(1)
#     turtle.penup()
#     turtle.goto(-300, -50)
#     turtle.pendown()
#     turtle.pensize(3)
#     kooh(600, 3)
#     turtle.hideturtle()
# main()

# import turtle as t
# def kooh(size, n):
#     if n == 0:
#         t.fd(size)
#     else:
#         for angle in [0, 60, -120, 60]:
#             t.left(angle)
#             kooh(size/3, n-1)
# def main():
#     t.setup(800, 800)
#     t.speed(0)
#     t.penup()
#     t.goto(-200, 100)
#     t.pendown()
#     t.pensize(3)
#     level=5
#     kooh(400, level)
#     t.right(120)
#     kooh(400, level)
#     t.right(120)
#     kooh(400, level)
#     t.hideturtle()
# main()

# import turtle as tu
# def drawAntline():
#     tu.fd(10)
#     tu.penup()
#     tu.fd(10)
#     tu.pendown()
# def drawOneside():
#     for i in range(5):
#         drawAntline()
#
# def drawLongside():
#     for i in range(4):
#         drawOneside()
#     tu.fd(10)
# def drawRside():
#     drawLongside()
#     tu.right(90)
#     tu.penup()
#     tu.fd(100)
#     tu.right(90)
#     tu.pendown()
#
# def drawLside():
#     drawLongside()
#     tu.left(90)
#     tu.penup()
#     tu.fd(100)
#     tu.left(90)
#     tu.pendown()
# def drawLines():
#     drawRside()
#     drawLside()
#     drawRside()
#     drawLside()
#     drawLongside()
#
# def drawRows():
#     drawLside()
#     drawRside()
#     drawLside()
#     drawRside()
#     drawLongside()
#
#
# def main():
#     tu.setup(800, 800)
#     tu.speed(4)
#     tu.penup()
#     tu.goto(-200, 200)
#     tu.pendown()
#     tu.pensize(1)
#     drawLines()
#     tu.penup()
#     tu.right(90)
#     tu.fd(5)
#     tu.right(90)
#     tu.fd(5)
#     tu.right(90)
#     tu.pendown()
#     drawRows()
#     tu.hideturtle()
#
# main()

# print("hello world")
# print("I will now count my chickens:")
# print("Hens", 25+30/5)
# print("Roosters", 100-25*3/4)
# print("Now I will count the eggs:")
# print(3 + 2 + 1 - 5 +4%2-1/4+6)
# print("Is it truw that 3 + 2 < 5-7?")
# print("What is 3 + 2?", 3+2)
# print("what is 5-7?", 5-7)
# print("Oh, that's why it's False")
# print("How about some more.")
# print("Is it greater?", 5>-2)
# print("Is it greater or equal?", 5>=-2)
# print("is it less or equal?", 5<=-2)

# types_of_people = 10
# x = f"There are {types_of_people} types of people"
# binary = "binary"
# do_not = "don't"
# y = f"Those who know {binary} and those who {do_not}."
# print(x)
# print(y)
# print(f"I said:{x}")
# print(f"I also said:'{y}'")
# hilarious = False
# joke_evaluation = "Isn't that joke so funny?!{}"
# print(joke_evaluation.format(hilarious))
# w = "This is the left side of..."
# e = "a string with a right side."
# print(w +e)

# print("Mary had a little lamb")
# print("Its fleece was white as {}.".format('snow'))
# print("And everywhere that Mary went.")
# print("."* 12)
# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"
# print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# print(end7 + end8 + end9 + end10 + end11 + end12)

# formatter = "{} {} {} {}"
# print(formatter.format(1, 2, 3, 4))
# print(formatter.format("one", "two", "three", "four"))
# print(formatter.format(True, False, False, True))
# print(formatter.format(formatter, formatter, formatter, formatter))
# print(formatter.format(
#     "try your",
#     "own text here",
#     "Maybe a poem",
#     "or a song about fear"
# ))

# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"
#
# print("Here are the days: ", days)
# print("Here are the months: ", months)
# print("""There;s something going on here.
# with the three double-quotes.
# We'll be able to type as much as we like
# Even 4 lines if we want, or 5, or 6.""")

# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\a \\cat."
# fat_cat = """
# I'll do a list:
# \t* cat food
# \t* fishies
# \t* catnip\n\t* Grass
# """
# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

# print("How old are you?", end=' ')
# age = input("enter your age:")
# print("How tall are you?", end=' ')
# height = input("enter your height(cm):")
# print("How much do you weigh?", end=' ')
# weight = input("enter your weight(kg):")
# print(f"So, you are {age} year old, {height} tall and {weight} heavy.")

# age = input("How old are you?")
# height = input("How tall are you?")
# weight = input("How much do you weight?")
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# from sys import argv
# script, first, second, third = argv
# print("The script is called:", script)
# print("Your first variable is :", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)
# print(input("this is a new line, you can type sth here:"))
# from sys import argv
# script, user_name = argv
# prompt='>'
#
# print(f"Hi {user_name}, I'm the {script} script.")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
# likes = input(prompt)
# print(f"Where do you live {user_name}?")
# lives = input(prompt)
# print("What kind of computer do you have?")
# computer = input(prompt)
# print(f"""
# Alright, so you said {likes} about liking me.
# You live in {lives}. Not sure where that is.
# And you have a {computer} computer. Nice.
# """)

# from sys import argv
# script, filename = argv
# txt = open(filename)
# print(f"Here's your file {filename}:")
# print(txt.read())
# print("Type the filename again:")
# file_again = input("> ")
# txt_again = open(file_again)
# print(txt_again.read())

# from sys import argv
# script, filename = argv
#
# print(f"We're going to erase {filename}.")
# print("If you don't want that, hit CTRL-C(^C).")
# print("If you do want that, hit RETURN")
# input("Opening the file...")
# target = open(filename, 'w')
# print("Truncating the file, Goodbye!")
# target.truncate()
# print("Now I'm going to ask you for three lines.")
# line1 = input("line 1:")
# line2 = input("line 2:")
# line3 = input("line 3:")
# print("I'm going to write these to the file.")
#
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
#
# print("And finally, we close it.")
# target.close()

# from sys import argv
# from os.path import exists
# script, from_file, to_file = argv
#
# print(f"copying form {from_file} to {to_file}")
# in_file = open(from_file)
# indata = in_file.read()
# print(f"The input file is {len(indata)} bytes long")
# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()
# out_file = open(to_file, 'w')
# out_file.write(indata)
# print("Alright, all done.")
# out_file.close()
# in_file.close()

# def print_two(*args):
#     arg1, arg2 = args
#     print(f"arg1: {arg1}, arg2:{arg2}")
#
# def print_two_again(arg1, arg2):
#     print(f"arg1: {arg1}, arg2: {arg2}")
#
# def print_one(arg1):
#     print(f"arg1: {arg1}")
#
# def print_none():
#     print("I got nothing'.")
# print_two("zed", "shaw")
# print_two_again("Swift", "Joe")
# print_one("SECOND")
# print_none()

# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print(f"You have {cheese_count} cheeses!")
#     print(f"You have {boxes_of_crackers} boxes of crackers!")
#     print("Man that's enough for a party!")
#     print("Get a blanket.\n")
#
# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 30)
#
# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
# print("We can even do much inside too:")
# cheese_and_crackers(10+20, 5+6)
#
# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# from sys import argv
# script, input_file = argv
#
# def print_all(f):
#     print(f.read())
#
# def rewind(f):
#     f.seek(0)
#
# def print_a_line(line_count, f):
#     print(line_count, f.readline())
# current_file = open(input_file)
# print("First let's print the whole file:\n")
# print_all(current_file)
# print("Now let's rewind, kind of like a tape.")
# rewind(current_file)
#
# print("Let's print three lines:")
# current_line = 1
# print_a_line(current_line, current_file)
# current_line = current_line + 1
# print_a_line(current_line, current_file)
# current_line = current_line + 1
# print_a_line(current_line, current_file)


# def add(a, b):
#     print(f"adding {a} + {b}")
#     return a + b
#
# def subtract(a, b):
#     print(f"Subtracting {a} - {b}")
#     return a - b
#
# def multiply(a, b):
#     print(f"MULTIPLY {a} * {b}")
#     return a * b
#
# def divide(a, b):
#     print(f"Diving {a} / {b}")
#     return a / b
#
# print("Let's do some math with just funcitions.")
#
# age = add(20, 12)
# height = subtract(78, 8)
# weight = multiply(90, 2)
# iq = divide(100, 2)
#
# print(f"AGE:{age}, Height:{height}, Weight:{weight}, IQ:{iq}.")
#
# print("here is a puzzle.")
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# print("That becomes:", what, "Can you do it by hand?")
# import sys
# script, encoding, error = sys.argv
#
# def main(language_file, encoding, errors):
#     line = language_file.readline()
#
#     if line:
#         print_line(line, encoding, errors)
#         return main(language_file, encoding, errors)
#
# def print_line(line, encoding, errors):
#     next_lang = line.strip()
#     raw_bytes = next_lang.encode(encoding, errors=errors)
#     cooked_string = raw_bytes.decode(encoding, errors=errors)
#     print(raw_bytes, "<==>", cooked_string)
# languages = open("languages.txt", encoding="utf-8")
#
# main(languages, encoding, error)

# print("Let's practice everything.")
# print('You\' d need to know \' bout escapes with \\that do:')
# print('\n newlines and \t tabs.')
# poem="""
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\t\t where there is none.
# """
# print("-----------------")
# print(poem)
# print("-----------------")
# five = 10-2+3-6
# print(f"This should be five:{five}")
# def secret_formula(started):
#     jelly_beams =started * 500
#     jars= jelly_beams/1000
#     crates = jars / 100
#     return jelly_beams, jars, crates
#
# start_point = 10000
# beans, jars, crates = secret_formula(start_point)
#
# print("With a starting point of :{}".format(start_point))
# print(f"We'd have {beans} beans, {jars}jars, and {crates}crates.")
#
# start_point = start_point/10
# print("We can also do that this way:")
# formula = secret_formula(start_point)
# print("We'd have {} beans, {}jars, and {} crates.".format(*formula))

# def break_words(stuff):
#     """this function will break up words for u"""
#     words = stuff.split(' ')
#     return words
#
# def sort_words(words):
#     """sorts the words"""
#     return sorted(words)
#
# def print_first_word(words):
#     word = words.pop(0)
#     print(word)
#
# def print_last_word(words):
#     word = words.pop(-1)
#     print(word)
#
# def sort_sentence(sentence):
#     words = break_words(sentence)
#     return sort_words(words)
#
# def print_first_and_last(sentence):
#     words = break_words(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
# def print_first_and_last_sorted(sentence):
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
# print("How old are you?", end=' ')
# age = input()
# print("How tall are you?", end=' ')
# height = input("> >")
# print("How much do you weight?", end=' ')
# weight = input()
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# from sys import argv
# script, filename = argv
#
# txt = open(filename)
# print(f"Here's your file{filename}:")
# print(txt.read())
# print("Type the filename again:")
# file_again = input("> ")
# txt_again = open(file_again)
#
# print(txt_again.read())
# print("let's practice everythin.")
# print('you\'d need to know \' bout escapes with \\ that do \n newlines and \t tabs.')
#
# poem = """
# \t The lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\twhere there is none.
# """
# print("---")
# print(poem)
# print("----")
# five = 10 - 2 + 3 -6
# print(f"This should be five:{five}")
# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars * 100
#     return jelly_beans, jars, crates
#
# start_point = 10000
# jelly_beans, jars, crates = secret_formula(start_point)
# print("With a starting point of :{}".format(start_point))
# print(f"We'd have {jelly_beans} beans, {jars} jars, and {crates} crates.")
#
# start_point = start_point / 10
# print("WE CAN ALSO DO THAT THIS WAY:")
# formula = secret_formula(start_point)
# print("We'd have {}beans, {} jars, and {} crates.".format(*formula))
#
# people = 20
# cates = 30
# dogs = 15
# if people < cates:
#     print("Too many cats! the world is doomed!")
# if people < cates:
#     print("Not many cats! the world is saved.")
# if people < dogs:
#     print("The world is drooled on.")
# if people > dogs:
#     print("The world is dry.")
#
# dogs += 5
# if people >= dogs:
#     print("People are greater than or equal to dogs.")
# if people <= dogs:
#     print("People are less than or equal to dogs.")
# if people==dogs:
#     print("people are equal numbers to dogs.")

# people = 30
# cats = 30
# dogs = 15
#
# if people < cats:
#     print("Too many cats! The world is doomed!")
#
# if people > cats:
#     print("Not many cats")
# if people < dogs:
#     print("The world is drooled on")
#
# if people > dogs:
#     print("The world is dry")
#
# dogs += 5
# if people >= dogs:
#     print("Peo are greater than or equal to dogs.")
#
# if people <= dogs:
#     print("People are less than or equal to dog")
#
# if people == dogs:
#     print("People are dogs.")

# people = 30
# cars = 40
# trucks = 15
#
# if cars > people:
#     print("We should take the cars")
# elif cars < people:
#     print("We should not take the cars.")
# else:
#     print("We can't decide.")
#
# if trucks > cars:
#     print("That's too many trucks")
# elif trucks < cars:
#     print("Maybe we could take the trucks")
# else:
#     print("We still can't decide.")
#
# if people > trucks:
#     print("Alright, let's just take the truck")
# else:
#     print("Fine, let's stay home then.")

# print("""YOU ENTER a dark room with two doors, Do you go through door1 or door2""")
# door = input(">>><>>")
# if door == "1":
#     print("There's a giant bear here eating a cheese cake.")
#     print("What do you do.")
#     print("1.take the cake.")
#     print("2.scream at the bear.")
#
#     bear = input(">><<")
#     if bear == "1":
#         print("The bear eats your face off. Good job.")
#     elif bear == "2":
#         print("The bear eats your legs off. Good job.")
#     else:
#         print(f"Well, doing {bear} if probably better.")
#         print("Bear runs away.")
# elif door == "2":
#     print("You stare into the endless abyss at Cthulhu's retina.")
#     print("1.Blueberries.")
#     print("2.yellow jacket clothespins.")
#     print("3.Understanding revolvers yelling melodies.")
#
#     insanity = input(">>>>>>")
#     if insanity == "1" or insanity == "2":
#         print("Your body survives powered by a mind of jello.")
#         print("Good job")
#     else:
#         print("The insanity rots your eyes into a pool of muck.")
#         print("Good job")
# else:
#     print("You stumble around and fall on a knife and die. Good job.")
# the_count=[1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for numbers in the_count:
#     print(f"This is count {numbers}")

# for fruit in fruits:
#     print(f"A fruit of type: {fruit}")

# for i in change:
#     print(f"I got {i}")

# elements = []

# for i in range(0, 6):
#     print(f"Adding {i} to the list.")
#     elements.append(i)

# for i in elements:
#     print(f"Element was: {i}")
# the_count = [1, 2, 3, 4, 5]
# fruits = ['apple', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for number in the_count:
#     print(f"This is count {number}.")

# for fruit in fruits:
#     print(f"A fruit of type: {fruit}")

# for i in change:
#     print(f"I got {i}")

# elements = []

# for i in range(0, 16):
#     print(f"Adding {i} to the list.")
#     elements.append(i)

# for i in elements:
#     print(f"Element was :{i}")

# i = 0
# numbers = []
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i += 1
#     print("Numbers now:", numbers)
#     print(f"At the bottom i is {i}")

# print("The numbers: ")
# for num in numbers:
#     print(num)

# from sys import exit

# def gold_room():
#     print("This room is full of gold. How much do you take.")

#     choice = input(">><>>>")
#     if "0" in choice or "1" in choice:
#         how_much = int(choice)
#     else:
#         dead("Man, learn to type a number.")

#         if how_much < 50:
#             print("Nice, you're not greedy, you win.")
#             exit(0)
#         else:
#             dead("You're brave.")

# def bear_room():
#     print("There is a bear here.")
#     print("The bear has a bunch of honey")
#     print("The fat bear is in front of another door.")
#     print("How are you going to move the bear")
#     bear_moved = False

#     while True:
#         choice = input(">>>")
#         if choice == "Take honey":
#             dead("The bear looks at you then slaps your face off.")
#         elif choice == "taunt bear" and not bear_moved:
#             print("The bear has moved from the door.")
#             print("You can go through it now.")
#             bear_moved = True
#         elif choice == "taunt bear" and bear_moved:
#             dead("The bear gets pissed off and chews your leg off.")
#         elif choice == "open door" and bear_moved:
#             gold_room()
#         else:
#             print("I got no idea what that means.")

# def Cthulhu_room():
#     print("Here you see the great evil Cthulhu.")
#     print("He, it, whatever stares at you and you go insane.")
#     print("Do you flee for your life or eat your head.")

#     choice = input(">>>")
#     if "flee" in choice:
#         start()
#     elif "head" in choice:
#         dead("WELL THAT WAS TASTY")
#     else:
#         Cthulhu_room()

# def dead(why):
#     print(why, "Good job.")
#     exit(0)

# def start():
#     print("You are in a dark room.")
#     print("There is a door to your right and left.")
#     print("WHICH one do you take")

#     choice = input("??")
#     if choice == "left":
#         bear_room()
#     elif choice == "right":
#         Cthulhu_room()
#     else:
#         dead("You stumble around the room until you starve.")

# start()、

# ten_things = "Apple Oranges Crows Telephone Light Sugar"

# print("Wait there are not 10 things that list. Let's fix that")

# stuff = ten_things.split(" ")
# more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print("Adding：", next_one)
#     stuff.append(next_one)
#     print(f"There are {len(stuff)} items now.")

# print("There we go: ", stuff)
# print("Let's do some things with stuff.")
# print(stuff[1])
# print(stuff[-1])
# print(stuff.pop())
# print(' '.join(stuff))
# print('#'.join(stuff[3:5]))

# stuff = {'name':'Ted', "age":35, "height":6*14+2}
# print(stuff['name'])
# print(stuff['age'])
# print(stuff['height'])
# stuff['city'] = 'LA'
# print(stuff['city'])

# states = {
#     'Oregon':'OR',
#     'Florida':'FL',
#     'California':'CA',
#     'New York':'NY',
#     'Michigan':'MI'
# }

# cities = {
#     'CA':'San Francisco',
#     'MI':'Detroit',
#     'FL':'Jacksonville'
# }

# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'
# print('-'*10)
# print("Michigan's abbreviation is: ", states['Michigan'])
# print("Florida's abreviation is: ", states['Florida'])

# print('-'*10)
# print("Michigan has:", cities[states['Michigan']])
# print("Florida has: ", cities[states["Florida"]])

# print('-'*10)
# for state, abbrev in list(states.items()):
#     print(f"{state} is abbreviated {abbrev}")

# print('-'*10)

# for abbrev, city in list(cities.items()):
#     print(f"{abbrev} has the city {city}")

# print('-'*10)
# for state, abbrev in list(states.items()):
#     print(f"{state} state is abbreviated {abbrev}")
#     print(f"and has city {cities[abbrev]}")

# print('-'*10)
# state = states.get('Texas')

# if not state:
#     print("Sorry, not Texas.")

# city = cities.get("TX", "Does not exist.")
# print(f"The city for state 'TX' is :{city}")

# mystuff = {'apple' : "I AM APPLES!"}
# print(mystuff['apple'])

