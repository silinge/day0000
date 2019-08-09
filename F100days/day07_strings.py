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