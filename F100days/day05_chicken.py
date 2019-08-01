# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             # print('公鸡：%d只， 母鸡：%d只，小鸡：%d只'%(x, y, z))
#             print(f"公鸡{x}只，母鸡{y}只，小鸡{z}只。")
# 100元100只鸡 公鸡五元 母鸡三元 小鸡3只一元

# craps game
"""
player rolls two dices when get 7 or 11 at 1st time, player wins, on 2 3 12  banker wins, otherwise
game on, player rolls again, when get 7, banker wins, if it is the same with the 1st time, player wins,

otherwise roll again. the player lost 1000 debt means game over
"""

# from random import randint
#
# money = 1000
#
# while money > 0:
#     print(f"You have {money} in total.")
#     while True:
#         debt = int(input("Put bet: "))
#         if debt > 0 and debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print(f"player rolls {first} point at first time.")
#     if first == 7 or first == 11:
#         print("Player wins!")
#         money += debt
#     elif first == 2 or first ==3 or first == 12:
#         print("Banker wins!")
#         money -= debt
#     else:
#         needs_go_on = True
#
#
#     while needs_go_on:
#         current = randint(1, 6) + randint(1, 6)
#         print(f"Player rolls {current} points.")
#         if current == 7:
#             print("banker wins")
#             money -= debt
#             needs_go_on = False
#         elif current == first:
#             print("player wins")
#             money += debt
#             needs_go_on = False
#
# print("Game over.")

# Fibonacci sequence 20

# a = 0
# b = 1
#
# for _ in range(20):
#     (a, b) = (b, a + b)
#     print(a, end= ' ')
# _ 表示临时变量

# import random
#
# answer = random.randint(1, 100)
# counter = 0
#
# while True:
#     counter += 1
#     number = int(input("Enter a number: "))
#     if number < answer:
#         print("put bigger one.")
#     elif number > answer:
#         print("put smaller one.")
#     else:
#         print("congratulations.")
#         break
# print(f"You guess {counter} times in total.")
# if counter > 7:
#     print("Pay attention to you IQ")

# 找出100-999之间的所有水仙花数
# 水仙花数是各位数的立方之和正好等于该数本身，如 153 = 1^3 + 5^3 + 3^3

# for i in range(100, 1000):
#     x_100 = i//100
#     x_10 = i//10%10 # 提取十位数 除以10的整数 再除以10的余数
#     x = i % 10 #个位数 是除以10的余数
#     if i == x_100**3 + x_10**3 + x**3:
#         print(i)

# num = int(input("输入一个正整数： "))
#
# temp = num
#
# num2 = 0
# while temp > 0:
#     num2 *= 10
#     num2 += temp %10
#     temp //=10
# if num == num2:
#     print(f"{num}是回文数。")
# else:
#     print(f"{num}不是回文数。")

#完美数，除了自身外所有因子数的和正好等于这个数的本身
# exp 6 = 1+2+3 28 = 1+2+4+7+14
# time.clock() 过于陈旧将会被弃用
import time
import math

# start = time.clock()
# start = time.perf_counter()
# for num in range(1, 10000):
#     sum = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             sum += factor
#             if factor > 1 and num/factor != factor:
#                 sum += num/factor
#     if sum == num:
#         print(num)
#
# # end = time.clock()
# end = time.perf_counter()
# print("执行时间：", (end), "秒")

#素数
# import math
#
# for num in range(2, 100):
#     is_prime = True
#     for factor in range(2, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=' ')

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{i}*{j}={i*j}", end="\t")
#         # print()
#     print()